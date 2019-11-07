from hashlib import sha1

import pymysql

link = pymysql.Connect(host='localhost', port=3306, user='root', password='123', db='bbs', charset='utf8')
cursor = link.cursor(cursor=pymysql.cursors.DictCursor)
name1= input("用户名：")
password1 = input("密码：")
password1 = sha1(password1.encode('utf8')).hexdigest()
sql = "select username,password from user where username='name1' and password='password1'"
result = cursor.execute(sql)
if result>0:
    print("登录成功")
else:
    print("登录失败")

