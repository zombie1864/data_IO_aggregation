'''  
Write a script that uses the API running on `localhost:8080` to build out datasets with a similar specification as `splitter.py`. Only consume data from the API that are from NY and NJ and have a sqft greater than or equal to 30000 to build your datasets. The directory specifications should be the same as in `splitter.py`.
'''

import os 
import pathlib
from utils_data_manipulation import fetch_data, pydantic_converter_of, sort, list_of_agencies_in, categorize
from utils_IO_bound import api_splitter
from schemas import FakeEnergyFacilityModel
from itertools import chain

this_dir = os.path.dirname(os.path.realpath(__file__)) 


def main():
    dir_filepath = pathlib.Path(this_dir) / 'project_data' / 'api_splitter'
    list_of_states, sqft_gte_param = ['NY','NJ'], 30000
    url = 'http://localhost:8080' + '/data/'
    list_of_datasets = [fetch_data(url, address_contains=state, sqft_gte=sqft_gte_param) for state in list_of_states]
    dataset = list(chain.from_iterable(list_of_datasets))
    list_of_inst_models = pydantic_converter_of(dataset, FakeEnergyFacilityModel)
    list_of_sorted_inst_models = sort(list_of_inst_models, 'facility_id')
    list_of_agencies = list_of_agencies_in(list_of_sorted_inst_models)
    categorized_dataset = categorize(list_of_sorted_inst_models, 'address', list_of_states) 
    if not dir_filepath.exists():
        dir_filepath.mkdir()
    api_splitter('json', list_of_agencies, categorized_dataset, dir_filepath) 


if __name__ == '__main__': 
    main() 
