from datetime import datetime

from sayhello import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    # timestamp用于储存时间戳（发布文章的时间），这个字段存储了datetime对象，index=True来开启索引，用default来设置默认值
    # 是datetime.now而不是datetime.now()。。。前者是可调用函数/方法对象(即名称),而后者是函数/方法调用(即动作).
    # SQLAlchemy会在创建新的数据库记录时(即用户提交表单实例化Message类时)调用该对象来设置默认值, 即达到了我们需要的内容
    # 如果传入的不是方法对象, 那么这个方法在加载模块时就会被执行, 这就不是正确的时间戳
    # 使用datetime.utcnow来生成当前的UTC,UTC格式时间就是不包含时区信息的纯正时间
