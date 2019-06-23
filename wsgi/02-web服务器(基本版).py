import socket


def hanlde_socket(socket):
    # 拿到用户请求的数据
    data = socket.recv(1024).decode('utf-8')
    if not data:
        return

    # print(data)

    # 先发送HTTP协议头
    response_header = 'HTTP/1.1 200 OK\r\n'
    response_header += '\r\n'
    # 连续两个换行表示头部已经结束了，开始body

    socket.send(response_header.encode('utf-8'))
    socket.send('hello'.encode('utf-8'))


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 9090))
    server_socket.listen(128)
    client_socket, client_addr = server_socket.accept()
    hanlde_socket(client_socket)
    pass


if __name__ == '__main__':
    main()
