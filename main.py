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
        self.setWindowTitle("Пример меню")
        self.setGeometry(100, 100, 300, 200)
        self.showContextMenu()
        button_layout = QHBoxLayout()
        # self.stacklayout = QStackedLayout()

    def showContextMenu(self):
        menu = QMenu(self)  # это созд меню
        layout = QHBoxLayout()  # с этим мы будем соединять для горзнт
        click_1 = QAction("New capture", self)  # QAction - действие, которое можно do
        click_2 = QAction("Visualisation", self)
        menu.addAction(click_1)  # с пом-ю адд сы назнач действие. не раб с др
        menu.addAction(click_2)  # нашем случае мы соедеинели с Menu

        # Показ меню в позиции по центру окна
        menu.exec(self.mapToGlobal(self.rect().center()))  # ни малейшего поенятия что это но без него не работает

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

