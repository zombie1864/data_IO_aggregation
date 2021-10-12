'''  
This application should take: 
 * optional argument base_url with the default of `http://localhost:8080`. 
 * A single positional argument that specifies the agency 
 * an optional argument `directory` that resolves relative to a directory. The default should be '.' (the current directory). If using a non default directory you should assure whether this exists or not and error out if it does not with a meaningful message. 
 * an optional argument specifying the type of file to write to. The choices are 'json' and 'csv', with the default being json.

 The application should query the API by the given agency. It should create the schema described in `summary.py` and write either a json file or a flattened csv to the filepath called `<agency>-portfolio.<fmt>` with the same specifications as outlined in `summary.py`.
'''

import os 
import copy 
import click 
import pathlib
from utils_data_manipulation import fetch_data, summarize, pydantic_converter_of, flatten, list_of_agencies_in, sort, categorize
from utils_IO_bound import summary_splitter
from schemas import SummaryFakeEnergyFacilityModel, FlattenSummaryFakeEnergyFacilityModel

this_dir = os.path.dirname(os.path.realpath(__file__))  


def portfolio(agency, base_url, directory, file_type):
    url = base_url + '/data/'
    if not os.path.isdir(directory):
        return click.echo('The following directory does not exist, please refer to the help document for more information')
    directory_path = pathlib.Path(directory)
    dataset = fetch_data(url,agency=agency)
    summarized_dataset = summarize(copy.deepcopy(dataset))
    list_of_summary_models = pydantic_converter_of(summarized_dataset, SummaryFakeEnergyFacilityModel)
    list_of_flatten_models = flatten(list_of_summary_models, FlattenSummaryFakeEnergyFacilityModel)
    list_of_agencies = list_of_agencies_in(list_of_summary_models)
    if file_type == 'json':
        list_of_sorted_sum_data = sort(list_of_summary_models, 'facility_id')
        categorized_sum_dataset = categorize(list_of_sorted_sum_data,'agency',list_of_agencies)
        summary_splitter('json', 'portfolio', categorized_sum_dataset, directory_path, list_of_agencies)
    elif file_type == 'csv':
        list_of_sorted_flat_data = sort(list_of_flatten_models, 'facility_id', 'energy_type', 'year')
        categorized_flat_dataset = categorize(list_of_sorted_flat_data,'agency',list_of_agencies)
        summary_splitter('csv', 'portfolio', categorized_flat_dataset, directory_path, list_of_agencies) 


url = 'http://localhost:8080'
@click.command()  
@click.argument('agency')    
@click.option('--base_url', '-url', default=url, help='URL address to API')  
@click.option('--directory', '-dir', default=this_dir, help='directory path. For nested directory please specify the path. Example dir_A/sub_dir_a01')  
@click.option('--file_type', '-f', default='json', help='json or csv')  
def main(agency, base_url, directory, file_type):
    ''' A CLI that fetches via API call, a portfolio summary record a given agency. The portfolio output can be either json or csv with default to json'''
    portfolio(agency, base_url, directory, file_type)


if __name__ == '__main__': 
    main()
