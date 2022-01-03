import smtplib

mail = 'tusharkanti2001maji@gmail.com'

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("learnky.edu@gmail.com", "Tushar@123")

msg = MIMEMultipart("alternative")
msg["From"] = "learnky.edu@gmail.com"
msg["To"] = mail
msg["Subject"] = "Email Verification Password OTP | Tourexp"
print("Doing2")
file_write = open('../TXT/store_otp_mail_signup.txt', 'w')
file_write.write(str("0" + str(4567)))
file_write.close()

file_append = open('../TXT/store_otp_mail_signup.txt', 'a')
file_append.write(str(mail))
file_append.close()
print("Doing3")
text_part = MIMEText(
    "Dear '{}'\nHere is Your OTP = {}.\n\nThank You so much for using Tourexp.\n--Team Tourexp".format(mail, my_otp), "plain")
msg.attach(text_part)
s.sendmail("learnky.edu@gmail.com", mail, msg.as_string())
s.quit()
print('''
<script>window.location = "signup_2.py?msg={}"</script>
''')
print("Doing4")
if s.sendmail("learnky.edu@gmail.com", mail, msg.as_string()):
    s.quit()
    print("Finally done")
else:
    print("NOT Possible")