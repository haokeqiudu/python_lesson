from wsgiref.simple_server import make_server


# 2. 定义一个函数，用来处理用户的请求
def app(environ, start_response):
    """
    用来处理用户的请求，给用户进行相应的
    :param environ: 保存了客户端的环境配置信息，格式是字典。有一个需要我们重点关注的key-->PATH_INFO,用来保存用户请求的路径
    :param start_response: 用来设置响应头
    :return: 用来设置响应体
    """
    # {'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\chris\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-MSEMOTH', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\chris', 'LOCALAPPDATA': 'C:\\Users\\chris\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-MSEMOTH', 'NUMBER_OF_PROCESSORS': '4', 'OS': 'Windows_NT', 'PATH': 'C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\Program Files (x86)\\Intel\\iCLS Client\\;C:\\Program Files\\Intel\\iCLS Client\\;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Git\\cmd;C:\\Program Files\\nodejs\\;C:\\Users\\chris\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Program Files\\JetBrains\\PyCharm 2018.3.3\\bin;;C:\\Program Files\\Redis\\;C:\\Program Files\\MySQL\\MySQL Server 5.7\\bin;C:\\MinGW\\bin;C:\\Program Files\\Java\\jre1.8.0_201\\bin;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;C:\\Users\\chris\\AppData\\Local\\Programs\\Python\\Python37;C:\\Users\\chris\\AppData\\Local\\Programs\\Python\\Python37\\Scripts;C:\\Users\\chris\\AppData\\Roaming\\npm', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 61 Stepping 4, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '3d04', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM': 'C:\\Program Files\\JetBrains\\PyCharm 2018.3.3\\bin;', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'C:\\Users\\chris\\Desktop\\Python基础\\day18(wsgi、miniweb框架)\\02-代码', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\chris\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\chris\\AppData\\Local\\Temp', 'USERDOMAIN': 'DESKTOP-MSEMOTH', 'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-MSEMOTH', 'USERNAME': 'chris', 'USERPROFILE': 'C:\\Users\\chris', 'WINDIR': 'C:\\WINDOWS', 'SERVER_NAME': 'DESKTOP-MSEMOTH', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8080', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/index.html', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'text/plain', 'HTTP_HOST': '127.0.0.1:8080', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_CACHE_CONTROL': 'max-age=0', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36', 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7', 'wsgi.input': <_io.BufferedReader name=536>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>, 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>}
    # print(environ)
    # environ["PATH_INFO"]
    file_name = environ.get('PATH_INFO')
    print(file_name)
    start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
    return ['hello'.encode('utf-8')]


if __name__ == '__main__':
    # 1. 调用 make_server 方法，创建一个服务器
    # 需要三个参数：
    # 第一个参数表示服务器的ip地址，一般使用 ''
    # 第二个参数表示端口号
    # 第三个参数是一个函数，用来处理请求
    ip = '0.0.0.0'
    port = 8080
    with make_server(ip, port, app) as httpd:
        # sa = httpd.socket.getsockname()
        # print('Server is running on ', sa[0], 'port', sa[1])
        print('server is running on {}:{}'.format(ip, port))
        # 3. 启动web服务器
        httpd.serve_forever()
