from scapy.utils import rdpcap
from pcap_handler import *
#TODO? other filters?
filters = {"protocol": None, "ip_src": None, "ip_dst": None,  "size": None, "port": None, "contains": None, }


def open_pcap(filename):
    pcap2df = pcapHandler(file=filename, verbose=True)
    df = pcap2df.to_DF(head=True)
    scapy_packets = rdpcap(filename)
    return df, scapy_packets
def filter(filters, df):
    #return COPY
    pass