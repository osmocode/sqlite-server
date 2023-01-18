from sqlite_server.client import SQLiteClient

if __name__ == '__main__':
    
    server = SQLiteClient('sqlite-server')
    server.connect()
    server.request('activity/slug-1', 'add', x = 1, y = 2)

    
