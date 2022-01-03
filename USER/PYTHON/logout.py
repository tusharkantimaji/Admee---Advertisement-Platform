#!C:/Python/python
import http.cookies

c = http.cookies.SimpleCookie()
c['u_info'] = ""
c['u_info']['expires'] = 0
print(c)
print("Content-type: text/html \r\n\r\n")
print("")
print('''
<script>
    window.location="login.py?msg=Logout successfully"
</script>''')
