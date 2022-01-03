#!C:/Python/python

import config
import cgi
import cgitb
import check_cookie
cgitb.enable()

cursor = config.database.cursor()
frm = cgi.FieldStorage()


def print_content(content_values):

    sql_quarry_6 = "SELECT * FROM `user` WHERE `User-id`= {}".format(
        content_values[1])
    cursor.execute(sql_quarry_6)
    user_name = cursor.fetchall()

    print('''<h6> <b>Advertiser : </b>{} </h6>'''.format(user_name[0][3]))
    print('''<div class="content"><h3> <b>Product : </b>{}</h3>'''.format(content_values[2]))
    print('''<h1> <b>Brand : </b>{}</h2>'''.format(content_values[3]))
    print(content_values[4])

    print('''<br><br><center><a class="btn btn-outline-danger btn-lg  mx-5 " href="edit_post.py?msg={}" role="button">Edit Post</a></center>'''.format(content_values[0]))

    # print('''<h5> {} </h5>'''.format(user_sname[0][3]))
    # print('''<h5> {} </h5>'''.format(content_values[2]))
    # print('''<div class="content"><h3>{}</h3>'''.format(content_values[3]))
    # print('''<h3>{}</h3>'''.format(content_values[4]))
    # print(content_values[4])
    print('''<hr>''')
    # print('''<div class = "accordion-header" id = "flush-headingOne" >
    # <button class = "accordion-button collapsed" type = "button" data-bs-toggle = "collapse" data-bs-target = "#flush-collapseOne" aria-expanded = "false" aria-controls = "flush-collapseOne" >
    # <h3> {} </h3><br>
    # <h4> {} </h4><br>
    # <h1> {} </h1>
    # </button >
    # </div >
    # <div id="flush-collapseOne" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#accordionFlushExample">
    #   <div class="accordion-body">{}</div>
    # </div>'''.format(user_name[0][3], content_values[3], content_values[4], content_values[5]))


print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Post | Admme</title>
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
# print(1)
# print('''<div class = "row align-items-center" >
#    <div class = "col" >
#     One of three columns
#     </div >
#     <div class = "col" >
#     One of three columns
#     </div >
#     <div class = "col" >
#     One of three columns
#     </div >
#   </div >''')
print('''<div class = "row align-items-center" >
    <div class = "col" >''')
sql_quarry_1 = "SELECT MAX(Content_id) FROM `content` WHERE user_id = {}".format(
    check_cookie.u_data[0][1:])
sql_quarry_2 = "SELECT MIN(Content_id) FROM `content` WHERE user_id = {}".format(
    check_cookie.u_data[0][1:])
cursor.execute(sql_quarry_1)
Content_id_max = cursor.fetchall()
cursor.execute(sql_quarry_2)
Content_id_min = cursor.fetchall()
# print(2)
# print('''<div class="container">''')
# print('''<div class="accordion " id="accordionFlushExample">''')
if Content_id_max[0][0] != None:
    # print(3)
    for item in range(Content_id_max[0][0], (Content_id_min[0][0]-1), -1):
        # print(4)
        sql_quarry = "SELECT * FROM `content` WHERE Content_id = '{}'".format(
            item)
        cursor.execute(sql_quarry)
        story = cursor.fetchall()
        if story:
            # print('''<div class="accordion-item">''')
            print_content(story[0])
            # print('''</div>''')
print('''</div >
# <div class = "col" >''')
# sql_quarry_3 = "SELECT MAX(Approved_id) FROM `content_approved` WHERE user_id = {}".format(
#     check_cookie.u_data[0][1:])
# sql_quarry_4 = "SELECT MIN(Approved_id) FROM `content_approved` WHERE user_id = {}".format(
#     check_cookie.u_data[0][1:])
# cursor.execute(sql_quarry_3)
# Approved_id_max = cursor.fetchall()
# cursor.execute(sql_quarry_4)
# Approved_id_min = cursor.fetchall()
# # print('''<div class="container">''')
# # print('''<div class="accordion " id="accordionFlushExample">''')
# if Approved_id_max[0][0] != None:
#     for item in range(Approved_id_max[0][0], (Approved_id_min[0][0]-1), -1):
#         sql_quarry = "SELECT * FROM `content_approved` WHERE Approved_id = '{}'".format(
#             item)
#         cursor.execute(sql_quarry)
#         story = cursor.fetchall()
#         if story:
#             # print('''<div class="accordion-item">''')
#             print_content(story[0])
#             # print('''</div>''')
# print('''</div >
#     <div class = "col" >''')
# # print(5)
# sql_quarry_5 = "SELECT MAX(Blocked_id) FROM `content_blocked` WHERE user_id = {}".format(
#     check_cookie.u_data[0][1:])
# sql_quarry_6 = "SELECT MIN(Blocked_id) FROM `content_blocked` WHERE user_id = {}".format(
#     check_cookie.u_data[0][1:])
# cursor.execute(sql_quarry_5)
# Blocked_id_max = cursor.fetchall()
# cursor.execute(sql_quarry_6)
# Blocked_id_min = cursor.fetchall()
# print(6)
# # print('''<div class="container">''')
# # print('''<div class="accordion " id="accordionFlushExample">''')
# if Blocked_id_max[0][0] != None:
#     print(7)
#     for item in range(Blocked_id_max[0][0], (Blocked_id_min[0][0]-1), -1):
#         sql_quarry = "SELECT * FROM `content_blocked` WHERE Blocked_id = '{}'".format(
#             item)
#         cursor.execute(sql_quarry)
#         story = cursor.fetchall()
#         if story:
#             # print('''<div class="accordion-item">''')
#             print_content(story[0])
#             # print('''</div>''')
print('''</div >
</div>''')


print('''
</div>
</body>
</ html>
''')
