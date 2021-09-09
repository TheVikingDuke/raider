import socket
import threading
import time
from halo import Halo

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}: {PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        clinet_handler = threading.Thread(target=handle_client, args=(client,))
        clinet_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        spinner = Halo(text='', spinner='dots')
        spinner.start("Processing")
        request = sock.recv(1024)
        time.sleep(3)
        spinner.succeed("Done...")
        print(f'[*] Recieved: {request.decode("utf-8")}')
        sock.send(b'ACK')
        
if __name__ == '__main__':
    main()