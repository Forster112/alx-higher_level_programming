import json
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
        with open(cls.__class__.__name__, "w", encoding="utf-8") as f:
            if list_objs is None:
                return f.write("[]")
            else:
                return f.write(Base.to_json_string(list_objs))
