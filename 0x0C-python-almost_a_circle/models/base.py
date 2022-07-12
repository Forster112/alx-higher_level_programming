import json
import csv
import turtle
class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
    
    def to_json_string(list_dictionaries):
        if list_dictionaries == None or len(list_dictionaries) == 0:
            return "[]"
        else:
            ret = json.dumps(list_dictionaries)
            return ret
    
    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))
