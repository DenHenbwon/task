from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config:
    # 定义和配置同名的调试模式
    DEBUG = True  # 设置调试模式
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3366/jingdong"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 从对象加载配置信息
app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
