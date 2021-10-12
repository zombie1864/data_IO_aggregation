"""Function wrappers around the requests package for use with the fake energy data server. 
While this might seem trivial for this particular app, one element of good 
application design is to isolate the different pieces of business logic so that 
the code becomes more testable. 
This becomes especially true for I/O bounded code since typically we do not 
want to reach out over the internet during unit testing. We do this using `pytest-mock` a 
wrapper around the `mock` API provided by python. 
NOTE that for the paginator I am asking you to implement a generator. This is a more advanced 
python language construct that allows us to yield values rather then return them in one go. This
technique is used to solve numerous problems. For our case we want to provide a simple function that will 
essentially work in a for loop (like range). 
"""


from typing import Any, Dict, Generator, Tuple
import requests
import time


def fetch(url: str, raise_for_status: bool=True, **query_params) -> Tuple[int, Dict[str, Any]]:
    """Fetches data using the requests API from the specified url. Raises a 
    requests.HTTPError for status codes above if raise_for_status is set to True. 

    Args:
        url (str, optional): The request url.
        raise_for_status(bool, optional): Whether to raise on an error code. Defaults to True. 
        **query_params (optional): Optional key word args to support to query the database.

    Raises:
        requests.HTTPError: if raise_for_status is set to true.

    Returns:
        Tuple[int, Dict[str, Any]]: A tuple of status code followed by the data.
    """
    # HINT carefully read the requests documentation to figure out the cleanest way to raise a requests error.
    #query_params is a dict, **query_params is keyword arg 
    res_obj = requests.get(url, params=query_params)
    if raise_for_status:# default to True 
        res_obj.raise_for_status()# if 200 result is None "All is well"
    return (res_obj.status_code, res_obj.json()) # returns code and dict 


def paginator(url: str, timeout: int=0.1, **kwargs) -> Generator[Tuple[int, Dict[str, Any]], None, None]: 
    """A simple paginator that will iterate through all the data in our API list view. It will yield a new chunk of 
    data from the API each iteration. After each call the thread will `sleep` for a short amount of time. This is 
    an important feature to working with APIs as many will throttle you if you hit it with too many requests in too short an 
    amount of time.
    As mentioned above this should be implemented as a generator.
    ex. 
    >>> for status, data in paginator(url, timeout=0.25, foo=bar, baz=bip):
            print(status, data) # <-- this yields one status, page using the filter **params
    Args:
        url (str, optional): The url.
        timeout (int, optional): A timeout parameter in between paginating calls. 
        **kwargs (optional): Optional keyword args that get forwarded to requests.
    Yields:
        Generator[Tuple[int, Dict[str, Any]]]: Yields a tuple of status code and dictionary.
    """
    while True:
        status, data = fetch(url, **kwargs) 
        yield status, data 
        next_url = data['next']
        if next_url is None: 
            break 
        else:
            url = next_url         
        time.sleep(timeout)
'''  
    old solution:
        status, data = fetch(url, **kwargs) 
        yield status, data # yields curr_page 
        if data['next'] == None:
            break 
        next_page_value_num = int(data['next'][-1]) #page=x 
        query_str = requests.get(url, params=kwargs).url
        symbol = '&' if kwargs else '?'
        status, data = fetch(query_str+f'{symbol}page={next_page_value_num}',**kwargs)
        next_page_value_num += 1 
        time.sleep(timeout)
'''

''' 
    suppose that you are fetching thousands of records from a db 
    you might want to process something 
    all the thousands of records will be loaded into memoery 
        ⮑ like return which will return everything 
            ⮑ this is bad - you will not want that b/c it can eatup your memory 
'''        

