import socket

UDP_IP = "10.160.108.101"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

MESSAGE=input("")
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
data,addr = sock.recvfrom(1024)
print("",data) 

code = "0011277"
print("",code)
    
sock.sendto(code.encode(), (UDP_IP, UDP_PORT))
data,addr = sock.recvfrom(1024)
print("",data) 
