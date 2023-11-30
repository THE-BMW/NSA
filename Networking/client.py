from socket import *

def main():
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print('Client connected to the server')

    message = b'This is the client. Here is a message for the server.'
    client_socket.send(message)
    print('Sent the message', message)

    data = client_socket.recv(1024)
    print('Received the message', data)

    client_socket.close()
    print('Client disconnected')

if __name__ == '__main__':
    main()