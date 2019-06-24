from wsgiref.simple_server import make_server
from utils import load_html, load_template

PAGE_ROOT = './pages'
TEMPLATES_ROOT = './templates'

urls = {}


def route(path):
    def handle_action(action):
        # print('path = {},action = {}'.format(path, action))  path=/  action=show_index
        urls[path] = action  # {'/':show_index,'/index.html':show_index,'/test.html':show_test,'/info.html':show_info}

        def do_action(start_response):
            return action(start_response)

        return do_action

    return handle_action


@route('/')
@route('/index.html')
def show_index(start_response):
    file_name = PAGE_ROOT + '/index.html'
    return load_html(file_name, start_response)


@route('/test.html')
def show_test(start_response):
    file_name = PAGE_ROOT + '/test.html'
    return load_html(file_name, start_response)


@route('/info.html')
def show_info(start_response):
    file_name = TEMPLATES_ROOT + '/info.html'
    return load_template(file_name, start_response, name='王五', age=34, gender='男')


@route('/detail')
def show_detail(start_response):
    start_response('200 OK', [("Content-Type", 'text/html;charset=utf-8')])
    return ['我是详情页面'.encode('utf-8')]


def application(environ, start_response):
    file_name = environ.get('PATH_INFO')
    # print(urls)
    try:
        return urls[file_name](start_response)
    except KeyError:
        start_response('404 Not Found', [('Content-Type', "text/html;charset=utf-8")])
        return ['对不起，您访问的页面不存在'.encode('utf-8')]


if __name__ == '__main__':
    ip = '0.0.0.0'
    port = 9000
    with make_server(ip, port, application) as httpd:
        print('server is running on {}:{}'.format(ip, port))
        httpd.serve_forever()
