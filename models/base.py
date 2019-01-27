import json
from operator import attrgetter


class Jsonable:
    @classmethod
    def from_json(cls, json_string):
        obj = cls()
        obj.__dict__ = json.loads(json_string)
        return obj

    @classmethod
    def from_json_obj(cls, json_obj):
        obj = cls()
        obj.__dict__ = json_obj
        return obj

    def to_json(self):
        return json.dumps(self, default=attrgetter('__dict__'), sort_keys=True)
