'''  
Write a script that uses the same business logic in `api_splitter.py` to build the datasets and subdirectories except write csv files instead of json. Use the same specifications for each csv file as outlined in `flatten.py`. 
'''

import os 
import pathlib 
from schemas import FakeEnergyFacilityModel, FlattenFakeEnergyFacilityModel
from utils_data_manipulation import fetch_data, list_of_agencies_in, pydantic_converter_of, flatten, sort, categorize
from utils_IO_bound import api_splitter
from itertools import chain


this_dir = os.path.dirname(os.path.realpath(__file__))  


def main():
    dir_filepath = pathlib.Path(this_dir) / 'project_data' / 'api_flatten_splitter'
    list_of_states, sqft_gte_param = ['NY','NJ'], 30000
    url = 'http://localhost:8080' + '/data/'
    list_of_datasets = [fetch_data(url, address_contains=state, sqft_gte=sqft_gte_param) for state in list_of_states]
    dataset = list(chain.from_iterable(list_of_datasets))
    list_of_inst_models = pydantic_converter_of(dataset, FakeEnergyFacilityModel)
    list_of_agencies = list_of_agencies_in(list_of_inst_models)
    list_of_flat_models = flatten(list_of_inst_models,FlattenFakeEnergyFacilityModel)
    list_of_sorted_models = sort(list_of_flat_models, 'facility_id','energy_type','timestamp','agency')
    categorized_dataset = categorize(list_of_sorted_models, 'address', list_of_states) 
    if not dir_filepath.exists():
        dir_filepath.mkdir()
    api_splitter('csv', list_of_agencies, categorized_dataset, dir_filepath) 


if __name__ == '__main__': 
    main() 

