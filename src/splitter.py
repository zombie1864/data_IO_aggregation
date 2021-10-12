import os 
import pathlib
from fileio import JsonReader
from schemas import FakeEnergyFacilityModel 
from utils_data_manipulation import categorize, list_of_agencies_in
from utils_IO_bound import splitter


this_dir = os.path.dirname(os.path.realpath(__file__))  
parent_dir = pathlib.Path(this_dir).parent
json_filepath = pathlib.Path(parent_dir) / 'data' / 'fake-energy-data-min.json'
dir_filepath = pathlib.Path(this_dir) / 'project_data' / 'splitter'


def main():
    list_of_inst_models = JsonReader().read(json_filepath, FakeEnergyFacilityModel)
    list_of_states = ['NY','NJ','PA']
    categorized_dataset = categorize(list_of_inst_models,'address',list_of_states) 
    list_of_agencies = list_of_agencies_in(list_of_inst_models)
    dir_filepath = pathlib.Path(this_dir) / 'project_data' / 'splitter'
    if not dir_filepath.exists():
        dir_filepath.mkdir()
    splitter('json', categorized_dataset, list_of_agencies, dir_filepath)


if __name__ == '__main__': 
    main() 
