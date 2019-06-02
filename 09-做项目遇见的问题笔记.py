# ==============================================
# 问题汇总
#
# {% csrf_token %} 放在form标签里面
#
# 手动创建数据库时候记得设置默认编码,要不然插入中文会出现问题
# create database 数据库名 default charset=utf8;
#
# 提交get的form表单
# <form action="/add_list/" method="GET">
#
#
# 路由中(?<名字>..) 要和视图函数中接受的参数 名字相同 呢
#
#
# QuerySet对象 才能进行ORM的删除,增加,更改的操作
#
#
# ORM操作  filter得出的是QuerySet类似列表, get直接拿到对象
#
# 模型 ForeignKey 1.11版本 默认 级联删除on_delete=models.CASCADE
# 2.0之后需要制定
#
# 外键字段名 会自动在数据空中 变成 外键字段名_id
# 若查询 带外键的字段  对象的外键字段(创建model时候的字段名) 会得到外键的对象
# 若查询 外键字段名_id 才会查处 外键的id
#
#
# 获取select options 选择标签中的值 取 select 标签中 name属性的名
# 会获取 options 中 value属性的 的值
#
#
# select options相关联默认选中
# <select name="press_id">
# 	{% for press_obj in presses_list %}
# 	<!-- 添加功能 书名称和出版社相连 -->
# 		{% if book_obj.presses == press_obj %} 	<!-- 如果图书的出版商和 出版商一样 -->
# 				<!-- 那么默认选中 -->
# 			<option  selected value="{{ press.id }}">{{ press_obj.name }}</option>
# 			}
# 		{% else %}
# 			<option value="{{ press.id }}">{{ press_obj.name }}</option>
# 		{% endif %}
# 	{% endfor %}
# </select>
#
#
#
# action=""  默认提交到当前页
#
#
# 使用ORM对数据库更改 最后更改的对象 要用 对象.save() 同步到数据库
#
#
# 在django已经建好的表中在添加一个字段
# 运行python3 manage.py makemigrations
# 会出现如下提示:
# 给数据库中已经存在的表调价另外一个字段,这个字段即没有默认值也不能为空
# ORM不知道数据库中已经存在的数据改怎么处理这个字段
#  1) Provide a one-off default now (will be set on all existing rows
#  	with a null value for this column)
# 选1 设置数据库中添加列的默认值
#  2) Quit, and let me add a default in models.py
# Select an option:
# 选2退出 在model.py 添加的字段整设置defaule值或者是填写 null=True表示这个字段
# 可以为空
#
#
# 多对s
# 	对象.aaa   # 这是一个ORM提供的桥梁工具,帮组查找对应关系
# 	对象.aaa.all() 夺取关联的所有数据
#
#
# django jinja2 不需要加()  jinjia2会自动执行
#
#
# {% for i in xxx %} 当i为空的时候 使用
# .....
# {% empty %}
# 做事情       # 页面上会显示 做事情
#
#
# select标签的多选属性 multiple
#
# 多对多关系添加关系数据 通过 表名.多对多变量.add(x)方法添加,一次只能加一个
#
# ORM 会根据数据库中的类型 将添加进来的数据自动转换成数据库中类型
#
# new_authors_obj.books.set(books_id) 用于添加元素为列表的元素(
# 如果原来有数据那么set意义为 删除原先的数据添加新的)
# 等同于 new_authors_obj.books.add(*books_id)(或 .add(id1,id2))
#
# ORM 中 .clear() 清空数据
#
# 上传文件form表单要带有enctype="multipart/form-data"属性 ,否则上传无效
#
# 获取POST 发送的文件 request.FILES.get
#
# 用f=request.FILES.get 接受到的是文件对象 用f.name获取文件的名字
#
# 文件的读写用官方推荐写法
# for chunk in file_obj.chunks():
# 	f.write(chunk)
#
# 注意网络传输的是2进制文件 ,所以读写都用2进制
#
# 获取django的路径
# 	from django.conf import settings
#
# button 按钮 type="submit" 和 input type="submit效果一样
#
#
# ==============================================
# 通过视频发现问题
# 外键的增删改查
#  press = models.ForeignKey(to="Press", on_delete=models.CASCADE)
#  外键查询
#  	obj.press     拿到的是obj关联的对象
#  	obj.press_id  拿到的是实际字段的值
# 多对对关系的增删改
# 	查询外键关联的所有数据
# 		obj1.外键.obj2.all()
# 	修改
# 		obj.set([a,b,c])
# 		obj.add(a,b,c)
# 	清除对应关系
# 		obj.clear()
#
#
# 字符串时间,格式化时间转换
# time.strptime("xx", "ttt") 将字符串时间转化成格式化时间
# time.localtime(132412123123) 传入描述将秒数转化成格式化时间
# time.strftime("ttt", g) # 将格式化时间转换成字符串
#
# 时间的计算用datatime(datatime.timedelta(x=xy)时间间隔)
#
# django添加包 django需要重启
#
#
# def wrapper(fn):
# 	def inner(*arg, **kwargs):
# 		ret = fn(*arg, **kwargs)
# 		return ret
# 	return inner
# @wrapper
# def test():
# 	pass
#
#
# 模板
# 	组件
# 		导入组件 {% include "nav.html" %}
#
# 	静态文件
# 		{% load static %}
# 		{% static "相对路径" %} --> 去settings中获取STATCI_URL "/static/" 和相对路径进行拼接
# 		{% get_static_prefix %} --> 去settings中获取STATCI_URL "/static/"
#
#
# 模板的静态文件导入
# {% load static %}
# {% static "xxxxx" %}
#
#
# 自定义inclusion_tag
# 	与include 的区别 能传参数, 可以接受参数,返回一个字典
#
# 当请求到来的时候执行view函数:
# 	1 实例化自己写的类
# 	self = cls(**initkwargs)
# 	2 self.request = request
# 	3 执行self.dispatch(reuqest, *args,**kwargs)
# 		1 执行父类中的dispatch方法
# 			1判断请求方式是否被允许
# 				1 允许的情况
# 					handler = 通过反射获取get post 方法
# 				2 不允许的情况
# 					handler = 不允许的方法
#
# 				3 handler(request, *args, **kwargs)
# 			2 返回HttpResponse对象
# 	返回HttpResponse对象 给django
#
#
# url命名和反向解析
# 	视图中应用
# 		from django.urls import reverse
# 		reverse("名字", args=(,))
# 		reverse("名子", kwargs={})
# 	在模板中应用
#
# 		{% url "名字" 参数1 参数2 %}
# 		{% url "名字" key1=参数1 key2=参数2%}
# 	命名空间
# 	reverse ("yingyong:home", args=(,))
# 	{% url "yingyong:home" 参数1 参数2 %}
#
#
#
# ORM查询
#
# 	1 返回对象列表
# 		all()
# 		filter()
# 		exclude()
# 		distinct()
# 		values()
# 		values_list()
# 	2 获取对象的
# 		get()
# 		first()
# 		last()
#
# 	3 返回数字的
# 		count()
#
# 	4 返回布尔值
# 		exists()
#
#
# 	单表中双下划线
# 		id__gt
# 		id__lt
# 		id__lte
# 		id__gte
#
# 		id__in=[]
# 		id__range=[]
#
# 		contains = ""
# 		icontains= ""
#
# 		startswith = ""
# 		istartswith = ""
# 		endswith = ""
# 		iendswith　= ""
#
# 		isnull = True
#
# 		__year
#
# 	外键查询
#
# 		正向查询
# 			obj.presses
# 			obj.presses.id
# 			obj.presses_id
#
# 		反向查询
# 			presses.book_set
# 			presses.book_set.all()
#
# 			book.objects.filter(presses__name="xx")
# 			presses.objects.filter(book__title="yy")
#
# 			related_name="books"
# 			press.books
#
# 			related_query_name = "xx"
# 			press.objects.filter(xx__title="xx")
#
# 	多对多
# 		正向
# 			author_obj.books -->管理对象
# 			author_obj.add()
# 			author_obj.books.remove()
# 			author_obj.books.clear()
# 			author_onj.books.set()
# 			author_obj.books.create()
#
# 		反向
# 			book_obj.authors -->管理对象
#
#
#
# cookie
#
# 	1 cookie
# 		是保存在浏览器本地的一组键值对
# 		cookie存在的意义 http协议是武装同,每次请求都是无关联的,没有办法保存状态
# 		使用cookie保存状态
#
# 	2 特性
# 		服务器让浏览器进行保存的cookie
# 		浏览器有权利是否进行保存
#
# 	3 cookie设置
# 		set_cookie本质是设置一个响应头
# 			ret = redirect("/press_list/")
# 			ret.set_cookie("login","1")
# 			return ret
#
# 		max_age = 秒  设置cookie保留时间,操作时间后会自动删除
#
#
# 	4 获取cookie中的gansu
# 		ret = request.COOKIES.get("xxx")
# 			to_url = request.path_info
# 	5 实现未登录客户登录网站其他页面,跳转或登录页面,
# 	  登录页面后,自动跳转会回最开始进入的其他页面,
# 	  原理
# 	  	客户被强制跳转会登录页面之前会发送GET请求
# 	  	捕获GET请求的url,带客户登录成功后自动跳转
# 	  	捕获的url
#
# 	6 删除Cookie
# 	def logout(request):
# 	    rep = redirect("/login/")
# 	    rep.delete_cookie("user")  # 删除用户浏览器上之前设置的usercookie值
# 	    return rep
#
#
#
#
# session
#
# 	session
# 		保存在服务器商一组组键值对
#
# 		session存在的意义
# 			cookie保存在浏览器商不安全
# 			cookie的长度收到限制
#
#
# 	设置session
# 		request.session["login"] = "1"
# 		request.sessoin.setdefault(key,value)
#
# 		设置超时时间
# 			request.session.set_expiry()
#
#
# 		其他公用设置项：
# 		SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
# 		SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
# 		SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
# 		SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
# 		SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
# 		SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
# 		SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）
# 		SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）
#
#
# 	获取session
# 		request.session.get("login")
# 		request.session["login"]
# 	删除session
# 		delf request.session["k1"]
# 		request.session.delete() 删除改用户的所有session数据,不删除cookie
# 		request.session.flush() 删除改用户的所有session数据,删除cookie
#
# 		清除所有的过期session
# 			request.session.clear_expired()
#
#
# ORM高级操作
# 	aggregate聚合 终止字句
# 	anotate 分组
# 	F
# 	Q Q()  & | ~
#
# 	事物
# 		from django.db import transaction
#
# 		try:
# 			with transaction.atomic():
# 				models.Author.objects.create(name="xx")
# 		except Exception as e:
# 			pritn(str(e))
#
#
#
# 中间件
#
# 	创建中间件创建一个py文件 ,定义类一定要继承
# 	from django.utils.deprecation import MiddlewareMixin
# 	class Md1(MiddlewareMixin):
# 		def process_request(self, request):
# 			print("这是Md1中的process_request方法")
# 			return HttpResponse("md1")
# 	别忘了在settings文件中注册中间件
#
# 	1 中间件定义
# 		是一个python类,用来在全局范围内处理请求和响应的一个钩子
#
# 	2 五个方法
# 		process_request(self,request)
# 		process_view(self, request, view_func, view_args, view_kwargs)
# 		process_template_response(self,request,response)
# 		process_exception(self, request, exception)
# 		process_response(self, request, response)
#
# 		参数 执行时间 执行顺序 返回值
#
# 			1 process_request(self,request)
# 				1 执行时间
# 					在视图函数执行之前
# 				2 参数
# 					request -->视图函数中用到的request
# 					使用参数request可以添加全局属性和方法
# 				3 执行顺序
# 					有多个process_request组件
# 					按照注册顺序执行中间件
# 				返回值
# 					None  正常流程走
# 					HttpResponse对象, 当前中间后面的中间件process_request和
# 					process_response,视图函数都不执行
# 					执行当前中间的process_response方法以及之前的中间的process_response方法
#
# 		2 process_response(self, request, response)
# 			1 执行时间
# 				在视图函数执行之后
# 			2 参数
# 				request -> 视图函数中用到的request
# 				response -> 视图函数中返回的response
# 			3 返回值
# 				必须是response对象
# 			4 执行顺序
# 				按照注册顺序倒序执行
#
#
# 			3 process_view(self, request, view_func, view_args, view_kwargs)
#
# 				1 执行时间
# 					在provess_request之后,以及路由匹配之后,在视图函数执行之前
# 				2 参数
# 					request -> 视图函数中用到的request
# 					view_func ->要执行的视图函数
# 					view_args ->要执行的位置参数
# 					view_kwargs ->要执行的关键字参数
# 				3 返回值
# 					None 正常走
# 					按照注册顺序执行
#
# 			4 pprocess_exception(self, request, exception)
# 				1 执行时间(触发条件:有异常才执行)
# 					在视图函数之后, 在process_response之前
# 				2 参数
# 					exception 错误对象
#
# 				3 返回值
# 					None 正常走
# 					HttpResponse对象
# 						注册顺序之前的中间件的process_exception方法不走了
# 						执行所有中间件的process_response方法
#
# 				4 执行顺序
# 					按照注册顺序倒序执行
#
#
#
# 			5 process_template_response(self,request,response)
# 				1 执行时间(触发条件:response对象要求有一个render方法)
# 					在视图函数之后,在process_response之前
# 				2 参数
# 					xxxxx
# 				3 返回值
# 					返回response
# 				4 顺序
# 					按照注册顺序倒序执行
#
# 	中间件的访问频率
# 		获取IP
# 		有访问记录
# 		根据访问记录做判断
#
#
# csrf_exempt
# post表单不加{% csrf_token %} 能提交表单
# 使用 @csrf_exempt装饰器 给单个视图排除校验
#
# csrf_protect
# 给单个视图必须校验
#
# ==============================================
# ==============================================