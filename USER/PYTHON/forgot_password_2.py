#!C:/Python/python
import cgi
import config
import cgitb
cgitb.enable()

frm = cgi.FieldStorage()
cursor = config.database.cursor()
print('''Content-type: text/html \r\n\r\n
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>signup Page | Tourexp</title>
        <link rel="stylesheet" href="../CSS/signup.css">
        <script src="../JAVA SCRIPT/terms_condition.js"></script>
    </head>
    <body>''')
try:
    file_read = open('../TXT/store_otp_mail_forgot_password.txt', 'r')
    f = file_read.read()
    file_read.close()
    if f[0] == '0':
        print('''<center>
        <h4>OTP Send Succesfully</h4>
        <form>OTP
        <input type="password" placeholder='OTP' name="otp" required>*
        <input type="submit" name="otp_submit" value="Submit">
        </form></center>
        ''')
        file_read = open('../TXT/store_otp_mail_forgot_password.txt', 'r')
        f = file_read.read()
        file_read.close()
        file_write = open('../TXT/store_otp_mail_forgot_password.txt', 'w')
        file_write.write(str(f[1:]))
        file_write.close()

    if frm.getvalue("otp_submit"):
        otp = frm.getvalue("otp")
        file = open('../TXT/store_otp_mail_forgot_password.txt', 'r')
        sending_otp = file.read()
        file.close()
        sending_otp = sending_otp[:4]
        if int(otp) == int(sending_otp):
            print('''<center>
            <form><table>
            <tr>
                <td>Password</td>
                <td><input type="password" name="Password" required>*</td>
            </tr>
            <tr>
                <td>Confirm Password</td>
                <td><input type="password" name="Confirm_password" required>*</td>
            </tr>
            </table>
            <input type="submit" name="password_changed" value="Submit">
            </form>
            </center>''')
        else:
            print(
                '''<script>window.location = forgot_password_2.py?msg=OTP is not Matched</script>''')
            print("OTP is not Matched")

    if frm.getvalue("password_changed"):
        Password = frm.getvalue('Password')
        Confirm_password = frm.getvalue('Confirm_password')
        file = open('../TXT/store_otp_mail_forgot_password.txt', 'r')
        email_id = file.read()
        file.close()

        file = open('../TXT/store_otp_mail_forgot_password.txt', 'w')
        file.close()

        mail = email_id[4:]
        if Password == Confirm_password:
            sql_quarry_1 = "UPDATE `user` SET `Password`='{}' WHERE `Email`='{}'".format(
                Password, mail)
            try:
                cursor.execute(sql_quarry_1)
                config.database.commit()
                print('''<script>
                window.location = "login.py?msg=Password Updated succesfully"
                </script>''')
            except:
                print('''<script>
                window.location = "login.py?msg=Sorry, Password is Not Updated"
                </script>''')
        else:
            print("Password and Confirm passward will be same")
except:
    print("Not Possible")

if frm.getvalue('msg'):
    print(frm.getvalue('msg'))

print('''
</body>
</html>
''')
