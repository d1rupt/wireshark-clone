import binascii
import json
import time

import pandas as pd
from scapy.layers.inet import IP, TCP, UDP
from scapy.utils import rdpcap


def open_pcap(filename):
    packets = rdpcap(filename)
    data = []
    ip_fields = [field.name for field in IP().fields_desc]
    tcp_fields = [field.name for field in TCP().fields_desc]
    udp_fields = [field.name for field in UDP().fields_desc]
    dataframe_fields = ip_fields + ['time'] + tcp_fields + ['payload', 'payload_raw', 'payload_hex', 'payload_strings']
    df = pd.DataFrame(columns=dataframe_fields)
    with open("./data/ip-protocol-numbers.json", 'r') as f:
        protocol_names = json.load(f)
    for packet in packets[IP]:
        field_vals = []
        for field in ip_fields:
            if field == 'options':
                field_vals.append(len(packet[IP].fields[field]))
            else:
                field_vals.append(packet[IP].fields[field])

        # print(time.strftime('%A, %d/%m/%y, %I:%M:%S %p', int(time.localtime(packet.time))))
        field_vals.append(time.strftime('%d/%m/%y, %I:%M:%S %p', time.localtime(int(packet.time))))
        layer_type = type(packet[IP].payload)
        for field in tcp_fields:
            try:
                if field == 'options':
                    field_vals.append(len(packet[layer_type].fields[field]))
                else:
                    field_vals.append(packet[layer_type].fields[field])
            except:
                field_vals.append(None)
        field_vals.append(len(packet[layer_type].payload))
        field_vals.append(packet[layer_type].payload.original)
        field_vals.append(binascii.hexlify(packet[layer_type].payload.original))
        payload = packet[layer_type].payload.original
        payload = [chr(x) for x in payload if (x in range(32, 126) or x == 10 or x == 13)]
        print(payload)
        payload = ''.join(payload)
        field_vals.append(payload)
        # Add row to DF
        df_append = pd.DataFrame([field_vals], columns=dataframe_fields)
        df = pd.concat([df, df_append], axis=0)
    df = df.reset_index()
    df = df.drop(
        ["version", "index", "ihl", "tos", "frag", "seq", "ack", "dataofs", "reserved", "flags", "window", "urgptr",
         "options", "id", "ttl", "chksum"], axis=1)
    df["proto"] = df["proto"].apply(lambda x: protocol_names[str(x)]["keyword"])
    return df