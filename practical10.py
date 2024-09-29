#10scoket
import socket
import ssl
hostname="www.python.org"
port=443
context=ssl.create_default_context()
#secure con
with socket.create_connection((hostname,port)) as sock:
    with context.wrap_socket(sock,server_hostname=hostname) as ssock:
        print(f"SSL protocol version:{ssock.version()}")
        #req
        req=f"GET / HTTP/1.1\r\nHost:{hostname}\r\n\r\n"
        ssock.send(req.encode())
        #res
        res=ssock.recv(4096).decode()
        print("response from the server:")
        print(res)
        ssock.close()