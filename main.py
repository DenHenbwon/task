from datetime import timedelta
from flask_script import Manager
from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_session import Session
from flask_migrate import Migrate, MigrateCommand
app = Flask(__name__)


class Config:
    # 定义和配置同名的调试模式
    DEBUG = True  # 设置调试模式
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3366/jingdong"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_HOST = "127.0.0.1"  # 设置redis的ip
    REDIS_PORT = 6379  # 设置redis的端口
    SESSION_TYPE = 'redis'  # session 存储
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # redis 对象
    SESSION_USE_SIGNER = True  # 设置加密
    SECRET_KEY = 'V5948Q3EHtn9bIwYJIQ8qasqzDOTJi3gZ8ZuI27Q7ET3HB7Mi3Iq9w8hJcna7MpL'
    PERMANENT_SESSIOM_LIFETIME = timedelta(days=7) # 设置session 过期时间


# 从对象加载配置信息
app.config.from_object(Config)
db = SQLAlchemy(app)
sr = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
Session(app)

#创建管理器
mgr = Manager(app)
# 初始化迁移器
Migrate(app, db)
# 管理器生成迁移命令
mgr.add_command("mc", MigrateCommand)

@app.route('/')
def index():
    session["age"] = 20
    return 'index'


if __name__== '__main__':
    mgr.run()
