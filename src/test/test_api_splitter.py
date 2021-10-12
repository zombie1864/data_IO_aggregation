import json 
import pytest 
import requests 
import requests_mock 
from module_two.utils_data_manipulation import fetch_data 


def test_fetch_data():
    with requests_mock.Mocker() as mocker:
        url = 'http://example.com'
        json_resp = {
            'count': 1,
            'next': None, 
            'prev': None, 
            'records': [{'_id':'123', 'energy_type': 'Elec', 'usage': 200 }]
        }
        mocker.get(url,json=json_resp)
        dataset = fetch_data(url)
        assert dataset == [{'energy_type': 'Elec', 'usage': 200 }]


def test_fetch_data_with_kwarg():
    with requests_mock.Mocker() as mocker:
        url = 'http://example.com'
        json_resp = {
            'count': 2,
            'next': None, 
            'prev': None, 
            'records': [
                {'_id':'123', 'sqft': 100, 'total_usgae': 2000 },
                {'_id':'345', 'sqft': 100, 'total_usgae': 4000 },
            ]
        }
        mocker.get(url + '?sqft_gte=100', json=json_resp)
        dataset = fetch_data('http://example.com', sqft_gte=100)
        assert dataset == [{'sqft': 100, 'total_usgae': 2000 },{'sqft': 100, 'total_usgae': 4000 }]
