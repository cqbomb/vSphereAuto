from Edit_VLAN import nxos1_configure_vlan, nxos3_configure_vlan, nxos1_vlan_lists, nxos3_vlan_lists
from Edit_SVI import nxos3_configure_svi
from Edit_VXLAN import nxos1and3_configure_vxlan
from random import randint

def N9K_ALL_AUTO(VLANID):
    while True:
        # VLANID = randint(1,100)
        NXOS1_VLAN_LISTS = nxos1_vlan_lists()
        NXOS3_VLAN_LISTS = nxos3_vlan_lists()
        if VLANID in NXOS1_VLAN_LISTS:
            continue
        if VLANID in NXOS3_VLAN_LISTS:
            continue
        break

    print('nsox1 vlan lists: ' + str(NXOS1_VLAN_LISTS))
    print('nsox3 vlan lists: ' + str(NXOS3_VLAN_LISTS))

    print('create vlan ' + str(VLANID) + ' on nsox1')
    nxos1_configure_vlan(VLANID)
    print('create vlan ' + str(VLANID) + ' on nsox3')
    nxos3_configure_vlan(VLANID)

    print('nsox1 vlan lists: ' + str(nxos1_vlan_lists()))
    print('nsox3 vlan lists: ' + str(nxos3_vlan_lists()))

    print('create vxlan on NXOS-1 adn NXOS-3')
    nxos1and3_configure_vxlan(VLANID)

    print('create vlan ' + str(VLANID) + ' SVI address'+ ' on nsox3:')
    nxos3_configure_svi(VLANID)

if __name__ == "__main__":
    N9K_ALL_AUTO()
    # print('='*50)