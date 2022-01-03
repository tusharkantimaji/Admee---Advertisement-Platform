#!C:/Python/python
import cgi
import config
import check_cookie
import cgitb
import os
import http.cookies

cgitb.enable()

frm = cgi.FieldStorage()

Destination = frm.getvalue('Destination')
Title = frm.getvalue('Title')
Description = frm.getvalue('Description')

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Post | Tourexp</title>
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
  <img src="../../IMAGE/logo.png" width="150px" alt="logo">
    <a class="navbar-brand" href="#">Travel Crew</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav me-auto mb-2 mb-lg-0">

        <li class="nav-item">
          <a class="nav-link" href="index.py">Starting Page</a>
        </li>
         <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="home-page.py">Home</a>
        </li>

        <li class="nav-item">
          <a class="nav-link" href="about-us.py">About Us</a>
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
    <a class="btn btn-outline-success btn-lg  mx-5 extra-padding" href="create-post.py" role="button">Create a New Post</a></center>
''')
    if Destination and Title and Destination:
        print('''<div>
            <form>
                <table>
                    <tr>
                        <td>Destination</td>
                        <td><input type="text" name="Destination" value="{}" required>*</td>
                    </tr>
                    <tr>
                        <td>Title</td>
                        <td><input type="text" name="Title" value="{}" required>*</td>
                    </tr>
                    <tr>
                        <td>Description</td>
                        <td><textarea name="Description" id="" cols="30" rows="10" required>{}</textarea>*</td>
                    </tr>
                </table>
                <input type="reset">
                <input type="submit" name="ok" value="Post">
            </form>
        </div>'''.format(Destination, Title, Description))
    else:
        print('''<div>
        <form>
            <table>
                <tr>
                    <td>Destination</td>
                    <td><input type="text" name="Destination" placeholder="Manali" required>*</td>
                </tr>
                <tr>
                    <td>Title</td>
                    <td><input type="text" name="Title" placeholder="Manali Wondered me" required>*</td>
                </tr>
                <tr>
                    <td>Description</td>
                    <td><textarea name="Description" id="" cols="30" rows="10" required></textarea>*</td>
                </tr>
            </table>
            <input type="reset">
            <input type="submit" name="ok" value="Post">
        </form>
    </div>''')
    print('''<a href="home-page.py">Back to Home Page</a>
''')

cookie_str = os.environ.get('HTTP_COOKIE')
c = http.cookies.SimpleCookie()
c.load(cookie_str)

u_data = c['u_info'].value.split(',')


if frm.getvalue('ok'):
    Destination = frm.getvalue('Destination')
    Title = frm.getvalue('Title')
    Description = frm.getvalue('Description')
    if "'" in Destination or "'" in Title or "'" in Description:
        print("Pls Don't enter ' in the vacent field. Here you have given   '   . Don't give it. Our database can't take any special character. We are really sorry for that.")
    else:
        try:
            cursor = config.database.cursor()
            sql_quarry = "INSERT INTO content (User_id, Product, Company, Description) VALUES ('{}', '{}', '{}', '{}')".format(
                int(u_data[0][1:]), Destination, Title, Description)
            if cursor.execute(sql_quarry):
                print('''<script>
                alert("Succesfully posted");
                window.location = "home-page.py"
                </script>
                ''')
            config.database.commit()
        except Exception as e:
            print(e)
            print("Not posted")
        finally:
            config.database.close()
print('''
</body>
</html>

''')
