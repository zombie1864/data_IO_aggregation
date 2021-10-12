import pytest 
from module_two.utils_data_manipulation import summarize

def test_summarize(records, summarized_dataset):
    assert summarize(records) == summarized_dataset

def test_summarize_for_empty_energy_records():
    empty_e_records = [
        {
            'facility_id':1,
            'name':'builing_1',
            'address':'neon dreams ave, Miami, FL, 9000',
            'longitude':27.07,
            'latitude':27.07,
            'agency':'A',
            'sqft':45000,
            'energy_records':[]
        }
    ]
    assert summarize(empty_e_records) == [{
            'facility_id':1,
            'agency':'A',
            'sqft':45000,
            'summary':[]
    }]