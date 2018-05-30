from QYTVC import get_networks,get_token

from cred import * #导入username,password,vcip(vcenter ip地址)

def get_network_id():
    token = get_token(vcip,username,password)

    result = get_networks(vcip,token)

    vlanid = []

    for x in result['value']:
        if 'VLAN' in x['name']:
            vlanid.append(int(x['name'].replace('VLAN','')))

    return  vlanid


if __name__ == "__main__":
    print(get_network_id())