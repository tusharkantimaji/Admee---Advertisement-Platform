#!C:\Python\python
import check_cookie
import config
import cgitb
import cgi
cgitb.enable()
cursor = config.database.cursor()
frm = cgi.FieldStorage()
searched = False
like = 0
dislike = 0


def print_content(content_values):

    sql_quarry_6 = "SELECT * FROM `user` WHERE `User-id`= {}".format(
        content_values[1])
    cursor.execute(sql_quarry_6)
    user_name = cursor.fetchall()

    print('''<h6> <b>Advertiser : </b>{} </h6>'''.format(user_name[0][3]))
    print('''<div class="content"><h3> <b>Product : </b>{}</h3>'''.format(content_values[2]))
    print('''<h1> <b>Brand : </b>{}</h2>'''.format(content_values[3]))
    print(content_values[4])

    try:
        to_id = content_values[2]
        file = open("../TEXT/store_user_id_to_like.txt", 'w')
        file.write(to_id)
        file.close()
        file = open("../TEXT/store_user_id_to_like.txt", 'a')
        file.write(" " + content_values[1])
        file.close()
        print(1)
        print('''<br>
                <button id="like" value="i_liked" onclick="i_like()">Like(<span id="like_count"></span>)</button>
                <button id="dislike">Dislike()</button>
                <div><br>
                ''')
        print('''<hr>''')
        print(2)
    except:
        print(3)
        print(Exception)
        print('''<hr>''')


print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page | Admee</title>
    <link rel="stylesheet" href="../CSS/home-page.css">
    <script src="../JAVA SCRIPT/home-page.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link href="../CSS/home-page.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
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
    <a class="btn btn-outline-success btn-lg  mx-5 extra-padding" href="login.py" role="button">Create a New Advertisement</a></center>''')
else:
    print('''<div class="dropdown">
        <a class="btn btn-secondary dropdown-toggle mx-5" href="www.google.com" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
            Account
        </a>

        <ul class="dropdown-menu" aria-labelledby="dropdownMenuLink">
            <li><a class="dropdown-item" href="profile.py">My Profile</a></li>
            <li><a class="dropdown-item" href="notification.py">Notification</a></li>
            <li><a class="dropdown-item" href="my_post.py">My Post</a></li>
            <li><a class="dropdown-item" href="logout.py">Logout</a></li>
        </ul>
    </div>
    </div>
    </nav><center>
    <a class="btn btn-outline-success btn-lg  mx-5 extra-padding" href="create-post.py" role="button">Create a New Advertisement</a></center>''')


if frm.getvalue('search'):
    sql_quarry_3 = "SELECT * FROM `content` WHERE Product = '{}'".format(
        frm.getvalue('place'))
    cursor.execute(sql_quarry_3)
    sorted_place = cursor.fetchall()
    searched = True
    # print('''<div class="accordion " id="accordionFlushExample">''')
    for j in sorted_place:
        print_content(j)

if not searched:
    sql_quarry_1 = "SELECT MAX(Content_id) FROM `content`"
    sql_quarry_2 = "SELECT MIN(Content_id) FROM `content`"
    cursor.execute(sql_quarry_1)
    content_id_max = cursor.fetchall()
    cursor.execute(sql_quarry_2)
    content_id_min = cursor.fetchall()
    print('''<div class="container">''')
    print('''<div class="accordion " id="accordionFlushExample">''')
    if content_id_max[0][0] != None:
        for item in range(content_id_max[0][0], (content_id_min[0][0]-1), -1):
            sql_quarry = "SELECT * FROM `content` WHERE Content_id = '{}'".format(
                item)
            cursor.execute(sql_quarry)
            story = cursor.fetchall()
            if story:
                # print('''<div class="accordion-item">''')
                print_content(story[0])
                # print('''</div>''')
print('''
</div>
</body>
</ html>
''')
