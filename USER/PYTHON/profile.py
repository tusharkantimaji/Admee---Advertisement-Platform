#!C:/Python/python
import check_cookie
import config
import cgi
import cgitb
cgitb.enable()

cursor = config.database.cursor()

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Profile | Tourexp</title>
</head>''')

Email = check_cookie.u_data[1][2: -1]
sql_quarry_1 = "SELECT * FROM `user` WHERE Email = '{}'".format(Email)
cursor.execute(sql_quarry_1)
details = cursor.fetchall()
print('''
<body><center>
    <div>
        <div>
            <h1>My Profile</h1>
        </div>
        <div>
            <img src="../../IMAGE/profile_picture_demo.png" alt="Profile Picture">
        </div>
        <div>
            <table cellpadding="7" cellspacing="0"  >
                <tr>
                    <td> <h2>Email Id</h2> </td>
                    <td> <h1> {} </h1> </td>
                </tr>
                <tr>
                    <td> <h2>Description</h2> </td>
                    <td> <h4>{}</h4> </td>
                </tr>
                    <td> <h2>Name</h2> </td>
                    <td> <h4>{}</h4> </td>
                </tr>
                <tr>
                    <td> <h2>Mobile<h2> </td>
                    <td> <h4>{}</h4> </td>
                </tr>
                <tr>
                    <td> <h2>Date of Birth</h2> </td>
                    <td> <h4>{}</h4> </td>
                </tr>
                <tr>
                <td> <h2>Gender<h2></td>
                <td> <h4>{}</h4> <td>
                </tr>'''.format(details[0][1], details[0][2], details[0][3], details[0][4], details[0][5], details[0][6]))
print('''
</table>
<button><a href="home-page.py">Back to Home Page</a></button>
<button><a href="edit_profile.py">Edit Profile</a></button>
</div>
</div>
</center>''')
frm = cgi.FieldStorage()
if frm.getvalue("msg"):
    print(frm.getvalue("msg"))
print('''
</body>
</html>''')
