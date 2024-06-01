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
        self.main_widget = QWidget()

        self.layout = QGridLayout(self.main_widget)

        self.menu = QMenuBar()
        self.layout.addWidget(self.menu, 0, 0, 1, 4)

        self.vis = QMenu("Visualisation", self)
        self.menu.addMenu(self.vis)
        self.capt = QMenu("New capture", self)
        self.menu.addMenu(self.capt)

        # Добавляем виджеты в GridLayout
        self.layout.addWidget(QLabel("IP"), 1, 0)
        self.layout.addWidget(QLineEdit(), 1, 1)
        self.layout.addWidget(QLabel("Port"), 1, 2)
        self.layout.addWidget(QLineEdit(), 1, 3)
        self.layout.addWidget(QLabel("Protocol"), 1, 4)
        self.layout.addWidget(QComboBox(), 1, 5)
        self.layout.addWidget(QLabel("Time"), 1, 6)
        self.layout.addWidget(QLineEdit(), 1, 7)
        self.layout.addWidget(QLabel("Contains"), 2, 0)
        self.layout.addWidget(QLineEdit(), 2, 1)
        self.layout.addWidget(QLabel("Size"), 2, 2)
        self.layout.addWidget(QLineEdit(), 2, 3)
        self.layout.addWidget(QLabel("Packet type"), 2, 4)
        self.layout.addWidget(QComboBox(), 2, 5)
        self.layout.addWidget(QPushButton("Apply"), 2, 6)
        self.layout.addWidget(QTableWidget(self.main_widget), 4, 1)

        # Устанавливаем созданный виджет в качестве верхнего виджета
        self.setMenuWidget(self.main_widget)
        self.setMenuWidget(self.main_widget)
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

