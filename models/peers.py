import hashlib
import uuid

from models.base import Jsonable


class Peer(Jsonable):
    def __init__(self, host: str, port: int, peer_id: str = None):
        self.host = host
        self.port = port
        self.peer_id = (
            peer_id if peer_id
            else hashlib.md5(str(uuid.uuid4()).encode('utf-8')).hexdigest()
        )


class Client(Peer):
    def __init__(self, host: str, port: int, nickname: str = None,
                 peer_id: str = None):
        super().__init__(host, port, peer_id)
        self.nickname = nickname

    @classmethod
    def from_peer(cls, peer: Peer, nickname: str = None):
        return cls(peer.host, peer.port, nickname, peer.peer_id)


class Server(Peer):
    def __init__(self, host: str, port: int, peer_id: str = None):
        super().__init__(host, port, peer_id)

    @classmethod
    def from_peer(cls, peer: Peer):
        return cls(peer.host, peer.port, peer.peer_id)
