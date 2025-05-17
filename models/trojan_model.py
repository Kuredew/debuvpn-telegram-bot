class Trojan:
    def __init__(self, username, id, host):
        self.username = username
        self.id = id
        self.host = host

    def get_non_tls(self):
        return '-'
    
    def get_tls(self):
        template = f'{self.id}@{self.host}:443?security=tls&sni={self.host}&type=ws&host={self.host}&path=%2Fwhatever%2Fvless#{self.username + " WS TLS DebuVPN"}'
        return 'trojan://' + template
    
    def get_grpc(self):
        template = f'{self.id}@{self.host}:443?security=tls&sni=&type=grpc&host={self.host}&serviceName=vless-grpc#{self.username + " GRPC DebuVPN"}'
        return 'trojan://' + template