from typing import Any
from .exceptions import *
import Pyro5.api


class SQLiteClient():

    def __init__(self,name: str, **kwargs) -> None:
        self.name = name
        self.host = kwargs.get('host', 'localhost')
        self.port = kwargs.get('port', 4242)
        self.remote = Pyro5.api.Proxy(f'PYRO:{self.name}@{self.host}:{self.port}')
        
    def request(self, uri: str, method: str, **kwargs) -> Any:
        if self.remote == None:
            raise ProxyIllegalStateException('Any connection with proxy...')
        return self.remote.request(uri, method, **kwargs)