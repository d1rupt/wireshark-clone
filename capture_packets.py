import datetime
from pathlib import Path
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
        self.cap_data = QLabel()
        self.layout.addWidget(self.cap_data)
        self.save_data = QLabel()
        self.layout.addWidget(self.save_data)

    def capture_packets(self):
        if self.capturing == False:
            self.button.setText("Stop and save capture")
            self.capturing = True
            captured_packets = []
            while self.capturing:
                packet = sniff(prn = self.process_packet, count = 1)
                captured_packets.append(packet)
                self.cap_data.setText(f"Captured packets: {len(captured_packets)}")
                QApplication.processEvents()
            #print(len(captured_packets))
            #save into file
            Path("./pcaps").mkdir(parents=True, exist_ok=True)

            filename = f"./pcaps/capture_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.pcap"
            wrpcap(filename, captured_packets)
            self.save_data.setText(f"Saved file: {filename}")



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