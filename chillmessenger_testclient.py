import sys
import socket

host = "localhost"
port = 61059
msg = 0
if len(sys.argv) > 1:
    msg = sys.argv[1].encode()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"Sending UDP Msg: {msg}")
sock.sendto(msg,(host, port))
