import Pyro5.api
import importlib


@Pyro5.api.expose
class SQLiteServer():
    
    def __init__(self, directory: str, **kwargs) -> None:
        self.directory = directory
        self.name = kwargs.get('name', 'sqlite-server')
        self.host = kwargs.get('host', 'localhost')
        self.port = kwargs.get('port', 4242)
        with Pyro5.api.Daemon(self.host, self.port) as deamon:
            uri = deamon.register(self, self.name)
            print(f"""
SQLite Server verison 0.1.2
Starting server at: {uri}
Quit the server with CONTROL-C.
            """)
            deamon.requestLoop()

    def _start(self):
        print('Starting server...')
        with Pyro5.api.Daemon(self.host, self.port) as deamon:
            uri = deamon.register(self, self.name)
            print(uri)
            deamon.requestLoop()

    def request(self, uri: str, method: str, **kwargs):
        module_dir = self.directory.replace("/", ".")
        module_name = uri.replace("/", ".")
        try:
            module = importlib.import_module(f"{module_dir}.{module_name}")
            return getattr(module, method)(kwargs)
        except Exception:
            return f"Could not import module '{module_name}'"
