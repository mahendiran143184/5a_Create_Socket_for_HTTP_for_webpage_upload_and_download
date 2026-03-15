import socket
s=socket.socket()
s.bind(("localhost",8080))
s.listen(1)
print("Server running...")
while True:
    c,addr=s.accept()
    req=c.recv(1024).decode()
    print("Request received")
    if "GET" in req:
        f=open("index.html","r")
        res="HTTP/1.1 200 OK\n\n"+f.read()
        f.close()
        c.send(res.encode())
    elif "POST" in req:
        data=req.split("\n\n")[1]
        f=open("upload.txt","w")
        f.write(data)
        f.close()
        c.send("HTTP/1.1 200 OK\n\nFile Uploaded".encode())
    c.close()