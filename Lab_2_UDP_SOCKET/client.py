from socket import *

servername="localhost"
port = 12000

client_socket = socket(AF_INET, SOCK_DGRAM)

server_address = (servername, port)

message = input("Inserisci il messaggio da inviare al server: ")

client_socket.sendto(message.encode("utf-8"), server_address)

buffer_size = 2048

server_response, address =client_socket.recvfrom(buffer_size)

print("Messaggio ricevuto dal server: ", server_response.decode("utf-8"))