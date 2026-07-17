import socket
import threading
HOST = "0.0.0.0"
PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            pass

def remove_client(client):
    if client in clients:
        index = clients.index(client)
        username = usernames[index]
        clients.remove(client)
        usernames.remove(username)
        client.close()
        broadcast(f"{username} left the chat.".encode())
        print(f"{username} disconnected")

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                remove_client(client)
                break
                broadcast(message)
            except:
            remove_client(client)
            break


def receive_connections():
    print(f"Server running on {HOST}:{PORT}")

    while True:
        client, address = server.accept()

        print(f"Connected with {address}")

        client.send("USERNAME".encode())

        username = client.recv(1024).decode()

        usernames.append(username)
        clients.append(client)

        print(f"{username} joined the chat.")

        broadcast(f"{username} joined the chat.".encode())

        client.send("Connected Successfully!".encode())

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()
