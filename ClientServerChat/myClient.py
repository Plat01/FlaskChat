import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # описываем тип соединения для клиента
client.connect(("localhost", 12345))

while True:
    data = client.recv(1024)
    print(data.decode("utf-8"))