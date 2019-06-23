import re
import socket
import threading
from multiprocessing import Process


class WSGIServer():
    def __init__(self, server, port, root):
        self.server = server
        self.port = port
        self.root = root

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.server, self.port))
        self.server_socket.listen(128)

    def handle_socket(self, socket):
        data = socket.recv(1024).decode('utf-8').splitlines()
        print(data)
        if not data:
            return
        data = data[0]
        file_name = re.match(r'[^/]+(/[^ ]*)', data)[1]
        # print(file_name)

        if file_name == '/':
            file_name = self.root + '/hello.html'
        else:
            file_name = self.root + file_name

        try:
            file = open(file_name, 'rb')
        except IOError:
            response_header = 'HTTP/1.1 404 NOT FOUND \r\n'
            response_header += '\r\n'
            response_body = '========Sorry,file not found======='.encode('utf-8')
        else:
            response_header = 'HTTP/1.1 200 OK \r\n'
            response_header += '\r\n'
            response_body = file.read()

        finally:
            socket.send(response_header.encode('utf-8'))
            socket.send(response_body)

    def forever_run(self):
        while True:
            client_socket, client_addr = self.server_socket.accept()
            self.handle_socket(client_socket)


if __name__ == '__main__':
    ip = '0.0.0.0'
    port = 8899
    server = WSGIServer(ip, port, './pages')
    print('server is running at {}:{}'.format(ip, port))
    server.forever_run()
