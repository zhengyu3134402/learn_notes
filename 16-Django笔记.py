
# # =================================================
# Django

    # 1.概念
        1
        # 模式
            # Model(模型)：负责业务对象与数据库的对象(ORM) (models.py)
            # Template(模版)：负责如何把页面展示给用户 (templates)
            # View(视图)：负责业务逻辑，并在适当的时候调用Model和Template (urls.py, views.py)
        1
    # 2.安装
        1
        # pip3 install django==1.11.3
        # pip3 install pymysql  为了连接mysql数据库
        1
    # 3.配置
        1
        # 1 创建项目
            # django-admin startproject 项目名

        # 2 配置与数据库连接

            # 1 settings.py文件中
                # DATABASES = {
                # "default": {
                #     "ENGINE": "django.db.backends.mysql",
                #     "NAME": "你的数据库名称",  # 需要自己手动创建数据库
                #     "USER": "数据库用户名",
                #     "PASSWORD": "数据库密码",
                #     "HOST": "数据库IP",
                #     "POST": 3306
                #     }
                # }
            # 2 进入mysql创建数据库（数据库名和配置的名字要一样）
                # create database 数据库名 charset=utf8;

            # 3 注册连接数据库使用模块（__init__.py）
                # import pymysql
                # pymysql.install_as_MySQLdb()

        # 3.创建注册应用

            # 1 创建
                # python3 manage.py startapp  应用名
            # 2 注册(settings.py)
                # INSTALLED_APPS = [
                #     'django.contrib.admin',
                #     ......
                #     'yingyong1.apps.Yingyong1Config',  # 写全的注册方式 在创建应用的apps.py文件中
                # ]

        # 4 模板路径配置（settings.py）

            # 1 配置模板
                # TEMPLATES = [
                # {
                #     'DIRS': [os.path.join(BASE_DIR, 'templates')],
                # }
            # 2 创建模板目录
                # templates

        # 5 静态文件配置

            # 1 settings.py
                # STATIC_URL = '/static/'  # HTML中使用的静态文件夹前缀
                # STATICFILES_DIRS = [
                    # os.path.join(BASE_DIR, "static"),  # 静态文件存放位置
                #]
            # 2 创建static目录
                # static

        # 6 （可选）配置使用模板语法jinja2

            # 1 安装
                # pip3 install jinja2
            # 2 配置
                # 1 settings.py同目录下创建文件backends.py内容为
                    # import sys
                    #
                    # from django.template.backends import jinja2 as jinja2backend
                    # from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy
                    # from django.template import TemplateDoesNotExist, TemplateSyntaxError
                    # from django.utils.module_loading import import_string
                    # import jinja2
                    # import six
                    #
                    #
                    # class Jinja2Backend(jinja2backend.Jinja2):
                    #     def __init__(self, params):
                    #         self.context_processors = [
                    #             import_string(p)
                    #             for p in params['OPTIONS'].pop('context_processors', [])
                    #         ]
                    #         super(Jinja2Backend, self).__init__(params)
                    #
                    #     def from_string(self, template_code):
                    #         return Template(
                    #             self.env.from_string(template_code), self.context_processors)
                    #
                    #     def get_template(self, template_name):
                    #         try:
                    #             return Template(
                    #                 self.env.get_template(template_name), self.context_processors)
                    #         except jinja2.TemplateNotFound as exc:
                    #             six.reraise(TemplateDoesNotExist, TemplateDoesNotExist(exc.args),
                    #                         sys.exc_info()[2])
                    #         except jinja2.TemplateSyntaxError as exc:
                    #             six.reraise(TemplateSyntaxError, TemplateSyntaxError(exc.args),
                    #                         sys.exc_info()[2])
                    #
                    #
                    # class Template(jinja2backend.Template):
                    #
                    #     def __init__(self, template, context_processors):
                    #         self.template = template
                    #         self.context_processors = context_processors
                    #
                    #     def render(self, context=None, request=None):
                    #         if context is None:
                    #             context = {}
                    #         if request is not None:
                    #             context['request'] = request
                    #             lazy_csrf_input = csrf_input_lazy(request)
                    #             context['csrf'] = lambda: lazy_csrf_input
                    #             context['csrf_input'] = lazy_csrf_input
                    #             context['csrf_token'] = csrf_token_lazy(request)
                    #             for cp in self.context_processors:
                    #                 context.update(cp(request))
                    #             # print(context)
                    #         return self.template.render(context)
                # 2 项目目录下创建jinja2_env.py文件，内容为
                    # from django.contrib.staticfiles.storage import staticfiles_storage
                    # from django.urls import reverse
                    #
                    # from jinja2 import Environment
                    #
                    # def environment(**options):
                    #     env = Environment(**options)
                    #     env.globals.update({
                    #         'static': staticfiles_storage.url,
                    #         'url': reverse,
                    #     })
                    #     return env
                # 3 django settings项目中更改
                    # CONTEXT_PROCESSORS = [
                    #     'django.template.context_processors.debug',
                    #     'django.template.context_processors.request',
                    #     'django.contrib.auth.context_processors.auth',
                    #     'django.contrib.messages.context_processors.messages',
                    # ]
                    #
                    # TEMPLATES = [
                    #     {
                    #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    #         'DIRS': [],
                    #         'APP_DIRS': True,
                    #         'OPTIONS': {
                    #             'context_processors': CONTEXT_PROCESSORS, },
                    #     },
                    # {
                    #         'BACKEND': 'django.template.backends.jinja2.Jinja2',
                    #         'DIRS': [os.path.join(BASE_DIR, 'templates')],
                    #         'APP_DIRS': False,
                    #         'OPTIONS': {
                    #             'context_processors': CONTEXT_PROCESSORS,
                    #             'environment': 'jinja2_env.environment'
                    #         },
                    #     },
                    #
                    # ]

        # 7 配置urls.py

            # 1 项目urls.py
                # from django.conf.urls import include
                # urlpatterns = [
                #     url(r'^', include('app.urls')),
                # ]
            # 2 在应用的目录下创建urls.py
                # from django.conf.urls import url
                # urlpatterns = [
                #     xxx
                # ]
        # 8 运行django
            # python manage.py runserver
        # 9 settings.py中其他配置
            # 1 是否开启URL访问地址后面不为/跳转至带有/的路径配置
                # APPEND_SLASH=True
        1
    # 4.路由系统
        1
        # 1 概念
            # 本质是URL与要为该URL调用的视图函数之间的映射表
        # 2 配置
            # 1 url方法     from django.conf.urls import url
            # 2 映射list    urlpatterns = []
            # 3 url的参数   url(正则表达式，view视图函数，参数，别名)

        # 3 捕获参数
            # 1 捕获的参数永远都是字符串
            # 2 匹配顺序按列表从左到右的顺序
            # 3 想要从url中捕获值，想要捕获值得部分必须加（）
            # 4 正则部分建议加上r
            # 5 url部分前面不需要加/

        # 4 路由参数分组命名匹配
            # 1 概念 分组命名匹配的正则表达式组来捕获URL中的值并以关键字参数形式传递给视图
            # 2 ()            # 捕获参数
            # 3  (?P<name>.*)  # 写在路由匹配列表中,url的格式 .*是正则表达式
            # 3 name          # cvb方法中要有self,request之外的另一个参数xx接收url捕获的值
            #
            # 浏览器-》 http://127.0.0.1:8000/group_name_rep/1111/
            # 路由列表-》 url(r'^group_name_rep/(?P<name>.*)/$', views.GroupNameRep.as_view())
            # views.py-》
            #     class GroupNameRep(View):
            #         def get(self,request, name):
            #             return HttpResponse(name)

        # 5 路由分组命名匹配设定默认值
            # 1 默认值   在cvb函数中request参数后指定
            # 2 url      带默认参数url匹配和不带参数url匹配要分开写
            #
            #             url(r'a/(?P<name>\d+)', views.A.as_view()),
            #
            # class A(View):
            #     def get(self, request, name="我是设定的默认参数"):
            #         return HttpResponse(name)


        # 6 命名URL和URL反向解析
            # 1 name            # 命名url url(r'^a/$', views.A.as_view(), name='a')
            # 2 命名url的模板引用    # {% url 'app1:a' %}    # jinja2语法 可传递参数
            # 3 reverse方法
                # from django.urls import reverse
                # reverse('app1:a', args=("2018", )) # 可传递参数
        # 7 命名空间
            # 1 作用
                # 即使不同的APP使用相同的URL名称，URL的命名空间模式也可以让你唯一反转命名的URL。
            # 2 创建命名空间
                # 1 项目下的urls.py中
                    # url(r'', include('app.urls,', namespace='app')),
                # 2 标识命名空间名（应用中的urls.py ）
                    # app_name = 'app'
                    # urlpatterns = [...]
            # 3 使用
                # 1 命名空间的模板使用
                    # {% url 'app1:b' %}
                # 2 命名空间的视图使用
                    # reverse('app:set_url_name') 可带参数 reverse('app01:detail', kwargs={'pk':11})
        1

    # 5 中间件
        1
        # 1 概念
            # Django的请求和响应的框架级别的钩子。它是一个轻量、低级别的插件系统，
            # 用于在全局范围内改变Django的输入和输出。每个中间件组件都负责做一些特定的功能。

        # 2 位置

            # setting文件中MIDDLEWARE配置项是一个列表，列表中是一个个字符串，
            # 这些字符串其实是一个个类，也就是一个个中间件。

        # 3 使用
            # 1 中间件的5中方法
                # process_request(self,request)
                    # 视图函数接受请求前
                # process_view(self, request, view_func, view_args, view_kwargs)
                    # 在process_request之后，视图函数之前执行的
                # process_template_response(self,request,response)
                    # 视图函数执行完成后立即执行，但是它有一个前提条件，那就是视图函数返回的对象有一个render()方法
                # process_exception(self, request, exception) #
                    # 视图函数中发生错误执行
                # process_response(self, request, response) #
                    # 视图函数响应之后 需要return response
            # 2 中间件的返回值
                # 返回值可以是None或一个HttpResponse对象，如果是None，
                # 则继续按照django定义的规则向后继续执行，如果是HttpResponse对象，
                # 则直接将该对象返回给用户。
            # 3 创建中间件

                # 1 导入类MiddlewareMixin
                # 2 创建类继承MiddlewareMixin
                # 3 使用中间件的方法
                # 4 注册创建的中间件settings的MIDDLEWARE中
                    # from django.utils.deprecation import MiddlewareMixin
                    #
                    # class Md(MiddlewareMixin):
                    #     def process_request(self, request):
                    #         print('我是Md')

            # 4 多个中间的顺序

                # 1 process_request
                    # 按照中间件的注册 顺序执行 ，然后执行视图函数

                # 2 process_response
                    # 先执行视图函数按照中间件注册的 倒叙执行

                # 3 process_view
                    # 按照注册循序， 执行相应的视图函数
                    # 如果return一个HttpResponse对象，则不执行视图函数
                # 4 process_exception
                    # 按照注册顺序倒叙执行
                    # 如果return None 交给下一个中间执行
                    # 如果return HttpResquest随想 则执行process_response方法
                # 5 process_template_response
                    # 视图函数执行完之后，立即执行了中间件的process_template_response方法，顺序是倒序

            # 5 中间件的总流程

                # 1 请求到达中间件之后，先按照正序执行每个注册中间件的process_reques方法，
                # 2 如果process_request方法返回的值是None，就依次执行
                # 3 如果返回的值是HttpResponse对象，不再执行后面的process_request方法，
                    # 而是执行当前对应中间件的process_response方法，将HttpResponse对象返回给浏览器。
        1

    # 6 Form
        1
        # 1 概念

            # 1 生成页面可用的HTML标签
            # 2 对用户提交的数据进行校验
            # 3 保留上次输入内容
        # 2 使用
            # 1 创建表单类
                # from django import forms
                # class RegForm(forms.Form)
                #     user = forms.CharField(label="xxx", 过滤条件)

            # 2 创建xx.html模板
            # 3 通过视图函数将表单类传入模板中
                # class A(View):
                #     def get(self, request):
                #         a = F()
                #         return render(request, 'a.html', {"form":a})

            # 4 模板中使用表单类
                # {{ a.as_p }} 根据类中定义自动生产多个p标签
                # {{ a.user }}  生成生产字段的input框
                # {{ a.user.label }} 生成类中指定label的内容
                # {{ a.user.errors }} 生成字段的所有错误信息
                # {{ a.user.errors.0 }} 生产字段的错误信息第一个
                # {{ a.errors }}  生产所有字段的错误信息
                # 生成的标签中自带前端校验规则，若想自定义校验规则，form中添加 novalidate属性去掉原校验规则）
            # 5 表单类的方法
                # 1 cleaned_data
                    # 校验成功之后才会返回结果字典类型{label标签名：用户输入信息}

            # 6 表单类的字段和校验参数
                # 1 django内置
                    # min_length = 6  最小长度为6
                    # required=True   是否允许为空
                    # widget = xx     Html插件
                    # label = xx      label标签显示内容（如果不加和字段变量名字一样）
                    # help_text=''    帮组信息（在标签旁边显示）
                    # error_message = xx  错误提示信息
                        # error_messages = {          # 重写错误提示信息
                        #     "required":"不能为空",
                        #     "invalid":"格式错误",
                        #     "min_length":"用户名最短x位置"
                        #             }
                    # validators = [],  自定义验证规则
                    # localize = False  是否支持本地化
                    # disabled = False  是否可以编辑
                    # label_suffix = xx  label内容后缀
                    # initial="xx"  输入框中的默认值
                    #
                    # CharField
                    #     max_length = None  最大长度
                    #     min_length = None  最小长度
                    #     strip = True        是否移除用户输入的空白
                    # IntegerField
                    #     max_value = None    最大值
                    #     min_value = None    最小值
                    # FloatField(IntegerField)
                    #
                    # DecimalField
                    #     max_value=None      最大值
                    #     min_value=None      最小值
                    #     max_digits=None     总长度
                    #     decimal_places=None 小数位长度
                    # BaseTemporalField
                    #     input_formats=None  时间格式化
                    #
                    # DateField(BaseTemporalField)  格式：xxxx-xx-xx
                    # TimeField(BaseTemporalField)  格式：xx：xx
                    # DateTimeField(BaseTemporalField) 格式：xxxx-xx-xx xx:xx
                    #
                    # DurationField(Field)    时间间隔：%d %H:%M:%s.%f
                    #
                    # RegexField(CharField)
                    #     regex,              自定义正则表达式
                    #     max_length=None,    最大长度
                    #     min_length=None，   最小长度
                    #     error_message=None，忽略，错误信息使用error_messages=
                    # ........
                # 2 自定义校验条件
                    # 1 自定义校验条件,使用正则

                        # from django.core.validators import RegexValidator

                        # a = forms.CharField(label="手机号",
                                        # validators=[RegexValidator(r'^1[3-9]\d{9}$', '错误提示')
                                        # ])
                    # 2 自定义校验条件,使用函数
                        # from django.core.exceptions import ValidationError

                        # def a(value):
                            # 写校验条件
                            # 若果不符合报错
                            # raise ValidationError('错误提示')

                        # a = forms.CharField(label="手机号", validators=[a])

                    # 3 自定义校验条件, 使用钩子函数
                        # 1 局部钩子（对一个字段进行校验）
                            # def clear_字段名(self):
                                # value = self.cleaned_data.get("字段名")
                                # if re.match(r'正则', value)
                                # return value
                                # raise validationError('错误提示信息')
                    # 2 全局钩子（可以对所有字段进行校验）
                        # def clean(self):  # 所有字段校验后拿到的数据
                            # 条件判断
                            # 如果条件为true：
                                # return self.cleaned_date
                            # self.add_error('字段名','错误提示')    # 吧错误放到了字段级别的错误提示中
                            # raise ValidationEror('错误提示信息')   # 错误提示放到了所有错误提示中

            # 7 form字段类型
                # from django.forms import widgets
                # 1 text类型（默认）
                    # name = forms.CharField(xx)

                # 2 password类型
                    # widget=widgets.PasswordInput
                    # 例子
                    # user = forms.CharField(label='用户名', widget=widgets.PasswordInput)

                # 3 下拉框
                    # a = forms.ChoiceField(choices=((1,"男"),(2,"女")))

                # 4 radio框
                    # widget = widgets.RadioSelect
                # 5 多选框
                    # widget = widgets.SelectMultiple
                # 6 checkbox单选框
                    # widget=widgets.CheckboxInput
                # 7 checkbox多选框
                    # widget=widgets.CheckboxSelectMultiple
                # 8 choice字段的实时更新
                    # 在使用选择标签时，需要注意choices的选项可以配置从数据库中获取，
                    # 但是由于是静态字段 获取的值无法实时更新，需要重写构造方法从而实现choice实时更新。

                    # 方式一：

                    # from django.forms import Form
                    # from django.forms import widgets
                    # from django.forms import fields
                    #
                    # class MyForm(Form):

                        # user = fields.ChoiceField(
                        # choices=((1, '上海'), (2, '北京'),),
                        # initial=2,
                        # widget=widgets.Select
                        # )

                        # def __init__(self, *args, **kwargs):
                        # super(MyForm,self).__init__(*args, **kwargs)
                        # self.fields['user'].choices = ((1, '上海'), (2, '北京'),)
                        # 或
                        # self.fields['user'].choices = models.Classes.objects.all().values_list('id','caption')

                    # 方式二：

                    # from django import forms
                    # from django.forms import fields
                    # from django.forms import models as form_model

                    # class FInfo(forms.Form):
                        # authors = form_model.ModelMultipleChoiceField(queryset=models.NNewType.objects.all())  # 多选
                        # authors = form_model.ModelChoiceField(queryset=models.NNewType.objects.all())  # 单选
        1

    # 7 用户认证
        1
        # 1 概念
            # django内置认证系统
            # 默认使用 auth_user 表来存储用户数据
        # 2 使用
            # (使用之前要对数据进行python manage.py migrate 让数据生产表auth_user表，要不然会报错)
            # (向默认的auth_user表中插入数数据  python manage.py createsuperuser 测试用，以后可自定义表存储用户数据 )

            # auth模块的方法
                # 1 authenticate
                    # 会去数据库auth_user表中检测用户是否存在，如果存在返回对象，不存返回None
                    # from django.contrib.auth import authenticate
                    # def post(self, request):
                        # username = request.POST.get("user_name")
                        # password = request.POST.get("user_pwd")
                        # a = authenticate(request, username=username, password=password) #
                        # print(a)
                        # return HttpResponse('haha')
                # 2 login
                    # 记录登录状态，本质上在后端为该用户生产相关session数据
                    # from django.contrib.auth import login
                    # login(request, user)

                # 3 logout(request)
                    # 当亲请求的session信息全部清除，即使没有session信息也不会报错


                # 4 is_authenticated()
                    # 用来判断当前请求是否通过了认证
                        # request.user.is_authenticated()


                # 5 login_required
                    # 使用装饰器验证当前状态是否是登录状态
                    # from django.contrib.auth.decorators import login_required
                    # from django.utils.decorators import method_decorator

                    # class A(View):
                    #     @method_decorator(login_required)
                    #     def get(self, request):
                    #         return HttpResponse('用户处于登录状态')
                    # 如果处于非登录状态 会自动跳转到settings.py中的
                    # LOGIN_URL = '/自定义url/'定义的参数路径


                # 6 create_user()
                    # 创建普通新用户，必要参数（usename,password）

                    # from django.contrib.auth.models import User

                    # User.objects.create_user(username='xx', password='xxx',...)
                        # User的其他属性
                            # User对象属性：username， password
                            # is_staff ： 用户是否拥有网站的管理权限.
                            # is_active ： 是否允许用户登录, 设置为 False，可以在不删除用户的前提下禁止用户登录。

                # 7 create_superuser()
                    # 创建超级新用户，必要参数（username, password）和创建普通用户一样

                # 8 check_password()
                    # 检验密码是否正确，必要参数密码
                    # request.user.check_password(‘密码’) 检验用户密码是否正确



                # 9 set_password()
                    # 修改密码，必要参数 新密码
                    # 保存密码
                    # request.user.set_password(password='新密码')
                    # request.user.save()

        # 3 扩展用户存储的信息
            # 1 创建新的模型(必须有个字段带有unique属性)
                # from django.contrib.auth.models import AbstractUser
                # class A(AbstractUser):
                    # phone = models.CharFiled(max_length=11, unique=True)
                    # def __str__(self):
                         # reutrn self.username
            # 2 注册类
                # settings.py中AUTH_USER_MODEL = '应用名.创建的类名'

            # 3 生成表
                # python manage.py makemigrations(如果执行此命令是次项目的第一次，没有问题，
                                              # 如果不是第一次，会出现问题，删除数据库更新记录等会解决此问题)
        1

    # 8 缓存
        1
        # 1 概念
            # 把数据先保存在某个地方，下次再读取的时候不用再去原位置读取
            # 不经常变换的数据应设置缓存
        # 2 配置
            # 1 缓存类型
                # 内存，文件，数据库 Memcache
            # 2 配置
                # 1 配置缓存到内存
                    # settings文件中
                        # CACHES = {
                            # 'default': {
                            # 'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # 缓存的位置，django所在程序的内存当中
                            # 'LOCATION': 'unique-snowflake',     # 在内存当中的唯一标识
                            # 'TIMEOUT': 300,          # 缓存超时时间（默认300，None表示永不过期，0表示立即过期）
                            # 'OPTIONS':{
                                # 'MAX_ENTRIES': 300,  # 最大缓存个数（默认300）
                                # 'CULL_FREQUENCY': 3, # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
                                    # },

                                # }
                            # }


                # 2 配置缓存到文件中

                    # settings文件中修改原缓存的配置
                    # CACHES = {
                        # 'default': {
                        # 'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',  # 缓存到文件中
                        # 'LOCATION': 'xx/xx',     # 指定缓存文件的路径位置
                        # 'TIMEOUT': 300,          # 缓存超时时间（默认300，None表示永不过期，0表示立即过期）
                            # 'OPTIONS':{
                                # 'MAX_ENTRIES': 300,  # 最大缓存个数（默认300）
                                # 'CULL_FREQUENCY': 3, # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
                            # },
                        #
                        # }
                    # }

                # 3 配置缓存到数据库
                    # 1 settings.py中配置
                        # CACHES = {
                            # 'default': {
                                # 'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
                                # 'LOCATION': '数据库表', # 数据库表
                            # }
                        # }

                    # 2 执行创建表命令
                        # python manage.py createcachetable

                # 4 配置缓存到Memcache（使用python-memcached模块，类似redis的内存数据库）

                    # 配置缓存到另一台服务器服务器内存中
                    # CACHES = {
                    # 'default': {
                            # 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
                            # 'LOCATION': '127.0.0.1:11211', # 另一台服务器的地址
                        # }
                    # }


                    # CACHES = {
                        # 'default': {
                            # 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
                            # 'LOCATION': 'unix:/tmp/memcached.sock',
                        # }
                    # }

                # 5 配置缓存到多台服务器服务器内存中（分布式）
                    # CACHES = {
                        # 'default': {
                            # 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
                            # 'LOCATION': [
                            # '172.19.26.240:11211',
                            # '172.19.26.242:11211',
                            # ]
                        # }
                    # }


        # 3 使用

        # 1 全站使用缓存
            # 1 在settings中配置缓存
                # MIDDLEWARE = [
                    # 'django.middleware.cache.UpdateCacheMiddleware',    # 如果缓存不存在将会保存至缓存
                    # 其他中间件...
                    # 'django.middleware.cache.FetchFromCacheMiddleware', # 获取内容返回给用户
                # ]

                # CACHE_MIDDLEWARE_ALIAS = ""
                # CACHE_MIDDLEWARE_SECONDS = ""   # 配置缓存的时间
                # CACHE_MIDDLEWARE_KEY_PREFIX = ""

        # 2 局部模板使用缓存
            # 1 模板中引入 cache
                # ｛% load cache %｝
            # 2 使用缓存
                # {% cache 秒 缓存的key(随意) %}
                    # 缓存的内容
                # {% endcache %}

            # 3 单独视图的缓存
                # 方法一 在视图上使用缓存
                    # 1 导入装饰器cache_page
                        # from django.views.decorators.cache import cache_page
                    # 2 应用到视图之上，视图中的变量就会缓存
                        # @cache_page(秒)
                        # def 视图名(request)
                # 方式二 在路由上使用缓存urls.py中
                    # 1 导入装饰器cache_page
                        # from django.views.decorators.cache import cache_page
                    # 2 应用到路由之中
                        # url(r'', cache_page(秒)(视图名))
        1

    # 9 序列化
        1
        # 1 使用
            # 1 serializers（了解）
                # 缺点：传递数据的时候，会把数据库中的表名也传过去
        # 2 json(推荐使用)
            # 1 从数据库取出的内容进行序列化
                # 从数据库从取去的类型是queryset类型
                # a = xx.objects.all().value('字段1', '字段2'。。。)
                # 序列化结果 = json.dumps(list(a))
            # 2 存储的数据类型含有不能序列化的类型如：datetime类型
                # 1 解决方法
                    # 本质的处理将datetime类型转换成字符串类型再进行序列化
                        # 1 导入JSONEncoder模块
                        # 2 创建类继承JSONEncoder
                        # 3 重构 default方法
                        # 4 使用创建的类进行转换

                        # from json import JSONEncoder
                        # class A(JSONEncoder):
                            # def default(self, field):   # 对数据字段进行判断
                                # if isinstance(field, datetime):
                                    # return field.strftime('%y-%m-%d %H:%M:%S') # 把datetime类型变成字符串
                                # elif isinstance(field, date):
                                    # return field.strftime('%Y-%m-%d') 把date类型转换成字符串
                                # else:
                                    # return JSONEncoder.default(self, field)  # 其他类型进行默认转换
                                # json.dumps(data, cls=A)
        1

    # 10 信号
        1
        # 1 概念
            # 是django中预留的对象，达到特定条件后自动触发
            # 中间件掌管进和出，信号遍布django
        # 2 内置信号

            # Model signals
                # pre_init                    # django的model执行其构造方法前，自动触发
                # post_init                   # django的model执行其构造方法后，自动触发
                # pre_save                    # django的model对象保存前，自动触发
                # post_save                   # django的model对象保存后，自动触发
                # pre_delete                  # django的model对象删除前，自动触发
                # post_delete                 # django的model对象删除后，自动触发
                # m2m_changed                 # django的model中使用m2m字段操作第三张表（add,remove,clear）前后，自动触发
                # class_prepared              # 程序启动时，检测已注册的app中modal类，对于每一个类，自动触发
            # Management signals
                # pre_migrate                 # 执行migrate命令前，自动触发
                # post_migrate                # 执行migrate命令后，自动触发
            # Request/response signals
                # request_started             # 请求到来前，自动触发
                # request_finished            # 请求结束后，自动触发
                # got_request_exception       # 请求异常后，自动触发
            # Test signals
                # setting_changed             # 使用test测试修改配置文件时，自动触发
                # template_rendered           # 使用test测试渲染模板时，自动触发
            # Database Wrappers
                # connection_created          # 创建数据库连接时，自动触发
        # 3 使用信号
            # 方法1
                # 1 位置
                    # 写在settings.py目录中的__init__文件中
                # 2 在文件中导入信号相关模块（一共就这么多，用哪个导入哪个就行）
                    # from django.core.signals import request_finished
                    # from django.core.signals import request_started
                    # from django.core.signals import got_request_exception
                    #
                    # from django.db.models.signals import class_prepared
                    # from django.db.models.signals import pre_init, post_init
                    # from django.db.models.signals import pre_save, post_save
                    # from django.db.models.signals import pre_delete, post_delete
                    # from django.db.models.signals import m2m_changed
                    # from django.db.models.signals import pre_migrate, post_migrate
                    #
                    # from django.test.signals import setting_changed
                    # from django.test.signals import template_rendered
                    #
                    # from django.db.backends.signals import connection_created

                # 3 定义一个方法
                    # def a(sender, **kwargs):  # 参数sender为触发该信号的相关信息和操作
                    # ...

                # 4 指定信号触发之后使用的函数(举例子：post_save)
                    # post_save.connect(a)

            # 方法2
                # 1 位置
                    # 写在settings.py目录中的__init__文件中
                # 2 在文件中导入信号相关模块（一共就这么多，用哪个导入哪个就行）
                    # from django.core.signals import request_finished
                    # from django.core.signals import request_started
                    # from django.core.signals import got_request_exception
                    #
                    # from django.db.models.signals import class_prepared
                    # from django.db.models.signals import pre_init, post_init
                    # from django.db.models.signals import pre_save, post_save
                    # from django.db.models.signals import pre_delete, post_delete
                    # from django.db.models.signals import m2m_changed
                    # from django.db.models.signals import pre_migrate, post_migrate
                    #
                    # from django.test.signals import setting_changed
                    # from django.test.signals import template_rendered
                    #
                    # from django.db.backends.signals import connection_created

                # 3 定义一个方法
                    # def a(sender, **kwargs):  # 参数sender为触发该信号的相关信息和操作
                    # ...

                # 4 导入receiver模块
                    # from django.dispatch import receiver

                # 5 将receiver装饰在定义的方法之上
                    # @receive(触发的信号)
                    # def a(sender, **kwargs):
                    # ....

        # 4 指定发送者（sender=xx）
            # 指定哪个对象能够触发该信号
            # 利用方法的写法
                # @receiver(pre_save, sender=MyModel)
                # def my_handler(sender, **kwargs):
                # ...
        # 5 自定义信号
            # 1 创建信号
                # import django.dispatch
                # pizza_done = django.dispatch.Signal(providing_ags=['a', 'b'])
            # 2 注册创建的信号（settings同目录下__init__.py）

                # from xxx import pizza_done
                # @receiver(pizza_done)
                # def xxxx(sender, **kwargs):
                    # ......
            # 3 触发信号
                # 想在哪触发信号 就导入要触发的信号
                # from xxx import pizza_done
                # pizza_done.send(sender='haha', a='xx',b='xx') # 触发信号(可以少传参数)
        1




# --------------------------------------------------
# Django admin
#
#     1 概念
#         基于 web 的管理工具。
#         Django 自动管理工具是 django.contrib 的一部分
#         django.contrib是一套庞大的功能集，它是Django基本代码的组成部分。
#         在项目的 settings.py 中的 INSTALLED_APPS 看到它：
#         INSTALLED_APPS = [
#             'django.contrib.admin',
#             。。。
#         ]
#     2 使用
#         1 配置（一般django进行默认配置）
#             1 urls.py中导入url模块，admin模块
#                 from django.conf.urls import url
#                 from django.contrib import admin
#             2 urls.py中设置参数
#                 urlpatterns = [
#                     url(r'^admin/', admin.site.urls),
#
#                 ]
#         2 创建管理员账号
#             python manage.py createsuperuser
#         3 进入admin页面
#             http://127.0.0.1:8000/admin/
#
#         4 注册数据模型
#             应用下的admin.py中注册
#                 admin.site.register(模型类)
#
#     3 扩展
#         1 基本流程定制~注册
#             1 定制admin基本规则
#                 1 创建类继承admin.ModelAdmin
#                     class Make(admin.ModelAdmin):
#                 2 设置字段显示
#                     list_display = ('xx','xxx')
#                 3 注册定制
#                     admin.site.register(kk, Make)
#             2 注册定制的两种方式方式
#                 1
#                     admin.site.register(xxx, aa)
#                 2
#                     @admin.register(类模型)
#                     创建自定义类
#         2 定制其他功能
#
#             1 list_display_links
#                 与list_display一起用，给出的字段可点击，点击后跳转到该对象编辑页面
#                     list_display = ('a', 'b')
#                     list_display_links = ('b',)
#             2 list_filter
#                 根据给出的字段，提供快速塞选框
#                     list_filter = ('a')
#
#             3 list_select_related
#                 设置list_select_related以告诉Django在检索管理更改列表页面上的对象列表时使用
#                 select_related()。这可以节省大量的数据库查询。
#                 该值应该是布尔值，列表或元组。默认值为False。
#
#             4 list_editable
#                 展示列表时，指定列变为可直接编辑
#                 list_editable = ('a',)
#
#             5 search_fields
#                 展示列表时，添加搜索条，对提供的字段可进行模糊搜索
#                 search_fields = ('a',)
#
#             6 date_hierarchy
#                 展示列表时， 对Date和DateTime类型进行搜索
#
#             7 inlines
#                 对带有FK的进行设置，对编辑不带FK的表的时候，可直接编辑带FK和不带FK的两个表
#                     1 创建类继承 admin.StackedInline
#                     2 定制创建类中的属性
#                         class A(admin.StackedInline):
#                             extra = 0
#                             model = 带有外键的类
#                     3 在不带有外键类中设置inlines
#                         @admin.register(Sex)
#                         class MakeSex(admin.ModelAdmin):
#                             list_display = ('sex_times', )
#                             inlines = [InlineGirls]
#             8 action
#                 展示列表时候 上方会出现action功能下拉框，选择功能点击go执行操作
#                     1 自定义admin类中创建方法func
#                         def fun(self, request,queryset):
#                             .....
#                     2 定制在action中显示功能描述
#                         func.short_description = '描述'
#                     3 向action功能中注册定制的函数func
#                         actions = [func,]
#                     4 （可选）action条的位置，选择个数
#                         Action选项都是在页面上方显示
#                             actions_on_top = True
#                         Action选项都是在页面下方显示
#                             actions_on_bottom = False
#                         是否显示选择个数
#                             actions_selection_counter = True
#
#             10 定制HTML模板
#
#                 add_form_template = None
#                 change_form_template = None
#                 change_list_template = None
#                 delete_confirmation_template = None
#                 delete_selected_confirmation_template = None
#                 object_history_template = None
#
#             11 raw_id_fields，详细页面，针对FK和M2M字段变成以Input框形式
#                 @admin.register(models.UserInfo)
#                 class UserAdmin(admin.ModelAdmin):
#                     raw_id_fields = ('FK字段', 'M2M字段',)
#
#             12  fields，详细页面时，显示字段的字段
#                 @admin.register(models.UserInfo)
#                 class UserAdmin(admin.ModelAdmin):
#                     fields = ('user',)
#             13 exclude，详细页面时，排除的字段
#
#                 @admin.register(models.UserInfo)
#                 class UserAdmin(admin.ModelAdmin):
#                     exclude = ('user',)
#             14  readonly_fields，详细页面时，只读字段
#
#                 @admin.register(models.UserInfo)
#                 class UserAdmin(admin.ModelAdmin):
#                     readonly_fields = ('user',)
#             15 fieldsets，详细页面时，使用fieldsets标签对数据进行分割显示
#
#
#                 @admin.register(models.UserInfo)
#                 class UserAdmin(admin.ModelAdmin):
#                     fieldsets = (
#                         ('基本数据', {
#                             'fields': ('user', 'pwd', 'ctime',)
#                         }),
#                         ('其他', {
#                             'classes': ('collapse', 'wide', 'extrapretty'),  # 'collapse','wide', 'extrapretty'
#                             'fields': ('user', 'pwd'),
#                         }),
#                     )
#
#             16 详细页面时，M2M显示时，数据移动选择（方向：上下和左右）
#
#                 @admin.register(models.UserInfo)
#                 class UserAdmin(admin.ModelAdmin):
#                     filter_vertical = ("m2m字段",) # 或filter_horizontal = ("m2m字段",)
#             17 ordering，列表时，数据排序规则
#
#                 @admin.register(models.UserInfo)
#                 class UserAdmin(admin.ModelAdmin):
#                     ordering = ('-id',)
#                     或
#                     def get_ordering(self, request):
#                         return ['-id', ]
#             18. radio_fields，详细页面时，使用radio显示选项（FK默认使用select）
#
#                 radio_fields = {"ug": admin.VERTICAL} # 或admin.HORIZONTAL
#             19 form = ModelForm，用于定制用户请求时候表单验证
#
#
#                 from app01 import models
#                 from django.forms import ModelForm
#                 from django.forms import fields
#
#
#                 class MyForm(ModelForm):
#                     others = fields.CharField()
#
#                     class Meta:
#                         model = models = models.UserInfo
#                         fields = "__all__"
#
#                 @admin.register(models.UserInfo)
#                 class UserAdmin(admin.ModelAdmin):
#
#                     form = MyForm
#
#             20 empty_value_display = "列数据为空时，显示默认值"
#
#                 @admin.register(models.UserInfo)
#                 class UserAdmin(admin.ModelAdmin):
#                     empty_value_display = "列数据为空时，默认显示"
#
#                     list_display = ('user','pwd','up')
#
#                     def up(self,obj):
#                         return obj.user
#                     up.empty_value_display = "指定列数据为空时，默认显示"
#
#
#
#             from django.contrib import admin
#
#             # Register your models here.
#
#             from .models import *
#
#             class BookInline(admin.StackedInline): # TabularInline
#                 extra = 0
#                 model = Book
#
#             class BookAdmin(admin.ModelAdmin):
#
#                 list_display = ("title",'publishDate', 'price',"foo","publisher")
#                 list_display_links = ('publishDate',"price")
#                 list_filter = ('price',)
#                 list_editable=("title","publisher")
#                 search_fields = ('title',)
#                 date_hierarchy = 'publishDate'
#                 preserve_filters=False
#
#                 def foo(self,obj):
#
#                     return obj.title+str(obj.price)
#
#                 change_list_template="my_change_list_template.html"
#
#
# Django admin源码剖析
#
#     1 单例模式概念
#         单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。
#         当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。
#         比如，某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息。
#         如果在程序运行期间，有很多地方都需要使用配置文件的内容，也就是说很多地方都需要创建 AppConfig 对象的实例，
#         这就导致系统中存在多个 AppConfig 的实例对象，而这样会严重浪费内存资源，
#         尤其是在配置文件内容很多的情况下。事实上，类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象。
#
#     2 实现单例类的方式
#
#         使用 __new__()
#         使用模块
#         使用装饰器（decorator）
#         使用元类（metaclass）
#         使用__new__()方式
#
#         1 使用 __new__()
#
#             class Person(object):
#                 def __init__(self, name, age):
#                     self.name = name
#                     self.age = age
#
#             class Singleton(object):
#                 _instance = None
#
#                 def __new__(cls, *args, **kwargs):
#                     print(1)
#                     if not cls._instance:
#                         cls._instance = super(Singleton, cls).__new__(cls)
#                     return cls._instance
#
#                 def __init__(self, name, age):
#                     print(2)
#                     self.name = name
#                     self.age = age
#
#
#             if __name__ == '__main__':
#                 p1 = Person("alex", 9000)
#                 p2 = Person("alex", 9000)
#
#                 print(p1 == p2)
#                 print(id(p1), id(p2))
#
#                 print("=" * 120)
#
#                 s1 = Singleton("alex", 9000)
#                 s2 = Singleton("alex", 9000)
#                 print(s1 == s2)
#                 print(id(s1), id(s2))
#
#         2 使用模块方式
#             其实，Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，
#             当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。因此，
#             我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。
#
#
#
#
#             class Singleton(object):
#                 def __init__(self, name, age):
#                     self.name = name
#                     self.age = age
#
#
#             p1 = Singleton("alex", 9000)
#
#             from singleton import p1
#
#             print(id(p1))
#             print(p1.name)
#             p1.name = "Bob"
#
#             from singleton import p1
#
#             print(id(p1))
#             print(p1.name)
#
#     admin执行流程
#         <1>循环加载执行所有已经注册的app中的admin.py文件
#
#         def autodiscover():
#             autodiscover_modules('admin', register_to=site)
#         <2>执行代码
#
#             ＃admin.py
#
#             class BookAdmin(admin.ModelAdmin):
#                 list_display = ("title",'publishDate', 'price')
#
#             admin.site.register(Book, BookAdmin)
#             admin.site.register(Publish)
#
#
#
#         <3> admin.site
#
#             这里应用的是一个单例模式，对于AdminSite类的一个单例模式，
#             执行的每一个app中的每一个admin.site都是一个对象
#
#         <4> 执行register方法
#
#             admin.site.register(Book, BookAdmin)
#             admin.site.register(Publish)
#
#             class ModelAdmin(BaseModelAdmin):pass
#
#             def register(self, model_or_iterable, admin_class=None, **options):
#                 if not admin_class:
#                         admin_class = ModelAdmin
#                 # Instantiate the admin class to save in the registry
#                 self._registry[model] = admin_class(model, self)
#
#
#         <5> admin的URL配置
#
#             urlpatterns = [
#                 url(r'^admin/', admin.site.urls),
#             ]
#
#             class AdminSite(object):
#
#                  def get_urls(self):
#                     from django.conf.urls import url, include
#
#                     urlpatterns = []
#
#                     # Add in each model's views, and create a list of valid URLS for the
#                     # app_index
#                     valid_app_labels = []
#                     for model, model_admin in self._registry.items():
#                         urlpatterns += [
#                             url(r'^%s/%s/' % (model._meta.app_label, model._meta.model_name), include(model_admin.urls)),
#                         ]
#                         if model._meta.app_label not in valid_app_labels:
#                             valid_app_labels.append(model._meta.app_label)
#
#
#                     return urlpatterns
#
#                 @property
#                 def urls(self):
#                     return self.get_urls(), 'admin', self.name
#
#         <6>  url()方法的扩展应用
#
#             from django.shortcuts import HttpResponse
#             def test01(request):
#                 return HttpResponse("test01")
#
#             def test02(request):
#                 return HttpResponse("test02")
#
#             urlpatterns = [
#                 url(r'^admin/', admin.site.urls),
#                 url(r'^yuan/', ([
#                                 url(r'^test01/', test01),
#                                 url(r'^test02/', test02),
#
#                                 ],None,None)),
#             ]
#
#
#
#             from django.conf.urls import url,include
#             from django.contrib import admin
#
#             from django.shortcuts import HttpResponse
#
#             def change_list_view(request):
#                 return HttpResponse("change_list_view")
#             def add_view(request):
#                 return HttpResponse("add_view")
#             def delete_view(request):
#                 return HttpResponse("delete_view")
#             def change_view(request):
#                 return HttpResponse("change_view")
#
#             def get_urls():
#
#                 temp=[
#                     url(r"^$".format(app_name,model_name),change_list_view),
#                     url(r"^add/$".format(app_name,model_name),add_view),
#                     url(r"^\d+/del/$".format(app_name,model_name),delete_view),
#                     url(r"^\d+/change/$".format(app_name,model_name),change_view),
#                 ]
#
#                 return temp
#
#
#             url_list=[]
#
#             for model_class,obj in admin.site._registry.items():
#
#                 model_name=model_class._meta.model_name
#                 app_name=model_class._meta.app_label
#
#                 # temp=url(r"{0}/{1}/".format(app_name,model_name),(get_urls(),None,None))
#                 temp=url(r"{0}/{1}/".format(app_name,model_name),include(get_urls()))
#                 url_list.append(temp)
#
#             urlpatterns = [
#                 url(r'^admin/', admin.site.urls),
#                 url(r'^yuan/', (url_list,None,None)),
#             ]
# --------------------------------------------------
# 同源策略
#
#     一个源的定义
#         如果两个页面的协议，端口（如果有指定）和域名都相同，则两个页面具有相同的源。
#
#     举个例子：
#
#         下表给出了相对http://a.xyz.com/dir/page.html同源检测的示例:
#
#         URL	结果	原因
#         http://a.xyz.com/dir2/other.html	成功
#         http://a.xyz.com/dir/inner/another.html	成功
#         https://a.xyz.com/secure.html	失败	不同协议 ( https和http )
#         http://a.xyz.com:81/dir/etc.html	失败	不同端口 ( 81和80)
#         http://a.opq.com/dir/other.html	失败	不同域名 ( xyz和opq)
#
#
#     同源策略是什么
#         同源策略是浏览器的一个安全功能，不同源的客户端脚本在没有明确授权的情况下，不能读写对方资源。所以xyz.com下的js
#         脚本采用ajax读取abc.com里面的文件数据是会被拒绝的。
#
#     同源策略限制了从同一个源加载的文档或脚本如何与来自另一个源的资源进行交互。这是一个用于隔离潜在恶意文件的重要安全机制。
#
#     不受同源策略限制的
#         1. 页面中的链接，重定向以及表单提交是不会受到同源策略限制的。
#
#         2. 跨域资源的引入是可以的。但是js不能读写加载的内容。如嵌入到页面中的<script src="..."></script>，<img>，<link>，<iframe>等。
#
#     举个例子
#     我们手写两个Django demo:
#
#     demo1
#     urls.py
#
#     urlpatterns = [
#         url(r'^abc/', views.abc),
#     ]
#     views.py
#
#     def abc(request):
#         return HttpResponse("rion")
#     demo2
#     urls.py
#
#     urlpatterns = [
#         url(r'^xyz/', views.xyz),
#     ]
#     views.py
#
#     def xyz(request):
#         return render(request, "xyz.html")
#     xyz.html
#
#     复制代码
#     <!DOCTYPE HTML>
#     <html>
#     <head>
#       <meta charset="UTF-8">
#       <meta http-equiv="x-ua-compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width, initial-scale=1">
#       <title>xyz</title>
#     </head>
#     <body>
#     <button id="b1">点我</button>
#     <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
#     <script>
#       $("#b1").click(function () {
#         $.ajax({
#           url: "http://127.0.0.1:8002/abc/",
#           type: "get",
#           success:function (res) {
#             console.log(res);
#           }
#         })
#       });
#     </script>
#     </body>
#     </html>
#     复制代码
#     现在，打开使用浏览器打开http://127.0.0.1:8000/xyz/，点击页面上的 '点我' 按钮，会在console页面发现错误信息如下：
#
#
#
#     为什么报错呢？因为同源策略限制跨域发送ajax请求。
#
#     细心点的同学应该会发现我们的demo1项目其实已经接收到了请求并返回了响应，是浏览器对非同源请求返回的结果做了拦截。
#
#     再细心点的同学会发现，我们使用cdn方式引用的jQuery文件也是跨域的，它就可以使用。
#
#     同样是从其他的站点拿东西，script标签就可以。那我们能不能利用这一点搞点事情呢？
#
#     把xyz.html中的代码改一下：
#
#     复制代码
#     <!DOCTYPE HTML>
#     <html>
#     <head>
#       <meta charset="UTF-8">
#       <meta http-equiv="x-ua-compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width, initial-scale=1">
#       <title>xyz</title>
#     </head>
#     <body>
#     <button id="b1">点我</button>
#     <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
#     <script src="http://127.0.0.1:8002/abc/"></script>
#     </body>
#     </html>
#     复制代码
#     现在，我们刷新一下页面，会出现如下错误提示：
#
#
#
#
#
#     看来后端返回的响应已经被拿到了，只不过把rion当成了一个变量来使用，但是该页面上却没有定义一个名为rion的变量。所以出错了。
#
#     那我定义一个rion变量还不行吗？
#
#     复制代码
#     <!DOCTYPE HTML>
#     <html>
#     <head>
#       <meta charset="UTF-8">
#       <meta http-equiv="x-ua-compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width, initial-scale=1">
#       <title>xyz</title>
#     </head>
#     <body>
#     <button id="b1">点我</button>
#     <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
#     <script>
#       var rion = 100;
#     </script>
#     <script src="http://127.0.0.1:8002/abc/"></script>
#     </body>
#     </html>
#     复制代码
#     这次就不会报错了。
#
#     我定义一个变量可以，那可不可以定义一个函数呢？
#
#     复制代码
#     <!DOCTYPE HTML>
#     <html>
#     <head>
#       <meta charset="UTF-8">
#       <meta http-equiv="x-ua-compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width, initial-scale=1">
#       <title>xyz</title>
#     </head>
#     <body>
#     <button id="b1">点我</button>
#     <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
#     <script>
#       function rion() {
#         console.log("选我不后悔！");
#       }
#     </script>
#     <script src="http://127.0.0.1:8002/abc/"></script>
#     </body>
#     </html>
#     复制代码
#     同时把返回的响应也改一下：
#
#     def abc(request):
#         return HttpResponse("rion()")
#     此时，再次刷新页面，可以看到下面的结果。
#
#
#
#     啊，真是让人性兴奋的操作！
#
#     我返回的 rion()，页面上拿到这个响应之后直接执行了rion函数！
#
#
#
#     那函数中可不可以传递参数呢？我们试一下！
#
#      demo2中的xyz.html
#
#     复制代码
#     <!DOCTYPE HTML>
#     <html>
#     <head>
#       <meta charset="UTF-8">
#       <meta http-equiv="x-ua-compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width, initial-scale=1">
#       <title>xyz</title>
#     </head>
#     <body>
#     <button id="b1">点我</button>
#     <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
#     <script>
#       function rion(res) {
#         console.log(res);
#       }
#     </script>
#     <script src="http://127.0.0.1:8002/abc/"></script>
#     </body>
#     </html>
#     复制代码
#     demo1中的视图函数：
#
#     def abc(request):
#         res = {"code": 0, "data": ["SNIS-561", "SNIS-517", "SNIS-539"]}
#         return HttpResponse("rion({})".format(json.dumps(res)))
#     刷新页面查看效果：
#
#
#
#     果然传递参数也是可以的！
#
#     我们通过script标签的跨域特性来绕过同源策略拿到想要的数据了！！！
#
#
#
#     这其实就是JSONP的简单实现模式，或者说是JSONP的原型：创建一个回调函数，然后在远程服务上调用这个函数并且将JSON 数据形式作为参数传递，完成回调。
#
#     将JSON数据填充进回调函数，这就是JSONP的JSON+Padding的含义。
#
#     但是我们更多时候是希望通过事件触发数据的获取，而不是像上面一样页面一刷新就执行了，这样很不灵活。
#
#     其实这很好解决，我们可以通过javascript动态的创建script标签来实现。
#
#     demo2中的xyz.html
#
#     复制代码
#     <!DOCTYPE HTML>
#     <html>
#     <head>
#       <meta charset="UTF-8">
#       <meta http-equiv="x-ua-compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width, initial-scale=1">
#       <title>xyz</title>
#     </head>
#     <body>
#     <button id="b1">点我</button>
#     <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
#     <script>
#       function rion(res) {
#         console.log(res);
#       }
#       function addScriptTag(src){
#         var scriptEle = document.createElement("script");
#         $(scriptEle).attr("src", src);
#         $("body").append(scriptEle);
#         $(scriptEle).remove();
#       }
#       $("#b1").click(function () {
#         addScriptTag("http://127.0.0.1:8002/abc/")
#       })
#     </script>
#     </body>
#     </html>
#     复制代码
#     这样当我们点击b1按钮的时候，会在页面上插入一个script标签，然后从后端获取数据。
#
#     为了实现更加灵活的调用，我们可以把客户端定义的回调函数的函数名传给服务端，服务端则会返回以该回调函数名，将获取的json数据传入这个函数完成回调。
#
#     demo2中的xyz.html
#
#     复制代码
#     <!DOCTYPE HTML>
#     <html>
#     <head>
#       <meta charset="UTF-8">
#       <meta http-equiv="x-ua-compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width, initial-scale=1">
#       <title>xyz</title>
#     </head>
#     <body>
#     <button id="b1">点我</button>
#     <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
#     <script>
#       function rion(res) {
#         console.log(res);
#       }
#
#       function addScriptTag(src) {
#         var scriptEle = document.createElement("script");
#         $(scriptEle).attr("src", src);
#         $("body").append(scriptEle);
#         $(scriptEle).remove();
#       }
#       $("#b1").click(function () {
#         addScriptTag("http://127.0.0.1:8002/abc/?callback=rion")
#       });
#     </script>
#     </body>
#     </html>
#     复制代码
#     demo1中的views.py
#
#     def abc(request):
#         res = {"code": 0, "data": ["SNIS-561", "SNIS-517", "SNIS-539"]}
#         func = request.GET.get("callback")
#         return HttpResponse("{}({})".format(func, json.dumps(res)))
#     这样就能实现动态的调用了。
#
#     jQuery中getJSON方法
#     jQuery中有专门的方法实现jsonp。
#
#     demo2中的xyz.html
#
#     复制代码
#     <!DOCTYPE HTML>
#     <html>
#     <head>
#       <meta charset="UTF-8">
#       <meta http-equiv="x-ua-compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width, initial-scale=1">
#       <title>xyz</title>
#     </head>
#     <body>
#     <button id="b1">点我</button>
#     <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
#     <script>
#       $("#b1").click(function () {
#         $.getJSON("http://127.0.0.1:8002/abc/?callback=?", function (res) {
#           console.log(res);
#         })
#       });
#     </script>
#     </body>
#     </html>
#     复制代码
#     要注意的是在url的后面必须要有一个callback参数，这样getJSON方法才会知道是用JSONP方式去访问服务，callback后面的那个？是jQuery内部自动生成的一个回调函数名。
#
#     但是如果我们想自己指定回调函数名，或者说服务上规定了回调函数名该怎么办呢？我们可以使用$.ajax方法来实现：
#
#     复制代码
#     <!DOCTYPE HTML>
#     <html>
#     <head>
#       <meta charset="UTF-8">
#       <meta http-equiv="x-ua-compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width, initial-scale=1">
#       <title>xyz</title>
#     </head>
#     <body>
#     <button id="b1">点我</button>
#     <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
#     <script>
#       $("#b1").click(function () {
#         $.ajax({
#           url: "http://127.0.0.1:8002/abc/",
#           dataType: "jsonp",
#           jsonp: "callback",
#           jsonpCallback: "rion2"
#         })
#       });
#       function rion2(res) {
#         console.log(res);
#       }
#     </script>
#     </body>
#     </html>
#     复制代码
#     不过我们通常都会讲回调函数写在success回调中：
#
#     复制代码
#     <!DOCTYPE HTML>
#     <html>
#     <head>
#       <meta charset="UTF-8">
#       <meta http-equiv="x-ua-compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width, initial-scale=1">
#       <title>xyz</title>
#     </head>
#     <body>
#     <button id="b1">点我</button>
#     <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
#     <script>
#       $("#b1").click(function () {
#         $.ajax({
#           url: "http://127.0.0.1:8002/abc/",
#           dataType: "jsonp",
#           success: function (res) {
#             console.log(res);
#           }
#         })
#       })
#     </script>
#     </body>
#     </html>
#     复制代码
#
#
#     JSONP应用
#     复制代码
#     // 跨域请求示例
#     $("#show-tv").click(function () {
#       $.ajax({
#         url: "http://www.jxntv.cn/data/jmd-jxtv2.html?callback=list&_=1454376870403",
#         dataType: 'jsonp',
#         jsonp: 'callback',
#         jsonpCallback: 'list',
#         success: function (data) {
#           var weekList = data.data;
#           var $tvListEle = $(".tv-list");
#           $.each(weekList, function (k, v) {
#             var s1 = "<p>" + v.week + "列表</p>";
#             $tvListEle.append(s1);
#             $.each(v.list, function (k2, v2) {
#               var s2 = "<p><a href='" + v2.link + "'>" + v2.name + "</a></p>";
#               $tvListEle.append(s2)
#             });
#             $tvListEle.append("<hr>");
#           })
#         }
#       })
#     });
#     复制代码
#
# 做开发离不开日志，以下是我在工作中写Django项目常用的logging配置。
#
#     复制代码
#     BASE_LOG_DIR = os.path.join(BASE_DIR, "log")
#     LOGGING = {
#         'version': 1,
#         'disable_existing_loggers': False,
#         'formatters': {
#             'standard': {
#                 'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
#                           '[%(levelname)s][%(message)s]'
#             },
#             'simple': {
#                 'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
#             },
#             'collect': {
#                 'format': '%(message)s'
#             }
#         },
#         'filters': {
#             'require_debug_true': {
#                 '()': 'django.utils.log.RequireDebugTrue',
#             },
#         },
#         'handlers': {
#             'console': {
#                 'level': 'DEBUG',
#                 'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
#                 'class': 'logging.StreamHandler',
#                 'formatter': 'simple'
#             },
#             'SF': {
#                 'level': 'INFO',
#                 'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，根据文件大小自动切
#                 'filename': os.path.join(BASE_LOG_DIR, "xxx_info.log"),  # 日志文件
#                 'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
#                 'backupCount': 3,  # 备份数为3  xx.log --> xx.log.1 --> xx.log.2 --> xx.log.3
#                 'formatter': 'standard',
#                 'encoding': 'utf-8',
#             },
#             'TF': {
#                 'level': 'INFO',
#                 'class': 'logging.handlers.TimedRotatingFileHandler',  # 保存到文件，根据时间自动切
#                 'filename': os.path.join(BASE_LOG_DIR, "xxx_info.log"),  # 日志文件
#                 'backupCount': 3,  # 备份数为3  xx.log --> xx.log.2018-08-23_00-00-00 --> xx.log.2018-08-24_00-00-00 --> ...
#                 'when': 'D',  # 每天一切， 可选值有S/秒 M/分 H/小时 D/天 W0-W6/周(0=周一) midnight/如果没指定时间就默认在午夜
#                 'formatter': 'standard',
#                 'encoding': 'utf-8',
#             },
#             'error': {
#                 'level': 'ERROR',
#                 'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
#                 'filename': os.path.join(BASE_LOG_DIR, "xxx_err.log"),  # 日志文件
#                 'maxBytes': 1024 * 1024 * 5,  # 日志大小 50M
#                 'backupCount': 5,
#                 'formatter': 'standard',
#                 'encoding': 'utf-8',
#             },
#             'collect': {
#                 'level': 'INFO',
#                 'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
#                 'filename': os.path.join(BASE_LOG_DIR, "xxx_collect.log"),
#                 'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
#                 'backupCount': 5,
#                 'formatter': 'collect',
#                 'encoding': "utf-8"
#             }
#         },
#         'loggers': {
#             '': {  # 默认的logger应用如下配置
#                 'handlers': ['SF', 'console', 'error'],  # 上线之后可以把'console'移除
#                 'level': 'DEBUG',
#                 'propagate': True,
#             },
#             'collect': {  # 名为 'collect'的logger还单独处理
#                 'handlers': ['console', 'collect'],
#                 'level': 'INFO',
#             }
#         },
#     }
#  django分页
#     当数据库中数据有很多，我们通常会在前端页面做分页展示。
#
#     分页的数据可以在前端页面实现，也可以在后端实现分页。
#
#     后端实现分页的原理就是每次只请求一页数据。
#
#     准备工作
#
#     我们使用脚本批量创建一些测试数据（将下面的代码保存到bulk_create.py文件中放到Django项目的根目录，直接执行即可。）：
#
#     复制代码
#     import os
#
#     if __name__ == "__main__":
#         os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm.settings")
#
#         import django
#         django.setup()
#
#         from app01 import models
#         bulk_obj = (models.Publisher(name='沙河第{}出版社'.format(i)) for i in range(300))
#         models.Publisher.objects.bulk_create(bulk_obj)
#
# 自定义分页
#
#     稳扎稳打版
#     def publisher_list(request):
#         # 从URL中取当前访问的页码数
#         try:
#             current_page = int(request.GET.get('page'))
#         except Exception as e:
#             # 取不到或者页码数不是数字都默认展示第1页
#             current_page = 1
#         # 总数据量
#         total_count = models.Publisher.objects.count()
#         # 定义每页显示多少条数据
#         per_page = 10
#         # 计算出总页码数
#         total_page, more = divmod(total_count, per_page)
#         if more:
#             total_page += 1
#         # 定义页面上最多显示多少页码(为了左右对称，一般设为奇数)
#         max_show = 11
#         half_show = max_show // 2
#         # 计算一下页面显示的页码范围
#         if total_page <= max_show:  # 总页码数小于最大显示页码数
#             page_start = 1
#             page_end = total_page
#         elif current_page + half_show >= total_page:  # 右边越界
#             page_end = total_page
#             page_start = total_page - max_show
#         elif current_page - half_show <= 1:  # 左边越界
#             page_start = 1
#             page_end = max_show
#         else:  # 正常页码区间
#             page_start = current_page - half_show
#             page_end = current_page + half_show
#         # 数据索引起始位置
#         data_start = (current_page-1) * per_page
#         data_end = current_page * per_page
#
#         publisher_list = models.Publisher.objects.all()[data_start:data_end]
#
#         # 生成页面上显示的页码
#         page_html_list = []
#         page_html_list.append('<nav aria-label="Page navigation"><ul class="pagination">')
#         # 加首页
#         first_li = '<li><a href="/publisher_list/?page=1">首页</a></li>'
#         page_html_list.append(first_li)
#         # 加上一页
#         if current_page == 1:
#             prev_li = '<li><a href="#"><span aria-hidden="true">&laquo;</span></a></li>'
#         else:
#             prev_li = '<li><a href="/publisher_list/?page={}"><span aria-hidden="true">&laquo;</span></a></li>'.format(current_page - 1)
#         page_html_list.append(prev_li)
#         for i in range(page_start, page_end + 1):
#             if i == current_page:
#                 li_tag = '<li class="active"><a href="/publisher_list/?page={0}">{0}</a></li>'.format(i)
#             else:
#                 li_tag = '<li><a href="/publisher_list/?page={0}">{0}</a></li>'.format(i)
#             page_html_list.append(li_tag)
#         # 加下一页
#         if current_page == total_page:
#             next_li = '<li><a href="#"><span aria-hidden="true">&raquo;</span></a></li>'
#         else:
#             next_li = '<li><a href="/publisher_list/?page={}"><span aria-hidden="true">&raquo;</span></a></li>'.format(current_page + 1)
#         page_html_list.append(next_li)
#         # 加尾页
#         page_end_li = '<li><a href="/publisher_list/?page={}">尾页</a></li>'.format(total_page)
#         page_html_list.append(page_end_li)
#         page_html_list.append('</ul></nav>')
#         page_html = "".join(page_html_list)
#         return render(request, "publisher_list.html", {"publisher_list": publisher_list, "page_html": page_html})
#
#     稳扎稳打版
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     封装保存版
#
#     class Pagination(object):
#         """自定义分页（Bootstrap版）"""
#         def __init__(self, current_page, total_count, base_url, per_page=10, max_show=11):
#             """
#             :param current_page: 当前请求的页码
#             :param total_count: 总数据量
#             :param base_url: 请求的URL
#             :param per_page: 每页显示的数据量，默认值为10
#             :param max_show: 页面上最多显示多少个页码，默认值为11
#             """
#             try:
#                 self.current_page = int(current_page)
#             except Exception as e:
#                 # 取不到或者页码数不是数字都默认展示第1页
#                 self.current_page = 1
#             # 定义每页显示多少条数据
#             self.per_page = per_page
#             # 计算出总页码数
#             total_page, more = divmod(total_count, per_page)
#             if more:
#                 total_page += 1
#             self.total_page = total_page
#             # 定义页面上最多显示多少页码(为了左右对称，一般设为奇数)
#             self.max_show = max_show
#             self.half_show = max_show // 2
#             self.base_url = base_url
#
#         @property
#         def start(self):
#             return (self.current_page-1) * self.per_page
#
#         @property
#         def end(self):
#             return self.current_page * self.per_page
#
#         def page_html(self):
#             # 计算一下页面显示的页码范围
#             if self.total_page <= self.max_show:  # 总页码数小于最大显示页码数
#                 page_start = 1
#                 page_end = self.total_page
#             elif self.current_page + self.half_show >= self.total_page:  # 右边越界
#                 page_end = self.total_page
#                 page_start = self.total_page - self.max_show
#             elif self.current_page - self.half_show <= 1:  # 左边越界
#                 page_start = 1
#                 page_end = self.max_show
#             else:  # 正常页码区间
#                 page_start = self.current_page - self.half_show
#                 page_end = self.current_page + self.half_show
#             # 生成页面上显示的页码
#             page_html_list = []
#             page_html_list.append('<nav aria-label="Page navigation"><ul class="pagination">')
#             # 加首页
#             first_li = '<li><a href="{}?page=1">首页</a></li>'.format(self.base_url)
#             page_html_list.append(first_li)
#             # 加上一页
#             if self.current_page == 1:
#                 prev_li = '<li><a href="#"><span aria-hidden="true">&laquo;</span></a></li>'
#             else:
#                 prev_li = '<li><a href="{}?page={}"><span aria-hidden="true">&laquo;</span></a></li>'.format(
#                     self.base_url, self.current_page - 1)
#             page_html_list.append(prev_li)
#             for i in range(page_start, page_end + 1):
#                 if i == self.current_page:
#                     li_tag = '<li class="active"><a href="{0}?page={1}">{1}</a></li>'.format(self.base_url, i)
#                 else:
#                     li_tag = '<li><a href="{0}?page={1}">{1}</a></li>'.format(self.base_url, i)
#                 page_html_list.append(li_tag)
#             # 加下一页
#             if self.current_page == self.total_page:
#                 next_li = '<li><a href="#"><span aria-hidden="true">&raquo;</span></a></li>'
#             else:
#                 next_li = '<li><a href="{}?page={}"><span aria-hidden="true">&raquo;</span></a></li>'.format(
#                     self.base_url, self.current_page + 1)
#             page_html_list.append(next_li)
#             # 加尾页
#             page_end_li = '<li><a href="{}?page={}">尾页</a></li>'.format(self.base_url, self.total_page)
#             page_html_list.append(page_end_li)
#             page_html_list.append('</ul></nav>')
#             return "".join(page_html_list)
#
#     封装保存版
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     封装保存版使用示例
#
#     def publisher_list(request):
#         # 从URL中取当前访问的页码数
#         current_page = int(request.GET.get('page'))
#         # 比len(models.Publisher.objects.all())更高效
#         total_count = models.Publisher.objects.count()
#         page_obj = Pagination(current_page, total_count, request.path_info)
#         data = models.Publisher.objects.all()[page_obj.start:page_obj.end]
#         page_html = page_obj.page_html()
#         return render(request, "publisher_list.html", {"publisher_list": data, "page_html": page_html})
#
#     封装保存版使用示例
#
# Django内置分页
#     from django.shortcuts import render
#     from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#
#     L = []
#     for i in range(999):
#         L.append(i)
#
#     def index(request):
#         current_page = request.GET.get('p')
#
#         paginator = Paginator(L, 10)
#         # per_page: 每页显示条目数量
#         # count:    数据总个数
#         # num_pages:总页数
#         # page_range:总页数的索引范围，如: (1,10),(1,200)
#         # page:     page对象
#         try:
#             posts = paginator.page(current_page)
#             # has_next              是否有下一页
#             # next_page_number      下一页页码
#             # has_previous          是否有上一页
#             # previous_page_number  上一页页码
#             # object_list           分页之后的数据列表
#             # number                当前页
#             # paginator             paginator对象
#         except PageNotAnInteger:
#             posts = paginator.page(1)
#         except EmptyPage:
#             posts = paginator.page(paginator.num_pages)
#         return render(request, 'index.html', {'posts': posts})
#
#     内置分页view部分
#
#
#
#
#
#
#
#
#
#
#
#     内置分页HTML部分
#     <!DOCTYPE html>
#     <html>
#     <head lang="en">
#         <meta charset="UTF-8">
#         <title></title>
#     </head>
#     <body>
#     <ul>
#         {% for item in posts %}
#             <li>{{ item }}</li>
#         {% endfor %}
#     </ul>
#
#     <div class="pagination">
#           <span class="step-links">
#             {% if posts.has_previous %}
#                 <a href="?p={{ posts.previous_page_number }}">Previous</a>
#             {% endif %}
#               <span class="current">
#                 Page {{ posts.number }} of {{ posts.paginator.num_pages }}.
#               </span>
#               {% if posts.has_next %}
#                   <a href="?p={{ posts.next_page_number }}">Next</a>
#               {% endif %}
#           </span>
#
#     </div>
#     </body>
#     </html>
#
# Session版登陆验证
#     from functools import wraps
#
#
#     def check_login(func):
#         @wraps(func)
#         def inner(request, *args, **kwargs):
#             next_url = request.get_full_path()
#             if request.session.get("user"):
#                 return func(request, *args, **kwargs)
#             else:
#                 return redirect("/login/?next={}".format(next_url))
#         return inner
#
#
#     def login(request):
#         if request.method == "POST":
#             user = request.POST.get("user")
#             pwd = request.POST.get("pwd")
#
#             if user == "alex" and pwd == "alex1234":
#                 # 设置session
#                 request.session["user"] = user
#                 # 获取跳到登陆页面之前的URL
#                 next_url = request.GET.get("next")
#                 # 如果有，就跳转回登陆之前的URL
#                 if next_url:
#                     return redirect(next_url)
#                 # 否则默认跳转到index页面
#                 else:
#                     return redirect("/index/")
#         return render(request, "login.html")
#
#
#     @check_login
#     def logout(request):
#         # 删除所有当前请求相关的session
#         request.session.delete()
#         return redirect("/login/")
#
#
#     @check_login
#     def index(request):
#         current_user = request.session.get("user", None)
#         return render(request, "index.html", {"user": current_user})
#
# Django中的Session配置
#
#     Django中默认支持Session，
#     其内部提供了5种类型的Session供开发者使用
#
#     1. 数据库Session
#     SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）
#
#     2. 缓存Session
#     SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎
#     SESSION_CACHE_ALIAS = 'default'                            # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置
#
#     3. 文件Session
#     SESSION_ENGINE = 'django.contrib.sessions.backends.file'    # 引擎
#     SESSION_FILE_PATH = None                                    # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir()
#
#     4. 缓存+数据库
#     SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'        # 引擎
#
#     5. 加密Cookie Session
#     SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'   # 引擎
#
#     其他公用设置项：
#     SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
#     SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
#     SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
#     SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
#     SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
#     SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
#     SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）
#     SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）
#
# 中间件版登录验证
#     中间件版的登录验证需要依靠session，所以数据库中要有django_session表。
#
#     urls.py
#
#
#     复制代码
#     from django.conf.urls import url
#     from app01 import views
#
#     urlpatterns = [
#         url(r'^index/$', views.index),
#         url(r'^login/$', views.login, name='login'),
#     ]
#     复制代码
#     views.py
#
#
#     复制代码
#     from django.shortcuts import render, HttpResponse, redirect
#
#
#     def index(request):
#         return HttpResponse('this is index')
#
#
#     def home(request):
#         return HttpResponse('this is home')
#
#
#     def login(request):
#         if request.method == "POST":
#             user = request.POST.get("user")
#             pwd = request.POST.get("pwd")
#
#             if user == "Q1mi" and pwd == "123456":
#                 # 设置session
#                 request.session["user"] = user
#                 # 获取跳到登陆页面之前的URL
#                 next_url = request.GET.get("next")
#                 # 如果有，就跳转回登陆之前的URL
#                 if next_url:
#                     return redirect(next_url)
#                 # 否则默认跳转到index页面
#                 else:
#                     return redirect("/index/")
#         return render(request, "login.html")
#     复制代码
#     login.html
#
#
#     复制代码
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta http-equiv="x-ua-compatible" content="IE=edge">
#         <meta name="viewport" content="width=device-width, initial-scale=1">
#         <title>登录页面</title>
#     </head>
#     <body>
#     <form action="{% url 'login' %}">
#         <p>
#             <label for="user">用户名：</label>
#             <input type="text" name="user" id="user">
#         </p>
#         <p>
#             <label for="pwd">密 码：</label>
#             <input type="text" name="pwd" id="pwd">
#         </p>
#         <input type="submit" value="登录">
#     </form>
#     </body>
#     </html>
#     复制代码
#     middlewares.py
#
#
#     复制代码
#     class AuthMD(MiddlewareMixin):
#         white_list = ['/login/', ]  # 白名单
#         balck_list = ['/black/', ]  # 黑名单
#
#         def process_request(self, request):
#             from django.shortcuts import redirect, HttpResponse
#
#             next_url = request.path_info
#             print(request.path_info, request.get_full_path())
#
#             if next_url in self.white_list or request.session.get("user"):
#                 return
#             elif next_url in self.balck_list:
#                 return HttpResponse('This is an illegal URL')
#             else:
#                 return redirect("/login/?next={}".format(next_url))
#     复制代码
#     在settings.py中注册
#
#
#     复制代码
#     MIDDLEWARE = [
#         'django.middleware.security.SecurityMiddleware',
#         'django.contrib.sessions.middleware.SessionMiddleware',
#         'django.middleware.common.CommonMiddleware',
#         'django.middleware.csrf.CsrfViewMiddleware',
#         'django.contrib.auth.middleware.AuthenticationMiddleware',
#         'django.contrib.messages.middleware.MessageMiddleware',
#         'middlewares.AuthMD',
#     ]
#     复制代码
#     AuthMD中间件注册后，所有的请求都要走AuthMD的process_request方法。
#
#     访问的URL在白名单内或者session中有user用户名，则不做阻拦走正常流程；
#
#     如果URL在黑名单中，则返回This is an illegal URL的字符串；
#
#     正常的URL但是需要登录后访问，让浏览器跳转到登录页面。
#
#     注：AuthMD中间件中需要session，所以AuthMD注册的位置要在session中间的下方。
#
#
#
#     附：Django请求流程图
#
#
# MVC框架和MTV框架
#
#     MVC:
#         模型(Model)、视图(View)和控制器(Controller)
#
#     MVT
#         Model（模型）、Template（模板）和View（视图）
#
#
#
#
# Django中操作Cookie
#
#     获取Cookie
#     request.COOKIES['key']
#     request.get_signed_cookie(key, default=RAISE_ERROR, salt='', max_age=None)
#     参数：
#     default: 默认值
#     salt: 加密盐
#     max_age: 后台控制过期时间
#
# 设置Cookie
#     rep = HttpResponse(...)
#     rep ＝ render(request, ...)
#
#     rep.set_cookie(key,value,...)
#     rep.set_signed_cookie(key,value,salt='加密盐', max_age=None, ...)
#     参数：
#     key, 键
#     value='', 值
#     max_age=None, 超时时间
#     expires=None, 超时时间(IE requires expires, so set it if hasn't been already.)
#     path='/', Cookie生效的路径，/ 表示根路径，
#             特殊的：根路径的cookie可以被任何url
#             的页面访问
#     domain=None, Cookie生效的域名
#     secure=False, https传输
#     httponly=False 只能http协议传输，
#                     无法被JavaScript获取（
#                     不是绝对，底层抓包可以获取到
#                     也可以被覆盖）
# 删除Cookie
#     def logout(request):
#         rep = redirect("/login/")
#         rep.delete_cookie("user")  # 删除用户浏览器上之前设置的usercookie值
#         return rep
#
#
#
# Django中Session相关方法
#     获取、设置、删除Session中数据
#     request.session['k1']
#     request.session.get('k1',None)
#     request.session['k1'] = 123
#     request.session.setdefault('k1',123) # 存在则不设置
#     del request.session['k1']
#
#
#     # 所有 键、值、键值对
#     request.session.keys()
#     request.session.values()
#     request.session.items()
#     request.session.iterkeys()
#     request.session.itervalues()
#     request.session.iteritems()
#
#     # 会话session的key
#     request.session.session_key
#
#     # 将所有Session失效日期小于当前日期的数据删除
#     request.session.clear_expired()
#
#     # 检查会话session的key在数据库中是否存在
#     request.session.exists("session_key")
#
#     # 删除当前会话的所有Session数据
#     request.session.delete()
#     　　
#     # 删除当前的会话数据并删除会话的Cookie。
#     request.session.flush()
#         这用于确保前面的会话数据不可以再次被用户的浏览器访问
#         例如，django.contrib.auth.logout() 函数中就会调用它。
#
#     # 设置会话Session和Cookie的超时时间
#     request.session.set_expiry(value)
#         * 如果value是个整数，session会在些秒数后失效。
#         * 如果value是个datatime或timedelta，session就会在这个时间后失效。
#         * 如果value是0,用户关闭浏览器session就会失效。
#         * 如果value是None,session会依赖全局session失效策略
#
#
#
#
# =========================================================
# 自学django分页功能
#
#
# 注意:
# 	如果数据庞大,django会显示所有的页数,可能造成假死状态
# 	所以推荐使用自定义分页功能
#
#
# 1 数据集合列表
#
# 	obj_list = Gupiao.objects.all() # 获取所有数据
#
# 2 导入Paginator,Page, PageNotAnInteger 类(from django.core.paginator import Paginator,Page,PageNotAnInteger)
#
# 	from django.core.paginator import Paginator,Page,PageNotAnInteger
#
# 3 要有当前页码指向
#
# 	current_pagnum = request.GET.get('page') # 获取当前页码
#
# 4 创建 Pagination 对象 并传入参数(被分页对象列表,每页显示数据条数)
#
# 	paginator = Paginator(r2,10)  # 创建分页列表,每页显示10条数据
#
# 5 捕获 向上翻页 传入到page的值不是integer类型
#
# 	try:    # 因为向上翻页 传入到page的值不是integer类型 捕获此错误
# 		posts = paginator.page(number=current_pagnum) # 当前第几页
# 	except PageNotAnInteger:
# 		posts = paginator.page(number=1)
#
# 6 传入模板参数 Pangination对象
#
# 	return render(request, "search.html", {"posts":posts})
#
# 7 模板中创建上一页功能
#
# 	{% if posts.has_previous %}
# 		<a href="/search/?page={{ posts.previous_page_number }}/">上一页</a>
# 	{% endif %}
#
# 8 模板中创建 页数功能
#
# 	{% for num in posts.paginator.page_range %}
# 		<a href="/search/?page={{ num }}/">{{ num }}</a>
# 	{% endfor %}
#
# 9 模板中创建下一页功能
#
# 	{% if posts.has_next %}
# 	<a href="/search/?page={{ posts.next_page_number }}">下一页</a>
# 	{% endif %}
#
# =========================================================
#
#
#
#
#
# =========================================================
# 自学django自定义分页
#
# 1 获取当前页码
#
# 	try:
# 		current_page = int(request.GET.get('page', 1))
# 		if current_page <= 0:
# 				current_page = 1
# 	except Exception as e:
# 		current_page = 1
#
# 2 定义显示最多页码
# 	# 最多显示的页码
# 	max_show = 11
# 	half_show = max_show//2
#
# 3 定义每页显示数据条数
# 	per_num = 1000  # 每页显示数据条数
# 	all_num = len(r2) # 总数据量
#
# 4 获取总页码数,判断页数决绝bug
# 	# 总页码数
# 	total_num, more = divmod(all_num, per_num)
# 	if more: 		# 如果有余数
# 		total_num += 1 # 总页码数+1
#
# 	# 为了数据不够时候显示过多的页数
# 	if total_num <= max_show:   # 如果总页码数 小于 最多显示页码数
# 		page_start = 1          # 开始页数设置为1
# 		page_end = total_num    # 结束页数设置为总页码数
# 	else:
#
# 		# 为了当前页数为1时, 1的前面不显示0,-1-2-3-4 页数
# 		if current_page<=half_show: # 如果当前页数小于一半页数
# 			page_start = 1          # 开始页数为1
# 			page_end = max_show     # 结束页数为 最大显示数
#
# 		# 为了结尾不显示多余页数
# 		elif current_page + half_show >= total_num: # 如果当前页数+一般页数大于总页数
# 			page_end = total_num 					# 结束页数 = 总页数
# 			page_start = total_num - max_show +1    # 开始页数 = 总页数-最大页数+1
#
# 		# 正常情况
# 		else:
# 			page_start = current_page-half_show
# 			page_end = current_page+half_show
#
# 	# 开始数据数 为了获取数据切片的开始位置
# 	start = (current_page-1)*per_num
# 	# 结束数据数 为了获取数据切片的结束位置
# 	end = current_page*per_num
#
#
# 	return render(request, "search.html", {"r2":r2[start:end], "total_num":range(page_start,page_end+1)})
#
# 模板
# <div>
# 	{% for j in total_num %}
# 	<a href="/search/?page={{ j }}">{{ j }}</a>
# 	{% endfor %}
# </div>
#
# =========================================================
#
#
# # =================================================
# --------------------------------------------------
# Django REST framework
1
#
#     0 知识回顾
#         django中间件和装饰器
#             适用于所有请求批量做操作
#                 场景
#                     基于角色的权限控制
#                     用户认证
#                     csrf
#                     session
#                     黑名单
#                     日志记录
#
#     1 安装
#
#         pip install djangorestframework
#     2 注册
#
#         INSTALLED_APPS = (
#             ...
#             'rest_framework',
#         )
#
#     3 验证用户是否登录
#
#         1 源码流程
#
#             1 django接受请求
#             2 执行dispatch方法
#             3 通过self.initialize_request(request, *args, **kwargs)对request进行了封装
#             4 封装中执行了authenticators=self.get_authenticators()返回了认证的类列表（可以自己写指定的类通过authentication_classes=[自己写的类]）
#             5 执行了dispathc中self.initial(request, *args, **kwargs) 方法
#             6 执行了self.initial()方法中的self.perform_authentication(request)
#             7 执行了request.user 执行了self._authenticate()对第4部的列表进行了循环
#             8 执行了user_auth_tuple = authenticator.authenticate(self)如果登录了旧返回一个元祖杜若没登录就报错
#             9  创建自定义类 重写 authenticate方法 将这个自定义添加乳到authentication_classes中可以进行用自己的规则判断用户是否登录
#         2 基本使用
#
#             class Myrenzheng（BasicAuthentication）: # 推荐继承BasicAuthentication类
#                 def authenticate(self, request):
#                     。。。。自己想写的认证条件，校验数据库等
#                     return ('xx', None)
#
#                 def authenticate_header(self,request):  # 作用是如果校验认证失败做的事情
#                     pass
#
#             class GirlsList(APIView):
#
#                 authentication_classes = [Myrenzheng,]
#
#                 def get(self, request):
#
#                     print(request.user)  # 会获取上面return的内容
#
#                     girls = Girls.objects.all()
#                     s = GirlsSerializer(girls, many=True)
#
#                     return Response(s.data)
#             补充orm操作
#                 数据不存在就创建，数据存在就更新
#                 xx.objects.updata_or_create(user=obj, defaults={'token':token})
#
#     4 认证
#         1 有些api需要用户登录成功之后才能访问，有些无需登录才能访问
#             1 创建两张表
#             2 用户登录（返回token并保存到数据库）# 通过客户端的post请求 使用用户名生成随机字符串（md5）
#               并返回给客户端，下回的用户请求的时候就携带的token，发送给服务端 服务端若验证成功该用户就可以继续访问
#
#         2 认证的全局配置
#             1 概念
#                 不用再单个类中逐个添加authentication_classes
#             2 源码流程
#
#                 authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
#
#             3 可以在settings中添加
#
#                 REST_FRAMEWORK = {
#
#                         'DEFAULT_AUTHENTICATION_CLASSES': ['app.lib.renzheng.Renzheng', ]  # 列表内为认证类的存放路径
#
#                     }
#             4 使单个视图类不需要验证
#
#                 authentication_classes = []  # 为空即可 就是不需要验证
#
#         3 匿名用户的配置
#
#             1 概念
#
#                 客户浏览不需要认证的网页
#
#                     通过源码设置了匿名用户的名称 默认为AnonymousUser
#
#
#                         def _not_authenticated(self):
#
#                             self._authenticator = None
#
#                             if api_settings.UNAUTHENTICATED_USER:
#                                 self.user = api_settings.UNAUTHENTICATED_USER() # 默认匿名用户
#                             else:
#                                 self.user = None
#
#                             if api_settings.UNAUTHENTICATED_TOKEN:
#                                 self.auth = api_settings.UNAUTHENTICATED_TOKEN() # 默认匿名用户的token
#                             else:
#                                 self.auth = None
#
#                 可更改匿名用户的用户名
#                     REST_FRAMEWORK = {
#
#                             'UNAUTHENTICATED_USER':lambda:'更改的名'
#                         }
#                 一般配置成(方便以后判断 如果为None就是匿名用户)
#                     REST_FRAMEWORK = {
#
#                             'UNAUTHENTICATED_USER':None,
#                             'UNAUTHENTICATED_TOKEN':None,
#                         }
#         4 内置认证类
#
#             from rest_framework.authentication import BasicAuthentication
#             1 BasicAuthentication自己写认证推荐继承
#
#
#     5 权限
#
#         1 有的网页符合权限等级可以访问，符合权限等级的不能访问
#
#             1 源码流程
#
#                 和用户认证基本一致
#
#             2 基本使用
#                 class MyPerssoin:
#                     message = '您的权限不是1，不能访问此网页'
#                     def has_permission(self, request, view): # 必须实现的方法
#
#                         if request._request.GET.get("user_type") != "1":
#                             print('1111')
#                             return False
#
#                         return True
#
#                 class Test_perssion1(APIView):
#
#                     authentication_classes = []
#                     permission_classes = [MyPerssoin, ]
#                     def get(self, request):
#
#                         return HttpResponse('已经验证您的权限等级为1，可以观看此网页')
#             3 全局和局部配置
#
#                 1全局
#                     REST_FRAMEWORK = {
#
#                                 DEFAULT_PERMISSION_CLASSES:['权限类的文件路径']  # 同认证
#                             }
#                 2 局部
#
#                     同认证
#
#             4 内置权限类
#
#                 1 自定义权限类推荐继承BasePermission
#
#
#     5 访问频率控制(节流)
#
#         0 基本使用
#
#             类，继承 BaseThrottle，实现 allow_request, wait
#             类，继承 SimpleRateThrottle 实现 get_cache_key, score="xxx" （xxx为配置文件中的k）
#
#         1 思路
#
#             如果想限制用户只能访问3次，超过60秒才能继续访问
#             获取用户ip和访问时间 加入到库  客户多访问一次 库中的数据就发生变化，通过库中的数据
#             访问时间个数（次数）， 和访问时间  对用户进行限制
#             匿名用户
#
#                 nobody_dict = {}
#
#                 import time
#
#                 class My_frequercy:
#
#                     def __init__(self):
#                         self.history = None
#
#
#                     def allow_request(self, request, view):
#
#                         now_time = time.time()
#                         nobody_ip = request.META.get('REMOTE_ADDR')  # 获取访问用户的ip
#
#                         if not nobody_ip in nobody_dict: # 如果用户ip不在库中
#
#                             nobody_dict[nobody_ip] = [now_time]  # 将用户第一次访问  用户ip:第一次访问时间 加入到列表中
#                             return True
#
#                         history = nobody_dict.get(nobody_ip) # 获取用户访问时间列表
#                         self.history = history
#                         while history and history[-1] < now_time - 60: # 如果用户第一次的访问时间小于当前时间-60（再次访问的时间和第一次访问的时间相隔60秒）
#                             self.a = now_time-60
#                             history.pop()   # 去掉用户的第一次访问时间，那么第二次访问时间就变成了第一次访问时间
#
#                         if len(history) < 3:    # 如果访问的次数小于3次
#                             nobody_dict[nobody_ip].insert(0, now_time) # 将用户的访问时间加入到前次访问时间之前
#                             return True
#
#
#                     def wait(self):     # 显示达到限制次数之后还剩多少秒可以继续访问
#                         # nobody_ip = request.META.get('REMOTE_ADDR')
#                         now_time = time.time()
#
#                         a = 60-(now_time-self.history[-1]) # 60-（当前时间-最开始次访问时间）
#                         return a
#
#                 class Test_frequercy(APIView):
#
#                     authentication_classes = []
#                     throttle_classes = [My_frequercy]
#
#                     def get(self, request):
#
#                         return HttpResponse('频率测试')
#
#         2 全局配置和局部配置
#
#             1 局部配置 同认证
#
#             2 全局配置
#
#                 REST_FRAMEWORK = {
#
#                     DEFAULT_THROTTLE_CLASSES:[频率控制类的路径]
#                 }
#
#         3 使用控制频率的内置类（）
#
#             1 自定义控制频率类的时候推荐继承（BaseThrottle）
#                 可以通过 self.get_ident(request) 获取匿名用户的ip
#
#             2 源码分析内置类SimpleRateThrottle
#                 源码分析  def __init__(self):
#                             if not getattr(self, 'rate', None):
#                                 self.rate = self.get_rate()     # 获取 scope 设定的值的值 如果这个值在自定义类中设置值，然后去配置文件中寻找这个值作为键的值
#                             self.num_requests, self.duration = self.parse_rate(self.rate)
#                         初始化得到数据后因为继承的是BaseThrottle 会自动去执行allow_request（）因为SimpleRateThrottle有
#                          allow_request 就执行自己的
#
#                          def allow_request(self, request, view):
#                             """
#                             Implement the check to see if the request should be throttled.
#
#                             On success calls `throttle_success`.
#                             On failure calls `throttle_failure`.
#                             """
#                             if self.rate is None:
#                                 return True
#
#                             self.key = self.get_cache_key(request, view) # 去缓存（django的默认缓存）中获取访问匿名用户的ip
#                             if self.key is None:
#                                 return True
#
#                             self.history = self.cache.get(self.key, [])  # 根据匿名用户的ip 取用户访问的时间和次数
#                             self.now = self.timer()
#                             # 剩下的和上自定义处理 次数和时间原理一样
#                             while self.history and self.history[-1] <= self.now - self.duration:
#                                 self.history.pop()
#                             if len(self.history) >= self.num_requests:
#                                 return self.throttle_failure()
#                             return self.throttle_success()
#
#             3 使用控制频率内置类SimpleRateThrottle
#
#                 1 匿名用户
#                     from rest_framework.throttling import SimpleRateThrottle
#
#                     class Test_niming_lei(SimpleRateThrottle):
#
#                         scope = "niming"  # 配置去setting的'DEFAULT_THROTTLE_RATES'中寻找
#
#                         def get_cache_key(self, request, view):  # 获取匿名用户请求的ip 然后去缓存中获取ip对应的浏览时间和次数
#
#                             return self.get_ident(request)
#
#                     class Watch_niming_lei(APIView):
#
#                         authentication_classes = []
#                         throttle_classes = [Test_niming_lei, ]
#
#
#                         def get(self, request):
#                             return HttpResponse('匿名用户频率限制')
#
#                     settings配置
#
#                         REST_FRAMEWORK = {
#
#                             'DEFAULT_THROTTLE_RATES':{'niming': '3/s'}
#                         }
#
#                 2 登录用户
#
#                        from rest_framework.throttling import SimpleRateThrottle
#
#                         class Test_niming_lei11(SimpleRateThrottle):
#
#                             scope = "niming1"  # 配置去setting的'DEFAULT_THROTTLE_RATES'中寻找
#
#                             def get_cache_key(self, request, view):  # 获取匿名用户请求的ip 然后去缓存中获取ip对应的浏览时间和次数
#
#                                 return request.user.username  # 登录用户用用户名记录访问时间和次数
#
#                 3 匿名和登录用户的频率限制使用（两个限制类）
#                     登录用户 全局限制
#                     匿名用户 局部限制  # 登录和匿名用户限制次数一致
#
#
#
#     6 版本
#
#         1 从url参数中获取版本信息（http://127.0.0.1:8000/test_version/?version=v1）
#
#             class My_version:
#
#                 def determine_version(self, request, *args, **kwargs):
#                     version = request.query_params.get('version')
#                     return version
#
#
#             class Test_version(APIView):
#
#                 versioning_class = My_version
#
#                 def get(self, request):
#                     print(request.version)
#                     return HttpResponse('版本控制')
#
#         2 从url中获取版本信息（推荐使用）
#
#             url(r'^(?P<version>[v1|v2]+)/test_version/$', views.Test_version.as_view()),
#
#             REST_FRAMEWORK = {
#                 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
#                 'DEFAULT_VERSION': 'v1',
#                 'ALLOWED_VERSIONS': ['v1', 'v2'],
#                 'VERSION_PARAM': 'version',
#             }
#
#             class Test_version(APIView):
#
#                 def get(self, request, *args, **kwargs):
#                     print(request.version)     # 可获取版本信息
#                     print(request.versioning_scheme) # 获取处理版本的对象
#                     print(request.versioning_scheme.reverse(viewname='url的name参数值', request=request)) # 反向解析
#                     return HttpResponse('版本控制')
#
#
#     7 解析器
#
#         1 内容回顾
#
#             django：request.POST和 request.body
#
#                 request.POST能接受到数据的要求
#
#                     1 请求头要求
#                         Content-Type: application/x-www-form-urlencoded
#                     2 数据格式要求
#                         name=xx&age=yy
#
#         2 概念
#
#             对请求体数据的解析
#
#         3 获取json格式数据自动解析
#
#             1 使用了from rest_framework.parsers import JSONParser
#
#             2 源码
#
#                 进行封装request的时候 parsers=self.get_parsers() # 将视图parser_classes = [JSONParser,]传入到parsers中也可以通过全局配置
#         4 全局配置（也可局部配置，推荐用全局配置）
#             rest_frameword默认全局配置了
#                 'DEFAULT_PARSER_CLASSES': (
#                     'rest_framework.parsers.JSONParser',
#                     'rest_framework.parsers.FormParser',
#                     'rest_framework.parsers.MultiPartParser'
#                 ),
#
#             1 自定义全局配置
#             REST_FRAMEWORK = {
#
#                 'DEFAULT_PARSER_CLASSES': ['rest_framework.parsers.JSONParser',  # 只解析content-type:application/json 头
#                                            'rest_framework.parsers.FormParser']  # 只解析content-type:application/x-www-form-urlencoded头
#             }
#
#
#     8 序列化
#
#         1 概念
#             请求数据进行校验
#             queryset进行序列化
#
#         2 基本使用
#             1 创建序列化类继承 （serializers.Serializer）
#                 根据模型中的字段定义类对象（即serializers.Charfield()）等
#             2 视图获取数据库中queryset数据
#             3 创建序列化类对象将得到的queryset数据传入序列化类的参数即instance=queryset数据，many=True表示多个数据
#             4 通过  序列化对象.data 获取已经被序列化的数据
#             4 用json.dumps对序列化数据进行格式转换
#             5 返回数据
#             class My_serializer(serializers.Serializer):
#
#                 role_name = serializers.CharField()
#
#
#             class Test_serializer(APIView):
#
#                 def get(self, request):
#
#                     query_data = Role.objects.all()
#                     ser = My_serializer(query_data, many=True)
#                     json_data = json.dumps(ser.data, ensure_ascii=False)
#                     return HttpResponse(json_data)
#
#         3 处理choick字段以及外键字段的显示，和自定义字段显示
#
#             class Foreignkey_serializers(serializers.Serializer):
#                 """测试外键字段choice字段和自定义序列化显示 序列化器"""
#
#                 id = serializers.IntegerField()
#                 user_type = serializers.CharField(source="get_user_type_display") # chocie属性的值的获取方法 source = get_字段名_display
#                 username = serializers.CharField()
#                 password = serializers.CharField()
#                 group = serializers.CharField(source="group.gruop_name") # 外键中获取值 source="字段.属性"
#                                                                     # source中填入序列化器对象对象的字段（此时字段为连接的外键模型的对象） “字段.属性" 获取信息
#                 #role = serializers.CharField(source="roles.all") # 多对多字段
#
#                 role = serializers.SerializerMethodField()  # 自定义对于多对多字段的信息的展示（其他字段也可以通过此方法自定义）
#
#                 def get_role(self, row):    # 与SerializerMethodField关联 通过 get_字段名建立
#                     role_obj_list = row.roles.all()
#                     ret = []
#                     for i in role_obj_list:
#                         ret.append({'id':i.id, "role_name": i.role_name})
#
#                     return ret
#
#             class Test_show_foreignkey_serializers(APIView):
#                 """测试外键字段choice字段和自定义序列化显示 视图函数"""
#
#                 def get(self, request):
#                     role_result = UserInfo.objects.all()
#                     ser = Foreignkey_serializers(instance=role_result, many=True)
#                     data = ser.data
#                     json_data = json.dumps(data, ensure_ascii=False)
#                     return HttpResponse(json_data)
#
#         4 基于继承serializers.ModelSerializer类的序列化处理字段显示
#             class Foreignkey_serializers(serializers.ModelSerializer):
#                 """测试外键字段choice字段和自定义序列化显示 序列化器"""
#
#                 user_type = serializers.CharField(source="get_user_type_display")
#                 group = serializers.CharField(source="group.gruop_name")
#                 role = serializers.SerializerMethodField()
#
#                 def get_role(self, row):    # 与SerializerMethodField关联 通过 get_字段名建立
#                     role_obj_list = row.roles.all()
#                     ret = []
#                     for i in role_obj_list:
#                         ret.append({'id':i.id, "role_name": i.role_name})
#
#                     return ret
#                 class Meta:
#
#                     model = UserInfo    # 指定模型
#                     fields = ['id', 'username', 'password', 'user_type', 'group', 'role'] # 指定显示字段
#
#
#             class Test_show_foreignkey_serializers(APIView):
#                 """测试外键字段choice字段和自定义序列化显示 视图函数"""
#
#                 def get(self, request):
#                     role_result = UserInfo.objects.all()
#                     ser = Foreignkey_serializers(instance=role_result, many=True)
#                     data = ser.data
#                     json_data = json.dumps(data, ensure_ascii=False)
#                     return HttpResponse(json_data)
#
#         5 ModelSerializer定义depth参数
#
#             1 概念
#
#                 如果存在连表 显示链表对应外键成数的信息
#
#             1 使用
#
#                 model = UserInfo    # 指定模型
#                 fields = "__all__"  # 指定显示字段
#                 depth = 手动层数      # 数字类型
#
#         6 返回给前端的新型中添加链接（如连接添的内容是外键连接表的详细信息）
#
#             1 使用
#                 生成连接的字段使用 serializers.HyperlinkedIdentityFiled(view_name="视图name属性名", lookup_field='展示连接的字段',lookup_url_kwarg="url中的参数名")
#
#                 class Foreignkey_serializers(serializers.ModelSerializer):
#
#                     group = serializers.HyperlinkedIdentityField(view_name="test_link", lookup_field="group_id", lookup_url_kwarg="pk")
#                     class Meta:
#
#                         model = UserInfo    # 指定模型
#                         fields = "__all__" # 指定显示字段
#                         depth = 0
#
#                 class Test_show_foreignkey_serializers(APIView):
#
#                     def get(self, request):
#                         role_result = UserInfo.objects.all()
#                         ser = Foreignkey_serializers(instance=role_result, many=True, context={'request': request})
#                         data = ser.data
#                         json_data = json.dumps(data, ensure_ascii=False)
#                         return HttpResponse(json_data)
#
#         7 请求数据校验()
#
#             1 概念
#                 对前端发过来的数据进行校验
#
#
#             2 使用
#
#                 1 自定义创建类进行验规则
#
#                     class M_validate:
#
#                         def __init__(self):
#                             pass
#
#                         def __call__(self, value):
#                             print(value)
#                             if value == "22":
#                                 raise serializers.ValidationError('不/让你过')
#
#                     class My_validate(serializers.Serializer):
#                         role_name = serializers.CharField(validators=[M_validate()])
#
#
#                     class Test_validate(APIView):
#                         """对数据进行验证"""
#
#                         def get(self, request):
#
#                             return HttpResponse("验证数据")
#
#                         def post(self, request):
#                             ser = My_validate(data=request.data)
#                             if ser.is_valid():
#                                 print(ser.validated_data)
#                                 return HttpResponse(ser.validated_data)
#                             else:
#                                 print(ser.errors)
#                                 return HttpResponse(ser.errors)
#                 2 在序列化器中利用钩子函数进行自定义验证规则
#
#
#                     class My_validate(serializers.Serializer):
#                         role_name = serializers.CharField(validators=[M_validate()])
#
#                         def validata_字段名(self, value):
#                             # 若果不通过验证
#                             raise exceptions.validataionError('xxxx')
#                             # 如果通过验证
#                             return value
#
#     9 分页
#
#         1 分类
#             from rest_framework.pagination import ..
#             1 看第n页 每页显示n条数据 （PageNumberPagination）
#
#                 from rest_framework.pagination import PageNumberPagination
#                 class My_page(PageNumberPagination):
#                     page_size = 3   # 一页显示几条数据
#
#                     # Client can control the page using this query parameter.
#                     page_query_param = 'page'   # 在网页url中指定的翻页参数http://127.0.0.1:8000/test_page/?page=2
#
#                     page_size_query_param = None # 网页中指定的 每页显示多少条数据的参数
#
#                     max_page_size = 5  # 最大每页显示数据数
#
#                 class Test_girl_page(serializers.ModelSerializer):
#
#                     class Meta:
#
#                         model = Girls
#                         fields = "__all__"
#
#
#                 class Test_page(APIView):
#
#                     def get(self, request):
#
#                         data = Girls.objects.all()
#                         pg = My_page() # 创建对象
#                         page_data = pg.paginate_queryset(queryset=data, request=request, view=self) # 对数据显示进行设置
#
#                         ser = Test_girl_page(instance=page_data, many=True)
#
#                         return Response(ser.data)
#             2 在n个位置，向后查看n条数据(LimitOffsetPagination)
#                 from rest_framework.pagination import LimitOffsetPagination
#                 class My_page(LimitOffsetPagination):
#                     default_limit = 2       # 默认每页显示数据个数
#                     limit_query_param = 'limit'   # 指定url参数中显示的数据个数
#                     offset_query_param = 'offset' # 指定显示的位置
#                     max_limit = None        # 每页显示最大数据数
#
#                     ....替他同上
#             3 加密分页，上一页和下一页 (CursorPagination)
#                 from rest_framework.pagination import CursorPagination
#                     class My_page(CursorPagination):
#                         cursor_query_param = 'cursor'  # url中配置的参数
#                         page_size = 2       # 每页显示数据
#                         ordering = 'id'  # 按照排序的字段 “id”正序 "-id"倒叙
#
#
#
#                     class Test_girl_page(serializers.ModelSerializer):
#
#                         class Meta:
#
#                             model = Girls
#                             fields = "__all__"
#
#
#                     class Test_page(APIView):
#
#                         def get(self, request):
#
#                             data = Girls.objects.all()
#                             pg = My_page() # 创建对象
#                             page_data = pg.paginate_queryset(queryset=data, request=request, view=self) # 对数据显示进行设置
#
#                             ser = Test_girl_page(instance=page_data, many=True)
#
#                             return pg.get_paginated_response(ser.data) # 返回的内容带有下一页和上一页的url
#
#     10 视图
#
#         总结：
#
#             1 只使用基本的增删改查
#
#                 ModelViewSet
#
#             2 只是用增删
#
#                 CreateModelMixin, DestoryModelMixin, GenericViewSet
#
#             3 复杂逻辑
#
#                 GenericViewSet 或 APIView
#
#
#         1 GenericAPIView
#             一般不用
#
#         2 GenericViewSet
#
#             1 导入
#
#                 from rest_framework.viewsets import GenericViewSet
#
#             2 主要作用
#
#                 1 对 as_view()进行了重写
#                 2 视图中的方法可以自定义重命名
#                     url(r'^test_genericviewset/$', views.Test_view1.as_view({"get": "have"})),
#
#                     from rest_framework.viewsets import GenericViewSet
#
#                     class Test_view1(GenericViewSet):
#
#                         def have(self, request):  # 根据url中定义如果get请求执行have方法
#
#                             return Response('GenericView')
#
#         3 ListModelMixin（与GenericView一起用）
#
#             1 导入
#
#                 from rest_framework.mixins import ListModelMixin
#
#             2 作用
#
#                 分页集成类
#
#             3 使用
#
#                 url(r'test_listmodelmixin/$', views.Test_listmodelmixin.as_view({"get":"list"}))
#
#                 from rest_framework.pagination import PageNumberPagination
#                 class My_page(PageNumberPagination):
#                     page_size = 2
#
#                     page_query_param = 'page'
#
#                     page_size_query_param = None
#
#                     max_page_size = None
#
#                 class Test_girl_page(serializers.ModelSerializer):
#
#                     class Meta:
#
#                         model = Girls
#                         fields = "__all__"
#
#                 from rest_framework.mixins import ListModelMixin
#                 from rest_framework.viewsets import GenericViewSet
#
#                 class Test_listmodelmixin(ListModelMixin, GenericViewSet):
#                     queryset = Girls.objects.all()
#                     serializer_class = Test_girl_page
#                     pagination_class = My_page
#
#         4 CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
#
#             1 作用
#
#                 增删改查 的封装
#
#             2 使用
#
#                 只需要 指定集合 指定序列化器 对于 RetrieveModelMixin，UpdateModelMixin，DestroyModelMixin需要在url中指定pk
#                 其他用法同上
#
#         5 ModelViewSet
#
#             1 作用
#
#                 继承了4 中的所有方法 和 GenericView方法
#
#             2 使用
#
#                 1 导入
#
#                     from rest_framework.viewsets import ModelViewSet
#
#                 2 使用（url需要创建两个 一个针对所有数据，一个针对单个数据（pk））
#
#                     url(r'^test_modelviewset/$', views.Test_modelviewset.as_view({'get':"list"})),
#
#                     # 定义了获取单个，删除单个，查询单个的方法（去源代码中找）
#                     url(r'^test_modelviewset/(?P<pk>\d+)/$', views.Test_modelviewset.as_view({'get':'retrieve','put':'update', 'delete':'destroy'})),
#
#                     class GirlsSerializer1(serializers.ModelSerializer):
#
#                         class Meta:
#                             model = Girls
#                             fields = '__all__'
#
#                     from rest_framework.viewsets import ModelViewSet
#
#                     class Test_modelviewset(ModelViewSet):
#
#                         queryset = Girls.objects.all()
#                         serializer_class = GirlsSerializer1
#
#     11 路由
#
#         http://127.0.0.1:8000/test_modelviewset/?format=json  # 生成不渲染json数据 第一种
#         http://127.0.0.1:8000/test_modelviewset.json    # 生产部渲染json数据 第二种
#         http://127.0.0.1:8000/test_modelviewset/
#         http://127.0.0.1:8000/test_modelviewset/(?P<pk>\d+)/
#
#         自动生成以上4中路由
#
#             router = routers.DefaultRouter()
#             router.register(r'test_modelviewset', views.yyy)
#
#             urlpatterns = {
#                 url(r'^/', include(router.urls))
#             }
#
#     12 渲染器
#
#         0 作用
#
#             返回好看的数据
#
#         1 原理
#
#             class Test(APIView):
#
#                 render_classes = [JSONRenderer, BrowableAPIRenderer] 通过此类可以执行渲染器 一个知识json数据，一个经过浏览器渲染（建议放配置文件中）
#
#                 def get(self, request):
#
#                     .....
#
#
#     13 django组件 contenttype
#
#         1 概念
#
#             django内置组件，用于连表操作
#
#         2 适用于
#
#             一张表和多张表进行关联的时候
#
#         3 使用
#
#             1 手动创建
#
#                 class A(models.Model):
#                     a = models.CharField()
#
#                 class B(models.Model):
#                     b = models.CharField()
#
#                 class C(models.Model):
#                     c = models.CharField()
#
#                     table_name = models.CharField(verbose_name='关联的表名称')
#                     object_id = models.CharField(verbose_name="关联的表中的数据行ID")
#
#             2 自动创建
#
#                 from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
#                 from django.contrib.contenttypes.models import ContentType # django自动创建的表将该表存储着django中所有创建的表名
#
#                 class A(models.Model):
#                     a = models.CharField()
#                     a_c_list = GenericRelation("C")  # 仅用于反向查找，不生成字段
#                 class B(models.Model):
#                     b = models.CharField()
#
#                 class C(models.Model):
#                     c = models.CharField()
#
#                     table_name = models.ForeignKey(ContentType, Verbose_name="关联的表名称")
#                     table_id = models.IntegerField(verbose_name="关联的表中的数据行ID")
#
#                     content_object = GenericForeignkey('table_name', 'table_id') # 帮助快速实现content_type操作
#
#                 添加数据的时候
#
#                     obj = A.objects.filter(a="111").first()
#                     C.objects.create(c="9.9", content_object=obj)
#
#                 获取表关联对象的所有信息
#
#                     A.a_c_list.all()
#
#
# --------------------------------------------------
1
# --------------------------------------------------

1
# -i https://pypi.douban.com/simple
#
#
#
# django的models定义表名
#
#     class xx(..):
#         class Meta:
#             db_table = "表名"
#
# --------------------------------------------------
# django的模块导入
#
#     如果出现找不到模块的问题
#         pycharm中 右键项目目录 mark director as 选择 source director # 标记根目录
# --------------------------------------------------

#
#
#
# --------------------------------------------------
# django概念
#
# django的MTV模式

#
#
# vue和django csrf_token解决
#
#     1.在django的view里设置request的cookie，让他带csrftoke。
#
#     2.修改前端的代码，获取cooke和请求头里的token值做比较。
# --------------------------------------------------
1
# --------------------------------------------------




1
# django解决css文件更改后由于缓存问题页面不跟新
#
#     1 解决问题思路
#         基于md5解决根据js, css的内容生成一个字符串，
#         当js，css繁盛改变的时候字符串也会随之更改
#     2 解决流程
#         1 设置STATICFILES_STORAGE
1
# --------------------------------------------------
#
#
#
#
# --------------------------------------------------
1
# django静态文件在模板中导入,使用
#     {% load static %}
#         {% static '路径' %}
1
# --------------------------------------------------
#
#
#
# --------------------------------------------------
1
# 批量向数据库中插入数据
#     知识点
#         xx.objects.bulk_create(对象列表)
#     步骤
#         1 创建空列表
#             a = []
#         2 将对象插入孔列表
#             a.append(obj)
#         3 执行批量插入操作
#             xx.objects.bulk_create(a)
1
# --------------------------------------------------
#
#
# --------------------------------------------------
1
# url根目录的路径配置
#     url(r'^$', views.xxxx)
# --------------------------------------------------
1
#
# --------------------------------------------------
1
# django返回json数据
#     知识点：
#         json.dumps(xx)
#     例子
#         from django.http import HttpResponse
#         def return_jsondata(request):
#             data = {"a": 1}
#             json_data = json.dumps(data)
#             return HttpResponse(json_data)
1
# --------------------------------------------------
#
#
# --------------------------------------------------
1
# django返回中文json数据
#     知识点：
#         json.dumps(xx, ensure_ascii=False)
#     例子
#         from django.http import HttpResponse
#         def return_cn_jsondata(request):
#             data = {"a": "我"}
#             json_cn_data = json.dumps(data, ensure_ascii=False)
#             return HttpResponse(json_cn_data)
1
# --------------------------------------------------
#
#
# --------------------------------------------------
1
# GET请求方式的参数添加
#
#     /aaaa?b=2  get 参数rul的添加方式
#     r'^aaaa/$'  路由匹配
1
# --------------------------------------------------
#
#
# --------------------------------------------------
1
# django获取GET请求参数
#     知识点
#         request.GET.get('参数的键值')
1
# --------------------------------------------------


1
# --------------------------------------------------
# django获取单个上传文件并存储到指定路径
#     知识点
#         0 概念        保存上传文件前，数据需要存放在某个位置。默认当上传文件小于2.5M时，
#                         django会将上传文件的全部内容读进内存。从内存读取一次，写磁盘一次。
#                         但当上传文件很大时，django会把上传文件写到临时文件中，然后存放到系统临时文件夹中。
#         1 form                      # form表单提交，别忘了csrf
#         2 method                    # 提交的方式
#         3 enctype                   # 提交文件form必须要有的属性enctype="multipart/form-data"
#         4 type="file" name="xx"     # 提交文件input的type属性file
#         5 request.method  == "POST"          # 后端获取提交的方式 "POST"必须大写
#         6 request.FILES.get('xx')   # 后端根据name指定的名字获取文件对象
#         7 request.FILES.get('xx').name  # 获取传输文件的名字
#
#     <form action="/update_one_file/" method="post" enctype="multipart/form-data">
#         <input type="file" name="file_obj" >
#         <input type="submit">
#     </form>
#
#     def update_one_file(request):
#         if request.method == "POST":
#             file = request.FILES.get('file_obj')
#             with open(os.getcwd()+'\\static\\save_update_file\\'+file.name, 'wb')as f:
#                 for i in file:
#                     f.write(i)
#
#         return render(request, 'update_one_file.html')
#
#
#
#
#
# --------------------------------------------------
1
#
1
# --------------------------------------------------
# django获取多个上传文件并存储到指定路径
#
#     知识点
#         1 multiple                      # 上传多个文件添加的属性
#         2 request.FILES.getlist('xxxx') # 获取多个上传文件的对象列表
#
#     html
#         <form action="/put_database/" method="post" enctype="multipart/form-data">
#             <input type="file" multiple  name="files">
#
#         </form>
#     views.py
#         files = request.FILES.getlist('files')
# --------------------------------------------------
1
#
1
# --------------------------------------------------
# django注意事项
#
# django QuerySet类型不支持负索引
#
# request.methods == 'xx'  xx中必须为大写
#
#
# 类装饰器
#     CSRF Token相关装饰器在CBV只能加到dispatch方法上，或者加在视图类上然后name参数指定为dispatch方法。
#     csrf_protect，为当前函数强制设置防跨站请求伪造功能，即便settings中没有设置全局中间件。
#     csrf_exempt，取消当前函数防跨站请求伪造功能，即便settings中设置了全局中间件。
# --------------------------------------------------
1
#
1
# --------------------------------------------------
# django 将QuerySet转换为列表类型
#     list（QuerySet）
# --------------------------------------------------
#
#
# --------------------------------------------------
# django 设置cookies
#
#     def set_cookies(request):
#     ref = HttpResponse('我设置了cookies')
#     ref.set_cookie('a','100')
#     return ref
# --------------------------------------------------
#
#
#
#
# --------------------------------------------------
# django的CBV (用类相应用户请求GET)
#     知识点
#         1 View                  # 导入Views模块
#         2 views.xx.as_view()    # url使用的方法
#         3 class xx(View)        # 类继承View
#         4 def get(self, request)# get方法也需要有request参数
#
#
#         url(r'^cbv_get/$', views.Cbv_get.as_view()),
#
#         from django.views import View
#         class Cbv_get(View):
#             def get(self, request):
#                 return HttpResponse('cbc_get')
# --------------------------------------------------
#
#
# --------------------------------------------------
# django的CBV (用类相应用户请求POST)
#     知识点
#         def post(self, request)      接收用户POST请求的post方法
#
#     class Cbv_post(View):
#         def post(self, request):
#             return HttpResponse('cbv_post')
# --------------------------------------------------
#
#
# --------------------------------------------------
# CBV中的dispatch方法
#     知识点
#         执行顺序
#             1 浏览器提交请求去执行dispatch方法
#             2 走到ret 执行父类的dispatch方法，然后去执行get或post请求
#             3 通过post或get请求返回response对象之后，在执行dispatc函数中的 return ret 返回给浏览器
#
#     def dispatch(self, request, *args, **kwargs):
#
#         ret = super().dispatch(request, *args, **kwargs)
#         return ret
#     def get(self, request)
#         ...
#     def post(self, request)
#         ...
# --------------------------------------------------
#
#
# --------------------------------------------------
# CBV中get或post方法上添加装饰器
#     知识点
#         1 method_decorator
#         2 @method_decorator(xxx)
#
# --------------------------------------------------
#
#
# --------------------------------------------------
#
# cbv单独添加装饰器到get方法上（单独加在post方法上也是一样）
#     知识点
#         1 装饰器函数的位置          装饰器如果和类在同一个文件中必须写在类的上面要不找到
#         2 method_decorator          导入模块 from django.utils.decorators import method_decorator
#         3 @method_decorator（xx）   需要在哪个上面加上装饰器就在这个方法上面加并且括号内是装饰器的名字
#         4 装饰器中必须返回的函数     必须返回传进来的函数
#
# from django.utils.decorators import method_decorator
# def test_decorator(func):
#     def waraper(*args, **kwargs):
#         ret = func(*args, **kwargs)
#         print('我是装饰器')
#         return ret
#     return waraper
#
#
# class GetPostDecorator(View):
#
#     @method_decorator(test_decorator)
#     def get(self, request):
#         return HttpResponse('装饰器get')
#     def post(self, request):
#         pass
# --------------------------------------------------
#
#
# --------------------------------------------------
# cbv 是get和post方法全部加上装饰器
#     1.第一种思想，两个方法智商分别添加@method_decorator（xx）
#     2.第二种思想，加载dispatch方法上，因为执行get和post方法之前都先执行dispatch方法
#
#     知识点
#         1 dispatch                                   装饰器装饰在dispatch方法之上
#         1 super().dispatch(request, *args, **kwargs) dispatch方法继承父方法
# def test_decorator2(func):
#     def waraper(*args, **kwargs):
#         ret = func(*args, **kwargs)
#         print('我是装饰器')
#         return ret
#     return waraper
#
# from django.utils.decorators import method_decorator
# class DispatchDecorator(View):
#
#     @method_decorator(test_decorator2)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def get(self, request):
#         return HttpResponse('get dispatch装饰器')
#
#     def post(self, request):
#         return HttpResponse('post dispatch装饰器')
# --------------------------------------------------
#
# --------------------------------------------------
# cbv将装饰器加载视图类之上
#     知识点
#         1 method_decorator位置    写在类的上面
#         2 name=“xx”             用name属性指定被装饰的函数 method_decorator（xxx， name=“yy”）
#
# def test_decorator3(func):
#     def waraper(*args, **kwargs):
#         ret = func(*args, **kwargs)
#         print('我是装饰器')
#         return ret
#     return waraper
#
# from django.utils.decorators import method_decorator
#
# method_decorator(test_decorator3, name="get")
# method_decorator(test_decorator3, name="post")
# class UpClassDecorator(View):
#
#     def get(self, request):
#         return HttpResponse('类上装饰器get')
#     def post(self, request):
#
#         return HttpResponse('类上装饰器post')
# --------------------------------------------------
#
#
# --------------------------------------------------
# HttpResponse
#     知识点
#         1 过程 通过浏览器提交请求会走到 urls.py文件中 搜索路径根据路径的对应关系 执行函数
#         2 HttpResponse模块    # from django.shortcuts import HttpResponse
#         3 request             # 保存了所有和用户浏览器请求的相关数据
#
#     def index(request):
#         # request 保存了所有和用户浏览器请求的相关数据
#         print(request)
#         return HttpResponse("hello") # 返回响应字符串
# --------------------------------------------------
#
#
#
# --------------------------------------------------
# render
#     知识点
#         1  render 方法  from django.shortcuts import render
#         2  参数
#             return render(
#                 request    # 固定写法，用于生成相应的请求对象
#                 remplate_name   # 要使用模板的名字 可选
#                 context: 传给模板的 可选
#                 content_type   #生成的文档要使用的MIME类型。默认为 DEFAULT_CONTENT_TYPE 设置的值。默认为'text/html' 可选
#                 status: 相应状态码 默认200 可选
#                 useing:用于加载模板的引擎名 可选
#               )
#
# --------------------------------------------------
#
#
# --------------------------------------------------
# redirect
#     1 顺序
#         客户端发送请求 ---> 服务器返回重定向状态码302--客户根据重定向路径获取路径内容-->返回状态码200
#     1 redirect方法
#     2 参数
#         一个模型：将调用模型的get_absolute_url() 函数
#             object = MyModel.objects.get(...)
#             return redirect(object)
#         一个视图，可以带有参数：将使用urlresolvers.reverse 来反向解析名称
#         一个绝对的或相对的URL，将原封不动的作为重定向的位置。
#
#     3 永久重定向和临时重定向
#         它主要面向的是搜索引擎的机器人。
#         A页面临时重定向到B页面，那搜索引擎收录的就是A页面。
#         A页面永久重定向到B页面，那搜索引擎收录的就是B页面。
#         默认返回一个临时的重定向；
#         传递permanent=True 可以返回一个永久的重定向。
#
#     class ReturnRedirect(View):
#     def get(self, request):
#         return redirect("http://www.baidu.com")
#
# --------------------------------------------------
#
#
# --------------------------------------------------
# django请求流程(客户发起请求到拿到结果的django流程)
# 	1 浏览器发送请求
# 	2 wsgiref模块接受消息对消息进行拆分(python内置的一个收发消息的模块)
# 	2.5 中间件
# 	3 执行url.py(设置url和需要执行函数的对应关系)
# 	4 执行views.py(定义逻辑处理函数,执行render等..)
# 	5 执行views.py之后 将消息返回给 wsgiref模块
# 	6 wsgiref模块将响应消息发送给浏览器
# --------------------------------------------------
#
1

1
# --------------------------------------------------
# request对象
#     当一个页面被请求时，Django就会创建一个包含本次请求原
#     信息的HttpRequest对象。Django会将这个对象自动传递给响应的视图函数，
#     一般视图函数约定俗成地使用 request 参数承接这个对象。
#
#
#
# <a href="HttpRequest_obj">
# request请求相关属性
#     django将请求报文中的请求行、头部信息、内容主体封装成
#     HttpRequest 类中的属性。除了特殊说明的之外，其他均为只读的。
#     0.HttpRequest.scheme
#        表示请求方案的字符串（通常为http或https）
#
#         http
#
#     1.HttpRequest.body
#     　　一个字符串，代表请求报文的主体。在处理非 HTTP 形式的报文时非常有用，
#     例如：二进制图片、XML,Json等。但是，如果要处理表单数据的时候，
#     推荐还是使用 HttpRequest.POST 。另外，我们还可以用 python 的类文
#     方法去操作它，详情参考 HttpRequest.read() 。
#
#
#     2.HttpRequest.path
#     　　一个字符串，表示请求的路径组件（不含域名）。
#         /HttpRequest_obj/
#
#
#     3.HttpRequest.method
#     　　一个字符串，表示请求使用的HTTP 方法。必须使用大写。
#     　　
#         GET
#
#
#
#     4.HttpRequest.encoding
#         一个字符串，表示提交的数据的编码方式（如果为 None 则表示使用
#         DEFAULT_CHARSET 的设置，默认为 'utf-8'）。
#         这个属性是可写的，你可以修改它来修改访问表单数据使用的编码。
#         接下来对属性的任何访问（例如从 GET 或 POST 中读取数据）将使用新的 encoding 值。
#         如果你知道表单数据的编码不是 DEFAULT_CHARSET ，则使用它。
#
#         None
#
#
#     5.HttpRequest.GET
#         一个类似于字典的对象，包含 HTTP GET 的所有参数。
#         详情请参考 QueryDict 对象。
#
#         <QueryDict: {}>
#
#
#     6.HttpRequest.POST
#         一个类似于字典的对象，如果请求中包含表单数据，则将这些数据封装成 QueryDict 对象。
#         POST 请求可以带有空的 POST 字典 —— 如果通过 HTTP POST 方法发送一个表单，
#         但是表单中没有任何的数据，QueryDict 对象依然会被创建。
#         因此，不应该使用 if request.POST  来检查使用的是否是POST 方法；
#         应该使用 if request.method == "POST"
#         另外：如果使用 POST 上传文件的话，文件信息将包含在 FILES 属性中。
#
#         <QueryDict: {}>
#
#
#     7.HttpRequest.COOKIES
#         一个标准的Python 字典，包含所有的cookie。键和值都为字符串。
#
#         {}
#
#     8.HttpRequest.FILES
#         一个类似于字典的对象，包含所有的上传文件信息。
#         FILES 中的每个键为<input type="file" name="" /> 中的name
#         ，值则为对应的数据。注意，FILES 只有在请求的方法为POST 且提交的<form>
#         带有enctype="multipart/form-data" 的情况下才会包含数据。否则，
#         FILES 将为一个空的类似于字典的对象。
#
#         <MultiValueDict: {}>
#
#
#
#     9.HttpRequest.META
#         一个标准的Python 字典，包含所有的HTTP 首部。具体的头部信息取决于客户端和服务器，
#         下面是一些示例：
#             CONTENT_LENGTH —— 请求的正文的长度（是一个字符串）。
#             CONTENT_TYPE —— 请求的正文的MIME 类型。
#             HTTP_ACCEPT —— 响应可接收的Content-Type。
#             HTTP_ACCEPT_ENCODING —— 响应可接收的编码。
#             HTTP_ACCEPT_LANGUAGE —— 响应可接收的语言。
#             HTTP_HOST —— 客服端发送的HTTP Host 头部。
#             HTTP_REFERER —— Referring 页面。
#             HTTP_USER_AGENT —— 客户端的user-agent 字符串。
#             QUERY_STRING —— 单个字符串形式的查询字符串（未解析过的形式）。
#             REMOTE_ADDR —— 客户端的IP 地址。
#             REMOTE_HOST —— 客户端的主机名。
#             REMOTE_USER —— 服务器认证后的用户。
#             REQUEST_METHOD —— 一个字符串，例如"GET" 或"POST"。
#             SERVER_NAME —— 服务器的主机名。
#             SERVER_PORT —— 服务器的端口（是一个字符串）。
#         从上面可以看到，除 CONTENT_LENGTH 和 CONTENT_TYPE 之外，
#         请求中的任何 HTTP 首部转换为 META 的键时，
#         都会将所有字母大写并将连接符替换为下划线最后加上 HTTP_  前缀。
#         所以，一个叫做 X-Bender 的头部将转换成 META 中的 HTTP_X_BENDER 键。
#
#         {
#         'FP_NO_HOST_CHECK': 'NO',
#         'VIRTUAL_ENV': 'D:\\project\\git_cangku\\learn_django\\test_django_all\\venv',
#         'LOCALAPPDATA': 'C:\\Users\\Administrator\\AppData\\Local',
#         'PROGRAMFILES(X86)': 'C:\\Program Files (x86)',
#         'PROGRAMDATA': 'C:\\ProgramData',
#         'COMPUTERNAME': 'USER-20190202MM',
#         'PROCESSOR_LEVEL': '6',
#         'SESSIONNAME': 'Console',
#         'TMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp',
#         'PATH': 'D:\\project\\git_cangku\\learn_django\\test_django_all\\venv\\Scripts;C:\\Program Files\\Python36\\Scripts\\;C:\\Program Files\\Python36\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files\\nodejs\\;C:\\Users\\Administrator\\AppData\\Roaming\\npm;D:\\soft\\vscode\\Microsoft VS Code\\bin;D:\\soft\\pycharm\\PyCharm 2018.3.4\\bin;',
#         'PROGRAMFILES': 'C:\\Program Files',
#         'SYSTEMROOT': 'C:\\Windows',
#         'TERMINAL_EMULATOR': 'JetBrains-JediTerm',
#         'COMMONPROGRAMFILES(X86)': 'C:\\Program Files(x86)\\Common Files',
#         '_OLD_VIRTUAL_PATH': 'C:\\Program Files\\Python36\\Scripts\\;C:\\Program Files\\Python36\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files\\nodejs\\;C:\\Users\\Administrator\\AppData\\Roaming\\npm;D:\\soft\\vscode\\Microsoft VS Code\\bin;D:\\soft\\pycharm\\PyCharm 2018.3.4\\bin;',
#         '_DFX_INSTALL_UNSIGNED_DRIVER': '1',
#         '_OLD_VIRTUAL_PROMPT': '$P$G',
#         'WINDIR': 'C:\\Windows',
#         'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 15 Stepping 11, GenuineIntel',
#         'PROGRAMW6432': 'C:\\Program Files',
#         'TEMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp',
#         'PSMODULEPATH': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\',
#         'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files',
#         'PYCHARM': 'D:\\soft\\pycharm\\PyCharm 2018.3.4\\bin;',
#         'NUMBER_OF_PROCESSORS': '4',
#         'WINDOWS_TRACING_FLAGS': '3',
#         'PROCESSOR_REVISION': '0f0b',
#         'PROMPT': '(venv) $P$G',
#         'USERNAME': 'Administrator',
#         'COMSPEC': 'C:\\Windows\\system32\\cmd.exe',
#         'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files',
#         '__INTELLIJ_COMMAND_HISTFILE__': 'C:\\Users\\Administrator\\.PyCharm2018.3\\config\\terminal\\history\\history-7',
#         'PROCESSOR_ARCHITECTURE': 'AMD64',
#         'USERDOMAIN': 'USER-20190202MM',
#         'PUBLIC': 'C:\\Users\\Public',
#         'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW',
#         'HOMEPATH': '\\Users\\Administrator',
#         'WINDOWS_TRACING_LOGFILE': 'C:\\BVTBin\\Tests\\installpackage\\csilogfile.log',
#         'APPDATA': 'C:\\Users\\Administrator\\AppData\\Roaming',
#         'SYSTEMDRIVE': 'C:',
#         'LOGONSERVER': '\\\\USER-20190202MM',
#         'OS': 'Windows_NT',
#         'HOMEDRIVE': 'C:',
#         'ALLUSERSPROFILE': 'C:\\ProgramData',
#         'USERPROFILE': 'C:\\Users\\Administrator',
#         'DJANGO_SETTINGS_MODULE': 'all_django.settings',
#         'RUN_MAIN': 'true',
#         'SERVER_NAME': 'USER-20190202MM',
#         'GATEWAY_INTERFACE': 'CGI/1.1',
#         'SERVER_PORT': '8000',
#         'REMOTE_HOST': '',
#         'CONTENT_LENGTH': '',
#         'SCRIPT_NAME': '',
#         'SERVER_PROTOCOL': 'HTTP/1.1',
#         'SERVER_SOFTWARE': 'WSGIServer/0.2',
#         'REQUEST_METHOD': 'GET',
#         'PATH_INFO': '/HttpRequest_obj/',
#         'QUERY_STRING': '',
#         'REMOTE_ADDR': '127.0.0.1',
#         'CONTENT_TYPE': 'text/plain',
#         'HTTP_HOST': '127.0.0.1:8000',
#         'HTTP_CONNECTION': 'keep-alive',
#         'HTTP_CACHE_CONTROL': 'max-age=0',
#         'HTTP_UPGRADE_INSECURE_REQUESTS': '1',
#         'HTTP_USER_AGENT': 'Mozilla/5.0 (WindowsNT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',
#         'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#         'HTTP_REFERER': 'http://127.0.0.1:8000/',
#         'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br',
#         'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9',
#         'wsgi.input': <_io.BufferedReader name=760>,
#         'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>,
#         'wsgi.version': (1, 0),
#         'wsgi.run_once': False,
#         'wsgi.url_scheme': 'http',
#         'wsgi.multithread': True,
#         'wsgi.multiprocess': False,
#         'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>}
#
#
#
#
#     10.HttpRequest.user
#         一个 AUTH_USER_MODEL 类型的对象，表示当前登录的用户。
#         如果用户当前没有登录，user 将设置为 django.contrib.auth.models.AnonymousUser
#         的一个实例。你可以通过 is_authenticated() 区分它们。
#             例如：
#             if request.user.is_authenticated():
#                 # Do something for logged-in users.
#             else:
#                 # Do something for anonymous users.
#         user 只有当Django 启用 AuthenticationMiddleware 中间件时才可用。
#
#         AnonymousUser
#
#
#           匿名用户
#           class models.AnonymousUser
#           django.contrib.auth.models.AnonymousUser 类实现了
#           django.contrib.auth.models.User 接口，但具有下面几个不同点：
#             id 永远为None。
#             username 永远为空字符串。
#             get_username() 永远返回空字符串。
#             is_staff 和 is_superuser 永远为False。
#             is_active 永远为 False。
#             groups 和 user_permissions 永远为空。
#             is_anonymous() 返回True 而不是False。
#             is_authenticated() 返回False 而不是True。
#             set_password()、check_password()、save() 和delete() 引发 NotImplementedError。
#           New in Django 1.8:
#           新增 AnonymousUser.get_username() 以更好地模拟 django.contrib.auth.models.User。
#
#
#
#     11.HttpRequest.session
#      　　一个既可读又可写的类似于字典的对象，表示当前的会话。
#         只有当Django 启用会话的支持时才可用。
#         完整的细节参见会话的文档。
#
#         <django.contrib.sessions.backends.db.SessionStore object at 0x00000000044F6B70>
#
#
# request请求相关方法
#
#     1.HttpRequest.get_host()
#     　　根据从HTTP_X_FORWARDED_HOST（如果打开 USE_X_FORWARDED_HOST，默认为False）
#         和 HTTP_HOST 头部信息返回请求的原始主机。如果这两个头部没有提供相应的值，
#         则使用SERVER_NAME 和SERVER_PORT，在PEP 3333 中有详细描述。
#     　　USE_X_FORWARDED_HOST：一个布尔值，用于指定是否优先使用 X-Forwarded-Host 首部，
#         仅在代理设置了该首部的情况下，才可以被使用。
#     　　例如："127.0.0.1:8000"
#     　　注意：当主机位于多个代理后面时，get_host() 方法将会失败。除非使用中间件重写代理的首部。
#
#         127.0.0.1:8000
#
#
#     2.HttpRequest.get_full_path()
#     　　返回 path，如果可以将加上查询字符串。
#     　　例如："/music/bands/the_beatles/?print=true"
#
#         /HttpRequest_obj/
#
#
#
#     3.HttpRequest.get_signed_cookie(key, default=RAISE_ERROR, salt='', max_age=None)
#
#     　　返回签名过的Cookie 对应的值，如果签名不再合法则返回django.core.signing.BadSignature。
#     　　如果提供 default 参数，将不会引发异常并返回 default 的值。
#     　　可选参数salt 可以用来对安全密钥强力攻击提供额外的保护。
#       max_age 参数用于检查Cookie 对应的时间戳以确保Cookie 的时间不会超过max_age 秒。
#
#
#         >>> request.get_signed_cookie('name')
#         'Tony'
#         >>> request.get_signed_cookie('name', salt='name-salt')
#         'Tony' # 假设在设置cookie的时候使用的是相同的salt
#         >>> request.get_signed_cookie('non-existing-cookie')
#         ...
#         KeyError: 'non-existing-cookie'    # 没有相应的键时触发异常
#         >>> request.get_signed_cookie('non-existing-cookie', False)
#         False
#         >>> request.get_signed_cookie('cookie-that-was-tampered-with')
#         ...
#         BadSignature: ...
#         >>> request.get_signed_cookie('name', max_age=60)
#         ...
#         SignatureExpired: Signature age 1677.3839159 > 60 seconds
#         >>> request.get_signed_cookie('name', False, max_age=60)
#         False
#
#
#     4.HttpRequest.is_secure()
#     　　如果请求时是安全的，则返回True；即请求通是过 HTTPS 发起的。
#
#         False
#
#     5.HttpRequest.is_ajax()
#     　　如果请求是通过XMLHttpRequest 发起的，则返回True，
#       方法是检查 HTTP_X_REQUESTED_WITH 相应的首部是否是字符串'XMLHttpRequest'。
#       大部分现代的 JavaScript 库都会发送这个头部。如果你编写自己的 XMLHttpRequest
#       调用（在浏览器端），你必须手工设置这个值来让 is_ajax() 可以工作。
#
#     　　如果一个响应需要根据请求是否是通过AJAX 发起的，并且你正在使用某种形式的缓存例如Django
#       的 cache middleware，
#       你应该使用 vary_on_headers('HTTP_X_REQUESTED_WITH') 装饰你的视图以让响应能够正确地缓存。
#
#         False
#
#     6.request.POST.getlist("hobby")
#         键值对的值是多个的时候,比如checkbox类型的input标签，select标签，需要用：
# --------------------------------------------------
#
#
#
#
# --------------------------------------------------
# Response对象
#     与由Django自动创建的HttpRequest对象相比，
#     HttpResponse对象是我们的职责范围了。我们写的每个视图都需要实例化
#     ，填充和返回一个HttpResponse。
#     HttpResponse类位于django.http模块中
#
# 使用HttpResponse
#     传递字符串
#     class HttpResponseObj(View):
#         def get(self, request):
#             s = HttpResponse('haha')
#             return s
#
#     设置或删除响应头信息
#     class HttpResponseObj(View):
#         def get(self, request):
#             response = HttpResponse()
#             response['Content-Type'] = 'text/html; charset=GBK'
#             return response
#
# HttpResponse属性
#     HttpResponse.content：响应内容
#
#         response = HttpResponse('haha')
#         s = response.content
#         print(s)
#
#         b'haha'
#
#     HttpResponse.charset：响应内容的编码
#
#         response = HttpResponse('haha')
#         s = response.charset
#         print(s)
#
#         uft-8
#
#     HttpResponse.status_code：响应的状态码
#
#         response = HttpResponse('haha')
#         s = response.status_code
#         print(s)
#
#         200
#
# JsonResponse对象
#     1 作用             生成JSON编码的响应
#     1 JsonResponse     对象的导入 from django.http import JsonResponse
#     2 dict字典         默认清空下只允许传递字典类型
#     3 safe=False        若想传递非字典类型
#
#     传递字典类型
#     from django.http import JsonResponse
#     class JsonResponseObj(View):
#         def get(self, request):
#             jsonResponse = JsonResponse({'aa':1})
#             return jsonResponse
#
#     传递非字典类型
#     from django.http import JsonResponse
#     class JsonResponseObj(View):
#         def get(self, request):
#             jsonResponse = JsonResponse('aa', safe=False)
#             return jsonResponse
#
# --------------------------------------------------
# 在Python脚本中调用Django环境
#     import os
#     if __name__ == '__main__':
#         os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BMS.settings")
#         import django
#         django.setup()
#
#         from app01 import models
#
#         books = models.Book.objects.all()
#         print(books)
# --------------------------------------------------
#
1