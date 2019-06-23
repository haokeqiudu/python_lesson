import os
import socket


class WSGIServer(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def hanlde_socket(self, socket):
        data = socket.recv(1024).decode('utf-8')
        if not data:
            return
        req = data.splitlines()[0]
        file_name = req.split(' ')[1]

        if file_name == '/':  # 用户访问的主页
            file_name = '/index.html'  # 让用户加载index.html

        try:
            f = open('./pages' + file_name, 'rb')  # ./pages/hello.html
        except IOError:
            response_header = 'HTTP/1.1 404 file not found\r\n'
            f = open('./pages/error.html', 'rb')
            response_body = f.read()
        else:
            response_header = 'HTTP/1.1 200 OK\r\n'
            response_body = f.read()
            f.close()
        finally:
            # 指定返回的类型是 text/html 类型
            response_header += 'Content-Type: text/html\r\n'
            response_header += '\r\n'

            socket.send(response_header.encode('utf-8'))
            socket.send(response_body)

    def forever_run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.ip, self.port))
        server_socket.listen(128)
        while True:
            client_socket, client_addr = server_socket.accept()
            self.hanlde_socket(client_socket)


if __name__ == '__main__':
    ip = '0.0.0.0'
    port = 9090
    server = WSGIServer(ip, port)
    server.forever_run()
    print('server is running at {}:{}'.format(ip, port))
