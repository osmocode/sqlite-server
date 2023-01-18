from dataclasses import dataclass, field
from typing import Any
from .exceptions import *
import Pyro5.client


@dataclass
class SQLiteClient:

    name: str
    host: str = field(default='localhost')
    port: int = field(default=4242)
    remote: Pyro5.client.Proxy = field(default=None)

    def connect(self):
        if self.remote != None:
            raise ProxyIllegalStateException('Connection already exist...')
        self.remote = Pyro5.client.Proxy(f'PYRO:{self.name}@{self.host}:{self.port}')
    
    def request(self, uri: str, method: str, **kwargs) -> Any:
        if self.remote == None:
            raise ProxyIllegalStateException('Any connection with proxy...')
        self.remote.request(uri, method, kwargs=kwargs)