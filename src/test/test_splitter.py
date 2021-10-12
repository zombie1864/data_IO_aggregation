import pytest 
import pydantic 
from module_two.utils_data_manipulation import list_of_agencies_in, categorize


def test_list_of_agencies_in(list_of_agency_models):
    list_of_agencies = list_of_agencies_in(list_of_agency_models)
    assert sorted(list_of_agencies) == ['A','B','Z']
    assert 'C' not in list_of_agencies

    
def test_categorize(list_of_colored_item_models):
    class Item(pydantic.BaseModel):
        item: str
        color: str 
    categorized_items_by_color = categorize(list_of_colored_item_models, 'color', ['blue', 'yellow', 'green'])
    expected_res = {
        'blue_dataset': [Item(item='ball', color='blue'), Item(item='house', color='blue')],
        'yellow_dataset': [Item(item='banana', color='yellow'), Item(item='rubber docky', color='yellow')],
        'green_dataset': [Item(item='book', color='green')],
    }
    assert categorized_items_by_color == expected_res


# This was testing IO bound methods 
# def test_make_dir_for_each_in_(list_of_agencies,tmp_path):
#     filedir = tmp_path / 'tmp_splitter'
#     filedir.mkdir()
#     _make_dir_for_each_in_(list_of_agencies,filedir)
#     agencyA_filedir = filedir / 'agencyA'
#     assert agencyA_filedir.exists() is True 

# def test_list_of_agencies_in_(json_data,list_of_agencies):
#     assert list_of_agencies_in_(json_data) == list_of_agencies


# def test_if_json_data_is_categorized_by_state(json_data,categorized_dataset):
#     key = 'address'
#     list_of_items = ['NY','NJ','PA','FL','Wy']
#     assert _categorize_(json_data,key,list_of_items) == categorized_dataset


# def test_make_file_for_each_cat_in(json_data,tmp_path,categorized_dataset,list_of_agencies):
#     file_type = 'json'
#     dir = tmp_path / 'tmp_splitter'
#     test_list_of_agencies_in_(json_data,list_of_agencies)
#     test_make_dir_for_each_in_(list_of_agencies,tmp_path)
#     _make_file_for_each_cat_in_(categorized_dataset,dir,list_of_agencies,file_type)
#     agencyA_json_filepath = dir / 'agencyA' / 'agencyA-NY_dataset.json'
#     agencyB_json_filepath = dir / 'agencyB' / 'agencyB-NY_dataset.json'
#     agencyC_json_filepath = dir / 'agencyC' / 'agencyC-NY_dataset.json'
#     agencyD_json_filepath = dir / 'agencyD' / 'agencyD-NY_dataset.json'
#     assert agencyA_json_filepath.exists() is True 
#     assert agencyB_json_filepath.exists() is True 
#     assert agencyC_json_filepath.exists() is True 
#     assert agencyD_json_filepath.exists() is True 

