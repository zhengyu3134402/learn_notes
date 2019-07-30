# #
# #
# #
# #
# #
# # -i https://pypi.douban.com/simple

1
# # ====================================================
# # flaskflask
# 1
# #
# #
# #
# #     1 概念
# #         1 所有 Flask 程序都必须创建一个程序实例
# #         2 Web 服务器使用一种名为 Web 服务器网关接口
# #           （Web Server Gateway Interface，WSGI）的协议
# #         3 通过WSGI把客户端的所有请求都转交给Flask类对象处理
# #         4 Flask参数（__name__） 用来确定程序的根目录，方便处理先对目录资源
# #         5 处理url到函数的映射关系为路由
# #         6 使用程序实例@app.route把函数注册为路由
# #         7 支持动态路由匹配<变量> 函数种要有形参接受rul中的变量
# #         8 受用程序实例的run方法启动服务器run方法有可选参数 dubug=True
# #
# #     2 安装
# #         pip3 install flask
# #
# #     3 完整的程序
# #
# #         from flask import Flask
# #
# #
# #         app = Flask(__name__)
# #
# #
# #         @app.route('/')
# #         def index():
# #             return 'hello flask'
# #
# #
# #         if __name__ == '__main__':
# #             app.run(debug=True)
# #
# #     4 程序上下文和请求上下文
# #
# #         1 概念
# #
# #             1 客户端返送的HTTP请求，flask把他封装成request对象
# #                 通过request对象，可处理其他事情
# #             2 flask使用上下文临时把request变为全局可访问（注意不同的请求request是不同的对象）
# #             3 flask中的两种上下文
# #                 变量名         上下文         说明
# #                 current_app  程序上下文  当前激活程序的程序实例
# #                  g           程序上下文  处理请求时用作临时存储的对象。每次请求都会重设这个变量
# #                 request      请求上下文  请求对象，封装了客户端发出的 HTTP 请求中的内容
# #                 session      请求上下文  用户会话，用于存储请求之间需要“记住”的值的词典
# #
# #             4 在激活或推送程序和请求上下文之前， 全局变量都不可使用
# #     5 请求调度
# #
# #         1 概念
# #
# #             1 生成url和视图函数之间的映射
# #
# #                 1 使用app.route修饰器生成映射
# #                 2 或者app.add_url_rule()生成映射
# #             2 映射
# #
# #                 Map([<Rule '/' (OPTIONS, GET, HEAD) -> index>,
# #                      <Rule '/static/<filename>' (OPTIONS, GET, HEAD) -> static>])
# #
# #                  HEAD 和 OPTIONS 方法由 Flask 自动处理
# #
# #     6 请求钩子
# #
# #         1 概念
# #
# #             钩子函数
# #
# #                 before_first_reques：注册一个函数，在处理第一个请求之前运行。
# #                 before_request：注册一个函数，在每次请求之前运行。
# #                 after_request：注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行。
# #                 teardown_request：注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行。
# #
# #                 在请求钩子函数和视图函数之间共享数据一般使用上下文全局变量 g
# #                 before_request 处理程序可以从数据库中加载已登录用户，并将其保存到 g.user 中。随后调用视
# #                     图函数时，视图函数再使用 g.user 获取用户。
# #
# #
# #     7 响应
# #
# #         1 响应类返回字符串make_response
# #             1 创建make_response的类对象
# #                 response = make_response('返回给客户端的展示字符串'，状态码)
# #             2 可设置cookie
# #                 response.set_cookie('key', 'value')
# #             3 返回响应
# #                 return response
# #         2 响应类重定向 redirect
# #             return redirect（'网址'）
# #
# #
# #         3 返回类错误abort(404)
# #             abort(404)
# #
# #     7.1 404错误处理
# #
# #         @app.errorhandler(404)
# #             def page_not_found(args):
# #                 return render_template('404.html')
# #
# #
# #
# #
# #
# #     8 Flask 扩展
# #
# #         1 Flask-Script
# #
# #             1 概念
# #
# #                 命令行解析器，向flask插入外部脚本
# #
# #             2 安装
# #
# #                 pip3 install flask-script
# #
# #
# #             3 配置
# #
# #                 1 导入 Manager
# #
# #                     from flask_script import Manager
# #
# #                 2 创建 Manager类对象 将Flask的app实例作为参数传入到Manager类对象用
# #                     app = Flask(__name__)
# #                     manager = Manager(app)
# #
# #                 3 更改启动服务的对象
# #
# #                     if __name__ == '__main__':
# #                         manager.run()
# #
# #
# #             4 使用
# #                 python 文件.py runserver  启动服务
# #                 python 文件.py shell  启动shell  带有flask上下文
# #
# #                 python 文件.py runserver --help 查看其它功能
# #
# #     9 模板
# #
# #         1概念
# #
# #             为了渲染模板，Flask 使用了一个名为 Jinja2 的强大模板引擎
# #
# #         1 render_template
# #
# #             from flask import render_template
# #
# #             return render_template('模板文件名',键值对参数) # 键为模板中的占位符变量，值为模板中渲染的值
# #
# #         2 变量
# #
# #             1 魔板中表示
# #
# #                 {{ 变量名 }}
# #
# #             2 可识别复杂类型
# #
# #                 字典，列表 ，方法
# #
# #             3 过滤器
# #
# #                 1 书写形式
# #
# #                     {{ 变量名|过滤器名 }}
# #
# #                 2 过滤器
# #
# #                     safe 渲染值时不转义
# #                     capitalize 把值的首字母转换成大写，其他字母转换成小写
# #                     lower 把值转换成小写形式
# #                     upper 把值转换成大写形式
# #                     title 把值中每个单词的首字母都转换成大写
# #                     trim 把值的首尾空格去掉
# #                     striptags 渲染之前把值中所有的 HTML 标签都删掉
# #         3 控制结构
# #
# #             1 条件
# #
# #                 {% if xxx %}
# #                     ...
# #                 {% else %}
# #                     ..
# #                 {% endif %}
# #
# #             2 循环
# #
# #                 {% for i in a %}
# #                     {{ i }}
# #                 {% endfor %}
# #
# #             3 宏（函数）
# #
# #                 定义宏
# #                 {% marco 函数名（args） %}
# #                 {% endmacro %}
# #
# #                 使用宏
# #                 {% 函数名（参数） %}
# #
# #                 调用单独文件的宏
# #
# #                     {% import 'xx.html' as xxxx %}
# #
# #                 使用末班的代码片段
# #
# #                     {% include 'xx.html' %}
# #             4 继承
# #
# #                 基模板
# #                     base.html文件中
# #                     {% block aa %}
# #                     {% endblock aa %}
# #
# #                 继承基模板
# #
# #                     {% extends 'base.html' %}
# #                         {% block aa %}
# #                         ...
# #                         {% endblock aa %}
# #
# #     10  flask中使用bootstrap
# #
# #         1 安装
# #
# #             pip3 install flask-bootstrap
# #
# #         2 使用
# #
# #             1 导入 Bootstrap
# #
# #             2 创建类实例将app实例传入类的参数中
# #
# #             3 创建base.html文件 继承 bootstrap/base.html
# #
# #             4 创建其他文件继承 常见的base.html文件使用其中定义好的块即可
# #
# #
# #
# #             5 使用定义好的块
# #
# #                 块　　名        说　　明
# #                 doc 整个 HTML 文档
# #                 html_attribs <html> 标签的属性
# #                 html <html> 标签中的内容
# #                 head <head> 标签中的内容
# #                 title <title> 标签中的内容
# #                 metas 一组 <meta> 标签
# #                 styles 层叠样式表定义
# #                 body_attribs <body> 标签的属性
# #                 body <body> 标签中的内容
# #                 navbar 用户定义的导航条
# #                 content 用户定义的页面内容
# #                 scripts 文档底部的 JavaScript 声明
# #
# #             6 如果重新定义块（加super（）函数）
# #
# #                 {% block scripts %}
# #                 {{ super() }}    #  保留基模板中定义的块的原始内容
# #                 <script type="text/javascript" src="my-script.js"></script>
# #                 {% endblock %}
# #
# #     11 链接(模板和程序中都可使用)
# #
# #         1 获取函数的相对url 和绝对url
# #
# #             1 相对url
# #
# #                 url_for('函数名')
# #
# #             2 绝对url
# #
# #                 url_for('函数名', _external=True)
# #
# #             3 生成动态路由
# #
# #                 url_for('函数名', name="xx") # name="xx" 如果对应函数中包含有name参数 就会生成/xx
# #
# #             4 添加额外参数
# #
# #                 url_for('函数名', name="xx") # name="xx" 如果对应函数不包含有name参数 就会生成/?name=xx
# #
# #     12 静态文件
# #
# #          1 原理 url_map中 默认使用了
# #
# #             <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
# #
# #          2 引用
# #
# #             url_for('static', filename='xx/xxxx/xxxxx.xx')
# #
# #     13 Flask-Moment本地化日期和时间
# #
# #         把时间单位发送给 Web 浏览器，转换成当地时间，然后渲染
# #
# #     14 web表单（flask-wtf）
# #
# #         1 概念
# #             1默认情况下，Flask-WTF 能保护所有表单免受跨站请求伪造
# #             2这个类定义表单中的一组字段，每个字段都用对象表示。字段对象可附属一个或多个验证函数
# #         2 安装
# #
# #             pip3 install flask-wtf
# #
# #         3 csrf保护
# #
# #             1 可程序中配置也可也可从文件或环境中导入配置值（一般写入配置文件中）
# #
# #                 1 程序中配置
# #                     app.config['SECRET_KEY'] = '随机字符串' # flask-wtf使用这个秘钥生成加密令牌再用令牌验证请求中表单数据的真伪
# #
# #         4 表单类
# #
# #              1 创建表单类
# #                 from wtforms import StringField, SubmitField
# #
# #                 class TestForm(FlaskForm):
# #
# #                     name = StringField('你的名字', validators=[DataRequired(message='不能为空')])
# #                     submit = SubmitField(label='提交')
# #
# #              2 把表单渲染成HTML
# #
# #
# #
# #                 @app.route('/test_form/')
# #                 def test_form():
# #                     form = TestForm() # 创建表单类的对象
# #                     return render_template('test_form.html', form=form) # 表单对象类传入到模板中
# #
# #                 html文件中
# #                 <form action="{{ url_for('test_form') }}">
# #
# #                     {{ form.hidden_tag() }}
# #                     {{ form.name.label }}{{ form.name(id='xx') }}  # 可以为字段指定 id 或 class 属性，然后定义 CSS 样式
# #                     {{ form.submit() }}
# #
# #                 </form>
# #              3 使用bootstrap是表单样式变得更美（bootstrap提供的表单）
# #
# #                 {% extends 'base.html' %}
# #                 {% import 'bootstrap/wtf.html' as wtf %} # import 和python用法一样
# #
# #
# #                 {% block page_content %}
# #                     {{ wtf.quick_form(form) }}
# #                 {% endblock %}
# #
# #              4 路由函数接受post请求
# #                 app.route('/test_form/', methods=['GET', 'POST'])
# #                 def test_form():
# #                     ....
# #
# #              5 接受用户信息与用户互动
# #
# #                 @app.route('/test_form/', methods=['GET', 'POST'])
# #                 def test_form():
# #                     name = None
# #                     form = TestForm()
# #                     if form.validate_on_submit():  # 如果表单验证成功 数据的 POST 请求。 validate_on_submit() 会调用
# #                                                         # name 字段上附属的 Required() 验证函数。如果名字不为空，就能通过验证，
# #                                                         # validate_on_submit() 返回 True
# #                         name = form.name.data      # 获取用户输入的name值
# #                     return render_template('test_form.html', form=form, name=name)
# #
# #         5 重定向和用户会话
# #
# #             问题 1用户发送post后刷新页面的时候浏览器会提示是否重新提交post的弹框
# #                 2重定向之后 用户发送的post数据会丢失
# #
# #             解决
# #                 1 重定向 将post请求变成get请求
# #                 2 将用户发送的数据存到session中
# #                 class TestForm(FlaskForm):
# #
# #                     name = StringField('你的名字', validators=[DataRequired()])
# #                     submit = SubmitField(label='提交')
# #
# #
# #                 @app.route('/test_form/', methods=['GET', 'POST'])
# #                 def test_form():
# #
# #                     form = TestForm()
# #                     if form.validate_on_submit():  # 如果表单验证成功
# #                         session['name'] = form.name.data      # 获取用户输入的name值
# #                         return redirect(url_for('test_form'))
# #                     return render_template('test_form.html', form=form, name=session.get('name', None))
# #
# #         6 Flash消息
# #
# #             1 概念
# #
# #                 显示提示的消息
# #
# #             2 用户更改提交的名字若和之前不一样，会出现提示消息
# #                 class TestForm(FlaskForm):
# #
# #                     name = StringField('你的名字', validators=[DataRequired()])
# #                     submit = SubmitField(label='提交')
# #
# #
# #                 @app.route('/test_flash/', methods=['GET', 'POST'])
# #                 def test_flash():
# #
# #                     form = TestForm()
# #                     if form.validate_on_submit():
# #                         if session['name'] and form.name.data != session['name']:
# #                             flash('好像您改了名字哦！！！')
# #                         session['name'] = form.name.data
# #                         return redirect(url_for('test_flash'))
# #                     return render_template('test_form.html', form=form, name=session.get('name', None))
# #
# #                 主模板中
# #
# #                     {% for message in get_flashed_messages() %}
# #                         {{ message }}
# #                     {% endfor %}
# #
# #
# #         7 WTForms支持的HTML标准字段
# #             字段类型        说明
# #             StringField 文本字段
# #             TextAreaField 多行文本字段
# #             PasswordField 密码文本字段
# #             HiddenField 隐藏文本字段
# #             DateField 文本字段，值为 datetime.date 格式
# #             DateTimeField 文本字段，值为 datetime.datetime 格式
# #             IntegerField 文本字段，值为整数
# #             DecimalField 文本字段，值为 decimal.Decimal
# #             FloatField 文本字段，值为浮点数
# #             BooleanField 复选框，值为 True 和 False
# #             RadioField 一组单选框
# #             SelectField 下拉列表
# #             SelectMultipleField 下拉列表，可选择多个值
# #             FileField 文件上传字段
# #             SubmitField 表单提交按钮
# #             FormField 把表单作为字段嵌入另一个表单
# #             FieldList 一组指定类型的字段
# #
# #
# #         8 WTForms验证函数
# #             Email 验证电子邮件地址
# #             EqualTo 比较两个字段的值；常用于要求输入两次密码进行确认的情况
# #             IPAddress 验证 IPv4 网络地址
# #             Length 验证输入字符串的长度
# #             NumberRange 验证输入的值在数字范围内
# #             Optional 无输入值时跳过其他验证函数
# #             Required 确保字段中有数据
# #             Regexp 使用正则表达式验证输入值
# #             URL 验证 URL
# #             AnyOf 确保输入值在可选值列表中
# #             NoneOf 确保输入值不在可选值列表中
# #
# #
# #     15 数据库使用Flask-SQLAlchemy
# #
# #         1 安装
# #
# #             pip3 install flask-sqlalchemy
# #
# #         2 配置数据库
# #
# #             from flask_sqlalchemy import SQLAlchemy
# #             base_dir = os.path.abspath(os.path.dirname(__file__))
# #             app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
# #             app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True # 每次请求结束后都会自动提交数据库中的变动
# #             db = SQLAlchemy(app)
# #
# #         3 定义模型
# #
# #             class Role(db.Model):   # 注意继承sqlalchemy对象.Model
# #                 __tablename__ = 'role'  # 定义数据库中的表明
# #                 id = db.Column(db.Column(db.Integer, primary_key=True)) # 主键
# #                 rolename = db.Column(db.String(64), unique=True)  # unique 唯一
# #                 user = db.relationship('User', backref='role') # 代表这个关系的面向对象视角，
# #                                                                # 对于一个 Role 类的实例，其 users 属性将返回与角色相关联的用户
# #                                                                # 组成的列表db.relationship() 的第一个参数表明这个关系的另一端是哪个模型
# #                                                                #  backref 参数向 User 模型中添加一个 role 属性，从而定义反向关系。
# #                                                                # 这一属性可替代 role_id 访问 Role 模型，此时获取的是模型对象而不是外键的值
# #
# #                 def __repr__(self):
# #                     return self.rolename
# #
# #
# #             class User(db.Model):
# #                 __tablename__ = 'user'
# #                 id = db.Column(db.Integer, primary_key=True)
# #                 username = db.Column(db.String(64), unique=True, index=True) # index为创建索引，提升查询效率
# #                 role_id = db.Column(db.Integer, db.ForeignKey('role.id')) # 添加外键为role表中的行id值
# #
# #                 def __repr__(self):
# #                     return self.username
# #
# #             最常用的SQLAlchemy列类型
# #                 类型名     Python类型        说明
# #                 Integer         int         普通整数，   一般是 32 位
# #                 SmallInteger    int        取值范围小的整数，一般是 16 位
# #                 BigInteger  int 或 long 不限制精度的整数
# #                 Float       float   浮点数
# #                 Numeric decimal.Decimal 定点数
# #                 String      str         变长字符串
# #                 Text        str         变长字符串，对较长或不限长度的字符串做了优化
# #                 Unicode     unicode     变长 Unicode 字符串
# #                 UnicodeText unicode     变长 Unicode 字符串，对较长或不限长度的字符串做了优化
# #                 Boolean     bool 布尔值
# #                 Date        datetime.date 日期
# #                 Time        datetime.time 时间
# #                 DateTime    datetime.datetime 日期和时间
# #                 Interval    datetime.timedelta 时间间隔
# #                 Enum        str 一组字符串
# #                 PickleType 任何 Python 对象 自动使用 Pickle 序列化
# #                 LargeBinary     str 二进制文件
# #
# #             最常使用的SQLAlchemy列选项
# #                 primary_key 如果设为 True ，这列就是表的主键
# #                 unique 如果设为 True ，这列不允许出现重复的值
# #                 index 如果设为 True ，为这列创建索引，提升查询效率
# #
# #                  如果设为 True ，这列允许使用空值；如果设为 False ，这列不允许使用空值
# #                 default 为这列定义默认值
# #
# #             常用的SQLAlchemy关系选项
# #
# #                 选项名 说　　明
# #                 backref 在关系的另一个模型中添加反向引用
# #                 primaryjoin 明确指定两个模型之间使用的联结条件。只在模棱两可的关系中需要指定
# #                 lazy 指定如何加载相关记录。可选值有 select （首次访问时按需加载）、 immediate （源对象加
# #                         载后就加载）、 joined （加载记录，但使用联结）、 subquery （立即加载，但使用子查询），
# #                         noload （永不加载）和 dynamic （不加载记录，但提供加载记录的查询）
# #                 uselist 如果设为 Fales ，不使用列表，而使用标量值
# #                 order_by 指定关系中记录的排序方式
# #                 secondary 指定多对多关系中关系表的名字
# #                 secondaryjoin SQLAlchemy 无法自行决定时，指定多对多关系中的二级联结条件
# #
# #         4 数据库操作
# #
# #             1 增
# #
# #                 1 创建表
# #
# #                     db.create_all()  # 如果修改模型，执行此操作 数据库不会更新模型
# #
# #                 2 插入单行数据
# #
# #                     s= Role(name="xx")
# #                     db.session.add(s)
# #                     db.session.commit()
# #
# #                 3 插入多行数据
# #                     s1 = Role(name="xx")
# #                     s2 = Role(name="xx")
# #                     db.session.add_all([s1, s2])
# #                     db.session.commit()
# #
# #             2 删
# #
# #                 1 删除表
# #
# #                     db.drop_all()
# #
# #                 2 删除行数据
# #
# #                     db.session.delete(s)
# #                     db.session.commit
# #
# #             3 改
# #                 1 修改数据
# #                     s.name = 'yyy'
# #                     db.session.add(s)
# #                     db.session.commit()
# #
# #
# #             4 查
# #                 1 获取对象所有数据
# #
# #                     对象.qurey.all()
# #
# #                 2 查询原生SQL查询语句
# #
# #                     str(执行语句)
# #
# #                 3
# #
# #                 常用的SQLAlchemy查询过滤器
# #
# #                     过滤器         说明
# #                     filter()        把过滤器添加到原查询上，返回一个新查询 # 参数中用（对象.属性=xx）
# #                     filter_by()     把等值过滤器添加到原查询上，返回一个新查询 # 参数中用（属性=xx）
# #                     limit()         使用指定的值限制原查询返回的结果数量，返回一个新查询
# #                     offset()        偏移原查询返回的结果，返回一个新查询
# #                     order_by()      根据指定条件对原查询结果进行排序，返回一个新查询
# #                     group_by()      根据指定条件对原查询结果进行分组，返回一个新查询
# #
# #                 最常使用的SQLAlchemy查询执行函数
# #
# #                     all()       以列表形式返回查询的所有结果
# #                     first()     返回查询的第一个结果，如果没有结果，则返回 None
# #                     first_or_404() 返回查询的第一个结果，如果没有结果，则终止请求，返回 404 错误响应
# #                     get()       返回指定主键对应的行，如果没有对应的行，则返回 None
# #                     get_or_404() 返回指定主键对应的行，如果没找到指定的主键，则终止请求，返回 404 错误响应
# #                     count()     返回查询结果的数量
# #                     paginate()  返回一个 Paginate 对象，它包含指定范围内的结果
# #
# #             5 与视图模板数据库互动，新用户和老用户欢迎消息不同
# #
# #                 @app.route('/do_with_database/', methods=['GET', 'POST'])
# #                 def do_with_database():
# #
# #                     form = TestForm()
# #                     if form.validate_on_submit():
# #
# #                         if User.query.filter_by(username=form.name.data).first(): #
# #                             session['name'] = form.name.data
# #                             flash(message='老朋友%r,又见面了'%(form.name.data))
# #                             return redirect(url_for('do_with_database'))
# #
# #                         db.session.add(User(username=form.name.data))
# #
# #                         session['name'] = form.name.data
# #                         flash(message='欢迎您%r第一次到来'%(session.get('name')))
# #
# #                         return redirect(url_for('do_with_database'))
# #
# #                     return render_template('do_with_database.html', form=form)
# #
# #             6 集成python shell
# #
# #                 1 概念
# #
# #                     使用python shell 向数据库添加数据 不用再导入类模型等（省去了import 操作），直接使用命令
# #                     向数据库添加数据
# #
# #                 2 配置
# #                     1 为shell命令添加一个上下文
# #
# #                     from flask_script import Shell
# #
# #                     def make_shell_context():
# #                         return dict(app=app, db=db, User=User, Role=Role)
# #                     manager.add_command('shell', Shell(make_context=make_shell_context))
# #
# #             7 数据库迁移Flask-Migrate
# #
# #                 基本使用命令
# #
# #                     python xx.py db init    # 创建迁移仓库
# #                     python xx.py db migrate -m "initial migration"  # 若模型有改动执行此命令
# #                     python xx.py db upgrade # 执行迁移 将新的模型更新到数据库
# #
# #                 1 概念
# #                     使用flask-Migrate执行数据库创建
# #                     如果修改了数据模型， 不得不删除数据库再重新创建数据库达到模型跟新的目的，但是数据就会丢失
# #                     为了解决数据丢失，Flask_Migrate数据迁移功能
# #
# #                 2 安装
# #
# #                     pip3 install flask-migrate
# #
# #                 3 使用
# #
# #                     1 创建迁移仓库
# #
# #                         1 配置Flask-Migrate
# #
# #                             from flask_migrate import Migrate, MigrateCommand
# #                             migrate = Migrate(app, db)
# #                             manager.add_command('db', MigrateCommand)
# #
# #                         2 创建迁移仓库
# #
# #                             python xx.py db init # 会生成migrations目录
# #
# #
# #                     2 创建迁移脚本
# #
# #                         python xx.py db migrate -m "initial migration"
# #
# #                     3 跟新数据库
# #
# #                         python xx.py db upgrade
# #
# #         5 电子邮件
# #
# #             1 概念
# #
# #                 在flask程序中发送电子邮件
# #
# #             2 安装
# #
# #                 pip3 install flask-mail
# #
# #             3 配置
# #                 1 概念
# #                     Flask-Mail SMTP服务器的配置
# #
# #                     配　　置        默认值     说明
# #                     MAIL_SERVER  localhost 电子邮件服务器的主机名或 IP 地址
# #                     MAIL_PORT 25 电子邮件服务器的端口
# #                     MAIL_USE_TLS False 启用传输层安全（Transport Layer Security，TLS）协议
# #                     MAIL_USE_SSL False 启用安全套接层（Secure Sockets Layer，SSL）协议
# #                     MAIL_USERNAME None 邮件账户的用户名
# #                     MAIL_PASSWORD None 邮件账户的密码
# #
# #                 2 配置
# #
# #                     1 初始化 Flask-Mail
# #
# #                         from flask_mail import Mail
# #                         mail = Mail(app)
# #
# #                     1 将账户密码设置在环境变量中（为了安全 不这样做也行直接写入配置文件中）
# #
# #                         linux
# #                             (venv) $ export MAIL_USERNAME=<Gmail username>
# #                             (venv) $ export MAIL_PASSWORD=<Gmail password>
# #
# #                         windows
# #
# #                             (venv) $ set MAIL_USERNAME=<Gmail username>
# #                             (venv) $ set MAIL_PASSWORD=<Gmail password>
# #
# #                     2 主文件中配置
# #                         app.config['MAIL_SERVER'] = 'smtp.qq.com'
# #                         app.config['MAIL_PORT'] = 25
# #                         app.config['MAIL_USE_SSL'] = False
# #                         app.config['MAIL_USE_TLS'] = False
# #                         app.config['MAIL_USERNAME'] = "174927390@qq.com"
# #                         app.config['MAIL_PASSWORD'] = "baleguedteflbhci"
# #                     3 测试发送电子邮件
# #                         def send_mail():
# #                             msg = Message(subject='11111111', sender='174927390@qq.com', recipients=['174927390@qq.com'])
# #                             msg.body = 'body'
# #                             msg.html = '<b>html</b>'
# #                             mail.send(msg)
# #
# #
# #                         @app.route('/test_mail/')
# #                         def test_mail():
# #
# #                             send_mail()
# #                             return '1111'
# #
# #         6 大型程序结构
# #
# #             app/   # 放路由文件，static template
# #                 main/
# #                     __init__.py
# #                         from flask import Blueprint # 在蓝本中定义的路由处于休眠状态，需要注册到程序工厂函数中
# #                         main = Blueprint('main', __name__) # 参数1：蓝本的名字，参数2：蓝本所在模块
# #                         from . import views
# #                     views.py
# #                         使用蓝本定义路由
# #                             from flask import render_template
# #                             from . import main
# #
# #                             @main.route('/')    # 路由修饰器有蓝本提供 # url_for('main.index')
# #                             def index():
# #                                 return render_template('index.html')
# #
# #                 static/
# #                 templates/
# #                 __init__.py
# #                     from config import config
# #                     from flask import Flask
# #
# #                     def create_app():   # 工厂函数 在创建实例之前对环境进行配置
# #                         app = Flask(__name__)
# #                         app.config.from_object(config['default']) # 通过from_object方法直接导入配置
# #                         config['default'].init_app(app)  # 初始化配置
# #
# #                         from .main import main as main_blueprint  # 注意在此处导入蓝图
# #                         app.register_blueprint(main_blueprint)  # 注册蓝本
# #                         return app
# #                 models.py
# #             config.py # 配置文件
# #                 class Config:
# #                     DEBUG = True
# #
# #                     @staticmethod
# #                     def init_app(app):
# #                         pass
# #
# #                 config = {
# #                     "default": Config
# #                 }
# #             manage.py # 启动文件
# #                 from app import create_app
# #                 app = create_app()
# #                 if __name__ == '__main__':
# #                     app.run()
# #
# #             1 蓝图中配置静态文件
# #
# #                 main.static_folder = 'static'   # 配置静态文件
# #                 main.static_url_path = '/static' # 配置url静态文件位置
# #
# #                 html中使用
# #                 <img src="{{ url_for('main.static', filename='test.jpg') }}" alt="">
# #
# #             2 蓝图下的反向解析
# #
# #                 print(url_for('main.index'))  # 蓝图下的url反向解析
# #
# #             3 环境依赖包的保存文件和到了新项目的安装
# #
# #                 1 保存
# #                     1 创建文件 requirements.txt
# #                     2 执行命令将环境依赖包存入 requirements
# #                         pip3 freeze > requirements.txt
# #                 2 安装
# #                     pip3 install -r requirements.txt
# #
# #         7 用户认证
# #
# #             1 为用户密码加密 使用Werkzeug显示密码散列
# #
# #                 from werkzeug.security import generate_password_hash, check_password_hash
# #
# #                 class Test(db.Model):
# #
# #                     __tablename__ = 'test'
# #
# #                     id = Column(Integer, primary_key=True)
# #                     name = Column(String(32))
# #
# #                     password_hash = db.Column(db.String(128))
# #
# #                     @property
# #                     def password(self):
# #                         raise AttributeError('密码不可读取')
# #
# #                     @password.setter                # 通过 obj.password="xx" 对密码进行加工，生产加工后密码
# #                     def password(self, password):
# #                         self.password_hash = generate_password_hash(password)
# #
# #                     def check_password(self, password):  # 通过 obj.check_password("xx") 对密码进行加工后， 核对上面生成的加工密码
# #                         return check_password_hash(self.password_hash, password)
# #
# #             2 创建一个目录 用来验证用户，注册成蓝本
# #                     .....照旧
# #                     app.register_blueprint(auth_blueprint, url_prefix="/auth")  # url_prefix参数为url添加前缀
# #
# #
# #             3 安装用户认证组件flask_login
# #
# #                 pip3 install flask-login
# #
# #             4 使用flask_login
# #
# #                 1 创建用户登录的用户模型 添加加载用户的回调函数
# #
# #                     必须实现4个用户方法 或 模型直接继承 UserMixin
# #                         is_authenticated() 如果用户已经登录，必须返回 True ，否则返回 False
# #                         is_active() 如果允许用户登录，必须返回 True ，否则返回 False 。如果要禁用账户，可以返回 False
# #                         is_anonymous() 对普通用户必须返回 False
# #                         get_id() 必须返回用户的唯一标识符，使用 Unicode 编码字符串
# #
# #                     class Users(UserMixin, db.Model):
# #
# #                         __tablename__ = 'users'
# #
# #                         id = Column(Integer, primary_key=True)
# #                         name = Column(String(32))
# #                         password_hash = Column(db.String(128))
# #                         email = Column(String(64), unique=True, index=True)
# #                         role_id = Column(Integer, ForeignKey('roles.id'))
# #
# #
# #                         @login_manager.user_loader  # 添加加载用户的回调函数
# #                         def load_user(user_id):
# #                             return Users.query.get(int(user_id)) # 如果能找到用户，这个函数必须返回用户对象，否则返回None
# #
# #                         @property
# #                         def password(self):
# #                             raise AttributeError('密码不可读取')
# #
# #                         @password.setter                # 通过 obj.password="xx" 对密码进行加工，生产加工后密码
# #                         def password(self, password):
# #                             self.password_hash = generate_password_hash(password)
# #
# #                         def check_password(self, password):  # 通过 obj.check_password("xx") 对密码进行加工后， 核对上面生成的加工密码
# #                             return check_password_hash(self.password_hash, password)
# #
# #                     class Roles(db.Model):
# #                         __tablename_ = "roles"
# #                         id = Column(Integer, primary_key=True)
# #                         role_name = Column(String(64), unique=True, index=True)
# #                         users = db.relationship('Users', backref='roles')
# #
# #                 2 工厂函数中初始化flask-login
# #
# #                     from flask_login import LoginManager
# #
# #                     ...
# #                     login_manager = LoginManager()
# #                     login_manager.session_protection = "strong" # 值可设置为None，'basic','strong'为不同的安全防护等级设为
# #                                                                   #'strong' 时，Flask-Login 会记录客户端 IP地址和浏览器的
# #                                                                   # 用户代理信息，如果发现异动就登出用户
# #                     login_manager.login_view = 'auth.login'     # 登录页面的路由端点
# #
# #                     def create_app():
# #                         ...
# #                         login_manager.init_app(app)
# #                         ...
# #
# #                 3 是只有认证的用户才能访问路由（login_required修饰器）
# #
# #                     from flask_login import login_required
# #
# #                     @xx.route('/test_user_auth')
# #                     @login_required
# #                     def secret():
# #                         return '您不是认证用户'
# #
# #                 4 展示用户的登录状态
# #
# #                     <ul class="nav navbar-nav navbar-right">
# #                         {% if current_user.is_authenticated %}  # 如果当前用户是验证用户变量 current_user 由 Flask-Login 定义，
# #                                                                     # 且在视图函数和模板中自动可用。这个变量的值是当前登录的用户，
# #                                                                     # 如果用户尚未登录，则是一个匿名用户代理对象。如果是匿名用户，
# #                                                                     # is_authenticated() 方法返回 False
# #                         <li><a href="{{ url_for('auth.logout') }}">Sign Out</a></li>
# #                         {% else %}
# #                         <li><a href="{{ url_for('auth.login') }}">Sign In</a></li>
# #                         {% endif %}
# #                     </ul>
# #
# #                 5 接受用户的post 验证用户是否存在，验证密码是否正确，根据用户是否记住登录账户和密码绝对设置不设置cookie，登录成功后返回原来地址
# #
# #                     @auth.route('/login/', methods=['GET', 'POST'])
# #                     def login():
# #                         user_login = UserLogin()
# #                         if user_login.validate_on_submit():
# #                             user = Users.query.filter_by(email=user_login.email.data).first() # 去数据库中查询是否有此用户
# #                             if user and user.check_password(user_login.password.data):        # 如果用户存在 在测试密码是否正确
# #                                 login_user(user, user_login.remember_me.data)       # 如果用户点击记住账户密码，会在用户浏览器
# #                                                                                         # 中写入一个长期有效的 cookie，使用这个 cookie 可以复现用户会话
# #                                 return redirect(request.args.get('next') or url_for('main.index')) # Flask-Login会把原地址保存在查询字符串的 next 参数中
# #                             flash('账户密码错误或未注册')         # 如果出现错误会 出现错误提示
# #                         return render_template('login.html', user_login=user_login)
# #
# #
# #
# #                 6 退出登录
# #
# #                     @auth.route('/logout/')
# #                     @login_required
# #                     def logout():
# #                         logout_user() # 删除并重设用户会话
# #                         flash('您已经退出登录状态')
# #                         return redirect(url_for('main.index'))
# #
# #                 7 用户注册
# #
# #                     1 创建用户注册表单
# #                         class UserRegisterForm(FlaskForm):
# #                             """用户注册表单
# #                                 Regexp() 为正则验证方法
# #                                 EqualTo() 为比较字段的方法
# #                                 def_字段(self,field) 字段的自定义验证函数
# #                             """
# #                             email = StringField(label="邮箱", validators=[DataRequired(), Length(1,64), Email()])
# #                             username = StringField(label="用户名", validators=[DataRequired(), Length(1, 64), Regexp('^[a-zA-Z_.]*$',flags=0, message='取名字不符合规范')])
# #                             password = PasswordField(label="密码", validators=[DataRequired(), EqualTo('password2', message='密码两次输入不匹配')])
# #                             password2 = PasswordField(label="确认密码", validators=[DataRequired()])
# #                             submit = SubmitField(label="提交")
# #
# #                             def validate_email(self, field):
# #                                 if Users.query.filter_by(email=field.data).first():
# #                                     raise ValidationError('该邮箱已存在，存在请使用其他邮箱')
# #
# #                             def validate_username(self, field):
# #                                 if Users.query.filter_by(username=field.data).first():
# #                                     raise Validation
# #
# #                 8 测试登录
# #
# #                     {% block page_content %}
# #
# #                         {% if current_user.is_authenticated %}   # 如果当前用户是已验证用户
# #                             <h1>hello, {{ current_user.username }}</h1>  # 获取当前登录用户名， 如果未登录返回none
# #                         {% else %}
# #                             <h1>hello, 陌生人</h1>
# #                         {% endif %}
# #
# #                     {% endblock %}
# #
# #                 9 确认账户，向账户注册的邮箱中发送信息（对用户id进行加密发送），用户点击信息，确认成功
# #
# #                     1 加密工具(TimedJSONWebSignatureSerializer等)
# #
# #                         1 使用
# #                             1 导入模块
# #                             2 创建类对象： 类（字符串, expires_in=秒数）
# #                             3 加密 对象.dumps(..)
# #                             4 解密 对象.loads(..)
# #                                 from itsdangerous import  TimedJSONWebSignatureSerializer as Serializer
# #                                 s = Serializer('xx', expires_in=3600)
# #                                 a = s.dumps('aa')   # 加密
# #                                 s.loads(a)          # 解密
# #
# #                     2 向模型中添加 加密工具（TimedJSONWebSignatureSerializer）
# #
# #                         强烈注意 s.dumps(xx)方法 会生成二进制字符串， 发送到浏览器，从浏览器返回字后会变成 字符串类型
# #                         所以返送前后不一样 解决方法  把s.dumps(xx)转换成二进制用 .decode() 解码成字符串，那么发送到浏览器
# #                         再返回来的就都是字符串，就一样了！！！！
# #
# #
# #                         class Users(UserMixin, db.Model):
# #
# #                             __tablename__ = 'users'
# #
# #                             ...
# #                             activate = Column(Boolean, default=False)
# #                             ...
# #
# #                             def make_activate_info(self, expiration=3600):
# #                                 """生成令牌"""
# #                                 s = Serializer(current_app.config['SECRET_KEY'], expiration)
# #                                 return s.dumps({'activate': self.id}).decode() !!!!!!!!注意加上！！！decode()
# #
# #                             def to_activate(self, code_from_user): # 还检查令牌中的 id 是否和存储在 current_user 中的已登录用户匹配
# #                                 """检验令牌"""
# #                                 s = Serializer(current_app.config['SECRET_KEY'])
# #                                 try:
# #                                     data = s.loads(code_from_user)
# #                                 except:
# #                                     return False
# #
# #                                 if data.get('activate') != self.id:
# #                                     return False
# #                                 self.activate = True
# #                                 db.session(self)
# #                                 return True
# #
# #                     3 实现用户注册成功将数据添加到数据库之后，向用户注册的邮箱内发送激活认证邮件
# #                         @auth.route('/register/', methods=['GET', 'POST'])
# #                         def register():
# #                             form = UserRegisterForm()
# #                             if form.validate_on_submit():
# #                                 user = Users(email=form.email.data, username=form.username.data, password=form.password.data)
# #                                 db.session.add(user)
# #                                 db.session.commit()
# #                                 code = user.make_activate_info()
# #                                 send_mail(code, user.username)
# #                                 flash('注册完毕！请先登录,已经发送邮件到您的邮箱，请点击激活')
# #
# #                                 return redirect(url_for('auth.login'))
# #                             return render_template('register.html', form=form)
# #
# #
# #                         @auth.route('/active/<token>')
# #                         @login_required
# #                         def active(token):
# #                             print(token, 222222222222222222222222222)
# #                             if current_user.active:
# #                                 return redirect(url_for('main.index'))
# #                             if current_user.to_active(token):
# #                                 flash('您已经激活了你的账户')
# #                             else:
# #                                 flash('邮箱激活连接已经过期，请重新激活')
# #                             return redirect(url_for('main.index'))
# #
# #                     4 蓝本中使用全局请求钩子（before_app_request）拦截用户
# #                         实现了对登录后为激活邮箱的用户进行重定向到在此发送邮件路由
# #                         对用户拦截的条件
# #                             1 是登录用户 且
# #                             2 当前用户没有认证 且
# #                             3 请求的不是 auth.蓝本的视图函数
# #                             4 请求路径不是"static"
# #
# #                             @auth.before_app_request
# #                             def before_request():
# #                                 if current_user.is_authenticated() and \
# #                                     not current_user.to_active() and \
# #                                     request.endpoint[:5] != 'auth.' and \
# #                                     request.endpoint != 'static':
# #                                     return redirect(url_for('auth.un_active'))
# #
# #                             @auth.route('/un_active/')
# #                             def un_active():
# #
# #                                 if current_user.is_anonymous or current_user.active:
# #
# #                                     return redirect(url_for('main.index'))
# #                                 return render_template('un_active.html')
# #
# #                     5 重新发送确认邮件
# #                         @auth.route('/active/')
# #                         def resend_mail():
# #                             code = current_user.make_activate_info()
# #                             send_mail(code, current_user.username)
# #                             flash('一份新的邮件已经发送到您的邮箱')
# #                             return redirect(url_for('main.index'))
# #
# #                 10 管理账户
# #
# #                     1 修改密码  (@@@@@@@@@@对添加的代码就行修改)
# #                         要求
# #                             1 用户处于登录状态
# #                             2 要求用户输入旧密码和替换的新密码
# #                             @auth.route('/change_password/', methods=['GET', 'POST'])
# #                             def change_password():
# #                                 form = ChangePasswordForm()
# #                                 original_pass = form.original_password.data
# #                                 new_pass = form.new_password.data
# #                                 if form.validate_on_submit():
# #                                     if current_user.check_password(original_pass):
# #                                         current_user.password = new_pass
# #                                         flash('密码更新完毕，请重新登录')
# #                                         logout_user()
# #                                         return redirect(url_for('auth.login'))
# #                                     flash('您输入的原始密码不正确！！！')
# #                                     return render_template('change_password.html', form=form)
# #                                 return render_template('change_password.html', form=form)
# #
# #                     2 忘记密码重设密码（客户忘记密码时候使用）
# #                         要求
# #                             1 使用提供电子邮件地址
# #                             2 向邮件地址发送code，用户点击code进行验证，出现输入新密码表单
# #
# #                             @staticmethod
# #                             def restart_pwd(code, new_password):
# #
# #                                 s = Serializer(current_app.config['SECRET_KEY'])
# #                                 data = s.loads(code.encode('utf-8'))
# #
# #                                 user_id = data.get('active', None)
# #                                 if not user_id:
# #                                     return False
# #
# #                                 user = Users.query.filter_by(id=user_id).first()
# #
# #                                 user.password = new_password
# #                                 db.session.add(user)
# #                                 db.session.commit()
# #                                 return True
# #
# #                             @auth.route('/forget_password/', methods=['GET', 'POST'])
# #                             def forget_password():
# #                                 form = ForgetPasswordForm()
# #                                 if form.validate_on_submit():
# #                                     user = Users.query.filter_by(email=form.email.data).first()
# #                                     code = user.make_activate_info()
# #                                     print(repr(code), 22222222222222)
# #                                     send_restart_password_mail(code)
# #                                     flash('一份邮件发送到您的邮箱，请进行确认')
# #
# #                                 return render_template('forget_password.html', form=form)
# #
# #
# #                             @auth.route('/restart_password/<code>', methods=['GET', 'POST'])
# #                             def restart_password(code):
# #
# #                                 form = RestartPasswordForm()
# #                                 if form.validate_on_submit():
# #                                     print(repr(code), 11111111111111111)
# #                                     Users.restart_pwd(code=code, new_password=form.password.data)
# #                                     flash('您已经找回密码请登录')
# #                                     return redirect(url_for('auth.login'))
# #
# #
# #                                 return render_template('restart_password_form.html', form=form)
# #
# #
# #
# #                     3 修改电子邮件地址
# #                         要求
# #
# #                             1 验证新地址，发送确认邮件到新地址
# #                             2 储存用户的新地址到数据库，邮箱验证之后，和数据库邮箱对比（能对比？）更新邮箱
# #
# #
# #                         # 暂停！！！！！！！！！！！！！！！！！！！！！！！！！！学完django后再学
# #
# #
# #
# #
# 1
# # ====================================================
#
# 1
# # 使用项目后
# #
# # 1
# # 执行命令安装相关依赖包
# #
# # pip3
# # install - r
# # requirements.txt
# #
# # 2
# # 初始化数据库如果定义完模型类
# #
# # python
# # manage.py
# # db
# # init  # 创建迁移仓库
# # python
# # manage.py
# # db
# # migrate - m
# # "initial migration"  # 若模型有改动执行此命令
# # python
# # manage.py
# # db
# # upgrade  # 执行迁移 将新的模型更新到数据库
# #
# # 3
# # 开发模式下启动服务器
# #
# # python
# # manage.py
# # runserver - d
# 1
#
#
# 1
# # -*- coding:utf-8 -*-
#
# # cookie 和 session的原理
#
# # 自定义字典
#
# #   创建字典的子类 初始化子类
#
# #       def __init__(self):
# #             super(子类名, self).__init__(*args, **kwargs)
# #             self['a'] = True
#
# #         创建对象，对象中默认有{'a': True}
#
# # 配置文件，全局变量大写
#
# # flask第三放扩展网站
# #   flask.pocoo.org/extensions/
#
# # 安装 Flask
# #   pip3 install flask
#
#
# # 配置文件
# # 方式一 app.debug = True 或 app.config['DEBUG'] = True
# # 方式二 app.config.from_pyfile("python文件名") 文件名内部 DEBUG=True 不是主流
# # 主流方式 app.config.from_object('python类或类的路径')
#
#
# # 路由系统
# #   @app.route('/', methods=['GET', 'POST'], endpoint='index')
# #  路由源代码
# #  def route(self, rule, **options):
# #      def decorator(f):
# #          endpoint = options.pop('endpoint', None)
# #          self.add_url_rule(rule, endpoint, f, **options)
# #          return f
# #      return decorator
# #  支持vbv
# #
# #
#
#
# # 路由参数 @app.route和app.add_url_rule参数
# # rule 路由规则
# # view_func     视图函数名称
# # defaultes = None 默认值当URL中无参数，函数需要参数时，使用defaults={'k':'v'}提供参数
# # endpoint = None
# # method=None
# # strict_slashes = None 对URL最后/符号是否严格要求
# # redirect_to=None 重定向到的地址
# # subdomain=None 子域名访问
# # linux的host文件
#
# # 路由可添加正则表达式
# # 。。。。
#
#
# # 模板
# # 转义——宏
#
#
# # request
# # obj = request.files('the_file_name')
# # obj.save('/var/www/uploads/'+secure_file(f.filename))
#
# # make_response
# # response = make_response(render_template('index.html'))
# # response.set_cookie('key', 'value')
#
#
# # session
# # flask内置的使用 加密cookie(签名cookie)来保存数据
# # session['a1'] = 'a1'
# 1
#
#
# 1
# # -*- coding:utf-8 -*-
#
# # 创建网站核心思想
# #
# #   想清楚网站的核心价值，其他功能都是辅助功能
# #   一句话概括网站的核心价值/功能
# #
# #
# #   思维导图一步一步开始
# #
# #
# #
# #                            --isbn号搜索
# #                                       --调用外部API
# #                  --3搜索数据--关键字搜索
# #
# #               鱼书--1选择要赠送的图书：向他人赠送书籍
# #
# #                  --2选择自己想要的书：向他人所要书籍
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # 虚拟环境新的安装方法
# #
# #   使用pipenv
# #
# #       pipenv是安装虚拟环境的工具 pip install pipenv
# #       项目目录下安装虚拟环境 pipenv install
# #       激活虚拟环境 pipenv shell
# #       使用pipenv 安装虚拟环境，安装其他包的时候 也用命名 pipenv install 包名
# #
# #       pipenv相关命令
# #
# #               exit: 退出虚拟环境
# #               pipenv shell: 进入虚拟环境
# #               pipenv install flask: 安装包
# #               pipenv uninstall flask: 卸载包
# #               pipenv graph 显示包的依赖关系
# #               pipenv --venv 显示虚拟环境的安装目录
# #
# # 开发工具推荐
# #
# #   pycharm
# #
# #   Xampp(MySQL) 功能强大的建站集成包
# #
# #   Navicat(数据库可视化管理工具)
# #
# #
# # ubuntu安装mysql
# #
# #   首先执行下面三条命令：
# #
# #       sudo apt-get install mysql-server
# #
# #       sudo apt isntall mysql-client
# #
# #       sudo apt install libmysqlclient-dev
# #
# #       现在设置mysql允许远程访问，首先编辑文件/etc/mysql/mysql.conf.d/mysqld.cnf：
# #
# #       sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
# #
# #       注释掉bind-address = 127.0.0.1
# #
# #       保存退出，然后进入mysql服务，执行授权命令：
# #
# #       grant all on *.* to root@'%' identified by '你的密码' with grant option;
# #
# #       flush privileges;
# #
# #       然后执行quit命令退出mysql服务，执行如下命令重启mysql：
# #
# #       service mysql restart
# #
# #
# # ubuntu 安装 xampp
# #
# #   sudo chmod 777 xampp-linux-x64-5.6.37-0-installer.run
# #   sudo ./xampp-linux-x64-5.6.37-0-installer.run
# #   ./start_navicat
# #   sudo /opt/lampp/./manager-linux-x64.run
# #
# #
# # 创建最小的文件fisher.py
# #
# #   from flask import Flask
# #
# #   app = Flask(__name__)
# #
# #   app.run()
# #
# #
# # 基于类的视图（即插视图）
# #   好处继承 避免代码重复
# #
# #
# # 修改代码服务器自动重启
# #   app(debug=True)
# #
# #
# # 路由的第二种注册方式
# #   一般使用于基于类的视图
# #   def hello1():
# #     return 'hello1'
# #   app.add_url_rule('/hello1', view_func=hello1)
# #
# #
# # 接受外网的访问,更改端口号
# #   app.run(host='0.0.0.0', debug=True, port=8000)
# #
# # 创建配置文件config.py
# #
# #
# # 载入配置文件
# #   app.config.from_object('config') 导入配置文件的方法 接收参数为文件的路径
# #
# #
# # 读取配置文件
# #   app.config['DEBUG']  读取参数的名称
# #   通过app.config.from_object('config') 读取的配置文件， app.config['xxx']中的参数如果含有
# #   小写，flask会自动将其参数忽略掉
# #
# #
# # 路由器当中的函数的reutrn 的值进行的包装 返回了 status code , content-type ,http,headers
# # 默认清空下 content-type = text/html ,视图函数返回的是Response对象
# #
# #   @app.route('/hello')
# #   def hello():
# #
# #     headers = {
# #         'content-type': 'text/plain'
# #     }
# #     response = make_response('<h1></h1>', 404) 创建了response对象
# #     response.headers = headers                 对headers进行了改写
# #     return response
# #
# #   另一种写法（不用创建response的写法）
# #
# #   @app.route('/hello')
# #   def hello():
# #
# #     headers = {
# #         'content-type': 'text/plain'
# #     }
# #       return '<h1></h1>', 301, headers
# #
# #
# # 数据API 可调用外部数据
# #
# #   图书数据
# #
# #       基础地址：
# #
# #           http://t.yushu.im
# #
# #       关键字搜索：
# #
# #           用start count控制分页
# #           http://t.yushu.im/v2/book/search?q={}&start={}&count={}
# #
# #       isbn搜索：
# #
# #           http://t.yushu.im/v2/book/isbn/{isbn}
# #
# #
# #   豆瓣API
# #
# #       会有访问限制1小时150次 草果次数会被封ip
# #       https://api.douban.com/v2/book
# #
# #
# #
# # 查看外部API需要什么参数
# #
# #
# #
# # 视图函数中的代码根据简洁易读 封装到模块 然后导入
# #
# # python 当中发送请求 1 urllib 2 request
# #
# # requests 发送请求的第三方包
# #
# #   pip install requests
# #
# #
# # class HTTP:
# #    def get(self, url, return_json=True):
# #        r = requests.get(url)
# #        外部的api返回结果为json格式
# #        从r里面拿到json格式的数据
# #
# #        若返回结果的数据不是json格式
# #        if return_json:
# #           return r.json()
# #        else:
# #           return r.text
# #
# #
# # class Http 和 class Http(object)区别
# #
# #   经典类和新式类
# #   py3中没区别 py2中 没有（）是经典类 有（）是新式类
# #
# #
# #
# # 蓝图是解决分文件问题的方法
# #
# #                   app
# #                    |
# #       蓝图 —————— 蓝图 ————————蓝图
# #        |
# #       视图
# #
# #   要使用蓝图 首先要实例化一个蓝图对象
# #
# #       web = Blueprint('蓝图名称'， 蓝图路径（通常__name__）)
# #
# #           web = Blueprint('web', __name__)
# #
# #           @web.route('/book/seach/<q>/<page>')
# #
# #       然后要注册到Flask的核心对象上
# #           app/__init__.py
#
# #           def register_blueprint(app):
# #
# #               app.register_blueprint(web)
# #
# #           要在create_app中调用 register_blueprint(app)
# #
# #
# # 如何在同一个蓝图的下面把视图函数拆分成不同的文件
# #
# #   把web = Blueprint('web', __name__)放到web/__init__.py中
# #
# #   然后在其他文件中导入web
# #
# #       然后在下面导入文件名字如
# #
# #           from app.web import book
# #
# #
# # Request HTTP的请求信息在Request中
# #   q = request.args['q']   args是不可变的字典数据了性
# #   把不可便数据类型转变为可变的数据类型
# #   a = request.args.to_dict()
# #
# #
# #
# # 客户端传过来的参数限制
# #
# #       如   q = request.args['q']
# #               至少有一个字符， 长度限制
# #
# #            page = request.args['page']
# #               正整数，也要有一个最大值限制
# #
# #   第三方插件验证参数
# #
# #       pip install wtforms
# #
# #           验证层
# #
# #               class SearchForm(Form):
# #
# #                   q = StringField(validators=[Length(min=1, max=30)])
# #                   page = IntegerField(validators=[NumberRange(min=1, max=99)])
# #
# #           DataRequired() 判断用户输入中是否有空格
# #
# #           调用
# #
# #               form = SearchForm(request.args)
# #               if form.validate():
# #                   q = form.q.data.strip()
# #                   page = form.page.data
# #
# #
# #
# # 减少API请求数量
# #
#
# 1
#
#
# 1
# # -*- coding:utf-8 -*-
#
# # config.py  main.py : 创建了基本应用
#
# # 安装Flask Script扩展 作用可以创建命令，在Flask应用上下文执行，这样才能对
# #   Flask对象进行修改 ， 自带了一些默认命令，可以运行服务器或者开启带应用上下文的
# #   python命令行       pip install flask-script
#
# # manage.py 导入Flask script的对象
#
# # 使用数据库 安装python安装包   pip install flask-sqlalchemy
# #   使用数据库之前 需要先设置Flask SQLAlchemy。SOLALchemy通过一个特殊的数据库
# #   URI来创建数据库连接，这个URI是一个类是与URL的字符串， 包含了SQLAlchemy建立
# #   连接说需要的所有信息
# #       databasetype+driver：//user:password@ip:port/db_name
# #       在config.py文件中将URI添加到Dev_Config中
#
# #   创建数据库模型
# #   在main.py中创建连接 ， 创建User模型
#
# #   创建表 更新manage.py 执行命令 创建表 目录中生成了database.db文件
# #       python manage.py shell
# #       db.create_all()
#
# #   CRUD 增删改查 要使用这些功能， 需要在数据库中用到一个会话session的对象
# #   新曾数据
# #       1 创建对象
# #           user = User(username='zhengyu')
# #       2 在会话中添加对象
# #           db.session.add(user)
# #       3 在会话中提交对象
# #           db.session.commit()
# #   查询数据
# #       1 获取数据库中的所有行
# #           users = User.query.all()
# #       2 打印user
# #           users
# #
# #       限制行数
# #           users = User.query.limit(10).all()
# #       排序
# #           users = User.query.order_by(User.username).all()  正向排序
# #           users = User.query.order_by(User.username.desc()).all 逆向排序
# #       只返回一行数据
# #           user = User.query.first()
# #           user.username
# #       通过主键获取一行数据，可使用query.get()
# #           user = Usr.query.get(1)
# #           user.username
# #       以上方法都是链式调用， first()和all()方法会返回结果，并终止链式调用
# #           pass
# #       pagination(分页)
# #           user = user.query.paginate(1,10)  返回来的是一个pagination对象
# #           user.items   返回这一页包含的数据对象
# #           user.page    返回这一页的页数
# #           user.pages   返回总页数
# #           user.has_prev  判断上一页是否有对象显示
# #           user.has_next  判断下一页是否有对象显示
# #     条件查询
# #       query.filter_by过滤器
# #         接收到的参数查询数据库中的字段名值对
# #           users=User.query.filter_by(username='zhengyu').all()
# #         比较大小
# #           user=User.query.filter_by(User.id>1).all()
# #         复杂的SQL查询可以转换为用SQLAlchemy的函数来表示
# #           from sqlalchemy.sql.expression import not_,or_
# #           user = User.query.filter(User.username.in_(['zhengyu']))
# #           user = User.query.filter(not_(User.password == None))
# #           user = User.query.filter(or_(not_(User.password == None),
# #                   User.id >=1))
# #   修改数据
# #       在使用first()或all()等方法返回数据之前，调用update方法可以修改已存在的数据
# #       的值
# #           User.query.filter_by(username='zhengyu').update({
# #               'password': 'lingling'
# #           })
# #           对数据模型的修改已被自动加入session中
# #           db.session.commit()
# #   删除数据
# #       user = User.query.filter_by(username='zhengyu').first()
# #       db.session.delete(user)
# #       db.session.commit()
#
# #   数据模型之间的关联
# #       数据模型之间的关联在SQLAkchemy里表现为两个或更多模型之间的连接
# #     一对多
# #       main.py中创建一对多模型关系 创建完关系，并修改了User模型之后
# #       >>> user = User.query.get(1)
# #       >>> new_post = Post('Post Title')
# #       >>> new_post.user_id = user.id
# #       >>> db.session.add(new_post)
# #       >>> db.session.commit()
# #       >>> user.posts
# #       -------------------------------------
# #       posts = db.relationship('Post', backref='user', lazy='dynamic')
# #       backref='user'
# #       backref参数则可以使我们通过 Post.user属性对User对象进行读取和修改
# #       上面的操作可以写成
# #           user = User.query.get(1)
# #       >>> second_post = Post('Second Title')
# #       >>> second_post.user = user
# #       >>> db.session.add(second_post)
# #       >>> db.session.commit()
# #       >>> user.posts
# #       -------------------------------------
# #       由于user.posts是一个列表，所以我们也可以通过吧Post对象直接添加进这个列表
# #       来自动保存它
# #       user = User.query.get(1)
# #       second_post = Post('Second Title')
# #       user.posts.append(second_post)
# #       db.session.add(user)
# #       db.session.commit()
# #       user.posts
# #       -------------------------------------
# #       由于backref选项被设置为动态方式，所以我们既可以把这个关联字段看作列表，
# #       也可以把它看作一个查询对象
# #       user.posts
# #       user.posts.order_by(Post.publish_date.desc()).all()
#
# #   创建一个模型用来实现用户评论 main.py中
#
# #   多对多 两个模型互相引用
# 1
#
# 1
# # 问题：
# #      系统输入密码 登录后出现蓝屏
# # 解决：
# #      0 crtl+alt+f4 进入字符页面 输入帐号密码登录
# #      1 重置dpkg ： sudo dpkg --configure -a
# #      2 sudo apt-get install xserver-xorg-lts-utopic
# #      3 sudo dpkg-reconfigure xserver-xorg-lts-utopic
# #      4 reboot
# 1
#
# 1
# # -*- coding:utf-8 -*-
#
# # Flask基本介绍
#
#     # Flask 以来Jinja模板引擎和 Werkezeug WSGI套件
#
#     # Flask 的目标是保持核心简单而又可扩展
#
#     # 惯例 templates 和static
#
#     # Flask 的设计原则之一是简单的任务不应当使用很多代码
#
#     # Flask 的内部使用本地线程对象
#
#     # Flask 可防御 XSS（跨站代码攻击） 和下层的Jinja2模板引擎会保护你免受这种攻击
#
#
# # Flask安装
#
#     # Flask1.0 的版本 支持python3.4 即更高的版本,python2.7和PyPy
#
#     # 当安装Flask时， 配套软件会被安装：
#
#         # Werkzeug :用于实现WSGI，应用和服务之间的标准python接口
#
#         # Jinja：用于渲染页面的模板语言
#
#         # MarkupSafe ：与Jinja共用，在渲染页面时用于避免不可信的输入，防止注入攻击
#
#         # ItsDangerous: 保证数据完整性的安全标志数据， 用于保护Flask的session cookie
#
#         # Click： 是一个命令行应用框架， 用于提供flask命令， 并允许添加自定义管理命令
#
#     # 可选依赖软件
#
#         # Blinker： 为信号提供支持
#
#         # SimpleJSON：是一个快速的JSON实现，兼容python's json模块，如果安装了这个软件，
#                      # 那么会优先使用这个软件来进行JSON操作
#
#         # python-dotenv： 当运行falsk命令时为 通过dotenv设置环境变量提供支持。
#
#         # Watchdog： 为开发服务器提供快速高效的重载
#
#     # 安装Flask
#
#         # pip install Flask
#
# 1
#
# 1
# # -*- coding:utf-8 -*-
#
# # 最小的应用
#
# # 导入了Flask类， 该类的实例将会成为我们的WSGI应用
# # from flask import Flask
#
# # 创建该类的实例。 第一个参数是应用模块或者包的名称，如果使用一个单一的模块（就像本例）
# #  那么应当使用__name__, 因为名称会根据这个模块是按应用方式使用还是作为一个模块导入而
# #  发生编号，这个参数是必须的， 这样Flask 才能知道在哪里可以找到模板和静态文件等东西
# # app = Flask(__name__)
#
# # 然后我们使用route()装饰器来告诉flask触发函数的URL
#
# # @app.route('/')
# # 函数名称被用于生成相关联的URL
# # def hello_world():
#
#     # 函数最后返回需要在用户浏览器中显示信息
#     # return 'Hello,world!'
#
# # 启动之前 用命令
#
#     # export FLASK_APP=运行的文件
#         # FLASK_app环境变量中存储的是模块的名称，
#     # python -m flask run # 启动flask
#         # 运行flask run命令就会导入这个模块，常常出现的错误
#         # 是因为拼写错误而没有真正的创建一个app对象
#     # 默认 127.0.0.1:5000
#
#     # flask run --host=0.0.0.0  让服务器可以被公开访问
#
#     # 调试模式
#
#         # 修改代码之后不用手动重启服务器
#
#             # export FLASK_ENV=development
#             # flask run
# 1
#
#
# 1
# # -*- coding:utf-8 -*-
#
# # from flask import Flask
# #
# # app = Flask(__name__)
# #
# # @app.route('/')
# # def index():
# #     return 'index'
# #
# # @app.route('/hello')
# # def hello():
# #     return 'hello'
# 1
#
# 1
# # -*- coding:utf-8 -*-
#
# # from flask import Flask
# #
# # app = Flask(__name__)
# #
# # # 通过吧URL的一部分标记<xxx> 就可以在URL中添加变量
# # #  标记的部分会作为关键字参数传递给函数
# # @app.route('/user/<args>')
# # def t_args(args):
# #
# #     return 'hello, %s'%args
# #
# # # int 加上了一个转换器，为变量指定规则
# # @app.route('/post/<int:age>')
# # def t_int_args(age):
# #
# #     return 'your age is %d'%age
# #
# # # path 类是string 但包含斜杠
# # @app.route('/path/<path:addr>')
# # def t_path_args(addr):
# #
# #     return addr
#
# # 转换器类型还有
#     # <float:xxxx> 接受正浮点数
#     # <uuid:xxx>  接受UUID字符串
# 1
#
#
# 1
# # -*- coding:utf-8 -*-
# #
# # from flask import Flask
# #
# # app = Flask(__name__)
# #
# # # url尾部带/
# # # 尾部带斜杠是中规中矩，访问一个没有带斜杠的url时，Flask会自动进行重定向，帮你在尾部加一个/
# # @app.route('/projects/')
# # def projects():
# #
# #     return 'projects'
# #
# # # url尾部不带/
# # # 访问这个url，若尾部添加了一个/， 则访问的时候会出错。这样可以保持URL唯一， 并帮助
# # #  搜索引擎避免重复索引同一页面
# # @app.route('/about')
# # def about():
# #     return 'about'
# 1
#
#
# 1
# # -*- coding:utf-8 -*-
#
# # url_for() 函数用于构建指定函数的URL。它把函数名称作为第一个参数，它可以接受任意个关键字参数
#  # 每个关键字参数对应url中的变量。未知变量将添加将添加URL中作为查询参数
#
# # 使用 反转函数url_for()动态构建的优点
#     # 1反转通常比硬编码URL的描述性更好
#     # 2可以只在一个地方改变URL，而不用到处乱找
#     # 3URL创建会为你处理特殊字符的转义和Unicode数据，比较直观
#     # 4生成的路径总是绝对路径，可以编码相对路径产生副作用
#     # 5如果应用是放在URL跟路径之外的地方（如在/myapplication,不再/中），url_for()
#         # 会为你妥善处理
#
# # from flask import Flask, url_for
# #
# # app = Flask(__name__)
# #
# # @app.route('/')
# # def index():
# #     return 'index'
# #
# # @app.route('/login')
# # def login():
# #     return 'login'
# #
# # @app.route('/user/<username>')
# # def profile(username):
# #     return '{}\'s profile'.format(username)
# #
# # # test_request_context()告诉Flask正在处理一个请求
# # with app.test_request_context():
# #
# #     print(url_for('index'))
# #     print(url_for('login'))
# #     print(url_for('login', next='/'))
# #     print(url_for('profile', username='Jhon Doe'))
# 1
#
# 1
# # -*- coding:utf-8 -*-
#
# # from flask import Flask, request
# #
# # app = Flask(__name__)
# #
# # @app.route('/')
# # def index():
# #     return 'index'
# #
# # # flask http方法 默认get请求
# # # 可以使用route()装饰器的methods参数来处理不同的HTTP方法
# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         return 'post'
# #     else:
# #         return 'other method'
# 1
#
# 1
# # -*- coding:utf-8 -*-
#
#
# # 静态文件
# # css javascript 开发过程中静态文件位置为 /static
# # 使用特定的‘断电就可以生成想对应的URL’
#     # url_for('static', filename='xxx.css')
# 1
#
# 1
# # -*- coding:utf-8 -*-
#
# # 渲染模板
# # 使用render_template()方法可以渲染模板， 提供模板名和模板参数即可
# # Flask会在templates文件夹内寻找模板
# # 在模板内部可以和访问get_flashed_messages()函数一样访问request, session和g对象
# # from flask import Flask, render_template
# #
# # app = Flask(__name__)
# #
# # @app.route('/hello/<name>')
# # def index(name=None):
# #
# #     return render_template('index09.html', name=name)
# 1
#
# 1
# # -*- coding:utf-8 -*-
#
# # flask自动转义
#
# # flask中自动转移是默认开启的
#
# # from flask import Flask, render_template, Markup
# #
# # app = Flask(__name__)
# #
# # @app.route('/')
# # def index():
# #
# #     # 用Markup类把它标记为安全
# #
# #     # 转义的第一种方法
# #     name1 = Markup('<html>hello %s >')%'<blink> '
# #     print(name1)
# #
# #     # 转义的第二种方法
# #
# #     name2 = Markup.escape('<blink> ')
# #     print(name2)
# #     return render_template('index10.html', name1=name1, name2=name2)
# 1
#
#
# 1
# # -*- coding:utf-8 -*-
#
# # 在Flask中全局对象request来提供请求信息
#
# # 这个对象是全局的，怎么还能保持线程安全 答案就是本地环境
#     # 某些对象在Flask中的全局对象，不是通常意义的全局对象，实际上是
#     # 特点个环境下本地对象的代理
#     # 如现在处于处理线程的环境中。一个请求进来了，服务器绝对生成一个新线程。
#     # 当Flask开始其每部请求处理时候会把当前线程作为活动环境，并把当前应用和WSGI
#     # 绑定到这个环境（线程），使得一个应用在不中断的情况下调用另一个应用
#     # 这个只有在单元测试的时候才有用，简单的单元测试解决方案test_request_context
#     # 环境管理器。通过使用with语句可以绑定一个测试请求，以便于交互
#
# # from flask import request, Flask
# #
# # app = Flask(__name__)
# #
# # with app.test_request_context('/hello', method='POST'):
# #
# #     assert request.path == '/hello'
# #     assert request.method == 'POST'
#
# #>>> assert 1==1
# #>>> assert 1==0
# #Traceback (most recent call last):
# #  File "<pyshell#1>", line 1, in <module>
# #    assert 1==0
# #AssertionError
# 1
#
#
# 1
# # -*- coding:utf-8 -*-
#
# # 请求对象
#
# # from flask import Flask, request, render_template,
# # app = Flask(__name__)
# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     error = None
# #     if request.method == 'POST':
# #         # 当form属性中不存在这个键的时候，会引发一个KeyError
# #         if valid_login(request.form['username'], request.form['password']):
# #             return log_the_user_in(request.form['username'])
# #         else:
# #             error = 'Invalid username/password'
# #     return render_template('login12.html', error=error)
# # 要操作URL(如？key=value)中提价的参数
#     # serchword = request.args.get('key', '')
#     # 建议使用get或通过不做keyerror来访问Url参数
#
# 1
#
# 1
# # -*- coding:utf-8 -*-
#
# # 文件上传
#
# # Flask处理文件上传，确保一点 HTML表单中设置 enctype="multipart/form-data" 属性
#
# # 以上传的文件被储存在内存或文件系统的临时位置。可以通过请求对象files属性来访问上传的文件
# #   每个上传的文件都存储在这个字典型属性中，基本和python file对象一样，另外多个出一个用于
# #   把上传文件保存到服务器的文件系统中的save()方法
#
# # from flask import Flask, request, render_template
# #
# # app = Flask(__name__)
# #
# # @app.route('/upload', methods=['POST', 'GET'])
# # def upload_file():
# #     if request.method == 'POST':
# #         f = request.files['the_file']
# #         f.save('/static/upload/upload.txt')
# #
# # 若想把客户端的文件名作为服务器上的文件名，可以通过Werkzeug提供secure_filename()函数
# # from werkzeug.utils import secure_filename
# # @app.route('/upload', methods=['POST', 'GET'])
# # def upload_file():
# #     if request.method == 'POST':
# #         f = request.files['the_file']
# #         f.save('/static/upload/' + secure_filename(f.filename))
# #
# #
# #
# # @app.route('/upto')
# # def upto():
# #     return render_template('upload13.html')
# 1
#
# 1
# # -*- coding:utf-8 -*-
#
# # Cookies
#
# #   访问cookies 可使用cookies属性
# #       请求对象的cookies属性是一个包含了客户端传输的所有cookies的字典，
# #       Flask中，如果使用会话，那么就不要直接使用cookies，因为会话比较安全一些
# #   设置cookies 可使用set_cookie方法
#
# # from flask import Flask, request, make_response
# #
# # app = Flask(__name__)
# #
# # @app.route('/read')
# # def read_cookie():
# #     # 读取cookies
# #     username = request.cookies.get('username')
# #
# # @app.route('/set')
# # def set_cookie():
# #     # 存储cookies
# #     # 如果想显示的转换，呢码可以是用make_response
# #     resp = make_response('index14.html')
# #
# #     resp.set_cookie('username', 'fuck')
# #
# #     return resp
# 1
#
#
# 1
#
# # -*- coding:utf-8 -*-
#
# # 重定向和错误
#
# #   使用redirect()函数可以重定向，使用abort()可以更早退出请求，并返回错误代码
#
# # from flask import abort, redirect, url_for, Flask
# #
# # app = Flask(__name__)
# #
# #
# # @app.route('/')
# # def index():
# #     return redirect(url_for('login'))
# #
# #
# # @app.route('/login')
# # def login():
# #     abort(401)
# 1
#
#
# 1
# # -*- coding:utf-8 -*-
#
# # 自定义出错页面
#
# #   使用 errorhandler()装饰器定制出错页面
#
# # from flask import render_template, Flask
# #
# # app = Flask(__name__)
# #
# # @app.errorhandler(404)
# # def page_not_found(error):
# #
# #     # 注意render_template 后面的404,这表示页面对就的出错代码是404
# #     return render_template('page_not_found16.html'), 404
# 1
#
#
#
# 1
# # -*- coding:utf-8 -*-
#
# # 关于响应
#
# #   试图函数的返回值会自动转换为一个响应对象。
# #   如果返回值是一个字符串。那么会被换为：
# #       一个包含作为响应体的字符串，
# #       一个200 ok出错代码
# #       一个text/html类型的响应对象
#
# #   转换规则为：
# #       1 如果试图返回的是一个响应对象，那么就直接返回它
# #       2 如果返回的是一个字符串，那么根据这个字符串和缺省值生成一个用于返回的对象
# #       3 如果返回的是一个元祖， 那么元祖中的项目可以提供额外的信息
# #         元祖中必须至少包含一个项目，且项目应当有(response, status, headers)
# #         或者(response,headers)组成，status的值会重载状态代码，headers
# #         是由一个由额外头部值组成的列表或字典
# #       4 如果以上都不是， 那么Flask会假定返回值是一个有效的WSGI应用并把它
# #         转换为一个响应对象。
#
# # 如果想要在视图内部掌控响应对象的结果，可以用make_response()
#
# #   使用make_response()包囊返回表达式，获得响应对象，并对该对象进行修改，饭后在返回
#
# # from flask import Flask, make_response, render_template
# #
# # app = Flask(__name__)
# #
# # @app.errorhandler(404)
# # def not_found(error):
# #     resp = make_response(render_template('error.html'), 404)
# #     resp.headers['X-something'] = 'A value'
# #     return resp
# 1
#
#
# 1
# # -*- coding:utf-8 -*-
#
# # 会话 session
#
# #   除了请求对象之外还有一种称为session的对象，允许你在不同请求之间存储信息。这个对象相当于用
# #   密钥签名加密的cookie，及用户可以查看你的cookie，但是如果没有密钥就无法修改它
#
# #   使用会话之前必须设置一个密钥
# # from flask import Flask, session, redirect, url_for, escape, request
# #
# # app = Flask(__name__)
# #
# # app.secret_key = b'sdfsgsgag'
# #
# # @app.route('/')
# # def index():
# #     if 'username' in session:
# #                                    # escape用来转义的
# #         return 'logged in as %s' % escape(session['username'])
# #     return 'you are not logged in '
# #
# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         session['username'] = request.form['username']
# #         return redirect(url_for('index'))
# #     return '''
# #             <form method="post">
# #                 <input type="text" name="username"><br>
# #                 <input type="submit" value="login">
# #             </form>
# #             '''
# #
# # @app.route('/logout')
# # def logout():
# #     session.pop('username', None)
# #     return redirect(url_for('index'))
# 1
#
# 1
# # -*- coding:utf-8 -*-
#
# # 生成一个好的密钥
#
# #   生成随机数的关键在于一个好的随机种子，因此一个好的密钥应当有足够的随机型
# #   使用下面命令可以快捷的为Flask.secret_key生成值
# #       python -c 'import os;print(os.urandom(16))'
#
# # 基于cookie的会话的说明：
#
# #   flask 会取出会话对象中的值，把值序列化后储存到cookie中。在打开cookie的清空下，
# #   如果需要查找某个值，但是这个值在请求中没有持续存储的化，那么不会得到一个清晰的出错信息
# #   除了缺省的客户端会话之外，还有许多Flask扩展支持服务端会话
# 1
#
# 1
# # 消息闪现
#
# #   消息闪现系统的基本工作原理是在请求结束 记录一个消息，提供且只提供给下一个请求使用
# #   通常通过一个布局模板来展现闪现的消息
# #   flash（）用于闪现一个消息。在模板中，使用get_flashed_messages()来操作消息
# 1
#
#
# 1
# # -*- coding:utf-8 -*-
#
# # 集成WSGI中间件
#
# #   如果想要在应用中添加一个WSGI中间件，可以包装内部的WSGI应用。假设为了解决lighttpd的错误
# #   要使用一个来自Werkzeug包的中间件，可以这样做：
# #from werkzeug.contrib.fixers import LighttpdCGIRootFix
# #app.wsgi_app = LighttpdCGIRootFix(app.wsgi_app)
# 1
#
# 1
# # -*- coding:utf-8 -*-
#
# # 项目结构
# #   项目基本结构
# #       flasky
# #           app/
# #               tempaltes/
# #               static/
# #               main/
# #                   __init__.py
# #                   errors.py
# #                   forms.py
# #                   views.py
# #               __init__.py
# #               email.py
# #               models.py
# #           migrations/
# #           tests/
# #               __init__.py
# #               test*.py
# #           venv/
# #           requirements.txt
# #           config.py
# #
# #        这种结构有4个顶级文件夹
# #
# #           app：Flask程序一般都保存在名为app保重
# #           migrations:包含数据库迁移脚本
# #           tests：单元测试编写
# #           venv：包含python虚拟环境
# #           requirements.txt：列出了所有依赖包，便于在其他电脑中重新生成相同的
# #                               虚拟环境
# #           config.py:存储配置
# #           manage.py用于启动程序以及其他的程序任务
# #
# #   配置选项
# #
# #       config.py 程序的配置
# #
# #             import os
# #
# #             BASEDIR = os.path.abspath(os.path.dirname(__file__))
# #
# #             class Config:
# #                 # or 'fsfasfaaaa'
# #                 SECRET_KEY = os.environ.get('SECRET_KEY')
# #                 SQLALCHEMY_COMMIT_ON_TEARDOWN = True
# #                 FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
# #                 FLASKY_MAIL_SENDER = '174927390@qq.com'
# #                 FLASKY_ADMIN = '174927390@qq.com'
# #
# #                 @staticmethod
# #                 def init_app(app):
# #                     pass
# #
# #             class Development_config(Config):
# #                 DEBUG = True
# #                 MAIL_SERVER = 'smtp.qq.com'
# #                 MAIL_PORT = 465
# #                 MAIL_USE_SSL = True
# #                 MAIL_USERNAME = '174927390'
# #                 MAIL_PASSWORD = 'padundmltvrlcbdc'
# #
# #                 # or os.environ.get('DEV_DATABASE_URL')
# #                 SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASEDIR, 'data-dev.sqlite')
# #
# #             class Testing_config(Config):
# #                 TESTING = True
# #
# #                 # or os.environ.get('TEST_DATABASE_URL')
# #                 SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'data-test.sqlite')
# #
# #             class Production_config(Config):
# #
# #                 # or os.environ.get('DATABASE_URL')
# #                 SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'data.sqlite')
# #
# #             config = {
# #
# #                 'development': Development_config,
# #                 'testing': Testing_config,
# #                 'production': Production_config,
# #
# #                 'default': Development_config,
# #             }
# #
# #           基类Config中包含通用配置，子类分别定义专用的配置。如果需要，还可以
# #           添加其他配置类
# #
# #           为了让配置方式更灵活且安全，某些配置可以从环境变量中导入。如SECRET_KEY
# #           的值，可以在环境中设定但系统也提供了一个默认值，以防环境中没有定义
# #
# #           在3个子类中，SQLALCHEMY_DATABASE_URI变量都被指定了不同的值。这样程序
# #           就可在不同的配置环境中运行，每个环境都使用不同的数据库
# #
# #           配置类可以定义init_app()类方法，其参数是程序实例。在这个方法中，可以
# #           执行对当前环境配置的初始化。现在基类Config中的init_app()方法为空
# #
# #           在这个配置脚本末尾，config字典中注册了不同的配置环境，而且还注册了一个默认
# #           的配置
# #
# #       程序包
# #
# #           程序包用来保存程序的所有代码， 模板和静态文件。我们可以把这个包直接称为
# #           app(应用)，如果有需求，也可使用的一个程序专用名字templates和static
# #           文件夹是程序包的一部分，因此这两个文件夹被移到了app中。数据库模型和电子
# #           邮件支持函数也被移到了这个包中
# #
# #           使用程序工厂函数
# #
# #               在单个文件中开发程序很方便，但有个很大的缺点，因为程序在全局作用域中
# #               创建,所以无法动态修改配置。运行脚本时，程序实例已经创建，再修改配置
# #               为时已晚。这一点对单元测试尤其重要，因为有时为了提高测试覆盖度，必须
# #               在不同的配置环境中运行程序。
# #
# #               这个问题的解决方法是延迟创建程序实例，把创建过程移到可显示调用的工厂
# #               函数中。这种方法不尽可以给脚本留出配置程序时间，还能够创建多个程序
# #               实例，这些实例在测试中非常有用，程序的工厂函数在app包的构造文件中定义
# #
# #               构造文件导入了大多数正在使用的Flask扩展。由于尚未初始化所需的程序
# #               实例，所以没有初始化扩展，创建扩展类没有向构造函数传入参数，
# #               create_app()函数就是程序的工厂函数，接受一个参数，是程序使用的配置名
# #               。配置类在config.py文件中定义，其中保存的配置可以使用
# #               Flask app.config配置对象提供的from_object()方法直接导入程序。
# #               至于配置对象，则可以通过名字从config字典中选择。程序创建并配置好后
# #               就能初始化扩展了。在之前创建的扩展对象上调用init_app()可以完成
# #               初始化过程
# #
# #           app/__init__.py程序包的构造文件
# #
# #                 from flask import Flask
# #                 from flask_bootstrap import Bootstrap
# #                 from flask_mail import Mail
# #                 from flask_sqlalchemy import SQLAlchemy
# #                 from flask_moment import Moment
# #                 from flask_web_len_1.config import config
# #
# #                 bootstrap = Bootstrap()
# #                 mail = Mail()
# #                 moment = Moment()
# #                 db = SQLAlchemy()
# #
# #
# #                 def create_app(config_name):
# #                     app = Flask(__name__)
# #                     app.config.from_object(config[config_name])
# #                     config[config_name].init_app(app)
# #
# #                     bootstrap.init_app(app)
# #                     mail.init_app(app)
# #                     moment.init_app(app)
# #                     db.init_app(app)
# #
# #                     附加路由和自定义错误的页面
# #
# #                     return app
# #
# #               工厂函数返回创建的程序实例，不过要注意，现在工厂函数创建的程序还
# #               不完整，因为没有路由和自定义错误页面处理程序
# #
# #           在蓝本中实现程序功能
# #
# #               转换程序工厂函数的操作让定义路由变的更复杂了。在但脚本程序中，程序
# #               实例存在于全局作用域中，路由可以直接使用app.route修饰器。但现在
# #               程序在运行时创建，只有调用create_app()之后才能使用app.route
# #               修饰器，这时候定义路由就太晚了。和路由一样，自定义的错误页面处理
# #               程序也面临相同的困难，因为错误页面处理程序使用app.errorhandler
# #               修饰器定义
# #
# #               性好Flask使用蓝本提供了更好的解决方法。蓝本和程序类似，也可以定义
# #               路由。不同的是，在蓝本中定义的路由出于休眠状态，直到蓝本注册到程序上
# #               后， 路由猜真正成为程序的一部分。使用位于全局作用域的蓝本时，定义
# #               路由方法几乎和单脚本程序一样
# #
# #               和程序一样，蓝本可以在单个文件中定义，也可使用更结构化的方式在多个
# #               模块中创建。为了获得最大的灵活性，程序包中创建了一个子包，用于保存
# #               蓝本
# #
# #               app/main/__init__.py中 创建蓝本
# #
# #                   from flask import Blueprint
# #
# #                   main = Blueprint('main', __name__)
# #
# #                   from . import views, errors
# #
# #                   通过实例化一个Blueprint类对象可以创建蓝本。这个构造函数有
# #                   两个必须指定的参数，蓝本的名字和码本所在的包或模块。和程序
# #                   一样，大多数情况下第二个参数使用python的__name__变量即可
# #
# #                   程序的路由保存在包里的app/main/views.py模块中，而错误处理
# #                   程序保存在app/main/errors.py模块中。导入这两个模块就能把
# #                   路由和错误处理程序和蓝本关联起来。注意，这些模块在app/main/
# #                   __ini__.py脚本的末尾导入，这是为了避免循环导入依赖，因为在
# #                   views.py和errors.py中还有导入蓝本main
# #
# #               蓝本在工厂函数create_app()中注册到程序上
# #               app/__init__.py中 注册蓝本
# #
# #                   from .main import main as main_blueprint
# #                   app.resister_blueprint(main_blueprint)
# #
# #               app/main/errors.py 蓝本中的错误处理程序
# #
# #                   from flask import render_template
# #                   from . import main
# #
# #                   @main.app_errorhandler(404)
# #                   def page_not_found(e):
# #                       return render_template('404.html'), 404
# #
# #                   @main.app_errorhandler(500)
# #                   def inernal_server_error(e):
# #                       return render_template('500.html'), 500
# #
# #                   在蓝本中编写错误处理程序稍有不同，如果使用errorhandler修饰器
# #                   那么只有蓝本中的错误才能触发处理程序。要想注册程序全局的错误
# #                   处理程序，必须使用app_errorhandler
# #
# #               app/main/view.py 蓝本中定义的程序路由
# #
# #                   @main.route('/', methods=['GET', 'POST'])
# #                   def index():
# #                       ....
# #                       return redirect(url_for('.index'))
# #                       ...
# #
# #                   在蓝本中编写函数主要有两点不同：第一和前面的作物处理程序一样，
# #                   路由修饰器有蓝本提供;第二，url_for()函数的用法不同。你可能
# #                   还记得，url_for()函数的dingier参数是路由的端点名，在程序的
# #                   路由中，默认为试图函数的名字。
# #
# #                   在蓝本中就不一样了，Flask会为蓝本中的全部端点加上一个命名
# #                   空间，这样就可以在不同的蓝本中使用相同的端点名定义函数试图，
# #                   而不会产生冲突。命名空间就是蓝本的名字（Blueprint构造函数的
# #                   第一个参数）， 所以试图函数index()注册的端点名是main.index,
# #                   而URL使用url_for (‘main.index’)获取
# #
# #                   url_for()函数还支持一种简写的端点形式，在蓝本中可以省略蓝本名
# #                   如url_for('.index').在这种写法中，命名空间是但前请求所在的
# #                   蓝本。这就以为在同一蓝本中的重定向可以使用简写形式，但跨蓝本的
# #                   重定向必须使用带有命名空间的断电名
# #
# #           启动脚本
# #
# #               manage.py文件中
# #
# #                   import os
# #                    from app import create_app, db
# #                    from flask_script import Manager, Shell
# #                    from flask_migrate import Migrate, MigrateCommand
# #
# #                    app = create_app(os.getenv('FLASK_CONFIG'))
# #                    manager = Manager(app)
# #                    migrate = Migrate(app, db)
# #
# #                    def make_shell_context():
# #                        return dict(app=app, db=db)
# #
# #                    manager.add_command("shell", Shell(make_context=make_shell_context))
# #                    manager.add_command('db', MigrateCommand)
# #
# #                    if __name__ == '__main__':
# #                        manager.run()
# #
# #                   这个脚本先创建程序。如果已经定义了环境变量FLASK_CONFIG,则从
# #                   中读取配置名，否则使用默认配置，然后初始化Flask-Script，
# #                   Flask-Migrate和为python shell定义的上下文
# #
# #           需求文件
# #
# #               程序包中必须包含一个requirements.txt文件，用于记录所有依赖包及
# #               精确的版本号。如果在另一台电脑上重新生成习俗虚拟环境
# #               使用pip命令自动生成这个文件
# #
# #                   pip freeze > requirements.txt
# #
# #               安装或升级包后，最好更新这个文件
# #
# #               在新的虚拟环境 自动重装文件中的软件
# #
# #                   pip install -r requirements.txt
# #
# #           单元测试
# #               ????
# #
# #           创建数据库
# #
# #               重组后的程序和单脚本版本使用不同的数据库
# #
# #               首选从环境变量中读取数据库URL，荣是还提供了一个默认的SQLite数据库
# #               备用。3中配置环境中的环境变量名和SQLite数据库文件名都不一样。
# #
# #               不关从哪里获取数据库URL，都要在新数据库中创建数据表。如果使用Flask
# #               -Migrate跟踪迁移，可使用如下命令创建数据库表或者升级到最新的修订版本
# #
# #                   python manage.py db upgrade
# 1
#
#
# 1
# # -*- coding:utf-8 -*-
#
# #   虚拟环境安装
# #       virtualenv --version  检查是否安装虚拟环境
# #       suso apt-get install python-virtualenv  安装虚拟环境
# #   flask安装
# #       pip install flask
#
#
#
# #   程序基本结构
# #       初始化
# #           所有Flask程序都必须创建一个程序实例。web服务器使用一种名为Web服务网关
# #           接口WSGI的协议，把接收自客户端的所有请求都转交给这个对象处理。
# #           app = Flask(__name__) flask类的构造函数只有一个必须指定的参数，
# #           即程序主模块或包的名字， name这个参数的作用是 Flask用这个参数决定程序
# #           的根目录，以便稍后能够找到相对于程序根目录的资源文件位置
#
#
#
# #   路由和试图函数
# #       处理URL和函数之间的关系的程序称为路由
# #       定义路由的最简便方式， 是使用程序实例提供的app.route修饰器，把修饰的函数
# #       注册为路由
# #       修饰器的惯常用法是使用修饰器把函数注册为事件的处理程序
# #        @app.route('/')
# #        def index():   试图函数
# #           return 'haha' 函数返回值称为响应，是客户端接收到的内容 若客户端是
# #                           web浏览器，响应就是显示给用户查看的文档
# #
# #       route修饰器中的特殊句法
# #           @app.route('/user/<name>')
# #           def user(name):
# #               return 'hello %s' % name
# #       尖括号中的内容就是动态比分，flask将动态部分作为参数传入函数
# #       动态部分默认使用字符串 也可以定义其他类型<int:name> ,float,path等
# #       但不把斜线视作分隔符，而将其当作动态片段的一部分
# #
#
#
#
# #   启动服务器
# #       程序实实例用run方法启动Flask集成的开发Web服务器
# #           if __name__ == '__main__':
# #               app.run(debug=True)
# #           __name__ == '__main__', 确保直接执行这个个脚本时才启动，若这个
# #           脚本由其他脚本引入，程序假定父级脚本会启动不同的服务器，因此不会执行
# #           app.run()
# #
# #       一个完整的程序
# #           hello.py
# #
# #       一个完整的程序的增强版
# #           hello.py
#
#
#
# #   请求-响应循环
# #
# #       程序和请求上下文
# #           Flask从客户端收到请求时， 要让试图函数能访问一些对象，这样猜能处理请求
# #           请求对象就是一个很好的例子，它封装了客户端发送的HTTP请求
# #
# #           要让试图函数能够访问请求对象，一个显而易见的方式是将其作为参数传入试图
# #           函数，不过这会导致程序中的每个试图函数都增加一个参数，为了避免这个情况
# #           flask使用 上下文 临时吧某些对象变为全局可访问：
# #               from flask import request
# #               @app.route('/')
# #               def index():
# #                   user_agent = request.headers.get('User-Agent')
# #                   return 'you browser is %s'%user_agent
# #               这个试图函数中把request当作全局变量。事实上，request不可能是
# #               全局变量，在多线程服务器中，多个线程同时处理不同客户端发送的不
# #               同请求时，每个线程看到的request对象必然不同，flask使用上下文
# #               让特定的变量在一个线程中全局访问，于此同时不会干扰其他线程
# #
# #           flask中有两种上下文：程序上下文和请求上下文
# #           变量名        上下文         说明
# #           current_app 程序上下文    当前激活程序的程序实例
# #           g           程序上下文    处理请求时用作临时存储对象。每次请求都会重设这个变量
# #           request     请求上下文    请求对象，封装了客户端发出的HTTP请求中的内容
# #           session     请求上下文    用于存储请求之间需要“记住”的值的词典
# #               Flask在分发请求之前激活程序和请求上下文，请求处理完成后再将其删除。
# #               程序上下文被推送后， 就可以在线程中使用current_app和g变量。类似的
# #               请求上下文被推送后，就可以使用request和session变量。如果使用这些
# #               变量时我们没有激活程序上下文或请求上下文，就会导致错误
# #                In [1]: from hello import app
# #                In [2]: from flask import current_app
# #                In [z]: current_app.name
# #                Out[z]: fsdlafjlsxxxxxxxxxxxx 会出错
# #                In [3]: app_ctx = app.app_context()
# #                In [4]: app_cux.push()
# #                In [5]: app_ctx.push()
# #                In [6]: current_app.name
# #                Out[6]: 'hello'
# #                In [7]: app_ctx.pop()
# #                   没激活程序上下文之前调用current_app.name会导致错误，
# #                   推送完上下文之后就可以调用了，app.app_context()可获得
# #                   一个程序上下文
# #
# #       请求调度
# #           程序接收客户端发来的请求时， 要找到处理该请求的试图函数。为了完成这个
# #           任务，Flask会在程序的URL映射中查找请求的URL。URL映射是URL和视图函数
# #           之间的对应关系,Flask使用app.route修饰器或者非修饰器形式的
# #           app.add)url_rule()生成映射
# #
# #           查看Flask程序中的URL映射
# #             In [1]: from hello import app
# #             In [2]: app.url_map
# #             Out[2]:
# #                Map([<Rule '/' (HEAD, OPTIONS, GET) -> index>,
# #               <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
# #               <Rule '/user/<name>' (HEAD, OPTIONS, GET) -> user>])
# #             /和/user/<name>路由在程序中使用app.route修饰器定义
# #             /static/<filename>路由是Flask添加的特殊路由，用于访问静态文件
# #             URL映射中的HEAD，OPTIONS，GET是请求方法，由路由进行处理。Flask
# #             为每个路由都指定了请求方法，这样不同的请求方法发送到相同的URL上时
# #             会使用不同的试图函数进行处理，HEAD和OPTIONS方法由Flask自动处理
# #             在这个程序中 URL映射中的3个路由都使用GET方法
# #
# #       请求钩子
# #           有时在处理请求之前或之后执行代码会很有用。如，在请求开始时，可能需要
# #           创建数据库连接或者认证发起请求的用户。为了避免在每个视图函数中都使用
# #           重复的代码Flask提供了注册通用函数的功能， 注册的函数可在请求被分发到
# #           试图函数之前或之后调用，请求钩子使用装饰器实现。Flask支持4中钩子
# #               before_first_request:
# #                   注册一个函数，在处理第一个请求之前运行
# #               before_request:
# #                   注册一个函数，在每次请求之前运行
# #               after_request:
# #                   注册一个函数，如果没有未处理的异常抛出，再没次请求之后运行
# #               teardown_request
# #                   注册一个函数， 即使有未出里的异常抛出，也在每次请求之后运行
# #           在请求钩子函数和试图函数之间共享数据一般使用上下文全局变量g。如
# #           before_request处理程序可以从数据库中加载已登录用户，并将其保存到
# #           g.user中。随后出现视图函数时在使用g.user获取用户
# #
# #       响应
# #           Flask调用数图函数后，会将其返回值作为响应的内容。大多数情况下，响应
# #           是一个简单的字符串，作为HTML页面会送客户端
# #           但HTTP协议需要的不仅是作为请求响应的字符串。HTTP响应中一个很重要的
# #           部分是 状态码，Flask默认设为200,这个代码表明请求已经被成功处理
# #           如果视图函数返回的响应需要使用不同的状态码，那么可以把数字代码作为
# #           第二个返回值，添加到响应文本之后
# #               @app.route('/')
# #               def index():
# #                   return '<h1>bad request</h1>', 400
# #           视图函数返回的响应还可以接受第三个参数，这是一个由首部(header)组成
# #           的字典，可以添加到HTTP响应中。不推荐
# #
# #           如果不想用 return 'xxx', 200, {'a':'b'}, Flask试图函数还可以返回
# #           Response对象。make_response()函数可以代替return接受参数，并返回一个
# #           Response对象，有时候我们需要在视图函数中进行这种转换，然后在响应对象上
# #           调用各种方法，进一步设置响应。设置cookie：
# #               from flask import make_response
# #               @app.route('/')
# #               def index():
# #                   response = make_response('haha')
# #                   response.set_cookie('a', '12')
# #                   return response
# #
# #           有一种名为 重定向 特殊响应类型，重定向经常使用302状态码表示，指向的地址
# #           有location首部提供。重定向可以使用3个值的形式的返回值生成，也可在
# #           response对象中设定，由于使用频繁，flask提供了redirect()辅助函数
# #               from flask import redirect
# #               @app.route('/')
# #               def index():
# #                   return redirect('http://xxx.com')
# #
# #           还有一种特殊的响应由abort函数生成，用于处理错误。
# #               如果URL中动态参数id对应的用户不存在，就返回状态码404
# #               from flask import abort
# #               @app.route('/user/<id>')
# #               def get_user(id):
# #                   user = load_user(id)
# #                   if not user:
# #                       abort(404)
# #                   return 'hello,%s' user.name
# #               abort 不会吧控制权交还给调用它的函数，而是抛出异常把控制权交给
# #               web服务器
#
#
#
# #   Flask扩展
# #       使用Flask-Script支持命令行选项
# #           Flask的开发web服务器支持很多启动设置选项，但只能在脚本中作为参数传给
# #           app.run()函数。这不方便，传递设置选项的理想方式是使用命令行参数
# #           flask-script是一个flask扩展，为flask程序添加了一个命令行解析器，
# #           flask-script自带了一组常用选项，而且还支持自定义命令
# #
# #       安装
# #           pip install flask-script
# #
# #       修改hello文件代码
# #           from flask.ext.script import Manager
# #           manager = Manager(app)
# #               ....
# #           if __name__ == '__main__':
# #               manager.run()
# #           专为flask开发的扩展都暴漏在 flask.ext命名空间下，flask-script输出
# #           了一个名为Manager的类，可从flask.ext.script中导入
# #           ***python2.7*** flask-script-2.0.6***不支持 flask.ext.script
# #           ***导入， 直接用 from flask_script import Manager*****
# #           这个扩展的初始化方法也适用于其他很多扩展：把程序实例作为参数传给构造
# #           函数，初始化主类的实例。创建的对象可以在各个扩展中使用。服务器由
# #           manager.run()启动，启动后就能解析命令行了
# #
# #       运行
# #           python hello会出现
# #               positional arguments:
# #               {shell,runserver}
# #                                在flask应用上下文中运行 python shell
# #               shell            Runs a Python shell inside Flask
# #                                 application context.
# #                                运行flask可发服务器：app.run()
# #               runserver        Runs the Flask development server
# #                                 i.e. app.run()
# #
# #               optional arguments:
# #                                       显示帮助信息并退出
# #                   -?, --help         show this help message and exit
# #
# #           运行 python hello.py runserver 出现
# #
# #               usage: hello.py runserver [-?] [-h HOST]
# #                         [-p PORT] [--threaded][--processes PROCESSES]
# #                         [--passthrough-errors] [-d] [-D] [-r] [-R]
# #                         [--ssl-crt SSL_CRT] [--ssl-key SSL_KEY]
# #
# #               Runs the Flask development server i.e. app.run()
# #
# #               optional arguments:
# #                   -?, --help    show this help message and exit
# #                                 -h HOST, --host HOST
# #                                 -p PORT, --port PORT
# #                                 --threaded
# #                                 --processes PROCESSES
# #                                 --passthrough-errors
# #                                 -d, --debug           enable the
# #                                                       Werkzeug debugger
# #                                                       (DO NOT use in
# #                                                        production code)
# #                                 -D, --no-debug        disable the
# #                                                       Werkzeug debugger
# #                                 -r, --reload          monitor Python
# #                                                       files for changes
# #                                                       (not 100% safe for
# #                                                       production use)
# #                                 -R, --no-reload       do not monitor
# #                                                       Python files for
# #                                                       changes
# #                                 --ssl-crt SSL_CRT     Path to ssl
# #                                                       certificate
# #                                 --ssl-key SSL_KEY     Path to ssl key
# #               --host参数，它告诉web服务器在哪个网络接口上监听来自客户端的连接
# #               默认情况下，Flask开发web服务监听localhost上的连接，只接受来自
# #               服务器所在计算机发起的连接。下面的命令让web服务器监听公共网络接口
# #               上的连接，允许其他计算机连接服务器
# #                   python hello.py runserver --host 0.0.0.0
# #
# #   模板
# #       业务逻辑：
# #           用户在表单中输入电子邮件地址和密码，然后点击提交按钮。服务器接受到包含用户
# #           输入的数据请求，然后Flask把请求分发到处理注册请求的视图函数。
# #       表现逻辑：
# #           处理函数需要反问数据库，添加新用户，然后生成响应回送浏览器。
# #       把变现逻辑移动到模板中能够提升程序的可维护性
# #
# #       渲染：
# #           模板shingle包含响应文本的文件，其中包含用占位变量表示动态部分，其具体值
# #           只在请求的上下文中才能知道。使用真实值替换变量，再返回最终得到响应字符串
# #           这一过程称为渲染。为了渲染模板，flask使用了一个名为jinja2的强大模板引擎
# #
# #       jinjia2模板引擎
# #           最简单的jinja2模板就是一个包含响应文本的文件。
# #               1 <h1>hello world</h1>
# #               2 <h1>hello, {{ name }}</h1>
# #
# #         渲染模板
# #           默认清空下，Flask在程序文件中的templates子文件夹中寻找模板，创建
# #           templates目录， 子目录下创建index.html和user.html,hello.py中
# #           添加渲染模板代码
# #               @app.route('/')
# #               def index():
# #                   return render_template('index.html')
# #
# #               @app.route('/user/<name>')
# #               def user(name):
# #                   return render_template('user.html', name=name)
# #               flask提供的render_template()函数吧jinja2模板引擎集中到了
# #               程序中，render_template('模板文件名', 键值对,键值对，...)
# #               键值对表示模板中的变量对应的真实值
# #               name=name是关键字参数，左边的name表示参数名，就是模板中使用的
# #               占位符，右边的name是当前作用域中的变量
# #
# #         变量
# #           在模板中使用{{ name }}结构表示一个变量， 它是一种特殊的占位符，告诉
# #           模板引擎这个位置的值从渲染模板时使用的数据中获取
# #
# #           jinja2能识别所有类型的变量，如列表，字典和对象，
# #
# #           使用过滤器修改变量，过滤器名添加在变量名之后，中间使用竖线分隔
# #           部分常用过滤器
# #               {{ name | safe }}       渲染时不转义
# #               {{ name | capitalize }} 把值首字母换成大写，其他字母转换成小写
# #               {{ name | lower }}      把值转换成小写模式
# #               {{ name | upper }}      把值转换成大写模式
# #               {{ name | title }}      把值中每个单词的首字母都转换成大写
# #               {{ name | trim }}       把值的首位空格去掉
# #               {{ name | striptags }}  渲染之前把值中所有的HTML标签都删掉
# #
# #               过滤器safe默认清空下出于安全考虑，jinja2会转移所有变量
# #
# #         控制结构
# #           jinja2提供了多种控制结构，可用来改变模板的渲染流程
# #               {% if user %}
# #                   hello,{{ user }}
# #               {% else %}
# #                   hello,stranger
# #               {% endif %}
# #
# #            渲染一组元素
# #               {% for i in comments %}
# #                   <li>{{ i }}</li>
# #               {% endfor %}
# #
# #            jinja2还支持宏。宏类食欲python代码中的函数
# #               {% macro render_comment(comment) %}
# #                   <li>{{ comment }}</li>
# #               {% endmacro %}
# #
# #               {% for comment in comments %}
# #                   {{ render_comment(comment) }}
# #               {% endfor %}
# #
# #               为了重复使用宏，可以将其保存在单独的文件中，然后在模板中导入
# #                   {% import 'macros.html' as macros %}
# #                       {% for comment in comments %}
# #                           {{ macros.render_comment(comment) }}
# #                       {% endfor %}
# #
# #               需要在多处重复是哟你模板代码片段可以写入单独的文件，在包含在所有
# #               的模板中，以避免重复
# #                   {% include 'common.html' %}
# #
# #             另一种重复使用代码的强大方式是模板继承，它类是与python代码中的
# #             继承，创建base.html基模板
# #
# #                   <!DOCTYPE html>
# #                   <html lang="en">
# #                   <head>
# #                       {% block head %}
# #                   <meta charset="UTF-8">
# #                   <title>{% block title %}{% endblock %}</title>
# #                       {% endblock %}
# #                   </head>
# #                   <body>
# #                       {% block body %}
# #                       {% endblock %}
# #                   </body>
# #                   </html>
# #
# #                   block标签定义的元素可只在衍生版本中修改，定义衍生版本
# #
# #                   {% extends "base.html" %}
# #                   {% block title %}Index{% endblock %}
# #                   {% block head %}
# #                       {{ super() }}
# #                       <sytle>
# #                       </style>
# #                   {% endblock %}
# #                   {% block body %}
# #                   <h1>hello, world</h1>
# #                   {% endblock %}
# #
# #                   extends 指令声明这个模板衍生自base.html, 在extends指令
# #                   之后，基模板中其内容不是空的，所以使用super()获取原来的内容
# #
# #         使用Flask-Bootstrap集成Twitter Bootstrap
# #
# #           Bootstrap是客户端框架，不会直接涉及服务器。服务器需要作的只是提供引用了
# #           Bootstrap层叠样式(css)和javascript文件的HTML响应，并在html,css,
# #           和javascript代码中实例化所需组件。这些操作最理想的执行场所就是模板
# #
# #           安装Flask-Bootstrap的flask扩展
# #               pip install flask-bootstrap
# #               flask扩展一般都在创建程序实例时初始化
# #
# #           在hello.py中加入扩展flask-bootstrap,并初始化
# #               from flask_bootstrap import Bootstrap
# #               app = Flask(__name__)
# #               bootstrap = Bootstrap(app)
# #
# #               初始化Flask-Bootstrap之后，就可以在程序中使用一个包含所有
# #               Bootstrap文件的基模板，这个模板利用Jinja2的模板继承机制，
# #               让程序扩展一个具有基本页面结构的模板，其中就有用来引入Bootstrap
# #               的元素
# #
# #               改写user.html为衍生模板后的新版本,使用Flask—bootstrap的模板
# #                     {% extends "bootstrap/base.html" %}
# #                     {% block title %}Flasky{% endblock %}
# #                     {% block navbar %}
# #
# #                     <div class="navbar navbar-inverse" role="navigation">
# #                         <div class="container">
# #                             <div class="navbar-header">
# #                                 <button type="button" class="navbar-toggle"
# #                                 data-toggle="collapse" data-target=".navbar-collapse">
# #                                     <span class="sr-only">Tooggle navigation</span>
# #                                     <span class="icon-bar"></span>
# #                                     <span class="icon-bar"></span>
# #                                     <span class="icon-bar"></span>
# #                                 </button>
# #                                 <a href="/" class="navbar-brand">flasky</a>
# #                             </div>
# #                             <div class="navbar-collapse collapse">
# #                                 <ul class="nav navbar-nav"></ul>
# #                                 <li><a href="/">Home</a></li>
# #                             </div>
# #                         </div>
# #                     </div>
# #                     {% endblock %}
# #
# #                     {% block content %}
# #                     <div class="container">
# #                         <div class="page-header">
# #                             <h1>hello, {{ name }}!</h1>
# #                         </div>
# #                     </div>
# #                     {% endblock %}
# #
# #                     Jinja2中的extends指令从Flask-Bootstrap中导入
# #                     bootstrap/base.html,实现模板继承。flask-Bootstrap
# #                     中的基模板提供了一个网页框架，引入了Bootstrap中的所有
# #                     css和javascript文件
# #                     基模版中定义了可在衍生版中重新定义的块。block和endblock
# #                     指令定义的块中可添加到基模板中
# #                     上面这个user.html模板定义了3个块 分别title， navbar，
# #                     content 这些块都是基模板提供的
# #
# #               flask-Bootstrap的base.html模板还提供了很多其他块
# #                   块名          说明
# #                 doc           整个HTML文档
# #                 html_attribs  <html>标签的属性
# #                 html          <html>标签中的内容
# #                 head          <head>标签中的内容
# #                 title         <title>标签中的内容
# #                 metas         一组<meta>标签
# #                 styles        层叠样式表定义
# #                 body_attribs  <body>标签的属性
# #                 navbar        <body>标签中的内容
# #                 content       用户定义的页面内容
# #                 scripts       文档底部的javascript声明
# #
# #                 很多块都是Flask-Bootstrap自用的，如果直接重定义可能会导致
# #                 一些问题。如bootstrap所需的文件在styles和scripts块中声明
# #                 如果程序需要想已经有内容的块中添加新内容，必须使用jinja2中
# #                 提供的super()函数，如果哟啊在衍生模板中添加新的javascript
# #                 文件，需要这么定义scripts块：
# #                   {% block scripts %}
# #                   {{ super() }}
# #                   <script xxxxxx></script>
# #                   {% endblock %}
# #
# #         自定义错误页面
# #
# #           flask允许程序使用基于模板的自定义错误页面。最常见的错误代码有
# #           两个：404, 客户端请求未知页面或路由时显示，500,有未处理的异常时显示
# #           hello.py中添加自定义错误页面
# #               @app.errorhandler(404)
# #               def page_not_found(e):
# #                   return render_template('404.html'), 404
# #
# #               @app.errorhandler(500)
# #               def internal_server_error(e):
# #                   return render_template('500.html'), 500
# #
# #               和试图函数一样，错误处理程序也会返回响应。还返回与该错误对应的数字
# #               状态码
# #
# #           templates/base.html 中 继承flask-bootstrap/base.html
# #
# #           404.html 继承base.html
# #
# #           user.html 继承base.html
# #
# #       链接
# #           对于包含可变部分的动态路由，在模板中构建正确的URL就很困难，而且，
# #           直接编写URL会对代码中定义的路由产生不必要的依赖关系。如果重新定义路由
# #           ，模板中的链接可能会失效，为了避免这些问题，flask提供了url_for()
# #           辅助函数，它可以使用程序URL映射中保存的信息生成URL
# #
# #           url_for()函数最简单的用法是以试图函数名最为参数，返回对应的URL
# #               如 url_for('index')得到的是 /
# #                  url_for('index', _external=True)返回的是绝对地址为
# #                       http://localhost:5000
# #               生成连接城西内不同路由的链接时，使用相对地址就足够了，如果要生成
# #               在浏览器之外使用的连接，则必须使用绝对地址，例如在电子邮件中发送
# #               的链接
# #
# #           使用url_for()生成动态地址时，将动态部分作为关键字参数传入
# #               url_for('url', mame='john', _external=True)的返回结果
# #               是http://localhost:5000/user/john
# #
# #           传入url_for()的关机子参数不仅限于动态路由的参数。函数能将任何额外
# #           参数添加到查询字符串中
# #               url_for('index', page=2)的返回结果是 /?page=2
# #
# #       静态文件
# #           flask对静态文件的引用被当成一个特殊的路由
# #               url_for('static', filename='css/style.css', _external=True)
# #               将得到的结果是http://localhost:5000/static/css/style.css
# #
# #           默认清空下，flask在程序更目录中名为static的字目录中寻找静态文件。
# #           如果需要，可在static文件夹中使用子文件夹村反文件。服务器收到前面
# #           哪个URL后，会生成一个响应，包含文件系统中static/css/style.css
# #           文件的内容
# #
# #           在base.html中定义收藏夹图标
# #               {% block head %}
# #               {{ super() }}
# #               <link rel="shortcut icon"
# #               href="{{ url_for('static', filename='favicon.ico') }}"
# #               type="image/x-icon">
# #               <link rel="icon"
# #               href="{{ url_for('static', filename='favicon.ico') }}"
# #               type="image/x-icon">
# #               {% endblock %}
# #
# #               图标的声明会插入head块的末尾。注意如何使用super()保留偶基模板
# #               中定义的块的原始内容
# #
# #       使用Flask-Moment本地化日期和时间
# #           服务器需要同一时间单位，这和用户所在地地理位置无关，所以一般使用协调
# #           世界时 UTC, utc格式的时间会感到困惑，他们那更希望看到当地时间而采用
# #           当地惯用格式
# #
# #           要在服务器上只使用UTC时间，就是把时间单位发送给Web浏览器，转换成当地
# #           时间，然后渲染。web浏览器可以更好地完成这一任务，它能获取用户电脑中
# #           的时区和区域设置
# #
# #           Flask-Moment是一个Flask程序扩展， 能把moment.js集成到Jinja2
# #           模板中，可以在浏览器值嗯渲染日期和时间， 安装
# #               pip install flask-moment
# #
# #           hello.py中初始化Flask-moment
# #               from flask_moment import Moment
# #               app = Flask(__name__)
# #               moment = Moment(app
# #               .....
# #               除了moment.js, Flask-Moment还依赖jquery.js.要在HTML文档的
# #               某个地方引入这两个库，因为Bootstrap已经引入了jquery.js因此
# #               只需引入moment.js即可
# #
# #           在base.html中引入moment.js库  注意要放入{% block head %}块中
# #               {% block scripts %}
# #               {{ super() }}
# #               {{ moment.include_moment() }}
# #               {% endblock %}
# #
# #           为了处理时间戳，Flask-Moment想模板开放了moment类
# #           hello.py中，加入一个datetime变量,把变量current_time传入模板
# #           进行渲染
# #               @app.route('/')
# #               def index():
# #               return render_template('index.html',
# #                        current_time=datetime.utcnow())
# #
# #           在index.html模板中渲染current_time
# #               {% extends 'base.html' %}
# #
# #               {% block head %}
# #               {{ super() }}
# #               {{ moment.lang('zh-CN') }}
# #               {% endblock %}
# #
# #               {% block body %}
# #                   现在时间是----{{ moment(current_time).format('LLL') }}<br>
# #                   那是--{{ moment(current_time).fromNow(refresh=True) }}
# #               {% endblock %}
# #
# #               format('LLL')根据客户端电脑中的时区和区域设置渲染日期和时间，参数决定了
# #               渲染的方式， ‘L’到‘LLLL’分别对应不同的复杂度。
# #               第二行中 fromNow()渲染线对时间戳，而且会随着时间的退役自动刷新显示时间。
# #               这个时间戳最开始显示为‘几秒前’， 但指定refresh参数后，其内容会随着时间的退役而
# #               更新。如果一直等待，几分钟后，会看到显示的文本变成‘4分钟之前’
# #
# #               Flask-Moment渲染的时间戳可实现多种语言本地化
# #                   在模板中引入 moment.js库时候使用
# #                       {{ moment.lang('zh-CN') }}
# #
# #               纯正的时间戳，英文为navie time 指不包含时区的时间戳
# #               细致的时间戳，英文为awart time 指包含时间戳
# #
#
#
#
#
# #   web表单
# #       Flask-WTF扩展处理web表单
# #       安装
# #           pip install flask-wtf
# #
# #       跨站请求伪造
# #           默认情况下，Flask-WTF能够保护所有表单免受跨站请求伪造的攻击
# #           恶意网站把请求发送到被攻击者已登录的其他网站时就会引发CSRF攻击
# #
# #           为了实现CSRF保护，Flask-WTF需要程序设置一个密钥。Flask-WTF使用这个密钥生成
# #           加密令牌，再用令牌验证请求中表单数据的真伪
# #
# #           hello.py 设置Flask-WTF
# #               app.config['SECRET_KEY'] = 'xxxxx
# #
# #               app.config字典可用来储存框架，扩展和程序本身的配置变量。使用标准的字典句法
# #               就能把配置值添加到app.config对象
# #
# #               SECRET_KEY 配置变量是通用密钥，可在Flask和多个第三方扩展中使用。加密的强度
# #               取决于变量值的机密程度。不同的程序要使用不同的密钥
# #
# #       表单类
# #           使用Flask-WTF时，每个Web表单都由一个继承自Form的类表示。这个类定义表单中的一组字段
# #           每个字段都用对象表示。字段对象可附属一个或多个验证函数。验证函数用来验证用户提交的输入
# #           值是否符合要求
# #
# #           hello.py中 定义表单类
# #               from flask_wtf import Form
# #               from wtforms import StringField, SubmitField
# #               from wtforms.validators import DataRequired
# #               class Name_form(Form):
# #                   name = StringField('What is your name?',
# #                                       validators=[DataRequired()])
# #                   submit = SubmitField('Submit')
# #
# #               这个表单中的字段都定义为类变量，类变量的值是相应字段类型的对象，Name_form表单
# #               有一个名为name的本文字段和一个名为submit的提交按钮
# #               StringField类表示属性为type="text"的<input>元素。
# #               SubmitFiled类表示属性为type='submit'的<input>元素
# #               字段构造函数的第一个参数是把表单渲染成HTML时使用的标号
# #               可选参数validators指定一个由验证函数组成的列表，在接受用户提交的数据之前验证
# #               数据。验证函数DataRequired()确保提交的字段不为空
# #
# #               Form基类由Flask-WTF扩展定义，从flask_wtf中导入，字段和验证函数直接中
# #               wtforms包中导出
# #
# #           WTForms支持HTML标准字段
# #               字段类型                说明
# #             StringField       文本字段
# #             TextAreaField     多行文本字段
# #             PasswordField     密码文本字段
# #             HiddenField       隐藏文本字段
# #             DateField         文本字段， 值为datetime.date格式
# #             DateTimeField     文本字段， 值为datetime.datetime格式
# #             IntegerField      文本字段， 值为整数
# #             DecimalField      文本字段， 值为decimal.Decimal
# #             FloatField        文本字段， 值为浮点数
# #             BooleanField      复选框 值为True和False
# #             RaidField         一组单选框
# #             SelectField       下拉列表
# #             SelectMultipleField   下拉列表，可选多个值
# #             FileField         文件上传字段
# #             SubmitField       表单提交按钮
# #             FormField         把表单作为字段嵌入另一个表单
# #             FieldList         一组指定类型的字段
# #
# #           WTForms验证函数
# #             Email         验证电子邮件地址
# #             EqulTo        比较两个字段的值，常用于要求输入两次密码进行确认的清空
# #             IPAddress     验证IPv4网络地址
# #             Length        验证输入字符串字段的长度
# #             NumberRange   验证输入的值在数字范围内
# #             Optional      无输入值时跳过其他验证函数
# #             Required      确保字段中有数据
# #             Regexp        使用正则表达式验证输入的值
# #             URL           验证URL
# #             AnyOf         确保输入值在可选值列表中
# #             NoneOf        确保输入值不在可选值列表中
# #
# #       把表单渲染成HTML
# #           表单字段是可调用的，在模板中调用后会渲染成HTML，如把视图函数Name_form实例通过
# #           参数form传入模板，在模板中可以生成一个简单的表单
# #               <form method="post">
# #                   {{ form.hidden_tga() }}
# #                   {{ form.name.label }}{{ form.name() }}
# #                   {{ form.submit() }}
# #               </form>
# #
# #               若想改进表单的外观，可以把参数传入渲染字段的函数，传入的参数会被转换成
# #               字段的HTML属性。可以为字段指定id 或 class属性，然后定义css样式
# #
# #                   <form method="post">
# #                    {{ form.hidden_tga() }}
# #                    {{ form.name.label }}{{ form.name(id='my-text-field') }}
# #                    {{ form.submit() }}
# #                   </form>
# #
# #               即使能指定HTML属性，但按照这种方式渲染表单的工作量还是很打，所以在条件允许的
# #               情况下最好能使用Bootstrap中的表单演示。Flask-Bootstrap提供了一个非常高端
# #               的辅助函数， 可以使用Bootstrap中预先定义号的表单样式渲染整个Flask-wtf表单
# #
# #                   {% import "bootstrap/wtf.html" as wtf %}
# #                   {{ wtf.quick_form(form) }}
# #
# #                   import指令使用方法和普通python一样，允许导入模板中的元素并用在多个模板
# #                   中。导入的boostrap/wtf.html文件中定义了一个使用Boostrap渲染Flask-wtf
# #                   表单对象的辅助函数。wtf.quick_form()函数的参数为Flask-WTF表单对象，
# #                   使用Bootstrap的默认样式渲染传入的表单
# #
# #               index.html中使用Flask-WTF和Flask-Bootstrap渲染表单
# #                   {% extends "base.html" %}
# #                   {% import "bootstrap/wtf.html" as wtf %}
# #
# #                   {% block title %}Flasky{% endblock %}
# #
# #                   {% block page_content %}
# #                       <div class="page-header">
# #                           <h1>Hello,{% if name %}</h1>
# #                                       {{ name }}
# #                                     {% else %}
# #                                       Stranger
# #                                     {% end if %}
# #                       </div>
# #                       {{ wtf.quick_form(form) }}
# #                       {% endblock %}
# #
# #       在视图函数中的表单处理
# #
# #           hello.py中，添加接收表单数据功能
# #               @app.route('/', methods=['GET', 'POST'])
# #               def index():
# #                   name = None
# #                   form = Name_form()
# #                   if form.validate_on_submit():
# #                       name = form.name.data
# #                       form.name.data = ''
# #                   return render_template('index.html',
# #                                            current_time=datetime.utcnow(),
# #                                           form=form, name=name)
# #
# #               修饰器中添加了methods擦数告诉falsk在URL映射中把这个数图函数注册为GET
# #               和POST请求的处理程序。如果没有指定的methods参数，就只把视图参数注册为
# #               GET请求的处理程序
# #
# #               表单大豆作为post请求处理
# #
# #               局部变量name用来存放表单中输入有效名字，如果没有输入，其值为None。在视图
# #               函数中创建一个Name_form类实例用于表示表单。提交表单后，如果数据能被所有
# #               验证函数接受，那么validate_on_submit()方法的返回值为True，否则返回False
# #               这个函数的返回值决定是重新渲染表单还是处理表单提交的数据
# #
# #               用户第一次访问程序时，服务器会接受到一个没有表单数据的GET请求，所有validate_
# #               _on_submit()将返回False。if语句的内容将被跳过，通过渲染模板处理请求，并
# #               传入表单对象和值为None的name变量作为参数。用户会看到浏览器中显示了一个表单
# #
# #               用户提交表单后，服务网其收到一个包含数据的POST请求，validate_on_submit()
# #               会调用name字段上附属的Requeired()验证函数。如果名字不为空，就能通过验证
# #               validate_on_submit()反谁True。
# #               用户输入的名字可通过字段的data属性获取。在if语句中，把名字赋值给局部变量name，
# #               然后再把data属性设为空字符串，从而清空表单字段。最后一行调用render_template
# #               函数渲染模板，但这一次参数name的值为表单中输入的名字，因此会显示一个针对该用户
# #               的欢迎消息
# #
# #       重定向和用户会话
# #
# #           此刻的hello.py会存在一个可用性问题。用户输入名字后提交表单，然后点击浏览器的刷新
# #           按钮，会看到一个警告，要求再次提交表单之前进行确认。值所以出现这个情况，是因为刷新
# #           页面时浏览器会重新发送之前已经发送果的最后一个请求，如果这个请求是一个包含表单数据
# #           post请求，刷新页面后会再次提交表单
# #
# #           解决方法，不让web程序把post请求最为浏览器发送的最后一个请求
# #
# #           实现方式，使用重定向作为post请求的响应，为不是使用常规响应。重定向是一种特殊的
# #           响应，响应内容是URL，而不是包含HTML代码的字符串，浏览器收到这种响应时，会向重定向
# #           的URL发起get请求，显示页面的内容。这个技巧称为 Post/重定向/Get模式
# #
# #           这中方法会带来令一个问题，程序处理POST请求时，使用form.name.data获取用户输入
# #           的名字，可是一旦这个请求结束，数据也就丢失了，因为这个POST请求使用重定向处理，所以
# #           程序需要保存输入的名字，这样重定向后的请求才能获得并使用这个名字，从而够真真正的，
# #           响应
# #
# #           程序可以把数据存储在用户会话中，在请求之间“记住”数据，用户会话是一种私有存储
# #           ，存在于每个连接到服务器的客户端中。用户会话，它是一种请求上下文中的变量，名为
# #           session 想标准的python字典一样操作
# #
# #           默认情况下，用户会话保存在客户端cookie中，使用设置的SECRET_key进行加密，如果
# #           修改了cookie中的内容，签名就会失效，会话也随之失效
# #
# #           修改hello.py 添加重定向和用户会话功能
# #               @app.route('/', methods=['GET', 'POST'])
# #               def index():
# #               form = Name_form()
# #               if form.validate_on_submit():
# #                   session['name'] = form.name.data
# #                   return redirect(url_for('index'))
# #               return render_template('index.html', current_time=datetime.utcnow(),
# #                            form=form, name=session.get('name'))
# #
# #               前一个版本，局部变量name被用于存储用户在表单中输入的名字。这个变量现在保存在用户
# #               会话中，即session['name'],所以在两次请求之间也能记住输入的值
# #
# #               现在包含合法表单数据的请求最后最后会调用redirect()函数。redirect()辅助函数，
# #               用来生成HTTP重定向响应。redirect()函数的参数是重定向的URL，这里使用的重定向
# #               URL是程序的根地址，因此重定向响应本可以写的更简单一些，写成redirect('/'),但
# #               却使用flask提供的url生成函数url_for(),推荐使用url_for()生成URL，因为这个
# #               函数是使用URL映射生成URL，从而保证URL和定义的路由兼容，而且修改路由名字后依然
# #               可用
# #
# #               url_for()函数的第一个且唯一必须指定的参数是 端点 名，即路由的内部名字。默认
# #               情况下，路由的端点是相应试图函数的名字，即路由的内部名字。
# #
# #               使用session.get('name')直接从会话中读取name参数的值，和普通字典一样，这里
# #               使用get()获取字典中键对象值以避免未找到键的异常情况，因为对于不存在的键，get
# #               会返回默认值None
# #
# #       Flash消息
# #           读取完成后，有时需要让用户知道状态发生了变化。可以使用确认消息，警告或者错误提醒
# #           典型的例子，用户提交了以偶一项错误的登录表单后，服务器发回的响应重新渲染了登录，
# #           表单，并在表但上面显示一个消息，提示用户用户名和密码错误
# #
# #           hello.py中 添加 Flash消息
# #               app.route('/', methods=['GET', 'POST'])
# #               def index():
# #                   form = Name_form()
# #                   if form.validate_on_submit():
# #                       old_name = session.get('name')
# #                           if old_name is not None and old_name != form.name.data:
# #                               flash('你好像改了你的名字')
# #                       session['name'] = form.name.data
# #                       return redirect(url_for('index'))
# #                   return render_template('index.html', current_time=datetime.utcnow(),
# #                            form=form, name=session.get('name'))
# #
# #               每次提交的名字都会和储存在用户会话中的名字进行比较，而会话中存储的名字是前一次
# #               在这个表单中提交的数据。如果两个名字不一样，就会调用flash()函数，在发给客户端的
# #               下一个响应中显示一个消息
# #
# #               仅调用flash()函数不能把消息显示出来，程序使用的模板要渲染这条消息，最好在
# #               基模板中渲染Flash消息，因为这样所有的页面能使用这些消息。Flask把
# #               get_flashed_messages()函数开放给模板，用来获取并渲染消息
# #
# #               base.html 渲染Flash消息
# #
# #                   {% for message in get_flashed_messages() %}
# #                       {{ message }}
# #                   {% endfor %}
# #
# #                   在模板中使用循环是因为在之前的请求循环中每次调用flash()函数时都会
# #                   生成一个消息，所有可能有多个消息在排队等带显示.get_flashed_messages()
# #                   函数获取的消息在下次调用时不会再次返回，因此Flash消息只显示一次，然后就
# #                   消失了
#
#
#
# #   数据库
# #
# #       web程序中最长于基于 关系模型的数据库，这种数据库也称SQL数据库，因为他们使用结构化语言
# #       不过最近几年文档数据库和键值对数据可成了流行的替代选择，这两种数据库合成NoSQL
# #
# #       SQL数据库
# #           关系型数据库把数据存储在表中，表模拟程序中不同的实体。
# #           表的列数是固定的，行数是可变的。列定义表所表示实体的数据属性。表中的行定义各列对应
# #           的真数数据
# #           表中有个特殊的列，称为主键，其值为表中各行的唯一标识符。表中还可以有称为外键的列，
# #           引用同一个表或不同表中的某行的主键。行之间的联系称为关系，这是关系型数据库模型的基础
# #
# #           角色(roles)          用户(user)
# #           id   ——|————           id
# #           name        |        username
# #                       |        password
# #                       |——————  role_id
# #
# #           在这个数据库关系图中，roles表示储存所有可用的用户角色，每个角色都使用一个唯一的
# #           id值（主键）进行标识， users包含用户列表, 每个用户也有唯一的id值。除了id主键之外
# #           ，roles表中还有name列，user表中有username和password列。users表中的role_id列
# #           是外键，引用角色的id，通过这种方式为每个用户指定角色
# #
# #           关系型数据库存储数据很高效，而且避免了重复。将这个数据库中的用户角色重命名也很简单，
# #           因为角色名只出现在一个地方。一旦roles表中修改完角色名，所有通过role_id应用这个角色的
# #           用户都能立即看到更新
# #
# #           从另一方面来看，把数据库分别存放在多个表中还是很复杂的。生成一个包含角色的用户列表会
# #           遇到一个小问题，因此在此之前哟啊分别从两个表中读取用户和用户角色，在将其联结起来
# #           关系型数据库引擎为连接操作提供了必要的支持
# #
# #       NoSQL数据库
# #
# #           所有不遵循sql的关系模型的数据库统称为NoSQL数据库，NoSQL数据库一般使用集合代替表
# #           使用，文档代替记录。NoSQL数据库采用的设计方式使联结变得困难，所以大多数数据库根本
# #           根本不支持这种操作。
# #
# #               用户(user)
# #                   id
# #                   username
# #                   password
# #                   role
# #
# #               它减少了表的数量，却增加了数据重复量，这种结构的数据库要把角色名存储在每个
# #               用户中。如此一来，将角色重复名的操作就变得很耗时，可能数要更新大量文档
# #
# #               使用NoSQL数据库当然也有好处。数据重复可以提升查询速度。列出哟南湖及其角色的
# #               操作很简单，因为无需联结
# #
# #       使用SQL还是NoSQL
# #
# #           SQL数据库善于用高且且紧凑的形式存储结构化数据。这种数据库需要话费大量精力保证数据
# #           的一致性。NoSQL数据库放宽了对这种一致性的要求，从而获得性能上的优势
# #
# #           对于中小型程序来说，SQL和NoSQL数据库都是很好的选择，而且性能相当
# #
# #       python数据库框架
# #
# #           大多数数据库引擎都由对应的python包，包括开源包和商业包。flask并不限制你使用
# #           和种类型的数据包，因此可以根据自己的喜好选择MySQL, Postgres, SQLite,Redis
# #           MongoDB或者CouchDB
# #
# #           还有一些数据库抽象层代码包， 如SQLAlchemy和MongoEngine 可以直接使用这些抽象包
# #           直接处理高等级的Python对象，而不用处理如表，文档或查询语言此类的数据库实体
# #
# #           选择数据库框架时，要考虑很多因素
# #
# #               易用性
# #                   如果直接比较数据库引擎和数据可抽象层，抽象层取胜。抽象层，也称为对象关系
# #                   映射（ORM）或对象文档映射(ODM)，在用户不知觉的情况下把高层的面向对象
# #                   操作转换成低层的数据库指令
# #
# #               性能
# #                   ORM和ODM把对象业务转换成数据库业务会有一定的损耗。大多数情况下，这种性能
# #                   的降低微不足道，但也不一定都是如此，一般情况下，ORM和ODM对生产效率的提升
# #                   远远超过了这一丁点的性能降低， 所以性能降低这个理由不足以说服用户完全放弃
# #                   ORM和ODM。真正的关键点在于如何选择一个能直接操作底层数据库的抽象层，以防
# #                   特定的操作需要直接使用数据库原生指令优化
# #
# #               可移植性
# #                   选择数据库时， 必须考虑其是否能在你的开发平台和生成平台中使用。如果打算
# #                   利用云平台托管程序，就要知道这个云服务提供哪些数据库可供选择。可移植性
# #                   还针对ORM和ODM。尽管有些框架职位一种数据库引擎提供抽象层，但其他框架
# #                   可能做了更高层的抽象，他们支持不同的数据库引擎，而且都使用相同的面向对象
# #                   接口。SQLAlchemy ORM就是一个很好的例子，它支持很多关系熊数据库引擎，
# #                   包括MySQL，Postgres和SQLite
# #
# #               Flask集成度
# #                   选择框架时，不一定非得选择已经继承了Flask的框架，但选择这些框架可以节省
# #                   你编写继承代码的时间。使用继承了Flask框架可以简化配置和操作，所以专门为
# #                   Flask开发的扩展是你的首选
# #
# #       使用Flask-SQLAlchemy管理数据库
# #
# #           Flask-SQLAlchemy是一个Flask扩展，简化了在Flask程序中使用SQLAlchemy的操作。
# #           SQLAlchemy是一个很强大的关系型数据库框架，支持多种数据库后他。SQLAlchemy提供
# #           了高层ORM，也提供了使用数据库原生SQL的底层功能
# #
# #           安装
# #               pip install flask-sqlalchemy
# #
# #           在Flask-SQLAlchemy中，数据库使用URL指定。最流行的数据库引擎采用的数据库URL
# #
# #               MySQL    mysql://username:password@hostname/database
# #               Postgres    postgresql://username:password@hostname/database
# #               SQLite(Unix)  sqlite:////absolute/path/to/database
# #
# #               hostname表示MySQL服务器所在的主机，可以是本地主机(localhost)
# #               也可以是远程服务器。数据库服务器上可以托管多个数据库，因此database
# #               表示要使用的数据库名。如果数据库需要认证，username和password表示数据库
# #               用户密令，SQLite数据库不需要使用服务器，因此不用指定hostname,username和
# #               password. URL中的database是硬盘上文件的文件名
# #
# #               程序使用的数据库URL必须保存到Flask配置对象的SQLALCHEMY_DATABASE_URI
# #               键中。配置对象还有一个很有用的选项，即SQLALCHEMY_COMMIT_ON_TEARDOWN键
# #               ，将其设置为True时，每次请求结束后都会自动提交数据库的变动。
# #
# #           在hello.py中 配置一个简单的SQLite数据库
# #
# #               from flask_sqlalchemy import SQLAlchemy
# #               basedir = os.path.abspath(os.path.dirname(__file__))
# #               app.config['SQLALCHEMY_DATABASE_URI'] = \
# #                           'sqlite:///'+os.path.join(basedir, 'data.sqlite')
# #               app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# #               db = SQLAlchemy(app)
# #
# #               db对象是SQLAlchemy类的实例，表示程序使用的数据，同时还获得了Flask-SQLAlchemy
# #               提供的所有功能
# #
# #           定义模型
# #               模型这个术语表示程序四海用的持久化实体。在ORM中，模型一般是一个python类，类
# #               中的属性对应数据库表中的列
# #
# #               Flask-SQLAlchemy创建的数据库实例为模型提供了一个基类以及一系列辅助类和辅助
# #               函数，可用于定义模型的结构
# #
# #               hello.py中， 定义 role（角色）和 user（用户）模型
# #                   class Role(db.Model):
# #                   __tablename__ = 'roles'
# #                   id = db.Column(db.Integer, primary_key=True)
# #                   name = db.Column(db.String(64), unique=True)
# #
# #                   def __repr__(self):
# #                       return '<Role %r>' % self.name
# #
# #               class User(db.Model):
# #                   __tablename__ = 'users'
# #                   id = db.Column(db.Integer, primary_key=True)
# #                   username = db.Column(db.String(64), unique=True, index=True)
# #
# #                   def __repr__(self):
# #                       return '<User %r>' % self.username
# #
# #               类变量 __tablename__定义在数据库中使用的表明。如果没有定义__tablename__
# #               ,Flask-SQLAlchemy会使用一个默认的名字,但默认的表名没有准收使用复数形式进行
# #               命名的约定，推荐自己命名。其余的类变量都是该模型的属性，被定义为db.Column类
# #               的实例
# #
# #               db.Column类构造函数的第一个参数是数据库列和模型属性的类型
# #               一些可用的列类型以及在模型中的python类型
# #                   类型名         python类型            说明
# #                   Integer         int                普通整数，一般32位
# #                   SmallInteger    int                 取值范围小的整数，一般是16位
# #                   BigInteger      int或long            不限精度的整数
# #                   Float           float               浮点数
# #                   Numeric         decimal.Decimal     定点数
# #                   String          str                 变长的字符串
# #                   Text            str                 变长的字符串，对较长或不限长度的字符串做了优化
# #                   Unicode         unicode             变长的Unicode字符串
# #                   UnicodeText     unicode             变长的Unicode字符串，对较长或不限长度的字符串做了优化
# #                   Boolean         bool                布尔值
# #                   Date            datetime.date       日期
# #                   Time            datetime.time       时间
# #                   Datetime        datetime.datetime   日期和时间
# #                   Interval        datetime.timedelta  时间间隔
# #                   Enum            str                 一组字符串
# #                   PickleType      任何python对象       自动使用Pickle序列化
# #                   LargerBinary    str                 二进制文件
# #
# #               db.Column中其余的参数指定属性配置选项
# #
# #                   选项名             说明
# #                   primary_key         如果设为True，这就是表的主键
# #                   unique              如果设为True，这列不允许出现重复的值
# #                   index               如果设为True，为这列创建索引，提升查询效率
# #                   nullable            如果设为True，这列允许使用空值;如果设为False,这列不允许使用控制
# #                   default             为这列定义默认值
# #
# #               Flask-SQLAlchemy要求每个模型都要定义主键，这一列经常命名为id
# #               虽然没有强制要求，但这个两个模型都定义了__repr()__方法，返回一个具有可读性的
# #               字符串表示模型，可在调试和测试时使用。
# #
# #       关系
# #           关系型数据库使用关系把不同表中的行联系起来， 角色和用户的一对多关系，一个角色可属于
# #           多个用户，而每个用户都只能有一个角色
# #
# #           hello.py中添加关系
# #
# #               class Role(db.Model):
# #                   ...
# #                   users = db.relationship('User', backref='role')
# #
# #               class User(db.Model):
# #                   ...
# #                   role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
# #
# #               关系是由users表中的外键连接了两行。添加到User模型中的role_id列被定义为
# #               外键，就是这个外键建立起了关系。传给db.ForeignKey()的参数'roles.id'表明
# #               ，这列的值是roles表中行的id值。
# #
# #               添加Role模型中的users属性代表这个关系的面向对象视角。对于一个Role类的实例
# #               其users属性将返回与角色相关连的用户组成的列表。db.relationship()的第一个
# #               参数表明这个关系的另一端是哪个模型。如果模型类尚未定义，可使用字符串形式指定
# #
# #               db.relationship()中的backref参数相关User模型中添加一个role属性，从而
# #               定义方向关系，这一属性可替代role_id反问Role模型，此时获取的是模型对象，而
# #               不是外键的值
# #
# #               大多数情况下，db.relationship()都能自行找到关系中的外键，但优势却无法决定
# #               把哪一列作为外键。如，如果User模型中有两个或以上的列定为Role模型的外间。
# #               SQLAlchemy就不知道该使用哪列。如果无法决定外键，你就要为db.relationship()
# #               提供额外的参数，从而确定所用外键
# #
# #               常用的SQLAlchemy关系选项
# #                   选项名         说明
# #                 backref       在关系的另一个模型中添加反向引用
# #                 primaryjoin   明确指定两个模型之间使用的联结条件。只有在模棱两可的关系中需要指定
# #                 lazy          abiding如何加载相关记录，
# #                                   可选值有select ：首次访问时按需加载
# #                                         immediate：源对象加载后就加载
# #                                         joined：加载记录，但使用联结
# #                                         subquery：路基加载，但使用子查询
# #                                         noload：永不加载
# #                                         dynamic：不加载记录，但提供哦加载记录的查询
# #                 uselist       如果设为Flaes，不使用列表，而使用标量值
# #                 order_by      指定关系中记录的排序方式
# #                 secondary     指定多对多关系中关系表的名字
# #                 secondaryjoin SQLAlchemy无法自行决定时，指定多对多关系中的二级联结条件
# #
# #               除了一对多之外，还有几种其他的关系类型。一对一关系可以用前面介绍的一对多关系
# #               表示，但调用db.relationship()时要把uselist设为False，把"多"变成1
# #               多对一关系也可使用一对多表示，对调两个表即可，或者把外键和db.relationship()
# #               都放在多这一次。最复杂的关系类型是多对多，需要用到第三张表，这个表称为关系表
# #
# #           数据库操作
# #
# #               创建表
# #                   python shell中
# #                       >>> from hello import db
# #                       >>> db.create_all()
# #
# #                       查看程序目录，发现了一个名为data.sqlite的文件。这个SQLite数据库文件
# #                       的名字就是在配置中指定的，如果数据库表已经存在于数据库中，那么
# #                       db.create_all()重新创新或者更新这个表。如果修改模型后要把改动
# #                       应用到现有的数据库中，这一特性会带来不便，更新现有数据表的粗暴方式
# #                       是先删除旧表再重新创建
# #                           db.drop_all()
# #                           db.create.all()
# #
# #               插入行
# #                   创建角色和用户
# #                       >>> from hello import Role, User
# #                       >>> admin_role = Role(name='Admin')
# #                       >>> mod_role = Role(name='Moderator')
# #                       >>> user_role = Role(name='User')
# #                       >>> user_john = User(username='john', role=admin_role)
# #                       >>> user_susan = User(username='susan', role=user_role)
# #                       >>> user_david = User(username='david', role=user_role)
# #
# #                       模型的构造函数接受的参数是使用关键字参数指定的模型属性初始值，role
# #                       属性也可使用，虽然它不是真正的数据库列，但却是对一对多关系的高级表示
# #                       这些新建对象的id属性并没有明确设定，因为主键是由Flask-SQLAlchemy
# #                       管理的。现在对这些对象只存在于python中，还未写入数据库
# #
# #                       通过数据库会话管理对数据库所作的改动，在Flask_SQLAlchemy中，会话
# #                       由db.session表示，准备把对象写入数据库之前，先要将其添加到会话中
# #
# #                           >>> db.session.add(admin_role)
# #                           >>> db.session.add(mod_role)
# #                           >>> db.session.add(user_role)
# #                           >>> db.session.add(user_john)
# #                           >>> db.session.add(user_susan)
# #                           >>> db.session.add(user_david)
# #
# #                           或简写成：
# #                               db.session.add_all([admin_role, mod_role,
# #                                                  user_role, user_john,
# #                                                  user_sudan, user_david])
# #
# #                       为了把对象写入数据库，要调用commit()方法提交会话
# #
# #                           db.session.commit()
# #
# #                       数据库会话也称事物
# #
# #                       数据库会话能够保证数据库的一致性，提交操作使用原子方式把会话中的对象
# #                       全部写入数据库。如果在写入会话的过程中发生了错误，整个会话都会失效
# #                       。如果你始终把相关改动放在会话中提交，哪就能避免因部分更新导致的数据库
# #                       不一致性
# #
# #                       数据库会话也会回滚，调用db.session.rollback()后，添加到数据库会话
# #                       中的所有对象都会还原它们在数据库时的状态
# #
# #               修改行
# #                   数据库会话上调用add()方法也能更新模型。
# #
# #                       >>> admin_role.name = 'Administrator'
# #                       >>> db.session.add(admin_role)
# #                       >>> db.session.commit()
# #
# #               删除行
# #                   delete()方法
# #                       >>> db.session.delete(mod_role)
# #                       >>> db.session.commit()
# #
# #               查询行
# #                   Flask-SQLAlchemy为每个模型都提供了query对象，最基本的模型查询是取回
# #                   对应表中的所有记录
# #                       >>> Role.query.all()
# #                           [<Role u'Administrator'>, <Role u'User'>]
# #                       >>> User.query.all()
# #                           [<User u'john'>, <User u'susan'>, <User u'david'>]
# #
# #                   使用过滤器filter_by配上query对象进行更精确的查找
# #                       >>> User.query.filter_by(role=user_role).all()
# #                       [<User u'susan'>, <User u'david'>]
# #
# #                   若要查看SQLAlchemy为查询生成的SQL查询语句，只需要把query对象转换成字符串
# #                       >>> str(User.query.filter_by(role=user_role))
# #                           'SELECT users.id AS users_id, users.username AS
# #                           users_username, users.role_id AS users_role_id \n
# #                           FROM users WHERE ? = users.role_id'
# #
# #                   若退出了shell会话，前面这些例子中创建的对象就不会以python对象的形式存在
# #                   而是作为各数据库表中的行，如果你打开了一个新的shell会话，就要从数据库
# #                   中读取行，在重新创建python对象
# #
# #                   常用的SQLAlchemy查询过滤器
# #
# #                       filter()    把过滤器添加到原查询上，返回一个新查询
# #                       filter_by() 把等值过滤器添加到原查询上，返回一个新查询
# #                       limit()     使用指定的值限制原查询返回的结果数量
# #                       offset()    偏移查询返回的结果，返回一个新的 查询
# #                       order_by()  根据指定条件对原查询结果进行排序，返回一个新查询
# #                       group_by()  根据指定条件对原查询结果进行分组，返回一个新查询
# #
# #                   常用的SQLAlchemy查询执行函数
# #
# #                       方法              说明
# #                       all()           以列表形式返回查询的所有结果
# #                       first()         返回查询的第一个结果，如果没有结果，则返回None
# #                       first_or_404()  返回查询的第一个结果，如果没有结果，则终止请求，返回
# #                                       404错误响应
# #                       get()           返回指定主键对应的行，如果没有对应的行，则返回None
# #                       get_or_404()    返回指定主键对应的行，如果没找到指定的主键，这终
# #                                       止请求，返回404错误响应
# #                       count()         返回查询结果的数量
# #                       paginate()      返回一个Paginate对象，它包含指定范围内的结果
# #
# #                   关系和查询的处理方式类似。
# #
# #                       >>> user_role = Role.query.filter_by(name='User').first()
# #                       >>> users = user_role.users
# #                       >>> users
# #                           [<User u'susan'>, <User u'david'>]
# #                       >>> users[0].role
# #                           <Role u'User'>
# #
# #                       例子中user_role.users有个小问题。执行user_role.users表达式时
# #                       隐含的查询会调用all()返回一个用户列表。query对象是隐藏的，因此无法
# #                       更精确的查询过滤器。就这个特定示例而言，返回一个按照字母顺序排序的
# #                       用户列表可能更好
# #
# #                       hello.py 添加了动态关系 参数lazy，禁止自动执行查询
# #
# #                           class Role(db.Model):
# #                               ...
# #                               users = db.relationship('User', backref='role',
# #                                                        lazy='dynamic')
# #
# #                          加入了lazy参数之后， user_role.users会返回一个尚未执行的查询，
# #                          lazy = 'dynamic' 不加载记录，但加载记录的查询
# #                           因此可以在其上添加过滤器
# #
# #                               >>> user_role = Role.query.filter_by(name='User').first()
# #                               >>> user_role.users.order_by(User.username).all()
# #                                   [<User u'david'>, <User u'susan'>]
# #                               >>> user_role.users.count()
# #                                   2
# #
# #           在试图函数中操作数据库
# #
# #               hello.py中 添加处理收到post的代码与数据库互动
# #                   @app.route('/', methods=['GET', 'POST'])
# #                   def index():
# #                   form = Name_form()
# #                   if form.validate_on_submit():
# #                       user = User.query.filter_by(username=form.name.data).first()
# #                       if user is None:
# #                           user = User(username=form.name.data)
# #                           db.session.add(user)
# #                           session['known'] = False
# #                       else:
# #                           session['known'] = True
# #                       session['name'] = form.name.data
# #                       form.name.data = ''
# #                       return redirect(url_for('index'))
# #                   return render_template('index.html', form=form, name=session.get('name'),
# #                            known=session.get('known', False))
# #
# #                   提交表单后，程序会使用filter_by()查询过滤器在数据库中查找提交的名字
# #                   变量known被写入用户会话中，因此重定向之后，就可以把数据传给模板，用来显示
# #                   自定义的欢迎消息
# #
# #               更新index.html 使用known参数
# #
# #                   {% if not known %}
# #                   <p>pleased to meet you</p>
# #                   {% else %}
# #                   <p>Happy to see you again</p>
# #                   {% endif %}
# #
# #           集成python shell
# #               每次启动shell会话都要导入数据库实例和模型，十分枯燥的工作。为了避免重复
# #               导入，可以做些配置，让 Flask-script的shell命令自动导入特定的对象
# #
# #               若想把对象添加到导入列表中，要为shell命令注册一个make_context回调哈数
# #
# #               hello.py 中继承python shell 为shell命令添加一个上下文
# #
# #                   def make_shell_context():
# #                       return dict(app=app, db=db, User=User, Role=Role)
# #                   manager.add_command("shell", Shell(make_context=make_shell_context))
# #
# #                   make_shell_command()函数注册了程序，数据库实例以及模型，因此这些
# #                   对象能直接导入shell
# #
# #                       >>> app
# #                           <Flask 'hello'>
# #                       >>> db
# #                           <SQLAlchemy engine=sqlite:////home/
# #                            zhengyu/PycharmProjects/
# #                            flask_web/flask_web_len/data.sqlite>
# #                       >>> User
# #                           <class '__main__.User'>
# #
# #           使用Flask-Migrate实现数据库迁移
# #
# #               开发程序过程中，会发现时候需要修改数据库模型，而且修改之后还需要更新数据库
# #               仅当数据库表不存在时，Flask-SQLAlchemy才会根据模型进行创建。因此，根新表
# #               唯一方式就是下那删除旧表，不过这样做会丢失数据库中的所有数据
# #
# #               更新表的更好的方法是使用数据库迁移框架。源码版本控制工具可以跟踪源码文件的变化
# #               类似的，数据库迁移框架能跟踪数据库模式的变化，然后增量式的把变化应用到数据库中
# #               SQLAlchemy的主力开发人员编写了一个迁移框架，称为Alembic。除了Alembic之外，
# #               Flask程序还可以使用Flask-Migrate扩展。这个扩展对Alembic做了轻量级包装，并
# #               集成到Flask-Script中，所有操作都通过Flask-Script命令完成
# #
# #               创建迁移仓库
# #
# #                   安装Flask-Migrate
# #
# #                       pip install flask-migrate
# #
# #                   hello.py 配置Flask_Migrate
# #
# #                       from flask_migrate import Migrate, MigrateCommand
# #                       migrate = Migrate(app, db)
# #                       manager.add_command('db', MigrateCommand)
# #
# #                       为了导出数据库迁移命令，Flask-Migrate提供了一个MigrateCommand类
# #                       可附加到Flask-Script的manager对象上，MigrateCommand类使用db
# #                       命令附加
# #
# #                   在维护数据库迁移之前，要使用init子命令创建迁移仓库
# #
# #                       python hello.py db init
# #
# #                       这个命令会创建migrations文件夹，所有迁移脚本都存放其中
# #                       数据库迁移仓库中的文件要和程序的其他文件一起纳入版本控制
# #
# #               创建迁移脚本
# #
# #                   在Alembic中，数据库迁移用 迁移脚本 表示。脚本中有俩个函数，分别是
# #                   upgrade()和downgrade().upgrade()函数把迁移中的改动与应用到数据库
# #                   中，downgrade()函数则将改动删除。Alembic具有添加和删除的能力，因此
# #                   数据库可重设到修改历史的任意一点
# #
# #                   可以使用 revision 命令手动创建 Alembic迁移，也可使用migrate命令
# #                   自动创建。手动创建的迁移只是一个骨架，upgrade()和downgrade()函数都是
# #                   空的， 开发者要使用Alembic提供 Operations 对象指令实现具体操作。自动
# #                   创建的迁移会根据模型定义和数据库当前状态之间的差异生成upgrade()和
# #                   downgrade()函数的内容
# #
# #                   自动创建的迁移不一定总是正确的，有可能会漏掉一些细节。自动生成迁移脚本后
# #                   一定要进行检查
# #
# #                   migrate子命令用来自动创建迁移脚本
# #
# #                       python hello.py db migrate -m "initial migration"
# #
# #               更新数据库
# #
# #                   检查并修正好迁移脚本之后，我们可以是引用db upgrade命令把迁移应用到
# #                   数据库中
# #
# #                       python hello.py db upgrade
# #
# #                   第的第一个迁移来说，其作用和调用 db.create_all()方法一样，但在后续的
# #                   迁移中，upgrade命令能把改动应用到数据库中，且不影响其中保存的数据
#
#
#
# #   电子邮件
# #
# #       使用Flask-Mail提供电子邮件的支持
# #
# #           安装Flask-Mail
# #
# #               pip install flask-mail
# #
# #           Flask-Mail连接到简单邮件传输协议（SMTP）服务器，并把邮件交给这个服务器发送。
# #           如果不进行配置， Flask-Mail会连接 localhost上的端口25,无需验证即可发送电子
# #           邮件
# #
# #           Flask-Mail SMTP服务器的配置
# #
# #               配置            默认值         说明
# #              MAIL_SERVER      localhost    电子邮件服务器的主机名或IP地址
# #              MAIL_PORT        25           电子哟键服务器的端口
# #              MAIL_USE_TLS     False        启动传输层安全（TLS）协议
# #              MAIL_USE_SSL     False        启用安全套接层（SSL）协议
# #              MAIL_USERNAME    None         邮箱账户的用户名
# #              MAIL_PASSWORD    None         邮箱账户的密码
# #
# #           在开发过程中，如果连接到外部SMTP服务器， 则可能更方便。
# #
# #           hello.py 中配置Flask—Mail使用 google Gmail账户发送电子邮件
# #
# #               app.config['MAIL_SERVER'] = 'smtp.qq.com'
# #               app.config['MAIL_PORT'] = 465
# #               app.config['MAIL_USE_SSL'] = True
# #               app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
# #               app.config['MAIL_PASSWORD'] = 'padundmltvrlcbdc'
# #
# #               经过反复测试次配置正确能发邮件 不同邮箱的SMTP协议不同，以qq邮箱为例
# #               需要开启SMTP服务，会得到授权码 也就是登录的密码
# #
# #
# #               为了保护账户信息，你需要让脚本从环境中导入敏感信息
# #
# #           hello.py中 初始化Flask—Mail
# #
# #               from flask_mail import Mail
# #               mail = Mail(app)
# #
# #           保存电子邮件服务器用户名和密码的两个环境变量要在环境中定义。如果linux中
# #
# #               export MAIL_USERNAME=<邮箱名字>
# #               export MAIL_PASSWORD=<密码名字>
# #
# #           在python shell中发送电子邮件
# #
# #               >>> from flask_mail import Message
# #               >>> from hello import mail
# #               >>> msg = Message('1111', sender='174927390@qq.com', recipients=['174927390@qq.com'])
# #               >>> msg.body = 'aaa'
# #               >>> msg.html = '<b>HTML</b> body'
# #               >>> with app.app_context():
# #               ...     mail.send(msg)
# #               ...
# #               试过之后有错误 有待修改
# #
# #           在程序中集成发送电子邮件功能
# #
# #               为了避免每次都手动编写电子邮件消息，我们最好把程序发送电子邮箱的通用部分抽象
# #               出来，定义成一个函数。这么作还有个好处，即函数可以使用Jinja2模板渲染邮件正文，
# #               灵活性极高
# #
# #           hello.py中 集成发送电子邮件功能
# #
# #               为了避免每次都动手编写电子邮件消息，我们最好把程序发送电子邮件的通用部分抽象出
# #               来，定义成一个函数。这么作还有一个好处，即该函数可以使用Jinja2模板渲染邮箱正文
# #               灵活性极高
# #
# #                   from flask_mail import Message
# #                   app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
# #                   app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin 174927390@qq.com'
# #                   def send_email(to, subject, template, **kwargs):
# #                       msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX']+subject,
# #                                       sender=app.config['FLASKY_MAIL_SENDER'],
# #                                       recipients=[to])
# #                       msg.body = render_template(template+'.txt', **kwargs)
# #                       msg.html = render_template(template+'.html', **kwargs)
# #                       mail.send(msg)
# #
# #                   这个函数用到了两个程序特定配置项，分别定义邮件主题的前缀和发件人地址
# #                   send_email函数的参数分别为接收人地址，主题，渲染邮件正文的模板和关
# #                   键字参数列表，指定模板的时候不能包含扩展名，这样才能使两个模板分别渲染
# #                   纯文本正文和富文本正文调用者将关键字参数传给render_template()函数，
# #                   以便在模板中使用，进而生成电子邮件正文
# #
# #               index()函数很容易被扩展，每当表单接收新名字时，程序都会给管理员发送一封电子
# #               邮件
# #
# #               hello.py中 电子邮件示例
# #
# #                   app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
# #
# #                   @app.route('/', methods=['GET', 'POST'])
# #                   def index():
# #                       form = Name_form()
# #                       if form.validate_on_submit():
# #                           user = User.query.filter_by(username=form.name.data).first()
# #                           if user is None:
# #                               user = User(username=form.name.data)
# #                               db.session.add(user)
# #                               session['known'] = False
# #                               if app.config['FLASKY_ADMIN']:
# #                                   send_email(app.config['FLASKY_ADMIN'],
# #                                       'New User', 'mail/new_user',user=user)
# #                           else:
# #                               session['known'] = True
# #                           session['name'] = form.name.data
# #                           form.name.data = ''
# #                           return redirect(url_for('index'))
# #                       return render_template('index.html', form=form,
# #                               name=session.get('name'),known=session.get('known', False))
# #
# #                   电子邮件的收件人保存在环境变量FLASKY_ADMIN中，在程序启动过程中，他会加载
# #                   到一个同名配置变量中。我们要创建俩个模板文件，分别用于渲染纯文本和HTML
# #                   版本的邮件正文。这两个模板文件都保存在templates文件夹下的mail子文件夹中
# #                   以便和普通同版本区分开来。电子邮件的模板中要有一个模板参数是用户，因此调用send_mail
# #                   函数时要以关键字参数的形式传入用户
# #
# #                   使用环境变量FLASKY_ADMIN
# #
# #                       export FLASKY_ADMIN=174927390@qq.com
# #
# #                       若不使用环境变量
# #
# #                           app.config['FLASKY_ADMIN'] = '174927390@qq.com'
# #
# #           异步发送电子邮件
# #
# #               如果你发送了几封测试邮件，可能会注意到mail.send()函数在发送电子邮件时
# #               停滞了几秒钟，在这个过程中浏览器就像无响应一样。为了避免处理请求过程中
# #               不必要的延迟我们可以把发送电子邮件的函数移到后台线程中
# #
# #               hello中，异步发送电子邮件
# #
# #                   from threading import Thread
# #                   def send_async_email(app, msg):
# #                       with app.app_context():
# #                       mail.send(msg)
# #
# #                   def send_email(to, subject, template, **kwargs):
# #                       msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX']+subject,
# #                       sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
# #                       msg.body = render_template(template+'.txt', **kwargs)
# #                       msg.html = render_template(template+'.html', **kwargs)
# #                       thr = Thread(target=send_async_email, args=[app, msg])
# #                       thr.start()
# #                       return thr
# #
# #                   上述实现涉及一个有趣的问题。很多Flask扩展都假设已经存在激活的程序上下文
# #                   和请求上下文。Flask-Mail中的send()函数使用current_app，因此必须激活
# #                   程序上下文。不过，在不同线程中执行mail.send()函数时候，程序上下文要使用
# #                   app.app_context()人工创建
# #
# #                   现在运行程序，你会发现程序流畅多了，不过要记住，程序要发送给大量电子邮件，
# #                   使用专门发送电子邮件的作业要比给每逢邮件都创建一个线程更合适，我们可以把
# #                   执行send_async_email()函数的操作发给Celery
# #                   （http://www.celeryproject.org/）任务队列
# 1
#
# 1
# # -*- coding:utf-8 -*-
#
# # 使用Flask扩展
#
# #   扩展是帮助完成公共任务的包 如Flask-SQLAlchemy在Flask 中轻松使用SQLAlchemy
# 1
#
#
# 1
# # -*- coding:utf-8 -*-
#
# # 在SQLite中，数据库存在表和列中。在存储和调取数据之前需要先创建他们。
# #  项目Flask_project会把用户数据储存在user表中，把博客内容存储在post表中
# # 下面为创建一个文件存储于创建空表的SQL命令
# # '''
# # DROP TABLE IF EXISTS user;
# # DROP TABLE IF EXISTS post;
# # CREATE TABLE user (
# #   id INTEGER PRIMARY KEY AUTOINCREMENT,
# #   username TEXT UNIQUE NOT NULL,
# #   password TEXT NOT NULL
# # );
# # CREATE TABLE post (
# #   id INTEGER PRIMARY KEY AUTOINCREMENT,
# #   author_id INTEGER NOT NULL,
# #   created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
# #   title TEXT NOT NULL,
# #   body TEXT NOT NULL,
# #   FOREIGN KEY (author_id) REFERENCES user (id)
# # );
# # '''
# 1
#
#
# 1
#
# # ================================================
# # ubuntu 软件安装 命令
#
# # 	apt
#
# # 		定义
# # 			ubuntu软件管理器
#
#
# # 		apt命令
#
# # 			1 安装软件
#
# # 				sudo apt-get install xxxx 安装软件
#
# # 			2 删除软件
#
# # 				sudo apt-get remove xxxxx 删除软件
#
# # 				sudo apt-get autoremove 自动删除不需要的包
#
# # 			3 更新
#
# # 				sudo apt-get upgrade 更新已安装的包
#
# # 				sudo apt-get update 更新源
#
# #     系统命令
#
# #     	1 重启
#
# #     		reboot
#
#
# # ================================================
#
#
# # ================================================
# # nodejs ubuntu
#
# # 目的
# # 	安装最新nodejs
#
# # 思路
#
# # 	先用普通的apt工具安装低版本的node，然后再升级最新。
#
# # 安装过程
# # 	1 安装低版本nodejs
#
# # 		sudo apt-get update
# # 		sudo apt-get install nodejs
#
# # 		sudo apt install npm
#
# # 	2 更新淘宝的镜像
#
# # 		sudo npm config set registry https://registry.npm.taobao.org
#
# # 	3 查询更新镜像是否有效
#
# # 		sudo npm config list
#
# # 	4 更新npm 更新nodejs
#
# # 		sudo npm install n -g
# # 		sudo n stable
#
# # ================================================
#
#
# # ================================================
# # webpack
#
# # 文档
#
# # https://webpack.docschina.org/concepts/
#
#
# # 作用
#
# # 	实现js文件的打包压缩
#
# # 运行环境
#
# # 	nodejs环境
#
# # 使用
#
# # 	1 执行命令创建 package.json文件
#
# # 		sudo npm init
#
# # 	2 执行命令安装本地安装webpack
#
# # 		sudo npm install webpack --save-dev
#
# # 		检验安装是否成功
#
# # 			在 package.json文件中会多一项配置:
# # 			"devDependencies":{
# # 				"webpack" : "^2.3.2"
# # 3 执行命令安装本地安装webpack-dev-server
#
# # 	sudo npm install webpack-dev-server --save-dev
#
# # 4 执行命令安装本地安装webpack-cli
#
# # 	sudo npm i -D webpack-cli
#
# # 5 创建合理项目文件结构
#
# # 	创建目录
#
# # 		src/   存储项目的原文件
#
# # 		out/   存储项目要的输出文件
#
# # 		config/  配置文件
#
# # 6 配置webpack
#
# # 	config/目录下创建 webpack.config.js文件
#
# # 		初步的配置
#
# # 			const path = require('path'); #//为了使用nodejs的path.resoleve()方法导入的包
#
# # 			module.exports = {
# # 				entry:{
#
# # 					index: "./src/js/index.js"   #//希望处理文件的路径
# # 				},
# # 				output:{
#
# # 					filename: '[name].js',    #// 表示要输出的文件名称[name]是一个变量
# # 											#//表示输入的名字是什么输出的名字就是什么
# # 					path: path.resolve(__dirname, '../out')		#//配置文件输出路径
# # 												#// 使用的是nodejs方法,__dirname表示当前文件的绝对路径
#
# # 				},   //出口配置,配置成品文件的基本信息
# # 				mode:"development" 	#//模式可以不写,控制开发版本还是项目版本,默认生产模式
# # 			}
#
# # 7 配置快速启动命令
#
# # 	在package.json的scripts里,执行命令为 npm run 配置的命令
#
# # 	"scripts":{
# # 		"test":"echo \"Error:no test specified\" && exit 1",
# # 	启动服务的命令
# # 		"dev": "webpack-dev-server --open --config config/webpack.config.js" ,
# # 	打包命令
# # "命令名":"webpack --config config/webpack.config.js"
#
# # 说明:
# # 	当运行 npm run dev 命令时,就会执行 webpack-dev-server --open --config webpack.config.js命
# # 	令。其中 --config 是指向 webpack-dev-server 读取的配置文件路径,这里直接读取我们在上一步创
# # 	建的 webpack.config扣文件。--open 会在执行命令时自动在浏览器打开页面,默认地址是
# # 	127.0.0.1 :8080
#
# #  可选(配置ip和端口)
# # 	{
# # 	"scripts": {
# # 		"dev" : "webpack-dev-server --host 172.172.172.1 --port 8888 --open --configwebpack.config.js"
# # 	}
# # 	}
#
# # 8 SPA的入口
#
# # 	html文件中
#
# # 		<script src=/dist/main.js></script>
#
# # 9 配置其他加载器
#
# # 	css-loader
#
# # 	在webpack.config.js里
# # 		module.exports = {
# # 		module: {
# # 		rules: [
# # 		  {
# # 		    test: /\.css$/,
# # 		    use: [
# # 		      { loader: 'style-loader' },
# # 		      {
# # 		        loader: 'css-loader',
# # 		        options: {
# # 		          modules: true
# # 		        }
# #        		 }
#
#
# # ================================================
#
#
# # ================================================
# # matplotlib 模块
#
# # 作用
# # 	是一个python 2D 绘图库
#
# # 安装
#
# # 	python3 -m pip install -U matplotlib
# # ================================================
#
#
# # ================================================
# # visual studio code 编辑器
# # 1. 下载 deb包
# # 2. 安装
# # 	sudo dpkg -i  deb包
# # 3.运行
# # 	在命令行执行 code 既可
#
# # 配置中文
#
# # 	1 ctrl + shift + x 输入Chinese 安装中文插件
# # 	2 ctrl + shift + p 输入 lanauage
# # 		选择 Configure display lanaguage
# # 			将"locale":"zh-en"改成"locale":"zh-cn"
# # 配置vue
# # 	https://www.jianshu.com/p/454c3a7c5602
# # ================================================
#
#
# # ================================================
# # vuecli
#
# # package.json文件
#
# # 	创建项目
#
# # 		vue create 项目名
#
# # 		生成文件
#
# # 			package.json
# # 				{
# # 				"name": "test1",   项目名称
# # 				"version": "0.1.0",
# # 				"private": true,
# # 				"scripts": { 		执行脚本 简化命令操作
# # 					"serve": "vue-cli-service serve",
# # 					"build": "vue-cli-service build",
# # 					"lint": "vue-cli-service lint"
# # 				},
# # 				"dependencies": { 		依赖项
# # 					"element-ui": "^2.5.2",
# # 					"vue": "^2.5.21"
# # 				},
# # 				"devDependencies": { 	开发选项的插件
# # 					"@vue/cli-plugin-babel": "^3.3.0",
# # 					"@vue/cli-plugin-eslint": "^3.3.0",
# # 					"@vue/cli-service": "^3.3.0",
# # 					"babel-eslint": "^10.0.1",
# # 					"eslint": "^5.8.0",
# # 					"eslint-plugin-vue": "^5.0.0",
# # 					"vue-template-compiler": "^2.5.21"
# # 				},
# # 				"eslintConfig": { 	其他配置选项
# # 					"root": true,
# # 					"env": {
# # 					"node": true
# # 					},
# # 					"extends": [
# # 					"plugin:vue/essential",
# # 					"eslint:recommended"
# # 					],
# # 					"rules": {},
# # 					"parserOptions": {
# # 					"parser": "babel-eslint"
# # 					}
# # 				},
# # 				"postcss": { 	其他配置选项
# # 					"plugins": {
# # 					"autoprefixer": {}
# # 					}
# # 				},
# # 				"browserslist": [ 	其他配置选项
# # 					"> 1%",
# # 					"last 2 versions",
# # 					"not ie <= 8"
# # 				]
# # 				}
#
#
# # 	添加插件
# # 		在终端项目目录下命令
#
# # 			vue add 插件名添
#
# # 	项目本地的插件
#
# # 		使用本地的插件
#
# # 			1 在json
# # 			  "vuePlaugins": {
# #   				  "service":["my-commands.js"]
# #   				},
# # 			2 在项目目录下创建my-commands.js
#
# # 	插件的文件
#
# #	Preset 预编译的配置项
#
# # ================================================
#
#
# # ================================================
# # webpack
# #
# # 作用
# #
# # # 1 能够处理js文件的互相依赖关系
# # 2
# # 能够处理js的兼容问题, 把高级浏览器不识别的语法, 转为低级浏览器能正常识别的语法
# #
# # 使用
# # 1
# # 安装(推荐本地安装)
# #
# # 全局安装
# # npm
# # i
# # webpack - g
# # npm
# # i
# # webpack - cli - g
# # 本地安装
# # npm
# # install - -save - dev
# # webpack
# # npm
# # install - -save - dev
# # webpack - cli
# # 制定版本安装
# # npm
# # i
# # webpack @ x.x.x - g
# # 2
# # 初始化项目
# #
# # npm
# # init - y
# # 会生成一个package.json文件
# #
# # 3
# # 创建相关目录
# #
# # src / 存放原代码
# # css / css文件夹
# # js / js文件夹
# # images / 图片文件夹
# # index.html
# # 首页html
# # main.js
# # js入口文件
# # 在这里引入包和css文件
# # 举例导入jquery
# # 1
# # 安装jquery
# #
# # npm
# # i
# # jquery - S
# #
# # 会深成node_modules文件夹和package - lock.json文件
# #
# # 2
# # 导入jquery
# #
# # import $ from
# #
# # 'jquery'
# # 从node_modules文件中导入jquery用$变量来接受
# # 涉及知识点
# # import ** * from ** ** *是ES6中导入模块的方式
# # 注意
# # 此时浏览器不支持es6语法
# # import ** from **
# # 解决办法
# # 使用webpack进行处理文件, 见5
# #
# # 3
# # 写入jquery代码
# #
# # 4
# # 在html文件中通过script引入main.js文件
# #
# # 5
# # 使用webpack进行处理文件
# #
# # sudo
# # webpack. / src / main.js. / dist / bundle.js
# # 使用webpack
# # 处理文件main.js
# # 处理之后的文件放到dist文件目录下
# # 的bundel.js文件中, bundle.js通用文件名(推荐)
# # dist / 会生成bundle.js文件
# #
# # 涉及知识点
# # 语法
# # 第1种方法
# # webpack
# # 要打包的文件路径
# # 打包号的输出文件路径 + 文件名
# # 第2种方法
# # 进行文件的入口和出口的配置4
# # .2
# # 6
# # 使用生成的文件
# #
# # 将生成的文件在html中利用script引入
# #
# # dist / 项目发布的包
# #
# # 4
# # 进行配置文件
# #
# # 1
# # 项目目录下创建文件
# # webpack.config.js
# # 1
# # 获取当前项目目录路径
# # const
# # path = require('path')
# # 2
# # 配置入口和出口(为了改项目每次打包方便)
# # 通过Node中的模块操作, 向外暴露了一个配置对象
# # module.exports = {
# #                      entry: path.join(__dirname, './src/main.js')        入口, 表示钥使用webpack打包哪个文件
# # output: { 输出文件的相关配置
# # path :path.join(__dirname, './dist') 指定打包好的文件 ,输出哪个目录中去
# # filename :'bundle.js'	指定输出文件的名称
# # }
# # }
# # 3 执行命令自动打包
# #
# # webpack
# #
# # 做的事情
# # 1 webpack检测到未用命令形式制定入口和出口
# # 2 webpack会去根目录中 查找webpack.config.js配置文件;
# # 3 webpack会解析这个配置文件 ,导出配置对象
# # 4 wepack得到配置对象后 ,zhiidng入口和出口进行打包和构建
# # # ================================================
# #
# #
# #
# #
# # # ================================================
# # webpac k -de v -server
# #
# # 作用
# # 来实现自动打包编译的功能
# #
# # 安装
# # sudo npm i webpac k -cl i @3.
# # 0.0
# # sudo npm i webpac k -de v -serve r @2.1
# # 1.3 -g
# #
# # 使用
# # 使用方法和webpack一样
# # 命令
# # webpack - dev - server(若是全局安装执行此命令)
# #
# # 若本地安装, 需要做
#
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
#
# # ================================================
# # ================================================
#
1
#



