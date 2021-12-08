import socket
import index
from threading import Thread

def listen_for_client(cs):
    """
    This function keep listening for a message from `cs` socket
    Whenever a message is received, broadcast it to all other connected clients
    """
    while True:
        try:
            # keep listening for a message from `cs` socket
            msg = cs.recv(1024).decode()
        except Exception as e:
            # client no longer connected
            # remove it from the set
            print(f"[!] Error: {e}")
            index.client_sockets.remove(cs)
        else:
            # if we received a message, replace the <SEP>
            # token with ": " for nice printing
            msg = msg.replace(index.separator_token, ": ")
        # iterate over all connected sockets
        for client_socket in index.client_sockets:
            # and send the message
            client_socket.send(msg.encode())


while True:
    # we keep listening for new connections all the time
    client_socket, client_address = index.s.accept()
    print(f"[+] {client_address} connected.")
    # add the new connected client to connected sockets
    index.client_sockets.add(client_socket)
    # start a new thread that listens for each client's messages
    t = Thread(target=listen_for_client, args=(client_socket,))
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()
    # close client sockets
for cs in client_sockets:
    cs.close()
# close server socket
s.close()
open("client.py","r")
