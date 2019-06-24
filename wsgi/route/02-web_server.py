from wsgiref.simple_server import make_server

from utils import load_html, simple_resp

PAGE_ROOT = './pages'
TEMPLATES_ROOT = './templates'


def show_index(start_response):
    """
    处理首页
    :param start_response:
    :return:
    """
    file_name = PAGE_ROOT + '/index.html'
    return load_html(file_name, start_response)


def show_test(start_response):
    """
    处理test页面
    :param start_response:
    :return:
    """
    file_name = PAGE_ROOT + '/test.html'
    return load_html(file_name, start_response)


def do_register(start_response):
    # 第一步：获取用户输入的信息
    # 第二步： 操作数据库，存入数据
    # 第三步：获取到数据库操作的结果
    # 第四步：根据结果，判断是否操作成功
    # start_response('200 OK', [("Content-Type", "text/html;charset=utf-8")])
    # return ['注册成功'.encode('utf-8')]
    return simple_resp(start_response, '注册成功')


def do_login(start_response):
    # 第一步：获取用户输入的用户名密码
    # 第二步：到数据库里查询，看用户名密码是否匹配
    # 第三步：根据查询结果，返回是否登录成功
    is_access = True
    if is_access:
        # start_response('200 OK', [("Content-Type", "text/html;charset=utf-8")])
        # return ['登录成功'.encode('utf-8')]
        return simple_resp(start_response, '登录成功')
    else:
        start_response('403 Forbidden', [("Content-Type", "text/html;charset=utf-8")])
        return ['用户名密码验证失败'.encode('utf-8')]


def show_info(start_response):
    file_name = TEMPLATES_ROOT + '/info.html'

    try:
        file = open(file_name, encoding='utf-8', mode='r')
    except IOError:
        start_response('410 Deleted', [("Content-Type", "text/html;charset=utf-8")])
        return ['您访问的资源已经被删除了'.encode('utf-8')]
    else:
        start_response('200 OK', [("Content-Type", "text/html;charset=utf-8")])

        content = file.read()
        # "<ul><li>姓名:{name}</li><li>年龄:{age}</li></ul>"
        # content = content.format(**{'name': '张三', "age": 18, 'gender': 'female', 'addr': '湖北'})
        content = content.format(name='张三', age=18, gender='female', addr='湖北')
        file.close()
        return [content.encode('utf-8')]


def application(environ, start_response):
    file_name = environ.get('PATH_INFO')

    if file_name == '/' or file_name == '/index.html':
        return show_index(start_response)
    elif file_name == '/test.html':
        return show_test(start_response)
    elif file_name == '/register':
        return do_register(start_response)
    elif file_name == '/login':
        return do_login(start_response)
    elif file_name == '/info.html':
        return show_info(start_response)
    else:
        start_response('404 Not Found', [('Content-Type', "text/html;charset=utf-8")])
        return ['对不起，您访问的页面不存在'.encode('utf-8')]

    # return ['hello'.encode('utf-8')]


if __name__ == '__main__':
    ip = '0.0.0.0'
    port = 8080
    with make_server(ip, port, application) as httpd:
        print('server is running on {}:{}'.format(ip, port))
        httpd.serve_forever()
