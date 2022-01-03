#!C:/Python/python
import http.cookies
import cgitb
import config
import cgi
cgitb.enable()

frm = cgi.FieldStorage()
if frm.getvalue('ok'):
    user_name = frm.getvalue('user_name')
    password = frm.getvalue('password')
    try:
        sql_quarry = "SELECT * FROM user WHERE Email='{}' AND Password='{}'".format(
            user_name, password)
        cursor = config.database.cursor()
        cursor.execute(sql_quarry)
        check = cursor.fetchall()
        cook = ''
        counter = 0
        if check:
            for info in check:
                if counter == 0:
                    cook += str(info)
                    counter = 1
                else:
                    cook = cook + ',' + info
            c = http.cookies.SimpleCookie()
            c['u_info'] = cook
            c['u_info']['expires'] = 60*60*24*30
            print(c)
            print('''
            <script>
                window.location = "home-page.py";
            </script>
            ''')
        else:
            sql_quarry = "SELECT * FROM user WHERE Email='{}'".format(
                user_name)
            cursor = config.database.cursor()
            cursor.execute(sql_quarry)
            result = cursor.fetchall()
            if result:
                print('''
                <script>
                    window.location = "login.py?msg=Enter a valid Password"
                </script>
                ''')
            else:
                print('''
                <script>
                    window.location = "signup_1.py?msg=This mail is not registered yet, so signup"
                </script>
                ''')
        config.database.commit()
    except Exception as e:
        print(e)
    finally:
        config.database.close()
