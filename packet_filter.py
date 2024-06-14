from scapy.utils import rdpcap
from pcap_handler import *
#TODO? other filters?
filters = {"ip_src": None, "ip_dest":None, "port_src": None, "port_dest":None, "protocol": None, "contains": None, "size": None,}

def filter(filters, df):
    #return COPY
    pass