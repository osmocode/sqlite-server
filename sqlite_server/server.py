from dataclasses import dataclass, field
from typing import Any
import Pyro5.server

@Pyro5.server.expose
@dataclass
class SQLiteServer:
    
    host: str = field(default='localhost')
    port: int = field(default=4242)

    def _start(self):
        print('Starting server...')
        with Pyro5.server.Daemon(self.host, self.port) as deamon:
            uri = deamon.register(self, 'sqlite-server')
            print(uri)
            deamon.requestLoop()

    def request(self, uri: str, method: str, **kwargs: dict[str, Any]):
        print(f'Request: {uri}, method: {method}')
        print(kwargs)
