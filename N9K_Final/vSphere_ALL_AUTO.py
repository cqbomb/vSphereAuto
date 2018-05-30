from Clone_VM import clone_vm_from_no
from Create_PortGroup import create_pg
from GET_VM import get_vm_id
from GET_PortGroup import get_network_id
from EDIT_PortGroup import edit_nic
from random import randint
from Edit_PortGroup_VlanID import edit_pg_vlan_id
from N9K_ALL_AUTO import N9K_ALL_AUTO

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
    print('创建端口组VLAN' + str(VLANID) + '...')
    create_pg(VLANID)

    print('创建虚拟机CentOS_'+str(VLANID)+'...')
    clone_vm_from_no(VLANID,temp_no)

    print('创建主机网络适配器，并且关联端口组...')
    edit_nic(VLANID)

    print('编辑端口组VLAN ID - '+str(VLANID)+'...')
    edit_pg_vlan_id(VLANID)

    print('='*100)
    print('开始配置N9K网络:')
    N9K_ALL_AUTO(VLANID)

    print('=' * 100)
    print('完成vSphere自动化任务！-')
    # return VLANID


Choose_VM_Banner = """ 1. OS: CentOS ; CPU: 1 ; RAM: 1
 2. OS: CentOS ; CPU: 1 ; RAM: 2
 3. OS: CentOS ; CPU: 2 ; RAM: 1
 4. OS: CentOS ; CPU: 2 ; RAM: 2
 Please select the Virtual Machine Template you want to create (1-4)"""

if __name__ == "__main__":
    Choose_VM_No = input(Choose_VM_Banner+":")
    print(vsphere_all_auto(int(Choose_VM_No)))



