import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12346))

while True:
    message = input("Enter a message: ")
    client.send(bytes(message, "utf-8"))
    data = client.recv(1024)
    print("Received from server: {}".format(data.decode("utf-8")))



