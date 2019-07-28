# -i https://pypi.douban.com/simple


1
# HTTP通讯过程

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

# web框架
#
#     核心功能: 实现路由和视图
#
#
# 框架的轻重

#     重量级框架 django
#     轻量级框架 flask Tornado(自由灵活)
#

# Flask
#
#     1 介绍
#
#         flask框架核心是Werkzeug和Jinja2
#         flask.pocoo.org/docs/0.11/
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
#
#     3 虚拟环境创建
#
#         查看 06-操作系统笔记.py
#
#         1 收集虚拟环境中的安装包
#             pip3 freeze > requirements.txt
#         2 安装收集的所有安装包
#             pip3 install -r requeirements.txt
#
#     4 flask基本程序
#
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
#
#     5 应用参数
#
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
#
#     6 配置相关
#
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
#
#     7 路由相关
#
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

        # 8 request
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
        #
        #
        # 9 获取上传文件并保存
        #
        #     # 得到的是类似文件句柄类型
        #     a = request.files.get('xx')
        #     # 保存文件
        #     a.save("路径")
        #
        # 10 abort函数
        #
        #     from flask import abort, Response
        #     # 终止视图执行 返回给前端信息
        #
        #     # 返回状态码, 必须是标准的http状态码
        #     abort(404)
        #
        #     # 返回信息
        #     abort(Response('xx'))
        #
        # 11 自定义异常处理
        #
        #     @app.errorhandler(404)
        #     def handle_404_error(err):
        #         return '40411'
        #
        # 12 响应信息处理
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
        #
        # 13 返回json数据
        #
        #     from flask import jsonify
        #
        #     a = {"a":1}
        #     return jsonify(a)
        #
        # 14 cookie的使用
        #
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
        #
        # 15 session
        #
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
        #
        # 16 请求钩子
        #
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
        #
        # 17 请求上下文和应用上下文
        #
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

        # 18 Flask-Script扩展命令行工具
        #
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
        19 jinja2 模板

            1 变量
                {{ name }}

            2 渲染模板

                from flask import render_template

                return render_template("xx.html")

                传递参数

                    return render_template("index.html",a=1)
                    或
                    return render_template("index.html",**a)

            3 模板中获取值

                data = {
                    "a":"aaa",
                    "b":1,
                    "c":{"cccc":4},
                    "d":[1,2,3,4],
                    "e":0
                }
                return render_template("index.html",**data)

                {{c["cccc"]}}
                {{c.cccc}}
                {{d}}
                {{d[e]}}

                {{ d[0]+d[1] }} # 数字加法, 字符串加法

            4 过滤器

                {{ '<p>sss</p>'|safe }} # 禁止转义

                {{ " flask world "|trim|upper }} # 可链式
                ....

                1 列表过滤器

                    取第一个元素
                    {{ [1,2,3,4,5]|first }}

                    取最后一个元素
                    {{ [1,2,3,4,5]|last }}

                    获取列表长度
                    {{ [1,2,3,4,5]|length }}

                    列表求和
                    {{ [1,2,3,4,5]|sum }}

                    列表排序
                    {{ [1,2,3,4,5]|sort }}

                2 自定义过滤器

                    方式1

                        1 定义函数
                            def a(li):

                                return li[::2]
                        2 注册过滤器
                            app.add_template_filter(a, "xx") # 参数1 函数 参数2 模板中使用的名字

                        3 模板使用
                            {{ listxx|xx }}

                    方式2

                    1 定义函数, 用装饰器注册并命名

                    @app.template_filter("xx")
                    def a(li):
                        return li[::2]