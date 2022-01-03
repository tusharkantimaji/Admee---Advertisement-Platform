#!C:/Python/python
import cgi
import cgitb
cgitb.enable()
print('''Content-type: text/HTML \r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admee | Advertise your brand</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link href="../CSS/index.css" rel="stylesheet">
</head>
<body>
    <div class="row justify-content-center">
        <center class="col-4">
            <div class="pt-5 pb-4">
                <div><img src="../../IMAGE/newlogo.png"
                alt="logo" width="200px" class ="logo-image"></div>
                <h1 class="name">Admee</h1>
            </div>
            <div>
                <h4 class="pt-3 pb-5">Advertise your brand</h4>
                <p>Float Your Boat For a New</p>
                <h1 class="adventure">Customer</h1>
            </div>
                <a href="home-page.py" class="btn btn-warning m-5 p-3 g_s black_border"> Get Started</a>
            </center>
            
        </center>
        <center class="col-4">
            <h2 class="mt-5 mb-5"><u>Login</u></h2>
        <div>

            <form  method="post" action="login_block.py">
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
            <a class="btn btn-primary mt-5 mb-3 black_border" href="home-page.py" role="button">Cancel</a>
            </form>
        </div>
        <p>Don't have an Account,</p>
        <a class="btn btn-info black_border" href="signup_1.py" role="button">Create Account</a><br>
            <a href="#"><img src="../../IMAGE/lock.png"
                alt="lock" width="100px" class ="lock-image"></a>
            </div>
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
