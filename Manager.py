import socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

serverSocket.bind(("127.0.0.1",9090));

serverSocket.listen();

# Accept connections
(clientConnected, clientAddress) = serverSocket.accept();

print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));
while(True):
    # Send some data back to the client
    op=int(input("1. GetRequest\n2. GetNextRequest\n3. SetRequest\n4. Poll device\n5. Exit\n"))
    if op==1:
        oid_or_obj = input("Enter OID/Obj_name ")
        msg =  "GetRequest " + oid_or_obj
        clientConnected.sendall(msg.encode('utf-8'))
    elif op==2:
        msg =  "GetNextRequest"
        clientConnected.sendall(msg.encode('utf-8'))
    elif op==3:
        old_oid_or_obj = input("Enter old OID/Obj_name ")
        new_obj_name = input("Enter new Obj_name ")
        msg = "SetRequest " + old_oid_or_obj + " "+new_obj_name
        clientConnected.sendall(msg.encode('utf-8'))
    elif op==4:
        msg = "Poll device"
        clientConnected.sendall(msg.encode('utf-8'))
    elif op==5:
        msg = "exit"
        clientConnected.sendall(msg.encode('utf-8'))
        break
    else:
        print("Invalid operation")

    dataFromClient = clientConnected.recv(5000)

    print(dataFromClient.decode());