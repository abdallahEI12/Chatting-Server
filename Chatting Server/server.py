import socket

sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

sock.bind(("192.168.1.20", 55555))

print("server is up ....")
print("waiting for connections, send your message")
print("-" * 70)
while True:
    #recive client's message
    connection , address = sock.recvfrom(1024)
    msgs = connection.decode("UTF-8")
    if msgs == "exit":
        print("client has terminated the connection")
        sock.sendto("exit".encode('UTF-8'), address)
        socket.close()
        break
    print(msgs)

    #send my message
    myMsg = str(input("~:"))
    sock.sendto(myMsg.encode("UTF-8"), address)
