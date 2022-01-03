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
    file_read = open('../TXT/store_otp_mail_signup.txt', 'r')
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
        file_read = open('../TXT/store_otp_mail_signup.txt', 'r')
        f = file_read.read()
        file_read.close()
        file_write = open('../TXT/store_otp_mail_signup.txt', 'w')
        file_write.write(str(f[1:]))
        file_write.close()

    if frm.getvalue("otp_submit"):
        otp = frm.getvalue("otp")
        file = open('../TXT/store_otp_mail_signup.txt', 'r')
        sending_otp = file.read()
        file.close()
        sending_otp = sending_otp[:4]
        if int(otp) == int(sending_otp):

            print('''<center><form class="container" id="blur"><table>

            <tr>
                <td>Name</td>
                <td><input type="text" placeholder="abc def" name="Name" required>*</td>
            </tr>
            <tr>
                <td>Description</td>
                <td><textarea name="Description" placeholder="I am a travellar" cols="60" rows="5" ></textarea></td>
            </tr>
            <tr>
                <td>Mobile Number</td>
                <td><input type="number" placeholder="9876543210" name="mobile"></td>
            </tr>
            <tr>
                <td>Date of Birth</td>
                <td><input type="date" name="DOB"></td>
            </tr>
            <tr>
                <td>Gender</td>
                <td>
                    <select name="Gender">
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                        <option value="Others">Others</option>
                        <option value="" selected>-Select-</option>
                    </select>
                </td>
            </tr>
            <tr>
                <td>Password</td>
                <td><input type="password" name="Password" required>*</td>
            </tr>
            <tr>
                <td>Confirm Password</td>
                <td><input type="password" name="Confirm_password" required>*</td>
            </tr>
            <tr>
                <td><input type="checkbox" required></td>
                <td><a href="index.py" onclick="toggle">Terms and Conditions*</a></td>
            </tr>
            </table>''')
            print('''<button type="reset">Reset</button>
            <input type="submit" name="ok"><br><br>
            <a href="login.py">Back to Login Page</a><br>
            <a href="index.py">Back to Home Page</a>''')
        else:
            print("OTP is not Matched")

    # print('''
    # </form>
    # <div id="popup">
    # <h2>Terms and Condition</h2>
    # <p>qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbn</p>
    # <a href="#" onclick="toggle">Close</a>
    # </div>
    # </center>
    # <br><br>  ''')

    if frm.getvalue('ok'):
        file = open('../TXT/store_otp_mail_signup.txt', 'r')
        email_id = file.read()
        file.close()

        file = open('../TXT/store_otp_mail_signup.txt', 'w')
        file.close()

        Email = email_id[4:]
        Name = frm.getvalue('Name')
        Description = frm.getvalue('Description')
        Mobile = frm.getvalue('mobile')
        DOB = frm.getvalue('DOB')
        Gender = frm.getvalue('Gender')
        Password = frm.getvalue('Password')
        Confirm_password = frm.getvalue('Confirm_password')
        if Password == Confirm_password:
            try:
                sql_quarry_1 = "SELECT Email FROM user WHERE Email='{}'".format(
                    Email)
                cursor.execute(sql_quarry_1)
                checker = cursor.fetchall()
                if checker:
                    print("You have already registered")
                else:
                    sql_quarry_2 = "INSERT INTO user (Email, Description, Name, Mobile, DOB, Gender, Password) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(
                        Email, Description, Name, Mobile, DOB, Gender, Password)

                    if cursor.execute(sql_quarry_2):
                        config.database.commit()
                        print('''<script>
                        window.location = "login.py?msg=Insert Succesfully"
                        </script>
                        ''')
            except Exception as e:
                print(e)
            finally:
                config.database.close()
        else:
            print("Password and Confirm password will be Same")
except:
    print("Not possible")
print('''
<a href="login.py">Back to Login Page</a><br>
<a href="home-page.py">Back to Home Page</a><br>
<a href="index.py">Back to Starting Page</a>
</body>
</html>
''')
