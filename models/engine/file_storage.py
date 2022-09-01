#!/usr/bin/python3
""" Defines FileStorage class """
import json


class FileStorage:
    """Represent FileStorage.

    Serializes classs instances to a JSON file and 
    Deserializes JSON file to class instances
    """
    
    __file_path = 'file.json'
    __objects = {}
    
    # def __init__(self):
    #     """initializes a new storage class"""
        
    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
        
    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for k, v in self.__objects.items():
                dict_storage[k] = v.to_dict()
            json.dump(dict_storage, f)
        
    def reload(self):
        """
        Deserializes the JSON file to __objects
        -> Only IF it exists!
        """
        try:
            with open(self.__file_path) as f:
                return json.load(f)
        except FileNotFoundError:
            return