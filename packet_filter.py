from scapy.utils import rdpcap
from pcap_handler import *
#TODO? other filters?
filters = {"src": None, "dst":None,"sport": None,"dport": None, "proto": None,"len": None, "contains": None,}

def filter(filters, df):
    print(filters)
    #return COPY
    for col in list(filters.keys())[:-1]:
        if filters[col]:
            df = df[df[col] == filters[col]]

    if filters['contains']:
        df = df[df['payload_strings'].str.contains(filters['contains'])]

    print(df)
    return df