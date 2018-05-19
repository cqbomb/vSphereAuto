from Clone_VM import clone_vm_from_no
from Create_PortGroup import create_pg
from GET_VM import get_vm_id
from GET_PortGroup import get_network_id
from EDIT_PortGroup import edit_nic
from random import randint
from time import sleep

def vsphere_all_auto(temp_no):
    while True:
        VLANID = randint(1,100)
        VMID = get_vm_id()
        NETID = get_network_id()
        if VLANID in VMID:
            continue
        if VLANID in NETID:
            continue
        break
    print('创建虚拟机CentOS_'+str(VLANID)+'...')
    clone_vm_from_no(VLANID,temp_no)
    print('创建端口组VLAN' + str(VLANID) + '...')
    create_pg(VLANID)
    print('创建主机网络适配器，并且关联端口组...')
    sleep(5)
    edit_nic(VLANID)
    print('完成vSphere自动化任务！+')
    return VLANID

if __name__ == '__main__':
    print(vsphere_all_auto(4))



