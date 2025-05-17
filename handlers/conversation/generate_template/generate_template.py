from models import ssh_model, vmess_model, vless_model, trojan_model
from utils import file_utils, date_utils

def generate(data):
    account_type = data['account_type']

    expired_date = date_utils.get_date_after(int(data['expired']))

    if account_type == 'ssh':
        config = ssh_model.SSH(data['name'], data['password'], data['host'])

        ws_payload = config.get_ws_payload()

        template = file_utils.read_ssh_template().format(
            name=data['name'],
            password=data['password'],
            provider=data['provider'],
            ws_payload=ws_payload,
            expired_date=expired_date,
            max_device=data['max_device']
        )

        return template
    elif account_type == 'vmess':
        config = vmess_model.Vmess(data['name'], data['password'], data['host'])
    elif account_type == 'vless':
        config = vless_model.Vless(data['name'], data['password'], data['host'])
    elif account_type == 'trojan':
        config = trojan_model.Trojan(data['name'], data['password'], data['host'])

    non_tls = config.get_non_tls()
    tls = config.get_tls()
    grpc = config.get_grpc()

    template = file_utils.read_v2ray_template().format(
        name=data['name'],
        password=data['password'],
        provider=data['provider'],
        non_tls=non_tls,
        tls=tls,
        grpc=grpc,
        expired_date=expired_date,
        max_device=data['max_device']
    )

    return template