import pytest 
from unittest import mock 
from module_two.utils_data_manipulation import flatten
from module_two.schemas import FlattenFakeEnergyFacilityModel


def test_flatten(list_of_inst_models,list_of_flat_models):
    assert list_of_flat_models == flatten(list_of_inst_models, FlattenFakeEnergyFacilityModel)


def test_flatten_inst_is_pydantic(list_of_inst_models):
    result = flatten(list_of_inst_models, FlattenFakeEnergyFacilityModel)
    for obj in result:
        assert isinstance(obj, FlattenFakeEnergyFacilityModel)
