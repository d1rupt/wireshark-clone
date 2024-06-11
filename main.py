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
        self.setGeometry(500, 400, 800, 300)
        self.main_widget = QWidget()

        self.layout = QGridLayout(self.main_widget)

        self.menu = QMenuBar()
        self.layout.addWidget(self.menu, 0, 0, 1, 4)

        self.vis = QAction("Visualisation", self)
        self.menu.addAction(self.vis)

        self.capt = QAction("New capture", self)
        self.menu.addAction(self.capt)
        self.capt.triggered.connect(self.open_capture)

        self.open = QAction("Open", self)
        self.menu.addAction(self.open)
        self.open.triggered.connect(self.file_dialog)

        #создаю переменные
        enter_ip = QLineEdit()
        enter_port = QLineEdit()
        enter_time = QLineEdit()
        enter_contains = QLineEdit()
        enter_size = QLineEdit()

        choose_protocol = QComboBox()
        choose_packet_type = QComboBox()

        # Добавляем виджеты в GridLayout
        self.layout.addWidget(QLabel("IP"), 1, 0)
        self.layout.addWidget(enter_ip, 1, 1)
        self.layout.addWidget(QLabel("Port"), 1, 2)
        self.layout.addWidget(enter_port, 1, 3)
        self.layout.addWidget(QLabel("Protocol"), 1, 4)
        self.layout.addWidget(choose_protocol, 1, 5)
        self.layout.addWidget(QLabel("Time"), 1, 6)
        self.layout.addWidget(enter_time, 1, 7)
        self.layout.addWidget(QLabel("Contains"), 2, 0)
        self.layout.addWidget(enter_contains, 2, 1)
        self.layout.addWidget(QLabel("Size"), 2, 2)
        self.layout.addWidget(enter_size, 2, 3)
        self.layout.addWidget(QLabel("Packet type"), 2, 4)
        self.layout.addWidget(choose_packet_type, 2, 5)
        self.layout.addWidget(QPushButton("Apply"), 2, 6)
        self.table = QTableWidget(self.main_widget)
        self.layout.addWidget(self.table, 3, 0, 8, 8)

        # Устанавливаем созданный виджет в качестве верхнего виджета
        self.setMenuWidget(self.main_widget)
        self.setMenuWidget(self.main_widget)

        #просто тестирую всякое
        #self.df, self.s_df = open_pcap("./pcaps/capture_2024-06-02_14-22-46.pcap")
        #self.df_filtered = self.df.copy()
        #self.display_pcap(self.df)

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

