import socket  # importing lib for webSocket connection

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # описываем протокол TCPIP
server.bind(("localhost", 12345))  # открываем наш сервер для подключения на нашем устройстве "lockalhost", и записываем любой номер порта 1 - 2^16

server.listen()  # start server

while True:
    user, address = server.accept()  # registrate all client, accept function can see IP, connect type ets

    print(f"Client {user}, {address} connected!")
    user.send("Connected secusessfule!".encode("utf-8"))  # send message with utf-8 encoding
