""" Tests for the `fileio` module 
"""

import csv
import pathlib
import pytest  
import json 
from module_two.schemas import FakeEnergyFacilityModel
from module_two.fileio import JsonReader, JsonWriter, CsvWriter


def test_JsonWriter(tmp_path,list_of_inst_models, records): # tmp_path is a fixture provided by pytest 
    writer_interface = JsonWriter()
    tmp_dir_path = tmp_path / 'sub'
    tmp_dir_path.mkdir()
    tmp_file_path = tmp_dir_path / 'test_jsonwriter.json'
    writer_interface.write(list_of_inst_models,tmp_file_path)
    assert json.load(open(tmp_file_path,'r')) == records 


def test_JsonReader(tmp_path,records,list_of_inst_models):
    reader_interface = JsonReader()
    tmp_dir_path = tmp_path / 'sub' 
    tmp_dir_path.mkdir()
    tmp_file_path = tmp_dir_path / 'data_records.json'
    json_obj = json.dumps(records)
    tmp_file_path.write_text(json_obj)
    inst_models = reader_interface.read(tmp_file_path,FakeEnergyFacilityModel)
    assert inst_models == list_of_inst_models 


def test_CsvWriter(tmp_path,list_of_flat_models, flatten_records_by_csvwriter):
    tmp_dir_path = tmp_path / 'sub' 
    tmp_dir_path.mkdir()
    tmp_file_path = tmp_dir_path / 'test_csvwriter.csv'
    CsvWriter().write(list_of_flat_models,tmp_file_path)
    reader = csv.DictReader(open(tmp_file_path,'r'))
    assert pathlib.Path.exists(tmp_file_path) is True 
    assert [dict_obj for dict_obj in reader] == flatten_records_by_csvwriter