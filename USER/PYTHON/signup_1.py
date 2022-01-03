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
        <title>Signup Page | Travelcrew</title>
        <link rel="stylesheet" href="../CSS/signup.css">
        <script src="../JAVA SCRIPT/terms_condition.js"></script>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link href="../CSS/signup_1.css" rel="stylesheet">
    </head>
    <body>''')


print('''
<div class="row justify-content-center">
<center class="col-3 name">
        <div>T</div>
        <div>R</div>
        <div>A</div>
        <div>V</div>
        <div>E</div>
        <div>L</div>
        <div>C</div>
        <div>R</div>
        <div>E</div>
        <div>W</div>
</center>
<center class="col-7">
    <h2 class="mt-5 mb-5"><u>SignUp</u></h2>

    <form>
        <div class="mb-5 px-5">
            <label for="exampleInputEmail1" class="form-label">Email Id*</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="abc@gmail.com" name="Email" required>
        </div>
        <input class="btn btn-success black_border" type="submit" value="Send OTP" name="send">
    </form>
    <div>
    <a href="login.py" class="btn btn-info mt-5 mb-1 black_border">Back to Login Page</a><br>
    <a href="home-page.py" class="btn btn-info m-1 black_border">Back to Home Page</a><br>
    <a href="index.py" class="btn btn-info m-1 black_border">Back to Starting Page</a>
    </div>   
</center>
</div>
''')


if frm.getvalue('send'):
    mail = frm.getvalue('Email')
    sql_quarry_3 = "SELECT * FROM user WHERE Email= '{}'".format(mail)
    cursor.execute(sql_quarry_3)
    exist = cursor.fetchall()
    print("check1")
    if exist:
        print('''<script>
        window.location = "login.py?msg=Email Already exists, Login Please"
        </script>
        ''')
    else:
        # print('''
        #     <script>window.location = "signup_2.py"</script>
        #     ''')
        print("Doing1")
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("learnky.edu@gmail.com", "Tushar@123")

        msg = MIMEMultipart("alternative")
        msg["From"] = "learnky.edu@gmail.com"
        msg["To"] = mail
        msg["Subject"] = "Email Verification Password OTP | Tourexp"
        print("Doing2")
        file_write = open('../TXT/store_otp_mail_signup.txt', 'w')
        file_write.write(str("0" + str(my_otp)))
        file_write.close()

        file_append = open('../TXT/store_otp_mail_signup.txt', 'a')
        file_append.write(str(mail))
        file_append.close()
        print("Doing3")
        text_part = MIMEText(
            "Dear '{}'\nHere is Your OTP = {}.\n\nThank You so much for using Admme.\n--Team Admee".format(mail, my_otp), "plain")
        msg.attach(text_part)
        s.sendmail("learnky.edu@gmail.com", mail, msg.as_string())
        s.quit()
        print('''
        <script>window.location = "signup_2.py?msg={}"</script>
        ''')
        print("Doing4")
        if s.sendmail("learnky.edu@gmail.com", mail, msg.as_string()):
            s.quit()
            print('''
            <script>window.location = "signup_2.py"</script>
            ''')
        else:
            print('''
            <script>window.location = "signup_1.py?msg=Mail can not be sent"</script>
            ''')
if frm.getvalue('msg'):
    print('''<br>''')
    print(frm.getvalue('msg'))
print('''

</body>
</html>
''')
