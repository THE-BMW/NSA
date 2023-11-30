from socket import *
import time

def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print('Server is ready to accept connections')

    while True:
        connection_socket, addr = server_socket.accept()
        print('Got a connection from', addr)

        data = connection_socket.recv(1024)
        print('Received the message', data)

        message = b'This is the server. The client request is processed successfully.'
        connection_socket.send(message)
        print('Sent the message', message)

        connection_socket.close()
        print('Connection closed')
        
        # Simulated Firewall Rule in Python

def process_request(request):
    # Firewall Rule: Block requests with 'BLOCK.'
    if 'BLOCK.' in request:
        return "Blocked: Request contains 'BLOCK.'"
    else:
        # Process the request and generate a response
        response = "Processed: " + request
        return response

# Example Usage
client_request = input("Enter client request: ")
response = process_request(client_request)
print("Server Response:", response)


if __name__ == '__main__':
    main()
    