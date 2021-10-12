import itertools
import pydantic
from typing import Any, Dict, List, Type, TypeVar
from http_file import paginator
from itertools import chain

TPydanticModel = TypeVar('TPydanticModel', bound=pydantic.BaseModel)


''' flattening related methods '''


def sort(dataset: List[TPydanticModel], *organizor) -> List[TPydanticModel]:
    '''  sorts a list of pydantic models according to the organizor 
        Args:
            dataset: list of pydantic models 
            organizor: tuple of string arguments 
        Returns:
            sorted_data: list of pydantic models ascending in the order of the organizor 
    '''
    sorted_data = sorted(dataset,key = lambda model_obj: tuple(getattr(model_obj, str_arg) for str_arg in organizor) )
    return sorted_data


def _keys_in(nested_data_piece:List[TPydanticModel]) -> List[str]:
    ''' returns a list of unique keys found in the nested_data_piece 
        Args: 
            nested_data_piece: nested value of a dict 
        Returns:
            a list of unique strs 
    '''
    return list(set(key for model in nested_data_piece for key in model.dict().keys()))


def _find_name_of_nested_data_piece_in(dict_obj:Dict[str,Any]) -> str:
    ''' returns the key for a nested value 
        Args:
            dict_obj: py dict 
        Returns:
            key: string key 
    '''
    for key, value in dict_obj.items():
        if isinstance(value, list):
            return key 


def flatten(dataset:List[TPydanticModel],schema:Type[TPydanticModel]) -> List[TPydanticModel]:
    ''' flattens a dataset and uses schema to validate datatypes
        returns a flatten dataset 
        Args: 
            dataset: list of pydantic models  
            schema: pydantic class model 
        Returns:
            flatten_dataset: list of flatten pydantic models 
    '''
    flatten_dataset = []
    name_of_key = _find_name_of_nested_data_piece_in(dataset[0].dict())
    for model_obj in dataset:#iterate thr dataset 
        flat_model_obj = {}#flat model_obj 
        nested_data_piece = getattr(model_obj, name_of_key).copy()#[{},...,{}] List DS 
        list_of_keys = _keys_in(nested_data_piece) 
        for i in range(len(nested_data_piece)):#len of energy_records [{},...,{}]
            flat_model_obj = model_obj.dict().copy() # copy of model_obj 
            for key in list_of_keys:
                flat_model_obj[key] = getattr(nested_data_piece[i],key)
            validated_flat_model_obj = schema(**flat_model_obj)
            flatten_dataset.append(validated_flat_model_obj)
            flat_model_obj = {}
    return flatten_dataset


''' splitting related methods '''


def list_of_agencies_in(list_of_inst_models:List[TPydanticModel]) -> List[TPydanticModel]:
    ''' iterates through a list of pydantic models and returns a unique list of agencies found in the dataset 
        Args:
            list_of_inst_models: list of pydantic models 
        Returns:
            list_of_agencies: a list of TPydanticModel with unique agency names found in dataset 
    '''
    return list(set(model_obj.agency for model_obj in list_of_inst_models))



def categorize(list_of_inst_models:List[TPydanticModel], key_matcher:str, list_of_items:List[str]) -> Dict[str, List[TPydanticModel]]: 
    ''' categorizes the list_of_inst_models into a dict has a value according to each item, acting as a key, in the list_of_items
        Args:
            list_of_inst_models: list of pydantic models 
            key_matcher: string by which to obtain pydantic field attribute 
            list_of_items: a list of items to categorize dataset by 
        Returns:
            categorized_dataset: dict obj with key matching item in list and value containing list of pydantic models matching key value 
    '''
    categorized_dataset = {}
    for item in list_of_items: 
        categorized_dataset[f'{item}_dataset'] = []
        for model_obj in list_of_inst_models: 
            if item in getattr(model_obj,key_matcher): # ~ model_obj.address 
                categorized_dataset[f'{item}_dataset'].append(model_obj)
    return categorized_dataset


''' api_splitting related methods '''

def fetch_data(url, **kwarg:Any) -> List[Dict]:
    ''' makes API call according to args, if none makes API call with no query str 
        Args:
            kwarg: key word args 
        Returns:
            list of python dict, a dataset [{},..,{}]
    '''
    list_of_datasets = []
    for _, data in paginator(url, **kwarg):
        records = data['records']
        _remove_from(records, '_id')
        list_of_datasets.append(records)
    return list(chain.from_iterable(list_of_datasets))


def pydantic_converter_of(dataset:List[Dict],schema:Type[TPydanticModel]) -> List[TPydanticModel]:
    ''' converts a list of python dict into a list of pydantic model 
        Args:
            dataset: list of python dict 
            schema: pydantic model class 
        Returns:
            list of pydantic models 
    '''
    return [schema(**{key: value for key, value in dict_obj.items()}) for dict_obj in dataset]


def _remove_from(dataset:List[Dict], *entries:str) -> None:
    ''' removes from a python dict an entry 
        Args:
            dataset: list of python dict 
            entries: key args you wish to rm 
        Returns:
            None - method mutates list of dict 
    '''
    for data_obj in dataset:
        for entry in entries:
            data_obj.pop(entry)



''' summary related methods '''

def summarize(dataset:List[Dict]) -> List[Dict]:
    ''' converts a list of records, in similar structure to server API endpoint, into a list of summarized records 
        Args:
            dataset: list of python dict 
        Returns:
            dataset: list of summarized dict 
    '''
    _remove_from(dataset,'name', 'address', 'longitude', 'latitude')
    for data_obj in dataset:
        sorted_energy_records = sorted(data_obj['energy_records'],key=lambda data_obj:(data_obj['energy_type'], data_obj['timestamp']) )
        data_obj['energy_records'] = sorted_energy_records
        summarized_dataset = _summarize_energy_records(data_obj)
        data_obj['summary'] = summarized_dataset
    _round(dataset)
    return dataset 


def _summarize_energy_records(data_obj:Dict) -> List[Dict]: 
    ''' takes an object containing an energy_records entry, removes it and summarizes for each year per energy type
        Args:
            dataset: list of python dict 
        Returns:
            list_of_summarized_energy_records 
    '''
    removed_energy_records = data_obj.pop('energy_records')#rm [{},...,{}]
    grouped_energy_record = itertools.groupby(removed_energy_records, key=lambda energy_record: (energy_record['energy_type'], energy_record['timestamp'][:4]))  
    list_of_summarized_energy_records = []
    for (energy_type, year), grp in grouped_energy_record:
        list_of_usage_records = [record_obj['usage'] for record_obj in list(grp)]
        sum_obj = {
            'year': int(year),
            'energy_type': energy_type,
            'num_records': len(list_of_usage_records),
            'average_usage_per_sqft': (sum(list_of_usage_records) / len(list_of_usage_records))/ data_obj['sqft'] 
        }
        list_of_summarized_energy_records.append(sum_obj)
    return list_of_summarized_energy_records


def _round(dataset:List[Dict]) -> None:
    ''' rounds the avergae_usgae_per_sqft to 4 significant figures 
        Args:
            dataset: list of python dict 
        Returns:
            None -> mutates dataset 
    '''
    for data_obj in dataset:
        for summary_obj in data_obj['summary']:
            summary_obj['average_usage_per_sqft'] = round(summary_obj['average_usage_per_sqft'], 4)

