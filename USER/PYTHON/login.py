#!C:/Python/python
import cgi
import cgitb
cgitb.enable()
print('''Content-type: text/html \r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login page | Tourexp</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link href="../CSS/login.css" rel="stylesheet">
</head>
<body>
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
        <h2 class="mt-5 mb-5"><u>Login</u></h2>
        <div>

            <form  method="post" action="login_block.py">
                <div class="mb-5 px-5">
                    <label for="exampleInputEmail1" class="form-label">User Name*</label>
                    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="abc@gmail.com" name="user_name" required>
                </div>
                <div class="mb-5 px-5">
                    <label for="exampleInputPassword1" class="form-label">Password*</label>
                    <input type="password" class="form-control" id="exampleInputPassword1" type="password" name="password"  required>
                </div>
            
            <input class="btn btn-warning black_border" type="reset" value="Reset">
            <input class="btn btn-success black_border" type="submit" value="Submit" name="ok">
            <a class="btn btn-danger black_border" href="forgot_password_1.py" role="button">Forgot Password</a><br>
            <a class="btn btn-primary mt-5 mb-5 black_border" href="home-page.py" role="button">Cancel</a>
            </form>
        </div>
        <p>Don't have an Account,</p>
        <a class="btn btn-info black_border" href="signup_1.py" role="button">Create Account</a>
    </center>
</div>
''')
frm = cgi.FieldStorage()
if frm.getvalue('msg'):
    print(frm.getvalue('msg'))

print('''
</body>
</html>
''')
