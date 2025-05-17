class SSH:
    def __init__(self, username, password, host):
        self.username = username
        self.password = password
        self.host = host

    def get_ws_payload(self):
        return f'GET / HTTP/1.1[crlf]Host: {self.host}[crlf]Upgrade: Websocket[crlf]Connection: Keep-Alive[crlf][crlf]'