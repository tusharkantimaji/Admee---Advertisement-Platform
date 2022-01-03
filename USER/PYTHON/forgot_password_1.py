#!C:/Python/python
import cgi
import config
import cgitb
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
cgitb.enable()

frm = cgi.FieldStorage()
cursor = config.database.cursor()

my_otp = random.randint(1000, 9999)

print('''Content-type: text/html \r\n\r\n
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Forgot Password | Tourexp</title>
        <link rel="stylesheet" href="../CSS/signup.css">
        <script src="../JAVA SCRIPT/terms_condition.js"></script>
    </head>
    <body>''')


print('''
<center>
    <h2>Forgot Password</h2>
    <form>
        <table>
            <tr>
                <td>Email Id</td>
                <td><input type="email" placeholder="abc@gmail.com" name="Email" required>*</td>   
            </tr>
        <table>
        <input type="submit" name="send" value="Send OTP">
    </form>   
</center>''')


if frm.getvalue('send'):
    mail = frm.getvalue('Email')
    sql_quarry_3 = "SELECT * FROM user WHERE Email= '{}'".format(mail)
    cursor.execute(sql_quarry_3)
    result = cursor.fetchall()
    if result:
        name = result[0][3]
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("learnky.edu@gmail.com", "Tushar@123")

        msg = MIMEMultipart("alternative")
        msg["From"] = "learnky.edu@gmail.com"
        msg["To"] = mail
        msg["Subject"] = "Forgot Password OTP | Tourexp"

        file_write = open('../TXT/store_otp_mail_forgot_password.txt', 'w')
        file_write.write(str("0" + str(my_otp)))
        file_write.close()

        file_append = open('../TXT/store_otp_mail_forgot_password.txt', 'a')
        file_append.write(str(mail))
        file_append.close()

        text_part = MIMEText(
            "Dear '{}'\nHere is Your Forgot Password \n OTP = {}.\n\n Thank You so much for using Tourexp.\n--Team Tourexp".format(name, my_otp), "plain")
        msg.attach(text_part)
        s.sendmail("learnky.edu@gmail.com", mail, msg.as_string())
        s.quit()
        print('''
        <script>window.location = "forgot_password_2.py"</script>
        ''')
    else:
        print('''
        <script>window.location = "signup_1.py?msg=This Email id is not register"</script>
        ''')
print('''
</body>
</html>
''')
