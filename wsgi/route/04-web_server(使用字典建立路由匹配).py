from wsgiref.simple_server import make_server
from utils import load_html, load_template

PAGE_ROOT = './pages'
TEMPLATES_ROOT = './templates'

urls = {
    '/': 'show_index',
    '/index.html': 'show_index',
    '/test.html': 'show_test',
    '/info.html': 'show_info'
}


def show_index(start_response):
    file_name = PAGE_ROOT + '/index.html'
    return load_html(file_name, start_response)


def show_test(start_response):
    file_name = PAGE_ROOT + '/test.html'
    return load_html(file_name, start_response)


def show_info(start_response):
    file_name = TEMPLATES_ROOT + '/info.html'
    return load_template(file_name, start_response, name='王五', age=34, gender='男')


def application(environ, start_response):
    file_name = environ.get('PATH_INFO')
    # try:
    #     func_str = urls[file_name]  # 'show_index'
    # except KeyError:
    #     start_response('404 Not Found', [('Content-Type', "text/html;charset=utf-8")])
    #     return ['对不起，您访问的页面不存在'.encode('utf-8')]
    # else:
    #     func = eval(func_str)  # show_index 函数
    #     return func(start_response)

    func_str = urls.get(file_name)
    if func_str:
        func = eval(func_str)  # show_index 函数
        return func(start_response)
    start_response('404 Not Found', [('Content-Type', "text/html;charset=utf-8")])
    return ['对不起，您访问的页面不存在'.encode('utf-8')]


if __name__ == '__main__':
    ip = '0.0.0.0'
    port = 9000
    with make_server(ip, port, application) as httpd:
        print('server is running on {}:{}'.format(ip, port))
        httpd.serve_forever()
