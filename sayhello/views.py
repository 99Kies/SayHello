from flask import flash, redirect, url_for, render_template

from sayhello import app, db
from sayhello.models import Message
from sayhello.forms import HelloForm

@app.route('/',methods=['GET','POST'])
def index():
    # 加载所有记录
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    # 若不加最后的all() 返回的只是SQL语句, 加上all() 返回的就是 排好序的Message
    # print(Message.query.order_by(Message.timestamp.desc()))
    # print('\n')
    # print(messages)
    # 利用order_by()过滤器对数据库记录进行排序, 参数是排序的规则(即按发布的时间戳进行排序),排序方法为desc(),代表降序,asx()为..
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name,body=body) # 实例化模型类, 创建记录(将提交表单的数据转移到数据库中)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    return render_template("index.html",form=form, messages=messages)