import requests
import json

my_headers = {'content-type': 'application/json-rpc'}

username = "admin"
password = "Cisc0123"
nxos3_ip = str('192.168.1.103')
nxos1_ip = str('192.168.1.101')
# VLANid = str('67')

# url = "http://"+ ip +"/ins"

def nxos1_configure_vlan(VLANid):
    url = "http://" + nxos1_ip + "/ins"

    payload = [
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "conf t", "version": 1}, "id": 1},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "vlan " + str(VLANid), "version": 1}, "id": 2},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "exit", "version": 1}, "id": 3}
    ]

    response = requests.post(url, data=json.dumps(payload), headers=my_headers, auth=(username, password)).json()


def nxos3_configure_vlan(VLANid):
    url = "http://" + nxos3_ip + "/ins"

    payload = [
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "conf t", "version": 1}, "id": 1},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "vlan " + str(VLANid), "version": 1}, "id": 2},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "exit", "version": 1}, "id": 3}
    ]

    response = requests.post(url, data=json.dumps(payload), headers=my_headers, auth=(username, password)).json()


def nxos1_vlan_lists():
    url = "http://" + nxos1_ip + "/ins"
    payload = [
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "show vlan brief", "version": 1}, "id": 1}
    ]
    response = requests.post(url, data=json.dumps(payload), headers=my_headers, auth=(username, password)).json()
    vlan_table = response['result']['body']['TABLE_vlanbriefxbrief']['ROW_vlanbriefxbrief']

    vlanlists = []

    for x in vlan_table:
        vlanlists.append(int(x['vlanshowbr-vlanid-utf']))

    return vlanlists


def nxos3_vlan_lists():
    url = "http://" + nxos3_ip + "/ins"
    payload = [
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "show vlan brief", "version": 1}, "id": 1}
    ]
    response = requests.post(url, data=json.dumps(payload), headers=my_headers, auth=(username, password)).json()
    vlan_table = response['result']['body']['TABLE_vlanbriefxbrief']['ROW_vlanbriefxbrief']

    vlanlists = []

    for x in vlan_table:
        vlanlists.append(int(x['vlanshowbr-vlanid-utf']))

    return vlanlists

if __name__ == "__main__":
    print('NXOS1 VLAN Lists:',nxos1_vlan_lists())
    print('NXOS3 VLAN Lists:',nxos3_vlan_lists())
    # nxos1_configure_vlan(67)
    # nxos3_configure_vlan(67)
    # print('NXOS1 VLAN Lists:',nxos1_vlan_lists())
    # print('NXOS3 VLAN Lists:',nxos3_vlan_lists())