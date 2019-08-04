# ======================================================================================
# flask 我爱房屋项目

1 在单一文件中构建所有依赖工具（然后逐一拆解到其他模块）

    1 创建manage.py文件

        配置信息类
            DEBUG
            SECRET_KEY

            # 数据库
            SQLALCHEMY_DATABASE_URI
            SQLALCHEMY_TRACK_MODIFICATIONS

            app.config.form_object(xx)

            # redis
            REDIS_HOST = "ip:port"
            REDIS_PORT = 6317

            # session配置(配合了flask-session)
            SESSION_TYPE = "redis"
            SESSION_REDIS = redis.StricRedis(host=xx, prot=6379)
            SESSION_USE_SIGNER = True # 对cookie中的session_id进行隐藏
            PERMANENT_SESSION_LIFETIME = 86400 # session数据的有效期


        数据库对象

        redis对象

            import redis
            redis_store = redis.StricRedis(host=xx, port=6379)

        session储存位置设置(flask默认session存在浏览器)

            1 安装flask-session工具

                pip3 install flask-session

            2 使用
                from flask_session import Session

                # 利用flask-session,将sessin数据保存到redis中
                Session(app) # 修改了flask的中的session的默认机制


        添加csrf防护机制
            from flask_wtf import CSRFProtect
            CSRFProtect(app)

2 拆分文件manage.py

    0 项目推荐目录

        ihome
            /蓝图目录1.0   # 按照版本区分
                __init__.py
                views.py
            /__init__.py
        static
        utils
        config.py
        manage.py


    1 配置文件

        config.py

        # 基本配置信息
        class Config:

        # 开发模式配置
        class DevelopmentConfig(Config):
            DEBUG = True

        # 生存环境配置
        class ProductConfig(Config)

        # 构建映射关系
        config_map = {
            "develop": DevelopmentConfig,
            "product": ProductConfig
        }

        # manage.py中使用函数模式创建app
        from xx import config_map
        def create_app(config_name):

            app = Flask(__name__)

            config_class = config_map.get(config_name)
            app.config.form_object(config_class)

            return app

        app = create_app("develop")

    2 __init__.py

        # 注册蓝图
        from ihome import 蓝图目录1.0

        db = SQLALchemy()

        redis_store = None

        create_app函数

            db.init_app(app) # 避免延迟导入 创建SQLALchemy对象不能绑定到app对象的问题

            # 初始化redis
            global redis_store
            redis_store = redis.StricRedis(xx)

            Session(app)

            CSRFProtect(app)

            # 注册蓝图
            app.register_bluprint(蓝图目录1.api, url_prifix="xxx")

    3 manage.py

        只进行启动
        app = create_app("xx")
        manager = Manager(app)

        Migrate(app, db)
        manager.add_command("db", MigrateCommand)

        manage.run() # 启动

    4 蓝图目录1.0下__init__.py文件

        from flask import Blueprint
        api = Blueprint("api_1_0")

        # 注册views.py
        from . import view

    5 蓝图目录1.0下views.py

        from . import api

        @api.route("/index")
        def xx():
            ...

    6 循环引入的问题
        在create_app中导入
# =====================================================================================




# ======================================================================================
# # flask 微信公众号开发项目
1
#
#     1 介绍
#
#         1 公众号消息会话开发流程（需要公网ip）
#
#                       发送消息           转发消息
#                     -------->           --------->
#             微信客户端           微信服务器           开发者服务器
#                     <---------          <---------
#                      回复消息          返回响应消息
#
#
#         2 公众号内网页开发流程
#
#                         转发消息        寻求用户信息
#                     -------->         --------->
#             微信客户端         网页服务器         微信者服务器
#                     <---------        <---------
#                     返回网页            返回用户信息
#
#         3 开发文档
#             https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1445241432
#
#
1
# ======================================================================================





# ======================================================================================
# django天天生鲜项目
1
# 1 项目介绍

    # 1 电商

    #     B2B 企业对企业 阿里巴巴
    #     C2C 个人对个人 淘宝
    #     B2C 企业对个人 唯品会
    #     C2B 个人对企业 海尔商城 商品定制
    #     O2O 线上到线下 美团
    #     F2C 工厂到个人 戴尔
    #     B2B2C  企业企业个人 京东 天猫

    # 2 项目开发流程


        # 1 项目立项(做什么项目)
        #
        # 2 需求分析(功能分析)
        #
        # 3 原型设计(产品原型图 软件axure rp)
        #
        #     (后端)3.1架构设计 ---3.2数据库设计 ---3.3模块代码实现和单元测试代码
        #             3.1
        #                 1 模块划分
        #                 2 开发环境选择
        #                 3 其他技术
        #                 4 部署架构
        #             3.2
        #                 1 分析数据表和表字段
        #                 2 表关系
        #             3.3
        #                 实现代码
        #
        #     (前端)3.1UI设计---3.2前端设计
        #
        # 4 代码整合
        #
        # 5 集成测试
        #
        # 6 网站发布


    # 3 数据库设计

        # 1 用户模块
        #
        #     用户表
        #         ID
        #         用户名
        #         密码
        #         邮箱
        #         收件人
        #         地址
        #         邮编
        #         联系方式
        #
        #     一个用户添加多个收货地址
        #         用户表
        #             ID
        #             用户名
        #             密码
        #             邮箱
        #             激活
        #             权限标识
        #         地址表
        #             ID
        #             收件人
        #             地址
        #             邮编
        #             联系方式
        #             是否默认
        #             用户ID
        # 2 商品相关模块
        #
        #     SKU与SPU概念
        #
        #         SPU 标准产品单位
        #         SKU 细分单位
        #
        #     商品SKU表
        #         ID
        #         名称
        #         价格
        #         描述
        #         库存
        #         详情
        #         图片 为了减少跨表 保留图片字段
        #         状态标记
        #         种类ID
        #         SPU ID
        #
        #     商品SPU表
        #         ID
        #         名称
        #         详情
        #
        #     种类表
        #         ID
        #         种类名称
        #         logo
        #         图片
        #
        #     商品图片表
        #         ID
        #         图片
        #         SKU id
        #
        #     首页轮播商品表
        #         ID
        #         SKU ID
        #         图片
        #         index  轮播循序
        #
        #     首页促销活动表
        #
        #         ID
        #         图片
        #         活动url
        #
        #     首页分类商品展示表
        #
        #         ID
        #         SKU ID
        #         种类ID
        #         index
        #         展示标识
        #
        # 3 redis实现购物车功能
        #     保存用户历史浏览记录
        # 4 订单模块
        #
        #     订单信息表
        #         订单ID
        #         地址ID
        #         用户ID
        #         支付方式
        #         总数目
        #         总金额
        #         运费
        #         支付状态
        #         创建时间
        #
        #     订单商品表
        #         ID
        #         SKU ID
        #         商品数量
        #         商品价格
        #         订单ID
        #         评论


    # 4 模型类设计

        # 0 定义抽象模型类
            # class BaseModel(models.Model):
            #     create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
            #     update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
            #     is_delete = models.BooleanField(default=False, verbose_name="删除时间")
            #
            #     class Meta:
            #         abstract = True  # 抽象基类必加


        # 1 用户模型表
            # class User(Abstractuser, BaseModel):
            #   """用户模型类"""
            #     def generate_active_token(self):
            #         serializer = Serializer(settings.SECRET_KEY, 3600)
            #         info = {"confim": self.id}
            #         token = serializer.dumps(info)
            #         return token.decode()
            #
            #     class Meta:
            #         db_table = "df_user"
            #         verbose_name = '用户'
            #         verbose_name_plural = verbose_name
            #

        # 2 地址模型表
            # class Address(BaseModel):
            #     user = models.ForeignKey("User", verbose_name='???????§')
            #     receiver = models.CharField(max_length, verbose_name='??????')
            #     addr = models.CharField(max_length=256, verbose_name='???????·')
            #     zip_code = models.CharField(max_length=6, null=True, verbose_name="????±???")
            #     phone = models.CharField(max_length=11, verbose_name="???????°")
            #     id_default = models.BooleanField(default=False, verbose_name="??·?????")
            #
            #     class Meta:
            #         db_table = "df_address"
            #         verbose_name = '用户收货地址'
            #         verbose_name_plural = verbose_name
            #

        # 3商品类型模型类
            # class GoodType(BaseModel):
            #     name = models.CharField(max_length=20, verbose_name="????????")
            #     logo = models.CharField(max_length=20￡? vernpse_name = "±???")  # ??±???
            #     image = models.ImageField(upload_to='type', verbose_name="???·????????")
            #
            #     class Meta:
            #         db_table = "df_goods_type"
            #         verbose_name = '商品种类'
            #         verbose_name_plural = verbose_name
            #
            #     def __str__(self):
            #         reutrn
            #         self.name

        # 4 商品SPU类
            # class Goods(BaseModel):
            #     name = models.CharField(max_length=20, verbose_name="???·SPU????")
            #     detail = HTMLField(blank=True, verbose_name="???·????")  富文本
            #
            #     class Meta:
            #         db_table = "df_goods"
            #         verbose_name = "商品SPU"
            #         verbose_name_plural = verbose_name

        # 5 商品SKU类

            # class GoodsSKU(BaseModel):
                # status_choices = (
                #     (0, "上线"),
                #     (1, "下线"),
                # )
                # type = models.ForeignKey("GoodsType", verbose_name="???·????")
                # goods = models.ForeignKey("Goods", verbose_name="???·SPU")
                # name = models.CharField(max_length=20, verbose_name="???·????")
                # desc = models.CharField(max_length=256, verbose_name="???·????")
                # price = models.Decimalfield(max_digits=10, decimal_places=2, verbose_name="???·????")
                # unite = models.CharField(max_length=20, verbose_name="???·?￥??")
                # image = models.IntegerField(upload_to="goods", verbose_name="???·????")
                # stock = models.IntegerField(default=1, verbose_name="???·????")
                # sales = models.IntegerField(default=0, verbose_name="???·????")
                # status = models.SmallIntegerField(default=1, choices=status_chices,
                #                                   verbose_name="???·×???")  # ??????????￡?choice????????·??§
                #
                #
                # class Meta:
                #     db_table = "df_goods_sku"
                #     verbose_name = "???·"
                #     verbose_name_plural = verbose_name

        # 6 商品图片模型类
            # class GoodsImage(BaseModel):
            #     sku = models.ForeignKey("GoodsSKU", verbose_name="???·")
            #     image = models.ImageField(upload_to="goods", verbose_name="?????·??")
            #
            #     class Meta:
            #         db_table = "df_goods_image"
            #         verbose_name = "???·????"
            #         verbose_name_plural = verbose_name
            #

        # 7 首页轮播商品表
            # class IndexGoodsBanner(BaseModel):
            #     sku = model.ForeignKey("GoodSKU", verbose_name="???·")
            #     image = models.ImageField(upload_to="banner", verbose_name="????")
            #     index = models.SmallIntegerField(default=0, verbose_name='????????')
            #
            #     class Meta:
            #         db_table = "df_index_banner"
            #         verbose_name = "???￥???·????"
            #         verbose_name_plural = verbose_name
        # 8 首页促销活动表

            # class IndexPromotionBanner(BaseModel):
            # name = models.CharField(max_length=20, verbose_name="活动名称")
            # url = models.URLField(verbose_name="????????")
            # image = model.ImageField(upload_to="banner", verbose_name="????????")
            # index = models.SmallIntegerField(default=0, verbose_name="????????")
            #
            #
            # class Meta:
            #     db_table = "df_index_promotion"
            #     verbose_name = "????????"
            #     verbose_name_plural = verbose_name
            #

        # 9 首页分类商品展示表

            # class IndexTypeGoodsBanner(BaseModel):
            #     DISPLAY_TYPE_CHOICES = (
            #         (0, "标题"),
            #         (1, "图片")
            #     )
            #     type = models.ForeignKey('GoodsType', verbose_name="????????")
            #     sku = models.ForeignKey('GoodsSKU', verbose_name="???·SKU")
            #     display_type = models.SmallIntegerField(default=1
            #     n
            #     choices = DISPLAY_TYPE_CHOICES, verbose_name = "????????")
            #     index = models.SmallIntegerField(default=0, verbose_name="????????"
            #
            #     class Meta:
            #         db_table = "df_index_type_goods"
            #         verbose_name = "·??????????·"
            #         verbose_name_plural = verbose_name
            #
        # 10 订单信息表
            # class OrderInfo(BaseModel):
            #     PAY_METHOD_CHOICES = (
            #         (1, "货到付款"),
            #         (2, "微信支付"),
            #         (3, "支付宝"),
            #         (4, "银联支付"),
            #     )
            #
            #     ORDER_STATUS_CHOICES = (
            #
            #         (1, "待支付"),
            #         (2, "待发货"),
            #         (3, "待收货"),
            #         (4, "待评价"),
            #         (5, "已完成"),
            #     )
            #
            #     order_id = models.CharField(max_length=128, primary_key=True, verbose_name="???￥±???")
            #     user = models.ForeignKey("user.User", verbose_name="???§")  # user.User 如果关联的类不在同一个app应用中 导入方式变为 app名.类名
            #     addr = models.ForeignKey("user.Address", verbose_name="???·")
            #     pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES, default=3, verbose_name="?§??·???")
            #     total_count = models.IntegerField(default=1, verbose_name="???·????")
            #     total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="×???")
            #     transit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="??·?")
            #     order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, varbose_name="?§??×???")
            #     trade_no = models.CharField(max_length=128, verbose_name="?§??±???")
            #
            #     class Meta:
            #         db_table = "df_order_info"
            #

        # 11 订单商品表
            # class OrderGoods(BaseModel):
                # order = models.ForeignKey("OrderInfo", verbose_name="???￥")
                # sku = models.ForeignKey("goods.goodsSKU", verbose_name="???·????SKU")
                # count = models.IntegerField(default=1, verbose_name="???·????")
                # price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="???·????")
                # comment = models.CharField(max_length=256, verbose_name="????")
                #
                #
                # class Meta:
                #     db_table = "df_order_goods"

        # 999 其他

            # choice字段代表限定取值范围
            #





# django choice字段的使用

#
#     限定选择范围,在页面中是选择标签
#
#     class A(models.Model):
#         a = (
#             (0,"a"),
#             (1, "b")
#         )
#
#     b = models.SmallIntegerField(choice=a)
#
#

# django 富文本编辑器

#     能够像office一样编写出漂亮的文字页面
#
#     1 安装
#         pip3 install django-tinymce
#
#     2 注册
#         应用注册
#             "tinymce"
#
#     3 配置富文编辑器
#         1 settings中
#             TINYMCE_DEFAULT_CONFIG = {
#                 'theme': 'advanced',  # 高级主题功能多
#                 'width': 600,
#                 'height': 400,
#             }
#
#         2 url.py中
#
#             url(r'tinymce/', include('tinymce.urls')),
#
#     4 使用
#         模型类中
#             from tinymce.models import HTMLField
#             class A(models.Model):
#                 s = HTMLField()
#
# django类型中verbose_name和verbose_name_plural
#
#     成套使用 admin后台管理系统中模型类会显示指定的中文
#     verbose_name = "商品"
#     verbose_name_plural = verbose_name


# 4 项目框架的搭建

#
#     1 应用配置
#
#         所有应用发到1个apps目录中
#
#             选择1
#
#                 1 注册应用
#                         'apps.应用名'
#                 2 配置路由
#                         模块url放前面，主页url方在最后
#                         url(r'^user/', include('apps.user.urls'))
#
#             选择2
#
#                 settings中添加(即添加了django的搜索路径)
#                     sys.path.insert(0, os.path.join(BASE_DIR, 'app'))
#                 照常--
#                 1 注册应用
#                     '应用名'
#                 2 配置路由
#                     模块url放前面，主页url方在最后
#                     url(r'^user/', include('user.urls'))
#
#     2 定义模型抽象基类
#
#         1 创建目录db
#         2 db中创建base_model.py文件
#             class BaseModel(models.Model):
#                 """模型抽象基类"""
#                 create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
#                 update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
#                 is_delete = models.BooleanField(default=False, verbose_name="删除标记")
#
#                 class Meta:
#                     abstract = True  # 指定说明是一个抽象说明类
#
#     3 把写好的模型类添加到各自类中
#
#     4 指定django认证系统使用的模型类
#         指定之后就不会生产原来的默认表auth_user等
#
#         settings中
#
#             AUTH_USER_MODEL = 'user.User'
#
#



# 1 注册逻辑

#     1 写视图函数 返回对应 html
#         配置 html 文件引入
#         配置 表单action
#
#         处理函数的一般步骤
#             1 接收数据
#                 username = request.POST.get("username")
#                 password = request.POST.get("pwd")
#                 email = request.POST.get("email")
#                 alloww = request.POST.get("allow")
#
#             2 对数据进行校验
#
#                 校验数据是否含有空
#                 if not all([username, password,email]):
#                     return render(xx)
#
#                 校验邮箱
#                 if not re.match(xx, email)
#                     return render(xx)
#
#                 检验是否同意
#                 if allow != 'on':
#                     return render(xx)
#
#                 校验用户名是否重复
#                 try:
#                     User.objects.get(username=username)
#                 except User.DoesNotExist:
#                     user = None
#                 if user:
#                     return render(xx, {"errmsg":"用户名已存在"})
#
#             3 进行业务处理
#
#                 User.objects.create_user(username, email, password)_
#
#
#             4 发送激活邮件，包含激活链接
#
#                 激活链接中需要包含用户的身份信息，并且把身份信息进行加密
#                 使用itsdangerous
#
#                 加密用户什么信息
#                     serializer = TimewebJson...(settings.SECRET_KEY, 3600)
#                     info = {'confirm':user.id}
#                     token = serializer.dumps{info}.decode("utf8") #
#
#                 发送邮件
#                     发送邮件流程
#                         网站发送邮件-->smtp服务器-->目的邮箱
#                     配置发送邮件(163服务地址)
#                         EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
#                         EMAIL_HOST = 'smtp.163.com'
#                         EMAIL_PORT = 25
#                         EMAIL_HOST_USER = '发送邮件的邮箱'
#                         EMAIL_HOST_PASSWORD = '授权码'
#                         EMAIL_FROM = '收件人看到的发件人同EMAIL_HOST_USERS值相同' # 可写成xx<xx@163.com>
#
#                     发邮件（别忘了异步发送邮箱工具celery）
#                         subject = '主题'
#                         message =''
#                         sender = settings.EMAIL_FROM
#                         receiver = ["接收人的邮箱"]
#                         # 如果发送的信息中含有html标签
#                         html_message = '<h1>%s,欢迎</h1>请点击链接激活账户<br><a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>'%(username, token, token)
#                         send_mail(subject, message, sender, receiver, html_message=html_message)
#
#             5 返回应答, 跳转首页
#
#                 return redirect(reverse('good:index'))
#
#
#     2 使用类视图
#         类视图的原理
#             用dispatch方法分发调用 类中的对应的get，post或其他方法
#
#     3 激活视图
#         class Active(View):
#             def get(self, request, token):
#
#                 serializer = TimewebJson...(settings.SECRET_KEY, 3600)
#                 try:
#                     info = serializer.loads(token)
#                     user_id = info['confirm']
#
#                     user = User.objects.get(id=user_id)
#                     user.is_active = 1
#                     user.save()
#
#                     return 返回登录页面
#
#                 except SignatureExpired:
#                     # 激活链接过期，实际提示又发送了一个激活邮件请点击
#                     return HttpResponse('xxx')



# 2 登录逻辑

    # 1 登录校验流程

        # from django.contrib.auth import authenticate, login
        # class LoginView(View):
        #
        #     def get(self, request):
        #         判断是否记住了用户名
        #         if 'username' in request.COOKIES:
        #             username = request.COOKIES.get('username')
        #             checked = 'checked'
        #         else:
        #             username = ''
        #             checked = ''
        #         return render(request, 'xx.html', {"username":username, 'check':checked})

        #
        #     def post(self, request):
        #         """登录校验"""

        #
        #         接收数据
        #         username = request.POST.get("username")
        #         password = request.POST.get("pwd")
        #
        #         校验数据
        #         if not all([username, password]):
        #             return render(xxxx)
        #
        #         业务处理:登录校验
        #
        #         user = authenticate(username=username, password=password)
        #         if user is not None:
        #             if user.is_active:
        #                 print("用户已经激活")
        #
        #                 记录登录状态
        #                 login(request, user)
        #                 return redirect(xx)
        #                 获取登录后所要跳转的地址
        #                 next_url = request.GET.get('next', reverse(xx)) # 如果获取不到 设置默认值
        #                 response = redirect(next_url)
        #                 判断是否需要记住用户名
        #                 remember = request.POST.get('remember')
        #                 if remember == 'on':
        #                     response.set_cookie('username', username, max_age=7*24*3600)
        #                 else:
        #                     response.delete_cookie('username')
        #                 return response
        #
        #             else:
        #                 # 用户名密码错误
        #                 return '用户未激活'
        #         else:
        #             return '用户名或密码错误'

    # 2 使用redis存储session信息

        # 方式1
        #     1 安装
        #         pip3 install django-redis-session
        #
        #     2 配置
        #
        #         SESSION_ENGINE = "redis_sessions.session"
        #         SESSION_REDIS_HOST = "localhost"
        #         SESSION_REDIS_PORT = 6379
        #         SESSION_REDIS_DB = 2
        #         SESSION_REDIS_PASSWORD = ''
        #         SESSION_REDIS_PREFIX = 'session'
        #
        #     3 使用
        #         def test(request):
        #             request.session['h1'] = 'hello'
        #             a = reuquest.session.get('h1')
        #             del request.session['h1']
        #             request.session.flush()
        # 方式2
        #
        #     django-redis 使django支持Redis cache/session后端的全功能支持
        #
        #     1 安装
        #         pip3 install django-redis
        #
        #     2 配置
        #
        #
        #             django的配置缓存
        #
        #                 CACHES = {
        #                     "default":{
        #                         "BACKEND":'django_redis.cache.RedisCache',
        #                         "LOCATION": 'redis://127.0.0.1:6379/1',
        #                         "OPTIONS": {
        #                                 "CLIENT_CLASS":"django_redis".clent.DefaultClient,
        #                             }
        #                         }
        #                     }
        #
        #             配置为sesshon存储
        #
        #                 SESSION_ENGINE = "django.contrib.sessions.backends.cache"
        #                 SESSION_CACHE_ALIAS = "default"
        #


# 3 抽离父模板

# 4 登录装饰器和登录后页面跳转

    # 1 配置未登录后的的自动跳转地址
    #
    #     LOGIN_URL = '/XX/XXXX'
    #     注意
    #         前段表单不要设置action属性
    #         因为默认提交地址就是当前页地址
    #         如果设置了action, 获取next参数的时候会出现问题
    # 2 判断用户是否登录
    #
    #     创建类重写as_view方法类判断用户是否登录
    #         from django.contrib.auth.decorators import login_required
    #
    #         class A:
    #             @classmethod
    #             def as_view(cls, **initkwargs):
    #                 view = super(A, cls).as_view(**initkwargs)
    #                 return login_required(view)
    #
    #
    #         视图的使用
    #
    #             class B(A, view):
    #                 .....

# 5 登录后欢迎信息

    # is_authenticated() # 除了给模板文件传递的模板变量之外，django框架会吧request.user也传递给模板文件
    # 后端中判断
    # def get(self, request):
    #     # 如果登录a为True(request.user为User类一个实例) 否则False（request.user为AnonymousUser一个实例）
    #     a = request.user.is_authenticated()
    # 前段中判断
    #     {% if user.is_authenticated %}
    #         xxx
    #     {% else %}
    #         yyy
    #     {% end %}

# 6 退出登录

#     from django.contrib.auth.decorators import login_out
#     class LogutView(View):
#
#         def get(self, request):
#
#             清除session信息
#             logout(request)
#
#             跳转到首页
#             return redirect(xxx)
#

# 7 用户中心信息页

    # class UserInfo(xx):
    #     def get(self, request):
    #
    #     获取用户的个人信息
    #     user = request.user
    #     address = Address.objects.get_default_address(user) # 模型类管理器
    #
    #     获取用户历史浏览记录
    #     创建redis操作对象的方式二
    #     from django_redis import get_redis_connection
    #     con = get_redis_connection('default')
    #     history_key = 'history_%d'%user.id
    #
    #
    #     获取用户最新浏览的5个商品id
    #     sku_ids = con.lrage(history_key, 0 ,4)
    #
    #     从数据空中查询用户浏览的商品的具体信息(通过redis获取到浏览商品的列表商品id的顺序,
    #                         去数据库中获取商品返回的顺序不一样)
    #     goods_li = []
    #     for id in sku_ids:
    #         goods = GoodsSKU.object.get(id=id)
    #         goods_li.append(goods)
    #
    #     return rendr(xxxxx)


# 8 用户中心订单页

    # 获取用户订单信息
    #

# 9 用户中心地址页

#     class AddressView(View):
#
#         def get(self,request):
#
#             获取用户默认收货地址
#             user = request.user
#
#             try:
#                 address = Address.objects.get(user=user, is_default=True)
#
#             except Address.DoesNotExist:
#                 不存在默认收货地址
#                 address = None
#
#             return render(xxx,{"default_addr":address})
#
#         def post(self,request):
#             接收数据
#             receiver = request.POST.get('receiver')
#             addr = request.POST.get('addr')
#             zip_code = request.POST.get('zip_code')
#             phone = request.POST.get('phone')
#             校验数据
#             if not all([receiver, addr, phone]):
#                 return render '数据不完整'
#
#             校验手机号
#             re.match(r'xxxx', phone)
#                 return render '手机格式不正确'
#             业务处理: 地址添加
#             如果用户已存在默认收货地址, 添加的地址不作为默认收货地址，否则默认收货地址
#
#             user = request.user
#
#             address = Address.objects.get_default_address(user) # 使用了模型管理器类
#             if address:
#                 is_default = False
#             else:
#                 is_default = True
#
#             Address.objects.create(user=user, receiver=receiver,
#                                    addr=address,zip_code=zip_code,
#                                    phone=phone,
#                                    is_default=is_default)
#
#
#             返回应答 刷新地址页面
#             return redirect(reverse('user:address'))
#

# 10 模型类管理器类

#     自定义管理器
#     models文件中（视图函数中存在了相同的查询方法，使用模型管理器类，进行封装）
#
#         class xxManager(model.Manager):
#
#             作用
#                 1 改变原有查询的结果集all()
#                 2 封装方法 用户操作模型类对应的数据表(增删改查)
#
#             获取用户默认地址
#             def get_defautl_address(self, user):
#                 # self.model 获取self对象所在的模型类
#                 try:
#                     address = self.get(user=user, is_default=True)
#
#                 except self.model.DoesNotExist:
#                     不存在默认收货地址
#                     address = None
#
#                 return address


# 11 获取用户的历史浏览记录

#     1 访问商品详情页面的时候添加浏览记录,在商品详情对应的视图中
#     2 访问用户中心个人信息的时候获取历史浏览记录
#     3 历史浏览记录存储在redis数据库
#     4 redis中粗出历史浏览记录的格式
#         每个用户的历史浏览记录用一条数据保存
#         list:
#             history_用户id:[2,3,1]
#         添加历史浏览记录时, 用户最新浏览的商品的id从列表左侧插入,如果列表
#         中存在此商品,则先删除，在从左面插入
#         conn = get_redis_connection('default')
#
#         history_key = 'history_%d'%user.id

#         移除列表中goods_id
#         conn.lrem(history_key, 0, goods_id)

#         把goods_id插入到列表左侧
#         conn.lpush(history_key, goods_id)

#         只保存用户最新浏览的5条信息
#         conn.ltrim(history_key, 0, 4)



# 12 分布式图片服务器FastDFS

    # 1 介绍

    #
    #     用c语言编写的一款开源的分布式文件系统
    #     提供文件上传和下载的服务
    #     架构包括 Tracker server 和Strorage server
    #         Tracker server进行文件上传, 下载 调度作用
    #         Tracker server 通过调度最终由Strorage server
    #         完成文件上传和下载, 文件存储作用
    #
    #     优点
    #         海量存储, 存储容量扩展方便
    #         文件内容重复, 只保存一份
    #         结合nginx提高网站提供图片的效率

    # 1.1 流程

    #     通过admin页面上传图片-->django服务器-->把文件上传到fast dfs文件存储服务器
    #
    #                         保存在django对应表中<--返回文件id<--
    #     用户请求图片 -->django服务器渲染页面<img src="http:xx.xx.xxx.xx/文件id">
    #             返回给浏览器<--nginx去FDFS文件存储服务器中获取文件--浏览器根据地址请求nginx<--返回给浏览器<--

    # 2 安装和配置

    #
    #     linux安装
    #
    #         1 安装fastdfs依赖包
    #             1解压缩libfastcommon-master.zip
    #             2进入libfastcommon-master目录
    #             3执行 ./make.sh
    #             4执行sudo ./make.sh install
    #
    #         2 安装fastdjs
    #             1 接压缩fastdfs-master.zip
    #             2 进入到 fastdfs-master 目录中
    #             3 执行./make.sh
    #             4 执行sudo ./make.sh install
    #
    #         3 配置跟踪服务器tracker
    #             1 sudo cp /ect/fdfs/tracker.conf.sample /ect/fdfs/tracker.conf
    #             2 在/home/python/目录中创建目录 fastdfs/tracker
    #
    #                 mkdir -p /home/python/fastdfs/tracker
    #             3 编辑/ect/fdfs/tracker.conf配置文件
    #                 sudo vim /etc/fdfs/tracker.conf
    #                 修改 base_path=/home/python/fastdfs/tracker
    #
    #         4 配置存储服务器storage
    #
    #             1 sudo cp /ect/fdfs/storage.conf.sample /ect/fdfs/storage.conf
    #             2 在/home/python/fastdfs/ 目录中创建目录 storage
    #                 mkdir -p /home/python/fastdfs/storage
    #             3 编辑/etc/fdfs/storage.conf配置文件
    #                 sudo vim /ect/fdfs/storage.conf
    #                 修改内容 base_path=/home/python/fastdfs/storage
    #                         store_path0=/home/python/fastdfs/storage
    #                         tracker_server = 自娱Ubuntu虚拟机的ip地址:22122
    #         5 启动tracker和storage
    #             sudo service fdfs_trackerd start
    #             sudo service fdfs_storaged start
    #
    #         6 测试
    #             1 sudo cp/etc/fdfs/client.conf.sample /etc/fdfs/client.conf
    #             2 编辑/ect/fdfs/client.conf配置文件
    #                 sudo vim /etc/fdfs/client.conf
    #
    #                 修改
    #                     base_path=/home/python/fastdfs/tracker
    #                     tracker_server=自己ubuntu虚拟机的ip地址22122
    #             3 上传文件测试
    #                 fdfs_upload_file /etc/fdfs/client.conf 要上传的图片文件
    #                 如果返回类似 group1/Mod/00/00/fsdgfddhshsdhsdhssd.jpg 说明成功

    # 3 Nginx配合FastDFS使用安装和配置

    #     解决FastDFS用户量比较大的问题借助Nginx
    #
    #     1 安装nginx和fastdfs-nginx-module
    #
    #         1 解压缩 nginx-1.8.1   # web 服务器 epoll
    #         2 解压缩 fastdfs-nginx-module-master.zip
    #         3 进入nginx-1.8.1目录中
    #         4 执行
    #             sudo ./configure --prefix=/usr/local/nginx/ --add-module-fastdfs-nginx-module-master解压
    #                 后的目录的绝对路径/src
    #
    #             sudo ./make
    #             sudo ./make install
    #
    #             sudo cp fastdfs-nginx-module-master 解压后的目录中src下的
    #                 mod_fastdfs.conf /etc/fdfs/mod_fastdfs.conf
    #
    #             sudo vim /etc/fdfs/mod_fastdfs.conf
    #                 修改内容
    #                     connect_timeout=10
    #                     tracker_server=自己ubuntu虚拟机ip地址:22122
    #                     url_have_group_name=true
    #                     store_path0=/home/python/fastdfs/storage
    #
    #             sudo cp 解压缩的fastdfs-master目录conf目录中的http.conf /etc/fdfs/http.conf
    #
    #             sudo cp 解压缩的fastdfs-master目录conf目录中的mine.types /etc/fdfs/mime.types
    #
    #             sudo vim /user/local/nginx/conf/nginx.conf
    #                 在http部分中添加配置信息:
    #                     server{
    #                         listen  8888;
    #                         server_name  localhost;
    #                         location ~/group[0-9]/{
    #                             ngx_fastdfs_module;
    #                         }
    #                         error_page 500 502 503 504 /50x.html;
    #                         location = /50x.html{
    #                             root html;
    #                         }
    #                     }
    #         5 启动nginx
    #             sudo /usr/local/nginx/sbin/nginx
    #

    # 4 使用python客户端上传测试

    #     1 安装依赖包
    #         先下载源码包fdfs_client-py-master.zip
    #         进入包所在目录 pip install fdfs_client-py-master.zip
    #
    #     2 上传文件
    #         from fdfs_client.client import Fdfs_client
    #         client = Fdfs_client("/ect/fdfs/client.conf") # 参数为client.conf文件所在路径
    #         ret = client.upload_by_filename('test')
    #         ret返回值 会返回来
    #                 {
    #                   'Group name':'xx', 'Status':'Upload successed', 'Remote file_id':'xxx',
    #                   ........
    #                 }
    #

    # 5 修改django的上传行为(即将原本文件存储路径存到FastDFS中)

        # 1 自定义文件存储类
        # from django.core.files.storage import Storage
        # from fdfs_client.client import Fdfs_client
        #
        # class A(Storage):
        #
        #     def __init__(self, client_conf=None, base_url=None):
        #         """为了动态配置文件路径，
        #             和返回的文件路径
        #
        #         """
        #         if client_conf is None:
        #             client_conf = 'client.conf的相对项目路径'
        #         self.client_conf = client_conf
        #
        #         if base_url is None :
        #             base_url = 'http://127.0.0.1:80000'
        #         self.base_url = base_url
        #
        #
        #
        #     def _open(self, name, mode='rb'):
        #         """打开文件时使用"""
        #         pass
        #
        #     def _save(self, name, content):
        #         """
        #         保存文件时使用
        #         参数：
        #             name 上传文件的名字
        #             content 包含上传文件内容file类的对象
        #         """
        #
        #         # 创建一个Fdfs_client对象
        #         # 参数需要指定配置文件
        #             # 需要client.conf配置文件放在此类文件的同目录下
        #             #     修改 base_path = /xx/  记录日志路径
        #             #         tacker_server=xxxx
        #         client = Fdfs_client(self.client_conf)
        #
        #         # 上传文件到fast dfs系统中, 根据文件内容上传文件
        #         res = client.upload_by_buffer(content.read())
        #
        #         if res.get('Status') != 'Upload successed':
        #             # 上传失败
        #             raise  Exception('删除文件fast dfs失败')
        #         # 获取返回的文件id
        #         filename = res.get('Remote file_id')
        #
        #         return filename
        #
        #     def exists(self, name):
        #         """django判断文件名是否可用
        #             因为上传的是fastdfs,不存在文件名不可用
        #         """
        #         return False
        #
        #     def url(self, name):
        #         """返回范根文件的url路径"""
        #         return self.base_url+name
        #
        #
        # 2 让django使用自定义的存储类
        #
        #     settings中
        #         DEFAULT_FILE_STORAGE='自定义类的路径'

# 13 网站首页生成静态页面

    # 1作用
    #     对于不经常改变的网页而言,减轻服务器查询数据库压力
    #
    # 2使用工具和考虑条件
    #     首页页面的静态化
    #         使用工具
    #             celery
    #         重新生成条件
    #             当管理员后台修改首页数据的时候, 需要重新生成首页静态页面
    #
    # 3定义任务函数
    #     from django.template import loader, RequestContext
    #
    #     @app.task
    #     def a():
    #         # 查询首页需要的数据
    #
    #         context = {xx:xxx}
    #         1 加载模板文件, 返回模板对象
    #             temp = loader.get_template('xx.html')
    #
    #         2 渲染模板
    #             static_index_html = temp.render(context)
    #
    #         3 生成首页对应的静态文件
    #             save_path = os.path.join(settings.BASE_DIR, 'static/index.html')
    #             with open(save_path, 'w') as f:
    #                 f.write(static_index_html)
    #
    # 4配置nginx提交静态页面
    #
    #     server{
    #         listen  80;
    #         server_name  localhost;
    #         location /static {
    #             xxxx
    #         }
    #         location / {
    #             root 路径
    #             index index.html index.htm
    #         }
    #     }
    #
    # 5 后台管理员更新首页数据时重新生产静态页面
    #
    #     class A(admin.ModelAdmin):
    #         def save_model(self, request, obj, form, change):
    #             """新增或更新表中的数据时调用"""
    #             super().save_model(request, obj, form, change)
    #
    #             # 发出任务, 让celery 重新生产首页静态页面
    #             xx.delay()
    #
    #         def delete_model(self, request, obj):
    #             super().delete_model(request, obj)
    #
    #             # 发出任务, 让celery 重新生产首页静态页面
    #             xx.delay()
    #
    #     admin.site.register(xx, A)
    #
    # 6 由于有多个类所以抽象基类
    #
    #
    #     class Base_A(admin.ModelAdmin):
    #         def save_model(self, request, obj, form, change):
    #             """新增或更新表中的数据时调用"""
    #             super().save_model(request, obj, form, change)
    #
    #             # 发出任务, 让celery 重新生产首页静态页面
    #             xx.delay()
    #
    #         def delete_model(self, request, obj):
    #             super().delete_model(request, obj)
    #
    #             # 发出任务, 让celery 重新生产首页静态页面
    #             xx.delay()
    #
    #     class A(Base_A):
    #         pass
    #
    #     class B(Base_A):
    #         pass
    #     ...
    #
    #     admin.site.register(xx, A)
    #     admin.site.register(xxx, B)
    #
    # 7 通过nginx调度放分django网站返回index.html或
    #     访问celery服务器返回index.html
    #
    #     设置
    #         网址 ---> django网站
    #         网址/index --> celery服务器
    #
    #     1 更改django index路由匹配
    #         url(r'^/index$')
    #
    #     2 部署 未完。。。。


# 14 页面数据缓存

    # 把页面使用的数据存放在缓存中, 当再次使用这些数据时,
    #     先从缓存中获取,如果获取不到,再去查询数据库, 减少数据库查询的次数
    #
    #
    # 1 设置缓存
    #     from django.core.cache import cache
    #
    #     class A(View):
    #
    #         def get(self,request):
    #
    #             尝试从缓存中获取数据
    #             context = cache.get('xxx')
    #             if context is None:
    #
    #
    #                 获取数据
    #                     ...
    #                 设置缓存
    #                 context = {"a":1, "b":2}
    #                 cache.set("aaaa", context, 3600) # 名称 缓存内容 过期时间
    #
    #             return render(xxxx)
    #
    # 2 缓存的数据更新
    #     当管理员后台修改首页信息对应的表格中的数据时候,需要缓存更新
    #     class Base_A(admin.ModelAdmin):
    #         def save_model(self, request, obj, form, change):
    #             """新增或更新表中的数据时调用"""
    #             super().save_model(request, obj, form, change)
    #
    #             # 发出任务, 让celery 重新生产首页静态页面
    #             xx.delay()
    #
    #             # 清除首页缓存数据(当首页数据进行跟新的时候, 清除
    #             #               了缓存,视图就会重新创建缓存)
    #             cache.delete("xxxx")
    #
    #         def delete_model(self, request, obj):
    #             super().delete_model(request, obj)
    #
    #             # 发出任务, 让celery 重新生产首页静态页面
    #             xx.delay()
    #
    #             # 清除首页缓存数据
    #             cache.delete("xxxx")
    #
    #     class A(Base_A):
    #         pass
    #
    #     class B(Base_A):
    #         pass
    #     ...
    #
    #     admin.site.register(xx, A)
    #     admin.site.register(xxx, B)


# 15 首页内容获取和展示

        # class Index(View):
        #     def get(self, request):
        #
        #         # 获取商品的种类信息
        #
        #         # 获取首页轮播商品信息
        #
        #         # 获取首页促销活动信息
        #
        #         # 获取首页分类商品展示信息
        #
        #         # 获取用户购物车中商品的的数目
        #
        #         # 组织模板上下文
        #
        #         context = {xxx}
        #         return render(xxx)

# 16 redis存储购物车记录分析

    # 1 分析
        # 更新购物车记录
        #
        #     当用户点击加入购物车时需添加购物车记录
        #
        # 获取购物车记录
        #
        #     使用购物车中数据和访问购物车页面的时候需要获取购物车记录
        #
        # 使用redis存储购物车记录
        #     需要记录的数据 商品sku 数量
        #
        #     cat_用户id:{"sku_id1": 商品数目, "sku_id2":商品数目}
        #     获取商品条目数
        #         hlen
    # 2 使用

        # conn = get_redis_connection('default')
        # cart_key = 'xx%d'%user.id
        # cart_count = conn.hlen(cart_key)
        #


# 17 商品详细页信息的获取和显示

    # class Detail(View):
    #     def get(self, request, goods_id):
    #
    #         验证是否有商品信息
    #         try:
    #             sku = xx.Objects.get(id=goods_id)
    #         except xx.DoesNotExist:
    #             ......
    #
    #         获取页面上相关信息去数据库查询
    #
    #         return render(xx)


# 18 商品列表页的内容和显示

    # 按照17

# 19 购物车记录添加到后台

    # 请求方式 采用ajax
        # 请求方式
        #     如果涉及到数据的修改(新增, 更新, 删除),采用post
        #     如果只涉及到数据的获取, 采用get
    # 传递参数 商品id 商品数量

    # class A(View):
    #     def post(self, request):
    #
    #         判断用户是否登录
    #
    #         接收数据
    #         request.POST.get(xxx)
    #         数据校验
    #
    #         if not all([xx,yy]): # 接收数据时候为空
    #             return JsonResponse(xxxx)
    #
    #         try:
    #             a = B.objects.get(id=xxxx) # 校验商品是否存在
    #         except:
    #             return JsonResponse(xxxx)
    #
    #         业务处理:添加购物车记录
    #         先获取值是否有, 如果有进行累加
    #         conn = get_redis_connection('default')
    #         cart_key = 'cart_%d'%user.id
    #         cart_count = conn.hget(cart_key, sku_id)
    #         if cart_count:
    #             累加
    #             count += int(cart_count)
    #
    #         校验商品库存
    #         if count > sku.stock:
    #             return JsonResponse(xxx, '库存不足')
    #
    #         如果没有进行设置
    #
    #         conn.hset(cart_key, sku_id, count)
    #
    #         返回应答
    #         return JsonResponse(xxxx)


# 20 购物车页面显示

    # class A(View):
    #
    #     def get(self, request):
    #
    #         获取登录的用户
    #         user = request.user
    #         获取用户购物车中信息
    #         conn = get_redis_connection(xxx)
    #         cart_key = 'cart_%d'%user.id
    #         cart_dict = conn.hgetall(cart_key)
    #
    #         遍历获取商品信息
    #         return xx

# 21 订单页面的显示

    # class A(View):
    #     获取参数
    #     校验参数
    #     遍历参数获取用户要购买的商品的信息
    #
    #     运费
    #
    #     实付款
    #
    #     获取用户收货地址
    #
    #     上下文

# 22 订单创建

    # 用户每下一个订单, 就要向 订单表中添加一条记录
    # 用户的订单中有几个商品, 就要向订单商品表中加入几条记录

    # 1 视图
    # class A(View):
    #
    #     def post(self,request):
    #
    #         判断用户是否登录
    #
    #         接收参数
    #
    #         校验参数
    #             校验支付方式
    #             校验地址
    #         判断商品库存
    #         创建订单
    #
    #             向订单表中添加记录
    #
    #             订单id
    #             datatime.now().strftime('%Y%m%d%H%M%S')+str(user.id)
    #
    #
    #         更新商品库存和销量
    #
    #         清除用户购物对应的订单信息


    # 2 mysql 事务
    #
    #     一组mysql语句, 要么执行, 要么全不不执行
    #     特点
    #         原子性
    #             一组事务,要么成功, 要么驳回
    #         稳定性
    #             有非法数据,外键约束之类, 事务驳回
    #         隔离性
    #             事务独立运行, 一个事务处理后的结果, 影响了其他事务, 那么其他事务
    #             会驳回, 事务的100%隔离, 需要牺牲速度
    #
    #         可靠性
    #             软, 硬件崩溃或, innoDB数据表驱动会利用日志文件重构修改
    #
    #
    #     事务的控制语句
    #
    #         BEGIN;
    #         ...
    #         COMMIT; # 提交
    #
    #         BEGIN;
    #         ...
    #         ROOBACK; # 回滚
    #
    #
    #         设置部分可回滚(设置事务保存点)
    #
    #             savepoint 名;
    #                 .....
    #             rooback to 名;
    #
    #         删除保存点
    #             release savepoint 名

    # 3 django视图中使用事务
    #
    #     事务全部成功或全部失败
    #         函数中的数据库相关操作就会执行事务(要么都成功要么都撤销)
    #         from django.db import transaction
    #         @transaction.atomic
    #         def a(self, request):
    #
    #
    #     部分事务设置
    #
    #         @transaction.atomic
    #         def a(self, request):
    #
    #             设置保存点
    #             save_id = transaction.savepoint()
    #             ...
    #             回滚保存点
    #             transaction.savepoint_rollback(save_id)
    #
    #             提交事务
    #             transaction.savepoint_commit(save_id)


    # 4 订单并发的控制
    #
    #     1 悲观锁解决
    #
    #         两个用户同意时间操作数据库中一个数据, 得到锁的用户可以对数据进行操作
    #         没得到的等待用户锁的用户用完之后(事务结束之后锁会释放)再那锁进行对数据的操作
    #
    #         mysql中的悲观锁
    #             语句 + for update
    #
    #         django中的悲观锁
    #
    #             A.objects.select_for_update().get(id=xx)
    #
    #     2 乐观锁解决
    #
    #         mysql事务的隔离界别
    #
    #             Read Uncommitted(读取未提交内容)
    #                 事务A和事务B
    #                 不管事务A是否提交, 事务B都能拿到内容
    #
    #             Read Committed(读取提交内容)
    #                 事务A和事务B
    #                     事务A提交之前 事务B拿不到内容
    #
    #             Repeatable Read(可重读 mysql默认的级别)
    #                 事务A和事务B
    #                     及时事务A对内容进行了修改, 事务B还是拿到之前的内容
    #
    #             Serializable(可串行化)
    #
    #                 最高隔离级别, 强制事务排序, 不互相冲突, 但耗时
    #
    #
    #         查询数据的时候不加锁, 在修改时进行判断, 在更新时候的库存
    #         和之前查出的库存是否一样
    #
    #         会有问题: 及时库存够, 库存也有可能和原来的不一样
    #         a为返回受影响行数
    #         a = A.objects.filter(id=xx, stock=xxxx).update(stock=ne_xx, sotck=new_xxxx)
    #
    #         if a == 0:
    #             transaction.savepoint_rollback(save_id)
    #             return ...
    #
    #         为了解决及时库存够,也有可能和原来不一样
    #         应给进行循环 查询 但要有次数限制 for ,
    #         但涉及到事务的隔离级别, 所以还是有问题
    #         将隔离级别设置为 Read Committed(读取提交内容)
    #
    #             sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
    #
    #             skip-external-locking下面添加:
    #                 transaction-isolation = READ-COMMITTED
    #
    #             重启mysql服务
    #
    #                 sudo service mysql restart
    #
    #     3 悲观锁和乐观锁使用建议
    #
    #         1 悲观锁
    #             冲突比较多的时候使用
    #         2 乐观锁
    #             冲突比较少的时候使用


# 23 订单的支付

    # 1 支付宝
    #
    #     支付宝开放平台登录
    #
    #         正常流程
    #             https://open.alipay.com/platform/home.htm
    #
    #             开发者中心-->网页&移动应用
    #
    #             创建应用--支付接入 --->创建--最后得到APPID
    #
    #         测试流程(沙箱--开发模拟环境)
    #
    #             开发者中心-->研发服务
    #
    # 2 电脑网站支付快速接口
    #
    #     1 创建应用
    #
    #     2 配置秘钥
    #                   采用网络请求方式
    #         django网站--------------->支付宝平台
    #
    #         需要用自己的私钥加密 ----> django网站公钥解密
    #
    #         用字符包公钥解密<---------支付宝用自己的私钥加密
    #
    # 3 搭建和配置开发环境
    #
    #     网站如果想让支付宝平台访问,需要有公网的ip
    #     可以访问支付宝网站的接口,返回用户的支付结果
    #
    #
    # 4 网站和支付宝支付接口对接流程
    #
    #     用户访问网站支付接口---->网站调用支付宝接口并传递参数(订单id, 总金额, 订单标题, returl_url, notify_url)--->
    #     支付宝平台返回给网站支付页面--->网站返回给用户支付页面--->用户登录支付宝,确认支付--
    #     --->同步访问网站的return_url传递参数告诉网站用户支付的结果(需要公网ip)
    #     --->异步访问网站的notify_url传递参数告诉网站用户支付的结果(需要公网ip)
    #
    #     如果没有公网ip 用户浏览器访问交易结果,访问支付宝接口 返回用户支付的结果,显示用户支付结果
    #
    # 5 python工具包(支付宝python SDK)
    #
    #     https://github.com/fzlee/alipay/blob/master/README.zh-hans.md
    #
    #     1 安装
    #         pip3 uninstall pycrypto
    #         pip3 install python-alipay-sdk --upgrade
    #         pip3 install openssl
    #
    #     2 生成秘钥文件
    #         终端执行命令
    #
    #             openssl
    #             OpenSSL> genrsa -out app_private_key.pem   2048  # 私钥
    #             OpenSSL> rsa -in app_private_key.pem -pubout -out app_public_key.pem # 导出公钥
    #             OpenSSL> exit
    #
    #
    #         在支付宝上下载的公钥是一个字符串，你需要在文本的首尾添加标记位
    #             (-----BEGIN PUBLIC KEY-----和-----END PUBLIC KEY-----)
    #
    #     3 初始化
    #
    #         alipay = AliPay(
    #             appid="",
    #             app_notify_url=None,  # 默认回调url
    #             app_private_key_string=app_private_key_string, # 私钥路径
    #             # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    #             alipay_public_key_string=alipay_public_key_string, # 公钥路径
    #             sign_type="RSA" # RSA 或者 RSA2
    #             debug=False  # 默认False # 如果是沙箱环境需要改成true
    #         )
    #
    #     4 视图
    #         from alipay import AliPay
    #         class A:
    #
    #             def post(self, request):
    #                 # 用户是否登录
    #
    #                 # 接收参数
    #                 order_id = request.POST.get("order_id")
    #                 # 校验参数
    #                 if not order_id:
    #                     return xxxx
    #
    #                 try:
    #                     order = xx.objects.get(order_id=order_id,
    #                                            user=user,
    #                                            pay_method=3, # 支付宝支付
    #                                            order_status=1,# 未支付状态
    #                                            )
    #                 except xx.DoesNotExist:
    #                     return JsonResponse(xxx)
    #
    #                 # 业务处理:使用python sdk低啊用支付宝的支付接口
    #
    #                 # 初始化
    #                 alipay = AliPay(
    #                     appid="xxxxx",
    #                     app_notify_url=None,  # 默认回调url
    #                     app_private_key_string='',  # 私钥路径 可使用路径拼接
    #                     # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    #                     alipay_public_key_string='',  # 公钥路径
    #                     sign_type="RSA2",  # RSA 或者 RSA2
    #                     debug = True  # 默认False # 如果是沙箱环境需要改成true
    #                 )
    #                 # 调用支付接口
    #
    #                 order_string = alipay.api_alipay_trade_page_pay(
    #                     out_trade_no="20161112",# 订单id
    #                     total_amount=0.01, # 总金额
    #                     subject=subject, # 标题
    #                     return_url=None,
    #                     notify_url=None  # 可选, 不填则使用默认notify url
    #                 )
    #
    #                 pay_url = 沙箱地址
    #
    #                 # 返回应答
    #                 return xxxxx
    #
    #     5 查看订单支付结果
    #
    #         class A:
    #
    #             def post(self, request):
    #                 # 用户是否登录
    #
    #                 # 接收参数
    #                 order_id = request.POST.get("order_id")
    #                 # 校验参数
    #                 if not order_id:
    #                     return xxxx
    #
    #                 try:
    #                     order = xx.objects.get(order_id=order_id,
    #                                            user=user,
    #                                            pay_method=3,  # 支付宝支付
    #                                            order_status=1,  # 未支付状态
    #                                            )
    #                 except xx.DoesNotExist:
    #                     return JsonResponse(xxx)
    #
    #                 # 业务处理:使用python sdk低啊用支付宝的支付接口
    #
    #                 # 初始化
    #                 alipay = AliPay(
    #                     appid="xxxxx",
    #                     app_notify_url=None,  # 默认回调url
    #                     app_private_key_string='',  # 私钥路径 可使用路径拼接
    #                     # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    #                     alipay_public_key_string='',  # 公钥路径
    #                     sign_type="RSA2",  # RSA 或者 RSA2
    #                     debug=True  # 默认False # 如果是沙箱环境需要改成true
    #                 )
    #
    #                 # 调用支付宝查询接口
    #
    #                 while True:
    #                     a = alipay.alipay_trade_query(order_id)
    #
    #                     # a为返回
    #                     #     a = {
    #                     #         "trade_no": '..', # 支付宝交易号
    #                     #         "code":'..' # 接口调用是否成功
    #                     #         "trade_status": "TRADE_SUCCESS" # 支付结果
    #                     #         ...
    #                     #     }
    #                     code = a.get('code')
    #                     if code =='10000' and a.get('trade_status') == 'TRADE_SUCCESS':
    #                         # 支付成功
    #                         # 获取支付宝交易号
    #                         trade_no = a.get('trade_no')
    #                         # 更新订单状态
    #                         order.trade_no = trade_no
    #                         order.order_status = 4 # 待评价
    #                         order.save()
    #                         # 返回结果
    #                         return JsonResponse(xxx)
    #                     elif code=='40004' or (code == '10000' and a.get('trade_status') == 'WAIT_BUYER_PAY'):
    #                         # 等待买家付款
    #                         # 业务处理失败
    #                         import time
    #                         time.sleep(5)
    #                         continue
    #                     else:
    #                         # 支付出错
    #                         return xx


# 24 部署

    # 0 部署的架构解析
    #
    #     1最简单的项目部署(无静态文件)
    #         用户浏览器----uwsgi----django项目
    #
    #         用户向uwsgi发送请求--->uwsgi调用django项目应用--->
    #         django项目应用进行处理返回给uwsgi---->uwsgi将信息返回给用户浏览器
    #
    #     2带有静态文件的项目部署
    #         用户浏览器 ----nginx----uwsgi----django项目
    #
    #         1 动态请求
    #             用户浏览器向nginx发送动态请求--->nginx转交给uwsgi-->uwsgi调用django项目应用-->
    #             django项目应用返回给uwsgi-->uwsgi返回给nginx-->nginx返回给用户
    #
    #         2 静态请求
    #
    #             提前把静态文件放到nginx所在电脑的某个目录中,根据配置nginx就会去目录下方找到静态文件
    #             返回给用户浏览器
    #
    #         动态和静态的请求区分
    #             根据nginx中的 location配置
    #             一般
    #                 location / 动态
    #                 location /static 静态

    # 1 uwsgi服务器
        #     1 介绍
        #         uwsgi作为web服务器(代替python manage.py runserver)
        #     2 安装
        #         pip3 install uwsgi
        #
        #     3 配置
        #         settings.py
        #             DEBUG=False
        #             ALLOWED_HOST=['*']
        #
        #         创建配置文件uwsgi.ini
        #             [uwsgi]
        #             #使用nginx连接时使用
        #             #socket=127.0.0.1:8000
        #             #直接做web服务器使用
        #             http=127.0.0.1:8000
        #             #项目目录
        #             chdir=/////////
        #             #项目中wsgi.py文件的目录,项对于项目目录
        #             wsgi-file=xx
        #             #指定启动的工作进程数
        #             processes=4
        #             #指定工作进程的线程数
        #             threads=2
        #             #在这些进程中有一个主进程
        #             master=True
        #             #保存启动之后主进程的pid
        #             pidfile=uwsgi.pid
        #             #设置uwsgi后台运行不在占用终端,保存日志信息到uwsgi.log
        #             daemonize=uwsgi.log
        #             #设置虚拟环境的路径
        #             virtualent=/////
        #     4 启动和停止
        #
        #         1 启动
        #             uwsgi --ini 配置文件路径
        #             例子
        #                 uwsgi --ini uwsgi.ini
        #         2 停止
        #             uwsgi --stop uwsgi.pid路径
        #             例子
        #                 uwsgi --stop uwsgi.pid

    # 2 nginx和uwsgi对接
    #
    #     1 配置uwsgi.ini文件
    #         [uwsgi]
    #         #使用nginx连接时使用
    #         socket=127.0.0.1:8000   # 和nginx的对接配置！！
    #         #直接做web服务器使用
    #         # http=127.0.0.1:8000 注释掉！！！
    #         #项目目录
    #         chdir=/////////
    #         #项目中wsgi.py文件的目录,项对于项目目录
    #         wsgi-file=xx
    #         #指定启动的工作进程数
    #         processes=4
    #         #指定工作进程的线程数
    #         threads=2
    #         #在这些进程中有一个主进程
    #         master=True
    #         #保存启动之后主进程的pid
    #         pidfile=uwsgi.pid
    #         #设置uwsgi后台运行不在占用终端,保存日志信息到uwsgi.log
    #         daemonize=uwsgi.log
    #         #设置虚拟环境的路径
    #         virtualent=/////
    #
    #
    #     2 配置nginx文件
    #
    #         /user/local/nginx/conf/nginx.conf
    #
    #         修改配置文件
    #
    #             server{
    #
    #                 location / {
    #                     # 包含uwsgi的请求参数
    #                     include uwsgi_parmas;
    #                     # 转交请求给uwsgi
    #                     uwsgi_pass 127.0.0.1:8000 # uwsgi.ini 配置文件中的socket地址
    #                 }
    #
    #             }

    # 3 nginx处理静态文件
    #
    #
    #     1 创建静态文件存储目录
    #
    #         sudo mkdir -p /var/www/项目../static
    #
    #     2 修改用户使用目录权限
    #
    #         sudo chmod 777 /var/www/项目../static/
    #
    #     2 收集所有的静态文件到指定路径
    #
    #         settings.py下
    #
    #             STATIC_ROOT=/var/www/项目../static
    #         执行命令
    #             python manage.py collectstatic
    #
    #     3 修改配置文件
    #
    #
    #         /user/local/nginx/conf/nginx.conf
    #
    #         server{
    #
    #             location / {
    #                 # 包含uwsgi的请求参数
    #                 include uwsgi_parmas;
    #                 # 转交请求给uwsgi
    #                 uwsgi_pass 127.0.0.1:8000 # uwsgi.ini 配置文件中的socket地址
    #             }
    #
    #             location /static {
    #                 # 指定静态文件存放目录
    #                 alias /var/www/项目../static/;
    #             }
    #
    #         }


    # 4 首页静态页面服务器配置
    #
    #     1 流程
    #                     ---- uwsgo+django
    #
    #         用户---nginx
    #
    #                     -----静态页面服务器,nginx
    #
    #
    #         如果访问 /  就访问静态页面服务器
    #
    #         如果访问 其他 就转交给uwsgi
    #
    #
    #     2 配置/user/local/nginx/conf/nginx.conf
    #
    #         server {
    #
    #             location = / {  # 精确匹配只是斜杠
    #                 # 传递请求给静态文件服务器的nginx
    #                 proxy_pass http://ip地址:80;
    #             }
    #         }

    # 5 实现负载均衡

        # 可以启动多个项目(即多个uwsgi+django 业务处理服务器)
        #
        # 配置/user/local/nginx/conf/nginx.conf
        #
        #     upstream xx {
        #
        #         server 127.0.0.1:8000;
        #         server 127.0.0.1:8001;
        #     }
        #     server {
        #
        #         location / {
        #             proxy_pass xx # 就会从上面的服务器中进行转交
        #         }
        #     }


# 25 项目总结

    # 1 生鲜类产品 B2C PC电脑端网页
    #
    # 2 功能模: 用户模块 商品模块(首页, 搜索 , 商品)
    #     购物车模块 订单模块(下单, 支付)
    #
    # 3 用户模块:注册,登录, 激活,退出,个人中心,地址
    #
    # 4 商品模块:首页, 详情, 列表, 搜索(haystack+whoosh)
    #
    # 5 购物车: 增加,删除,修改,查询
    #
    # 6 订单模块: 确认订单页面, 提交订单, 请求支付, 查询支付结果, 评论
    #
    # 7 django默认的认证系统AbstractUser
    #
    # 8 itsdangerous 生成签名的token(序列化工具dumps loads)
    #
    # 9 邮件(django提供邮件支持 配置参数 send_mail)
    #
    # 10 celery(重点, 整体认识, 异步任务)
    #
    # 11 页面静态化(缓解压力 celery nginx)
    #
    # 12 缓存(缓解压力, 保存的位置, 有效期, 与数据库的一致性问题)
    #
    # 13 FastDFS(分布式的图片存储服务, 修改了django的默认文件存储系统)
    #
    # 14 搜索(whoosh 索引 分词)
    #
    # 15 购物车redis 哈希 历史记录 redis list
    #
    # 16 ajax 前段用 ajax请求后端接口
    #
    # 17 事务
    #
    # 18 高并发的库存问题(悲观锁, 乐观锁)
    #
    # 19 支付宝使用流程
    #
    # 20 nginx(负载均衡 提供静态文件)
    #
    #
1
# ======================================================================================