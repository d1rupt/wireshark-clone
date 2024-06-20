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
    #df['time'] = df['time'].astype(float)
    pattern = '%d/%m/%y, %I:%M:%S %p'
    df['time'] = df['time'].apply(lambda x : int(time.mktime(time.strptime(x, pattern))))
    #print(df['time'])
    plt.plot(pd.to_datetime(df['time'], unit='s'), df['len'], color='red')
    plt.title('Трафик с течением времени')
    plt.xlabel('Время')
    plt.ylabel('Длина пакета')
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    file_path = "./pcaps/http-fault-post.pcap"
    df = open_pcap(file_path)

    plot_packet_length_distribution(df)
    plot_traffic_over_time(df)