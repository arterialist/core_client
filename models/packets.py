from models.actions import Action
from models.base import Jsonable
from models.messages import Message


class Packet(Jsonable):
    def __init__(self, action=None, message=None):
        self.action = action
        self.message = message

    @staticmethod
    def from_json_obj(json_obj):
        return Packet(
            action=Action.from_json_obj(
                json_obj=json_obj["action"]),
            message=Message.from_json_obj(
                json_obj=json_obj["message"]))
