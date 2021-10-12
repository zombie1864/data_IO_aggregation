'''  
This application should take as an argument a facility_id and as an optional argument the base_url with the default of `http://localhost:8080`. It will 
simply reach out to the API and print the result to stdout using `click.echo`. A user should be able to pipe the output to a correctly formmatted json 
file using bash whether the request succeeds or not.
'''

import os 
import click 
from http_file import fetch 
from utils_data_manipulation import pydantic_converter_of
from schemas import FakeEnergyFacilityModel

this_dir = os.path.dirname(os.path.realpath(__file__))  


def fetch_one(facility_id:str, base_url:str) -> None:
    ''' makes api call to fetch a single record user can pipe to file
        Args:
            facility_id: user inputs facility id number 
            base_url: optional base url with default 
        Returns:
            None
    '''
    try:
        _, data_obj = fetch(f'{base_url}/data/{facility_id}')#response is tuple
        data_obj.pop('_id')
        list_of_single_model = pydantic_converter_of([data_obj], FakeEnergyFacilityModel)
        click.echo(list_of_single_model[0].json())
    except Exception: #NOTE find an exception from requests 
        click.echo('http error, please check url') #NOTE echoing the msg from Exception is better 
    

url = 'http://localhost:8080'
@click.command() 
@click.argument('facility_id') 
@click.option('--base_url', '-url', default=url, help='URL address to API')  
def main(facility_id, base_url):
    ''' A CLI that fetches a single record from an backend API server via facility_id '''
    fetch_one(facility_id,base_url)


if __name__ == '__main__':
    main()

