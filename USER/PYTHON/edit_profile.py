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
    <title>Edit My Profile | Tourexp</title>
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
        <div> <form>
            <table cellpadding="7" cellspacing="0"  >
                <tr>
                    <td> <h2>Email Id</h2> </td>
                    <td> <h1> {} </h1> </td>
                </tr>
                <tr>
                    <td> <h2>Description</h2> </td>
                    <td> <textarea rows="5" cols="55" name="Description">{}</textarea> </td>
                </tr>
                    <td> <h2>Name</h2> </td>
                    <td> <input value='{}' name="Name" size="60"></td>
                </tr>
                <tr>
                    <td> <h2>Mobile<h2> </td>
                    <td> <input name="Mobile" value='{}' size="60"></td>
                </tr>
                <tr>
                    <td> <h2>Date of Birth</h2> </td>
                    <td> <input name="DOB" type="date" value='{}' size="60"></td>
                </tr>
                <tr>
                <td> <h2>Gender<h2></td>
                <td>
                <select name="Gender">'''.format(details[0][1], details[0][2], details[0][3], details[0][4], details[0][5]))
if details[0][6] == 'Male':
    print('''
                    <option value="Male" selected>Male</option>
                    <option value="Female">Female</option>
                    <option value="Others">Others</option>
    ''')
elif details[0][6] == 'Female':
    print(''' 
                    <option value="Male" > Male </option>
                    <option value="Female" selected > Female </option>
                    <option value="Others" > Others </option>
    ''')
elif details[0][6] == 'Others':
    print(''' 
                    <option value="Male" selected > Male </option>
                    <option value="Female" > Female </option>
                    <option value="Others" selected > Others </option>
    ''')
print('''
</select>
</td>
</tr>
</table>
<input type="reset">
<input type="submit" name="ok" value="Submit">
<button><a href="profile.py">Cancel</a></button>
</form>
</div>
</div> ''')
frm = cgi.FieldStorage()
if frm.getvalue("ok"):
    Name = frm.getvalue('Name')
    Description = frm.getvalue('Description')
    Mobile = frm.getvalue('Mobile')
    DOB = frm.getvalue('DOB')
    Gender = frm.getvalue('Gender')
    try:
        sql_quarry_2 = "SELECT Email FROM user WHERE Email='{}'".format(
            Email)
        cursor.execute(sql_quarry_1)
        checker = cursor.fetchall()
        if checker:
            sql_quarry_2 = "UPDATE `user` SET `Description`='{}',`Name`='{}',`Mobile`='{}',`DOB`='{}',`Gender`='{}' WHERE `Email` = '{}'".format(
                Description, Name, Mobile, DOB, Gender, Email)

            if cursor.execute(sql_quarry_2):
                config.database.commit()
                print('''<script>
                window.location = "Profile.py?msg=Update Succesfully"
                </script>
                ''')
            else:
                print('''<script>
                window.location = "Profile.py?msg=Update is not possible at this moment"
                </script>
                ''')
    except Exception as e:
        print('''<script>
                window.location = "Profile.py?msg=Update is not possible at this moment"
                </script>
                ''')
    finally:
        config.database.close()
print('''</center>
</body>
</html>''')
