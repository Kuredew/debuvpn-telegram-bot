import base64

def encode(string):
    return base64.b64encode(str(string).encode('ascii')).decode('ascii')