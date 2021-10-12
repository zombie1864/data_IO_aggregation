''' 
Write a script that reads in `fake-energy-data-min.json` from the root `data` directory and flattens it to a csv named `flat.csv` based on the specifications outlined in `schemas.py`. The records in the resulting csv file should be sorted ascending in the following order: `facility_id`, `agency`, 'energy_type` and `timestamp. The script should create the directory `flatten/` in the project_data folder and write the csv file to that folder.
'''


import os
import pydantic
from fileio import JsonReader, CsvWriter
from schemas import FakeEnergyFacilityModel, FlattenFakeEnergyFacilityModel
from utils_data_manipulation import flatten, sort
import pathlib 

this_dir = os.path.dirname(os.path.realpath(__file__))  
parent_dir = pathlib.Path(this_dir).parent
json_filepath = pathlib.Path(parent_dir) / 'data' / 'fake-energy-data-min.json'
flatten_dir_filepath = pathlib.Path(this_dir) / 'project_data' / 'flatten'
csv_filepath = pathlib.Path(this_dir) / 'project_data' / 'flatten' / 'flat.csv'


def main():
    if not flatten_dir_filepath.exists():
        flatten_dir_filepath.mkdir()
    list_of_inst_models = JsonReader().read(json_filepath,FakeEnergyFacilityModel) 
    list_of_flatten_models = flatten(list_of_inst_models,FlattenFakeEnergyFacilityModel) 
    sorted_data = sort(list_of_flatten_models, 'facility_id','energy_type','timestamp','agency')
    CsvWriter().write(sorted_data,csv_filepath) 


if __name__ == '__main__': 
    main()