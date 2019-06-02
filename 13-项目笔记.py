#
#
#
# =============================================
# blogblog
#
#     1 说明
#         1 使用django 1.11.3版本开发
#         2 使用的是默认数据库sqlite3
#
#     2 配置
#
#         1 安装django
#         2 创建项目
#         3 创建应用
#         4 注册应用
#         5 设置时区
#         6 创建类模型
#         7 生产迁移数据，生成数据库
#         8 创建超级管理员, 注册类模型（admin.py）
#         9 编辑admin页面显示（admin.py）, 并注册
#         10 创建templates目录,配置模板路径（settings.py）
#         11 创建并编写base.html模板文件
#         12 创建title.html 继承base.html
#         13 配置url(urls.py)
#         14 应用下创建urls.py ，配置
#         15 创建对应url对应的函数(views.py)
#         16 创建对应标题的超链接，点击后显示详细内容
#         17 配置动态路由
#         18 创建并配置详细页面内容content.html
#         19 配置动态路由的视图函数
#         20 设置静态文件位置(settings.py), 根目录下创建static文件夹
#         21 创建新的网页头部header.html基础模板文件
#         22 创建foot.html 基础模板文件
#         23 重写base.html文件
#         24 处理更改配置'APP_DIRS': False后不能加载到模板admin问题
#         25 创建账户(account)应用 ，注册应用，url配置
#         26 创建login的url以及 对应函数
#         27 account下创建forms.py文件使用django表单单类，写表单
#         28 创建login.html创建login登录视图,get请求时候返回登录表单，post请求时候对用户发送的账户和密码进行校验
#             如果是已经注册用户允许登录，如果不是注册过的用户拒绝登录
#         29 将login的超链接加入到头部(header.html)
#         30 使用内置方法实现用户的登录和退出
#         31 登录状态显示用户名 和退出按钮（header.html）
#         32 用户点击退出按钮 退出登录
#         33 用户注册，写表单类
#         34 编写用户注册视图函数
#             1 接受post请求传入表单类创建表单对象
#                 2 如果接受数据验证成功 存储数据构成的用户对象
#                     3 对用户进行密码设置
#                     4 存储用户， 返回成功
#                 5 如果验证不成功 返回错误消息
#             6 如果不是post请求 返回注册表单html
#         35 创建模型类添加数据库User中没有的字段，使用onetoone关联
#         36 完善注册视图和注册html
#         37 修改密码功能（使用内置修改密码函数）
#
#         38 内置忘记密码发送邮箱重置密码
#
#         39 使用第三方密码忘记发送邮箱重置密码
#
#         40 维护个人信息
#
#             1 创建模型类和表单类
#             2 展示个人信息
#             3 编辑个人信息
#                 1 上传和裁剪头像图片
#
#         41 文章管理和显示(文章管理-栏目管理)
#
#             1 访客浏览文档
#
#             2 用户管理自己的文章
#                 1 创建文章应用
#                 2 设置栏目
#                 3 编辑栏目
#                 4 删除栏目
#
#         42 文章管理和显示（文章管理-发布文章,有可能用到富文本编辑器markdown）
#             1 发布
#              1 再每个栏目后面正价发布文章按钮
#              2 进入新页面显示 能编辑的框 标题
#              4 栏目 根据前面的url定制
#              3 内容：大文本输入框
#              4 发布按钮
#             2 文章列表
#
#                序号 标题  栏目 操作（删除，修改） 点击文章显示详细信息
#
#         43 设置分页功能
#         44 网站文章的展示
#                 1 采用分页展示文章列表（登录用户和非登录用户都可以浏览）
#                 2 模板部分显示
#                     作者：xx
#                     概要：
#                         截取文章前70个字符
#
#         45 网站功能扩展
#             1 静态页面的处理（直接返回html文件）
#
#             2 设置用户登录之后跳转的页面()
#
#         46 为文章点赞
#             1 为发布文章增加新字段用于记录点赞，为多对多数据乐行一个用户可以
#                 给多遍文章点赞，一篇文章可以接受多个用户点赞
#             2 详细文章页面显示点占数，和点赞连接
#
#         47 文章阅读次数
#             使用redis记录文章阅读次数
#
#         48 显示最热文章
#
#             创建redis集合 使用redis排序功能
#
#         49 文章评论功能
#             登录网站的用户有权限对任何文章发表评论
#                 创建模型外键与文章
#             评论内容都显示在文章后面
#
#         50 某用户发布的文章总数统计
#             最新发布的文章列表
#             评论最多的文章列表
#             （使用自定义模板标签）
#
#         51 收集和展示网站图片
#             1 创建应用
#             2 创建模型类
#                 1 多对一用户
#                 2 图片名
#                 3 url地址
#                 4 图片描述
#                 5 图片收集时间
#                 6 图片
#             3 创建表单类
#             4 视图函数
#             5 图片保持配置
#             6 URL配置
#             7 缩略图  （第三方插件）
#
#
#
#             1 pip3 install -i https://pypi.douban.com/simple django==1.11.3
#
#             2 django-admin startproject blog_django
#
#             3 python manage.py startapp blog_app
#
#             5 TIME_ZONE = 'Asia/Shanghai'
#
#             6 class BlogArticles(models.Model):
#
#                 title = models.CharField(max_length=300)
#                 author = models.ForeignKey(User, related_name="blog_posts")
#                 body = models.TextField()
#                 publish = models.DateTimeField(default=timezone.now)
#
#                 class Meta:
#                     ordering = ("-publish",)
#
#                 def __str__(self):
#                     return self.title
#             7 python manage.py makemigrations
#                 python manage.py migrate
#
#             8 python manage.py createsuperuser
#                 from .models import BlogArticles
#                 admin.site.register(BlogArticles)
#
#             9 class BlogArticlesAdmin(admin.ModelAdmin):
#                 list_display = ("title", "author", "publish")
#                 list_filter = ("publish", "author")
#                 search_fields = ("title", "body")
#                 raw_id_fields = ("author", )
#                 date_hierarchy = "publish"
#                 ordering = ['publish', 'author']
#
#                 admin.site.register(BlogArticles, BlogArticlesAdmin)
#
#             10 'DIRS': [os.path.join(BASE_DIR, 'templates')],
#                'APP_DIRS': False,   # 不再按照django默认寻找方式搜索魔板 (注意：此处改成False 后台管理admin会出现找不到显示模板的问题)
#
#             11 <!DOCTYPE html>
#                 <html lang="en">
#                 <head>
#                     <meta charset="UTF-8">
#                     <title>{% block title %}{% endblock %}</title>
#
#                 </head>
#                 <body>
#                     <div class="container">
#                         {% block content %}
#                         {% endblock %}
#                     </div>
#                 </body>
#                 </html>
#
#             12 {% extends 'base.html' %}
#
#
#                 {% block title %}
#                     title
#                 {% endblock %}
#
#                 {% block content %}
#                     <div>
#                         <h1>我的博客</h1>
#                     </div>
#                     <div>
#                         <ul>
#                             {% for blog in blogs %}
#                                 <li>{{ blog.title }}</li>
#                             {% endfor %}
#                         </ul>
#                     <div>
#                         <h2>django版本1.11.3</h2>
#                     </div>
#                     </div>
#                 {% endblock %}
#
#             13 url(r'^blog/', include('blog_app.urls', namespace='blog', app_name="blog_app"))
#
#             14 from django.conf.urls import url
#
#                 from . import views
#
#                 urlpatterns = [
#
#                     url(r'^$', views.blog_title, name='blog_title')
#                 ]
#
#             15 def blog_title(request):
#
#                 blogs = BlogArticles.objects.all()
#                 return render(request, 'title.html', {"blogs": blogs})
#
#             16 {% block content %}
#                     <div>
#                         <h1>我的博客</h1>
#                     </div>
#                     <div>
#                         <ul>
#                             {% for blog in blogs %}
#                                 <li><a href="{{ blog.id }}">{{ blog.title }}</a></li>
#                             {% endfor %}
#                         </ul>
#                     <div>
#                         <h2>django版本1.11.3</h2>
#                     </div>
#                     </div>
#                 {% endblock %}
#
#             17  url(r'^(\d+)/$', views.blog_article, name="blog_articles"),
#
#             18 {% extends 'base.html' %}
#
#                 {% block title %}
#                     article_content
#                 {% endblock %}
#
#                 {% block content %}
#
#                     <p><span>标题：</span>{{ article.title }}</p>
#                     <p><span>作者：</span>{{ article.author }}</p>
#                     <p><span>内容：</span>{{ article.body }}</p>
#                     <p><span>发表时间：</span>{{ article.publish }}</p>
#                 {% endblock %}
#
#             19 def blog_article(request, blog_id):
#
#                 #blog = BlogArticles.objects.filter(id=blog_id).first()
#                 blog = get_object_or_404(BlogArticles, id=blog_id)
#                 return render(request, 'content.html', {"article": blog})
#
#             20 STATICFILES_DIRS = (
#                     os.path.join(BASE_DIR, "static")
#                 )
#
#             21 {% load staticfiles %}   # 声明引入静态文件的标签 才能使用 ｛% static xxx %｝
#                 <div class="container">
#                     <nav class="navbar navbar-default" role="navigation">
#                         <div class="navbar-header">
#                             <a href="" class="navbar-brand">
#                                 <img src="{% static '/images/timg.jpg' %}" alt="">
#                             </a>
#                         </div>
#                         <div>
#                             <ul class="nav navbar-nav" role="navigation">
#                                 <li><a href="{% url 'blog:blog_title' %}">BLOG</a></li>
#                             </ul>
#                             <ul class="nav navbar-nav navbar-right">
#                                 <li><a href="#">登录</a></li>
#                             </ul>
#                         </div>
#                     </nav>
#                 </div>
#             22 <div class="container">
#                     <hr>
#                     <p class="text-center">@django1.11.3</p>
#                 </div>
#
#             23 {% load staticfiles %}
#                 <!DOCTYPE html>
#                 <html lang="en">
#                 <head>
#                     <meta charset="UTF-8">
#                     <title>{% block title %}{% endblock %}</title>
#                     <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
#                 </head>
#                 <body>
#
#                     {% include "header.html" %}
#                     <div class="container">
#                         {% block content %}
#
#                         {% endblock %}
#                     </div>
#                     {% include "footer.html" %}
#                     {% block javascript %}
#
#                     {% endblock %}
#                 </body>
#                 </html>
#             24 去环境中django包下templates的admin目录和registration目录复制到项目templates目录下
#
#             27 from django import forms
#
#                 class LoginForm(forms.Form): # 若果表单不会对数据库进行更改使用Form
#
#                     username = forms.CharField()
#                     password = forms.CharField(widget=forms.PasswordInput)
#
#             28 {% extends 'base.html' %}
#
#                 {% block content %}
#                     <form action="{% url 'account:login' %}" method="post">
#                    {% csrf_token %} {# 与表单内容一同被提交#}
#                         {{ form.as_p }}
#                         <input type="submit" value="提交">
#                     </form>
#                 {% endblock %}
#
#
#                 def user_login(request):
#
#                     if request.method == 'POST':
#                         print(request.POST)
#                         login_form = LoginForm(request.POST)
#                         if login_form.is_valid():   # 验证所传入数据是否合法
#
#                             data = login_form.cleaned_data
#                             print(data)
#                             user = authenticate(username=data['username'], password=data['password']) # 判断此用户是否为本站注册用户和验证密码是否正确
#                             print(user)
#                             if user:
#                                 login(request, user) # 将用户id保存在session中，完整用户登录操作
#                                 return HttpResponse('欢迎，您的验证成功！')
#                             else:
#                                 return HttpResponse("对不起，您输入的账号密码有误")
#                         else:
#                             return HttpResponse('对不起您的账户并未激活')
#
#                     if request.method == "GET":
#                         login_form = LoginForm()
#                         return render(request, 'login.html', {"form":login_form})
#             29 <ul class="nav navbar-nav navbar-right">
#                     <li><a href="{% url 'account:user_login' %}">登录</a></li>
#                 </ul>
#
#             30 from django.contrib.auth import views as user_inside
#                 url(r'login_inside/$', user_inside.login, {"template_name": 'login.html'}, name="user_inside")
#
#             31 {% if user.is_authenticated %}
#
#                     <ul class="nav navbar-nav navbar-right">
#                         <li><a href="#">退出</a></li>
#                     </ul>
#                     <ul class="nav navbar-nav navbar-right">
#                         <li><a href="#">欢迎！{{ user.username }}</a></li>
#                     </ul>
#                 {% else %}
#                     <ul class="nav navbar-nav navbar-right">
#                     <li><a href="{% url 'account:user_login' %}">登录</a></li>
#                 </ul>
#                 {% endif %}
#
#             32 def user_logout(request):
#                 logout(request)
#                 return redirect(reverse('account:user_login'))
#
#             33 class RegisterForm(forms.ModelForm):  # 若果表单中吸入数据库或修改数据库，使用ModelForm
#
#                     password = forms.CharField(label="密码", widget=forms.PasswordInput)
#                     password2 = forms.CharField(label="确认密码", widget=forms.PasswordInput)
#
#                     class Meta:
#                         model = User  # 声明表单类所应用到的数据模型
#                         fields = ("username", "email") # 声明所有选用的字段
#
#                     def clean_password2(self):   # 自定义检测 clean_+ 属性名称，在 对象.is_valid()方法时候会执行
#                         data = self.cleaned_data
#                         if data['password'] != data['password2']:
#                             raise forms.ValidationError('输入密码不一致')
#                         return data['password2']
#
#             34 def register(request):
#
#                     if request.method == 'POST':
#                         register_form = RegisterForm(request.POST)
#                         if register_form.is_valid():
#                             user = register_form.save(commit=False) # 生成数据对象不存入到数据库中
#                             user.set_password(register_form.cleaned_data['password'])
#                             user.save() # 将对象存储到数据库中
#                             return redirect(reverse('account:user_login'))
#
#                     register_form = RegisterForm()
#                     return render(request, 'register.html', {"form":register_form})
#
#
#             35 class UserOtherInfo(models.Model):
#
#                 phone = models.CharField(max_length=20, null=True)
#                 birth = models.DateField(blank=True, null=True)
#                 user = models.OneToOneField(User, unique=True)
#
#                 def __str__(self):
#                     return self.user.username
#
#             36 def register(request):
#
#                 if request.method == 'POST':
#
#                     register_form = RegisterForm(request.POST)
#                     register_other_info_form = RegisterOtherInfoForm(request.POST)
#                     if register_form.is_valid() and register_other_info_form.is_valid():
#                         new_user = register_form.save(commit=False) # 生成数据对象不存入到数据库中
#                         user_other = register_other_info_form.save(commit=False)
#                         new_user.set_password(register_form.cleaned_data['password'])
#                         new_user.save()  # 必须先存储 不然后面找不到onetonone对象
#                         user_other.phone = register_other_info_form.cleaned_data['phone']
#                         user_other.birth = register_other_info_form.cleaned_data['birth']
#                         user_other.user = new_user # 指定了onetoone对象
#                         user_other.save()
#
#                         return redirect(reverse('account:user_login'))
#                 register_other_info_form = RegisterOtherInfoForm()
#                 register_form = RegisterForm()
#                 return render(request, 'register.html', {"form":register_form, 'form1':register_other_info_form})
#
#
#                 class RegisterOtherInfoForm(forms.ModelForm):
#
#                     class Meta:
#
#                         model = UserOtherInfo
#                         fields = ('phone', 'birth')
#
#
#                 {% extends 'base.html' %}
#
#                 {% block content %}
#
#                     <form action="{% url 'account:register' %}" method="post">
#                         {% csrf_token %}
#                         {{ form.as_p }}
#                         {{ form1.as_p }}
#                         <input type="submit" value="注册">
#                     </form>
#                 {% endblock %}
#
#             37  根据源码设定参数
#                 from django.contrib.auth.views import password_change, password_change_done
#                 url(r'password_change/$', password_change, {"post_change_redirect": '/account/password_change_done'}, name="password_change"),
#                 url(r'password_change_done/$', password_change_done, name="password_change_done"),
#
#             38 password_reset内置重设密码
#                 url(r'password_reset/$', password_reset, {"post_reset_redirect": '/account/password_reset_done'}, name="password_reset"),
#                 url(r'password_reset_done/$', password_reset_done, name="password_reset_done"),
#                 url(r'password_reset_confirm/$', password_reset_confirm, {"post_reset_redirect": "/account/password_reset_complete"}, name="password_reset_confirm"),
#                 url(r'password_reset_complete/$', password_reset_complete, name="password_reset_complete"),
#                 url(r'password_reset_confirm/(?P<uidb64>.+)/(?P<token>.+)/$', password_reset_confirm, {"post_reset_redirect": "/account/password_reset_complete"}, name="password_reset_confirm"),
#
#                 url(r'^accounts/', include('account.urls', namespace='account', app_name="account"))
#
#                 EMAIL_HOST = 'smtp.qq.com'
#                 EMAIL_HOST_USER = '174927390@qq.com'
#                 EMAIL_HOST_PASSWORD = 'baleguedteflbhci'
#                 EMAIL_PORT = 25
#                 EMAIL_USE_TLS = False
#                 EMAIL_USE_SSL = False
#                 DEFAULT_FROM_EMAIL = '174927390@qq.com' # 发件人邮箱地址
#
#                 其他模板配置等
#
#             39 使用第三方密码重置功能
#
#                 1 安装
#                     pip3 install django-password-reset
#                 2 注册应用
#
#                     "password_reset"
#
#                 3 配置url
#
#                     将虚拟环境中该组件下的templates中文件复制拷贝到本项目下的templates中
#
#                 4 使用方法和内置方法差不多（选择用原来的）
#
#
#             40 class UserInfo(models.Model):
#                 user = models.OneToOneField(User, unique=True)
#                 school = models.CharField(max_length=100, blank=True)
#                 company = models.CharField(max_length=100, blank=True)
#                 profession = models.CharField(max_length=100, blank=True)
#                 address = models.CharField(max_length=100, blank=True)
#                 aboutme = models.TextField(blank=True) # blank=True 该数据项可以为空，即在前端页面允许用户不填写
#
#                 def __str__(self):
#                     return "self.user.username"
#
#
#
#                 class UserInfoForm(forms.ModelForm):
#
#                     class Meta:
#                         model = UserInfo
#                         fields = ('school', 'company', 'profession', 'address', 'aboutme')
#
#                 class UserForm(forms.ModelForm):
#
#                     class Meta:
#                         model = User
#                         fields = ('email',)
#
#
#                 from django.contrib.auth.decorators import login_required
#
#                 @login_required(login_url='/account/login/')  # 在执行函数之前执行装饰器 只有登录用户才能执行下面函数
#                                                                 # 参数是如果不是登录用户会自动跳转到参数执行的网页
#                 def myself(request):
#                     user = User.objects.get(username=request.user.username)
#                     user_other_info = UserOtherInfo.objects.get(user=user)
#                     user_into = UserInfo.objects.get(user=user)
#                     return render(request, 'myself.html', {"user":user, "user_other_info":user_other_info, "user_info":user_into})
#
#
#
#                 @login_required(login_url='/account/login/')
#                 def myself_edit(request):
#
#                     user = User.objects.get(username=request.user.username)
#                     user_other_info = UserOtherInfo.objects.get(user=user)
#                     user_info = UserInfo.objects.get(user=request.user)
#
#                     user_form = UserForm(instance=request.user)
#                     user_other_info_form = UserOtherInfoForm(initial={"birth":user_other_info.birth,
#                                                                   "phone":user_other_info.phone})
#                     user_info_form = UserInfoForm(initial={"school":user_info.school,
#                                                        "company":user_info.company,
#                                                        "profession":user_info.profession,
#                                                        "address":user_info.address,
#                                                        "aboutme":user_info.aboutme})
#                     if request.method == "POST":
#                         user_form = UserForm(request.POST)
#                         user_other_info_form = UserOtherInfoForm(request.POST)
#                         user_info_form = UserInfoForm(request.POST)
#                         if user_form.is_valid() and user_other_info_form.is_valid() and user_info_form.is_valid():
#                             user_data = user_form.cleaned_data
#                             user_other_info_data = user_other_info_form.cleaned_data
#                             user_info_data = user_info_form.cleaned_data
#
#                             user.email = user_data['email']
#                             user_other_info.birth = user_other_info_data['birth']
#                             user_other_info.phone = user_other_info_data['phone']
#                             user_info.school = user_info_data['school']
#                             user_info.company = user_info_data['company']
#                             user_info.profession = user_info_data['profession']
#                             user_info.address = user_info_data['address']
#                             user_info.aboutme = user_info_data['aboutme']
#
#                             user.save()
#                             user_other_info.save()
#                             user_info.save()
#
#
#                             return HttpResponseRedirect('/account/myself')
#
#                     return render(request, 'myself_edit.html', {"user_form":user_form,
#                                                                 "user_other_info_from":user_other_info_form,
#                                                                 "user_info_form":user_info_form})
#
#
#                     @login_required(login_url='/account/login/')
#                     def my_image(request):
#                         form = UserPhotoForm()
#                         if request.method == 'POST':
#                             if request.FILES.get('img'):
#                             # if form.is_valid():
#
#                                 current_user_info = UserInfo.objects.filter(user_id=request.user).first()
#
#                                 if current_user_info:
#
#                                     pic = request.FILES['img'] # 获取post文件
#                                     current_user_info.photo = 'user_images\\'+str(request.user)+pic.name
#
#                                     save_photo_to_static(pic, current_user_info.photo)
#                                     current_user_info.save()
#                                     return redirect(reverse('account:myself'))
#
#                                 else:
#                                     return redirect(reverse('account:user_login'))
#
#                             return redirect(reverse('account:user_login'))
#
#                         return render(request, 'imagecrop.html', {"form":form})
#
#
#                     def save_photo_to_static(pic, path):  # 保存文件
#                         import base64
#                         import os
#
#                         print(path)
#                         print(type(path))
#                         # path_url = current_user + pic_name
#                         path1 = os.path.join(BASE_DIR, 'static\\'+str(path))
#
#                         print(path1)
#                         with open(path1, 'wb') as f:
#
#                             for i in pic:
#                                 f.write(i)
#
#
#                     <li>
#                         <img alt="头像" class="img-circle" width="270px" src="{% static user_info.photo %}">
#                     </li>
#
#
#                     photo = models.FileField(blank=True, upload_to='user_images') # upload_to='文件目录' 与配置文件
#                         中的STATIC_URL = '/static/'
#                                 STATICFILES_DIRS = [
#                                     os.path.join(BASE_DIR, "static"),
#                                 ]
#                         相呼应
#
#
#             41 class ArticleColumn(models.Model):
#
#                 column = models.CharField(max_length=200)
#                 created = models.DateField(auto_now_add=True)
#                 user = models.ForeignKey(User, related_name='article_column')
#
#                 def __str__(self):
#                     return self.column
#
#
#                class ArticleColumnForm(forms.ModelForm):
#
#                 class Meta:
#                     model = ArticleColumn
#                     fields = ("column",)
#
#
#                 增
#                 @login_required(login_url='/account/login/')
#                 def add_article_column(request):
#                     form = ArticleColumnForm()
#                     if request.method == 'POST':
#                         form = ArticleColumnForm(request.POST)
#
#                         if form.is_valid():
#
#                             ArticleColumn.objects.create(column=form.cleaned_data['column'], user=request.user)  # 栏目的添加
#                             return redirect(reverse('article:article_column'))
#
#                         print('认证未成功')
#                         return redirect(reverse('article:article_column'))
#
#                     return render(request, 'add_article_column.html', {'form': form})
#
#                 删
#                 @login_required(login_url='/account/login/')
#                 def del_article_column(request, id):
#
#                     article = ArticleColumn.objects.filter(id=id).first()
#                     if article:       # 如果对象存在
#                         article.delete()   # 删除，不用写save方法
#                         return redirect(reverse('article:article_column'))
#
#                     return redirect(reverse('article:article_column'))
#
#                 改
#                 @login_required(login_url='/account/login/')
#                 def change_article_column(request, id):
#
#                     form = ArticleColumnForm()
#
#                     article = ArticleColumn.objects.filter(id=id).first()
#
#                     if request.method == 'POST':
#
#                         form = ArticleColumnForm(request.POST)  # 把post信息传入表单类
#                         if article and form.is_valid():
#
#                             article.column = form.cleaned_data['column']  # 更改数据
#                             article.save()      # 存储更改数据的操作
#                         return redirect(reverse('article:article_column'))
#
#                     return render(request, 'change_article_column.html', {'form':form, 'article':article})
#
#
#             42
#
#                 def article_column(request):
#                     columns = ArticleColumn.objects.filter(user=request.user)
#
#                     return render(request, 'article_column.html', {"columns": columns})
#
#
#                 @login_required(login_url='/account/login/')
#                 def add_article_column(request):
#                     form = ArticleColumnForm()
#                     if request.method == 'POST':
#                         form = ArticleColumnForm(request.POST)
#                         if form.is_valid():
#                             user = ArticleColumn.objects.filter(user=request.user).first() # 请求用户的确认
#                             if user:
#                                 ArticleColumn.objects.create(column=form.cleaned_data['column'], user=request.user) # 栏目的添加
#                                 return redirect(reverse('article:article_column'))
#                             return redirect(reverse('article:article_column'))
#                         print('认证未成功')
#                         return redirect(reverse('article:article_column'))
#
#                     return render(request, 'add_article_column.html', {'form': form})
#
#
#                 @login_required(login_url='/account/login/')
#                 def del_article_column(request, id):
#
#                     article = ArticleColumn.objects.filter(id=id).first()
#                     if article:       # 如果对象存在
#                         article.delete()   # 删除，不用写save方法
#                         return redirect(reverse('article:article_column'))
#
#                     return redirect(reverse('article:article_column'))
#
#
#                 @login_required(login_url='/account/login/')
#                 def change_article_column(request, id):
#
#                     form = ArticleColumnForm()
#
#                     article = ArticleColumn.objects.filter(id=id).first()
#
#                     if request.method == 'POST':
#
#                         form = ArticleColumnForm(request.POST)  # 把post信息传入表单类
#                         if article and form.is_valid():
#
#                             article.column = form.cleaned_data['column']  # 更改数据
#                             article.save()      # 存储更改数据的操作
#                         return redirect(reverse('article:article_column'))
#
#                     return render(request, 'change_article_column.html', {'form':form, 'article':article})
#
#
#                 @login_required(login_url='/account/login/')
#                 def article_post(request):
#                     form = ArticlePostForm()
#                     art_queryset = ArticleColumn.objects.filter(user=request.user).all()
#                     if request.method == 'POST':
#                         form = ArticlePostForm(request.POST)
#                         if form.is_valid():
#
#                             column = ArticleColumn.objects.filter(id=request.POST.get('article')).first()
#                             ArticlePost.objects.create(column=column, title=form.cleaned_data['title'],
#                                 content=form.cleaned_data['content'],
#                                 user=request.user)
#                             return redirect(reverse('article:article_list'))
#                         return redirect(reverse('article:article_column'))
#
#
#
#                     return render(request, 'article_post.html', {"form": form,"art_column":art_queryset})
#
#
#                 @login_required(login_url='/account/login/')
#                 def article_list(request):
#
#                     article_list = ArticlePost.objects.filter(user=request.user).all()
#
#                     return render(request, 'article_list.html', {"article_list": article_list})
#
#
#                 @login_required(login_url='/account/login/')
#                 def article_list_del(request, id):
#
#                     article = ArticlePost.objects.filter(id=id).first()
#                     if article:
#                         article.delete()
#
#
#                     return redirect(reverse('article:article_list'))
#
#
#                 @login_required(login_url='/account/login/')
#                 def article_list_edit(request, id):
#
#                     if request.method == 'POST':
#                         article_post_obj = ArticlePost.objects.filter(id=request.POST.get('article_id')).first()
#                         if article_post_obj:
#                             column = request.POST.get('column')
#
#                             column_obj = ArticleColumn.objects.filter(id=column).first()
#
#                             article_post_obj.title = request.POST.get('title')
#                             article_post_obj.column = column_obj
#                             article_post_obj.content = request.POST.get('content')
#                             article_post_obj.save()
#                         return redirect(reverse('article:article_list'))
#
#                     article = ArticlePost.objects.filter(id=id).first()
#                     columns = ArticleColumn.objects.filter(user=request.user).all()
#                     return render(request, 'article_list_edit.html', {"article": article, "columns":columns})
#
#
#                 @login_required(login_url='/account/login/')
#                 def article_info(request, id):
#
#                     article = ArticlePost.objects.filter(id=id).first()
#                     return render(request, 'article_info.html', {"article": article})
#
#             43 from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#             @login_required(login_url='/account/login/')
#             def article_list(request):
#
#                 article_list = ArticlePost.objects.filter(user=request.user).all()
#
#                 pagintor = Paginator(article_list, 2)  # 创建分页对象实例， 每页最多显示2个
#                 page = request.GET.get('page')  # 获取浏览器当前GEI请求参数page
#                 try:
#                     current_page = pagintor.page(page) # 用于指定页面的内容，参数必须是大于或等于1的整数
#                     articles = current_page.object_list # 输球该页所有对象列表
#                 except PageNotAnInteger:  # 对于异常 页码数值不是整数
#                     current_page = pagintor.page(1)
#                     articles = current_page.object_list
#                 except EmptyPage:  # 请求页面为空或在URL参数中没有page参数
#                     current_page = pagintor.page(pagintor.num_pages)  # 返回的是页数
#                     articles = current_page.object_list
#
#                 return render(request, 'article_list.html', {"articles": articles, "page": current_page})
#
#             创建分页末模板文件
#
#                 {% if page.has_previous %}   # 判断是否有上一页
#                 <a href="?page={{ page.previous_page_number }}">上一页</a> # 返回上一页的页码
#                 {% endif %}
#
#                 <span>第{{ page.number }}/{{ page.paginator.num_pages }} 页</span> # 当前页码和总页码
#
#                 {% if page.has_next %}
#                     <a href="?page={{ page.next_page_number }}">下一页</a> 返回下一页页码
#                 {% endif %}
#
#             44
#             @login_required(login_url='/account/login/')
#             def article_info(request, id):
#
#                 article = ArticlePost.objects.filter(id=id).first()
#                 return render(request, 'article_info.html', {"article": article})
#
#
#             def article_index(request):
#
#                 articles = ArticlePost.objects.all().order_by('-update_time')
#
#                 return render(request, 'article_index.html', {'articles': articles})
#
#
#             def user_of_article_list(request, id):
#
#                 try:
#                     articles = ArticlePost.objects.filter(user_id=id)
#
#                 except:
#                     return HttpResponse('404')
#
#
#                 return render(request, 'user_of_article_list.html', {"articles": articles})
#
#
#             def anonymous_article_info(request, id):
#                 article = ArticlePost.objects.filter(id=id).first()
#                 return render(request, 'anonymous_article_info.html', {"article": article})
#
#
#
#             45
#
#                 1 from django.views.generic import TemplateView
#                 url(r'^static_test/$', TemplateView.as_view(template_name="static_test.html"), name="static_test"),
#
#                 2 LOGIN_REDIRECT_URL = '/home/'
#
#             46
#                 class ArticlePost(models.Model):
#                     ...
#                     article_like = models.ManyToManyField(User, related_name='article_user_like', blank=True)
#                     ...
#
#
#                 @login_required(login_url='/account/login/')
#                 def user_like(request, id):
#                     """接受用户点赞，更新到数据库"""
#                     like_user = request.user
#                     article = ArticlePost.objects.filter(id=id).first()
#                     article.article_like.add(like_user)  # 为多对多外键增加对象
#                     # print(article.article_like.count())  # 获多对多点赞的人数
#                     # print(article.article_like.all())   # 获取多对多点赞的用户的集合
#
#                     return HttpResponse('点赞ok')
#
#             47  @login_required(login_url='/account/login/')
#                 def article_info(request, id):
#
#                     article = ArticlePost.objects.filter(id=id).first()
#                     r = redis.StrictRedis(host="localhost", port=6379, db=0) # 连接redis数据库
#                     r.incr("article:{}:view".format(id))  # 插入并增加键的值
#                     like_nums = article.article_like.count()
#                     like_users = article.article_like.all().order_by('-id')
#                     reads = r.get("article:{}:view".format(id)) # 获取键的值
#                     return render(request, 'article_info.html', {"article": article,
#                                                                  "like_nums":like_nums,
#                                                                  "like_users":like_users,
#                                                                  "reads":reads})
#
#             48 def anonymous_article_info(request, id):
#
#                 article = ArticlePost.objects.filter(id=id).first()
#                 r = redis.StrictRedis(host="localhost", port=6379, db=0)
#                 r.incr("article:{}:view".format(id))
#                 like_nums = article.article_like.count()
#                 like_users = article.article_like.all().order_by('-id')
#                 reads = r.get("article:{}:view".format(id))
#                 r.zincrby('article_ranking', reads, id)  # zincrby(self, name, amount, value):
#                 # 设置集合名字, 总数, 值
#                 article_ranking = r.zrange('article_ranking', 0, -1, desc=True)[:5]  # 对集合进行排序
#                 article_id_list = [int(i) for i in article_ranking]
#                 article_hot = ArticlePost.objects.filter(id__in=article_id_list)  # 根据多个id获取文章
#
#                 return render(request, 'article_info.html', {"article": article,
#                                                              "like_nums": like_nums,
#                                                              "like_users": like_users,
#                                                              "reads": reads,
#                                                              "article_hot": article_hot})
#
#             49 @login_required(login_url='/account/login/')
#                 def article_info(request, id):
#
#                     article = ArticlePost.objects.filter(id=id).first()
#                     r = redis.StrictRedis(host="localhost", port=6379, db=0)
#                     r.incr("article:{}:view".format(id))
#                     like_nums = article.article_like.count()
#                     like_users = article.article_like.all().order_by('-id')
#                     reads = r.get("article:{}:view".format(id))
#
#                     r.zincrby('article_ranking', reads, id) # zincrby(self, name, amount, value):
#                                                             # 设置集合名字, 总数, 值
#                     article_ranking = r.zrange('article_ranking', 0,-1,desc=True)[:5] # 对集合进行排序
#                     article_id_list = [int(i) for i in article_ranking]
#                     article_hot = ArticlePost.objects.filter(id__in=article_id_list) # 根据多个id获取文章
#                     commenter = ArticleComment.objects.filter(article=article).all()
#
#                     form = ArticleCommentForm()
#
#                     if request.method == 'POST':
#                         form = ArticleCommentForm(request.POST)
#                         if form.is_valid():
#                             com_user = request.user
#                             com_content = form.cleaned_data['comment_content']
#                             com_art = ArticlePost.objects.filter(id=id).first()
#                             ArticleComment.objects.create(article=com_art, commenter=com_user,
#                                                           comment_content=com_content)
#
#                     return render(request, 'article_info.html', {"article": article,
#                                                                  "like_nums": like_nums,
#                                                                  "like_users": like_users,
#                                                                  "reads": reads,
#                                                                  "article_hot": article_hot,
#                                                                  "form": form,
#                                                                  'commenter': commenter})
#
#             50 def user_of_article_list(request, id):
#             from django.db.models import Count
#             user = User.objects.filter(id=id).first()
#
#             try:
#                 articles = ArticlePost.objects.filter(user_id=id)
#                 # print(articles)
#
#             except:
#
#                 return HttpResponse('404')
#
#             num = ArticlePost.objects.filter(user_id=id).count()
#             # print(num)
#             lately = ArticlePost.objects.filter(user_id=id).order_by('-update_time')
#
#
#             dic = {}
#
#             for article in articles:
#                 com = ArticleComment.objects.filter(article=article).all()
#                 if com:
#                     for i in com:
#
#                         if not article.title in dic:
#                             dic[article.title] = 1
#                         else:
#                             dic[article.title] += 1
#
#             result = sorted(dic.items(), key=lambda x:x[1], reverse=True)[0:3]  # 根据键的值进行排序
#
#             com_hot = []
#             for title in result:
#                 article = ArticlePost.objects.filter(title=title[0]).first()
#                 com_hot.append(article)
#
#
#             # print(dic)
#             return render(request, 'user_of_article_list.html', {"articles": articles, "num": num,
#                                                                  "lately": lately, "com_hot":com_hot})
#
#
#
#
#
#
#
# =============================================
# =============================================
# django通用视图
#
#
# TemplateView
#
#     第一种写法（不用写视图类）
#
#         from django.views.generic import TemplateView
#         url(r'^about/$', TemplateView.as_view(template_name='course/about.html'), name="about"),
#
#     第二种写法
#         url(r'^about1/', views.AboutView.as_view(), name="about1"),
#         class AboutView(TemplateView):
#             template_name = "course/about.html"
#
#
# ListView(相当于实现了Course.object.all()功能)
#
#     class CourseListView(ListView):
#         model = Course
#         context_object_name = "courses"  # 声明了传入模板中的变量名称
#         template_name = 'course/course_list.html'