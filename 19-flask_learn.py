# -i https://pypi.douban.com/simple



HTTP通讯过程

    tcp传输
        浏览器---发起HTTP请求(请求报文 请求头 请求体) ---> django--->
        返回HTTP响应(响应报文 起始行 响应头 响应体)--->浏览器

    django做的事情
        接收从前端发送过来的请求
        解析http报文
        进行路由分发
        根据用户请求的url
        执行对应的视图函数
        将视图函数返回值打包成http响应报文
        借助刚才建立好的tcp链接将响应回传


web框架

    核心功能: 实现路由和视图


框架的轻重

    重量级框架 django
    轻量级框架 flask Tornado(自由灵活)


Flask

    1 介绍
        flask框架核心是Werkzeug和Jinja2
        flask.pocoo.org/docs/0.11/
    2 扩展包

        Flask-SQLalchemy 操作数据库
        Flask-migrate 管理迁移数据库
        Flask-Mail 邮件
        Flask-WTF 表单
        Flask-script 插入脚本
        Flask-Login 认证用户状态
        Flask-RESTful 开发REST API的工具
        Flask-Boostrap 集成前段Twitter Bootstrap框架
        Flask-Moment 本地化日期和时间

    3 虚拟环境创建

        查看 06-操作系统笔记.py

        1 收集虚拟环境中的安装包
            pip3 freeze > requirements.txt
        2 安装收集的所有安装包
            pip3 install -r requeirements.txt

    4 flask基本程序

        from flask import Flask

        # 创建flask应用对象
        # __name__当前模块名字：
        #       flask以这个模块所在的目录为总目录,
        #       默认这个目录中的static为静态目录,
        #       templates为模板目录

        app = Flask(__name__)


        @app.route("/")
        def index():
            return 'hello'


        if __name__ == '__main__':
            # 启动flask程序
            app.run()