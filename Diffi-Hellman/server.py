import sys
from socket import socket, AF_INET, SOCK_STREAM

BUFSIZE = 4096

class ServerOptions:
    def __init__(self, port, ip="0.0.0.0", *args):
       
        self.ip = ip
        self.port = int(port)

    def get_socket(self):
        return self.ip, self.port

def handle_client(client):
    
    go_on = True

    while go_on:
        data = client.recv(BUFSIZE)
        if len(data) == 0:
            go_on = False
        else:
            
            print(data.decode('utf-8'))

    client.close()

def main(args):

    options = ServerOptions(*args[1:]) 

    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(options.get_socket())
        print(f"Server bound to {options.get_socket()}")
        s.listen()

        while True:
            print(f"Wait for a new connection")
            client, client_address = s.accept()
            print(f"New connection from {client_address}")
            handle_client(client)
            print(f"{client_address} ended connection")


if __name__ == "__main__":
    main(sys.argv)
