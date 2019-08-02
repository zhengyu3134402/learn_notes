# -i https://pypi.douban.com/simple



# HTTP通讯过程
1
#     tcp传输
#         浏览器---发起HTTP请求(请求报文 请求头 请求体) ---> django--->
#         返回HTTP响应(响应报文 起始行 响应头 响应体)--->浏览器
#
#     django做的事情
#         接收从前端发送过来的请求
#         解析http报文
#         进行路由分发
#         根据用户请求的url
#         执行对应的视图函数
#         将视图函数返回值打包成http响应报文
#         借助刚才建立好的tcp链接将响应回传
#
1

# web框架
1
#     核心功能: 实现路由和视图
#
#
# 框架的轻重
#     重量级框架 django
#     轻量级框架 flask Tornado(自由灵活)
#
1

# Flask
#
#     1 介绍
1
#         flask框架核心是Werkzeug和Jinja2
#         flask.pocoo.org/docs/0.11/
#     1.1 安装
#         pip3 install flask
#
#     2 扩展包
#
#         Flask-SQLalchemy 操作数据库
#         Flask-migrate 管理迁移数据库
#         Flask-Mail 邮件
#         Flask-WTF 表单
#         Flask-script 插入脚本
#         Flask-Login 认证用户状态
#         Flask-RESTful 开发REST API的工具
#         Flask-Boostrap 集成前段Twitter Bootstrap框架
#         Flask-Moment 本地化日期和时间
1
#     3 虚拟环境创建
1
#         查看 06-操作系统笔记.py
#
#         1 收集虚拟环境中的安装包
#             pip3 freeze > requirements.txt
#         2 安装收集的所有安装包
#             pip3 install -r requeirements.txt
1
#     4 flask基本程序
1
#         from flask import Flask
#
#         # 创建flask应用对象
#         # __name__当前模块名字：
#         #       flask以这个模块所在的目录为总目录,
#         #       默认这个目录中的static为静态目录,
#         #       templates为模板目录
#
#         app = Flask(__name__)
#
#
#         @app.route("/")
#         def index():
#             return 'hello'
#
#
#         if __name__ == '__main__':
#             # 启动flask程序
#             app.run()
1
#     5 应用参数
1
#
#         1 Flask(参数)
#             参数
#                 import_name: 导入路径(寻找静态目录与模板目录位置的参数)
#                 static_url_path: 访问静态资源url前缀, 默认值是static
#                 static_folder: 静态文件目录, 默认static
#                 template_folder: 模板文件目录, 默认templates
#         2 app.run()的启动参数
#
#             配置启动ip端口
#                 app.run(host='0.0.0.0', port=5000) # 0.0.0.0 任何本机ip
#             配置debug
#                 app.run(debug=True)
1
#     6 配置相关
1
#         1 配置
#             方式1
#
#                 1 创建配置文件
#
#                     xxx.cfg
#                         文件中写入配置参数如DEBUG=True
#                 2 使用配置文件
#
#                     app.config.from_pytfile("config.cfg")
#
#             方式2
#
#                 1 创建类
#                     class Config:
#                         DEBUG=True
#                 2 使用配置的类
#                     app.config.from_object(Config)
#
#             方式3
#
#                 app.config["DEBUG"]=True
#
#         2 获取配置文件中的参数
#
#             方式1
#                 app.config.get(xx)
#
#             方式2
#                 from flask import current_app
#                 current_app.config.get(xx)
1
#     7 路由相关
1
#         1 获取flask路由信息
#             app.url_map
#
#         2 限定访问方式
#
#             @app.route("/xx", methods=["GET", "POST"])
#             def xx():
#                 return 'xxxxx'
#
#         3 同一路由使用不同函数
#
#             用 methods=['GET'] methods= ['POST']控制
#
#         4 不同路由使用同意函数
#
#             @app.route('/a')
#             @app.route('/b')
#             def xx():
#                 return 'xxx'
#
#         5 反向解析
#
#             from flask import redirect, url_for
#
#             def xx():
#                 url = url_for("函数名")
#                 return redirect(url)
#
#         6 获取参数(转换器)
#
#             @app.route("/a/<int:id>")
#             def a(id):
#                 return 'aa'
#             或
#             @app.route("/a/<id>")
#             def a(id):
#                 return 'aa'
#
#         7 自定义路由匹配规则(自定义转换器)
#
#             1 创建类继承BaseConverter
#                 from werkzeug.routing import BaseConverter
#                 class A(BaseConverter):
#
#                     def __init__(self, url_map, regex):
#                         # 将正则表达式的参数保存到对象的属性中,
#                         # flask会去使用这个属性来进行路由的正则匹配
#                         self.regex = regex
#                         super().__init__(url_map)
#
#                     def to_python(self, value):  # 如果有需要 可以写,省略也可
#                         return '这个返回的值就是路由函数中接收的值'
#

#                     def to_url(self, value):  # 使用url_for方法的时候被调用
#                         return 'url_for的值'

#             2 将自定义转换器添加到flask的应用中
#                 app.url_map.converters["re"] = A
#
#             3 使用
#                 @app.route("/a/<re(r'匹配规则'):bbb>")
#                 def s(bbb):
#                     return 'xxxxx'
1
        # 8 request
        1
        #     from flask import request
        #
        #     # 获取请求体数据
        #     request.data
        #
        #     # 获取表单中数据, 类字典格式
        #     request.form
        #
        #     # 获取url参数, 类字典格式
        #     request.args
        #
        #     # 获取同名key的方法
        #     request.data.getlist("xx")
        #     request.form.getlist("xx")
        #     request.args.getlist("xx")
        #
        #     # 获取请求中的cookies信息
        #     request.cookies
        #
        #     # 获取请求中的报文头
        #     request.headers
        #
        #     # 获取请求使用的HTTP方法
        #     request.method
        #
        #     # 获取请求的url地址
        #     request.url
        #
        #     # 获取请求的上传文件
        #     request.files
        #
        #     # 如果前段发送的请求数据是json格式 会解析成字典
        #     a = request.get_json()
        #
        1
        # 9 获取上传文件并保存
        1
        #     # 得到的是类似文件句柄类型
        #     a = request.files.get('xx')
        #     # 保存文件
        #     a.save("路径")
        1
        # 10 abort函数
        1
        #     from flask import abort, Response
        #     # 终止视图执行 返回给前端信息
        #
        #     # 返回状态码, 必须是标准的http状态码
        #     abort(404)
        #
        #     # 返回信息
        #     abort(Response('xx'))
        1
        # 11 自定义异常处理
        1
        #     @app.errorhandler(404)
        #     def handle_404_error(err):
        #         return '40411'
        1
        # 12 响应信息处理
        1
        #     # 方法1
        #         # 使用元祖返回自定义响应信息
        #             # 响应体, 状态码, 响应头
        #         return "xx", 200, [("a", "1"),("b","2")]
        #         或
        #         return "xx", 200, {"a":1, "b":2}
        #             # 响应体, "状态码 状态码描述信息", 响应头
        #         return "xx", "200 哈哈", {"a":1, "b":2}
        #
        #     # 方法2
        #
        #         from flask import make_response
        #
        #         resp = make_response("xx") # 响应体
        #         resp.status = "999 vv" # 设置状态码
        #         resp.headers["a"] = 1 # 设置响应头
        #
        #         return resp
        1
        # 13 返回json数据
        1
        #     from flask import jsonify
        #
        #     a = {"a":1}
        #     return jsonify(a)
        1
        # 14 cookie的使用
        1
        #     原理
        #         在响应头设置了Set_cookie: xxxxxx 的值
        #
        #     from flask import make_response
        #
        #     # 设置cookie, 默认临时会话
        #     a = make_response("aa")
        #     a.set_cookie("a", "1", max_age=None)
        #     return a
        #
        #     # 获取cookie
        #     request.cookies.get("xx")
        #
        #     # 删除cookie
        #     a.delete_cookie("a")
        #     return a
        1
        # 15 session
        1
        #     # 1 session的机制
        #
        #         flask默认把session默认保存到了cookie中
        #         在前段当中保存session id 在后端当中保存session id的值
        #
        #         如果没有cookie也可以 使用session(放到url中, 局限性, 不能设置过期时间)
        #
        #
        #     # 2 使用session
        #         from flask import session
        #
        #         # 需要用秘钥
        #         app.config["SECRET_KEY"] = "FSVXVSAFSADF"
        #
        #         # 设置session
        #         session['a'] = "11"
        #
        #         # 获取session
        #         session.get("a")
        1
        # 16 请求钩子
        1
        #     @app.before_first_request # 在第一次请求处理之前
        #     def a():
        #         xx
        #
        #     @app.before_request # 在每次请求之前
        #     def a():
        #         xx
        #
        #     @app.after_request # 视图函数无异常, 在每次请求之后执行
        #     def a(response):
        #         xx
        #         return response
        #
        #     @app.teardown_request # 视图函数有异常, 在每次请求之后执行(调试模式下不起作用)
        #     def a(response):
        #         xx
        #         return response
        1
        # 17 请求上下文和应用上下文
        1
        #     上下文概念
        #         同样的代码 操作同一个对象, 执行的时候, 得到的值根据执行时候得具体环境有关系
        #
        #     请求上下文
        #
        #         request, session
        #
        #     应用上下文
        #
        #         current_app , g
        #
        #     实现上下文的原理
        #
        #         全局变量-线程局部变量
        #
        #         request = {
        #             "线程编号A":{
        #                 form:{"a":1}
        #             }
        #             "线程编号B":{
        #                 form:{"b":1}
        #             }
        #         }
        #
        #     g变量 临时存储数据用
        #         g.aa = "aa"
        #
        #         函数之间传递变量用, 每次处理请求之后自动清空
        #         def a():
        #
        #             g.aa = 1
        #
        #         def b():
        #             print(g.aa)
        1
        # 18 Flask-Script扩展命令行工具
        1
        #     1 安装
        #         pip3 install flask-script
        #
        #     2 使用
        #
        #         from flask_script import Manager # 启动命令管理类
        #
        #         # 创建管理类对象
        #         manage = Manager(app)
        #
        #         # 启动管理对象
        #         manage.run()
        #
        #         # 执行启动命令
        #         python 文件名 runserver
        #
        #         # shell
        #         python 文件名 shell
        1
        # 19 jinja2 模板
        1
        #     1 变量
        #         {{ name }}
        #
        #     2 渲染模板
        #
        #         from flask import render_template
        #
        #         return render_template("xx.html")
        #
        #         传递参数
        #
        #             return render_template("index.html",a=1)
        #             或
        #             return render_template("index.html",**a)
        #
        #     3 模板中获取值
        #
        #         data = {
        #             "a":"aaa",
        #             "b":1,
        #             "c":{"cccc":4},
        #             "d":[1,2,3,4],
        #             "e":0
        #         }
        #         return render_template("index.html",**data)
        #
        #         {{c["cccc"]}}
        #         {{c.cccc}}
        #         {{d}}
        #         {{d[e]}}
        #
        #         {{ d[0]+d[1] }} # 数字加法, 字符串加法

        #     4 过滤器
        #
        #         {{ '<p>sss</p>'|safe }} # 禁止转义
        #
        #         {{ " flask world "|trim|upper }} # 可链式
        #         ....
        #
        #         1 列表过滤器
        #
        #             取第一个元素
        #             {{ [1,2,3,4,5]|first }}
        #
        #             取最后一个元素
        #             {{ [1,2,3,4,5]|last }}
        #
        #             获取列表长度
        #             {{ [1,2,3,4,5]|length }}
        #
        #             列表求和
        #             {{ [1,2,3,4,5]|sum }}
        #
        #             列表排序
        #             {{ [1,2,3,4,5]|sort }}
        #
        #         2 自定义过滤器
        #
        #             方式1
        #
        #                 1 定义函数
        #                     def a(li):
        #
        #                         return li[::2]
        #                 2 注册过滤器
        #                     app.add_template_filter(a, "xx") # 参数1 函数 参数2 模板中使用的名字
        #
        #                 3 模板使用
        #                     {{ listxx|xx }}
        #
        #             方式2
        #
        #             1 定义函数, 用装饰器注册并命名
        #
        #             @app.template_filter("xx")
        #             def a(li):
        #                 return li[::2]
        #     5 模板的继承
        #
        #         extend
        #
        #     6 模板的包含
        #
        #         # 与extend为相反的操作
        #         include
        #
        #     7 flask中的特殊变量(可以模板中直接访问)
        #
        #         1 config对象
        #         2 request对象
        #         3 url_for方法
        #            {{ url_for('book_delete', id=book.id) }}
        #
        #     8 模板中的闪现
        #
        #         1 作用
        #             是用户就能看到一次的提示消息
        #
        #         2 使用
        #             视图
        #                 def a():
        #
        #                     flash("111")
        #                     flash("222")
        #                     return xx
        #             模板
        #                 {% for message in get_flashed_messages() %}
        #                     {{ message }}
        #                 {% endfor %}
        1
        # 20 flask-wtf表单
        1
        #     1 介绍
        #         校验数据
        #         快速生成前端
        #         完成csrf_token验证工作
        #
        #     2 pip3 install flask-wtf
        #
        #     3 使用
        #
        #         1 定义表单模型类
        #             from flask_wtf import FlaskForm
        #             from wtforms import StringField, PasswordField, SubmitField
        #             from wtforms.validators import DataRequired,EqualTo
        #             class AForm(FlaskForm):
        #
        #                 username = StringField(label="用户名", validators=[DataRequired(message="用户名不能为空")])
        #                 password = PasswordField(label="密码", validators=[DataRequired(message="密码不能为空")])
        #                 re_password = PasswordField(label="确认密码", validators=[DataRequired(message="密码不能为空"), EqualTo("password", message="两次输入密码不一致")])
        #                 submit = SubmitField(label="提交")
        #         2 使用表单类渲染
        #
        #             form = AForm()
        #             return render_template("xx.html", form=form)
        #
        #             模板中
        #
        #                 # csrf认证
        #                 {{ form.csrf_token }}
        #
        #                 # 展示表单字段
        #                 {{ form.username.label }} {{ form.username }}
        #
        #                 # 显示表单错误信息
        #                 {% for i in form.username.errors %}
        #                     {{ i }}
        #                 {% endfor %}
        #
        #                 # 展示表单字段
        #                 {{ form.submit }}
        #
        #             3 使用表单类验证
        #
        #                 form = AForm()
        #                 if form.validate_on_submit():
        #                     return '验证成功'
        #
        #             4 表单类提取数据
        #
        #                 form = AForm()
        #                 if form.validate_on_submit():
        #
        #                     username = form.username.data
        #
        #             5 宏
        #
        #                 1 作用
        #                     模板中的函数
        #
        #                 2 创建宏
        #                     1 不带参数的宏
        #                         {% macro xx() %}
        #                             <input type="text">
        #                         {% endmarco %}
        #                     2 带参数的宏
        #                         {% macro xx(a) %}
        #                             <input type="text" value="{{ a }}">
        #                         {% endmarco %}
        #                     3 带默认参数的宏
        #                         {% macro xx(a=1) %}
        #                             <input type="text" value="{{ a }}">
        #                         {% endmarco %}
        #
        #                 3 使用宏
        #                     不带参数的宏
        #                         {{ xx() }}
        #
        #                     带参数的宏
        #                         {{ xx(2) }}
        #
        #                 4 把宏作为模块
        #
        #                     1 使用html文件, 只写宏即可 其他标签都不要
        #                     2 导入创建的宏
        #                         {% improt 'xx.html' as a %}
        #                         {{ a.yy() }}
        #
        1

        # 21 数据库
        1
        #
        #     1 安装
        #
        #         pip3 install flask-sqlalchemy
        #         pip3 install pymysql
        #
        #     2 配置
        #
        #         class Config:
        #
        #
        #             SQLALCHEMY_DATABASE_URI = "mysql+pymysql://用户名:密码@ip:端口号/数据库名"
        #
        #             # 自动跟踪数据库
        #             SQLALCHEMY_TRACK_MODIFIVACTIONS = True
        #
        #     3 注册
        #
        #         from flask_sqlalchemy import SQLAlchemy
        #         db = SQLAlchemy(app)
        #
        #     4 创建模型类
        #
        #         class User(db.Model):
        #
        #             __tablename__ = "test_users"
        #
        #             id = db.Column(db.Integer, primary_key=True) # 整型的主键, 会默认设置为自增主键
        #             name = db.Column(db.String(64), unique=True)
        #             email = db.Column(db.String(128), unique=True)
        #             password = db.Column(db.String(128))
        #             role_id = db.Column(db.Integer, db.ForeignKey("test_roles.id"))
        #
        #
        #         class Role(db.model):
        #
        #             __tablename__ = "test_roles"
        #
        #             id = db.Column(db.Integer, primary_key=True)  # 整型的主键, 会默认设置为自增主键
        #             name = db.Column(db.String(32), unique=True)
        #             users = db.relationship("User", backref="role") # role.users 获取所有该角色用户 backref-->user.role获取对象
        #     5 创建表
        #
        #         # 清除数据库里的所有数据
        #         db.drop_all()
        #
        #         # 创建表
        #         db.create_all()
        #
        #     6 增删改查
        #
        #         1 增
        #             a = Role(name="admin")
        #             db.session.add(a)
        #             db.session.commit()
        #
        #             添加多个
        #             db.session.add_all([a,b,c,d])
        #             db.session.commit()
        #             一对多数据添加
        #             author = Author(name=author_name)
        #             db.session.add(author)
        #             db.session.commit()
        #
        #             book = Book(name=book_name, author_id=author.id)
        #             db.session.add(book)
        #             db.session.commit()


        #         2 删
        #
        #             user = User.query.get(1)
        #             db.session.delete(user)
        #             db.session.commit()
        #
        #
        #         3 改
        #
        #             user = User.query.get(1)
        #             user.name = "xx"
        #             db.session.add(user)
        #             db.session.commit()
        #
        #
        #             user = User.query.filter_by(name="xx").update("name":"aaa")
        #             db.session.commit()
        #
        #         4 查
        #             Role.query.all() 或 db.session.query(Role).all()
        #
        #             Role.query.first()
        #
        #             Role.query.get(2) # 参数只能接受主键
        #
        #             Role.query.filter(User.name=="wang")
        #
        #             from sqlalchemy import or_ # 或
        #             User.query.filter(or_(User.name=="wang", User.email.endswith("11")))
        #
        #             Role.query.filter_by(name="wang") #
        #
        #             User.query.offset(2).all() # 从跳过两条数据取所有
        #
        #             User.query.offset(2).limit(2).all() # 跳过两条取两条数据
        #
        #             User.query.order_by("-id").all()
        #             User.query.order_by(User.id.desc()).all() # 降序排序 升序asc()
        #
        #
        #             from sqlalchemy import func
        #             db.session.query(User.role_id, func.count(User.role_id)).group_by(User.role_id).all()  # 分组
        #
        #             # 关联查询
        #
        #                 # 从1向多中查询
        #                     role = Role.query.get(1)
        #                     users = role.users
        #
        #                 # 从多向1中查询
        #                     user = User.quer.get(1)
        #                     user.role
        1

        # 22 flask-migrate数据库迁移工具
        1
            # 1 介绍
            #
            #     数据库迁移工具
            #     配合flask_script使用
            #
            # 1 安装
            #
            #     pip3 install flask-migrate
            #
            # 2 配置
            #
            #     from flask_script import Manager
            #     from flask_migrate import Migrate, MigrateCommand
            #
            #     # 创建对象
            #     manager = Manager()
            #     Migrate(app, db)
            #
            #     # 添加db命令
            #     manager.add_command(('db', MigrateCommand)) # 此db非彼db
            #
            # 3 相关命令
            #
            #     1 迁移模型到数据库3步骤
            #
            #         1 初始化(生成migrations目录)
            #
            #             python3 xx.py db init
            #
            #         2 生成迁移文件
            #
            #             python3 xx.py db migrate
            #             或
            #             添加备注信息的文件迁移
            #             python3 xx.py db migrate -m "备注信息"
            #         3 迁移到数据库
            #
            #             python3 xx.py db upgrade
            #
            #     2 撤回迁移操作
            #
            #         1 查看迁移历史记录
            #
            #             python3 xx.py db history
            #
            #         2 撤回
            #
            #             python3 xx.py db downgrade 查询出来的状态码
        1

        # 23 flask发送邮件
            1
            # 1 安装
            #
            #     pip3 install flask-mail
            #
            # 2 配置
            #
            #     MAIL_SERVER='smtp.pp.com' # 邮件服务器
            #     MAIL_PROT=465   # 服务器对应端口号
            #     MAIL_USE_TLS = True # 传输层安全协议
            #     MAIL_USERNAME = "xx@qq.com" # 用户名
            #     MAIL_PASSWORD = "xxxxx" # 授权密码
            #
            # 3 使用
            #
            #     from mail import Mail, Message
            #
            #     mail = Mail(app)
            #     msg = Message("xx", sender="xxx", recipients=["xxx"])
            #     msg.body = "xxx"
            #     mail.send(msg)
            1
        # 24 蓝图
        1
        #     1 介绍
        #
        #         模块的划分
        #
        #         划分模块 双方进行导入会产生循环导入的问题
        #             解决方法1 是推迟一方的导入（但flask运行之后找
        #                 不到推迟导入的路由及对应的函数）
        #
        #             解决方法2 让路由装饰器变成执行函数接受函数
        #
        #             @app.route("/xxx")
        #             def xxx():
        #                 return "z"
        #             变成
        #             从其他模块中导入xxx函数
        #             app.route("/xxx")(xxx)
        #
        #         蓝图 将 路由和对应函数彻底划分
        #
        #     2 使用
        #
        #         1 创建注册蓝图
        #
        #             1 创建蓝图对象
        #                 xx = Blueprint("蓝图名称", __name__)
        #             2 注册蓝图路由
        #
        #                 @admin.route('/'):
        #                 def xx():
        #                     return 'xx'
        #             3 在程序势力中注册蓝图
        #                 app.register_blueprint(xx, url_prifix="名") # 该名为 xx:8000/名 也可省略
        #                                                             #  省略后变成 xx:8000/蓝图名称
        #         2 以目录形式构建蓝图
        #
        #             1 创建目录 及文件__init__
        #
        #             2 配置__init__.py
        #
        #                 from flask import Blueprint
        #
        #                 xx = Blueprint("xx", __name__)
        #
        #                 # 注册views
        #                 from .views import aa
        #
        #             3 创建views文件
        #
        #                 from . import xx
        #
        #                 @xx.route("/")
        #                 def aa():
        #                     return 'zz'
        #
        #             4 注册蓝图
        #
        #
        #
        #                 主文件
        #                 from 目录 import xx
        #                 app.register_blueprint(xx, url_perfix="/aa")
        #
        #             5 处理蓝图目录中的模板和静态文件
        #
        #                 如果不配置就去主目录中的templates中找
        #                 如果蓝图templates中和朱目录templates中有同名模板目录
        #                     主模板目录优先级高于蓝图模板目录优先级
        #
        #                 __init__文件的蓝图
        #                     xx = Blueprint("xx", __name__, template_folder="templates")
        1
        # 25 单元测试
        1
            # 1 介绍
            #
            #     功能代码完成后, 为了检验其是否满足程序的要求
            #     可以通过编写测试代码, 模拟程序运行的过程, 检验功能
            #     功能代码是否符合预期
            #
            #     使用断言assert
            #
            #         格式
            #             assert 表达式
            #
            #         常用断言方法
            #
            #             assertEqual     如果两个值相等则pass
            #             assertNotEqual  如果两个值不相等则pass
            #             assertTrue      判断bool值为True则pass
            #             assertFalse     判断bool值为False则pass
            #             assertIsNone    不存在则pass
            #             assertIsNotNone 存在则pass
            #
            #         如果断言为真程序正常运行
            #         如果断言为假程序停止运行, 会抛出AssertionError
            #
            #
            #         def a(b,c):
            #             assert isinstance(b, int)
            #             assert isinstance(c, int)
            #             assert c !=0
            #             print(b/c)
            #
            #         a("1", "2")
            #
            # 2 实现简单的单元测试
            #
            #     把想测试的逻辑函数 全部疯子到测试类中
            #     函数方法名字必须以test_为前缀
            #
            #
            #     import unittest
            #     from xxxx import app
            #
            #     class xx(unittest.TestCase):
            #
            #         def setUp(self):
            #             """执行测试之前执行该函数"""
            #             self.client = app.test_client()
            #
            #             # 设置flask工作在测试模式下, 如果被测试的试图出现错误会提示
            #                 # 出精确的测试位置, 如果不开启, 只在本车是类中报错(不精确)
            #             app.testing = True 或 app.config["TESTING"] = True
            #
            #         def test_xx1(self):
            #
            #             # 创建进行web请求的客户端, 使用flask提供的
            #             # client = app.test_client() 可写在setUp函数中
            #
            #             # 利用客户端模拟发送web请求, 返回值为试图响应对象
            #             ret = client.post("/路径", data={数据})
            #
            #             # 响应体数据
            #             resp = ret.data
            #
            #             # 开始断言测试
            #             self.assertIn("aa", resp)
            #             self.assertEqual(resp["code"], 1)
            #
            #     if __name__ == '__main__':
            #         unittest.main()
            #
            # 3 数据库测试
            #
            #     import unittest
            #     from xxxx import app
            #     from xxxxx import Author, db
            #
            #     class xx(unittest.TestCase):
            #
            #         def setUp(self):
            #
            #             app.testing = True
            #
            #             # 构造测试数据库, 并进入mysql创建测试数据库
            #             app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://用户名:密码@ip:端口号/数据库名"
            #
            #             # 创建测试数据库表
            #             db.create_all()
            #         def test_xx(self):
            #             """测试添加作者的数据库操作"""
            #             author = Author(name="yy")
            #             db.session.add(author)
            #             db.session.commit()
            #
            #             result_author = Author.query.filter_by(name="yy").first()
            #             self.assertIsNotNone(result_author)
            #
            #         def tearDown(self):
            #             """所有测试执行后执行tearDown函数, 通常用来清理操作"""
            #
            #             db.session.remove()
            #             db.drop_all()
        1

        # 26 部署
        1
            # 框架
            #     Nginx(负载均衡, 提供静态文件) -->可以多台Gunicorn + Flask-->共享mysql和redis
            #
            #
            # 1 安装gunicorn
            #
            #     pip3 install gunicorn
            #
            # 2 启动gunicorn
            #
            #     1 以执行命令方式运行
            #
            #         1 执行命令
            #
            #             # -w 4 开启4个进程
            #             # -b 绑定端口号
            #             # --access-logfile ./logs/log  获取日志信息放在相对当前文件logs目录下的log文件中
            #             # main:app 使用启动main文件中的 app实例
            #             gunicorn -w 4 -b 127.0.0.1:5000 --access-logfile ./logs/log main:app
            #
            #     2 以后台形式运行
            #
            #         # -D 以后台形式运行
            #         gunicorn -w 4 -b 127.0.0.1:5000 -D --access-logfile ./logs/log main:app
            #
            #         # 停止
            #         kill ...
            #
            # 3 配置nginx
            #
            #     注意 nginx配置文件名为 nginx.conf的配置 注意备份
            #
            #
            #     1 配置文件
            #         /usr/local/nginx/conf/nginx.conf
            #
            #         # 配置负载均衡服务器
            #         upstream 名 {
            #
            #             server ip地址:端口号1;
            #             server ip地址:端口号2;
            #             ......
            #         }
            #
            #         server {
            #             ...
            #
            #             location / {
            #                 # 转发请求地址
            #                 proxy_pass http://名; # 负载均衡中的所起的名
            #
            #                 # 携带用户信息
            #                 proxy_set_header Host $host;
            #                 proxy_set_header x-Real-IP $remote_adder
            #
            #
            #         }
            #
            #     2 重启nginx
            #
            #         执行命令
            #             sudo /usr/local/nginx/sbin/nginx -s relaod
            #
            #
            #
        1