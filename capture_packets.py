from scapy.all import sniff
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
class PacketCaptureWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.button = QPushButton("Begin capture")
        self.button.clicked.connect(self.capture_packets)

        self.layout.addWidget(self.button)
    def capture_packets(self):
        if self.button.text() == "Begin capture":
            self.button.setText("Stop & save capture")
            self.capturing = True
            while self.capturing:
                sniff(prn = self.process_packet, count = 1)
                QApplication.processEvents()
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