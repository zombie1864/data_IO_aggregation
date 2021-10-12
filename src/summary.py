'''  
Write a script that uses the API running on `localhost:8080`. Create a subdirectory called `summary/` in the project_data folder. For each facility in the database we will create an energy summary for _each year_ worth of data per energy type. We will use the following schema to model our output: 
```
    {
        facility_id: int  
        agency: str
        sqft: int
        summary: [
            {
                year: int 
                energy_type: str
                num_records: int
                average_usage_per_sqft: float  
            }, 
            ... 
        ]
    }
```
Create a flattened version of this schema with the following column headers: facility_id, agency, sqft, year, energy_type, num_records, unit, average_usage_per_sqft. 

For each agency write both a json file and csv with the format `<agency>-summary.<fmt>`. The json files should be sorted ascending by facility_id. The csv files should be sorted ascending by facility_id, energy_type and year. 
'''


import os 
import copy 
import pathlib 
from schemas import SummaryFakeEnergyFacilityModel, FlattenSummaryFakeEnergyFacilityModel
from utils_data_manipulation import fetch_data, summarize, pydantic_converter_of, flatten, sort, list_of_agencies_in, categorize
from utils_IO_bound import summary_splitter


url = 'http://localhost:8080' 
this_dir = os.path.dirname(os.path.realpath(__file__))  
summary_dir_filepath = pathlib.Path(this_dir) / 'project_data' / 'summary'


def main():
    url = 'http://localhost:8080' + '/data/'
    original_dataset = fetch_data(url)
    summarized_dataset = summarize(copy.deepcopy(original_dataset))
    list_of_summary_models = pydantic_converter_of(summarized_dataset,SummaryFakeEnergyFacilityModel)
    list_of_flatten_models = flatten(copy.deepcopy(list_of_summary_models), FlattenSummaryFakeEnergyFacilityModel)
    list_of_sorted_sum_data = sort(list_of_summary_models, 'facility_id')
    list_of_sorted_flat_data = sort(list_of_flatten_models, 'facility_id', 'energy_type', 'year')
    list_of_agencies = list_of_agencies_in(list_of_summary_models)
    if not summary_dir_filepath.exists():
        summary_dir_filepath.mkdir()
    categorized_sum_dataset = categorize(list_of_sorted_sum_data,'agency',list_of_agencies)
    categorized_flat_dataset = categorize(list_of_sorted_flat_data,'agency',list_of_agencies)
    summary_splitter('json', 'summary', categorized_sum_dataset, summary_dir_filepath,list_of_agencies)
    summary_splitter('csv', 'summary', categorized_flat_dataset, summary_dir_filepath,list_of_agencies)


if __name__ == '__main__': 
    main() 
