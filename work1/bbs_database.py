from hashlib import sha1

import pymysql

link = pymysql.Connect(host='localhost', port=3306, user='root', password='123', db='bbs', charset='utf8')
cursor = link.cursor(cursor=pymysql.cursors.DictCursor)

try:
    username = input("用户名：")
    password = input("密码：")
    email = input("邮箱：")
    usertype = input("类型：")
    regtime = input("时间：")
    password = sha1(password.encode('utf8')).hexdigest()
    print(username,usertype,password,regtime,email)
    sql = "insert into user(username,usertype,password,regtime,email) values('{}','{}','{}','{}','{}')".format(username,usertype,password,regtime,email)
    result = cursor.execute(sql)
    link.commit()
except Exception as e:
    print(e)
    link.rollback()
finally:
    cursor.close()
    link.close()
