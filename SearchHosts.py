import socket
import os


# execulte como root !!!!!!!!!!!!!!!!
#para ter o resultado execulte o ping de algum site para ver o pacote que foi enviado.


#host que ouvira  #ifconfig ou ipconfig(windows)
host= "192.168.0.103 "

#cria um socket puro e associa-o a interface publica

if os.name == "nt":
    socket_protocolo = socket.IPPROTO_IP

else :
    socket_protocolo = socket.IPPROTO_ICMP

sniffer= socket.socket(socket.AF_INET,  socket.SOCK_RAW,  socket_protocolo)


sniffer.bind((host,0))


#queremos os cabecalhos IP

sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)


#le o pacote

print sniffer.recvfrom(65565)
