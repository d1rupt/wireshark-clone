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
        '''do-QAction действие которое возможно в интерфс.
         addaction назнач действ через do.add'''

        '''
        toolbar = QToolBar(self)
        totoo = QToolBar(self)
        self.addToolBar(toolbar)
        self.addToolBar(totoo)

        butt_action = QAction("Visualisation", self)
        butt_action_2 = QAction("New capture", self)

        toolbar.addAction(butt_action)
        totoo.addAction(butt_action_2)
        '''
        # это прикольно, но я думала так; с помощью QMenu - я написала это еще в моём рисуночке)
        self.menu = QMenuBar()
        self.setMenuBar(self.menu) #создаем сверху менюшку

        self.vis = QMenu("Visualisation", self) #добавляем туды кнопочку
        self.menu.addMenu(self.vis)
        #аналогично добавить New Capture

    def contextMenuEvent(self,event):
        event.ignore()

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

