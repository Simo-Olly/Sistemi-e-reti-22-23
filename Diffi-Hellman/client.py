import sys
from socket import socket, AF_INET, SOCK_STREAM

class ClientOptios:
    def __init__(self, ip, port, *args):
         self.ip = ip
         self.port = int(port)
 
    def get_socket(self):
        return self.ip, self.port

def ask_command():
    return input("$> ")

def main(args):
    options = ClientOptios(*args[1:])
    go_on = True

    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(options.get_socket())

        while go_on:
        
            cmd = ask_command()

            if cmd == "exit":
                go_on = False
            else:
                s.send(cmd.encode('utf-8'))


if __name__ == "__main__":
    main(sys.argv)

    
