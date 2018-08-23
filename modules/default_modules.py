import base64
import json

from models.packets import Packet
from .module import BaseModule, BasePreModule, processing_method, BasePostModule


class SendAsJSONModule(BaseModule):
    def __init__(self):
        super().__init__()

    def on_send(self, data):
        super().on_send(data)
        return data.to_json().encode('utf8')

    def on_receive(self, data, sock):
        super().on_receive(data, sock)
        return Packet.from_json_obj(json.loads(data))

    def disable(self):
        super().disable()
        self.enabled = True


class Base64EncodeModule(BasePreModule):
    def __init__(self):
        super().__init__()

    @processing_method
    def on_receive(self, data, sock):
        super().on_receive(data, sock)
        if data.message and data.message.text:
            data.message.text = base64.b64decode(data.message.text.encode()).decode()
        return data

    @processing_method
    def on_send(self, data):
        super().on_send(data)
        if data.message and data.message.text:
            data.message.text = base64.b64encode(data.message.text.encode()).decode()
        return data


class Base64SendModule(BasePostModule):
    def __init__(self):
        super().__init__()

    @processing_method
    def on_receive(self, data, sock):
        super().on_receive(data, sock)
        data = base64.b64decode(data)
        return data

    @processing_method
    def on_send(self, data):
        super().on_send(data)
        data = base64.b64encode(data)
        return data
