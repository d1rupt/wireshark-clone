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
        self.df, self.s_df = open_pcap("./pcaps/capture_2024-06-02_14-22-46.pcap")
        self.df_filtered = self.df.copy()
        self.display_pcap(self.df)
    def open_pcap(self, filename):
        pcap2df = pcapHandler(file=filename, verbose=True)
        df = pcap2df.to_DF(head=True)
        scapy_capture = rdpcap(filename)
        print(df)
        return df, scapy_capture
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


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

