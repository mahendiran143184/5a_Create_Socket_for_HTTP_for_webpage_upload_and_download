import socket
s=socket.socket()
s.connect(("localhost",8080))
ch=input("1.Download 2.Upload : ")
if ch=="1":
    s.send("GET / HTTP/1.1\nHost: localhost\n\n".encode())
    print(s.recv(4096).decode())
else:
    msg=input("Enter data to upload: ")
    s.send(("POST / HTTP/1.1\nHost: localhost\n\n"+msg).encode())
    print(s.recv(1024).decode())
s.close()