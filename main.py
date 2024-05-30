from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import pandas as pd
from pcap_handler import *
from scapy.utils import rdpcap
from packet_filter import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #TODO: лена и соня - здесь кодьте главное окно


    def open_pcap(self, filename):
        pcap2df = pcapHandler(file=filename, verbose=True)
        df = pcap2df.to_DF(head=True)
        scapy_capture = rdpcap(filename)
        return df, scapy_capture

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

