import paramiko


def sshclient_execmd(hostname, port, username, password, execmd):
    paramiko.util.log_to_file("paramiko.log")

    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    s.connect(hostname=hostname, port=port, username=username, password=password)
    stdin, stdout, stderr = s.exec_command(execmd)

    result = stdout.read().decode()

    s.close()

    # PortGroup_List = result.split('\n')[2:-1]
    # # print(VLAN_List)
    #
    # VLAN_List = []
    #
    # for x in PortGroup_List:
    #     if "VLAN" in x.split()[0]:
    #         VLAN_List.append(int(x.split()[0].replace('VLAN',"")))
    # return VLAN_List

from random import randint
vm_name_no = randint(1,100)

if __name__ == "__main__":

    hostname = "172.16.1.201"
    port = 22
    username = "root"
    password = "Cisc0123"
    VLAN_ID = str(vm_name_no)
    execmd = "esxcli network vswitch standard portgroup add -p VLAN"+VLAN_ID+"-v vSwitch1"
    #execmd = 'esxcli network vswitch standard portgroup list '

    sshclient_execmd(hostname, port, username, password, execmd)

    # VLAN_LIST = (sshclient_execmd(hostname, port, username, password, execmd))
    # print(VLAN_LIST)
