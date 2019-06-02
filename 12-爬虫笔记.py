#
# pip3 install -i https://pypi.douban.com/simple 软件名1
# ====================================================
# 爬虫爬虫
#
#
#
#     拿来即用(post)
#         import requests
#
#         # 反爬机制
#         headers={
#             "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
#         }
#         url=""
#         data={
#
#         }
#         reponse=requests.post(url=url, headers=headers, data=data)
#         print(reponse.json()) # json的格式数据
#
#
#
#     1 概念
#
#         1 编写程序模拟浏览器上网，然后让其去上网爬取数据的过程
#         2 分类
#             通用爬虫：搜索引擎 抓取系统（爬虫程序）的主要组成部分
#             聚焦爬虫：根据指定需要抓取以页面中指定的内容
#         3 反爬机制：
#             门户网站通过相关的技术手段或者策略来阻止爬虫进行数据的爬取
#             robots.txt协议
#         4 反反爬策略：
#             爬虫程序通过相关的技术或策略破解反爬
#         5 http 超文本传输协议（客户端和服务端进行数据交互的一种交互形式）
#           https:安全超文本传输协议（SSL加密层）
#           User_Agent:请求载体的身份标识
#           Content-Type：响应的数据类型
#         6 对称秘钥加密：
#           非对称秘钥加密
#           证书加密
#
#     2 request模块
#
#         1 概念
#
#             是python中一个原生的基于网络请求的模块
#             作用是 模拟浏览器发起请求
#
#         2 安装
#
#             pip3 install requests
#
#         3 使用
#
#             1 基本流程
#
#                 0 导入模块
#                     import requests
#                 1 指定url
#                     url='https://www.sogou.com'
#                 2 发起请求(返回值为相应对象)
#                     response=requests.get(url=url)
#                 3 获取页面数据
#                     response.text #返回的是字符串类型页面数据
#                     response.content # 返回的是二进制类型的页面数据
#                     response.json() # 返回相应对象中携带的json数据
#                     response.url # 返回的是请求的url
#                     response.headers # 返回字典类型
#                 4 持久化存储
#
#             2 相关扩展
#
#                 1 发请求使用代理ip
#                     推荐网站 www.goubanjia.com 找到适合的ip和端口
#
#                     request.get(url=url, proxies={'https':'165.155.138.149:80'})
#
#                 2 UA反爬机制处理（对UA进行伪装）
#
#                     1 制作请求头信息,发送请求
#                         headers = {
#                             'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
#                         }
#                         requests.get(url=url, headers=headers)
#
#                 3 post在登录页面输入账号密码进行登录
#
#                     1 指定url是点击登录按钮（登录成功后）发送数据的url
#
#                         1 将post请求携带的参数封装到字典中发送请求（去浏览器检查中查找）
#                             data=｛
#                                 "xx":"xx",
#                                 ......
#                             ｝
#                             request.post(url=url, headers=headers, data=data)
#
#                 4 ajax的数据抓取
#
#                     1 浏览器检查中XHR是基于ajax的请求
#                     2 找打带有参数的url请求
#                     3 去掉参数定制url
#                         url=“xxxx”
#                     4 定制参数(去浏览器检查url的请求中去找)
#                         parm = {
#                             yyyy
#                         }
#                     5 获取数据
#                         request.get(url=url, params=param, headers=xxx)
#
#                 4 获取返回多个类型数据的指定类型数据
#                     # 判断返回的类型
#                     if res.headers['Content-Type'] = 'aplication/json;charset=UTF-8'
#                         res.json()
#
#
#
# 学习视频网址
#     https://www.bilibili.com/video/av44518113/?p=40
#
# 在浏览器中请求一个url，浏览器会对这个url进行一个编码，除英文字母，数字和部分符号外，其他全部使用百分号+十六进制码
# 值进行编码
#
# 请求头常见参数
#
#     User-Agent 浏览器相关信息
#     Referfer   表明当前请求是从哪个url过来的
#     Cookie     识别用户
#
# urllib库
#
#     1 概念
#         基本的网络请求库，可以模拟浏览器行为，向指定的服务器发送请求，并
#         可以保存服务器返回的数据
#
#     2 urlopen使用
#         from urllib import request
#         a = request.urlopen("http://www.baidu.com")  # 指定请求网址
#         print(a.read())  # 读取返回的内容
#
#     3 urlretrieve使用
#         可以将指定网页文件存到本地文件中，下载图片用等
#             from urllib import request
#             request.urlretrieve("http://www.baidu.com", 'a.html') # 参数为指定网址，保存到本地文件名
#
#     4 urlencode使用
#         对发送请求的参数编码成url形式（如果有中文）
#         from urllib import parse
#         b = {"c":"我是你", "d":"dddd","e":2222}
#         a = parse.urlencode(b)
#         print(a)
#         # >>> c=%E6%88%91%E6%98%AF%E4%BD%A0&d=dddd&e=2222
#
#     5 parse_qs使用
#         对经过编码后的url参数进行解码
#         from urllib import parse
#         a = "c=%E6%88%91%E6%98%AF%E4%BD%A0&d=dddd&e=2222"
#         print(parse.parse_qs(a))
#         # >>> {'c': ['我是你'], 'd': ['dddd'], 'e': ['2222']}
#
#     6 urlparse和urlsplit
#         对url进行分割
#         from urllib import parse
#         url = "https://www.baidu.com/s?ie=UTF-8&wd=python"
#
#         a = parse.urlparse(url)
#         b = parse.urlsplit(url)
#         print(a)
#         print(b)
#         # >>> ParseResult(scheme='https', netloc='www.baidu.com',
#         # path='/s', params='', query='ie=UTF-8&wd=python', fragment='')
#
#         # >>> SplitResult(scheme='https', netloc='www.baidu.com',
#         # path='/s', query='ie=UTF-8&wd=python', fragment='')
#
#     7 request.Request类使用
#
#         请求的时候增加请求头
#         from urllib import request
#         headers = {
#             "User-Agent":
#                 "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
#         }
#
#         url = "http://www.baidu.com"
#         a = request.Request(url, headers=headers)
#         b = request.urlopen(a)
#         print(b.read())
#
#     8 ProxyHandler处理器（代理设置）
#         # http://httpbin.org/ 此网站可以方便查看http请求的一些参数
#         使用代理ip访问网页 如果ip被封，被封后用其他ip
#         from urllib import request
#
#         handler = request.ProxyHandler({"http": "183.245.98.6:8118"})
#         opener = request.build_opener(handler)
#
#         url = "http://httpbin.org/ip"  # 返回访问此网页客户端ip
#         a = request.Request(url)
#         b = opener.open(a)
#         print(b.read())
#
#
# cookie
#
#     请求是无状态的，第一次和服务器连接后并且登录后，第二次请求服务器依然不能知道
#     当前请求是哪个用户。cookie就是解决这个问题，第一次登录后服务器返回一些数据给
#     浏览器，然后浏览器保存在本地，当改用户发送第二次请求的时候，就会自动把上次请求
#     存储的cookie数据自动的携带给服务器，服务器通过浏览器携带的数据就能判断当前
#     是哪个用户。cookie存储数据邮箱，不同浏览器有不同的存储大小，一般不操作4KB
#
#
#     cookie的格式
#     Set-Cookie: NAME=VALUE;Expires/Max.age=DATE;Path=PATH;Domain=DOMAIN_NAME;SECURE
#
#         NAME     cookie名字
#         VALUE    cookie值
#         Expires/Max.age=DATE  cookie的过期时间
#         Path=PATH   cookie作用的路径
#         Domain=DOMAIN_NAME  cookie作用的域名
#         SECURE     是否在https协议下起作用
#
#     利用cookie爬取需要登录后才能浏览的信息1
#         直接使用cookie访问网页
#         from urllib import request
#         headers = {
#             "User-Agent":
#                 "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
#             "Cookie":
#                 "xxxxx"  # 获取方式 使用账号登录后查看cookie中信息
#         }
#         url = "http://www.baidu.com"
#         a = request.Request(url, headers=headers)
#         b = request.urlopen(a)
#         print(b.read())
#     利用cookie爬取需要登录后才能浏览的信息2
#         from urllib import request
#         from http.cookiejar import CookieJar
#         from urllib import parse
#
#         cookiejar = CookieJar()
#         handler = request.HTTPCookieProcessor(cookiejar)
#         opener = request.build_opener(handler) # 包含了登录所需要的cookie信息
#         headers={
#             "User-Agent":
#                 "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
#         }
#         data = {
#             '账户名':"xxx",
#             'password':"xxx"
#         }
#         req = request.Request(url="xx", data=parse.urlencode(data).encode('utf-8'), headers=headers)
#         opener.open(req)
#
#         r=opener.open('登录需要浏览的网址信息')
#
#     保存cookie到本地（包括过期的cookie信息）
#
#         from urllib import  request
#         from http.cookiejar import MozillaCookieJar
#
#         cookiejar = MozillaCookieJar("文件名")
#         # cookiejar.load(ignore_discard=True) # 加载过期的coookie信息
#         handler = request.HTTPCookieProcessor(cookiejar)
#         opener = request.build_opener(handler)
#
#         req = opener.open("网址")
#         cookiejar.save(ignore_discard=True) # ignore_discard=True保存过期的cookie信息
#
#
# requests库
#
#
#     1 安装
#         pip3 install requests
#
#     2 相关方法
#         import requests
#         reponse = requests.get("http://www.baidu.com")
#         print(reponse.content.decode('utf-8')) # 获取网络源代码
#         print(reponse.url)        # 获取访问网页的url
#         print(reponse.encoding)   #
#         print(reponse.status_code) # 获取响应状态码
#
#     3 发送get请求
#
#         import requests
#         kw = {"ww":'ccc'}
#         headers={
#                     "User-Agent":
#                         "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
#                 }
#
#         reponse = requests.get("http://www.baidu.com", params=kw, headers=headers)
#
#         # print(reponse.content.decode('utf-8'))
#
#     4 发送post请求
#
#         import requests
#
#         kw = {"ww":'ccc'}
#
#         headers={
#                     "User-Agent":
#                         "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
#                 }
#
#         reponse = requests.post("http://www.baidu.com", data=kw, headers=headers)
#
#         print(reponse.json())
#
#     5 使用代理：
#
#         import requests
#
#         kw = {"ww":'ccc'}
#
#         headers={
#                     "User-Agent":
#                         "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
#                 }
#         proxy = {
#             "http": "171.14.209.180:27829"
#         }
#
#         reponse = requests.get("http://www.baidu.com", headers=headers, proxies=proxy) #
#
#         print(reponse.json())
#
#     6 获取cookie
#         import requests
#
#         headers={
#                     "User-Agent":
#                         "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
#                 }
#
#
#         reponse = requests.get("http://www.baidu.com")
#
#         print(reponse.cookies)
#         print(reponse.cookies.get_dict())
#
#     7 session
#
#         import requests
#
#         headers={
#                     "User-Agent":
#                         "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
#                 }
#
#         data = {
#             "email":"账户",
#             'password': "密码"
#         }
#
#         session = requests.session()
#
#         session.post(url="xx", data=data, headers=headers)
#
#         reponse = session.get("登录后希望获取的页面网址")
#
#         print(reponse.content.decode('utf-8'))
#
#     8 处理不信任的SSL证书
#
#         import requests
#
#         headers={
#                     "User-Agent":
#                         "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
#                 }
#
#         req = requests.get('http://www.12306.cn/mormhweb/', headers=headers, verify=False)
#         print(req.content.decode('utf-8'))
#
#
# XPath
#
#     1 概念
#         是一门在XML和HTML文档中查找信息的语言，可用来在XML和HTML文档中对
#         元素和属性进行遍历
#
#     2 xpath开发工具
#         1 chrome插件XPath Helper
#         2 Firefox 插件 Try XPath
#     3 XPath语法
#         1 选取节点
#             /div   网页根节点查找div元素不查找子节点
#             //div  会查找子孙节点
#             //div[@id] 会查找所有div元素的id属性
#
#         2 谓语
#             //body/div[1]   获取body标签下的第一个div元素
#             //body/div[last()] 获取去body标签下的最后一个div元素
#             //body/div[position()<3]  获取body标签下的前两个div元素
#             //div[@id='a']  获取所有div元素属性id='a'的元素
#             //div[contains(@id, 'a')] 在所有div标签中查找id属性中包含a的标签（模糊匹配）
#
#         3 通配符
#             //body/*   在所有body标签下的子标签
#             //div[@*]  获取所有带属性的div标签
#
#         4 选取多个路径
#             //div/a  | //div/i  获取所有div下的子标签a和获取所有div下子标签i标签
#
#         5 运算符（基本上和python运算符一样）
#
#             //div[@class='a'] and @id='aa'  获取所有div标签class属性等于‘a’，id属性等于‘aa’的div标签
#
# lxml库
#
#     1 概念
#         lxml是一个HTML/XML的解析器，主要功能是如何解析和提取 HTML/XML数据
#
#     2 安装
#
#         pip3 install lxml
#
#     3 解析字符串
#         text = """
#             <ul class="nav-bd">
#             <li class="pipe">|</li>
#             <li><a href="https://qiang.taobao.com">淘抢购</a></li>
#             <li><a href="https://3c.tmall.com">电器城</a></li>
#             <li><a href="https://sf.taobao.com">司法拍卖</a></li>
#             <li><a href="https://good.tmall.com">淘宝心选</a></li>
#             <li><a href="https://www.taobao.com/markets/xt/znfp">兴农扶贫</a></li>
#             </ul>
#
#         """
#
#         from lxml import etree
#         html =etree.HTML(text)
#         result = etree.tostring(html, encoding='utf-8').decode('utf-8') # 是html内容规范化
#         print(result)
#
#     4 解析html文件
#
#         from lxml import etree
#
#         # html = etree.parse("test.html")
#
#         # 有的html网页标签不规范 使用默认的xml解析器会报错，需要指定html解析器
#         parser = etree.HTMLParser(encoding='utf-8') # html解析器
#         html = etree.parse("a.html", parser=parser)
#
#         result = etree.tostring(html, encoding='utf-8').decode('utf-8')
#         print(result)
#
#     5 xpath和lxml的结合
#         from lxml import etree
#         parser = etree.HTMLParser(encoding="utf-8")
#         html = etree.parse("a.html", parser=parser)
#
#         # 获取所有div标签
#         # div = html.xpath("//div")
#         # for i in div:
#         #     print(etree.tostring(i, encoding="utf-8").decode("utf-8"))
#
#         # 获取第二个div标签
#         # div_1 = html.xpath("//div[2]")[1]
#         # print(etree.tostring(div_1, encoding="utf-8").decode("utf-8"))
#
#         # 获取所有class等于even的div标签
#         # div_2 = html.xpath("//div[@class='s_form_wrapper']")
#         # print(div_2)
#         # for i in div_2:
#         #     print(print(etree.tostring(i, encoding="utf-8").decode("utf-8")))
#
#
#         # 获取所有a标签的href属性的值
#         # div_3 = html.xpath("//a/@href")
#         # for i in div_3:
#         #     print(i)
#
#
#         # 获取从第二div标签开始所有div标签下的a标签的下的文本值
#         # div_4 = html.xpath("//div[position()>1]")
#         # for i in div_4:
#         #     href = i.xpath(".//a/text()") # .表示当前标签下即 i标签下的a标签
#         #     for j in href:
#         #         print(j)
#
#
# BeautifulSoup4库
#     1 概念
#         和lxml一样，是一个HTML/XML的解析器，主要功能也是解析和提取 HTML/XML数据
#         lxml只会局部遍历，而BeautiSoup是基于HTML DOM的，会载入整个文档，性能要低于lxml
#         好处是 api好用
#         直接读取字符串，不能加载文件
#     2 安装
#
#         pip3 install bs4
#
#     3 BeautifulSoup的解析器
#         1 BeautifulSoup(text, "html.parser")  # 默认 python标准库中解析器（优点：速度适中容错率强）
#         2 BeautifulSoup(text, "lxml")  # lxml HTML解析器（优点：速度快容错率强，缺点：需要安装c语言库）
#         3 BeautifulSoup(text, ["lxml", "xml"])  # lxml XML解析器（优点：速度快唯一支持xml的解析器，缺点：需要安装c语言库）
#         4 BeautifulSoup(text, "html5lib")   # html5lib解析器（优点：容错率最强，以浏览器方式解析文档，生产html5格式文档，缺点：速度慢，不依赖外部扩展）
#             需要安装 pip3 install html5lib
#     3 使用
#         from bs4 import BeautifulSoup
#
#         soup = BeautifulSoup(text, "lxml")  # 第二个参数是解析器
#
#         # 获取所有div标签
#         # a1 = soup.find_all('div')
#         # for i in a1:
#         #     print(i)
#
#
#
#
#         # 获取第二个div标签
#         # a2 = soup.find_all('div', limit=2)  # limit 最多提取两个元素
#         # print(a2[1])
#
#
#
#         # 获取所有class='nav-items' 属性的标签1
#         # a3 = soup.find_all('div', class_='nav-items') # 为了和pyhon关键字class区分 参数用class_
#         # for i in a3:
#         #     print(a3)
#
#
#
#         # 获取所有class='nav-items' 属性的标签2
#         # a3 = soup.find_all('div', attrs={"class": 'nav-items'})
#         # for i in a3:
#         #     print(a3)
#
#
#         # 获取a标签的属性值1
#         # a4 = soup.find_all('a')
#         # for i in a4:
#         #     href = i['href']
#         #     print(href)
#
#
#         # 获取a标签的属性值2
#         # a4 = soup.find_all('a')
#         # for i in a4:
#         #     href = i.attrs['href']
#         #     print(href)
#
#
#         # 获取文本
#         # a5 = soup.find_all('a')
#         # for i in a5:
#         #     print(i.string)
#
#
#
#
#         # 获取标签下的所有文本(包括空白字符)
#         # a6 = soup.find_all('a')
#         # for i in a6:
#         #     print(list(i.strings))
#
#
#         # 获取标签下的所有文本(非空白字符)
#         # a6 = soup.find_all('a')
#         # for i in a6:
#         #     print(list(i.striped_strings))
#
#     4 方法
#         find  返回符合条件的第一个标签
#         find_all 返回符合条件的所有标签
#
#         string   获取某个标签下的非标签字符串（一层）如果标签下有多行字符，用.contents获取多行文本 返回的是字符串
#         strings  获取某个标签下的所有非标签字符串（所有层） 返回的是生成器
#         stripped_strings 获取某个标签下的所有非标签字符串（所有层）会去掉空白  返回是生成器
#         get_text 获取某个标签下的所有非标签字符串（所有层）返回不是列表形式 返回普通字符串
#
#     5 select方法
#
#         1 select方法（语法类似css选择器）查找元素
#
#         2 使用
#             from bs4 import BeautifulSoup
#
#             soup = BeautifulSoup(text, 'lxml')
#
#             # 查找所有a标签
#             # r = soup.select('a')
#             # for i in r:
#             #     print(i)
#
#
#
#             # 查找类名等于nav-items的标签
#             # r1 = soup.select('.nav-items')
#             # for i in r1:
#             #     print(i)
#
#
#
#             # 查找id=“aa”的标签
#             # r2 = soup.select('#aa')
#             # for i in r2:
#             #     print(i)
#
#
#             # 组合查找
#             # r3 = soup.select('s #bb')
#             # print(r3)
#
#
#             # 直接子标签查找
#             # r4 = soup.select('s1 > #bb')
#             # print(r4)
#
#
#             # 查找a标签href属性值为www.baidu.com的标签
#             # r5 = soup.select("a[href='www.baidu.com']")
#             # print(r5)
#
#
#             # 获取a标签下的内容
#             # r6 = soup.select("a")
#             # for i in r6:
#             #     print(i.get_text())
#
#             # 获取标签下的所有内容包括换行符
#             r6 = soup.select("a")
#             p = soup.find("p")
#             print(p.contents)
#
#     6 四个常用对象
#
#         1 Tag
#             BeautifulSoup继承了Tag
#             BeautifulSoup中所有标签都是Tag类型
#
#         2 NavigableString
#             字符串类型 继承了python的字符串类型
#         3 BeautifulSoup
#         4 Comment
#             继承NavigableString
#
#     7 遍历文档树contents和children
#         contents返回的是列表
#         children返回的是生成器
#
#         from bs4 import BeautifulSoup, NavigableString
#
#         soup = BeautifulSoup(text, 'lxml')
#
#         r = soup.select('div')
#         for i in r:
#             print(i.contents)
#             print(i.children)
#
# 正则表达式
#
#     按照一定的规则，从某个字符串中匹配出想要的数据
#
#     1 语法
#         # . 匹配不到换行符
#         # match 匹配到一个就马上返回 即使后面也有符合的正则
#
#         # 匹配某个字符串
#         # import re
#         # a = "text"
#         # ret = re.match("t", a)  # 从头匹配
#         # print(ret.group())
#         # >>> t
#
#
#
#         # 匹配任意字符
#         # a = "text"
#         # ret = re.match(".", a)
#         # print(ret.group())
#         # >>> t
#
#
#         # 匹配任意数字
#         # a = "12a"
#         # ret = re.match("\d", a)
#         # print(ret.group())
#         # >>> 1
#
#
#         # 匹配任意非数字
#         # a = "\n"
#         # ret = re.match("\D", a)
#         # print(ret.group())
#         # >>> a
#
#
#         # 匹配空白字符
#         # a = "\n"
#         # ret = re.match('\s', a)
#         # print(ret.group())
#         # >>>
#
#
#         # 匹配数字字母和下划线
#         # a = "_3f"
#         # ret = re.match("\w", a)
#         # print(ret.group())
#         # >>> _
#
#
#         # 匹配非数字字母和下划线
#         # a = "^4g"
#         # ret = re.match("\W", a)
#         # print(ret.group())
#         # >>> ^
#
#
#         # 组合匹配[], 只要满足中括号中内容就能匹配到
#         # a = "a1"
#         # ret = re.match("[5645a]", a)
#         # print(ret.group())
#         # >>> a
#
#
#         # 相同的匹配方式
#         # \d : [0-9]
#         # \D : [^0-9]
#         # \w : [0-9a-zA-Z_]
#         # \w : [^0-9a-zA-Z_]
#
#         # group分组提取数值
#         # a = "afdsaga23fdgdf45"
#         # b = re.match("[a-z]+(\d+)[a-z]+(\d+)", a)
#         # print(b.group(1))
#         # print(b.group(2))
#         # >>> 23
#         # >>> 45
#
# 读取csv文件
#
#     1 csv文件定义
#
#         1 纯文本
#         2 由记录组成（典型的是每行一条记录）
#         3 每台记录被分隔符分割为字段
#         4 每条记录都有同样的字段序列
#         5 可以用txt和表格打开
#
#     2 读取csv文件1
#         import csv
#
#         with open("aaa.csv", "r") as f:
#             read = csv.reader(f)
#             a = next(read) # >>>['      日期\t    开盘\t    最高\t    最低\t    收盘\t    成交量\t    成交额']
#             for i in read:
#                 print(i) # >>> ['2019/01/25\t3.75\t3.78\t3.74\t3.75\t4080697\t15329731.00']
#
#     3 读取csv文件2
#         import csv
#
#         with open("aaa.csv", "r") as f:
#             read = csv.DictReader(f)
#             for i in read:
#                 print(i['xx'])
#
#     4 写入数据到csv文件1
#
#         import csv
#
#         header = ['name', 'age', 'sextime']
#         values = [
#             ("lingling", 25, 24),
#             ("yingying", 23, 18),
#             ("dcxmy", 21, 12),
#         ]
#         with open("aaa.csv", 'w', newline='') as f:
#             w = csv.writer(f)
#             w.writerow(header)
#             w.writerows(values)
#
#     5 写入数据到csv文件2
#         import csv
#
#         header = ['name', 'age', 'sextime']
#         values = [
#             {"name":"lingling", "age":25 , "sextime":24},
#             {"name":"yingying", "age":23 , "sextime":18},
#             {"name":"dcxmy", "age":21, "sextime":12}
#
#         ]
#         with open("aaa.csv", 'w', newline='') as f:
#             w = csv.DictWriter(f, header)
#             w.writeheader()
#             w.writerows(values)
#
#
# 线程类
#
#     import threading
#
#     class A(threading.Thread):
#
#         def run(self):
#             # 做事情
#
#     class B(threading.Thread):
#
#         def run(self):
#             # 做事情
#
#     t1 = A()
#     t2 = B()
#     t1.start()
#     t2.start()
#
# Selenium和chromedriver（注意版本对应问题）
#
#     1 概念
#
#         selenium模拟人在浏览器上的行为动作
#         chromedriver是一个驱动chrome浏览器驱动程序（不同浏览器驱动程序不同）
#
#     2 安装
#
#         pip3 install selenium
#         下载chromedriver文件是exe结尾 放在能找到的非中文目录即可
#
#     3 使用
#
#         1 打开网页返回源代码
#             import os
#             from selenium import webdriver
#
#             dirver_path = os.getcwd()+"\\chromedriver.exe"
#
#             driver = webdriver.Chrome(executable_path=dirver_path)
#
#             driver.get('https://www.baidu.com') # 会打开一个浏览器
#
#             a = driver.page_source  # 返回打开网页的源代码
#             print(a)
#
#         2 关闭页面当前页面
#             driver.close()
#         3 关闭浏览器
#             driver.quit()
#
#         4 定位元素
#
#             获取一个元素方法
#                 find_element_xxxx
#             获取所有元素方法
#                 find_elements_xxxx
#
#             1 通过id查找元素
#                 # 根据id获取百度首页input框填充数据
#                 input_tag = driver.find_element_by_id('kw')
#                 input_tag.send_keys("玲玲")
#             2 通过类名查找元素
#                 # 根据类名获取百度首页input框填充数据
#                 input_tag = driver.find_element_by_class_name('s_ipt')
#                 input_tag.send_keys("yingyingfuck")
#
#             3 通过name属性值查找元素
#                 # 根据name属性获取百度首页input框填充数据
#                 input_tag = driver.find_element_by_name('wd')
#                 input_tag.send_keys("dcxmy")
#
#             4 通过标签名查找元素
#             5 根据xpath语法来获取元素
#                 # 根据xpath语法获取百度首页input框填充数据
#                 input_tag = driver.find_element_by_xpath('//input[@id="kw"]')
#                 input_tag.send_keys("cwxsb")
#             6 根据css选择器选择元素
#
#         5 操作表单元素
#
#             1 操作输入框
#                 1 找到输入框元素，向输入框内填充数据
#                 2 清空输入框内内容
#                 input_tag = driver.find_element_by_xpath('//input[@id="kw"]')
#                 input_tag.send_keys("cwxsb")
#                 input_tag.clear()
#             2 操作checkbox
#                 1 找到checkbox元素点击选取
#                 input_tag = driver.find_element_by_id("auto_login_in_five_days_pwd")
#                 input_tag.click()
#
#             3 操作select
#                 from selenium.webdriver.support.ui import Select
#
#                 select_tag = Select(driver.find_element_by_name("SerchType"))
#                 select_tag.select_by_index(1) # 根据索引选择
#                 select_tag.select_by_value("xx") # 根据值选择
#                 select_tag.select_by_visible_text("文本内容") # 根据可视的文本选择
#
#                 select_tag.deselect_all() # 取消选中所有选项
#
#             4 操作按钮
#
#                 input_tag = driver.find_element_by_name("xx")
#                 input_tag.click() # 点击
#
#
#         6 行为链
#
#             在页面执行多步操作，鼠标点点点
#             from selenium.webdriver.common.action_chains import ActionChains
#             input_tag = driver.find_element_by_name("xx")
#             sub_tag = driver.find_element_by_name("xxxx")
#
#             actions = ActionChains(driver)
#             actions.move_to_element(input_tag) # 移动鼠标到input框
#             actions.send_keys_to_element(input_tag, "aaa") # 向input框输入信息
#             actions.move_to_element(sub_tag) # 移动鼠标到sub_tag标签
#             actions.click(sub_tag) # 点击标签
#             actions.perform() # 执行上面的操作
#
#             其他方法
#                 actions.click_and_hold(element) # 鼠标点击单不松开鼠标
#                 actions.context_click(elemetn) # 邮件点击
#                 actions.double_click(element)  # 双击
#
#         7 cookie操作
#
#             1 获取所有的cookie
#
#                 for cookie in driver.get_cookie():
#                     print(cookie)
#             2 根据cookie的key获取value
#                 value = driver.get_cookie("xx")
#
#             3 删除所有cookie
#                 driver.delete_all_cookies()
#
#             4 删除某个cookie
#                 driver.delete_cookie("xx")
#
#         8 页面等待
#
#             由于ajax技术，不能确定何时某个元素完全加载出来，
#                 解决方式等待，一种隐式等待，一种显示等待
#
#             1 隐式等待（获取不可用的元素之前，会先等待10秒）
#                 driver.implicitly_wait(10)
#                 driver.get('https://www.sina.com.cn/') # 会打开一个浏览器
#
#             2 显示等待（等待10秒 如果10秒内获取到了元素就不再等待）
#
#                 from selenium.webdriver.support.ui import WebDriverWait
#                 from selenium.webdriver.support import expected_conditions as EC
#                 from selenium.webdriver.common.by import By
#
#                 try:
#                     element = WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.ID, "xx"))
#                     )
#                 finally:
#                     driver.quit()
#
#         9 切换页面
#
#             打开一个新的页面
#                 driver.execute_script("window.open('新页面网址')")
#
#             切换页面
#
#                 driver.switch_to.window(driver.window_handles[1]) # 切换到第二个窗口
#
#
#         10 设置代理ip
#
#             from selenium import webdriver
#             options = webdriver.ChromeOptions()
#             options.add_argument("--proxy-server=http://代理ip地址:端口")
#             driver_path = r'xxxxx\chromedriver.exe'
#             driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
#             driver.get("xxx")
#
#         11 webElement元素
#
#             从网页中获取元素的类型就是webElement类型
#             sub = driver.find_element_by_name("xx")
#             sub.get_attribute("value") # 获取元素的属性值
#
#             截图
#
#                 driver.save_screenshot('保存的文件名') # 网页截图
#
#
# Tesseract库
#
#     图形验证码识别技术
#
#     1 安装（为了终端下使用）
#
#         1 windows
#             https://github.com/tesseract-ocr/
#             需路径添加到环境变量中
#         2 linux
#             sudo apt install tesseract-ocr
#
#     2 安装（为了代码下使用）
#
#         1 pip3 install pytesseract
#
#     3 使用
#
#         1 终端下使用，找到识别图片所在位置
#
#             执行命令
#                 tesseract 图片名 存储的文件名
#
#         2 代码下使用
#
#             import pytesseract
#             from PIL import Image
#
#             # 指定执行文件所在路径
#             pytesseract.pytesseract.tesseract_cmd = r'D:\softstatic\tesseract_orc\tesseract.exe'
#
#             image = Image.open("aaa.png")
#             text = pytesseract.image_to_string(image) # 如果向识别中文参数中(image, lang='chi_sim')
#             print(text)
#
#
# Scrapy框架(需要继续学习)
#
#     1 安装
#
#         pip3 install scrapy
#
#         windows推荐照着文档安装
#     	@@@@@@@@@安装完毕？测试是否成功
#
#     2 使用
#
#         1 创建项目
#
#             scrapy startproject 项目名
#
#         2 默认生产的项目结构
#
#             scrapy.cfg # 默认配置文件
#             items.py # 定义模型的文件
#             middlewares.py # 中间键
#             pipelines.py # 处理爬下来的数据
#             settings.py # 处理爬虫设置文件
#
#         3 创建一个爬虫
#
#             scrapy genspider 爬虫名 "网站名"
#             # 在项目的spiders中会生成 爬虫名.py文件
#
#         4 设置setting.py
#
#             1 取消遵守机器人协议
#
#                 ROBOTSTXT_OBEY = False # 遵守机器人协议
#
#             2 设置请求头
#                 添加"User-Agent"项
#                 DEFAULT_REQUEST_HEADERS = {
#                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#                   'Accept-Language': 'en',
#                   'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
#                 }
#         5 运行爬虫
#
#             scrapy crawl 爬虫名
#
#         6 爬虫文件的编写
#
#             # -*- coding: utf-8 -*-
#             import scrapy
#
#
#             class QsbkSpider(scrapy.Spider):
#                 name = 'qsbk'   # 爬虫名字
#                 allowed_domains = ['https://www.qiushibaike.com/'] # 允许域名
#                 start_urls = ['https://www.qiushibaike.com/8hr/page/1/'] # 开始url
#
#                 def parse(self, response): # 解析函数
#                     print(response)
#
#         7 CrawlSpider
#
#
#
#
#
# ===============================================