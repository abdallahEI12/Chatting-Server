import socket
sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
print("make sure the server is up...")
while True:
	

	myMsg = str(input("~:")) 

	sock.sendto(myMsg.encode("UTF-8"), ("192.168.1.20",55555))

	print("-" * 70)

	print("waiting for the server to respond")
	print("-" * 70)

	connection , address = sock.recvfrom(1024)

	serverMsg = connection.decode("UTF-8")
	if serverMsg == 'exit':
		print("server has terminated the connection")
		socket.close()
		break
	print(f"{serverMsg} ")
