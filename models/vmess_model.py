from utils import base64_utils

class Vmess:
    def __init__(self, username, id, host):
        self.username = username
        self.id = id
        self.host = host

        self.template = {
            "v": "2",
            "ps": self.host,
            "add": self.host,
            "port": None,
            "id": self.id,
            "aid": "0",
            "scy": "auto",
            "net": "ws",
            "type": "none",
            "host": self.host,
            "path": "/whatever/vmess",
            "tls": None,
            "sni": None,
            "alpn": ""
        }

    def get_non_tls(self):
        template = self.template
        self.template['ps'] += ' WS NTLS DebuVPN'
        self.template['port'] = 80
        self.template['tls'] = ''
        self.template['sni'] = ''

        return 'vmess://' + base64_utils.encode(template)
    
    def get_tls(self):
        template = self.template
        self.template['ps'] += ' WS TLS DebuVPN'
        self.template['port'] = 443
        self.template['tls'] = 'tls'
        self.template['sni'] = self.host

        return 'vmess://' + base64_utils.encode(template)
    
    def get_grpc(self):
        template = self.template
        self.template['ps'] += ' GRPC DebuVPN'
        self.template['port'] = 443
        self.template['net'] = 'grpc'
        self.template['type'] = 'gun'
        self.template['path'] = 'vmess-grpc'
        self.template['tls'] = 'tls'
        self.template['sni'] = self.host

        return 'vmess://' + base64_utils.encode(template)