#!C:/Python/python
import http.cookies
import os
print('Content-type:text/html\n\n')
if 'HTTP_COOKIE' in os.environ:
    cookie_str = os.environ.get('HTTP_COOKIE')
    c = http.cookies.SimpleCookie()
    c.load(cookie_str)
    try:
        u_data = c['u_info'].value.split(',')
        login = True
    except KeyError:
        login = False
else:
    login = False
