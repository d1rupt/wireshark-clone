from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import pandas as pd
from pcap_handler import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def open_pcap(self, filename):
        pcap2df = pcapHandler(file=filename, verbose=True)
        df = pcap2df.to_DF(head=True)
        print(df)



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

