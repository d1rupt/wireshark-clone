import binascii
import json
import time

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import pandas as pd
from pcap_handler import *
from scapy.all import rdpcap, Packet, Raw
from scapy.layers.inet import IP, TCP, UDP

from packet_filter import *
from capture_packets import PacketCaptureWindow
from pathlib import Path
from read_pcap import open_pcap
class MainWindow(QMainWindow):
    def __init__(self, sizeHint=None):
        super().__init__()
        #TODO: лена и соня - здесь кодьте главное окно
        self.setGeometry(500, 400, 800, 600)
        self.main_widget = QWidget()

        self.layout = QGridLayout(self.main_widget)

        self.menu = QMenuBar()
        self.layout.addWidget(self.menu, 0, 0, 1, 8)

        self.vis = QAction("Visualisation", self)
        self.menu.addAction(self.vis)

        self.capt = QAction("New capture", self)
        self.menu.addAction(self.capt)
        self.capt.triggered.connect(self.open_capture)

        self.open = QAction("Open", self)
        self.menu.addAction(self.open)
        self.open.triggered.connect(self.file_dialog)

        #создаю переменные
        enter_src_ip = QLineEdit()
        enter_dest_ip = QLineEdit()
        enter_src_port = QLineEdit()
        enter_dest_port = QLineEdit()
        enter_contains = QLineEdit()
        enter_size = QLineEdit()

        choose_protocol = QComboBox()

        # Добавляем виджеты в GridLayout
        self.layout.addWidget(QLabel("source IP"), 1, 0)
        self.layout.addWidget(enter_src_ip, 1, 1)
        self.layout.addWidget(QLabel("destination IP"), 1, 2)
        self.layout.addWidget(enter_dest_ip, 1, 3)
        self.layout.addWidget(QLabel("source Port"), 1, 4)
        self.layout.addWidget(enter_src_port, 1, 5)
        self.layout.addWidget(QLabel("destination Port"), 1, 6)
        self.layout.addWidget(enter_dest_port, 1, 7)
        self.layout.addWidget(QLabel("Protocol"), 2, 2)
        self.layout.addWidget(choose_protocol, 2, 3)
        self.layout.addWidget(QLabel("Contains"), 2, 4)
        self.layout.addWidget(enter_contains, 2, 5)
        self.layout.addWidget(QLabel("Size"), 2, 0)
        self.layout.addWidget(enter_size, 2, 1)
        self.layout.addWidget(QPushButton("Apply"), 2, 6)

        self.table = QTableWidget(self.main_widget)
        self.table.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.layout.addWidget(self.table, 3, 0, 30, 8)

        # Устанавливаем созданный виджет в качестве верхнего виджета
        self.setCentralWidget(self.main_widget)

    def file_dialog(self):
        filename, ok = QFileDialog.getOpenFileName(self,
                                                   "Select a Pcap File:",
                                                   "C:\\Users",
                                                   "Pcap files (*.pcap)"
                                                   )
        if filename:
            self.df = open_pcap(filename)
            self.display_pcap(self.df)
            path = Path(filename)


    def display_pcap(self, df):
        data = df.values.tolist()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data[0]))
        self.table.setHorizontalHeaderLabels(df.columns)
        for i in range(len(data)):
            for j in range(len(data[0])):
                self.table.setItem(i,j, QTableWidgetItem(str(data[i][j])))
    def apply_filters(self, df, filters):
        self.df_filtered = filter(df, filters)
        self.display_pcap(self.df_filtered)

    def open_capture(self):
        print("opening")
        self.capture_cam = PacketCaptureWindow()
        self.capture_cam.show()



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

