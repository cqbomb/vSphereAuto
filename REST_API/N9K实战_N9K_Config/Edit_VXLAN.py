import requests
import json

my_headers = {'content-type': 'application/json-rpc'}

username = "admin"
password = "Cisc0123"
nxos1_ip = str('192.168.1.101')
nxos3_ip = str('192.168.1.103')
nxos1_url = "http://" + nxos1_ip + "/ins"
nxos3_url = "http://" + nxos3_ip + "/ins"

def nxos1_configure_vxlan(VLANID):
    url = "http://" + nxos1_ip + "/ins"

    VXLANID = '100' + str(VLANID)
    print(VXLANID)

    payload = [
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "conf t", "version": 1}, "id": 1},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "vlan " + str(VLANID), "version": 1}, "id": 2},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "vn-segment " + str(VXLANID), "version": 1}, "id": 3},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "interface nve 1", "version": 1}, "id": 4},
        {"jsonrpc": "2.0", "method": "cli",
         "params": {"cmd": "member vni " + str(VXLANID) + ' mcast-group 225.0.0.120', "version": 1}, "id": 5},
    ]

    response = requests.post(url, data=json.dumps(payload), headers=my_headers, auth=(username, password)).json()

def nxos3_configure_vxlan(VLANID):
    url = "http://" + nxos3_ip + "/ins"

    VXLANID = '100' + str(VLANID)
    print(VXLANID)

    payload = [
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "conf t", "version": 1}, "id": 1},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "vlan " + str(VLANID), "version": 1}, "id": 2},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "vn-segment " + str(VXLANID), "version": 1}, "id": 3},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "interface nve 1", "version": 1}, "id": 4},
        {"jsonrpc": "2.0", "method": "cli",
         "params": {"cmd": "member vni " + str(VXLANID) + " mcast-group 225.0.0.120", "version": 1}, "id": 5},
    ]

    response = requests.post(url, data=json.dumps(payload), headers=my_headers, auth=(username, password)).json()

def nxos1and3_configure_vxlan(VLANID):
    VXLANID = '100' + str(VLANID)
    print('VXLAN ID: ',VXLANID)

    payload = [
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "conf t", "version": 1}, "id": 1},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "vlan " + str(VLANID), "version": 1}, "id": 2},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "vn-segment " + str(VXLANID), "version": 1}, "id": 3},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "interface nve 1", "version": 1}, "id": 4},
        {"jsonrpc": "2.0", "method": "cli",
         "params": {"cmd": "member vni " + str(VXLANID) + " mcast-group 225.0.0.120", "version": 1}, "id": 5},
    ]

    nxos1_response = requests.post(nxos1_url, data=json.dumps(payload), headers=my_headers, auth=(username, password)).json()
    nxos3_response = requests.post(nxos3_url, data=json.dumps(payload), headers=my_headers, auth=(username, password)).json()


if __name__ == '__main__':
    # nxos1_configure_vxlan()
    # nxos3_configure_vxlan()
    nxos1and3_configure_vxlan()