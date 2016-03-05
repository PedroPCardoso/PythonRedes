import socket

target_host="127.0.0.1"
target_port= 24124

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# faz o cliente se conectar
client.connect((target_host,target_port))
#send msg
client.send( " ola")
#recebe dados
response = client.recv(1024)

print response
