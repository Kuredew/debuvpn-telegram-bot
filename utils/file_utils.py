v2ray_template_file = 'templates/v2ray_transaction_template.txt'
ssh_template_file = 'templates/ssh_transaction_template.txt'

def read_v2ray_template():
    with open(v2ray_template_file, 'r', encoding='utf-8') as f:
        return str(f.read())
    
def read_ssh_template():
    with open(ssh_template_file, 'r', encoding='utf-8') as f:
        return str(f.read())