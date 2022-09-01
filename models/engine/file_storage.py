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
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in __objects the obj"""
        obj_class = type(obj).__name__+"."+obj.id
        FileStorage.__objects[obj_class] = obj.to_dict()
        
    # def save(self):
    #     """serializes __objects to the JSON file"""
    #     with open(FileStorage.__file_path, mode="w") as f:
    #         json.dump(FileStorage.__objects, f)
        
    # def reload(self):
    #     """deserializes the JSON file to __objects"""
    #     with open(FileStorage.__file_path) as f:
    #         return json.load(f)