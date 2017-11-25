#!/usr/bin/python
# coding:utf-8

"""
项目名：db_project - the name of the current project.
文件名：config - the name of the new file which you specify in the New File dialog box during the file creation.
电脑：Administrator - baiyang
时间：2017/11/25 18:41 
IDE:PyCharm - the name of the IDE in which the file will be created.
"""


class MysqlConf(object):
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def connect(self):
        import pymysql
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password)
        return conn


class PgConf(object):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        import psycopg2
        conn = psycopg2.connect(host=self.host, port=self.port, user=self.user, password=self.password,database=self.database)
        return conn


class MgConf(object):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password
        self.database = database