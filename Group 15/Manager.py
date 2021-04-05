import socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
serverSocket.bind(("127.0.0.1",9090));
serverSocket.listen();

# Accept connections
(clientConnected, clientAddress) = serverSocket.accept();

print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));
while(True):
    # Send some data back to the client
    op=int(input("1. GetRequest\n2. SetRequest\n3. Poll devices\n4. Exit\n"))
    if op==1:
        oid_or_obj = input("Enter OID/Obj_name ")
        msg =  "GetRequest " + oid_or_obj
        clientConnected.sendall(msg.encode('utf-8'))
    elif op==2:
        old_oid_or_obj = input("Enter OID/Obj_name ")
        new_obj_name = input("Enter new value you want to modify")
        new_value=input("enter new value")
        msg = "SetRequest " + old_oid_or_obj + " "+new_obj_name+" "+new_value
        clientConnected.sendall(msg.encode('utf-8'))
    elif op==3:
        msg = "Poll device"
        clientConnected.sendall(msg.encode('utf-8'))
    elif op==4:
        msg = "exit"
        clientConnected.sendall(msg.encode('utf-8'))
        break
    else:
        print("Invalid operation")

    dataFromClient = clientConnected.recv(5000)

    print(dataFromClient.decode());