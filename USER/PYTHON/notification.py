#!C:/Python/python
from pymysql.cursors import Cursor
import check_cookie
import cgi
import config
import check_cookie
import cgitb
import os
import http.cookies

cgitb.enable()
cursor = config.database.cursor()

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
        crossorigin="anonymous"></script>
</head>''')

cookie_str = os.environ.get('HTTP_COOKIE')
c = http.cookies.SimpleCookie()
c.load(cookie_str)

u_data = c['u_info'].value.split(',')
user_id = u_data[0][1:]


print('''
<body>
    <div class="container">
        <div class="row">''')

print('''<div class="col">
        <h1>Tourexp Notification</h1>''')

sql_quarry_1 = "SELECT MAX(Notification_id) FROM `notification`WHERE User_id_from = 'Tourexp' and User_id_to = {}".format(
    user_id)
cursor.execute(sql_quarry_1)
max_admin_notification_id = cursor.fetchall()
sql_quarry_2 = "SELECT MIN(Notification_id) FROM `notification`WHERE User_id_from = 'Tourexp' and User_id_to = {}".format(
    user_id)
cursor.execute(sql_quarry_2)
min_admin_notification_id = cursor.fetchall()
if max_admin_notification_id[0][0] != None:
    for item in range(max_admin_notification_id[0][0], min_admin_notification_id[0][0]-1, -1):
        sql_quarry_3 = "SELECT * FROM `notification`WHERE Notification_id = {}".format(
            item)
        cursor.execute(sql_quarry_3)
        details = cursor.fetchall()
        if details:
            print('''<hr><h5>{}<h5>'''.format(details[0][4]))


print('''</div>''')


print('''<div class="col">
    <h1>User Notification</h1>
</div>''')
print('''</div>
    </div>
</body>
</html>''')
