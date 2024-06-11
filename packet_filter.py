from scapy.utils import rdpcap
from pcap_handler import *
#TODO? other filters?
filters = {"protocol": None, "ip_src": None, "ip_dst": None,  "size": None, "port": None, "contains": None, }

def filter(filters, df):
    #return COPY
    pass