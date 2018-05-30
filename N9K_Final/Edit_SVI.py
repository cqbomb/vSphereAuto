import requests
import json

my_headers = {'content-type': 'application/json-rpc'}

username = "admin"
password = "Cisc0123"
nxos3_ip = str('192.168.1.103')
# nxos1_ip = str('192.168.1.101')
# vlanId = str('67')

url = "http://"+ nxos3_ip +"/ins"



def nxos3_configure_svi(VLANID):
    SVIipadd = '172.100.' + str(VLANID) + '.1'

    print('VLAN ' + str(VLANID) + ' SVI ip address is: '+ SVIipadd)

    payload=[
        {"jsonrpc": "2.0","method": "cli","params": {"cmd": "conf t","version": 1},"id": 1},
        {"jsonrpc": "2.0","method": "cli","params": {"cmd": "interface vlan "+str(VLANID),"version": 1},"id": 2},
        {"jsonrpc": "2.0","method": "cli","params": {"cmd": "ip address "+str(SVIipadd)+"/24","version": 1},"id": 3},
        {"jsonrpc": "2.0","method": "cli","params": {"cmd": "no shut","version": 1},"id": 4},
    ]

    response = requests.post(url,data=json.dumps(payload), headers=my_headers,auth=(username,password)).json()


if __name__ == '__main__':
    nxos3_configure_svi(22)