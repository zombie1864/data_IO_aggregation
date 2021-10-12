""" Tests for the `schemas` module 
"""
from module_two.schemas import FakeEnergyFacilityModel, EnergyRecordModel, NegativeValueError

import pytest  


def test_good_FakeEnergyFacilityModel_inst(): 
    good_model_inst = FakeEnergyFacilityModel(
            facility_id=0,
            name='building_0',
            address='abc street, NY, 12345',
            longitude=12.00,
            latitude=1.00,
            agency='A',
            sqft=100,
            energy_records=[EnergyRecordModel(timestamp="2020-10-11T07:55:26",energy_type='Elec',usage=20.0)]
    )
    assert isinstance(good_model_inst, FakeEnergyFacilityModel)


def test_bad_FakeEnergyFacilityModel_inst(): 
    ''' test to check if an exeception is raised '''
    with pytest.raises(NegativeValueError):
        FakeEnergyFacilityModel(
                facility_id=0,
                name='building_0',
                address='abc street, NY, 12345',
                longitude=12.00,
                latitude=1.00,
                agency='A',
                sqft=-100,
                energy_records=[EnergyRecordModel(timestamp="2020-10-11T07:55:26",energy_type='Elec',usage=20.0)]
        )
    
    

