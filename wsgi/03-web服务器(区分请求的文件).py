import os
import socket


def hanlde_socket(socket):
    # 拿到用户请求的数据
    data = socket.recv(1024).decode('utf-8')
    if not data:
        return
    """
    data的内容
     GET /hello.html HTTP/1.1
     Host: 127.0.0.1:9090
     Connection: keep-alive
     Cache-Control: max-age=0
     Upgrade-Insecure-Requests: 1
     User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36
     Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
     Accept-Encoding: gzip, deflate, br
     Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7
     """
    req = data.splitlines()[0]  # GET /hello.html HTTP/1.1
    file_name = req.split(' ')[1]
    # print(file_name)  # /hello.html

    if file_name == '/':  # 用户访问的主页
        file_name = '/index.html'  # 让用户加载index.html

    try:
        f = open('./pages' + file_name, 'rb')  # ./pages/hello.html
    except IOError:
        response_header = 'HTTP/1.1 404 file not found\r\n'
        response_body = '对不起，文件丢失了'.encode('utf-8')
    else:  # 文件存在
        response_header = 'HTTP/1.1 200 OK\r\n'
        response_body = f.read()
        f.close()
    finally:
        # 指定返回的类型是 text/html 类型
        response_header += 'Content-Type: text/html\r\n'
        response_header += '\r\n'

        socket.send(response_header.encode('utf-8'))
        socket.send(response_body)


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 9090))
    server_socket.listen(128)
    client_socket, client_addr = server_socket.accept()
    hanlde_socket(client_socket)
    pass


if __name__ == '__main__':
    main()
