'''  
This application should take an optional argument base_url with the default of `http://localhost:8080`. You should use a multi-value option to allow for filtering 
by key value pairs. For example: 
```
$ python fetch_many.py -o agency=myagency -o sqft_gte=42000
```
Like fetch_one we will print the result to stdout using `click.echo` and the user should be able to pipe the output to a correctly formatted json file. 
'''

import os
from typing import Any 
import click 
import json 
from utils_data_manipulation import fetch_data, pydantic_converter_of
from schemas import FakeEnergyFacilityModel
this_dir = os.path.dirname(os.path.realpath(__file__))


def fetch_many(keyword:Any, base_url:str) -> None:
    ''' CLI which makes API call according to query params, stdout result and converts result into list of pydantic models
        Args:
            keyword: -kw inputs from user 
            base_url: basic url string 
        Returns:
            None 
    '''
    try:
        kw_dict = {}
        for kw in keyword: #itr thr tuple 
            splitted = kw.split('=') # split str on = 
            kw_dict[splitted[0]] = splitted[1] # assign to dict 
        dataset = fetch_data(base_url, **kw_dict)
        list_of_inst_models = pydantic_converter_of(dataset, FakeEnergyFacilityModel)
        dataset = [json.loads(model_obj.json()) for model_obj in list_of_inst_models]
        click.echo(json.dumps(dataset))
    except Exception: # NOTE think more abt that 
        click.echo('http error, please check url')


url = 'http://localhost:8080' + '/data/'
@click.command()  
@click.option('--keyword','-kw',help='URL address to API',multiple=True)
@click.option('--base_url','-url',default=url,help='URL address to API')
def main(keyword, base_url):
    ''' a CLI that fetches a single record filtered by keyword argument '''
    fetch_many(keyword,base_url)



if __name__ == '__main__':
    main()
