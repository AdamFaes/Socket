import socket

UDP_IP = "10.160.108.101"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

MESSAGE=input("")
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
data,addr = sock.recvfrom(1024)
print("",data) 

code = 0
code =(((data[0]))|(data[1]<<8))|((data[2]<<16)|(data[3]<<24))

print("",code)
    
sock.sendto(str(code).encode(), (UDP_IP, UDP_PORT))
data,addr = sock.recvfrom(1024)
print("",data) 
