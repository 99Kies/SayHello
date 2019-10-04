# import os
# from sayhello import app
#
# dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path),'data.db')
#
# SECRET_KEY = os.getenv('SECRET_KEY','secret string')
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
# # 用于连接数据的数据库。例如：
# # sqlite:////tmp/test.db
# # mysql://username:password@server/db

# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import os
import sys

from sayhello import app

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
DEBUG_TB_INTERCEPT_REDIRECTS = False
# FLASK_ENV=development
