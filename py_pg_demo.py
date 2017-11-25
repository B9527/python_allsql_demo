#!/usr/bin/python
# coding:utf-8

"""
项目名：db_project - the name of the current project.
文件名：py_pg_demo - the name of the new file which you specify in the New File dialog box during the file creation.
电脑：Administrator - baiyang
时间：2017/11/25 19:33 
IDE:PyCharm - the name of the IDE in which the file will be created.
"""


# 链接pg
def coonect2pg():
    from config import PgConf
    pg = PgConf(host='192.168.44.149',
                port=5432,
                user='baiyang',
                password='123456',
                database='testdb'
                )
    return pg.connect()


# 选择数据库增加表
def add_table():
    conn = coonect2pg()
    cur = conn.cursor()
    # cur.execute('')
    cur.execute('CREATE TABLE user_tbl(name VARCHAR(20), signup_date DATE);')
    cur.execute("INSERT INTO user_tbl(name, signup_date) VALUES('张三', '2013-12-22');")
    conn.commit()
    conn.close()


if __name__=="__main__":
    add_table()
