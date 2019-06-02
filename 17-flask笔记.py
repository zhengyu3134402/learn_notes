#
#
#
#
#
#
# ====================================================
# flaskflask
#
#
#
#     1 概念
#         1 所有 Flask 程序都必须创建一个程序实例
#         2 Web 服务器使用一种名为 Web 服务器网关接口
# （Web Server Gateway Interface，WSGI）的协议
#         3 通过WSGI把客户端的所有请求都转交给Flask类对象处理
#         4 Flask参数（__name__） 用来确定程序的根目录，方便处理先对目录资源
#         5 处理url到函数的映射关系为路由
#         6 使用程序实例@app.route把函数注册为路由
#         7 支持动态路由匹配<变量> 函数种要有形参接受rul中的变量
#         8 受用程序实例的run方法启动服务器run方法有可选参数 dubug=True
#
#
#
#     2 安装
#         pip3 install flask
#
#     3 完整的程序
#
#         from flask import Flask
#
#
#         app = Flask(__name__)
#
#
#         @app.route('/')
#         def index():
#             return 'hello flask'
#
#
#         if __name__ == '__main__':
#             app.run(debug=True)
#
#     4 程序上下文和请求上下文
#
#         1 概念
#
#             1 客户端返送的HTTP请求，flask把他封装成request对象
#                 通过request对象，可处理其他事情
#             2 flask使用上下文临时把request变为全局可访问（注意不同的请求request是不同的对象）
#             3 flask中的两种上下文
#                 变量名         上下文         说明
#                 current_app  程序上下文  当前激活程序的程序实例
#                  g           程序上下文  处理请求时用作临时存储的对象。每次请求都会重设这个变量
#                 request      请求上下文  请求对象，封装了客户端发出的 HTTP 请求中的内容
#                 session      请求上下文  用户会话，用于存储请求之间需要“记住”的值的词典
#
#             4 在激活或推送程序和请求上下文之前， 全局变量都不可使用
#     5 请求调度
#
#         1 概念
#
#             1 生成url和视图函数之间的映射
#
#                 1 使用app.route修饰器生成映射
#                 2 或者app.add_url_rule()生成映射
#             2 映射
#
#                 Map([<Rule '/' (OPTIONS, GET, HEAD) -> index>,
#                      <Rule '/static/<filename>' (OPTIONS, GET, HEAD) -> static>])
#
#                  HEAD 和 OPTIONS 方法由 Flask 自动处理
#
#     6 请求钩子
#
#         1 概念
#
#             钩子函数
#
#                 before_first_reques：注册一个函数，在处理第一个请求之前运行。
#                 before_request：注册一个函数，在每次请求之前运行。
#                 after_request：注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行。
#                 teardown_request：注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行。
#
#                 在请求钩子函数和视图函数之间共享数据一般使用上下文全局变量 g
#                 before_request 处理程序可以从数据库中加载已登录用户，并将其保存到 g.user 中。随后调用视
#                     图函数时，视图函数再使用 g.user 获取用户。
#
#
#     7 响应
#
#         1 响应类返回字符串make_response
#             1 创建make_response的类对象
#                 response = make_response('返回给客户端的展示字符串'，状态码)
#             2 可设置cookie
#                 response.set_cookie('key', 'value')
#             3 返回响应
#                 return response
#         2 响应类重定向 redirect
#             return redirect（'网址'）
#
#
#         3 返回类错误abort(404)
#             abort(404)
#
#     7.1 404错误处理
#
#         @app.errorhandler(404)
#             def page_not_found(args):
#                 return render_template('404.html')
#
#
#
#
#
#     8 Flask 扩展
#
#         1 Flask-Script
#
#             1 概念
#
#                 命令行解析器，向flask插入外部脚本
#
#             2 安装
#
#                 pip3 install flask-script
#
#
#             3 配置
#
#                 1 导入 Manager
#
#                     from flask_script import Manager
#
#                 2 创建 Manager类对象 将Flask的app实例作为参数传入到Manager类对象用
#                     app = Flask(__name__)
#                     manager = Manager(app)
#
#                 3 更改启动服务的对象
#
#                     if __name__ == '__main__':
#                         manager.run()
#
#
#             4 使用
#                 python 文件.py runserver  启动服务
#                 python 文件.py shell  启动shell  带有flask上下文
#
#                 python 文件.py runserver --help 查看其它功能
#
#     9 模板
#
#         1概念
#
#             为了渲染模板，Flask 使用了一个名为 Jinja2 的强大模板引擎
#
#         1 render_template
#
#             from flask import render_template
#
#             return render_template('模板文件名',键值对参数) # 键为模板中的占位符变量，值为模板中渲染的值
#
#         2 变量
#
#             1 魔板中表示
#
#                 {{ 变量名 }}
#
#             2 可识别复杂类型
#
#                 字典，列表 ，方法
#
#             3 过滤器
#
#                 1 书写形式
#
#                     {{ 变量名|过滤器名 }}
#
#                 2 过滤器
#
#                     safe 渲染值时不转义
#                     capitalize 把值的首字母转换成大写，其他字母转换成小写
#                     lower 把值转换成小写形式
#                     upper 把值转换成大写形式
#                     title 把值中每个单词的首字母都转换成大写
#                     trim 把值的首尾空格去掉
#                     striptags 渲染之前把值中所有的 HTML 标签都删掉
#         3 控制结构
#
#             1 条件
#
#                 {% if xxx %}
#                     ...
#                 {% else %}
#                     ..
#                 {% endif %}
#
#             2 循环
#
#                 {% for i in a %}
#                     {{ i }}
#                 {% endfor %}
#
#             3 宏（函数）
#
#                 定义宏
#                 {% marco 函数名（args） %}
#                 {% endmacro %}
#
#                 使用宏
#                 {% 函数名（参数） %}
#
#                 调用单独文件的宏
#
#                     {% import 'xx.html' as xxxx %}
#
#                 使用末班的代码片段
#
#                     {% include 'xx.html' %}
#             4 继承
#
#                 基模板
#                     base.html文件中
#                     {% block aa %}
#                     {% endblock aa %}
#
#                 继承基模板
#
#                     {% extends 'base.html' %}
#                         {% block aa %}
#                         ...
#                         {% endblock aa %}
#
#     10  flask中使用bootstrap
#
#         1 安装
#
#             pip3 install flask-bootstrap
#
#         2 使用
#
#             1 导入 Bootstrap
#
#             2 创建类实例将app实例传入类的参数中
#
#             3 创建base.html文件 继承 bootstrap/base.html
#
#             4 创建其他文件继承 常见的base.html文件使用其中定义好的块即可
#
#
#
#             5 使用定义好的块
#
#                 块　　名        说　　明
#                 doc 整个 HTML 文档
#                 html_attribs <html> 标签的属性
#                 html <html> 标签中的内容
#                 head <head> 标签中的内容
#                 title <title> 标签中的内容
#                 metas 一组 <meta> 标签
#                 styles 层叠样式表定义
#                 body_attribs <body> 标签的属性
#                 body <body> 标签中的内容
#                 navbar 用户定义的导航条
#                 content 用户定义的页面内容
#                 scripts 文档底部的 JavaScript 声明
#
#             6 如果重新定义块（加super（）函数）
#
#                 {% block scripts %}
#                 {{ super() }}    #  保留基模板中定义的块的原始内容
#                 <script type="text/javascript" src="my-script.js"></script>
#                 {% endblock %}
#
#     11 链接(模板和程序中都可使用)
#
#         1 获取函数的相对url 和绝对url
#
#             1 相对url
#
#                 url_for('函数名')
#
#             2 绝对url
#
#                 url_for('函数名', _external=True)
#
#             3 生成动态路由
#
#                 url_for('函数名', name="xx") # name="xx" 如果对应函数中包含有name参数 就会生成/xx
#
#             4 添加额外参数
#
#                 url_for('函数名', name="xx") # name="xx" 如果对应函数不包含有name参数 就会生成/?name=xx
#
#     12 静态文件
#
#          1 原理 url_map中 默认使用了
#
#             <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
#
#          2 引用
#
#             url_for('static', filename='xx/xxxx/xxxxx.xx')
#
#     13 Flask-Moment本地化日期和时间
#
#         把时间单位发送给 Web 浏览器，转换成当地时间，然后渲染
#
#     14 web表单（flask-wtf）
#
#         1 概念
#             1默认情况下，Flask-WTF 能保护所有表单免受跨站请求伪造
#             2这个类定义表单中的一组字段，每个字段都用对象表示。字段对象可附属一个或多个验证函数
#         2 安装
#
#             pip3 install flask-wtf
#
#         3 csrf保护
#
#             1 可程序中配置也可也可从文件或环境中导入配置值（一般写入配置文件中）
#
#                 1 程序中配置
#                     app.config['SECRET_KEY'] = '随机字符串' # flask-wtf使用这个秘钥生成加密令牌再用令牌验证请求中表单数据的真伪
#
#         4 表单类
#
#              1 创建表单类
#                 from wtforms import StringField, SubmitField
#
#                 class TestForm(FlaskForm):
#
#                     name = StringField('你的名字', validators=[DataRequired(message='不能为空')])
#                     submit = SubmitField(label='提交')
#
#              2 把表单渲染成HTML
#
#
#
#                 @app.route('/test_form/')
#                 def test_form():
#                     form = TestForm() # 创建表单类的对象
#                     return render_template('test_form.html', form=form) # 表单对象类传入到模板中
#
#                 html文件中
#                 <form action="{{ url_for('test_form') }}">
#
#                     {{ form.hidden_tag() }}
#                     {{ form.name.label }}{{ form.name(id='xx') }}  # 可以为字段指定 id 或 class 属性，然后定义 CSS 样式
#                     {{ form.submit() }}
#
#                 </form>
#              3 使用bootstrap是表单样式变得更美（bootstrap提供的表单）
#
#                 {% extends 'base.html' %}
#                 {% import 'bootstrap/wtf.html' as wtf %} # import 和python用法一样
#
#
#                 {% block page_content %}
#                     {{ wtf.quick_form(form) }}
#                 {% endblock %}
#
#              4 路由函数接受post请求
#                 app.route('/test_form/', methods=['GET', 'POST'])
#                 def test_form():
#                     ....
#
#              5 接受用户信息与用户互动
#
#                 @app.route('/test_form/', methods=['GET', 'POST'])
#                 def test_form():
#                     name = None
#                     form = TestForm()
#                     if form.validate_on_submit():  # 如果表单验证成功 数据的 POST 请求。 validate_on_submit() 会调用
#                                                         # name 字段上附属的 Required() 验证函数。如果名字不为空，就能通过验证，
#                                                         # validate_on_submit() 返回 True
#                         name = form.name.data      # 获取用户输入的name值
#                     return render_template('test_form.html', form=form, name=name)
#
#         5 重定向和用户会话
#
#             问题 1用户发送post后刷新页面的时候浏览器会提示是否重新提交post的弹框
#                 2重定向之后 用户发送的post数据会丢失
#
#             解决
#                 1 重定向 将post请求变成get请求
#                 2 将用户发送的数据存到session中
#                 class TestForm(FlaskForm):
#
#                     name = StringField('你的名字', validators=[DataRequired()])
#                     submit = SubmitField(label='提交')
#
#
#                 @app.route('/test_form/', methods=['GET', 'POST'])
#                 def test_form():
#
#                     form = TestForm()
#                     if form.validate_on_submit():  # 如果表单验证成功
#                         session['name'] = form.name.data      # 获取用户输入的name值
#                         return redirect(url_for('test_form'))
#                     return render_template('test_form.html', form=form, name=session.get('name', None))
#
#         6 Flash消息
#
#             1 概念
#
#                 显示提示的消息
#
#             2 用户更改提交的名字若和之前不一样，会出现提示消息
#                 class TestForm(FlaskForm):
#
#                     name = StringField('你的名字', validators=[DataRequired()])
#                     submit = SubmitField(label='提交')
#
#
#                 @app.route('/test_flash/', methods=['GET', 'POST'])
#                 def test_flash():
#
#                     form = TestForm()
#                     if form.validate_on_submit():
#                         if session['name'] and form.name.data != session['name']:
#                             flash('好像您改了名字哦！！！')
#                         session['name'] = form.name.data
#                         return redirect(url_for('test_flash'))
#                     return render_template('test_form.html', form=form, name=session.get('name', None))
#
#                 主模板中
#
#                     {% for message in get_flashed_messages() %}
#                         {{ message }}
#                     {% endfor %}
#
#
#         7 WTForms支持的HTML标准字段
#             字段类型        说明
#             StringField 文本字段
#             TextAreaField 多行文本字段
#             PasswordField 密码文本字段
#             HiddenField 隐藏文本字段
#             DateField 文本字段，值为 datetime.date 格式
#             DateTimeField 文本字段，值为 datetime.datetime 格式
#             IntegerField 文本字段，值为整数
#             DecimalField 文本字段，值为 decimal.Decimal
#             FloatField 文本字段，值为浮点数
#             BooleanField 复选框，值为 True 和 False
#             RadioField 一组单选框
#             SelectField 下拉列表
#             SelectMultipleField 下拉列表，可选择多个值
#             FileField 文件上传字段
#             SubmitField 表单提交按钮
#             FormField 把表单作为字段嵌入另一个表单
#             FieldList 一组指定类型的字段
#
#
#         8 WTForms验证函数
#             Email 验证电子邮件地址
#             EqualTo 比较两个字段的值；常用于要求输入两次密码进行确认的情况
#             IPAddress 验证 IPv4 网络地址
#             Length 验证输入字符串的长度
#             NumberRange 验证输入的值在数字范围内
#             Optional 无输入值时跳过其他验证函数
#             Required 确保字段中有数据
#             Regexp 使用正则表达式验证输入值
#             URL 验证 URL
#             AnyOf 确保输入值在可选值列表中
#             NoneOf 确保输入值不在可选值列表中
#
#
#     15 数据库使用Flask-SQLAlchemy
#
#         1 安装
#
#             pip3 install flask-sqlalchemy
#
#         2 配置数据库
#
#             from flask_sqlalchemy import SQLAlchemy
#             base_dir = os.path.abspath(os.path.dirname(__file__))
#             app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
#             app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True # 每次请求结束后都会自动提交数据库中的变动
#             db = SQLAlchemy(app)
#
#         3 定义模型
#
#             class Role(db.Model):   # 注意继承sqlalchemy对象.Model
#                 __tablename__ = 'role'  # 定义数据库中的表明
#                 id = db.Column(db.Column(db.Integer, primary_key=True)) # 主键
#                 rolename = db.Column(db.String(64), unique=True)  # unique 唯一
#                 user = db.relationship('User', backref='role') # 代表这个关系的面向对象视角，
#                                                                # 对于一个 Role 类的实例，其 users 属性将返回与角色相关联的用户
#                                                                # 组成的列表db.relationship() 的第一个参数表明这个关系的另一端是哪个模型
#                                                                #  backref 参数向 User 模型中添加一个 role 属性，从而定义反向关系。
#                                                                # 这一属性可替代 role_id 访问 Role 模型，此时获取的是模型对象而不是外键的值
#
#                 def __repr__(self):
#                     return self.rolename
#
#
#             class User(db.Model):
#                 __tablename__ = 'user'
#                 id = db.Column(db.Integer, primary_key=True)
#                 username = db.Column(db.String(64), unique=True, index=True) # index为创建索引，提升查询效率
#                 role_id = db.Column(db.Integer, db.ForeignKey('role.id')) # 添加外键为role表中的行id值
#
#                 def __repr__(self):
#                     return self.username
#
#             最常用的SQLAlchemy列类型
#                 类型名     Python类型        说明
#                 Integer         int         普通整数，   一般是 32 位
#                 SmallInteger    int        取值范围小的整数，一般是 16 位
#                 BigInteger  int 或 long 不限制精度的整数
#                 Float       float   浮点数
#                 Numeric decimal.Decimal 定点数
#                 String      str         变长字符串
#                 Text        str         变长字符串，对较长或不限长度的字符串做了优化
#                 Unicode     unicode     变长 Unicode 字符串
#                 UnicodeText unicode     变长 Unicode 字符串，对较长或不限长度的字符串做了优化
#                 Boolean     bool 布尔值
#                 Date        datetime.date 日期
#                 Time        datetime.time 时间
#                 DateTime    datetime.datetime 日期和时间
#                 Interval    datetime.timedelta 时间间隔
#                 Enum        str 一组字符串
#                 PickleType 任何 Python 对象 自动使用 Pickle 序列化
#                 LargeBinary     str 二进制文件
#
#             最常使用的SQLAlchemy列选项
#                 primary_key 如果设为 True ，这列就是表的主键
#                 unique 如果设为 True ，这列不允许出现重复的值
#                 index 如果设为 True ，为这列创建索引，提升查询效率
#
#                  如果设为 True ，这列允许使用空值；如果设为 False ，这列不允许使用空值
#                 default 为这列定义默认值
#
#             常用的SQLAlchemy关系选项
#
#                 选项名 说　　明
#                 backref 在关系的另一个模型中添加反向引用
#                 primaryjoin 明确指定两个模型之间使用的联结条件。只在模棱两可的关系中需要指定
#                 lazy 指定如何加载相关记录。可选值有 select （首次访问时按需加载）、 immediate （源对象加
#                         载后就加载）、 joined （加载记录，但使用联结）、 subquery （立即加载，但使用子查询），
#                         noload （永不加载）和 dynamic （不加载记录，但提供加载记录的查询）
#                 uselist 如果设为 Fales ，不使用列表，而使用标量值
#                 order_by 指定关系中记录的排序方式
#                 secondary 指定多对多关系中关系表的名字
#                 secondaryjoin SQLAlchemy 无法自行决定时，指定多对多关系中的二级联结条件
#
#         4 数据库操作
#
#             1 增
#
#                 1 创建表
#
#                     db.create_all()  # 如果修改模型，执行此操作 数据库不会更新模型
#
#                 2 插入单行数据
#
#                     s= Role(name="xx")
#                     db.session.add(s)
#                     db.session.commit()
#
#                 3 插入多行数据
#                     s1 = Role(name="xx")
#                     s2 = Role(name="xx")
#                     db.session.add_all([s1, s2])
#                     db.session.commit()
#
#             2 删
#
#                 1 删除表
#
#                     db.drop_all()
#
#                 2 删除行数据
#
#                     db.session.delete(s)
#                     db.session.commit
#
#             3 改
#                 1 修改数据
#                     s.name = 'yyy'
#                     db.session.add(s)
#                     db.session.commit()
#
#
#             4 查
#                 1 获取对象所有数据
#
#                     对象.qurey.all()
#
#                 2 查询原生SQL查询语句
#
#                     str(执行语句)
#
#                 3
#
#                 常用的SQLAlchemy查询过滤器
#
#                     过滤器         说明
#                     filter()        把过滤器添加到原查询上，返回一个新查询 # 参数中用（对象.属性=xx）
#                     filter_by()     把等值过滤器添加到原查询上，返回一个新查询 # 参数中用（属性=xx）
#                     limit()         使用指定的值限制原查询返回的结果数量，返回一个新查询
#                     offset()        偏移原查询返回的结果，返回一个新查询
#                     order_by()      根据指定条件对原查询结果进行排序，返回一个新查询
#                     group_by()      根据指定条件对原查询结果进行分组，返回一个新查询
#
#                 最常使用的SQLAlchemy查询执行函数
#
#                     all()       以列表形式返回查询的所有结果
#                     first()     返回查询的第一个结果，如果没有结果，则返回 None
#                     first_or_404() 返回查询的第一个结果，如果没有结果，则终止请求，返回 404 错误响应
#                     get()       返回指定主键对应的行，如果没有对应的行，则返回 None
#                     get_or_404() 返回指定主键对应的行，如果没找到指定的主键，则终止请求，返回 404 错误响应
#                     count()     返回查询结果的数量
#                     paginate()  返回一个 Paginate 对象，它包含指定范围内的结果
#
#             5 与视图模板数据库互动，新用户和老用户欢迎消息不同
#
#                 @app.route('/do_with_database/', methods=['GET', 'POST'])
#                 def do_with_database():
#
#                     form = TestForm()
#                     if form.validate_on_submit():
#
#                         if User.query.filter_by(username=form.name.data).first(): #
#                             session['name'] = form.name.data
#                             flash(message='老朋友%r,又见面了'%(form.name.data))
#                             return redirect(url_for('do_with_database'))
#
#                         db.session.add(User(username=form.name.data))
#
#                         session['name'] = form.name.data
#                         flash(message='欢迎您%r第一次到来'%(session.get('name')))
#
#                         return redirect(url_for('do_with_database'))
#
#                     return render_template('do_with_database.html', form=form)
#
#             6 集成python shell
#
#                 1 概念
#
#                     使用python shell 向数据库添加数据 不用再导入类模型等（省去了import 操作），直接使用命令
#                     向数据库添加数据
#
#                 2 配置
#                     1 为shell命令添加一个上下文
#
#                     from flask_script import Shell
#
#                     def make_shell_context():
#                         return dict(app=app, db=db, User=User, Role=Role)
#                     manager.add_command('shell', Shell(make_context=make_shell_context))
#
#             7 数据库迁移Flask-Migrate
#
#                 基本使用命令
#
#                     python xx.py db init    # 创建迁移仓库
#                     python xx.py db migrate -m "initial migration"  # 若模型有改动执行此命令
#                     python xx.py db upgrade # 执行迁移 将新的模型更新到数据库
#
#                 1 概念
#                     使用flask-Migrate执行数据库创建
#                     如果修改了数据模型， 不得不删除数据库再重新创建数据库达到模型跟新的目的，但是数据就会丢失
#                     为了解决数据丢失，Flask_Migrate数据迁移功能
#
#                 2 安装
#
#                     pip3 install flask-migrate
#
#                 3 使用
#
#                     1 创建迁移仓库
#
#                         1 配置Flask-Migrate
#
#                             from flask_migrate import Migrate, MigrateCommand
#                             migrate = Migrate(app, db)
#                             manager.add_command('db', MigrateCommand)
#
#                         2 创建迁移仓库
#
#                             python xx.py db init # 会生成migrations目录
#
#
#                     2 创建迁移脚本
#
#                         python xx.py db migrate -m "initial migration"
#
#                     3 跟新数据库
#
#                         python xx.py db upgrade
#
#         5 电子邮件
#
#             1 概念
#
#                 在flask程序中发送电子邮件
#
#             2 安装
#
#                 pip3 install flask-mail
#
#             3 配置
#                 1 概念
#                     Flask-Mail SMTP服务器的配置
#
#                     配　　置        默认值     说明
#                     MAIL_SERVER  localhost 电子邮件服务器的主机名或 IP 地址
#                     MAIL_PORT 25 电子邮件服务器的端口
#                     MAIL_USE_TLS False 启用传输层安全（Transport Layer Security，TLS）协议
#                     MAIL_USE_SSL False 启用安全套接层（Secure Sockets Layer，SSL）协议
#                     MAIL_USERNAME None 邮件账户的用户名
#                     MAIL_PASSWORD None 邮件账户的密码
#
#                 2 配置
#
#                     1 初始化 Flask-Mail
#
#                         from flask_mail import Mail
#                         mail = Mail(app)
#
#                     1 将账户密码设置在环境变量中（为了安全 不这样做也行直接写入配置文件中）
#
#                         linux
#                             (venv) $ export MAIL_USERNAME=<Gmail username>
#                             (venv) $ export MAIL_PASSWORD=<Gmail password>
#
#                         windows
#
#                             (venv) $ set MAIL_USERNAME=<Gmail username>
#                             (venv) $ set MAIL_PASSWORD=<Gmail password>
#
#                     2 主文件中配置
#                         app.config['MAIL_SERVER'] = 'smtp.qq.com'
#                         app.config['MAIL_PORT'] = 25
#                         app.config['MAIL_USE_SSL'] = False
#                         app.config['MAIL_USE_TLS'] = False
#                         app.config['MAIL_USERNAME'] = "174927390@qq.com"
#                         app.config['MAIL_PASSWORD'] = "baleguedteflbhci"
#                     3 测试发送电子邮件
#                         def send_mail():
#                             msg = Message(subject='11111111', sender='174927390@qq.com', recipients=['174927390@qq.com'])
#                             msg.body = 'body'
#                             msg.html = '<b>html</b>'
#                             mail.send(msg)
#
#
#                         @app.route('/test_mail/')
#                         def test_mail():
#
#                             send_mail()
#                             return '1111'
#
#         6 大型程序结构
#
#             app/   # 放路由文件，static template
#                 main/
#                     __init__.py
#                         from flask import Blueprint # 在蓝本中定义的路由处于休眠状态，需要注册到程序工厂函数中
#                         main = Blueprint('main', __name__) # 参数1：蓝本的名字，参数2：蓝本所在模块
#                         from . import views
#                     views.py
#                         使用蓝本定义路由
#                             from flask import render_template
#                             from . import main
#
#                             @main.route('/')    # 路由修饰器有蓝本提供 # url_for('main.index')
#                             def index():
#                                 return render_template('index.html')
#
#                 static/
#                 templates/
#                 __init__.py
#                     from config import config
#                     from flask import Flask
#
#                     def create_app():   # 工厂函数 在创建实例之前对环境进行配置
#                         app = Flask(__name__)
#                         app.config.from_object(config['default']) # 通过from_object方法直接导入配置
#                         config['default'].init_app(app)  # 初始化配置
#
#                         from .main import main as main_blueprint  # 注意在此处导入蓝图
#                         app.register_blueprint(main_blueprint)  # 注册蓝本
#                         return app
#                 models.py
#             config.py # 配置文件
#                 class Config:
#                     DEBUG = True
#
#                     @staticmethod
#                     def init_app(app):
#                         pass
#
#                 config = {
#                     "default": Config
#                 }
#             manage.py # 启动文件
#                 from app import create_app
#                 app = create_app()
#                 if __name__ == '__main__':
#                     app.run()
#
#             1 蓝图中配置静态文件
#
#                 main.static_folder = 'static'   # 配置静态文件
#                 main.static_url_path = '/static' # 配置url静态文件位置
#
#                 html中使用
#                 <img src="{{ url_for('main.static', filename='test.jpg') }}" alt="">
#
#             2 蓝图下的反向解析
#
#                 print(url_for('main.index'))  # 蓝图下的url反向解析
#
#             3 环境依赖包的保存文件和到了新项目的安装
#
#                 1 保存
#                     1 创建文件 requirements.txt
#                     2 执行命令将环境依赖包存入 requirements
#                         pip3 freeze > requirements.txt
#                 2 安装
#                     pip3 install -r requirements.txt
#
#         7 用户认证
#
#             1 为用户密码加密 使用Werkzeug显示密码散列
#
#                 from werkzeug.security import generate_password_hash, check_password_hash
#
#                 class Test(db.Model):
#
#                     __tablename__ = 'test'
#
#                     id = Column(Integer, primary_key=True)
#                     name = Column(String(32))
#
#                     password_hash = db.Column(db.String(128))
#
#                     @property
#                     def password(self):
#                         raise AttributeError('密码不可读取')
#
#                     @password.setter                # 通过 obj.password="xx" 对密码进行加工，生产加工后密码
#                     def password(self, password):
#                         self.password_hash = generate_password_hash(password)
#
#                     def check_password(self, password):  # 通过 obj.check_password("xx") 对密码进行加工后， 核对上面生成的加工密码
#                         return check_password_hash(self.password_hash, password)
#
#             2 创建一个目录 用来验证用户，注册成蓝本
#                     .....照旧
#                     app.register_blueprint(auth_blueprint, url_prefix="/auth")  # url_prefix参数为url添加前缀
#
#
#             3 安装用户认证组件flask_login
#
#                 pip3 install flask-login
#
#             4 使用flask_login
#
#                 1 创建用户登录的用户模型 添加加载用户的回调函数
#
#                     必须实现4个用户方法 或 模型直接继承 UserMixin
#                         is_authenticated() 如果用户已经登录，必须返回 True ，否则返回 False
#                         is_active() 如果允许用户登录，必须返回 True ，否则返回 False 。如果要禁用账户，可以返回 False
#                         is_anonymous() 对普通用户必须返回 False
#                         get_id() 必须返回用户的唯一标识符，使用 Unicode 编码字符串
#
#                     class Users(UserMixin, db.Model):
#
#                         __tablename__ = 'users'
#
#                         id = Column(Integer, primary_key=True)
#                         name = Column(String(32))
#                         password_hash = Column(db.String(128))
#                         email = Column(String(64), unique=True, index=True)
#                         role_id = Column(Integer, ForeignKey('roles.id'))
#
#
#                         @login_manager.user_loader  # 添加加载用户的回调函数
#                         def load_user(user_id):
#                             return Users.query.get(int(user_id)) # 如果能找到用户，这个函数必须返回用户对象，否则返回None
#
#                         @property
#                         def password(self):
#                             raise AttributeError('密码不可读取')
#
#                         @password.setter                # 通过 obj.password="xx" 对密码进行加工，生产加工后密码
#                         def password(self, password):
#                             self.password_hash = generate_password_hash(password)
#
#                         def check_password(self, password):  # 通过 obj.check_password("xx") 对密码进行加工后， 核对上面生成的加工密码
#                             return check_password_hash(self.password_hash, password)
#
#                     class Roles(db.Model):
#                         __tablename_ = "roles"
#                         id = Column(Integer, primary_key=True)
#                         role_name = Column(String(64), unique=True, index=True)
#                         users = db.relationship('Users', backref='roles')
#
#                 2 工厂函数中初始化flask-login
#
#                     from flask_login import LoginManager
#
#                     ...
#                     login_manager = LoginManager()
#                     login_manager.session_protection = "strong" # 值可设置为None，'basic','strong'为不同的安全防护等级设为
#                                                                   #'strong' 时，Flask-Login 会记录客户端 IP地址和浏览器的
#                                                                   # 用户代理信息，如果发现异动就登出用户
#                     login_manager.login_view = 'auth.login'     # 登录页面的路由端点
#
#                     def create_app():
#                         ...
#                         login_manager.init_app(app)
#                         ...
#
#                 3 是只有认证的用户才能访问路由（login_required修饰器）
#
#                     from flask_login import login_required
#
#                     @xx.route('/test_user_auth')
#                     @login_required
#                     def secret():
#                         return '您不是认证用户'
#
#                 4 展示用户的登录状态
#
#                     <ul class="nav navbar-nav navbar-right">
#                         {% if current_user.is_authenticated %}  # 如果当前用户是验证用户变量 current_user 由 Flask-Login 定义，
#                                                                     # 且在视图函数和模板中自动可用。这个变量的值是当前登录的用户，
#                                                                     # 如果用户尚未登录，则是一个匿名用户代理对象。如果是匿名用户，
#                                                                     # is_authenticated() 方法返回 False
#                         <li><a href="{{ url_for('auth.logout') }}">Sign Out</a></li>
#                         {% else %}
#                         <li><a href="{{ url_for('auth.login') }}">Sign In</a></li>
#                         {% endif %}
#                     </ul>
#
#                 5 接受用户的post 验证用户是否存在，验证密码是否正确，根据用户是否记住登录账户和密码绝对设置不设置cookie，登录成功后返回原来地址
#
#                     @auth.route('/login/', methods=['GET', 'POST'])
#                     def login():
#                         user_login = UserLogin()
#                         if user_login.validate_on_submit():
#                             user = Users.query.filter_by(email=user_login.email.data).first() # 去数据库中查询是否有此用户
#                             if user and user.check_password(user_login.password.data):        # 如果用户存在 在测试密码是否正确
#                                 login_user(user, user_login.remember_me.data)       # 如果用户点击记住账户密码，会在用户浏览器
#                                                                                         # 中写入一个长期有效的 cookie，使用这个 cookie 可以复现用户会话
#                                 return redirect(request.args.get('next') or url_for('main.index')) # Flask-Login会把原地址保存在查询字符串的 next 参数中
#                             flash('账户密码错误或未注册')         # 如果出现错误会 出现错误提示
#                         return render_template('login.html', user_login=user_login)
#
#
#
#                 6 退出登录
#
#                     @auth.route('/logout/')
#                     @login_required
#                     def logout():
#                         logout_user() # 删除并重设用户会话
#                         flash('您已经退出登录状态')
#                         return redirect(url_for('main.index'))
#
#                 7 用户注册
#
#                     1 创建用户注册表单
#                         class UserRegisterForm(FlaskForm):
#                             """用户注册表单
#                                 Regexp() 为正则验证方法
#                                 EqualTo() 为比较字段的方法
#                                 def_字段(self,field) 字段的自定义验证函数
#                             """
#                             email = StringField(label="邮箱", validators=[DataRequired(), Length(1,64), Email()])
#                             username = StringField(label="用户名", validators=[DataRequired(), Length(1, 64), Regexp('^[a-zA-Z_.]*$',flags=0, message='取名字不符合规范')])
#                             password = PasswordField(label="密码", validators=[DataRequired(), EqualTo('password2', message='密码两次输入不匹配')])
#                             password2 = PasswordField(label="确认密码", validators=[DataRequired()])
#                             submit = SubmitField(label="提交")
#
#                             def validate_email(self, field):
#                                 if Users.query.filter_by(email=field.data).first():
#                                     raise ValidationError('该邮箱已存在，存在请使用其他邮箱')
#
#                             def validate_username(self, field):
#                                 if Users.query.filter_by(username=field.data).first():
#                                     raise Validation
#
#                 8 测试登录
#
#                     {% block page_content %}
#
#                         {% if current_user.is_authenticated %}   # 如果当前用户是已验证用户
#                             <h1>hello, {{ current_user.username }}</h1>  # 获取当前登录用户名， 如果未登录返回none
#                         {% else %}
#                             <h1>hello, 陌生人</h1>
#                         {% endif %}
#
#                     {% endblock %}
#
#                 9 确认账户，向账户注册的邮箱中发送信息（对用户id进行加密发送），用户点击信息，确认成功
#
#                     1 加密工具(TimedJSONWebSignatureSerializer等)
#
#                         1 使用
#                             1 导入模块
#                             2 创建类对象： 类（字符串, expires_in=秒数）
#                             3 加密 对象.dumps(..)
#                             4 解密 对象.loads(..)
#                                 from itsdangerous import  TimedJSONWebSignatureSerializer as Serializer
#                                 s = Serializer('xx', expires_in=3600)
#                                 a = s.dumps('aa')   # 加密
#                                 s.loads(a)          # 解密
#
#                     2 向模型中添加 加密工具（TimedJSONWebSignatureSerializer）
#
#                         强烈注意 s.dumps(xx)方法 会生成二进制字符串， 发送到浏览器，从浏览器返回字后会变成 字符串类型
#                         所以返送前后不一样 解决方法  把s.dumps(xx)转换成二进制用 .decode() 解码成字符串，那么发送到浏览器
#                         再返回来的就都是字符串，就一样了！！！！
#
#
#                         class Users(UserMixin, db.Model):
#
#                             __tablename__ = 'users'
#
#                             ...
#                             activate = Column(Boolean, default=False)
#                             ...
#
#                             def make_activate_info(self, expiration=3600):
#                                 """生成令牌"""
#                                 s = Serializer(current_app.config['SECRET_KEY'], expiration)
#                                 return s.dumps({'activate': self.id}).decode() !!!!!!!!注意加上！！！decode()
#
#                             def to_activate(self, code_from_user): # 还检查令牌中的 id 是否和存储在 current_user 中的已登录用户匹配
#                                 """检验令牌"""
#                                 s = Serializer(current_app.config['SECRET_KEY'])
#                                 try:
#                                     data = s.loads(code_from_user)
#                                 except:
#                                     return False
#
#                                 if data.get('activate') != self.id:
#                                     return False
#                                 self.activate = True
#                                 db.session(self)
#                                 return True
#
#                     3 实现用户注册成功将数据添加到数据库之后，向用户注册的邮箱内发送激活认证邮件
#                         @auth.route('/register/', methods=['GET', 'POST'])
#                         def register():
#                             form = UserRegisterForm()
#                             if form.validate_on_submit():
#                                 user = Users(email=form.email.data, username=form.username.data, password=form.password.data)
#                                 db.session.add(user)
#                                 db.session.commit()
#                                 code = user.make_activate_info()
#                                 send_mail(code, user.username)
#                                 flash('注册完毕！请先登录,已经发送邮件到您的邮箱，请点击激活')
#
#                                 return redirect(url_for('auth.login'))
#                             return render_template('register.html', form=form)
#
#
#                         @auth.route('/active/<token>')
#                         @login_required
#                         def active(token):
#                             print(token, 222222222222222222222222222)
#                             if current_user.active:
#                                 return redirect(url_for('main.index'))
#                             if current_user.to_active(token):
#                                 flash('您已经激活了你的账户')
#                             else:
#                                 flash('邮箱激活连接已经过期，请重新激活')
#                             return redirect(url_for('main.index'))
#
#                     4 蓝本中使用全局请求钩子（before_app_request）拦截用户
#                         实现了对登录后为激活邮箱的用户进行重定向到在此发送邮件路由
#                         对用户拦截的条件
#                             1 是登录用户 且
#                             2 当前用户没有认证 且
#                             3 请求的不是 auth.蓝本的视图函数
#                             4 请求路径不是"static"
#
#                             @auth.before_app_request
#                             def before_request():
#                                 if current_user.is_authenticated() and \
#                                     not current_user.to_active() and \
#                                     request.endpoint[:5] != 'auth.' and \
#                                     request.endpoint != 'static':
#                                     return redirect(url_for('auth.un_active'))
#
#                             @auth.route('/un_active/')
#                             def un_active():
#
#                                 if current_user.is_anonymous or current_user.active:
#
#                                     return redirect(url_for('main.index'))
#                                 return render_template('un_active.html')
#
#                     5 重新发送确认邮件
#                         @auth.route('/active/')
#                         def resend_mail():
#                             code = current_user.make_activate_info()
#                             send_mail(code, current_user.username)
#                             flash('一份新的邮件已经发送到您的邮箱')
#                             return redirect(url_for('main.index'))
#
#                 10 管理账户
#
#                     1 修改密码  (@@@@@@@@@@对添加的代码就行修改)
#                         要求
#                             1 用户处于登录状态
#                             2 要求用户输入旧密码和替换的新密码
#                             @auth.route('/change_password/', methods=['GET', 'POST'])
#                             def change_password():
#                                 form = ChangePasswordForm()
#                                 original_pass = form.original_password.data
#                                 new_pass = form.new_password.data
#                                 if form.validate_on_submit():
#                                     if current_user.check_password(original_pass):
#                                         current_user.password = new_pass
#                                         flash('密码更新完毕，请重新登录')
#                                         logout_user()
#                                         return redirect(url_for('auth.login'))
#                                     flash('您输入的原始密码不正确！！！')
#                                     return render_template('change_password.html', form=form)
#                                 return render_template('change_password.html', form=form)
#
#                     2 忘记密码重设密码（客户忘记密码时候使用）
#                         要求
#                             1 使用提供电子邮件地址
#                             2 向邮件地址发送code，用户点击code进行验证，出现输入新密码表单
#
#                             @staticmethod
#                             def restart_pwd(code, new_password):
#
#                                 s = Serializer(current_app.config['SECRET_KEY'])
#                                 data = s.loads(code.encode('utf-8'))
#
#                                 user_id = data.get('active', None)
#                                 if not user_id:
#                                     return False
#
#                                 user = Users.query.filter_by(id=user_id).first()
#
#                                 user.password = new_password
#                                 db.session.add(user)
#                                 db.session.commit()
#                                 return True
#
#                             @auth.route('/forget_password/', methods=['GET', 'POST'])
#                             def forget_password():
#                                 form = ForgetPasswordForm()
#                                 if form.validate_on_submit():
#                                     user = Users.query.filter_by(email=form.email.data).first()
#                                     code = user.make_activate_info()
#                                     print(repr(code), 22222222222222)
#                                     send_restart_password_mail(code)
#                                     flash('一份邮件发送到您的邮箱，请进行确认')
#
#                                 return render_template('forget_password.html', form=form)
#
#
#                             @auth.route('/restart_password/<code>', methods=['GET', 'POST'])
#                             def restart_password(code):
#
#                                 form = RestartPasswordForm()
#                                 if form.validate_on_submit():
#                                     print(repr(code), 11111111111111111)
#                                     Users.restart_pwd(code=code, new_password=form.password.data)
#                                     flash('您已经找回密码请登录')
#                                     return redirect(url_for('auth.login'))
#
#
#                                 return render_template('restart_password_form.html', form=form)
#
#
#
#                     3 修改电子邮件地址
#                         要求
#
#                             1 验证新地址，发送确认邮件到新地址
#                             2 储存用户的新地址到数据库，邮箱验证之后，和数据库邮箱对比（能对比？）更新邮箱
#
#
#                         # 暂停！！！！！！！！！！！！！！！！！！！！！！！！！！学完django后再学
#
#
#
#
# 11111111111111111111111111111111111111
# ====================================================