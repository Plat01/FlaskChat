import threading
import socket


class ClientThread(threading.Thread):
    def __init__(self, address, client):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        print("New connection from {}".format(address))

    def run(self):
        while True:
            data = self.client.recv(1024)
            if not data:
                break
            print(data)
            self.client.send(data)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 12346))
server.listen(5)

print("Server started")

while True:
    client, address = server.accept()
    ClientThread(address, client).start()
