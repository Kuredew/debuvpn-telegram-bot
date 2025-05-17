class Vless:
    def __init__(self, username, id, host):
        self.username = username
        self.id = id
        self.host = host

    def get_non_tls(self):
        template = f'{self.id}@{self.host}:80?encryption=none&security=none&sni=&type=ws&host={self.host}&path=%2Fwhatever%2Fvless#{self.username + " WS NTLS DebuVPN"}'
        return 'vless://' + template
    
    def get_tls(self):
        template = f'{self.id}@{self.host}:443?encryption=none&security=tls&sni={self.host}&type=ws&host={self.host}&path=%2Fwhatever%2Fvless#{self.username + " WS TLS DebuVPN"}'
        return 'vless://' + template
    
    def get_grpc(self):
        template = f'{self.id}@{self.host}:443?encryption=none&security=tls&sni=&type=grpc&host={self.host}&serviceName=vless-grpc#{self.username + " GRPC DebuVPN"}'
        return 'vless://' + template