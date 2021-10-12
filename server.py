""" This is the fake REST API server.

To start on localhost:8080 
$ python server.py 

"""


from typing import Any, Dict, List, Optional
from flask import Flask, jsonify, request, abort
import json
import copy


from flask.helpers import make_response, url_for

app = Flask(__name__)

import os 
thisdir = os.path.dirname(__name__)
data_file = os.path.join(thisdir, 'data', 'fake-energy-data-min.json')



def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

with open(data_file, 'r') as f: 
    raw_records = json.load(f)



class RecordFilterSet(object): 
    """ On each request we use this to simulate a filtred set of chunked records
    """

    def equals(self, records, key, value):
        return [{k:v for k,v in rec.items()} for rec in records if rec[key]==value] 

    def gte(self, records, key, value): 
        return [{k:v for k,v in rec.items()} for rec in records if rec[key]>=value] 

    def lte(self, records, key, value): 
        return [{k:v for k,v in rec.items()} for rec in records if rec[key]<=value] 

    def isin(self, records, key, value): 
        return [{k:v for k,v in rec.items()} for rec in records if value in rec[key]]
        


# simple paginator... the API delivers 12 facilities at a time - 9 pages total from 
# fake-energy-data-min.json file.

class ResponseSchema(object): 

    def __init__(self, next_url=None, prev_url=None, count=0, records=None):
        self.next_url = next_url 
        self.prev_url = prev_url 
        self.count = count 
        self.records = records if records is not None else []

    def dict(self): 
        return {
            'next': self.next_url, 
            'prev': self.prev_url, 
            'count': self.count, 
            'records': self.records
        }



class DB(object): 
    """Simulates a simple paginating database. 
    """

    def __init__(self, records: List[List[Dict[str, Any]]]): 
        self.records = records 
        self.count = sum([len(r) for r in records])

    def _index(self, page_num: int=None) -> int: 
        # convert page num to index in records
        if page_num is None:
            return 0
        return page_num - 1

    def _next_url(self, idx: int=None)-> Optional[str]: 
        # next will be i + 2 unless idx == len(records)
        if idx == len(self.records) - 1: 
            return None
        return f'?page={idx+2}'


    def _prev_url(self, idx: int=None) -> Optional[str]: 
        if idx == 0:
            return None
        return f'?page={idx}'


    def page(self, base_url: str='', page_num:int=None) -> ResponseSchema:

        if len(self.records) != 1:  # if we only have 1 page of data we bypass this logic
            if page_num < 1:
                raise ValueError('Page num must be greater then or equal to 1.')
            if page_num > len(self.records):
                return ResponseSchema()

        db_index = self._index(page_num)

        next_page = self._next_url(db_index)
        prev_page = self._prev_url(db_index)
        
        next_url = base_url + next_page if next_page is not None else next_page
        prev_url = base_url + prev_page if prev_page is not None else prev_page

        records = self.records[db_index]
        
        return ResponseSchema(next_url, prev_url, self.count, records)
    

    def get_one(self, facility_id: int) -> Optional[dict]:

        for chunk in self.records:
            for r in chunk:
                if r['facility_id'] == facility_id: 
                    return r  
    

    
@app.route('/data/')
def data():

    page_num = request.args.get('page')

    # filter by these query strings and chunk here... cheeky move.   
    query_strings = [
        ('agency', 'agency', 'equals', str), 
        ('sqft_lte', 'sqft', 'lte', int), 
        ('sqft_gte', 'sqft', 'gte', int),
        ('address_contains', 'address', 'isin', str)
    ]
    
    filterset = RecordFilterSet()
    
    records = copy.deepcopy(raw_records) # we whittle down this copy within the request
    
    for param, key, op, t in query_strings: 
        val = request.args.get(param)
        if val:
            try:
                val = t(val)  # cast or handle failure... the sqft params must be able to be cast to int
            except ValueError: 
                return make_response(jsonify(detail=f'{param} must be of type {str(t)}'))
            filter_op = getattr(filterset, op)
            records = filter_op(records, key, val)
    
    if len(records) == 0: # early return if there are no records
        return ResponseSchema().dict()

    records = list(chunks(records, 12))  # hardcode page_size = 12
    
    db = DB(records)   # now we can paginate 

    try:
        if page_num is None: 
            page_num = 1
        else: 
            page_num = int(page_num)

    except TypeError:
        return make_response(jsonify(detail="Page must be an integer."), 400)

    try:
        data = db.page(request.base_url, page_num)
        return data.dict()
        
    except ValueError as err: 
        return make_response(jsonify(detail=str(err)), 400)
    

@app.route(f'/data/<int:facility_id>')
def data_detail(facility_id): 
    
    records = list(chunks(raw_records, 12))
    
    db = DB(records)

    record = db.get_one(facility_id)

    if record is None: 
        return make_response(jsonify(detail='Not Found.'), 404)
    return record


if __name__ == '__main__': 
    app.run('0.0.0.0', 8080, debug=True)
