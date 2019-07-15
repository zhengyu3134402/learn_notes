#
# =========================================================
# 随机验证码
#
# 1 导入random模块
#     import random
# 2 定义函数，定义空列表，生成x位数字和字母(比如 5位)
#     def f():
#         li = []
# 3 生成小写字母
#     def f():
#         li=[]
#         for i in range(5):
#             a = chr(random.randint(97, 122))
# 4 生产随机大写字母
#     b = chr(random.randint(65, 90))
#
# 5 生产随机数字,并转化成字符串
#     c = str(random.randint(0, 9))
#
# 6 随机选取大写字母，小写字母，数字
#     d = rangom.choice([a, b, c])
# 7 将随机生成的对象加入到空列表li,
#     li.append(d)
#
# 8 返回5位随机数字或字母,并加入到session为了服务器校验用
#     request.session['xx'] = ''.join(li)
#     return ''.join(li)
# 9 截取一张图片
# 10 打开图片,进行读取（）
#     with open(图片, 'rb')as f:
#         png = f.read()
# 11 返回给浏览器 注意 content_type参数
#     return HttpResponse(data, content_type='image/png')
#
# 12 模板中获取图片
#     <img src="返回图片的url">
#
# 13 安装pillow插件
#     pip3 install pillow
#
# 14 使用pillow，创建图片
#     1 导入Image图片对象，ImageDraw画笔对象，ImageFont字体对象
#         from PIL import Image, ImageDraw
#     2 创建Image对象，并传入参数
#         a = Image.new('RGB',(长, 宽), (RGB颜色数字)) # RGB颜色数字为背景颜色可设置成随机函数
#     3 创建画笔对象
#         b = ImageDraw.Draw(a)
#
#     4 创建字体对象
#         c = ImageFont.truetype('字体文件路径'，字体大小)
#
#     5 利用画笔对象验证码写入图片
#         b.text((0,0),'内容',fill=(填充颜色RGB)，font=c)
#             # (0,0)为x轴，y轴坐标，font为指定字体对象，RGB填充颜色使用函数设置为随机颜色
#             # 循环一次写一个数字 注意调整y轴坐标，防止都写在一起
#
#     6 保存图片对象（建议将图片保存在内存中）
#         1 导入BytesIO模块
#             from io import BytesIO
#         2 创建BytesIO对象
#             s = BytesIO()
#         3 存储图片对象到内存
#             a.save(f1, format='PNG')
#     7 从内存中提起图片,然后返回浏览器
#         image_data = s.getvalue()
#         return HttpResponse(data, content_type='image/png')
#
# 总体流程
#     创建图片，写入图片，将图片存入内存，从内存提起图片返回给浏览器
#
# 扩展
#     是验证码点击局部刷新
#     <script>
#         img = document.getElementById('图片标签的ID')
#         img.onclick = function(){
#             img.src += '?'
#             }
#     </script>
#
#     图片加干扰线
#         width = 250   # 图片宽度
#         heigth = 25   # 图片高度
#         for i in range(5):
#             x1 = rangdom.randint(0, width)
#             x2 = rangdom.randint(0, width)
#             y1 = rangdom.randint(0, height)
#             y2 = rangdom.randint(0, height)
#             draw_obj.line((x1, y1, x2, y2), fill=random_color())
# =========================================================
#
#
# =========================================================
# excelexcel表格的写入
#
# Excel（xlsx结尾的2007版本以后）
#
#     1 安装openpyxl
#         pip3 install openpyxl
#
#     2 创建表格
#         def make_excel():
#             filepath = os.getcwd() + '\\test.xlsx'
#             wb = openpyxl.Workbook()
#             wb.save(filepath)
#     3 向表格写入数据，追加
#         def write_to_excel():
#             filepath = os.getcwd() + '\\test.xlsx'
#             wb = openpyxl.load_workbook(filepath)
#             ws = wb.active
#             a = [1,2,3]
#             ws.append(data)  # 用append方法直接向表格中按照列表的顺序添加一行数据，追加
#             wb.save(filepath)
#
# =========================================================


# ========================================================
# celery

# 	介绍分布式任务队列
# 	处理大量消息的分布式系统，实时处理任务队列，同时也支持任务调度
# 	流程
# 		发出任务(项目代码)  ----》 任务队列（中间人broker）---》处理任务worker

# 安装条件
# 	中间人（发送和接收消息）独立的服务形式
# 		RabbiMQ
# 		Redis
# 		数据库
# 		。。。。
# 安装
# 	pip3 isntall celery

# 使用
# 	1 创建包和文件
# 		推荐项目根目录下创建包 包中创建tasks.py文件
# 	2 文件中导入类 创建对象
# 		from celery import Celery
# 		app = Celery("推荐写次文件的路径", broker="redis://127.0.0.1:6379/0"')
	
# 	3 定义任务函数 在任务函数上面加上 @app.task 进行装饰
# 		@app.task
# 		def xx():
			
# 	4 其他模块中使用该函数
# 		导入
# 		xx.delay(如果需要传参数在此传参)
# 	5 启动任务处理者worker
		
# 		celery初始化
# 			django环境初始化(django中wsgi.py中自动进行了初始化django,celery需要手动处理初始化,) # 如果处理者在不用的机器
# 				import os
# 				imort django
# 				os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rest_api2.settings")
# 				django.setup()
		
# 		celery -A 创建Celery中写的路径 worker  不显示打印信息
# 		或
# 		celery -A 创建Celery中写的路径 worker -l info显示打印信息

# 出现错误处理
# 	windows会出现的错误
# 		ValueError: not enough values to unpack (expected 3, got 0)
		
# 		解决
			
# 			pip3 install eventlet

# 			启动 celery -A <mymodule> worker -l info -P eventlet

# 传入@app.task的下的函数参数不要有对象类型 因为序列化会出现错误

# ========================================================
# 
# ========================================================
# django中全文搜索功能
	
# 	介绍
# 		1 用mysql的like语句也能做，但效率极低，一般不用
# 		2 使用搜索引擎
# 			搜索引擎做的事情
# 				1 可以对表中某些字段进行关键词分析，建立关键词对应的索引数据
# 		3 使用全文检索框架
# 			用户通过--》全文检索框架--》使用搜索引擎
# 	全文检索框架haystack
		
# 		支持whoosh, solr, xapian, elasticsearc四种搜索引擎
			
# 			1 whoosh 为python编写的搜索因此，性能不如以上其他3个，但稳定对于小型网站足够使用
	
# 	使用whoosh
# 		1安装

# 			pip3 install django-haystack
# 			pip3 install whoosh
# 		2注册应用
# 			‘haystack’
# 		3配置
# 			HAYSTACK_CONNECTIONS={
# 				'default':{
# 					"ENGINE":"haystack.backends.whoosh_cn_backend.WhooshEngine", # 搜索引擎
# 					"PATH": os.path.join(BASE_DIR, 'whoosh_index'),# 搜索文件路径
# 					}
# 			}
			
# 			HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor' # 当添加，修改，删除数据时候，自动生成索引

# 		4 创建索引文件
			
# 			对模型类创建索引类

# 			1在应用下面创建search_indexes.py文件
# 			2定义索引类

# 				from haystack import indexes
# 				from xx # 导入要创建索引类的模型
# 				class A(indexes.SearchIndex, indexes.Indexable):
# 					text = indexes.CharField(document=True, use_template=True)# 索引字段
# 						# use_template=True 指定根据表中的哪些字段建立索引文件的说明放在一个文件中
					
# 					def get_model(self):
# 						return 导入的模型类
# 					def index_queryset(self, using=None):        # 建立索引的数据
# 						return self.get_model().objects.all()
					
# 		5 创建索引文件目录
# 			templates下创建 search/indexes/模型类所在应用名的目录/模型类小写_text.txt
# 		6 配置索引文件（模型类小写_text.txt）
# 			# 指定根据表中的哪些字段建立索引数据 可以写多个以为这在哪些字段范围内查找
# 			{{ object.字段 }}  # 根据字段建立索引
# 		7 建立索引文件
# 			执行命令
# 				python manage.py rebuild_index

# 		8 前段html配置

# 			搜索框
# 				<form method="get" action="xx">
# 					<input type="text" name="q">  # name="q" 固定写法
# 					<input type="submit">
# 				</form>
# 		9 配置路由
# 			url(r'^xx/', include('haystack.urls')),
# 		10 配置search.html
# 			搜索的结果会返回到search.html文件
# 			1 创建search.html
# 				templates/search/search.html
			
# 			2 获取返回的信息

# 				{{ query }} # 搜索的关键字
# 				{{ page }} # 当页的配置对象集合
				
# 				{% for i in page %}
# 					{{ i.object }} # 获取对象
# 				{% endfor %}

# 				{{ paginator }}  # 获取分页对象
		
# 		11 改变分词方式
			
# 			因为有的中文搜索不出来
			
# 			jieba分词包
# 				1  安装
# 					1 pip3 install jieba
# 				2 在虚拟环境包下..../python3.6/site-packages/haystack/backends/ 创建 ChineseAnalyzer.py文件
				
# 				3 ChineseAnalyzer.py中创建类
# 					class ChineseTokenizer(Tokenizer):
# 						def __call__(self, value, positions=False, chars=False,
# 								keeporiginal=False, removestops=True,
# 								start_pos=0, start_char=0, mode="", **kwargs):
# 						t = Token(positions, chars, removestops=removestops, mode=mode, **kwargs)
# 						seglist = jieba.cut(vaule, cut_all=True)
# 						for w in seglist:
# 							t.original = t.text = w
# 							t.boost = 1.0
# 							if positions:
# 								t.pos = start_pos + value.find(w)
# 							if chars:
# 								t.startchar = start_char + value.find(w)
# 								t.endchar = start_char + value.find(w) + len(w)
# 							yield t
					
# 					def ChineseAnalyzer():
# 						return ChineseTokenizer()
# 				4 备份 ..../python3.6/site-packages/haystack/backends/ 的whoosh_backend.py文件
# 					拷贝文件
# 						在拷贝文件中
# 							导入 .ChineseAnalyzer import ChineseAnalyzer
# 							在此文件中 查找 analyzer=StemmingAnalyzer()
# 							将StemmingAnalyzer()改成ChineseAnalyzer（）
# 				5 更改settings中的HAYSTACK_CONNECTIONS 下的 "ENGINE"配置 换乘上面 改变的文件
			
# 				6 重新生产索引文件
# 					python manage.py rebuild_index

# ========================================================