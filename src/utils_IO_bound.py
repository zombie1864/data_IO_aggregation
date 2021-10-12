from fileio import JsonWriter, CsvWriter
import pydantic
import pathlib
from typing import Any, Dict, List, TypeVar

TPydanticModel = TypeVar('TPydanticModel', bound=pydantic.BaseModel)


def _writer_interface(mode:str) -> TPydanticModel:
    ''' an interface that returns a pydantic model class based on str input
        Args:
            mode: a string specifiying the file type 
        Returns:
            pydantic model class 
    '''
    interface_dict = {'csv':CsvWriter(),'json':JsonWriter()}
    return interface_dict[mode]


def splitter(file_type:str, categorized_dataset:Dict[str,Any], list_of_agencies:List[TPydanticModel], dir_filepath:pathlib.Path) -> None:
    ''' wrapper function that wraps the business logic for splitting data
        Args:
            file_type: file type for which the data will be formated into 
            list_of_stats: list containing states that will be used to organize the dataset into
            list_of_inst_models: list of pydantic models 
            dir_filepath: file path 
        Returns:
            None
    '''
    _make_dir_for_each_in(list_of_agencies,dir_filepath)
    _make_file_for_each_cat_in(categorized_dataset,dir_filepath,list_of_agencies,file_type)


def _make_dir_for_each_in(list_of_agencies:List[TPydanticModel], dir:pathlib.Path) -> None: 
    ''' provided with a list of agencies in the form of Enums, creates dir 
        Args:
            list_of_agencies: list of enums models 
            dir: a valid path to create the dir 
        Returns:
            None 
    '''
    for agency in list_of_agencies: #creates dir 
        dir_name = f'agency{agency}'
        dir_filepath = dir / dir_name
        if not dir_filepath.exists():
            dir_filepath.mkdir()


def _make_file_for_each_cat_in(categorized_dataset:Dict[str, List[TPydanticModel]], dir:pathlib.Path, list_of_agencies: List[TPydanticModel],file_type: str) -> None: 
    ''' creates file for each category in the categorized_dataset according to file_type and sorts according to facility_id
        Args:
            categorized_dataset: a dict containing categorized datasets 
            dir: filepath to make file 
            list_of_agencies: list of pydantic agency enums 
            file_type: a string indicating file type 
        Returns:
            None 
    '''
    interface = _writer_interface(file_type)
    for name in list_of_agencies: 
        for str_desc,categorized_list in categorized_dataset.items(): 
            file_name = f'agency{name}-{str_desc}.{file_type}' 
            file_path = dir / f'agency{name}' / file_name 
            dataset = [model_obj for model_obj in categorized_list if model_obj.agency == name]
            interface.write(dataset,file_path)


def _make_file_for_each_sum_cat_in_(file_ext, categorized_dataset,dir,file_type):
    interface = _writer_interface(file_type)
    for str_desc, categorized_list in categorized_dataset.items():
        file_name = f'agency{str_desc[0]}-{file_ext}.{file_type}'
        file_path = dir / f'agency{str_desc[0]}' / file_name 
        interface.write(categorized_list,file_path)


def summary_splitter(file_type:str, file_ext:str ,categorized_dataset:Dict[str,Any], dir_filepath:pathlib.Path, list_of_agencies:List[TPydanticModel]) -> None:
    ''' wrapper function containing summary splitter business logic 
        Args:
            file_type: the file type 
            file_ext: file extension name 
            categorized_dataset: a dict containing categorized dataset 
            dir_filepath: file path 
            list_of_agencies: list of pydantic enum models 
        Returns:
            None 
    '''
    _make_dir_for_each_in(list_of_agencies,dir_filepath)
    _make_file_for_each_sum_cat_in_(file_ext, categorized_dataset,dir_filepath, file_type)


def api_splitter(file_type:str, list_of_agencies:List[TPydanticModel], categorized_dataset:Dict[str,Any], dir_filepath:pathlib.Path) -> None:
    ''' takes each entry in the categorized_dataset, creates a dir for each agency found and a file for each agency according to the file_type 
        Args:
            file_type: str that specifies the file type 
            list_of_agencies: list of pydantic enum agency names 
            categorized_dataset: a categorized_dataset for each value to be put into a file 
            dir_filepath: dir path to store results in 
        Returns:
            None 
    '''
    _make_dir_for_each_in(list_of_agencies,dir_filepath)
    _make_file_for_each_cat_in(categorized_dataset,dir_filepath,list_of_agencies,file_type)

