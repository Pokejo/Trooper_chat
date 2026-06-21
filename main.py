import socket
from typewriter import typewriter

state = ""

def network(host, port):
    global state

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((host, port))

        typewriter(f"Connected to {host} with success.")

        state = "client"

        return sock

    except:
        sock.close()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("0.0.0.0", 65535))
        sock.listen()

        client, client_ip = sock.accept()

        typewriter(f"Connected to {client_ip} with success.")

        state = "server"

        return client

def main():
    global state

    typewriter("This is a crypt messagerie program (enter '¤¤¤' for quit (copy this)).")

    host = input(typewriter("Enter the IP of the other device for connection (IPv4): "))
    while host == "":
        host = input(typewriter("Enter the ip: "))

    port = input(typewriter(f"Enter the listen port of {host} (default: 65535): "))
    while not port or int(port) < 0:
        port = 65535
    port = int(port)

    sock = network(host, port)

    while True:
        if state == "client":
            message = input(typewriter("Enter your message: "))
            if message == "¤¤¤":
                sock.close()
                typewriter(f"Connexion with {host} close.")
                exit()

            sock.send(message.encode('utf-8'))
            state = "server"

        else:
            data = sock.recv(1024)
            if not data:
                typewriter(f"{host} close the connection.")
                sock.close()
                exit()

            typewriter(f"Response: {data.decode()}")
            state = "client"

main()