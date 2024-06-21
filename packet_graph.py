import pandas as pd
import matplotlib.pyplot as plt
from read_pcap import open_pcap
import time
def plot_packet_length_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['len'], bins=50, color='purple', alpha=0.7)
    plt.title('Распределение длин пакетов')
    plt.xlabel('Длина пакета')
    plt.ylabel('Количество пакетов')
    plt.grid(True)
    plt.show()


def plot_traffic_over_time(df):
    plt.figure(figsize=(10, 6))
    pattern = '%d/%m/%y, %I:%M:%S %p'
    df['time'] = df['time'].apply(lambda x : int(time.mktime(time.strptime(x, pattern))))
    plt.plot(pd.to_datetime(df['time'], unit='s'), df['len'], color='red')
    plt.title('Трафик с течением времени')
    plt.xlabel('Время')
    plt.ylabel('Длина пакета')
    plt.grid(True)
    plt.show()

def plot_addresses_sending_payloads(df):
    plt.figure(figsize=(15, 8))
    payload_by_src = df.groupby('src')['payload'].sum()
    payload_by_src = payload_by_src.sort_values(ascending=False)
    plt.bar(payload_by_src.index, payload_by_src.values, color='yellow', alpha=0.7)
    plt.title('Адреса, по которым отправляется полезная нагрузка')
    plt.xlabel('Исходный IP-адрес')
    plt.ylabel('Полезная нагрузка')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.show()

def plot_destination_addresses(df):
    plt.figure(figsize=(15, 8))
    payload_by_dst = df.groupby('dst')['payload'].sum()
    payload_by_dst = payload_by_dst.sort_values(ascending=False)
    plt.bar(payload_by_dst.index, payload_by_dst.values, color='brown', alpha=0.7)
    plt.title('Целевые адреса')
    plt.xlabel('Целевой IP-адрес')
    plt.ylabel('Полезная нагрузка')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    file_path = "./pcaps/http-fault-post.pcap"
    df = open_pcap(file_path)

    plot_packet_length_distribution(df)
    plot_traffic_over_time(df)
    plot_addresses_sending_payloads(df)
    plot_destination_addresses(df)
