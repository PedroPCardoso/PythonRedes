import socket
import threading

bind_ip = "127.0.0.1"  #ip do servidor
bind_port= 24124 #porta do servidor

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))


server.listen(5)  #comece a ouvir maximo de conexoes 5

print "[*] listando on %s:%d" %(bind_ip,bind_port)

#thread de tratamento de clientes

def handle_client(client_socket):
    #exibe o que o cliente envia
    request= client_socket.recv(1024)
    print "[*] Recebido %s " %request

    #envia um pacote de volta
    client_socket.send("ACK!")

    client_socket.close()
while True:
    client,addr = server.accept()
    #print "[*] Aceitando conexao de: %s:%s "(addr[0],addr[1])

    #clocando nossa thread em acao para tratar dados de entrada
    client_handler = threading.Thread(target= handle_client,args=(client,))
    client_handler.start()
