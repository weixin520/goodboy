import pymysql

link = pymysql.Connect(host='localhost', port=3306, user='root', password='123', charset='utf8')
cursor = link.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'create database bbs'
cursor.execute(sql)
sql = 'use bbs'
cursor.execute(sql)
sql = "create table if not exists user(uid int  primary key auto_increment,\
       username varchar(10) unique not null,usertype enum('普通用户','管理员') default '普通用户', password varchar(100) not null,\
       regtime datetime not null,email varchar(30))"
cursor.execute(sql)
cursor.close()
link.close()