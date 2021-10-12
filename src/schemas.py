from datetime import datetime
import enum
from typing import List, Union 
import pydantic


def value_validator(value): # validator for usage, sqft 
    if value < 0 :
        raise NegativeValueError(value, message=f'{value} cannot be negative')
    return value 


class AgencyEnum(str, enum.Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'


class EnergyEnum(str, enum.Enum):#enums holds unique items and is a form of validation 
    Elec = 'Elec'
    Natural_Gas = 'Natural Gas'
    Fuel_Oil = 'Fuel Oil'


class UnknownAgencyError(Exception):
    ''' custom error that is raised when agency value not found in known agency list '''
    def __init__(self, value: str, message:str) -> None:
        self.value = value 
        self.message = message
        super().__init__(message)


class NegativeValueError(Exception):
    ''' custom error that is raise when value is negative '''
    def __init__(self, value: Union[float, int], message) -> None:
        self.value = value 
        self.message = message
        super().__init__(message)


class EnergyRecordModel(pydantic.BaseModel):
    ''' energy records schema '''
    timestamp: datetime
    energy_type: EnergyEnum = EnergyEnum.Elec 
    usage: float


    usage_validation = pydantic.validator('usage', allow_reuse=True)(value_validator)


class SummaryEnergyRecordModel(pydantic.BaseModel):
    ''' summary energy records schema '''
    year: int 
    energy_type: str 
    num_records: int 
    average_usage_per_sqft: float 


class FakeEnergyFacilityModel(pydantic.BaseModel):
    ''' Fake energy schema '''
    facility_id: int
    name: str
    address: str
    longitude: float
    latitude: float
    agency: AgencyEnum = AgencyEnum.A
    sqft: int
    energy_records: List[EnergyRecordModel]
    

    sqft_validation = pydantic.validator('sqft', allow_reuse=True)(value_validator)

class FlattenFakeEnergyFacilityModel(pydantic.BaseModel):
    ''' Flatten energy schema '''
    facility_id: int
    name: str
    address: str
    longitude: float
    latitude: float
    agency: AgencyEnum = AgencyEnum.A
    sqft: int
    energy_type: EnergyEnum = EnergyEnum.Elec
    timestamp: datetime
    usage: float
# This schema is to be passed to each piece of data in the dataset 
# The flattening happens in flatten.py which 'preps' the data for the schema to validate types 

class SummaryFakeEnergyFacilityModel(pydantic.BaseModel):
    ''' Summary energy schema '''
    facility_id: int
    agency: AgencyEnum = AgencyEnum.A
    sqft: int
    summary: List[SummaryEnergyRecordModel]


class FlattenSummaryFakeEnergyFacilityModel(pydantic.BaseModel):
    ''' flatten summary energy schema '''
    facility_id: int
    agency: AgencyEnum = AgencyEnum.A
    sqft: int
    year: int
    energy_type: EnergyEnum = EnergyEnum.Elec 
    num_records: int
    average_usage_per_sqft: float 