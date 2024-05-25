import datetime

from scapy.all import sniff
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from scapy.utils import wrpcap


class PacketCaptureWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.capturing = False
        self.layout = QVBoxLayout()
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.button = QPushButton("Begin capture")
        self.button.clicked.connect(self.capture_packets)

        self.layout.addWidget(self.button)

    def capture_packets(self):
        if self.capturing == False:
            self.button.setText("Stop & save capture")
            self.capturing = True
            captured_packets = []
            while self.capturing:
                packet = sniff(prn = self.process_packet, count = 1)
                captured_packets.append(packet)
                QApplication.processEvents()
            #print(len(captured_packets))
            #save into file
            filename = f"./pcaps/capture_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.pcap"
            wrpcap(filename, captured_packets)


        else:
            self.capturing = False
            self.button.setText("Begin capture")





    def process_packet(self, packet):
        print(packet.summary())


if __name__ == "__main__":
    app = QApplication([])
    window = PacketCaptureWindow()
    window.show()
    app.exec()