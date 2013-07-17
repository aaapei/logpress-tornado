#!/usr/bin/env python
#encoding=utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

DEBUG = False

SITE_NAME = u'aa3pei的自留地'
SITE_KEYWORDS=""""""
SITE_DESC= """少年去游荡"""
DOMAIN='http://127.0.0.1:9000'

THEME_NAME = 'fluid-blue'

DB_ENGINE = 'peewee.SqliteDatabase'  # peewee.SqliteDatabase,peewee.MySQLDatabase
DB_HOST= '127.0.0.1'
DB_USER = 'test'
DB_PASSWD ='test'
#DB_NAME = 'blog' #db file if DB_ENGINE is SqliteDatabase

DB_NAME = os.path.join(os.path.dirname(__file__),'blog.db')  #db file if DB_ENGINE is SqliteDatabase

ADMIN_EMAIL = '594611460@qq.com'
SMTP_SERVER ='smtp.qq.com'
SMTP_PORT = 587
SMTP_USER = 'noreply@szgeist.com'
SMTP_PASSWORD = 'xxxxxx'
SMTP_USETLS = True
