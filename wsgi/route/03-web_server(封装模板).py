from wsgiref.simple_server import make_server

from utils import load_html, load_template

PAGE_ROOT = './pages'
TEMPLATES_ROOT = './templates'


def show_index(start_response):
    file_name = PAGE_ROOT + '/index.html'
    return load_html(file_name, start_response)


def show_test(start_response):
    file_name = PAGE_ROOT + '/test.html'
    return load_html(file_name, start_response)


def show_info(start_response):
    file_name = TEMPLATES_ROOT + '/info.html'
    # return load_template(file_name, start_response, **{"name": '李四', 'age': 23, 'gender': '男'})
    return load_template(file_name, start_response, name='王五', age=34, gender='男')


def application(environ, start_response):
    file_name = environ.get('PATH_INFO')

    if file_name == '/' or file_name == '/index.html':
        return show_index(start_response)
    elif file_name == '/test.html':
        return show_test(start_response)
    elif file_name == '/info.html':
        return show_info(start_response)
    else:
        start_response('404 Not Found', [('Content-Type', "text/html;charset=utf-8")])
        return ['对不起，您访问的页面不存在'.encode('utf-8')]


if __name__ == '__main__':
    ip = '0.0.0.0'
    port = 9000
    with make_server(ip, port, application) as httpd:
        print('server is running on {}:{}'.format(ip, port))
        httpd.serve_forever()
