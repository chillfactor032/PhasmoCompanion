import socket
import threading
import time
from PySide6.QtCore import QObject, Signal, Slot

class ChillMessenger(threading.Thread):
    
    class Signals(QObject):
        on_msg = Signal(int)

    def __init__(self):
        super().__init__()
        self.signals = self.Signals()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(0.1)
        self.port = 61059
        self._stopped = False
        self._running = False

    def stop(self):
        self._stopped = True

    def running(self):
        return self._running
    
    def run(self):
        self.sock.bind(('localhost', self.port))
        msg = 0
        self._running = True
        while not self._stopped:
            try:
                message, address = self.sock.recvfrom(1024)
                msg = int(message.decode())
            except socket.timeout:
                continue
            except ValueError:
                continue
            self.send_msg(msg)
    
    def send_msg(self, msg: int):
        print(f"Sending msg [{msg}]")
        self.signals.on_msg.emit(msg)

if __name__=="__main__":
    def recv(msg: int):
        print(f"RECV: {msg}")
    server = ChillMessenger()
    server.signals.on_msg.connect(recv)
    try:
        print("Starting ChillMessenger Server")
        server.start()
        while True:
            time.sleep(0.001)
    except KeyboardInterrupt:
        print("Stopping ChillMessenger Server")
        server.stop()
        server.join()
        print("Done")
