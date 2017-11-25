#!/usr/bin/python
# coding:utf-8

"""
项目名：db_project - the name of the current project.
文件名：py_mysql_demo - the name of the new file which you specify in the New File dialog box during the file creation.
电脑：Administrator - baiyang
时间：2017/11/25 18:31 
IDE:PyCharm - the name of the IDE in which the file will be created.
"""
from config import MysqlConf
mysql = MysqlConf(host='192.168.44.149',
                  port=3306,
                  user='root',
                  password='123456'
                  )
conn = mysql.connect()
curs = conn.cursor()
curs.execute('drop database if EXISTS testdb;')
curs.execute('create database testdb;')
# 选择数据库
conn.select_db('testdb')
curs.execute('create table test(id int ,message VARCHAR (50));')
# 插入单条数据
value = [1, 'root']
curs.execute('insert into test VALUES (%s,%s);', value)
# 插入多条数据
values = []
for i in range(20):
    values.append((i, 'hello mysqldb' + str(i)))
curs.executemany('insert into test VALUES (%s,%s);', values)
conn.commit()
curs.close()
conn.close()
