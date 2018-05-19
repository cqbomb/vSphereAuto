import json
#from cred import *
from urllib3 import *
from base64 import b64encode

disable_warnings()

http = PoolManager()

vcip = '172.16.1.200'
username = 'administrator@vsphere.local'
password = 'Cisc0123,,..//'

user_pass_str = username + ':' + password
user_pass_str_encode = user_pass_str.encode()
userAndPass = b64encode(user_pass_str_encode).decode("ascii")

#print(user_pass_str)
#print(user_pass_str_encode)
#print(b64encode(user_pass_str_encode))
#print(userAndPass)

authen_headers = {'Authorization' : 'Basic %s' % userAndPass}

#print(authen_headers)

def get_token(vcip,username,password):
    url = 'https://' + vcip + '/rest/com/vmware/cis/session'
    r = http.request('POST',url,headers=authen_headers)
    token = r.data.decode()
    return json.loads(token)['value']

def get_vms(vcip,token):
    headers = {'vmware-api-session-id':token}
    url = 'https://' + vcip + '/rest/vcenter/vm'
    r = http.request('GET', url, headers=headers)
    return json.loads(r.data.decode())['value']

def get_networks(vcip,token):
    headers = {'vmware-api-session-id':token}
    url = 'https://' + vcip + '/rest/vcenter/network'
    r = http.request('GET', url, headers=headers)
    return json.loads(r.data.decode())['value']

def add_vm_nic(vcip,token,vmid,network_name):
    headers = {'vmware-api-session-id':token,'Content-Type':'application/json'}
    add_nic_json = {
                        "spec": {
                                 "backing": {
                                             "type": "STANDARD_PORTGROUP",
                                             "network": network_name
                                            },
                                 "allow_guest_control": True,
                                 "mac_type": "ASSIGNED",
                                 "wake_on_lan_enabled": True,
                                 "start_connected": True,
                                 "type": "VMXNET3"
                                 }
                        }
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/hardware/ethernet'
    r = http.request('POST', url, headers=headers,body=json.dumps(add_nic_json))
    return json.loads(r.data.decode())['value']

def get_vm_nics(vcip,token,vmid):
    headers = {'vmware-api-session-id':token}
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/hardware/ethernet'
    r = http.request('GET', url, headers=headers)
    return json.loads(r.data.decode())['value']

def get_vm_nic_detail(vcip,token,vmid,nic):
    headers = {'vmware-api-session-id':token}
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/hardware/ethernet/' + nic
    r = http.request('GET', url, headers=headers)
    return json.loads(r.data.decode())['value']

def update_vm_nic(vcip,token,vmid,nic,network_name):
    headers = {'vmware-api-session-id':token,'Content-Type':'application/json'}
    update_nic_json = {
        "spec": {
            "backing": {
                "type": "STANDARD_PORTGROUP",
                "network": network_name
            },
        }
    }
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/hardware/ethernet/' + nic
    r = http.request('PATCH', url, headers=headers,body=json.dumps(update_nic_json))
    return r.data

def get_vm_power_status(vcip,token,vmid):
    headers = {'vmware-api-session-id':token}
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/power'
    r = http.request('GET', url, headers=headers)
    return json.loads(r.data.decode())['value']




if __name__ == '__main__':
    token = get_token(vcip,username,password)
    #print(token)
    print(get_vms(vcip,token))
    print(get_networks(vcip,token))
    print(add_vm_nic(vcip, token, 'vm-83', 'network-31'))
    #print(get_vm_nics(vcip,token,'vm-77'))
    #print(get_vm_nic_detail(vcip,token,'vm-77','4000'))
    #print(update_vm_nic(vcip,token,'vm-77','4000','network-68'))
    #print(get_vm_power_status(vcip,token,'vm-77'))



