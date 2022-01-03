#!C:/Python/python

import config
import cgi
import cgitb
import check_cookie
cgitb.enable()

cursor = config.database.cursor()
frm = cgi.FieldStorage()


print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Post | Admme</title>
    <link rel="stylesheet" href="../CSS/home-page.css">
    <script src="../JAVA SCRIPT/home-page.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link href="../CSS/home-page.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
</head>
<body>''')
# c_id = frm.getvalue('msg')
# print(c_id)
if frm.getvalue('msg'):
    c_id = frm.getvalue('msg')

    file_write = open('../TXT/c_id.txt', 'w')
    file_write.write(c_id)
    file_write.close()

    # print(c_id, 'done-1')
    sql_quarry = "SELECT * FROM `content` WHERE Content_id = '{}'".format(c_id)
    cursor.execute(sql_quarry)
    story = cursor.fetchall()
    # print(story)
    print('''<div><center>
            <form>
                <br><br>
                <input type="submit" name="notok" value="Delete Post" class="btn btn-outline-danger btn-lg  mx-5 "><br><br><br>
                <table class="table table-dark">
                    <tr>
                        <td>Destination</td>
                        <td><input type="text" class="form-control" name="Destination" value="{}" required>*</td>
                    </tr>
                    <tr>
                        <td>Title</td>
                        <td><input type="text" class="form-control" name="Title" value="{}" required>*</td>
                    </tr>
                    <tr>
                        <td>Description</td>
                        <td><textarea name="Description" class="form-control" id="" cols="30" rows="10" required>{}</textarea>*</td>
                    </tr>
                </table>
                <input type="reset" class="btn btn-outline-warning btn-lg  mx-5 ">
                <input type="submit" name="ok" value="Update" class="btn btn-outline-success btn-lg  mx-5 "> </center>
            </form>
        </div>'''.format(story[0][2], story[0][3], story[0][4]))
# print(c_id)
if frm.getvalue('ok'):
    file_read = open('../TXT/c_id.txt', 'r')
    c_id = file_read.read()
    file_read.close()

    file_write = open('../TXT/c_id', 'w')
    file_write.write('')
    file_write.close()

    print(c_id, "Value of cid")
    # c_id = int(c_id)
    Destination = frm.getvalue('Destination')
    # print(1)
    # print(c_id)
    Title = frm.getvalue('Title')
    Description = frm.getvalue('Description')
    # print(2)
    if "'" in Destination or "'" in Title or "'" in Description:
        print("Pls Don't enter ' in the vacent field. Here you have given   '   . Don't give it. Our database can't take any special character. We are really sorry for that.")
        # print(3)
    else:
        # print(4)
        try:
            cursor = config.database.cursor()
            # print(5)
            # print(Destination, Title, Description, c_id)
            sql_quarry = "UPDATE `content` SET `Product`='{}',`Company`='{}',`Description`='{}' WHERE `Content_id`='{}'".format(Destination, Title, Description, c_id)
            # print(6)
            if cursor.execute(sql_quarry):
                print('''<script>
                alert("Succesfully updated");
                window.location = "my_post.py"
                </script>
                ''')
                # print(7)
            # else:
                # print('No')
            config.database.commit()
            # print(8)
        except Exception as e:
            print(e)
            print("Not posted")
        finally:
            config.database.close()

if frm.getvalue('notok'):
    file_read = open('../TXT/c_id.txt', 'r')
    c_id = file_read.read()
    file_read.close()

    file_write = open('../TXT/c_id', 'w')
    file_write.write('')
    file_write.close()

    try:
        cursor = config.database.cursor()
        # sql_quarry = "UPDATE `content` SET `Product`='{}',`Company`='{}',`Description`='{}' WHERE `Content_id`='{}'".format(Destination, Title, Description, c_id)
        sql_quarry = "DELETE FROM `content` WHERE `Content_id`='{}'".format(c_id)
        if cursor.execute(sql_quarry):
            print('''<script>
            alert("Succesfully Deleted");
            window.location = "my_post.py"
            </script>
            ''')
            # print(7)
        # else:
            # print('No')
        config.database.commit()
        # print(8)
    except Exception as e:
        print(e)
        print("Not posted")
    finally:
        config.database.close()


print('''
</body>
''')