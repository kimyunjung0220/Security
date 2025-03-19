from scapy.all import get_if_list

def find_interface():
    interfaces = get_if_list()
    for interface in interfaces:
        if interface.startswith('eth') or interface.startswith('ens'):
            return interface
