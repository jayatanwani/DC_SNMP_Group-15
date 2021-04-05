import socket, json
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket.connect(("127.0.0.1",9090));

count=0
with open('mib1.json') as mib1:
	data=json.load(mib1)
new=data[1]
#print(data[5]["Object"])
class SNMP:
	def getRequest(self,arg1):
		flag=0
		print("get request method called")
		#print(arg1)
		for i in range(0,11):
			new=data[i]
			
			if new["Object"]==arg1 or new["OID"]==arg1:
				print(new)
				flag=1
				break


		if flag==0:
			print("requested data is not found")
		return new

	def snmpWalk(self):
		n=[]
		print("Following are OID's of connected devices")
		for i in range(0,11):
			new=data[i]
			l=str(new["OID"])
			n.append(l)
			print(new["OID"])
		return n
	def setRequest(self,arg1,arg2,arg3):
		flag=0
		print("set request method called")
		
		for i in range(0,11):
			new=data[i]
			if (new["Object"]==arg1 or new["OID"]==arg1) :
				if(arg2=="Status" or arg2=="value")and new["Max-access"]=="read-write":
					new[arg2]=arg3
					data[i][arg2]=arg3
					mib1.close()
					a_file = open("mib1.json", "w")
					json.dump(data, a_file)
					mib1.close()


				else:
					print("you can't modify this")
				flag=1
				break


		if flag==0:
			print("requested data is not found")
		return new


snmp = SNMP()

while (True):
	
# Receive data from server
	dataFromServer = clientSocket.recv(5000).decode();
		

	if dataFromServer=="Poll device":
		new1=snmp.snmpWalk()
	elif dataFromServer=="exit":
		print("Server is disconnected, shutting down the system!")
		break
	else:
		l=dataFromServer.split()
		if len(l)==2:
			new1=snmp.getRequest(l[1])
			
		elif len(l)==4:
			new1=snmp.setRequest(l[1],l[2],l[3])
	
	data = "data received!"+str(new1)
	#data="data received"
	clientSocket.send(data.encode());