#!C:/Python/python
import check_cookie
import config

from_id = int(check_cookie.u_data[0][1:])
cursor = config.database.cursor()

file = open("../TEXT/store_user_id_to_like.txt", 'r')
to_id_content_id = file.write()
file.close()
to_id_content_id.split(' ')
to_id = to_id_content_id[0]
content_id = to_id_content_id[1]
sql_quarry_1 = "INSERT INTO `notification`(`User_id_from`, `User_id_to`, `Post_id`, `Msg_type`, `Message`) VALUES ('{}','{}','{}','{}','{}')".format(
    from_id, to_id, content_id, 1, "Like")

cursor.execute(sql_quarry_1)
