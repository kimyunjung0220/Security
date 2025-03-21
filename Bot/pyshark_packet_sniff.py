import pyshark
import re
import json

interface = "Input your NIC"

def trans_json(data : str) -> json:
    data_json = {}
    key = None
    object_key = None
    
    data = data.split("\n")
        
    for line in data:
        if line.startswith('Layer'):
            key = line
            data_json[key] = {}
            
        elif line.startswith('\t'):
            if "=" in line:
                end = line.find("=")
            else:
                end = line.find(":")
                
            start = line.find("\t") + 1
            object_key = line[start:end]
            value = line[end+1:]
            data_json[key][object_key] = value
            
    return json.dumps(data_json, indent=4)
        
def trans_data(data : str) -> str:
    ansi_escape = re.compile(r'\x1b\[[0-9;]*[mK]')
    data = re.sub(ansi_escape, '', data)
    data = data.replace("\n:", "\n")
    return data

def get_packet() -> json:
    get_sniff = pyshark.LiveCapture(interface=interface)
    for packet in get_sniff.sniff_continuously(packet_count=1):
        packet = trans_data(str(packet))
        packet = trans_json(packet)
        return packet
