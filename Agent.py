import socket, json
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

clientSocket.connect(("127.0.0.1",9090));

count=0
with open('mib1.json') as mib1:
	data=json.load(mib1)

print("obj 1", data[1])

class SNMP:
	def getRequest(self,arg1):
		print("method called")
	def snmpWalk(self):
		print("method called")
	def setRequest(self,arg1,arg2):
		print("method called")
	def getNextRequest(self,pos):
		print(data[pos])

snmp = SNMP()

while True:
# Receive data from server
	dataFromServer = clientSocket.recv(5000).decode();
	if dataFromServer=="GetNextRequest":
		snmp.getNextRequest(count)
		count+=1
	elif dataFromServer=="Poll device":
		snmp.snmpWalk()
	elif dataFromServer=="exit":
		print("Server is disconnected, shutting down the system!")
		break
	else:
		l=dataFromServer.split()
		if len(l)==2:
			snmp.getRequest(l[1])
		elif len(l)==3:
			snmp.setRequest(l[1],l[2])
	print(dataFromServer);
	data = "data received!";
	clientSocket.send(data.encode());