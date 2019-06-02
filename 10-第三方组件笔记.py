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