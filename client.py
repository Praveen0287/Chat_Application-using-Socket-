import socket
import threading
HOST = input("Enter Server IP : ")
PORT = 5000
username = input("Enter Username : ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
except Exception as e:
    print("Connection Failed")
    print(e)
    exit()

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == "USERNAME":
                client.send(username.encode())
            else:
                print(message)
        except:
            print("Disconnected from server.")
            client.close()
            break

def send_messages():
    while True:
        try:
            msg = input()

            if msg.strip() == "":
                print("Message cannot be empty.")
                continue

            full_message = f"{username}: {msg}"
            client.send(full_message.encode())

        except:
            break


receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
