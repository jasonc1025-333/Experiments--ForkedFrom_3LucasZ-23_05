import socket
import pyaudio

CHUNK = 4096
FORMAT = pyaudio.paInt8
CHANNELS = 1
RATE = 20480

MY_ADDR = ("", 7000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(MY_ADDR)

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=1, rate=RATE, output=True)

print("audio player started")
data, addr = sock.recvfrom(CHUNK)
while data != '':
    print("Received.")
    stream.write(data[CHUNK:])
    data, addr = sock.recvfrom(2 * CHUNK)

stream.stop_stream()
stream.close()
p.terminate()