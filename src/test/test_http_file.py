""" Tests for the `http` module 
"""

from typing import Generator
import requests
import pytest  
import requests 
import requests_mock 
from unittest import mock
from module_two.http_file import fetch, paginator


def test_fetch(mock_api_resp):
    with requests_mock.Mocker() as mocker:
        url = 'http://localhost:8080'
        mocker.get(url,json=mock_api_resp)#mocking api resp 
        resp_obj = requests.get(url)#calling api & gets mock_api_resp mock_obj 
        fetch_resp = fetch(url)#calling api & gets mock_api_resp 
        assert resp_obj.json()['records'] == fetch_resp[1]['records']
        assert resp_obj.status_code == 200 
        assert mocker.called 


def test_fetch_by_(mock_api_query_resp):
    with requests_mock.Mocker() as mocker:
        url_by_query = 'http://localhost:8080/data/?sqft_gte=99000'
        mocker.get(url_by_query,json=mock_api_query_resp)
        resp_obj = requests.get(url_by_query)
        fetch_resp = fetch(url_by_query)
        assert resp_obj.json()['records'] == fetch_resp[1]['records']
        

def test_fetch_404(): 
    mock_response = mock.Mock(status_code=404) # mocking the response  
    mock_request_get = mock.Mock(return_value=mock_response) #mocking api call
    requests.get = mock_request_get # assigning this to be mock
    url = 'http://localhost:8080/abc'
    result = (mock_response.status_code, mock_response.json() )
    print( 'mock_response.json()',mock_response.json() )
    assert fetch(url) == result



def test_paginator(mock_api_resp):
    with requests_mock.Mocker() as mocker:
        url = 'http://localhost:8080'
        mocker.get(url,json=mock_api_resp)
        paginator_resp = paginator(url)
        assert isinstance(paginator_resp,Generator) is True 


def test_paginator_breaks_on_none():
    responses = [
        (200, { 'next': "url1" }), 
        (200, {'next': "url2"}), 
        (200, {'next': None})
    ]
    url = 'http://localhost:8080'
    with mock.patch('module_two.http_file.fetch', side_effect=responses) as mock_req:
        for status, _ in paginator(url):
            assert status == 200 
        assert mock_req.call_count == 3