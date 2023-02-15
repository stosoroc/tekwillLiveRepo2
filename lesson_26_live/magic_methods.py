class Connection:
    def __init__(self, conn):
        self.connected = conn

    def __bool__(self):
        return self.connected

    def __repr__(self):
        return f'REPR: conn {"connected" if self.connected else "not connected"}'

    def __str__(self):
        return f'str: conn {"connected" if self.connected else "not connected"}'


conn = Connection(False)

if conn:
    print('I`m connected')
else:
    print('Not connected')

print(conn)
con_Str = str(conn)
print(con_Str)

con_list = [conn, conn, conn]
print(con_list)
