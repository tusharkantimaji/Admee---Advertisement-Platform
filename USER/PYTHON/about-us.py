#!C:/Python/python
import check_cookie
import config
import cgi
import cgitb
cgitb.enable()
print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us | Admee</title>
    <link rel="stylesheet" href="../CSS/home-page.css">
    <script src="../JAVA SCRIPT/home-page.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link href="../CSS/home-page.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
</head>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
  <img src="../../IMAGE/newlogo.png" width="150px" alt="logo">
    <a class="navbar-brand" href="#"><h1>Admee</h1></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">

        <li class="nav-item">
          <a class="nav-link" href="index.py">Starting Page</a>
        </li>
         <li class="nav-item">
          <a class="nav-link" aria-current="page" href="home-page.py">Home</a>
        </li>

        <li class="nav-item">
          <a class="nav-link active" href="about-us.py">About Us</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="contact-us.py">Contact Us</a>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="text" placeholder="Search" aria-label="Search" name="place">
        <button class="btn btn-outline-success" value="Search" name="search" type="submit">Search</button>
      </form>
    </div>''')
if not check_cookie.login:
    print('''<div class="dropdown">
        <a class="btn btn-secondary dropdown-toggle mx-5" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
            Account
        </a>

        <ul class="dropdown-menu" aria-labelledby="dropdownMenuLink">
            <li><a class="dropdown-item" href="login.py">Login</a></li>
            <li><a class="dropdown-item" href="signup_1.py">SignUp</a></li>
        </ul>
    </div>
    </div>
    </nav><center>
    <a class="btn btn-outline-success btn-lg  mx-5 extra-padding" href="login.py" role="button">Create a New Post</a></center>''')
else:
    print('''<div class="dropdown">
        <a class="btn btn-secondary dropdown-toggle mx-5" href="www.google.com" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
            Account
        </a>

        <ul class="dropdown-menu" aria-labelledby="dropdownMenuLink">
            <li><a class="dropdown-item" href="profile.py">My Profile</a></li>
            <li><a class="dropdown-item" href="notification.py">Notification</a></li>
            <li><a class="dropdown-item" href="#">My Post</a></li>
            <li><a class="dropdown-item" href="logout.py">Logout</a></li>
        </ul>
    </div>
    </div>
    </nav><center>
    <a class="btn btn-outline-success btn-lg  mx-5 extra-padding" href="create-post.py" role="button">Create a New Post</a></center>''')

print('''
<div>
    <div>
        <div>
            <h1>About Us</h1>
            <p>Admee is specially a advertisement website where the user can post their advertise. Here the customer will come and choose their perfect brand.</p>
        </div>
        
        <div>
            <h1>Suggations</h1><form>''')
if not check_cookie.login:
    print('''
                    <table>
                        <tr>
                            <td>Email</td>
                            <td><input type="email" placeholder="abc@gmail.com" name="Email" required>*</td>
                        </tr>
                        <tr>
                            <td>Name</td>
                            <td><input type="text" placeholder="Tushar Maji" name="Name"></td>
                        </tr>
                        <tr>
                            <td>Any Suggations</td>
                            <td><textarea name="Suggations" id="" cols="30" rows="10  required"></textarea>*</td>
                        </tr>
                    </table>''')
else:
    print('''<table>
                <tr>
                            <td>Email</td>
                            <td><input type="email" value="{}" name="Email" required>*</td>
                        </tr>
                        <tr>
                            <td>Name</td>
                            <td><input type="text" value="{}" name="Name"></td>
                        </tr>
                        <tr>
                            <td>Any Suggations</td>
                            <td><textarea name="Suggations" id="" cols="30" rows="10  required"></textarea>*</td>
                        </tr>
                </table>'''.format(check_cookie.u_data[1][2: -1], check_cookie.u_data[3][2:-1]))

print('''<input type="reset">
<input type="submit" name="ok" value="Submit"><br><br>

</form>
</div>
''')
frm = cgi.FieldStorage()
if frm.getvalue('ok'):
    Email = frm.getvalue('Email')
    Name = frm.getvalue('Name')
    Suggations = frm.getvalue('Suggations')
    try:
        cursor = config.database.cursor()
        sql_quarry = "INSERT INTO feedback (Email, Name, Feedback) VALUES ('{}', '{}', '{}')".format(
            Email, Name, Suggations)
        if cursor.execute(sql_quarry):
            print("Suggations Collected")
        config.database.commit()
    except Exception as e:
        print(e)
    finally:
        config.database.close()

print('''
        </div>
        <div>
            <div>
                <img src="../../IMAGE/Tushar.jpg" width="200px" alt="Tushar Image">
                <h3>Tushar Kanti Maji</h3>
            </div>
        </div>
    </div>
</body>
</html>

''')
