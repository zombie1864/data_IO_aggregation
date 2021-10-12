""" pytest fixtures belong here. 

Fixtures are basically ways to inject the same or similar data into each test in order to keep them 
DRY. They can also be used to import utilities like `mocker` to mock function calls or hold open database 
connections. 

Unlike many other python APIs, pytest fixtures do not need actually to be imported into test modules. 
When placed in a special file called `conftest.py`, they are essentially available to any test in the package.

Alot more information can be found here: https://docs.pytest.org/en/6.2.x/fixture.html

"""


import pathlib
import tempfile
import pytest 
import pydantic 

from module_two.schemas import FakeEnergyFacilityModel, EnergyRecordModel, FlattenFakeEnergyFacilityModel

@pytest.fixture
def list_of_agency_models():
    class FakeModelWithAgencies(pydantic.BaseModel):
        agency: str 
    return [FakeModelWithAgencies(agency='A'), FakeModelWithAgencies(agency='B'), FakeModelWithAgencies(agency='Z')]


@pytest.fixture 
def list_of_colored_item_models():
    class Item(pydantic.BaseModel):
        item: str
        color: str 
    return [Item(item='ball', color='blue'), Item(item='house', color='blue'), Item(item='banana', color='yellow'), Item(item='rubber docky', color='yellow'), Item(item='book', color='green')]

@pytest.fixture 
def list_of_inst_models():
    return [
        FakeEnergyFacilityModel(
        facility_id=1,
        name='builing_1',
        address='neon dreams ave, Miami, FL, 9000',
        longitude=27.07,
        latitude=27.07,
        agency='A',
        sqft=45000,
        energy_records=[
            EnergyRecordModel(
            energy_type='Elec',
            timestamp='2014-04-27T10:24:08',
            usage=5099.6442
            ), 
            EnergyRecordModel(
            energy_type='Natural Gas',
            timestamp='2018-09-11T10:36:41',
            usage=8099.6442
            ), 
            EnergyRecordModel(
            energy_type='Elec',
            timestamp='2016-07-23T11:51:47',
            usage=9099.6442
            ), 
        ]),
        FakeEnergyFacilityModel(
        facility_id=2,
        name='builing_2',
        address='neon dreams ave, Miami, FL, 9000',
        longitude=27.07,
        latitude=27.07,
        agency='A',
        sqft=45000,
        energy_records=[
            EnergyRecordModel(
            energy_type="Elec",
            timestamp="2014-04-27T10:24:08",
            usage=5099.6442
            ), 
            EnergyRecordModel(
            energy_type="Elec",
            timestamp="2014-06-27T10:24:08",
            usage=5089.6442
            ), 
            EnergyRecordModel(
            energy_type="Elec",
            timestamp="2014-07-27T10:24:08",
            usage=4099.6442
            ), 
        ]),
    ]

@pytest.fixture
def list_of_flat_models():
    return [
        FlattenFakeEnergyFacilityModel(
        facility_id=1,
        name='builing_1',
        address='neon dreams ave, Miami, FL, 9000',
        longitude=27.07,
        latitude=27.07,
        agency='A',
        sqft=45000,
        energy_type='Elec',
        timestamp='2014-04-27T10:24:08',
        usage=5099.6442
        ),
        FlattenFakeEnergyFacilityModel(
        facility_id=1,
        name='builing_1',
        address='neon dreams ave, Miami, FL, 9000',
        longitude=27.07,
        latitude=27.07,
        agency='A',
        sqft=45000,
        energy_type='Natural Gas',
        timestamp='2018-09-11T10:36:41',
        usage=8099.6442
        ),
        FlattenFakeEnergyFacilityModel(
        facility_id=1,
        name='builing_1',
        address='neon dreams ave, Miami, FL, 9000',
        longitude=27.07,
        latitude=27.07,
        agency='A',
        sqft=45000,
        energy_type='Elec',
        timestamp='2016-07-23T11:51:47',
        usage=9099.6442
        ),
        FlattenFakeEnergyFacilityModel(
        facility_id=2,
        name='builing_2',
        address='neon dreams ave, Miami, FL, 9000',
        longitude=27.07,
        latitude=27.07,
        agency='A',
        sqft=45000,
        energy_type="Elec",
        timestamp="2014-04-27T10:24:08",
        usage=5099.6442
        ),
        FlattenFakeEnergyFacilityModel(
        facility_id=2,
        name='builing_2',
        address='neon dreams ave, Miami, FL, 9000',
        longitude=27.07,
        latitude=27.07,
        agency='A',
        sqft=45000,
        energy_type="Elec",
        timestamp="2014-06-27T10:24:08",
        usage=5089.6442
        ),
        FlattenFakeEnergyFacilityModel(
        facility_id=2,
        name='builing_2',
        address='neon dreams ave, Miami, FL, 9000',
        longitude=27.07,
        latitude=27.07,
        agency='A',
        sqft=45000,
        energy_type="Elec",
        timestamp="2014-07-27T10:24:08",
        usage=4099.6442
        ),
    ]

@pytest.fixture 
def records():
    return [
        {
            'facility_id':1,
            'name':'builing_1',
            'address':'neon dreams ave, Miami, FL, 9000',
            'longitude':27.07,
            'latitude':27.07,
            'agency':'A',
            'sqft':45000,
            'energy_records':[
                {
                    'energy_type': 'Elec',
                    'timestamp': '2014-04-27T10:24:08',
                    'usage': 5099.6442
                },
                {
                    'energy_type': 'Natural Gas',
                    'timestamp': '2018-09-11T10:36:41',
                    'usage': 8099.6442
                },
                {
                    'energy_type': 'Elec',
                    'timestamp': '2016-07-23T11:51:47',
                    'usage': 9099.6442
                },
            ]
        },
        {
            'facility_id':2,
            'name':'builing_2',
            'address':'neon dreams ave, Miami, FL, 9000',
            'longitude':27.07,
            'latitude':27.07,
            'agency':'A',
            'sqft':45000,
            'energy_records':[
                {
                    "energy_type": "Elec",
                    "timestamp": "2014-04-27T10:24:08",
                    "usage": 5099.6442
                },
                {
                    "energy_type": "Elec",
                    "timestamp": "2014-06-27T10:24:08",
                    "usage": 5089.6442
                },
                {
                    "energy_type": "Elec",
                    "timestamp": "2014-07-27T10:24:08",
                    "usage": 4099.6442
                },
            ]
        },
    ]

@pytest.fixture 
def flatten_records_by_csvwriter():
    ''' csv file will stringfy everything '''
    return [
        {
            'facility_id':'1',
            'name':'builing_1',
            'address':'neon dreams ave, Miami, FL, 9000',
            'longitude':'27.07',
            'latitude':'27.07',
            'agency':'A',
            'sqft':'45000',
            'energy_type': 'Elec',
            'timestamp': '2014-04-27 10:24:08',
            'usage': '5099.6442'
        },
        {
            'facility_id':'1',
            'name':'builing_1',
            'address':'neon dreams ave, Miami, FL, 9000',
            'longitude':'27.07',
            'latitude':'27.07',
            'agency':'A',
            'sqft':'45000',
            'energy_type': 'Natural Gas',
            'timestamp': '2018-09-11 10:36:41',
            'usage': '8099.6442'
        },
        {
            'facility_id':'1',
            'name':'builing_1',            
            'address':'neon dreams ave, Miami, FL, 9000',
            'longitude':'27.07',
            'latitude':'27.07',
            'agency':'A',
            'sqft':'45000',
            'energy_type': 'Elec',
            'timestamp': '2016-07-23 11:51:47',
            'usage': '9099.6442'
        },
        {
            'facility_id':'2',
            'name':'builing_2',            
            'address':'neon dreams ave, Miami, FL, 9000',
            'longitude':'27.07',
            'latitude':'27.07',
            'agency':'A',
            'sqft':'45000',
            'energy_type': 'Elec',
            'timestamp': '2014-04-27 10:24:08',
            'usage': '5099.6442'
        },
        {
            'facility_id':'2',
            'name':'builing_2',            
            'address':'neon dreams ave, Miami, FL, 9000',
            'longitude':'27.07',
            'latitude':'27.07',
            'agency':'A',
            'sqft':'45000',
            'energy_type': 'Elec',
            'timestamp': '2014-06-27 10:24:08',
            'usage': '5089.6442'
        },
        {
            'facility_id':'2',
            'name':'builing_2',            
            'address':'neon dreams ave, Miami, FL, 9000',
            'longitude':'27.07',
            'latitude':'27.07',
            'agency':'A',
            'sqft':'45000',
            'energy_type': 'Elec',
            'timestamp': '2014-07-27 10:24:08',
            'usage': '4099.6442'
        },
    ]

@pytest.fixture 
def summarized_dataset():
    return [
        {
            'facility_id': 1, 
            'agency': 'A',
            'sqft': 45000,
            'summary': [
                {
                    'year': 2014, 
                    'energy_type': 'Elec',
                    'num_records': 1, 
                    'average_usage_per_sqft': 0.1133
                },
                {
                    'year': 2016, 
                    'energy_type': 'Elec',
                    'num_records': 1, 
                    'average_usage_per_sqft': 0.2022
                },
                {
                    'year': 2018, 
                    'energy_type': 'Natrual Gas',
                    'num_records': 1, 
                    'average_usage_per_sqft': 0.1800
                },
            ]
        },
        {
            'facility_id': 2, 
            'agency': 'A',
            'sqft': 45000,
            'summary': [
                {
                    'year': 2014, 
                    'energy_type': 'Elec',
                    'num_records': 3, 
                    'average_usage_per_sqft': 0.1058
                },
            ]
        },
    ]


@pytest.fixture
def unflatten_dataset():  
    return [
        {
            'facility_id': 00,
            'name': 'test_name_00',
            'address': 'address_00 ave, test, PY, 0000',
            'longitude': 00.00,
            'latitude': 00.00,
            'agency': 'A',
            'sqft': 101,
            'energy_records': [
                {
                    'energy_type': 'Elec',
                    'timestamp':'2021-01-01T00:00:00',
                    'usage': 00.00,
                },
                {
                    'energy_type': 'Natural Gas',
                    'timestamp':'2021-01-01T00:00:00',
                    'usage': 00.00,
                },
                {
                    'energy_type': 'Fuel Oil',
                    'timestamp':'2021-01-01T00:00:00',
                    'usage': 00.00,
                },
            ]
        }
    ]



@pytest.fixture 
def list_of_agencies(): 
    return ['A','B','C','D']

@pytest.fixture
def categorized_dataset():
    return {
        'NY_dataset': [{'facility_id':2,'name':'builing_2','address':'abc ave, Brooklyn, NY, 9000','longitude':27.07,'latitude':27.07,'agency':'A','sqft':1000000,'energy_records':[{'timestamp':'1984-06-18T12:00:00','energy_type':'Elec','usage':100000000}]},{'facility_id':6,'name':'builing_6','address':'44th street, Brooklyn, NY, 11219','longitude':27.07,'latitude':27.07,'agency':'B','sqft':1000000,'energy_records':[{'timestamp':'1984-06-18T12:00:00','energy_type':'Elec','usage':100000000}]
            },],
        'NJ_dataset': [{'facility_id':4,'name':'builing_4','address':'closer ave, knownish, NJ, 9000','longitude':27.07,'latitude':27.07,'agency':'C','sqft':1000000,'energy_records':[{'timestamp':'1984-06-18T12:00:00','energy_type':'Elec','usage':100000000}]},{'facility_id':7,'name':'builing_7','address':'404th street, atown, NJ, 11220','longitude':27.07,'latitude':27.07,'agency':'B','sqft':1000000,'energy_records':[{'timestamp':'1984-06-18T12:00:00','energy_type':'Elec','usage':100000000}]},],
        'FL_dataset': [{'facility_id':1,'name':'builing_1','address':'neon dreams ave, Miami, FL, 9000','longitude':27.07,'latitude':27.07,'agency':'A','sqft':1000000,'energy_records':[{'timestamp':'1984-06-18T12:00:00','energy_type':'Elec','usage':100000000}]
            },],
        'Wy_dataset': [{'facility_id':5,'name':'builing_5','address':'The void, infinite, Wy, 0000','longitude':00.00,'latitude':00.00,'agency':'D','sqft':1000000,'energy_records':[{'timestamp':'1984-06-18T12:00:00','energy_type':'Elec','usage':100000000}]},],
        'PA_dataset': [{'facility_id':3,'name':'builing_3','address':'Nowhere street, unknown, PA, 9000','longitude':27.07,'latitude':27.07,'agency':'B','sqft':1000000,'energy_records':[{'timestamp':'1984-06-18T12:00:00','energy_type':'Elec','usage':100000000}]},]
    }

@pytest.fixture 
def mock_api_resp(): 
    return {
    "count": 100,
    "next": "http://localhost:8080/data/?page=2",
    "prev": None,
    'records': [
        {
            'facility_id':1,
            'name':'builing_1',
            'address':'neon dreams ave, Miami, FL, 9000',
            'longitude':27.07,
            'latitude':27.07,
            'agency':'A',
            'sqft':1000000,
            'energy_records':[{
                'timestamp':'1984-06-18T12:00:00',
                'energy_type':'Elec',
                'usage':100000000
            }]
        },
        {
            'facility_id':2,
            'name':'builing_2',
            'address':'abc ave, Brooklyn, NY, 9000',
            'longitude':27.07,
            'latitude':27.07,
            'agency':'A',
            'sqft':1000000,
            'energy_records':[{
                'timestamp':'1984-06-18T12:00:00',
                'energy_type':'Elec',
                'usage':100000000
            }]
        },
        {
            'facility_id':3,
            'name':'builing_3',
            'address':'Nowhere street, unknown, PA, 9000',
            'longitude':27.07,
            'latitude':27.07,
            'agency':'B',
            'sqft':1000000,
            'energy_records':[{
                'timestamp':'1984-06-18T12:00:00',
                'energy_type':'Elec',
                'usage':100000000
            }]
        },
        {
            'facility_id':4,
            'name':'builing_4',
            'address':'closer ave, knownish, NJ, 9000',
            'longitude':27.07,
            'latitude':27.07,
            'agency':'C',
            'sqft':1000000,
            'energy_records':[{
                'timestamp':'1984-06-18T12:00:00',
                'energy_type':'Elec',
                'usage':100000000
            }]
        },
        {
            'facility_id':5,
            'name':'builing_5',
            'address':'The void, infinite, Wy, 0000',
            'longitude':00.00,
            'latitude':00.00,
            'agency':'D',
            'sqft':1000000,
            'energy_records':[{
                'timestamp':'1984-06-18T12:00:00',
                'energy_type':'Elec',
                'usage':100000000
            }]
        },
        {
            'facility_id':6,
            'name':'builing_6',
            'address':'44th street, Brooklyn, NY, 11219',
            'longitude':27.07,
            'latitude':27.07,
            'agency':'B',
            'sqft':1000000,
            'energy_records':[{
                'timestamp':'1984-06-18T12:00:00',
                'energy_type':'Elec',
                'usage':100000000
            }]
        },
        {
            'facility_id':7,
            'name':'builing_7',
            'address':'404th street, atown, NJ, 11220',
            'longitude':27.07,
            'latitude':27.07,
            'agency':'B',
            'sqft':1000000,
            'energy_records':[{
                'timestamp':'1984-06-18T12:00:00',
                'energy_type':'Elec',
                'usage':100000000
            }]
        },
    ]
}

@pytest.fixture 
def tmp_path():
    with tempfile.TemporaryDirectory() as tmp_dirname:
        yield pathlib.Path(tmp_dirname)
'''  creates a tmp_path and then deletes when done'''

@pytest.fixture
def mock_api_query():
    return {
        'http://localhost:8080/data/?address_contains=NY&sqft_gte=50000':{
            "count": 100,
            "next": "http://localhost:8080/data/?page=2",
            "prev": None,
            'records': [
                {
                    '_id': 'db_id_1',
                    'facility_id':2,
                    'name':'builing_2',
                    'address':'abc ave, Brooklyn, NY, 9000',
                    'longitude':27.07,
                    'latitude':27.07,
                    'agency':'A',
                    'sqft':1000000,
                    'energy_records':[{
                        'timestamp':'1984-06-18T12:00:00',
                        'energy_type':'Elec',
                        'usage':100000000
                    }]
                },
                {
                    '_id': 'db_id_2',
                    'facility_id':6,
                    'name':'builing_6',
                    'address':'44th street, Brooklyn, NY, 11219',
                    'longitude':27.07,
                    'latitude':27.07,
                    'agency':'B',
                    'sqft':1000000,
                    'energy_records':[{
                        'timestamp':'1984-06-18T12:00:00',
                        'energy_type':'Elec',
                        'usage':100000000
                    }]
                },
            ]
        },
    
        'http://localhost:8080/data/?address_contains=NJ&sqft_gte=50000':{
        "count": 100,
        "next": "http://localhost:8080/data/?page=2",
        "prev": None,
        'records': [
            {
                '_id': 'db_id_3',
                'facility_id':4,
                'name':'builing_4',
                'address':'closer ave, knownish, NJ, 9000',
                'longitude':27.07,
                'latitude':27.07,
                'agency':'C',
                'sqft':1000000,
                'energy_records':[{
                    'timestamp':'1984-06-18T12:00:00',
                    'energy_type':'Elec',
                    'usage':100000000
                }]
            },
            {
                '_id': 'db_id_4',
                'facility_id':7,
                'name':'builing_7',
                'address':'404th street, atown, NJ, 11220',
                'longitude':27.07,
                'latitude':27.07,
                'agency':'B',
                'sqft':1000000,
                'energy_records':[{
                    'timestamp':'1984-06-18T12:00:00',
                    'energy_type':'Elec',
                    'usage':100000000
                }]
            },
        ]
    },
        'http://localhost:8080/data/?address_contains=FL&sqft_gte=50000':{
            "count": 100,
            "next": "http://localhost:8080/data/?page=2",
            "prev": None,
            'records': [
                {
                    '_id': 'db_id_5',
                    'facility_id':1,
                    'name':'builing_1',
                    'address':'neon dreams ave, Miami, FL, 9000',
                    'longitude':27.07,
                    'latitude':27.07,
                    'agency':'A',
                    'sqft':1000000,
                    'energy_records':[{
                        'timestamp':'1984-06-18T12:00:00',
                        'energy_type':'Elec',
                        'usage':100000000
                    }]
                },
            ]
        },
        'http://localhost:8080/data/?address_contains=Wy&sqft_gte=50000':{
            "count": 100,
            "next": "http://localhost:8080/data/?page=2",
            "prev": None,
            'records': [
                {
                    '_id': 'db_id_6',
                    'facility_id':5,
                    'name':'builing_5',
                    'address':'The void, infinite, Wy, 0000',
                    'longitude':00.00,
                    'latitude':00.00,
                    'agency':'D',
                    'sqft':1000000,
                    'energy_records':[{
                        'timestamp':'1984-06-18T12:00:00',
                        'energy_type':'Elec',
                        'usage':100000000
                    }]
                },
            ]
        },
        'http://localhost:8080/data/?address_contains=PA&sqft_gte=50000':{
            "count": 100,
            "next": "http://localhost:8080/data/?page=2",
            "prev": None,
            'records': [
                {
                    '_id': 'db_id_7',
                    'facility_id':3,
                    'name':'builing_3',
                    'address':'Nowhere street, unknown, PA, 9000',
                    'longitude':27.07,
                    'latitude':27.07,
                    'agency':'B',
                    'sqft':1000000,
                    'energy_records':[{
                        'timestamp':'1984-06-18T12:00:00',
                        'energy_type':'Elec',
                        'usage':100000000
                    }]
                }
            ]
        },
    }

@pytest.fixture 
def fetch_one_output():
    return "{'_id': '60c9f1ca876decd5c3bd4ee4', 'address': '476 Eaton Court, Chase, NY, 3402', 'agency': 'A', 'energy_records': [{'energy_type': 'Natural Gas', 'timestamp': '2020-10-11T07:55:26', 'usage': 4295.02}, {'energy_type': 'Elec', 'timestamp': '2014-04-27T10:24:08', 'usage': 5099.6442}, {'energy_type': 'Fuel Oil', 'timestamp': '2018-09-11T10:36:41', 'usage': 5583.4303}, {'energy_type': 'Elec', 'timestamp': '2016-07-23T11:51:47', 'usage': 9837.6877}, {'energy_type': 'Fuel Oil', 'timestamp': '2017-10-11T02:01:24', 'usage': 1916.0777}, {'energy_type': 'Fuel Oil', 'timestamp': '2021-04-15T10:10:31', 'usage': 2661.5274}, {'energy_type': 'Fuel Oil', 'timestamp': '2018-12-06T05:23:57', 'usage': 897.1619}, {'energy_type': 'Fuel Oil', 'timestamp': '2021-02-23T05:48:59', 'usage': 661.3208}, {'energy_type': 'Natural Gas', 'timestamp': '2019-12-11T02:40:49', 'usage': 343.4757}, {'energy_type': 'Fuel Oil', 'timestamp': '2018-01-09T08:24:36', 'usage': 4287.9645}, {'energy_type': 'Elec', 'timestamp': '2016-12-14T01:55:49', 'usage': 1101.2439}, {'energy_type': 'Fuel Oil', 'timestamp': '2015-09-15T05:14:55', 'usage': 209.2868}, {'energy_type': 'Elec', 'timestamp': '2018-10-07T10:05:59', 'usage': 4294.4978}, {'energy_type': 'Elec', 'timestamp': '2018-03-02T01:34:01', 'usage': 8377.6537}, {'energy_type': 'Fuel Oil', 'timestamp': '2016-06-18T07:09:07', 'usage': 269.106}, {'energy_type': 'Natural Gas', 'timestamp': '2016-06-14T08:19:18', 'usage': 6270.6358}, {'energy_type': 'Natural Gas', 'timestamp': '2015-01-08T05:59:18', 'usage': 9422.3852}, {'energy_type': 'Fuel Oil', 'timestamp': '2014-07-29T04:47:40', 'usage': 6339.1759}, {'energy_type': 'Natural Gas', 'timestamp': '2016-10-28T08:06:13', 'usage': 4505.0042}, {'energy_type': 'Natural Gas', 'timestamp': '2019-10-13T08:24:54', 'usage': 9802.6804}, {'energy_type': 'Fuel Oil', 'timestamp': '2014-03-13T03:32:02', 'usage': 5470.1903}, {'energy_type': 'Fuel Oil', 'timestamp': '2019-05-25T11:33:47', 'usage': 4946.0739}, {'energy_type': 'Fuel Oil', 'timestamp': '2014-03-21T01:21:31', 'usage': 5919.7587}, {'energy_type': 'Natural Gas', 'timestamp': '2018-08-08T06:33:37', 'usage': 8543.7134}, {'energy_type': 'Natural Gas', 'timestamp': '2017-08-16T02:22:40', 'usage': 1825.3586}, {'energy_type': 'Fuel Oil', 'timestamp': '2014-02-26T04:40:20', 'usage': 5539.2578}, {'energy_type': 'Natural Gas', 'timestamp': '2015-06-07T06:30:35', 'usage': 6199.1121}, {'energy_type': 'Natural Gas', 'timestamp': '2018-12-13T05:43:21', 'usage': 1805.9443}, {'energy_type': 'Natural Gas', 'timestamp': '2019-12-02T07:27:23', 'usage': 3784.4607}, {'energy_type': 'Elec', 'timestamp': '2017-10-22T06:59:09', 'usage': 3681.8345}, {'energy_type': 'Fuel Oil', 'timestamp': '2019-04-10T07:11:59', 'usage': 2095.0475}, {'energy_type': 'Fuel Oil', 'timestamp': '2017-11-30T01:45:12', 'usage': 201.526}, {'energy_type': 'Fuel Oil', 'timestamp': '2017-11-26T05:45:33', 'usage': 4422.7291}, {'energy_type': 'Fuel Oil', 'timestamp': '2014-05-21T11:25:40', 'usage': 1671.5678}, {'energy_type': 'Natural Gas', 'timestamp': '2016-09-08T04:13:36', 'usage': 7922.1782}, {'energy_type': 'Fuel Oil', 'timestamp': '2020-02-20T05:28:08', 'usage': 2739.4775}, {'energy_type': 'Fuel Oil', 'timestamp': '2015-08-31T08:26:01', 'usage': 261.6415}, {'energy_type': 'Elec', 'timestamp': '2015-08-30T06:46:44', 'usage': 4010.9079}, {'energy_type': 'Fuel Oil', 'timestamp': '2019-08-28T10:26:53', 'usage': 5497.0606}, {'energy_type': 'Fuel Oil', 'timestamp': '2018-12-21T10:27:52', 'usage': 612.7584}, {'energy_type': 'Natural Gas', 'timestamp': '2016-10-10T04:59:06', 'usage': 2970.1808}, {'energy_type': 'Elec', 'timestamp': '2019-12-20T06:31:22', 'usage': 23.3775}, {'energy_type': 'Fuel Oil', 'timestamp': '2015-10-14T10:53:24', 'usage': 1959.5456}, {'energy_type': 'Natural Gas', 'timestamp': '2020-08-25T06:45:37', 'usage': 3475.9427}, {'energy_type': 'Fuel Oil', 'timestamp': '2019-11-15T11:10:37', 'usage': 1788.4744}, {'energy_type': 'Fuel Oil', 'timestamp': '2018-01-16T01:40:49', 'usage': 7701.4393}, {'energy_type': 'Elec', 'timestamp': '2016-06-19T06:52:34', 'usage': 9506.7283}, {'energy_type': 'Natural Gas', 'timestamp': '2016-06-11T03:51:00', 'usage': 4752.0809}, {'energy_type': 'Elec', 'timestamp': '2018-02-20T11:57:27', 'usage': 2265.1993}, {'energy_type': 'Natural Gas', 'timestamp': '2017-11-11T03:18:43', 'usage': 998.62}, {'energy_type': 'Natural Gas', 'timestamp': '2017-10-28T04:29:05', 'usage': 5793.6032}, {'energy_type': 'Natural Gas', 'timestamp': '2019-06-08T10:02:37', 'usage': 4781.6761}, {'energy_type': 'Elec', 'timestamp': '2021-01-08T06:02:53', 'usage': 9486.8912}, {'energy_type': 'Natural Gas', 'timestamp': '2018-12-24T10:28:38', 'usage': 280.3179}, {'energy_type': 'Natural Gas', 'timestamp': '2016-10-14T07:29:15', 'usage': 5302.2591}, {'energy_type': 'Fuel Oil', 'timestamp': '2015-11-02T12:50:50', 'usage': 7495.6194}, {'energy_type': 'Elec', 'timestamp': '2016-07-19T08:35:33', 'usage': 4272.3873}, {'energy_type': 'Fuel Oil', 'timestamp': '2017-01-25T11:48:40', 'usage': 8449.6288}, {'energy_type': 'Natural Gas', 'timestamp': '2014-10-04T06:42:18', 'usage': 2069.8066}, {'energy_type': 'Natural Gas', 'timestamp': '2020-10-08T03:47:19', 'usage': 6717.1273}, {'energy_type': 'Fuel Oil', 'timestamp': '2019-03-24T11:27:59', 'usage': 3393.8051}], 'facility_id': 0, 'latitude': -81.243973, 'longitude': -143.438778, 'name': 'Building 0', 'sqft': 46588}\n"

@pytest.fixture 
def fetch_many_output():
    return "{'count': 1, 'next': None, 'prev': None, 'records': [{'_id': '60c9f1ca1523ad0019b3e1ea', 'address': '478 Paerdegat Avenue, Harleigh, NJ, 3509', 'agency': 'C', 'energy_records': [{'energy_type': 'Natural Gas', 'timestamp': '2016-01-07T10:51:13', 'usage': 7358.8844}, {'energy_type': 'Elec', 'timestamp': '2018-06-21T07:00:04', 'usage': 7141.961}, {'energy_type': 'Elec', 'timestamp': '2018-03-24T05:14:10', 'usage': 8885.2922}, {'energy_type': 'Fuel Oil', 'timestamp': '2016-12-26T03:11:49', 'usage': 8620.2933}, {'energy_type': 'Fuel Oil', 'timestamp': '2018-05-26T01:35:33', 'usage': 7573.4968}, {'energy_type': 'Natural Gas', 'timestamp': '2018-06-06T01:37:38', 'usage': 762.6639}, {'energy_type': 'Natural Gas', 'timestamp': '2019-03-14T05:53:45', 'usage': 2515.4551}, {'energy_type': 'Natural Gas', 'timestamp': '2017-08-19T04:23:05', 'usage': 7431.0259}, {'energy_type': 'Natural Gas', 'timestamp': '2020-03-18T01:49:06', 'usage': 2708.0284}, {'energy_type': 'Fuel Oil', 'timestamp': '2015-10-22T09:07:29', 'usage': 3728.0924}, {'energy_type': 'Natural Gas', 'timestamp': '2020-05-14T01:12:38', 'usage': 7302.5535}, {'energy_type': 'Natural Gas', 'timestamp': '2017-10-15T11:00:56', 'usage': 4392.6329}, {'energy_type': 'Natural Gas', 'timestamp': '2014-05-04T02:16:07', 'usage': 2830.231}, {'energy_type': 'Elec', 'timestamp': '2019-09-09T01:39:37', 'usage': 8048.4141}, {'energy_type': 'Natural Gas', 'timestamp': '2021-04-02T04:45:05', 'usage': 9705.1008}, {'energy_type': 'Natural Gas', 'timestamp': '2015-06-23T08:51:27', 'usage': 8113.9583}, {'energy_type': 'Natural Gas', 'timestamp': '2015-10-05T07:53:42', 'usage': 5480.2403}, {'energy_type': 'Elec', 'timestamp': '2016-10-10T09:20:20', 'usage': 2418.9261}, {'energy_type': 'Natural Gas', 'timestamp': '2018-08-10T07:56:28', 'usage': 7111.8323}, {'energy_type': 'Elec', 'timestamp': '2014-04-06T11:00:03', 'usage': 5162.9635}, {'energy_type': 'Elec', 'timestamp': '2016-10-06T07:09:33', 'usage': 6731.7939}, {'energy_type': 'Natural Gas', 'timestamp': '2016-08-31T04:27:02', 'usage': 5046.0807}, {'energy_type': 'Elec', 'timestamp': '2014-08-23T01:59:57', 'usage': 3857.1683}, {'energy_type': 'Elec', 'timestamp': '2019-03-12T01:02:13', 'usage': 1300.258}, {'energy_type': 'Fuel Oil', 'timestamp': '2018-06-27T10:05:49', 'usage': 6345.6723}, {'energy_type': 'Elec', 'timestamp': '2014-02-24T02:57:33', 'usage': 9505.0717}, {'energy_type': 'Natural Gas', 'timestamp': '2015-12-04T12:25:48', 'usage': 3988.7097}, {'energy_type': 'Fuel Oil', 'timestamp': '2015-12-14T04:40:49', 'usage': 7465.9599}, {'energy_type': 'Fuel Oil', 'timestamp': '2018-03-17T06:46:47', 'usage': 3691.843}, {'energy_type': 'Elec', 'timestamp': '2015-06-18T08:11:43', 'usage': 9410.188}, {'energy_type': 'Elec', 'timestamp': '2020-08-16T12:28:07', 'usage': 9812.0667}, {'energy_type': 'Fuel Oil', 'timestamp': '2017-06-03T03:05:05', 'usage': 5456.4932}, {'energy_type': 'Natural Gas', 'timestamp': '2014-09-28T05:23:13', 'usage': 6614.7938}, {'energy_type': 'Natural Gas', 'timestamp': '2014-12-03T09:42:36', 'usage': 4979.3078}, {'energy_type': 'Natural Gas', 'timestamp': '2016-01-16T10:26:09', 'usage': 7031.9336}, {'energy_type': 'Natural Gas', 'timestamp': '2017-08-28T09:28:30', 'usage': 8939.3649}, {'energy_type': 'Elec', 'timestamp': '2017-01-28T08:48:15', 'usage': 9054.1227}, {'energy_type': 'Elec', 'timestamp': '2017-07-30T10:09:55', 'usage': 4187.2217}, {'energy_type': 'Natural Gas', 'timestamp': '2017-01-17T10:25:13', 'usage': 5800.2348}, {'energy_type': 'Fuel Oil', 'timestamp': '2017-09-04T07:19:39', 'usage': 4236.456}, {'energy_type': 'Elec', 'timestamp': '2017-06-27T07:44:54', 'usage': 6825.5506}, {'energy_type': 'Fuel Oil', 'timestamp': '2015-08-07T08:08:42', 'usage': 7662.4075}, {'energy_type': 'Fuel Oil', 'timestamp': '2020-12-09T09:49:20', 'usage': 1917.2752}, {'energy_type': 'Fuel Oil', 'timestamp': '2014-10-14T11:46:06', 'usage': 2042.4889}, {'energy_type': 'Natural Gas', 'timestamp': '2018-09-25T08:29:57', 'usage': 7959.4708}, {'energy_type': 'Natural Gas', 'timestamp': '2016-04-20T07:27:08', 'usage': 6025.9754}, {'energy_type': 'Natural Gas', 'timestamp': '2018-01-27T05:49:25', 'usage': 135.8437}, {'energy_type': 'Natural Gas', 'timestamp': '2014-07-11T07:47:12', 'usage': 597.4012}, {'energy_type': 'Fuel Oil', 'timestamp': '2020-03-25T11:22:06', 'usage': 2825.0485}, {'energy_type': 'Natural Gas', 'timestamp': '2016-03-08T11:57:42', 'usage': 9712.2624}, {'energy_type': 'Fuel Oil', 'timestamp': '2017-10-02T11:51:51', 'usage': 7574.82}, {'energy_type': 'Fuel Oil', 'timestamp': '2015-12-03T07:10:34', 'usage': 8729.0003}, {'energy_type': 'Fuel Oil', 'timestamp': '2014-02-23T06:26:44', 'usage': 94.1893}, {'energy_type': 'Fuel Oil', 'timestamp': '2014-06-25T02:26:48', 'usage': 2588.069}, {'energy_type': 'Natural Gas', 'timestamp': '2016-09-02T10:41:44', 'usage': 2154.1154}, {'energy_type': 'Natural Gas', 'timestamp': '2017-10-08T09:41:15', 'usage': 4301.6452}, {'energy_type': 'Fuel Oil', 'timestamp': '2014-03-13T01:03:10', 'usage': 2340.898}, {'energy_type': 'Fuel Oil', 'timestamp': '2016-08-01T08:19:33', 'usage': 5654.9013}, {'energy_type': 'Fuel Oil', 'timestamp': '2020-03-09T08:29:19', 'usage': 5947.3199}, {'energy_type': 'Elec', 'timestamp': '2016-09-28T06:51:34', 'usage': 8029.0753}, {'energy_type': 'Natural Gas', 'timestamp': '2017-06-30T10:45:44', 'usage': 3076.7409}, {'energy_type': 'Natural Gas', 'timestamp': '2018-04-29T01:50:41', 'usage': 6602.904}, {'energy_type': 'Fuel Oil', 'timestamp': '2017-07-03T04:46:25', 'usage': 465.4762}, {'energy_type': 'Natural Gas', 'timestamp': '2017-12-25T09:09:08', 'usage': 3194.1279}, {'energy_type': 'Elec', 'timestamp': '2017-03-06T01:18:31', 'usage': 4930.9698}, {'energy_type': 'Fuel Oil', 'timestamp': '2021-01-25T06:22:03', 'usage': 9869.7403}, {'energy_type': 'Elec', 'timestamp': '2016-08-15T12:24:56', 'usage': 9535.4434}, {'energy_type': 'Natural Gas', 'timestamp': '2015-04-29T07:33:33', 'usage': 3541.3133}, {'energy_type': 'Fuel Oil', 'timestamp': '2019-12-01T03:00:25', 'usage': 748.1279}, {'energy_type': 'Fuel Oil', 'timestamp': '2018-03-18T08:58:48', 'usage': 4509.5196}, {'energy_type': 'Natural Gas', 'timestamp': '2014-10-28T09:14:36', 'usage': 7781.8183}, {'energy_type': 'Natural Gas', 'timestamp': '2018-10-22T06:09:11', 'usage': 1969.1386}, {'energy_type': 'Natural Gas', 'timestamp': '2020-10-02T07:04:32', 'usage': 3104.7082}, {'energy_type': 'Fuel Oil', 'timestamp': '2014-09-09T10:27:35', 'usage': 994.7858}, {'energy_type': 'Elec', 'timestamp': '2016-05-26T10:03:50', 'usage': 3556.7048}, {'energy_type': 'Natural Gas', 'timestamp': '2020-05-29T06:55:46', 'usage': 1830.3231}, {'energy_type': 'Fuel Oil', 'timestamp': '2014-07-23T05:50:03', 'usage': 766.8076}, {'energy_type': 'Fuel Oil', 'timestamp': '2015-11-14T05:59:44', 'usage': 275.1859}, {'energy_type': 'Natural Gas', 'timestamp': '2020-07-28T10:13:12', 'usage': 7863.3973}, {'energy_type': 'Elec', 'timestamp': '2018-06-18T11:58:24', 'usage': 224.4168}, {'energy_type': 'Fuel Oil', 'timestamp': '2015-04-03T08:56:40', 'usage': 9504.856}, {'energy_type': 'Fuel Oil', 'timestamp': '2016-11-01T08:43:58', 'usage': 505.2644}, {'energy_type': 'Natural Gas', 'timestamp': '2015-01-14T03:55:54', 'usage': 5791.625}, {'energy_type': 'Elec', 'timestamp': '2018-10-28T06:11:07', 'usage': 2867.013}, {'energy_type': 'Fuel Oil', 'timestamp': '2017-03-07T08:23:35', 'usage': 2014.6833}, {'energy_type': 'Fuel Oil', 'timestamp': '2014-04-18T10:16:40', 'usage': 7441.8896}, {'energy_type': 'Natural Gas', 'timestamp': '2020-01-30T12:07:35', 'usage': 3494.9479}, {'energy_type': 'Fuel Oil', 'timestamp': '2014-10-31T07:00:11', 'usage': 3986.7218}, {'energy_type': 'Natural Gas', 'timestamp': '2017-07-05T06:00:03', 'usage': 1240.7878}, {'energy_type': 'Elec', 'timestamp': '2017-08-13T06:30:58', 'usage': 8184.3049}, {'energy_type': 'Elec', 'timestamp': '2020-07-19T02:16:12', 'usage': 9540.8539}, {'energy_type': 'Fuel Oil', 'timestamp': '2019-06-15T01:34:41', 'usage': 3644.0314}, {'energy_type': 'Natural Gas', 'timestamp': '2015-02-08T04:45:50', 'usage': 6726.8348}, {'energy_type': 'Natural Gas', 'timestamp': '2021-02-25T01:04:15', 'usage': 9111.8212}, {'energy_type': 'Elec', 'timestamp': '2020-09-29T10:21:19', 'usage': 1956.6999}, {'energy_type': 'Elec', 'timestamp': '2016-10-22T02:34:39', 'usage': 4584.6083}, {'energy_type': 'Elec', 'timestamp': '2014-01-07T03:20:22', 'usage': 5092.2879}], 'facility_id': 53, 'latitude': -6.00756, 'longitude': 62.618959, 'name': 'Building 53', 'sqft': 99845}]}\n"

@pytest.fixture 
def mock_api_query_resp():
    return {
        "count": 1,
        "next": None,
        "prev": None,
        "records": [
        {
        "_id": "60c9f1ca1523ad0019b3e1ea",
        "address": "478 Paerdegat Avenue, Harleigh, NJ, 3509",
        "agency": "C",
        "energy_records": [
        {
        "energy_type": "Natural Gas",
        "timestamp": "2016-01-07T10:51:13",
        "usage": 7358.8844
        },
        {
        "energy_type": "Elec",
        "timestamp": "2018-06-21T07:00:04",
        "usage": 7141.961
        },
        {
        "energy_type": "Elec",
        "timestamp": "2018-03-24T05:14:10",
        "usage": 8885.2922
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2016-12-26T03:11:49",
        "usage": 8620.2933
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2018-05-26T01:35:33",
        "usage": 7573.4968
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2018-06-06T01:37:38",
        "usage": 762.6639
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2019-03-14T05:53:45",
        "usage": 2515.4551
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2017-08-19T04:23:05",
        "usage": 7431.0259
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2020-03-18T01:49:06",
        "usage": 2708.0284
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2015-10-22T09:07:29",
        "usage": 3728.0924
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2020-05-14T01:12:38",
        "usage": 7302.5535
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2017-10-15T11:00:56",
        "usage": 4392.6329
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2014-05-04T02:16:07",
        "usage": 2830.231
        },
        {
        "energy_type": "Elec",
        "timestamp": "2019-09-09T01:39:37",
        "usage": 8048.4141
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2021-04-02T04:45:05",
        "usage": 9705.1008
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2015-06-23T08:51:27",
        "usage": 8113.9583
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2015-10-05T07:53:42",
        "usage": 5480.2403
        },
        {
        "energy_type": "Elec",
        "timestamp": "2016-10-10T09:20:20",
        "usage": 2418.9261
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2018-08-10T07:56:28",
        "usage": 7111.8323
        },
        {
        "energy_type": "Elec",
        "timestamp": "2014-04-06T11:00:03",
        "usage": 5162.9635
        },
        {
        "energy_type": "Elec",
        "timestamp": "2016-10-06T07:09:33",
        "usage": 6731.7939
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2016-08-31T04:27:02",
        "usage": 5046.0807
        },
        {
        "energy_type": "Elec",
        "timestamp": "2014-08-23T01:59:57",
        "usage": 3857.1683
        },
        {
        "energy_type": "Elec",
        "timestamp": "2019-03-12T01:02:13",
        "usage": 1300.258
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2018-06-27T10:05:49",
        "usage": 6345.6723
        },
        {
        "energy_type": "Elec",
        "timestamp": "2014-02-24T02:57:33",
        "usage": 9505.0717
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2015-12-04T12:25:48",
        "usage": 3988.7097
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2015-12-14T04:40:49",
        "usage": 7465.9599
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2018-03-17T06:46:47",
        "usage": 3691.843
        },
        {
        "energy_type": "Elec",
        "timestamp": "2015-06-18T08:11:43",
        "usage": 9410.188
        },
        {
        "energy_type": "Elec",
        "timestamp": "2020-08-16T12:28:07",
        "usage": 9812.0667
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2017-06-03T03:05:05",
        "usage": 5456.4932
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2014-09-28T05:23:13",
        "usage": 6614.7938
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2014-12-03T09:42:36",
        "usage": 4979.3078
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2016-01-16T10:26:09",
        "usage": 7031.9336
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2017-08-28T09:28:30",
        "usage": 8939.3649
        },
        {
        "energy_type": "Elec",
        "timestamp": "2017-01-28T08:48:15",
        "usage": 9054.1227
        },
        {
        "energy_type": "Elec",
        "timestamp": "2017-07-30T10:09:55",
        "usage": 4187.2217
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2017-01-17T10:25:13",
        "usage": 5800.2348
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2017-09-04T07:19:39",
        "usage": 4236.456
        },
        {
        "energy_type": "Elec",
        "timestamp": "2017-06-27T07:44:54",
        "usage": 6825.5506
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2015-08-07T08:08:42",
        "usage": 7662.4075
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2020-12-09T09:49:20",
        "usage": 1917.2752
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2014-10-14T11:46:06",
        "usage": 2042.4889
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2018-09-25T08:29:57",
        "usage": 7959.4708
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2016-04-20T07:27:08",
        "usage": 6025.9754
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2018-01-27T05:49:25",
        "usage": 135.8437
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2014-07-11T07:47:12",
        "usage": 597.4012
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2020-03-25T11:22:06",
        "usage": 2825.0485
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2016-03-08T11:57:42",
        "usage": 9712.2624
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2017-10-02T11:51:51",
        "usage": 7574.82
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2015-12-03T07:10:34",
        "usage": 8729.0003
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2014-02-23T06:26:44",
        "usage": 94.1893
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2014-06-25T02:26:48",
        "usage": 2588.069
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2016-09-02T10:41:44",
        "usage": 2154.1154
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2017-10-08T09:41:15",
        "usage": 4301.6452
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2014-03-13T01:03:10",
        "usage": 2340.898
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2016-08-01T08:19:33",
        "usage": 5654.9013
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2020-03-09T08:29:19",
        "usage": 5947.3199
        },
        {
        "energy_type": "Elec",
        "timestamp": "2016-09-28T06:51:34",
        "usage": 8029.0753
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2017-06-30T10:45:44",
        "usage": 3076.7409
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2018-04-29T01:50:41",
        "usage": 6602.904
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2017-07-03T04:46:25",
        "usage": 465.4762
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2017-12-25T09:09:08",
        "usage": 3194.1279
        },
        {
        "energy_type": "Elec",
        "timestamp": "2017-03-06T01:18:31",
        "usage": 4930.9698
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2021-01-25T06:22:03",
        "usage": 9869.7403
        },
        {
        "energy_type": "Elec",
        "timestamp": "2016-08-15T12:24:56",
        "usage": 9535.4434
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2015-04-29T07:33:33",
        "usage": 3541.3133
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2019-12-01T03:00:25",
        "usage": 748.1279
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2018-03-18T08:58:48",
        "usage": 4509.5196
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2014-10-28T09:14:36",
        "usage": 7781.8183
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2018-10-22T06:09:11",
        "usage": 1969.1386
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2020-10-02T07:04:32",
        "usage": 3104.7082
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2014-09-09T10:27:35",
        "usage": 994.7858
        },
        {
        "energy_type": "Elec",
        "timestamp": "2016-05-26T10:03:50",
        "usage": 3556.7048
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2020-05-29T06:55:46",
        "usage": 1830.3231
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2014-07-23T05:50:03",
        "usage": 766.8076
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2015-11-14T05:59:44",
        "usage": 275.1859
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2020-07-28T10:13:12",
        "usage": 7863.3973
        },
        {
        "energy_type": "Elec",
        "timestamp": "2018-06-18T11:58:24",
        "usage": 224.4168
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2015-04-03T08:56:40",
        "usage": 9504.856
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2016-11-01T08:43:58",
        "usage": 505.2644
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2015-01-14T03:55:54",
        "usage": 5791.625
        },
        {
        "energy_type": "Elec",
        "timestamp": "2018-10-28T06:11:07",
        "usage": 2867.013
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2017-03-07T08:23:35",
        "usage": 2014.6833
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2014-04-18T10:16:40",
        "usage": 7441.8896
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2020-01-30T12:07:35",
        "usage": 3494.9479
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2014-10-31T07:00:11",
        "usage": 3986.7218
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2017-07-05T06:00:03",
        "usage": 1240.7878
        },
        {
        "energy_type": "Elec",
        "timestamp": "2017-08-13T06:30:58",
        "usage": 8184.3049
        },
        {
        "energy_type": "Elec",
        "timestamp": "2020-07-19T02:16:12",
        "usage": 9540.8539
        },
        {
        "energy_type": "Fuel Oil",
        "timestamp": "2019-06-15T01:34:41",
        "usage": 3644.0314
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2015-02-08T04:45:50",
        "usage": 6726.8348
        },
        {
        "energy_type": "Natural Gas",
        "timestamp": "2021-02-25T01:04:15",
        "usage": 9111.8212
        },
        {
        "energy_type": "Elec",
        "timestamp": "2020-09-29T10:21:19",
        "usage": 1956.6999
        },
        {
        "energy_type": "Elec",
        "timestamp": "2016-10-22T02:34:39",
        "usage": 4584.6083
        },
        {
        "energy_type": "Elec",
        "timestamp": "2014-01-07T03:20:22",
        "usage": 5092.2879
        }
        ],
        "facility_id": 53,
        "latitude": -6.00756,
        "longitude": 62.618959,
        "name": "Building 53",
        "sqft": 99845
        }
        ]
    }