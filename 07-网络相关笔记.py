#
# 说明：
#     包含网络相关信息
#     1 HTTP --> 搜索httphttp
#     2 再浏览器输入地址后的流程 --> 搜索 再浏览器输入地址后的流程
#     3 URL --> 搜索 URLURL
#     4 Web --> 搜索 WebWeb
#     5 WSGI --> 搜索 WSGIWSGI
#     6 cookie --> 搜索 cookiescookies
#     7 session --> 搜索 sessionsession
#
#
# ==============================================
# sessionsession
1
# Session
#     cookie本身最大支持4096字节,Cookie本身保存在客户端，
#     可能被拦截或窃取
#
#     Session支持更多的字节，并且他保存在服务器，
#     有较高的安全性。这就是Session。
#
#     Cookie就起到桥接的作用。
#
#     我们可以给每个客户端的Cookie分配一个唯一的id，
#     这样用户在访问时，通过Cookie，服务器就知道来的
#     人是“谁”。然后我们再根据不同的Cookie的id，
#     在服务器上保存一段时间的私密资料，如“账号密码”等等。
#
#     总结而言：Cookie弥补了HTTP无状态的不足，
#     让服务器知道来的人是“谁”；但是Cookie以文本的
#     形式保存在本地，自身安全性较差；所以我们就通
#     过Cookie识别不同的用户，对应的在Session里保存
#     私密的信息以及超过4096字节的文本。
1
# ==============================================
#
#
#
#
# ==============================================
# cookiescookies
1
#     状态可以理解为客户端和服务器在某次会话中产生的数据，
#     那无状态的就以为这些数据不会被保留。会话中产生的数
#     又是我们需要保存的，也就是说要“保持状态”。
#     因此Cookie就是在这样一个场景下诞生。
#
#
#
#     Cookie具体指的是一段小信息，它是服务器发送出来存
#     储在浏览器上的一组组键值对，下次访问服务器时浏览器
#     会自动携带这些键值对，以便服务器提取有用信息。
#
#
#
#     cookie的工作原理是：由服务器产生内容，浏览器收到
#     请求后保存在本地；当浏览器再次访问时，浏览器会自动
#     带上Cookie，这样服务器就能通过Cookie的内容来判断
#     个是“谁”了。
1
# ==============================================
#
#
#
#
#
# ==============================================
# WSGIWSGI
1
#     一种规范,定义了使用python编写的web应用程序与web服务器程序
#     之间的接口格式,实现web应用程序与web服务器程序间的解耦
#
#     常见的WSGI服务器
#         uwsgi, Gunicorn
#
#     python标准库提供哦你的独立WSGI服务器wsgiref
#     django开发环境用的就是wsgiref
#
# 利用wsgiref写web框架的 socket server
#
#     import socket
#
#     from wsgiref.simple_server import make_server
#
#     def home(url):
#         s1 = "这是home页面".encode('utf-8')
#         return s1
#
#
#     def index(url):
#         f = open("index.html","r")
#         s = f.read()
#         f.close()
#         return s.encode("utf-8")
#
#     # url和实际要执行的函数的对应关系
#     list1 = [("/index/", index), ("/home/", home)]
#
#
#     def run_server(environ, start_response):
#
#         # 设置HTTP响应的状态码和头信息
#         start_response('200 ok',[("Content-Type","text/html;charset=utf8")])
#
#         url = environ['PATH_INFO'] # 获取用户输入的url
#
#         print(environ)
#         print(start_response)
#         func=None
#         for i in list1:
#             if i[0] == url:
#                 func = i[1]
#                 break
#         if func:
#             s = func(url)
#         else:
#             s =b'fuck off'
#
#         return [s,]
#
#     if __name__ == '__main__':
#         httpd = make_server("127.0.0.1", 10000, run_server)
#
#         print("111111111111111")
#         httpd.serve_forever()
1
# ==============================================
#
#
#
# =================================================
# WebWeb
1
# Web框架本质
#     Web应用本质上就是一个socket服务端，
#     而用户的浏览器就是一个socket客户端
#
# web服务端 添加响应状态
#     import socket
#     sk = socket.socket()
#     sk.bind(("127.0.0.1", 10001))
#     sk.listen()
#
#     try:
#         while True:
#             conn, addr = sk.accept()
#             data = conn.recv(8096)
#             print("hahahahah")
#             print(data)  # 将浏览器发来的消息打印出来
#             conn.send(b"HTTP/1.1 200 ok\r\n\r\n")
#             conn.send(b"OK")
#             conn.close()
#     finally:
#         sk.close()
#
#     客户端
#     从浏览器连接127.0.0.1:10001
#     浏览器收到 ok
#
#     服务器收到消息
#     s1 = b'GET / HTTP/1.1\r\nHost: 127.0.0.1:10001\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'
#     s2 = b'GET /favicon.ico HTTP/1.1\r\nHost: 127.0.0.1:10001\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36\r\nAccept: image/webp,image/apng,image/*,*/*;q=0.8\r\nReferer: http://127.0.0.1:10001/\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'
#     print(s1.decode("utf-8"))
#     print(s2.decode("utf-8"))
#
#     # s1
#     GET / HTTP/1.1
#     Host: 127.0.0.1:10001
#     Connection: keep-alive
#     Upgrade-Insecure-Requests: 1
#     User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36
#     Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
#     Accept-Encoding: gzip, deflate, br
#     Accept-Language: zh-CN,zh;q=0.9
#
#     # s2
#     GET /favicon.ico HTTP/1.1
#     Host: 127.0.0.1:10001
#     Connection: keep-alive
#     User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36
#     Accept: image/webp,image/apng,image/*,*/*;q=0.8
#     Referer: http://127.0.0.1:10001/
#     Accept-Encoding: gzip, deflate, br
#     Accept-Language: zh-CN,zh;q=0.9
#
# web服务器根据不同路径返回不同内容
#     import socket
#
#     sk = socket.socket()
#     sk.bind(("127.0.0.1", 10019))
#     sk.listen()
#
#     def hander_recv_byte(by):
#         s = by.decode("utf-8")
#         s1 = s.split("\r\n")[0]
#         # print(s1)  # GET / HTTP/1.1
#         url = s1.split()[1]
#         # print(url) # /
#         return url
#
#     def home(url):
#         # s = "这是home页面"
#         # return s.encode('utf-8')
#         s = "这是{}页面".format(url)
#         return bytes(s,encoding="utf-8")
#
#     def index(url):
#         s = "这是{}页面".format(url)
#         return bytes(s,encoding="utf-8")
#
#     # url和实际要执行的函数的对应关系
#     list1 = [("/index/", index), ("/home/", home)]
#
#
#     while True:
#         conn, addr = sk.accept()
#         data = conn.recv(8096)
#         if data:
#             url = hander_recv_byte(data)
#             # 因为要遵循HTTP协议，所以回复的消息也要加状态行 最后一个要家\r\n\r\n
#             conn.send(b"HTTP/1.1 200 ok\r\ncontent-type:text/html;charset=utf-8\r\n\r\n")
#
#             # func=None
#             for i in list1:
#                 if i[0] == url:
#                     func = i[1]
#                     break
#             if func:
#                 s = func(url)
#             else:
#                 s =b'fuck off'
#
#             conn.send(s)
#         conn.close()
#
#     sk.close()
#
# web服务器返回给客户端HTML文件
#     import socket
#
#     sk = socket.socket()
#     sk.bind(("127.0.0.1", 10012))
#     sk.listen()
#
#     def hander_recv_byte(by):
#         s = by.decode("utf-8")
#         s1 = s.split("\r\n")[0]
#         # print(s1)  # GET / HTTP/1.1
#         url = s1.split()[1]
#         # print(url) # /
#         return url
#
#     def home(url):
#         s1 = "这是home页面".encode('utf-8')
#         return s1
#
#
#     def index(url):
#         f = open("index.html","r")
#         s = f.read()
#         f.close()
#         return s.encode("utf-8")
#     # url和实际要执行的函数的对应关系
#     list1 = [("/index/", index), ("/home/", home)]
#
#
#     while True:
#         conn, addr = sk.accept()
#         data = conn.recv(8096)
#         if data:
#             url = hander_recv_byte(data)
#             # 因为要遵循HTTP协议，所以回复的消息也要加状态行
#             conn.send(b"HTTP/1.1 200 ok\r\ncontent-Type:text/html;charset=utf-8\r\n\r\n")
#
#             func=None
#             for i in list1:
#                 if i[0] == url:
#                     func = i[1]
#                     break
#             if func:
#                 s = func(url)
#             else:
#                 s =b'fuck off'
#
#             conn.send(s)
#         conn.close()
#
#     sk.close()
#
# web总结
# 	1 web框架的本质:
# 		socket服务端 与 浏览器通信
# 	2 socket服务端功能划分
# 		a.负责与浏览器收发消息 	wsgiref/uWsgi/gunicorn
# 		b.根据用户访问的不同的路径执行不同的函数
# 		c.从html读取的内容,并且完成字符串的替换  jinja2
# 	3 python中的web框架的分类:
#
# 		1 框架自带a,b,c  --->tornado
# 		2 框架自带b和c,使用第三方模块的a  --> django
# 		3 框架自带b,使用第三方的a和c --flask
1
# =================================================





# =================================================
# URLURL
1
# 超文本传输协议（HTTP）的统一资源定位符将从因特网获取信息的五个基本元素包括在一个简单的地址中：
#
# 	传送协议。
#
# 	层级URL标记符号(为[//],固定不变)
#
# 	访问资源需要的凭证信息（可省略）
#
# 	服务器。（通常为域名，有时为IP地址）
#
# 	端口号。（以数字方式表示，若为HTTP的默认值
# 			“:80”可省略）
#
# 	路径。（以“/”字符区别路径中的每一个目录名称）
#
# 	查询。（GET模式的窗体参数，以“?”字符为起点，
# 			每个参数以“&”隔开，再以“=”分开参数名称
# 			与数据，通常以UTF8的URL编码，
# 			避开字符冲突的问题）
#
# 	片段。以“#”字符为起点
#
# 	例子
#
# 		http://www.luffycity.com:80/news/index.html?id=250&page=1
# 			http，是协议；
# 			www.luffycity.com，是服务器；
# 			80，是服务器上的网络端口号；
# 			/news/index.html，是路径；
# 			?id=250&page=1，是查询。
1
# =================================================
#
#
#
#
#
#
# ==============================================
# 再浏览器输入地址后的流程
1
#     在浏览器地址栏键入URL，按下回车之后会经历以下流程:
#         1 浏览器向 DNS 服务器请求解析该 URL 中的域名所
#         对应的 IP 地址;
#
#         2 解析出 IP 地址后，根据该 IP 地址和默认端口 80，
#         和服务器建立TCP连接;
#
#         3 浏览器发出读取文件(URL 中域名后面部分对应的文件)的
#         HTTP 请求，该请求报文作为 TCP 三次握手的第三个报文的
#         数据发送给服务器;
#
#         4 服务器对浏览器请求作出响应，并把对应的 html
#         文本发送给浏览器;
#
#         5 释放 TCP连接;
#
#         6 浏览器将该 html 文本并显示内容; 　
1
# ==============================================




# ==============================================
# HTTPhttp
1
# http网络状态码（STATUS）
#     作用
#         能够反映出当前交互的结果及原因
#
#     200 ok 成功 只能证明服务器返回信息了，但是信息不一定是你业务需要的
#
#     301 永久转移（永久重定向）域名更改，访问原始域名重定向到新的域名
#
#     302 临时转移（临时重定向=》307）网站是居于HTTPS协议运作的，如果访问
#         的是HTTP协议，会基于307重定向到HTTPS协议上，302一般用于服务器负载
#         均衡，当一台服务器达到最大并发数的时候，会把后续访问的用户临时转移
#         到其他的服务器机组上处理，偶尔真是项目中会把所有的图片放到单独的
#         服务器上“图片处理服务器”，减少主服务器的压力
#
#     304 设置缓存
#         对于不经常更新的资源文件，css/js/html/img等 服务器结合客户端设置
#         304缓存，第一次加载这些资源就缓存到客户端了，下载在获取，从缓存
#         获取。
#
#     400 Bad Request 请求参数错误
#
#     402 Unauthorized 无权限访问
#
#     404 Not Found 找不到资源（地址不存在）
#
#     413 Request Entity Too Large 和服务器交互的内容资源超过服务器最大限制
#
#     500 Internal Server Error  未知服务器错误
#
#     503 Service Unavailable 服务器超负荷
#
#     总结
#         # 状态代码的第一个数字代表当前响应的类型：
#
#         # 	1xx消息——请求已被服务器接收，继续处理
#
#         # 	2xx成功——请求已成功被服务器接收、理解、并接受
#
#         # 	3xx重定向——需要后续操作才能完成这一请求
#
#         # 	4xx请求错误——请求含有词法错误或者无法被执行
#
#         # 	5xx服务器错误——服务器在处理某个正确请求时发生错误
#
# HTTP工作原理
#
#     HTTP 请求/响应的步骤
#
#     默认端口	HTTP:80
#             HTTPS:443
#
#     1. 客户端连接到Web服务器
#
#     2. 发送HTTP请求
#     客户端向Web服务器发送一个文本的请求报文，
#     一个请求报文由请求行、请求头部、空行和请求数据4部分组成。
#
#     3. 服务器接受请求并返回HTTP响应
#
#     4. 释放连接TCP连接
#     若connection 模式为close，则服务器主动关闭TCP连接，
#     客户端被动关闭连接，释放TCP连接;
#     若connection 模式为keepalive，则该连接会保持一段时间，
#     在该时间内可以继续接收请求;
#
#     5. 客户端浏览器解析HTML内容
#     客户端浏览器首先解析状态行，查看表明请求是否成功的状态代码。
#     然后解析每一个响应头，响应头告知以下为若干字节的HTML文档
#     和文档的字符集。客户端浏览器读取响应数据HTML，
#     根据HTML的语法对其进行格式化，并在浏览器窗口中显示。
#
# HTTP请求方法
#     HTTP/1.1协议中共定义了八种方法
#
#     1 GET
#         向指定的资源发出“显示”请求
#
#     2 HEAD
#         与GET方法一样，都是向服务器发出指定资源的请求。
#         只不过服务器将不传回资源的本文部分。
#         获取其中“关于该资源的信息”(元信息或称元数据)
#
#     3 POST
#         向指定资源提交数据，请求服务器进行处理
#
#     4 PUT
#         向指定资源位置上传其最新内容。
#
#     5 DELETE
#         请求服务器删除Request-URI所标识的资源。
#
#     6 TRACE
#         回显服务器收到的请求，主要用于测试或诊断
#
#     7 OPTIONS
#         这个方法可使服务器传回该资源所支持的
#         所有HTTP请求方法。用'*'来代替资源名称，
#         向Web服务器发送OPTIONS请求，
#         可以测试服务器功能是否正常运作。
#
#     8 CONNECT
#         HTTP/1.1协议中预留给能够将连接改为管道方式的
#         代理服务器。通常用于SSL加密服务器的链接
#         （经由非加密的HTTP代理服务器）
#
#
#     注意事项：
#
#     方法名称是区分大小写的。
#
#     当某个请求所针对的资源不支持对应的请求方法的时候，
#     服务器应当返回状态码405（Method Not Allowed），
#
#     当服务器不认识或者不支持对应的请求方法的时候，
#     应当返回状态码501（Not Implemented）。
#
#     HTTP服务器至少应该实现GET和HEAD方法，
#     其他方法都是可选的。当然，所有的方法支持的实现都应
#     当匹配下述的方法各自的语义定义。此外，除了上述方法，
#     特定的HTTP服务器还能够扩展自定义的方法。
#     例如PATCH（由 RFC 5789 指定的方法）
#     用于将局部修改应用到资源。
#
# HTTP请求格式
#
# 	请求方法 空格 URL 空格 协议版本 回车符 换行符   请求行
#
# 	头部字段名:值 回车符 换行符
# 	.....						请求头部
# 	头部字段名:值 回车符 换行符  \r\n
# 	回车符 换行符 \r\n
# 	.................			请求数据
#
# HTTP响应格式
#
# 	协议版本 空格 状态吗 空格 状态码描述 回车符 换行符 	状态行
#
# 	头部字段名:值 回车符 换行符
# 	.....						响应头部
# 	头部字段名:值 回车符 换行符
# 	回车符 换行符
# 	.................			响应数据
#
#  http请求方式
#     GET:从服务器获取数据
#     POST:向服务器推送数据
#     DELETE:删除服务器端的某些内容
#     PUT：向服务器上存放一些内容
#     HEAD:只想获取服务器返回的响应头信息，不要相应主体内容
#     OPTIONS:一般使用向服务器发送探测性请求，如果服务器反水
#         请求，说明当前客户端和服务器端建立了链接，就可以继续其他请求了
#         （TRACE是干这件事的，但是axios这个AJAX类库在基于
#         cross domain进行跨域请求的时候，就是先发送options请求进行
#         探测尝试，如果能连同服务器，才会继续发送其他请求）
#
# GET 和 POST区别
#
#     1 传递给服务器信息的方式不一样
#         GET
#             1 是基于URL地址“问号传参”的方式吧信息传递给服务器，
#                 传递参数 xhr.open('get', '/ss/kk?xxx=xxx&xxxx=xxxx')
#
#         POST
#             1 是基于“请求主体”把信息传递给服务器
#                 传递参数 xhr.send('xxx=xxx&xxxx=xxxx')
#
# 为什么传递方式不一样
#
#     1
#         浏览器对于url的长度有最大限度 post提交东西多 ，get少
#     2
#         GET 不安全
#             容易被URL劫持
#         POST相对安全
#     3
#         get会产生不可控制的缓存
#             产生原因：
#                 连续向多个相同的地址，并且传递的
#                 参数信息也是相同的，浏览器会吧之前获取的数据
#                 从缓存中拿到返回，导致无法获取服务器最新的数据
#
#             如何不产生缓存
#                 xhr.open('get', '/ss/sss?name=1000&_=${Math.random()}')
#                     可以保证每次请求的地址不完全一致
#
#         post不会产生不可控制的缓存
1
# ==============================================

=========================================
web项目开发流程（分离）

	1 项目立项
	2 需求分析 （项目的需求）
	3 原型设计  （产品原型图）
	
	4_1_1 架构设计 （后端人员，模块划分，功能能架构，开发环境选择，其他技术，部署架构）
	4_1_1_1 数据库设计（分析数据表和字段，表关系）
	4_1_1_2 模块代码的实现和单元测试 （分工，实现代码）	


	4_1_2 UI设计	（前段人员）
	4_1_2_1 前端设计

	5 代码整合 （后端代码和前端代码进行整合）
	6 集成测试 （代码整合之后进行测试）
	7 网站发布（项目上线）
