import pyshark
import find_interface

interface = find_interface.find_interface()
ll = []

def capp():
    cap = pyshark.LiveCapture(interface=interface)
    for packet in cap.sniff_continuously(packet_count=1):
        packet = str(packet)
        return packet
print(capp())