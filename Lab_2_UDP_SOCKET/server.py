from socket import *

serverName = '127.0.0.1'

serverPort = 12000

server_socket=socket(AF_INET, SOCK_DGRAM)

server_address = (serverName, serverPort)

server_socket.bind(server_address)

buffer_size=2048

while True:
    message,client_address = server_socket.recvfrom(buffer_size)
    message = message.decode("utf-8")
    
    print("Messaggio ricevuto dal client: ", message)
    
    modified_message = message.upper()
    
    server_socket.sendto(modified_message.encode("utf-8"), client_address)
    
    print("Messaggio inviato al client: ", modified_message)