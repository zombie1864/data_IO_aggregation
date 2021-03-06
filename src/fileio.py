import pydantic
import abc 
import pathlib
import json 
import csv 
from typing import List, Type, TypeVar


TPydanticModel = TypeVar('TPydanticModel', bound=pydantic.BaseModel)


class PydanticReader(abc.ABC): 

    @abc.abstractmethod
    def read(self, filepath: pathlib.Path, model_class: Type[TPydanticModel]) -> List[TPydanticModel]: 
        """Given a valid pathlib.Path and a pydantic model class, read in a file and return a list of pydantic model instances 
        of the given type.

        Args:
            filepath (pathlib.Path): path to some file 
            model_class (TPydanticModel): A subclass of pydantic.BaseModel

        Returns:
            List[TPydanticModel]: Returns instances of the given subclass
        """
        pass 



class PydanticWriter(abc.ABC): 

    @abc.abstractmethod
    def write(self, data: List[TPydanticModel], filepath: pathlib.Path) -> None:
        """Given some data as a list of PydanticModels, writes to a file. 

        Args:
            data (List[TPydanticModel]): A list of pydantic models to write 
            filepath (pathlib.Path): The filepath to write to.
        """
        pass



class JsonReader(PydanticReader):
    ''' 
    class with read from memory interface. Supplied with valid filepath and model class returns a list of class object of desired model class 
    ex List[<class 'FakeEnergyFacilityModel'>]
    '''
    def read(self, filepath: pathlib.Path, model_class: Type[TPydanticModel]) -> List[TPydanticModel]:
        """Given a valid pathlib.Path and a pydantic model class, read in a file and return a list of pydantic model instances 
        of the given type.

        Args:
            filepath (pathlib.Path): path to some file 
            model_class (TPydanticModel): A subclass of pydantic.BaseModel

        Returns:
            List[TPydanticModel]: Returns instances of the given subclass
        """
        with open(filepath) as json_file: 
            list_of_dict_data = json.load(json_file) # convert to dict
            list_of_inst_models = [model_class(**{key: value for key, value in dict_obj.items()}) for dict_obj in list_of_dict_data]
        return list_of_inst_models 


class JsonWriter(PydanticWriter):
    def write(self, data: List[TPydanticModel], filepath: pathlib.Path) -> None:
        """Given some data as a list of PydanticModels, writes to a file. 

        Args:
            data (List[TPydanticModel]): A list of pydantic models to write 
            filepath (pathlib.Path): The filepath to write to.
        """
        list_of_json = [model_obj.json() for model_obj in data]#converts pydantic models
        with open(filepath, 'w') as f:  
            joined_str = ','.join(list_of_json)
            f.write(f'[{joined_str}]')  


class CsvReader(PydanticReader):
    def read(self, filepath: pathlib.Path, model_class: Type[TPydanticModel]) -> List[TPydanticModel]:
        """Given a valid pathlib.Path and a pydantic model class, read in a file and return a list of pydantic model instances 
        of the given type.

        Args:
            filepath (pathlib.Path): path to some file 
            model_class (TPydanticModel): A subclass of pydantic.BaseModel

        Returns:
            List[TPydanticModel]: Returns instances of the given subclass
        """
        with open(filepath, newline='') as file: 
            reader = csv.DictReader(file) # converts headers and rows to dict
            list_of_inst_models = [model_class(**dict_obj) for dict_obj in reader] 
        return list_of_inst_models 



class CsvWriter(PydanticWriter):
    def write(self, data: List[TPydanticModel], filepath: pathlib.Path) -> None:
        """Given some data as a list of PydanticModels, writes to a file. 

        Args:
            data (List[TPydanticModel]): A list of pydantic models to write 
            filepath (pathlib.Path): The filepath to write to.
        """
        with open(filepath,'w') as new_csv_file:
            headers = []
            for model_obj in data:
                for key in model_obj.dict().keys():
                    if key not in headers:
                        headers.append(key) 
            csv_writer = csv.DictWriter(new_csv_file, fieldnames=headers) 
            csv_writer.writeheader()
            list_of_py_dict = [ model_obj.dict() for model_obj in data ]
            csv_writer.writerows(list_of_py_dict)
            '''  
                - .writerow(data): writes a single row of data and returns the number of characters written. 
                - .writerows(data): writes multiple rows of data and returns None
            ''' 