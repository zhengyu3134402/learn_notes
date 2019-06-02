# 说明
    # 此文档包含python3先关信息
    # 1 python3 --> 搜索python3python3
    1
        # 1安装
            # 1 windows安装说明
        # 2 标准库

            # 1 hashlib
                # 1 使用hashlib库进行md5加密
                # 2 小校验文件的一致性（原理 对文件进行读取 进行加密 对加密后的文件进行比较）
                # 3 超大文件一致性校验（对同一个字符串分段进行加密，最后得到结果跟一次性进行加密的结果一样）
            # 2 python3模块导入出现no model name 'xx'
            # 3 日期的加减datetime

            # 6 对象类型转换成json
            # 7 新版线程池的创建
            # 8 进程池的创建
                # 1 同步调用apply
                # 2 异步调用apply_async
                # 3 异步调用+回调函数(注意顺序会乱)
            # 9 二分法操作已经排序的序列bisect
                # 1 把变量插入序列 序列保持升序
            # 10 数组(只存放数字列表的时候,推荐使用数组替代列表)
                # 1 创建浮点型数组 类型为 ‘d’
                # 2 将数组写入文件
                # 3 从文件读取数组
                # 4 数组的排序
            # 11 双向队列（比列表对于头部操作更快）
                # 1 创建双向队列
                # 2 旋转操作
                # 3 向头部添加元素
                # 4 合并列表
                # 5 头部倒叙插入列表
            # 12 根据元祖的某个元素给元祖列表排序itemgetter
                # 1 多个参数传给itemgetter，她的构建的函数会返回提取的值构成元祖
            # 13 标准库中的装饰器
            # 14 LIFO
                # 栈
            # 15 FIFO
                # 使用队列应用（queue.Queue qsize put get）
                # 队列
            # 16 sys
                # 1 模块搜索路径列表sys.path
                # 2 获取计算机最大整型范围（sys.maxsize）
                # 3 获取python解释器版本信息（sys.version）
                # 4 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值（sys.path）
                # 5 显示当前环境加载了哪些模块(sys.modules)
                # 6 返回操作系统平台名称(sys.platform)
                # 7 获取文件名和获取文件执行时候添加的参数(sys.argv)
                # 8 退出程序（sys.exit(0)正常退出， 错误退出sys.exit(1)）
                # 9 查看对象引用次数sys.getrefcount(x)
                # 10 可执行程序内置模块名称sys.builtin_module_names
                # 11 异常的详细信息sys.exc_info[0],sys.exc_info[1]
            # 17 Counter
                # 1 统计列表中重复出现元素的次数
                # 2 根据元素出现的次数降序排列元素和出现次数
                # 3 计数器的相加(也支持+-&|运算)
            # 18 json
                # 1 将数据转换成json格式json.dumps
                # 2 读取json格式数据
                # 3 json对字典进行dumps
                # 4 json对列表进行dumps
                # 5 json对字符串进行dumps
                # 6 json对元祖进行dumps
                # 7 json对True, False进行dumps
                # 8 json对False进行dumps
                # 9 json对中文进行处理ensure_ascii=False
                # 10 用json向文件中写入中文
                # 11 多次dump数据到文件里，不能能用load读出来，若读不出来有什么办法(dumps write\n loads)
            # 19 os
                # 1 获取执行当前文件所在目录绝对路径（os.getcwd）
                # 2 改变当前文件的工作目录(os.chdir)
                # 3 创建多级目录（os.makedirs('xx', exist_ok=True)若目录存在则不创建）
                # 4 创建单级目录（os.mkdir）
                # 5 删除目录或文件 （os.rmdir 目录不为空不能删除）
                # 6 删除文件（os.remove）
                # 7 查看文件信息(os.stat)
                # 8 查看当前系统的目录分隔符(os.sep)
                # 9 查看当前系统使用的行终止符文（os.linesep）
                # 10 重命名文件目录(os.rename)
                # 11 查看用于分割文件的字符串(os,pathsep)
                # 12 查看到那个前使用平台(os.name)
                # 13 查看环境变量(os.environ)
                # 14 获取终端窗口大小os.get_terminal_size()
                # 15 获取 os,sys属性个数dir(sys),dir(os),dir(os.path)
                # 16 负责程序间通信os.pipe()
            # 20 time
                # 1 时间戳转换成字符串时间time
                # 2 字符串时间转换成时间戳time
                # 3 获取当前时间戳 格林威治时间（time.time）
                # 4 获取当前结构化时间(time.localtime())
            # 21 logger日志模块
                # 1 分别对日志的分级进行应用
                # 2 日志的对象配置型应用
            # 22 执行系统命令返回输入命令的结果(os.popen() .read())
            # 23 数据结构堆
            # 24 不改变原序列，进行合并排序（序列必须是排过序的）heapq.merge()
            # 25 pickle模块
            # 26 shelves模块
            # 27 struct模块
                # 1 struct模块进行打包(把一个数字打包成一个4字节的bytes)
                # 2 使用sturct模块进行解包
            # 28 subprocess模块
                # 1 使用subprocess模块在python代码中调用操作系统的命令

        # 3 数据类型

            # 1 字典
                # 1 获取字典中最大最，最小值的键
                # 2 字典的构造方法
                # 3 字典的其他种类
                    # 1 collections.OrderedDict
                    # 2 collection.ChainMap
                    # 3 collection.Counter
                    # 4 collections.UserDict
                    # 5 MappingProxyType
                # 4 字典获取值的原理
                # 5 为什么字典是无序的？
                # 6 删除字典中的元素（pop del）
            # 2 列表

                # 1 获取一个列表元素的多种组合
                # 2 获取多个列表的多种组合(元素个数不同也可以)
                # 3 切片
                    # 1 切片的命名
                    # 2 切片的赋值
                # 4 对序列使用 + 和 *
                # 5 *生成同一个对象
                # 6 避免*生成同一个对象
                # 7 列表的浅复制
                # 8 序列的比较大小

            # 3 推导式

                # 1 小数列表推导式
                # 2 列表推导式（组合出不同的元素）
                # 3 生成器表达式
                # 4 字典推导

            # 4 字符串

                # 1 将字符串转换成decimal类型
                # 2 字符串
                # 3 格式化%
                # 4 格式化.format()
                # 5 ascii的比较

            # 5 元祖

                # 1 拆包做参数
                # 2 元祖的排序
                # 3 嵌套元祖拆包
                # 4 具名元祖

            # 6 可散列数据类型
                # 1 可散列的对象必须满的条件
            # 7 类型比较
                # 1 python里的dict和set的效率有多高？
                # 2 为什么dict的键和set元素的顺序是跟据它们被添加的次序而定的，以及为什么在映射对象的生命周期中，这个顺序并不是一成不变的？
                # 3 为什么不应该在迭代循环dict或是set的同时往里添加元素？
                # 4 set和frozenset
            # 8 文本和字节序列
                # 1 文本和字节序列
                # 2 避免和处理编码错误
            # 9 字节和数组
                # 1 bytes、bytearray等二进制序列的独特特性
                # 2 字节和字节数组
            # 10 函数
                # 1 函数
                # 2 强制必须传入实参
                # 3 提取关于函数参数的信息
                # 4 函数注解
                # 5 函数的装饰器
                # 6 变量作用域规则
                # 7 闭包的定义和作用
                # 8 nonlocal
                # 9 叠放装饰器
                # 10 参数化装饰器
                # 11 让函数实参变成可选
                # 12 匿名函数lambda
            # 11 集合
                # 1 计算两个属性集合差
                # 2 将字典传入set()函数
                # 3 向集合中添加元素(add)
                # 4 随机弹出集合中的元素（pop）
                # 5 修改集合中的元素(remove, add)
                # 6 查询集合元素(in)
                # 7 求集合的交集(&)
                # 8 求集合的并集（|）
                # 9 求集合的差集（-）
                # 10 求集合的反交集（^）
            # 12 数字类型
                # 1 int型变量
                # 2 有符号int和无符号int的区别

            # 13 运算
                # 1 运算顺序
                # 2 字符串运算
            # 14 错误
                # 1 错误类型
            # 15 bool类型
                # 2 python中False的类型元素
            # 16 对象
                # 1 创建对象，执行对象方法的执行过程
                # 2 记录多少个类A的对象被创建
                # 3 创建对象把方法变成伪属性（property）并调用
                # 4 对伪属性进行修改@property
                # 5 对伪属性进行删除
            # 17 类
                # 1 鸭子类型
                # 2 类的静态方法(@staticmethod)
                # 3 创建类方法并通过类调用通过对象调用（@classmethod）
                # 4 定义借口或抽象基类(abc模块metaclass=ABCMeta,abstractmethod)
                # 5 类()做的事情
                # 6 类名空间的查询顺序
            # 18 float类型
                # 1 float和double的区别

        # 4 内置函数

            # 1 map函数的使用
            # 2 split字符串分割
            # 3 获取商和余数的函数divmod
            # 4 list.sort 和 sorted
            # 5 用setdefault处理找不到的键
            # 6 is 和 == 区别
            # 7 内置的iter
            # 8 int方法int()
            # 9 实参的计算
            # 10 函数中的变量和形参都是局部的
            # 11 泛化
            # 12 重构
            # 13 合并字典
            # 14 zip()
            # 15 help()
            # 16 去除字符串两端内容strip
            # 17 字符串左对齐右对齐剧中(ljust rjust center)
            # 18 拼接成字符串（join）,print拼接字符串
            # 19 字符串首字母转为大写(capitalize)
            # 20 字符串全部转换为小写lower
            # 21 字符串全部换为大写upper
            # 22 字符串大小写互相转换swapcase
            # 23 字符串"a"在序列中出现的次数(count)
            # 24 判断该字符串是否由字母或数字组成isalnum
            # 25 判断字符串只有字母组成isalpha
            # 26 判断字符串只有正整数组成isdigit
            # 27 将字符串转化成bytes类型（bytes）
            # 28 字符串创建新字节数组(bytearry)
            # 29 字符串类型代码的执行（eval,返回结果）简单类型
            # 30 复杂类型(exec,不返回结果)(执行eval或exec之前可对字符串语句进行编译)
            # 31 被特殊字符串隔开的英文首字母大写(title)
            # 32 对浮点数,整数进行四舍五入（round）
            # 33 把十进制分别转换为2进制，8进制，16进制(bin, oct hex)
            # 34 生成随机整数（random.randint(start,stop)）
            # 35 整数在内存中占用的二进制码的长度（bit_length）
            # 36 使用 range() 创建数字列表
            # 37 随机抽取一个元素(random.choine)
            # 38 随机抽取多个元素(random.sample)
            # 39 打乱列表的顺序(random.shuffle)
            # 40 对列表进行翻转(reversed)不改变原列表
            # 41 对列表进行翻转(reverse)改变原列表
            # 42 判断可迭代对象中是否全部是True (all)
            # 43 判断可迭代对象中如果有一个是True，那么就是True（any）
            # 44 自动把可迭代对象中元素逐个添加到函数中执行（filter）
            # 45 枚举方法创建字典(enumerate)
            # 46 对对象进行反射查询静态变量值（getattr）
            # 47 通过反射对类进行添加属性（setattr）
            # 48 通过反射对类进行删除静态变量(delattr)
            # 49 判断对象的所属类型（考虑继承关系isinstance,不考虑继承关系type)
            # 50 判断一个类是不是另一个类的子类（issubclass
            # 51 返回当前位置的全部局部变量（locals）
            # 52 返回全部全局变量（globals）
            # 53 查看当前对象有哪些属性（dir）
            # 54 判断所给的变量是不是可以被调用（callable）
            # 55 startswith()
            # 56 endswith()
            # 57 查找字符串 (find)
            # 58 生成0到1范围内均匀分布的浮点数（random.random）
            # 59 求绝对值 （abs）
            # 60 求次幂(pow)
            # 61 把字符串按照换行符进行分割到列表中返回splitlines()

        # 5 特殊方法

            # 1 __getitem__
            # 2 __len__
            # 3 __iter__
            # 4 __repr__
            # 5 __str__
            # 6 __repr__和__str__
            # 7 __bool__
            # 8 __iadd__
            # 9 __missing__
            # 10 __call__
            # 11 del和垃圾回收
            # 12 __bytes__
            # 13 __slots__
            # 14 __weakref__
            # 15 __setitem__
            # 16 __delitem__
            # 17 __eq__
            # 18 __hash__
            # 19 __mro__

        # 6 关键字

            # 1 关键字in
            # 2 判断出现的值,牢记计算的优先级(()>not>and>or)
            # 3 with 语句执行过程

        # 7 循环

            # 1 对一个空列表执行for循环

        # 8 例子

            # 1 双字符窜组成的元祖或列表转换转换成字典
            # 2 不打乱顺序对列表进行去重1
            # 3 不打乱顺序对列表进行去重2
            # 4 从字典中提取值大于200的项
            # 5 min() 和 max()函数在字典中获取最大最小值
            # 6 使用 sorted() 对字典进行排序
            # 7 创建新字典，对可迭代元素"abcd"中的每个元素作为键值进行创建字典，值都相同(fromkeys)
            # 8 查找两个字典的相同点（相同的键，相同的值,相同的项）
            # 9 通过某个关键字排序一个字典列表(sorted,倒序参数reverse=True)
            # 10 序列中出现的元素次数的计数
            # 11 编辑手动遍历迭代器迭代
            # 12 一个自定义分页的脚本

        # 9 流程控制

            # 1 三元表达式

        # 10 变量

            # 1 *变量
            # 2 小数据池中的内容(is id)

        # 11 文件

            # 1 判断是否存在该文件os.path.exists
            # 2 获取当前文件名sys.argv[0]
            # 3 获取当前文件的绝对路径,不包括文件名os.getcwd()
            # 4 获取文件绝对路径包括文件名os.path.abspath
            # 5 获取绝对路径最后一项文件名os.path.basename
            # 6 判断是否是文件os.path.isfile
            # 7 判断是否是目录os.path.isdir
            # 8 获取文件当前文件大小os.path.getsize
            # 9 获取文件的修改日期os.path.getmtime
            # 10 修改文件操作（打开文件将文件内容修改， 写入另一个文件，删除原文件，将另一个文件名字改成原文件名字）
            # 11 对文件夹进行遍历
            # 12 同时打开两个文件
            # 13 文件的类型
        # 12 异常

            # 1 万能的异常处理
            # 2 主动抛出一个异常

        # 13 算法

            # 二分查找算法

        # 14 正则

            # 1 匹配配数字的表达式（\d [0-9]）
            # 2 匹配数字字母或下划线的表达式（\w [0-9A-Za-z_]）
            # 3 匹配回车或空格（\s）
            # 4 匹配非数字（\D）
            # 5 匹配非数字字母下划线(\W)
            # 6 匹配非空白（\S）
            # 7 匹配字符串开始（^）
            # 8 匹配字符串结尾（$）
            # 9 匹配a或则b（|）
            # 10 非字符组的运用([^xxx])
            # 11 转义字符的运用（\）
            # 12 使用量词{}运用匹配
            # 13 使用量词+ 匹配一次或多次运用
            # 14 使用量词？ 匹配0次或者一次运用
            # 15 使用量词* 匹配0次或多次运用
            # 16 取消贪恋匹配运用（量词？）
            # 17 .*?x 匹配任意字符串直到找到x的运用
            # 18 分割字符串(re.split)
            # 19 捕获分组获取分组中值（()）
            # 20 不保留捕获分组（(?:)）
            # 21 查找字符串 (re.findall)
            # 22 匹配字符串中""中的内容1(.+)
            # 23 匹配字符串中""中的内容2(.*?)
            # 24 对多行进行匹配(\n)
            # 25 编译匹配模式匹配字符串(编译就是速度更快re.compile)
            # 26 替换字符串的内容（re.sub）
            # 27 将字符串中的日期匹配进行捕获分组,然后进行模式替换(re.sub)
            # 28 替换字符串返回之后的字符串和替换次数（re.subn）
            # 29 字符串忽略大小写,把字符串python替换成aaaa（flagS = re.IGNORECASE）

        # 15 模块

            # 1 创建包
            # 2 限制from xxx import * 可以导入的函数
            # 3 Greenlet模块（第三方组件 只是可以实现一个简单的切换功能，还是不能做到遇到IO就切换)
            # 4 gevent模块（第三方组件，实现智能化遇见IO就切换到另一个函数(只能识别自己认识的io操作)
            # 5 gevent模块(第三方组件，实现智能化遇见IO就切换到另一个函数)

        # 标准流

            # 1 标准流输入输出接口（sys.stdin, sys.stdout, sys.stderr）
            # 2 输出标准流(sys.stdout.write)
            # 3 输入标准流sys.stdin.readline
            # 4 重定向流到文件或程序
            # 5 利用shell语法 <filename 把标准输入流重定向到文件输入
            # 6 用管道(pipe)链接程序
            # 7 一个python脚本的输出可以哟个管道发送作为另一个python脚本的输入
            # 8 标准流上的排序和求和
            # 9 重定向流到python对象?
            # 10 print调用中的重定向语法
            # 11 用os.popen重定向如数或输出
            # 12 利用subprocess重定向输入输出
    1
    # 2 pip --> 搜索pippip
    1
        # 1 总提示让更新，更新了之后还提示更新
        # 2 指定源安装软件（快）
    1
    # 3 python3 网络编程
        # 1 架构
        1
            # 1 c / s架构以及优势（client和server
            # 2 b / s架构以及优势（browser和server
        1
        # 2 网络名词
        1
            # 1 mac地址
            # 2 ipv4地址
            # 3 公网的ip作用
            # 4 内网作用
            # 5 交换机的通信方式
            # 6 arp协议
            # 7 端口
                # 端口的范围
            # 8 确定电脑上运行程序
            # 9 路由器
            # 10 网关
            # 11 网段
            # 12 网桥
            # 13 回环地址
            # 14 路由器与交换机的区别（
            # 15 计算的硬件组成
                # 计算机的存储设备的运行速度
                # 计算机的发展
                # 计算机的操作系统
                # 计算机语言发展史
            # 16 并行和并发
                # 并发的本质
            # 17 同步和异步
            # 18 阻塞和非阻塞
            # 19 IPC
            # 20 共享资源
            # 21 cpu的切换
        1
        # 3 互联网协议osi五层模型
        # 4 通信的分类（
            # 全双工通信


        # 5 socket
            1
            # socket
            # socket的类型分类
            # 套接字类型
            # 套接字中的方法
            1
        # 6 进程
            1
            # 1 进程（概念，组成，基本状态，特性，通信限制）
            # 2 进程池(同步做任务apply)
            # 3 进程池(异步做任务apply_async)
            # 4 创建进程
            # 5 守护进程及特性
            # 6 创建守护进程（p.daemon）
            # 7 继承类Process开启进程
            # 8 生产者和消费者模型（JoinableQueue()，q.task_done()，q.join()）
            # 9 管道（了解）
            # 10 在多进程中使用管道
            # 11 进程之间的共享内存
            # 12 电脑进程池的数量(os.cpu_count()+1)
            1
        # 7 线程
            1
            # 1 线程的分类（线程又分为用户级线程和内核级线程（了解）
            # 2 开启线程(不加锁也许会出现数据错乱问题)
            # 3 类继承开启多线程(没加锁会产生数据错乱)
            # 4 守护线程
            # 5 开启守护线程（t.daemon = True）
            # 6 防止多线程的数据错乱1（加锁Lock, l.acquire(), l.release()）
            # 7 多线程的多个锁(防止出现死锁,多个锁一把钥匙 Rlock l.acquire() l.release())
            # 8 多线程的信号量（from threading import Swmphore）
            # 9 多线程的事件（from threading import Event）
            # 10 多线程条件（from threading import Condition
            # 11 多线程定时器
            # 12 线程池(submit异步提交任务不阻塞立即返回，顺序乱)
            # 13 线程池(map异步提交任务不阻塞立即返回，顺序乱, map知识取代了for循环)
            # 14 线程池的回调函数
            1
        # 8 # 线程和进程和协程
            1
                # 线程和进程的比较
                # 进程池和线程池的返回值
                # GIL：全局解释锁
            1
        # 9 TCP协议
            1
            # tcp协议（可靠的，面向连接（前提条件连接）的协议
            # tcp的三次握手
            # tcp的四次挥手
            # tcp的三次握手图文版
            # tcp的四次挥手图文版
            # 创建tcp服务端
            # 创建tcp客户端
            # socketserver模块（tcp协议中，解决服务器不能同时连接多个客户端的问题
            # 粘包
                # 1 粘包
                # 2 合包机制的粘包
                # 3 拆包机制造成的粘包
                # 4 udp协议不会发生粘包
            # 文件上传服务端
            # 文件上传服务端客户端
            1
        # 10 udp协议
            1
            # 创建UDP服务端
            # 创建UDP客户端（步骤 1创建套接字2发送和接受sendto(b'xxx',(ip，端口)3关闭套接字）
            1
        # 11 # 协程
            1
            # 协程的创建（yelid）
            # yield实现并发的假象
            1
        # 12 IO多路复用
            1
            # select 和 poll 和epoll的区别
            # socket用非阻塞io解决阻塞io(不推荐，循环造成cpu负担)
            # select解决非阻塞造成cpu负担（基于select的网络IO模型)
            1

# =================================================
# pippip
#
# 1 问题： 总提示让更新，更新了之后还提示更新
    # 解决：
        # pip uninstall pip
        # easy_install pip

# 2 指定源安装软件（快）

    # pip3 install - i https: // pypi.douban.com / simple 软件名1
# # =================================================



# =================================================
# python3python3

# windows安装说明
    # 1 去官网下载
    # 2 因为下载速度较慢，先下载迅雷然后复制下载地址在迅雷下载
    # 3 选择适合系统的版本，注意是executable installer结尾的
    # 4 去终端确认是否安装成功输入python成功的话会显示python版本

# 使用hashlib库进行md5加密
    # 1导入hashlib模块
    # 2创建md5对象
    # 3对字符串进行编码
    # 4对字符串进行md5编码
    # import hashlib
    # a = 'a'
    # m = hashlib.md5()
    # m.update(a.encode('utf-8'))
    # md5_info = m.hexdigest()
    # print(md5_info)
    # # >>> 0cc175b9c0f1b6a831c399e269772661


# python3模块导入出现no model name 'xx'
    # 解决方法： 模块所在的文件目录添加到sys.path中
    # import sys
    # sys.path.append('所要导入的文件的绝对路径文件目录的绝对路径')



# 获取字典中最大最，最小值的键
#     a = {"b": 1, "c": 2, "d": 3}
#     print(min(a, key=a.get))
#     # >>> b
#     print(max(a, key=a.get))
#     # >>> d


# 获取一个列表元素的多种组合
# import itertools

# 所有列表中元素组合重复出现，顺序不同
    # a = [1,2,3,4]
    # b = itertools.permutations(a, 2) # 返回可迭代元素之间的不同组合，第二个参数为选取几个对象进行组合
    # print(list(b))
    # >>>[(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]

# 所有列表中元素组合不重复出现
    # c = itertools.combinations(a, 2)
    # print(list(c))
    # >>>[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]


# 获取多个列表的多种组合(元素个数不同也可以)
    # import itertools
    # a = [1,2,3]
    # b = [4,5]
    # c = itertools.product(a, b)
    # print(list(c))
    # # >>> [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]

# 小数列表推导式
    # a = [i/10 for i in range(10)]
    # print(a)
    # >>> [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]


# map函数的使用
    # def a(s):
    #     return s*2
    # print(list(map(a, [1, 2])))
    # # >>> [2, 4]

# 将字符串转换成decimal类型
    # import decimal
    # a = decimal.Decimal('0.123456')
    # print(a)
    # # >>> 0.123456


# split字符串分割
    # a = "a,b,c"
    # print(a.split(","))
    # # >>> ['a', 'b', 'c']

# 日期的加减datetime
    # import datetime
    #
    # date1 = '2010/01/01'
    # date2 = '2012/01/05'
    #
    # a = datetime.datetime.strptime(date1, '%Y/%m/%d')  # 2010-01-01 00:00:00
    # b = datetime.timedelta(days=1)  # 1 day, 0:00:00
    # c = a - b   # 2009-12-31 00:00:00
    # d = datetime.datetime.strftime(c, '%Y/%m/%d')
    # print(d)
    # >>> 2009/12/31     str类型





# 时间戳转换成字符串时间
    # import time
    # a = time.time()     # 1557036387.8737695
    # b = time.localtime(a)  # time.struct_time(tm_year=2019, tm_mon=5, tm_mday=5...sdst=0)
    # c = time.strftime("%Y-%m-%d %H:%M:%S", b)
    # print(c)
    # >>> 2019-05-05 14:16:58


# 字符串时间转换成时间戳
    # import time
    # a = "2019-05-05 14:16:58"
    # b = time.strptime(a, "%Y-%m-%d %H:%M:%S")   # time.struct_time(tm_year=2019, tm_mon=5, ... tm_isdst=-1)
    # c = time.mktime(b)
    # print(c)
    # # >>> 1557037018.0

# 对象类型转换成json
    # import json
    #
    # class A:
    #     def __init__(self, a):
    #         self.a = a
    #
    # b = A(2)
    # c = b.__dict__
    # print(json.dumps(c))
    # # >>> {"a": 2}


# 获取商和余数的函数divmod
    # a = 10
    # b = 3
    # print(divmod(10, 3))
    # # >>> (3, 1)

# 新版线程池的创建
    # from concurrent.futures import ProcessPoolExecutor
    # import time
    # def test(s):
    #     print("子进程开始", s)
    #     time.sleep(2)
    #     print('子进程结束', s)
    #     return s**2
    # if __name__ == '__main__':
    #     p = ProcessPoolExecutor(max_workers=5)
    #     li = []
    #     for i in range(20):
    #         result = p.submit(test, i) # 向线程池对象中放任务 submit
    #         li.append(result)
    #     p.shutdown(True)   # 禁止在向线程池中添加任务,主线程等待线程池任务结束 shutdown
    #     for j in li:
    #         print(j.result()) # 将提交任务返回结果放入里表值嗯 子线程全部结束和循环列表



# 进程池的创建
# Pool([numprocess  [,initializer [, initargs]]]):创建进程池
# numprocess:要创建的进程数，如果省略，将默认使用cpu_count()的值
# initializer：是每个工作进程启动时要执行的可调用对象，默认为None
# initargs：是要传给initializer的参数组
# p.close():关闭进程池，防止进一步操作。如果所有操作持续挂起，它们将在工作进程终止前完成
# P.join():等待所有工作进程退出。此方法只能在close（）或teminate()之后调用
# 方法apply_async()和map_async（）的返回值是AsyncResul的实例obj。实例具有以下方法
# obj.get():返回结果，如果有必要则等待结果到达。timeout是可选的。如果在指定时间内还没有到达，将引发一场。如果远程操作中引发了异常，它将在调用此方法时再次被引发。
# obj.ready():如果调用完成，返回True
# obj.successful():如果调用完成且没有引发异常，返回True，如果在结果就绪之前调用此方法，引发异常
# obj.wait([timeout]):等待结果变为可用。
# obj.terminate()：立即终止所有工作进程，同时不执行任何清理或结束任何挂起工作。如果p被垃圾回收，将自动调用此函数

# 同步调用apply
    # from multiprocessing import Pool
    # import time, os
    #
    # def test(n):
    #     print("%s得到参数%s"%(os.getpid(), n))
    #     time.sleep(1)
    #     return n**2
    #
    # if __name__ == '__main__':
    #     p = Pool(5)
    #     li = []
    #     for i in range(10):
    #         result = p.apply(test, args=(i,))  # 在一个池工作进程中执行任务apply（）
    #         li.append(result)
    #     p.close()   # 执行完close后不会有新的进程加入
    #     p.join()    # join函数等待所有子进程结束
    #     for j in li:
    #         print(j)


# 异步调用apply_async
    # from multiprocessing import Pool
    # import time
    # import os
    # def test(n):
    #     print("%s得到了%s"%(os.getpid(), n))
    #     time.sleep(3)
    #     return n**2
    #
    # if __name__ == '__main__':
    #     p = Pool(5)
    #     li = []
    #     for i in range(10):
    #         result = p.apply_async(test, args=(i,))  # 异步执行任务
    #         li.append(result)
    #     p.close()  # 禁止再提交任务
    #     p.join()   # 主进程等待任务结束
    #     for j in li:
    #         print(j.get())  # 获取返回的任务结果要用.get方法取出


# 异步调用+回调函数(注意顺序会乱)

    # from multiprocessing import Pool
    #
    # def test(s):
    #     print("拿到了%s"%s)
    #     return s**2
    #
    # def test2(s):
    #     print("返回的结果",s)
    # if __name__ == '__main__':
    #     p = Pool(5)
    #     for i in range(10):
    #         p.apply_async(test, args=(i,), callback=test2) #  异步执行任务将返回值传入回调函数异步执行
    #
    #     p.close()
    #     p.join()
    #     print("主线程")



# __getitem__

    # class A:
    #     def __init__(self, a):
    #         self.a = a
    #
    #     def __getitem__(self, item):
    #         return self.a[item]
    #
    # a = A("abcd")
    # print(a[2]) # 通过对象的索引值获取时候触发__getitem__
    # # >>> c

# __len__

    # class A:
    #     def __init__(self, a):
    #         self.a = a
    #
    #     def __len__(self):
    #         return len(self.a)
    #
    # a = A([1,2,3,4])
    # print(len(a)) # len(对象)自动触发__len__
    # >>> 4



# __iter__

    # class A:
    #     def __init__(self, a):
    #         self.a = a
    #
    #     def __iter__(self):
    #         return (i for i in self.a)
    #
    #
    # a = A([1,2,3,4])
    # for i in a:   # 对对象进行for循环 自动触发了__iter__
    #     print(i)
    # # >>> 1
    #     # 2
    #     # 3
    #     # 4

# __repr__

    # class A:
    #     def __init__(self, a):
    #         self.a = a
    #
    #     def __repr__(self):  # 获取对象的字符串表现形式
    #         return "A({})".format(self.a)
    #
    # a = A("aa")
    # print(repr(a))  # 通过repr()触发__repr__
    # >>> A(aa)





# __str__

    # class A:
    #     def __init__(self, a):
    #         self.a = a
    #
    #     def __str__(self):  # str()函数被使用，或是在用print函数打印一个对象的时候才被调用的
    #         return "A({})".format(self.a)
    #
    # a = A("aa")
    # print(a)
    # print(str(a))
    # >>> A(aa)
    # >>> A(aa)

# __repr__和__str__
    # class A:
    #     def __init__(self, a):
    #         self.a = a
    #
    #     # def __str__(self):   因为如果一个对象没有__str__函数，而Python又需要调用它的时候，
    #                            解释器会用__repr__作为替代
    #     #     return "A({}) str".format(self.a)
    #
    #     def __repr__(self):
    #         return "A({}) repr".format(self.a)
    #
    # a = A("aa")
    # print(a)
    # print(repr(a))
    # # A(aa) repr
    # # A(aa) repr



# __bool__

    # bool(x)调用x.__bool__()的结果如果不存在__bool__方法，那么bool(x)会尝试调用x.__len__()

    # class A:
    #
    #     def __init__(self, a):
    #         self.a = a
    #
    #     def __bool__(self):
    #         return bool(self.a)
    #
    # a = A('')
    # print(bool(a))
    # >>> False


# 列表推导式（组合出不同的元素,并不是所有）
    # a = [1, 2, 3]
    # b = ['a', 'b', 'c']
    # c = [(i, j) for i in a for j in b]
    # print(c)
    # # >>> [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]

# 生成器表达式

    # # 作用
    # #
    # #     生成其他序列类型
    # #     遵守了迭代器协议，可以逐个地产出元素
    # #     语法和列表推导式差不多，更节省内存
    # #     在每个for循环运行时，才生产一个元素，不会生产列表
            # a = (i for i in range(3))
            # print(a)
            # # <generator object <genexpr> at 0x0000000002164BF8>



# 拆包做参数

    # def f(a,b):
    #     return a+b
    #
    # c = (1, 2)
    # s = f(*c)
    # print(s)
    # # >>> 3

# 元祖的排序
    # 可以使用排序方法reversed(), 但生成的元祖是新元祖，不是改变原来的元祖
    # a = (1, 2, 3, 4)
    # b = reversed(a)
    # print(tuple(b))
    # print(b is a)
    # >>> (4, 3, 2, 1)
    # >>>False




# 嵌套元祖拆包

    # a = (1,2,[3,4,(5,6)])
    # b,c,[d,e,f] = a
    # print(b,c,[d,e,f])
    # >>> 1 2 [3, 4, (5, 6)]


# 具名元祖

    # from collections import namedtuple
    #
    # a = namedtuple('Test', ['a', 'b', 'c'])  # 参数('类名', 字符串组成的可迭代对象或空格隔开的字符串)
    # b = a(a='haha', b='hehe', c='nuonuo')
    # print(b._fields)
    # # >>> ('a', 'b', 'c') # 显示字段名
    #
    # print(b._make([1, 2, 3])) # 创建具名元祖，替换原元祖中的属性
    # # >>>Test(a=1, b=2, c=3)
    #
    # print(b._asdict())  # 返回类字典形式
    # # >>>OrderedDict([('a', 'haha'), ('b', 'hehe'), ('c', 'nuonuo')])



# 切片的命名
#     a = ['a', 'b', 'c', 'd']
#     b = slice(0,2)
#     print(a[b])
#     # >>> ['a', 'b']


# 切片的赋值
#     a = ['a', 'b', 'c', 'd']
#     a[0:1] = [999]
#     print(a)
#     # >>> [999, 'b', 'c', 'd']




# 对序列使用 + 和 *

    # 不会对改变原列表
    # a = [1, 2, 3]
    # b = ['a', 'b', 'c']
    # print(a*2)
    # print(a+b)
    # print(a)
    # print(b)
    # >>> [1, 2, 3, 1, 2, 3]
        # [1, 2, 3, 'a', 'b', 'c']
        # [1, 2, 3]
        # ['a', 'b', 'c']


# *生成同一个对象

    # a = [[2]] *3
    # a[0].append(9)
    # print(a)
    # >>> [[2, 9], [2, 9], [2, 9]]


# 避免*生成同一个对象

    # a = [[2] for i in range(3)]
    # a[0].append(9)
    # print(a)
    # >>> [[2, 9], [2], [2]]



# __iadd__

    # 可变序列 +=之后改变原序列
    # 不可变序列 +=之后不改变原序列生产新序列
    # 对象 += x 自动触发 __iadd__
    # class A:
    #     def __init__(self,a):
    #         self.a = a
    #
    #     def __iadd__(self, other):
    #         return self.a + other
    #
    # a = A(1)
    # a += 1
    # print(a)
    # >>> 2


# list.sort 和 sorted

    # 1 都是排序
    #     list.sort 的返回值是None 改变的原列表
    #     sorted 的返回值是排完序的列表，不改变原列表，生产新的列表
    # 2 可变和不可变序列
    #     list.sort对可变序列进行排序
    #     sorted 对可变序列和不可变序列都能排序
    # 3 参数
    #      都有参数 reverse 和key
    #      reverse
    #         默认reverse=False 升序排列 reverse=True降序排列
    #      key
    #         一个只有一个参数的函数，这个函数会被用在序列的每一个元素上
    #         产生的结果将是排序算法依赖的对比关键字 如key=len 基于元素的
    #         长度排序
    # a = ['apple', 'rule', 'sex', 'lingling', 'yingyign']
    #
    # print(sorted(a))
    # # >>>['apple', 'lingling', 'rule', 'sex', 'yingyign']
    # print(sorted(a, key=len))
    # # >>>['sex', 'rule', 'apple', 'lingling', 'yingyign']
    # a.sort(key=len)
    # print(a)
    # # >>>['sex', 'rule', 'apple', 'lingling', 'yingyign']


# bisect
    # 二分法操作已经排序的序列
        # import bisect
        #
        # a = [1, 3, 5, 6, 7, 8, 9, 24, 54, 56, 87, 99]
        #
        # index = bisect.bisect(a, 24)  # 返回查询值索引的右边索引
        # index1 = bisect.bisect_left(a, 24) # 返回查询值当前索引
        # index2 = bisect.bisect_right(a, 24) # 返回查询值索引的右边索引
        # print(index)
        # print(index1)
        # print(index2)
        # >>> 8
        #     7
        #     8



    # 把变量插入序列 序列保持升序
        # bisect.insort(序列, 变量)
        # import bisect
        #
        # a = [23, 1, 6, 4, 5, 2, 7, 11]
        # li = []
        # for i in a:
        #     bisect.insort(li, i)
        # print(li)
        # # >>> [1, 2, 4, 5, 6, 7, 11, 23]


# 数组(只存放数字列表的时候,推荐使用数组替代列表)

    # 创建浮点型数组 类型为 ‘d’
        # a = array('d', (random() for i in range(5)))
        # print(a)
        # >>> array('d', [0.9630822375495147, 0.3624485412974797, 0.9147125645263343, 0.485004411974695, 0.266999018425945])


    # 将数组写入文件
        # with open('array.bin', 'wb') as f:
        #     floats.tofile(f)

    # 从文件读取数组
        # with open('array.bin', 'rb') as f2:
        #     a = array('d')
        #     a.fromfile(f2, 10)  # 把10个浮点数从二进制文件中读取出来


    # 数组的排序
        # 不支持list.sort()
        # from array import array
        #
        # a = array('b', [3, 1, 2, 5, 4])
        # b = array(a.typecode, sorted(a))
        # print(b)
        # # >>>array('b', [1, 2, 3, 4, 5])


# 双向队列

    # 创建双向队列
    #     from collections import deque
    #     dq = deque(range(5), maxlen=10)     # 创建双向队列，最大容纳10个元素
    #     print(dq)
    #     # >>> deque([0, 1, 2, 3, 4], maxlen=10)

    # 旋转操作
    #     dq.rotate(2)  # 旋转操作当n>0 队列最右面n个元素会被移动到左边
    #     # 当n<0,左边的n个元素会被移动到右边
    #     print(dq)
    #     # >>> deque([3, 4, 0, 1, 2], maxlen=10)

    # 向头部添加元素
    #     dq.appendleft(99)
    #     print(dq)
    #     # >>>deque([99, 0, 1, 2, 3, 4], maxlen=10)

    # 合并列表
    # dq.extend(['a', 'b', 'c'])
    # print(dq)
    # # >>>deque([0, 1, 2, 3, 4, 'a', 'b', 'c'], maxlen=10)

    # 头部倒叙插入列表
    #     dq.extendleft(['a', 'b', 'c'])
    #     print(dq)
    #     # 注意插入的列表是倒着插进去的
    #     # >>> deque(['c', 'b', 'a', 0, 1, 2, 3, 4], maxlen=10)


# 可散列数据类型
    # 可hash ，拥有__hash__()方法，__qe__()方法，和其他键做比较
    # t1 = (1, 2, (3, 4))  # 不可变
    # t2 = (1, 2, [3, 4])  # list可变
    # t3 = (1, 2, frozenset([30, 40])) # 不可变
    # print(hash(t1))
    # print(hash(t2))
    # print(hash(t3))
    # # >>> -2725224101759650258
    # # >>> TypeError: unhashable type: 'list'
    # # >>> 985328935373711578



# 字典的构造方法
    #
    # a = dict(one=1, two=2, three=3)
    # b = {'one': 1, 'two': 2, 'three': 3}
    # c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    # d = dict([('one', 1), ('two', 2), ('three', 3)])
    # e = dict({'one': 1, 'two': 2, 'three': 3})
    # print(a)
    # print(a == b == c == d == e)
    # >>> {'one': 1, 'two': 2, 'three': 3}
    # >>> True

# 字典推导

    # a = [(1, 'a'), (2, 'b'), (3, 'c')]
    # b = {key: value for key, value in a}
    # print(b)
    # >>> {1: 'a', 2: 'b', 3: 'c'}

# 用setdefault处理找不到的键

    # a = {}
    # a.setdefault('s', [])  # 如果字典中查询的键‘s’,那么字段中就会在字典中设置键值对's':[]
    # print(a)
    # # >>>{'s': []}
    # print(a.setdefault('s', []))  # 如果存在所字典中存在所查询的键's' 那么直接返回's'键所对应的值
    # # >>>[]



# __missing__
#
#     __missing__方法只会被__getitem__调用如果有一个类继承了dict，
#     然后这个继承类提供了__missing__方法，那么在__getitem__碰到找不到的键的时候，
#     Python就会自动调用它，而不是抛出一个KeyError异常。

# 字典的其他种类

# collections.OrderedDict
#     添加键的时候会保持顺序

# collection.ChainMap
#     容纳数个不同的映射对象, 操作的时候，这些对象会被当作一个整体被逐个查找
#     a = collections.ChainMap({"s": 1}, {"a": 2}, {"b": 3})
#     for i in a:
#         print(i)
#     # >>>s
#     #    b
#     #    a

# collection.Counter
#
#     计数器，结果是映射
#     import collections
#
#     a = collections.Counter('abcdabgtghhdhgk')
#     print(a)
#     # >>> Counter({'g': 3, 'h': 3, 'a': 2, 'b': 2, 'd': 2, 'c':1, 't': 1, 'k': 1})

# collections.UserDict
    # 用户自定义字典


# MappingProxyType
    # 不可变映射类
    #
    # from types import MappingProxyType
    #
    # a = {"a": 1}
    # b = MappingProxyType(a)
    # print(b)
    # # >>> {'a': 1}
    # print(b['a'])
    # # >>> 1
    # b['a'] = 2
    # # >>>TypeError: 'mappingproxy' object does not support ite
    # # m assignment

# 字典获取值的原理
#
#     0 my_dict[key]的背后原理
#     1调用hash(key)获取散列值，
#     2把这个值的最低几位数字当做偏移量，在散列表里查找
#     3如果为空抛出异常
#     4如果不为空，就会有键和值 ，判断查询的key和找到的键是否相同
#     5如果相同就返回值
#     6如果不同在散列值中另外取几位继续查找
#     7循环以上....

# 可散列的对象必须满的条件。
#     (1)支持hash()函数，并且通过__hash__()方法所得到的散列值是不变的。
#     (2)支持通过__eq__()方法来检测相等性。
#     (3)若a == b为真，则hash(a) == hash(b)也为真。

# Python里的dict和set的效率有多高？
#
#     比列表快字典在内存上的开销巨大



# 2为什么字典是无序的？
#     键的次序取决于添加顺序, 当往dict里添加新键而又发生散列冲突的时候，
#     新键可能会被安排存放到另一个位置如果在key1和key2被添加到字典里的过程
#     中有冲突发生的话，这两个键出现在字典里的顺序是不一样的置




# 为什么dict的键和set元素的顺序是跟据它们被添加的次序而定的，以及为什么在映射对象的生命周期中，这个顺序并不是一成不变的？
#     无论何时往字典里添加新的键，Python解释器都可能做出为字典扩容的决定。扩容导
#     致的结果就是要新建一个更大的散列表，并把字典里已有的元素添加到新表里。
#     这个过程中可能会发生新的散列冲突，导致新散列表中键的次序变化



# 为什么不应该在迭代循环dict或是set的同时往里添加元素？
#     无论何时往字典里添加新的键，Python解释器都可能做出为字典扩容的决定。扩容导
#     致的结果就是要新建一个更大的散列表，并把字典里已有的元素添加到新表里。
#     这个过程中可能会发生新的散列冲突，导致新散列表中键的次序变化


# set和frozenset
#     set和frozenset的实现也依赖散列表，但在它们的散列表里存放的只有元素的引用
#     （就像在字典里只存放键而没有相应的值）
#     集合里的元素必须是可散列的。
#     集合很消耗内存。
#     可以很高效地判断元素是否存在于某个集合。
#     元素的次序取决于被添加到集合里的次序。
#     往集合里添加元素，可能会改变集合里已有元素的次序。

# 文本和字节序列
#
#
#     字符串一个字符是一个字符序列
#     Python3的str对象中获取的元素是Unicode字符
#     Unicode标准把字符的标识和具体的字节进行区分
#     字符串的标识，即码位字符的具体表述取决于所用的编码
#     编码是在码位和字节序列之间转换时使用的算法
#
#     把码位转换成字节序列的过程是编码，把字节序列转换成码位的过程是解码



# bytes、bytearray等二进制序列的独特特性

    # bytes不可变字节类型
    # bytearray可变字节数组类型
    #
    # a = bytes('cafe', encoding='utf-8')  # 给str对象编码构建
    # print(a)
    # print(a[0])  # 各个元素是range（256）内的整数
    # print(a[:1])  # bytes类型切片 还是bytes对象
    # a_array = bytearray(a)
    # print(a_array)
    # print(a_array[-1:])
    # # >>> b'cafe'
    # # >>> 99
    # # >>> b'c'
    # # >>> bytearray(b'cafe')
    # # >>> bytearray(b'e') # 字节数组对象的切片还是字节数组对象

# 避免和处理编码错误
#     写入和输出推荐使用编码参数
#     处理文本文件的最佳实践
#     1解码输出的字节序列
#     2只处理文本
#     3编码输出文本
#
#     默认编码的陷阱和标准I / O的问题
#     写入和输出推荐使用编码参数

# 函数
#     函数是一等对象在运行时创建能赋值给变量或数据结构中的元素能作为参数传给函数能作为函数的返回结果


# __call__
#
#     用户自定义可调用类型（__call__）
#
#     class A:
#
#         def __call__(self):
#             return '我是可调用类型'
#
#     a = A()
#     print(a())
#     # >>> 我是可调用类型



# 计算两个属性集合差
    # class A:
    #     pass
    #
    #
    # def b():
    #     pass
    #
    #
    # a = A()
    #
    # print(set(dir(a)) - set(dir(b)))
    # # >>> ['__weakref__']



# 强制必须传入实参
#
#     def f(a, *, b):
#         return a, b


# 提取关于函数参数的信息
#
#
#     def f(a, c, b=2, *args, **kwargs):
#         return a, b, c
#         # 参数的默认值通过__defaults__元祖中的位置确定，从后向前扫描才能把参数和默认值对应起来
#     print(f.__defaults__)  # 存放关键字值的元祖
#     # >>> (2,)
#     print(f.__code__.co_varnames)  # 存放参数名称的元祖
#     # >>> ('a', 'c', 'b', 'args', 'kwargs')
#     print(f.__code__.co_argcount)  # 参数个数值不包括边长参数（*，**）
#     # >>> 3




# 函数注解
#     对函数的运行没有影响
#
#
#     def f(a: int, b: 'int>0' = 80) -> int:
#         return a + b
#
#     print(f(-1, -2))
#     print(f.__annotations__)  # 函数注解存储的地方
#     # >>> {'a': <class 'int'>, 'b': 'int>0', 'return': <class 'int'>}




# 根据元祖的某个元素给元祖列表排序itemgetter
#     from operator import itemgetter
#
#     a = [
#         ('b', 1, 'bbbbb'),
#         ('c', 12, 'ccccc'),
#         ('a', 5, 'aaaa')
#     ]
#
#     for i in sorted(a, key=itemgetter(0)):
#         print(i)
#
#     # >>> ('b', 1)
#     # ('a', 5)
#     # ('c', 12)





# 多个参数传给itemgetter，她的构建的函数会返回提取的值构成元祖
    # b = itemgetter(0, 2)
    # for i in a:
    #     print(b(i))
    # >>> ('b', 'bbbbb')
    # ('c', 'ccccc')
    # ('a', 'aaaa')



# 函数的装饰器

    # 装饰器在加载模块时立即执行
    #
    # def a(func):
    #     print('我是a')
    #     def c():
    #         print('我是c')
    #         func()
    #     return c
    #
    # @a
    # def b():
    #     print('我是b')
    #
    #
    # b()
    # # >>> 我是a
    # # 我是c
    # # 我是b



# 变量作用域规则
#     b = 2
#
#     def f(a):
#         print(a)
#         print(b)
#         b = 3
#
#
#     f(1)
#     # >>>UnboundLocalError: local variable 'b' referenced before assignment
#     python编译函数定义时候, 他判断b是局部变量，因为在函数体重给b赋值了，python会尝试
#     从本地环境获取b
#     调用函数f的时候会获取并打印局部变量a的值，但是尝试获取局部变量b的值
#     发现没有绑定值所以报错



# 闭包的定义和作用
#
#     闭包延伸了作用域的函数，其中包含函数定义体引用，不在定义体中定义的非全局变量
#     保存变量（下列方法只适用于自由变量为可变类型）
#
#     def a():
#         li = []  # 未在本地作用域中绑定的变量（自由变量）
#
#         def b(args):
#             li.append(args)
#             return sum(li) / len(li)
#
#         return b
#
#
#     s = a()
#     print(s(1))
#     print(s(2))
#     print(s(3))
#     # >>> 1.0
#     # 1.5
#     # 2.0
#
#     工作原理
#     保留定义函数时存在的自由变量的绑定，这样调用函数时
#     虽然定义作用域不可用了，但是仍能使用那些绑定




# nonlocal
    #
    # 当闭包函数中，声明的自由变量为不可变类型，那么久相当于生产了局部变量，为不是自由变量
    # nonlocal的作用就是把变量变成自由变量
    #
    #
    # def a():
    #     c = 0
    #     d = 0
    #
    #     def b(args):
    #         nonlocal c, d
    #         c += 1
    #         d += args
    #         return d / c
    #
    #     return b
    #
    #
    # s = a()
    # print(s(1))
    # print(s(2))
    # print(s(3))
    # # >>> 1.0
    # # 1.5
    # # 2.0



# 标准库中的装饰器
#
#     functools.wraps（经过测试没有覆盖__name__和__doc__属性）
#     普通装饰器会遮盖被装饰函数__name__和__doc__属性，functools.wraps把
#     相关属性赋值到函数中，还能正确处理关键字参数
#
#     functools.lru_cache(优化递归函数)
#     事项了备忘功能，他把耗时的函数结果保存起来，避免传入相同的参数
#     时重复计算





# 叠放装饰器

    # def d2(func):
    #     def f2(*args):
    #         s = func(*args)
    #         return s * 10
    #     return f2
    #
    #
    # def d1(func):
    #     def f1(*args):
    #         s = func(*args)
    #         return s * 10
    #     return f1
    #
    #
    # @d2
    # @d1
    # def test(a):
    #     return a
    #
    #
    # s = test(2)
    # print(s)
    # # >>> 200


# 参数化装饰器(装饰器外在嵌套一层函数传入的参数)
#
    # def a1(show):
    #     def d1(func):
    #         def f1(*args):
    #             s = func(*args)
    #             print(show)
    #             return s * 10
    #
    #         return f1
    #
    #     return d1
    #
    #
    # @a1(show=22)
    # def test(a):
    #     return a
    #
    #
    # s = test(10)
    # print(s)





# is 和 == 区别
#
#     == 比较两个对象的值（对象中保存的数据）
#     a == b等同于a.__eq__(b)
#     object的__eq__方法比较两个对象的ID，结果与 is 一样is 比较对象的标识（在变量和单值之间比较时）
#     is 运算符比 == 速度快, 直接比较两个整数ID




# 列表的浅复制

    # l1 = list(li)
    # l1 = li[:]
    # 浅拷贝注意的事情
    # l1 = [1, 2, 3, [44, 55]]
    # l2 = l1[:]
    # print(l2)
    # # >>>[1, 2, 3, [44, 55]]
    # l2[3].append(999)
    # print(l1)
    # # >>> [1, 2, 3, [44, 55, 999]]
    # print(l2)
    # # >>> [1, 2, 3, [44, 55, 999]]
    # l1.append(666)
    # print(l1)
    # # >>> [1, 2, 3, [44, 55, 999], 666]
    # print(l2)
    # # >>> [1, 2, 3, [44, 55, 999]]





# del和垃圾回收
#     在CPython中，垃圾回收使用的主要算法是引用计数每个对象都会统计有多少引用指向自己。
#     当引用计数归零时，对象立即就被销毁分代垃圾回收算法，用于检测引用循环中涉及的对象组，
#     如果一组对象之间全是相互引用，即使再出色的引用方式也会导致组中的对象不可获取
    # 弱引用
    # 弱引用不会增加对象的引用数量。引用的目标对象称为所指对象（referent）。因此我们
    # 说，弱引用不会妨碍所指对象被当作垃圾回收



# __bytes__
#
#     bytes()函数调用它获取对象的字节序列表示形式



# __format__
#
#     使用特殊的格式代码显示对象的字符串表示形式format()



# __slots__

    # 类属性节省空间
    # Python在各个实例中名为__dict__的字典里存储实例属性__slots__类属性，
    # 能节省大量内存，方法是让解释器在元组中存储实例属性，而不用字典缺点在类中定义__slots__
    # 属性之后，实例不能再有__slots__中所列名称之外的其他属性。这只是一个副作用

    # class A:
    #     __slots__ = ('a', 'b')
    #
    #
    # a = A()
    # a.b = 2
    # print(a.b)
    # # >>> 2
    #
    # __slots__# 的问题总之，如果使用得当，__slots__能显著节省内存，不过有几点要注意。
    # 每个子类都要定义__slots__属性，因为解释器会忽略继承的__slots__属性。
    # 实例只能拥有__slots__中列出的属性，除非把'__dict__'加入__slots__中
    # （这样做就失去了节省内存的功效）。如果不把'__weakref__'加入__slots__，实例就不能作为弱引用的目标

# __weakref__
#
#     为了让对象支持弱引用覆盖类属性
#     类属性可用于为实例属性提供默认值




# 内置的iter
#     函数有以下作用
#     (1)检查对象是否实现了__iter__方法，如果实现了就调用它，获取一个迭代器。
#     (2)如果没有实现__iter__方法，但是实现了__getitem__方法，Python会创建一个迭代器，尝试按顺序（从索引0开始）获取元素。
#     (3)如果尝试失败，Python抛出TypeError异常，通常会提示“Cobject is not iterable”
#         （C对象不可迭代），其中C是目标对象所属的类。




# 数字类型
#     int型 不能以0开头



# 运算顺序
#
#     括号 > 指数运算 > 乘法 / 除法 > 加法 / 减法 >
#     具有相同优先级的运算符按照从左到右的顺序进行计算(除了指数运算)




# 字符串运算
    # a = "a"
    # print(a + "b") # +  拼接
    # print(a * 5) # *重复执行
    # # >>> ab
    # # aaaaa


# 错误类型
#
#     语法错误(syntaxerror)、
#     运行时错误(runtimeerror)也可称为异常(exception)
#     语义错误(semanticerror)。




# int方法int()
#
#     int能将浮点数转换为整型数, 但是它并不进行舍入;只是截掉了小数点部分
#     a = 1.2345
#     print(int(a))
#     # >>> 1



# 实参的计算
#     在函数被调用之前, 实参会先进行计算




# 函数中的变量和形参都是局部的





# 泛化
#     为函数增加一个形参被称作泛化



# 重构
#
#     重新整理一个程序以改进函数接口和促进代码复用的这个过程, 被称作重构



# 关键字in
    # in是一个布尔运算符,对于列表他按顺序依次查找目标
    # 对于字典python用哈析表的算法无论字典中有多少项, in 运算符搜索所需的时间都是一样的



# 对一个空列表执行for循环时
#     将不会执行循环的主体





# 序列的比较大小
    # 会首先比较序列中的第一个元素, 如果它们相等, 就继续比较下一组元素,
    # 以此类推, 直至比值不同。其后的元素(即便是差异很大) 也不会再参与比较
    # a = [1,2,34]
    # b = [1,3,4]
    # print(a<b)
    # # >>> True




# LIFO
#     后进先出->栈
#
# FIFO
#     先进先出->队列





# 双字符窜组成的元祖或列表转换转换成字典
    # 源代码注释
        # d = {}
        # for k, v in iterable:
        #     d[k] = v
    # a = ['ab', 'cd', 'ef']
    # print(dict(a))
    # {'a': 'b', 'c': 'd', 'e': 'f'}





# 合并字典
    # a = {"a":1}
    # a.update({"b":2})
    # print(a)
    # >>> {'a': 1, 'b': 2}





# 将字典传入set()函数
    # a = {"a":1, "b":2}
    # print(set(a))
    # >>> {'a', 'b'}






# 不打乱顺序对列表进行去重
    # a = [5,3,4,6,5,7,5,6]
    # b = list(set(a))
    # b.sort(key=a.index)
    # print(b)
    # # >>> [5, 3, 4, 6, 7]





# 字典按照其中的值进行排序
    # a = [
    #     {'a': 1, 'b': 88},
    #     {'a': 2, 'b': 38},
    #     {'a': 3, 'b': 18},
    #     {'a': 4, 'b': 90},
    # ]
    #
    # b = sorted(a, key=lambda x:x['b'])
    # print(b)




# python中False的类型元素
    # 布尔False null类型 None 整型0 浮点型0.0 空字符串 ''
    # 空列表[] 空元组() 空字典{} 空集合set()




# zip()
    # a = "a", "b", "c"
    # b = "1", "2", "3"
    # print(list(zip(a, b)))
    # # >>> [('a', '1'), ('b', '2'), ('c', '3')]





# help()
    # 可以打印输出一个函数的文档字符串
    # def f():
    #     """function f"""
    #     return 1
    #
    # help(f)
    # # >>> f()
    #         # function f




# 模块搜索路径列表sys.path
    # import sys
    # # sys.path 返回模块搜索路径列表 第一个是当前文件所在的文件夹
    # print(sys.path)





# 统计列表中重复出现元素的次数
    # from collections import Counter
    # a = ['spam', 'spam', 'eggs', 'spam']
    # b = Counter(a)
    # print(b)
    # >>> Counter({'spam': 3, 'eggs': 1})




# 根据元素出现的次数降序排列元素和出现次数
    # from collections import Counter
    #
    # a = ['spam', 'spam', 'eggs', 'spam']
    # b = Counter(a)
    # c = b.most_common() # 参数内填int型， 表示查询多少项
    # print(c)





# 计数器的相加(也支持+-&|运算)
    # from collections import Counter
    #
    # a = ['spam', 'spam', 'eggs', 'spam']
    # b = ['eggs', 'spam', 'apple']
    # a1 = Counter(a)
    # b1 = Counter(b)
    # print(a1 + b1)
    # # Counter({'spam': 4, 'eggs': 2, 'apple': 1})






# 创建对象，执行对象方法的执行过程
    # a = Car()
    # car.b()
    # 做了以下两件事情:
    # 查找a对象所属的类Car;• 把a对象作为self参数传给Car类所包含的b()方法




# 记录多少个类A的对象被创建

    # class A():
    #     count = 0
    #     def __init__(self):
    #         A.count += 1



# 鸭子类型
#
#     不同名类 同名方法啊这是面向对象的语言中多态的传统形式。




# 字符串
#     Unicode字符组成的序列, 用于存储文本数据。


# 字节和字节数组
    # 比特整数组成的序列, 用于存储二进制数据。
    # 含8位 / 比特(bit), 可以存储256(2 ** 8)种不同的值。
    # 出于一些设计目的, ASCII只使用了7位(128种取值)







# 格式化%
    # a = 50
    # b = 1.23456
    # c = "abcdefg"
    #
    # d = "%d %f %s"%(a,b,c)
    # d1 = "%10d %10f %10s"%(a,b,c)  # 指定宽度右对齐格式化格式化
    # d2 = "%-10d %-10f %-10s"%(a,b,c) # 指定宽度左对齐格式化格式化
    # d3 = "%10.4d %10.4f %10.4s"%(a,b,c) # 阶段变量长度为4
    # d4 =  "%*.*d %*.*f %*.*s"%(10, 4, a,10, 4, b,10, 4, c) # 将域宽、字符宽度等设定作为参数
    # print(d)
    # print(d1)
    # print(d2)
    # print(d3)
    # print(d4)
    # # >>>
    # 50 1.234560 abcdefg
    #         50   1.234560    abcdefg
    # 50         1.234560   abcdefg
    #       0050     1.2346       abcd
    #       0050     1.2346       abcd



# 格式化.format()
    # a = 50
    # b = 1.23456
    # c = "abcdefg"
    #
    # d1 = "{} {} {}".format(a,b,c)
    # d2 = "{0} {1} {2}".format(a,b,c)
    # d3 = "{:10} {:10} {:10}".format(a,b,c)
    # d4 = "{:<10} {:<10} {:<10}".format(a,b,c)
    # d5 = "{:^10} {:^10} {:^10}".format(a,b,c)
    # print(d1) # 普通格式化
    # print(d2) # 位置参数格式化
    # print(d3) # 字符宽度格式化
    # print(d4) # 左对齐格式化
    # print(d5) # 居中格式化


# *变量
# def f(a, *b):
#     print(a)
#     print(b)
#     return 1
#
# f(1, 2,3,4)
# >>> 1
    # (2, 3, 4)





# 去除字符串两端内容strip
    # t = '-----hello====='
    # print(t.strip("-="))
    # # >>> hello





# 字符串左对齐右对齐剧中(ljust rjust center)

    # a = 'a'
    # print(a.ljust(5))
    # print(a.rjust(5))
    # print(a.center(5))
    # >>> a
        #     a
        #   a








# 拼接成字符串（join）,print拼接字符串
    # a = [1,2,3,4,5]
    # b = "1"
    # c = "2"
    # print("b".join([str(i) for i in a])) # 列表内元素必须是字符串
    # print(b,c, sep="b")
    # >>> 1b2b3b4b5
        # 1b2




# 小数据池中的内容(is id)
    # 数字小数据池范围(-5~256)
    # 纯文本信息 和存文本信息加下划线，带有特殊字符串的字符串
    # 单一字母 "a"*20时候否在小数据池中，"a"*21是否在小数据池中






# 字符串首字母转为大写(capitalize)

    # a = "hello"
    # print(a.capitalize())
    # >>> Hello



# 字符串全部转换为小写lower

    # a = "aBC"
    # print(a.lower())
    # >>> abc



# 字符串全部换为大写upper

    # a = "abc"
    # print(a.upper())
    # >>> ABC



# 字符串大小写互相转换swapcase

    # a = "aBcD"
    # print(a.swapcase())
    # >>> AbCd




# 字符串"a"在序列中出现的次数(count)
    # 以及第一次出现的索引位置
    # a = "anfhbajjca"
    # print(a.count("a"))




# 判断该字符串是否由字母或数字组成isalnum
    # a = "a3"
    # print(a.isalnum())
    # >>> True




# 判断字符串只有字母组成isalpha
    # a = "abc"
    # print(a.isalpha())
    # >>> True



# 判断字符串只有正整数组成isdigit
    # a= "123"
    # print(a.isdigit())
    # >>> True





# 将字符串转化成bytes类型（bytes）
    #
    # a = "abc123"
    # print(bytes(a, encoding="utf-8"))
    # >>> b'abc123'




# 字符串创建新字节数组(bytearry)
    # a = "abc123"
    # b = bytearray(a, encoding="utf-8")
    # print(b)
    # print(b[0])
    # print(b[0:1])
    # >>> bytearray(b'abc123')
        # 97
        # bytearray(b'a')




# 字符串类型代码的执行（eval,返回结果）简单类型
# a = "print('haha')"
# eval(a)
# >>> haha





# 复杂类型(exec,不返回结果)(执行eval或exec之前可对字符串语句进行编译)
# a = "for i in range(4):print(i)"
# exec(a)
# >>> 0
    # 1
    # 2
    # 3




# 被特殊字符串隔开的英文首字母大写(title)
    # a = "hello world￥hello我world"
    # print(a.title())
    # >>> Hello World￥Hello我World





# 对浮点数,整数进行四舍五入（round）

    # a = 1.3454324
    # b = 15555559
    # print(round(a, 3))
    # print(round(b, -2))
    # >>> 1.345
        # 15555600





# 把十进制分别转换为2进制，8进制，16进制(bin, oct hex)

    # a = 1
    # print(bin(a))
    # print(oct(a))
    # print(hex(a))
    # >>> 0b1
        # 0o1
        # 0x1




# 生成随机整数（random.randint(start,stop)）
    # import random
    # print(random.randint(0,5))
    # >>> 3
    # >>>...





# 整数在内存中占用的二进制码的长度（bit_length）
    # a = 11
    # print(a.bit_length())
    # >>> 1




# 判断出现的值,牢记计算的优先级(()>not>and>or)
    # print(1 and 2)
    # print(2 and 0)
    # print(0 and 3)
    # print(0 or 2)
    # print(2 or 0)
    # print(1 or 2)
    # >>> 2
    # >>> 0
    # >>> 0
    # >>> 2
    # >>> 2
    # >>> 1







# 使用 range() 创建数字列表
    # print(list(range(5)))
    # >>> [0, 1, 2, 3, 4]



# 随机抽取一个元素(random.choine)
    # import random
    # a = [1,2,3,4]
    # print(random.choice(a))
    # >>> 1
    # >>>....




# 随机抽取多个元素(random.sample)
    # import random
    # a = [1,2,3,4,5]
    # print(random.sample(a, 2))
    # >>> [3, 4]
    # >>> ...




# 打乱列表的顺序(random.shuffle)
    # import random
    # a = [1,2,3,4,5]
    # random.shuffle(a)
    # print(a)
    # >>> [3, 1, 4, 2, 5]
    # >>>....


# 对列表进行翻转(reversed)不改变原列表
    # a = [1,2,3,4]
    # print(list(reversed(a)))
    # >>> [4, 3, 2, 1]


# 对列表进行翻转(reverse)改变原列表
    # a = [1,2,3,4]
    # a.reverse()
    # print(a)
    # >>> [4, 3, 2, 1]




# 判断可迭代对象中是否全部是True (all)

    # a = [1,2,3,4]
    # print(all(a))
    # >>> True




# 判断可迭代对象中如果有一个是True，那么就是True（any）

    # a = ['', None, 1]
    # print(any(a))
    # >>> True







# 自动把可迭代对象中元素逐个添加到函数中执行（filter）
    # a = [1,2,3,4]
    # def b(s):
    #     print(s*10)
    # for i in filter(b, a):
    #     print(i)
    # >>> 10
        # 20
        # 30
        # 40






# 不打乱顺序对列表进行去重2

    # a = [1, 5, 2, 1, 9, 1, 5, 10]
    #
    # def b(s):
    #     sets = set()
    #     for i in s:
    #         if not i in sets:
    #             sets.add(i)
    #             yield i
    #         else:
    #             pass
    #
    # print(list(b(a)))
    # [1, 5, 2, 9, 10]








# 从字典中提取值大于200的项
    # a = {'a': 45.23, 'b': 612.78, 'c': 205.55, 'd': 37.20, 'e': 10.75}
    # b = { key:value for key, value in a.items() if value>200}
    # print(b)
    # >>> {'b': 612.78, 'c': 205.55}





# min() 和 max()函数在字典中获取最大最小值
    # a = {'a': 45.23, 'b': 612.78, 'c': 205.55, 'd': 37.20, 'e': 10.75}
    # b = min(i for i in a.values())
    # c = max(i for i in a.values())
    # print(b)
    # print(c)
    # >>> 10.75
        # 612.78





# 使用 sorted() 对字典进行排序
    # a = {'a': 45.23, 'b': 612.78, 'c': 205.55, 'd': 37.20, 'e': 10.75}
    # b = sorted((value,key) for key, value in a.items())
    # c = {key:value for value, key in b}
    # print(c)
    # {'e': 10.75, 'd': 37.2, 'a': 45.23, 'c': 205.55, 'b': 612.78}





# 创建新字典，对可迭代元素"abcd"中的每个元素作为键值进行创建字典，值都相同(fromkeys)

    # a = dict.fromkeys("abcd", 1)
    # print(a)
    # >>> {'a': 1, 'b': 1, 'c': 1, 'd': 1}





# 查找两个字典的相同点（相同的键，相同的值,相同的项）
    # a = {'a':1, 'b':2, 'c':100}
    # b = {'e':200, 'f':100, 'a':300, 'b':2}
    #
    # c = (i for i in a.keys() for j in b.keys() if i == j)
    # d = (i for i in a.values() for j in b.values() if i == j)
    # e = (i for i in a.items() for j in b.items() if i == j)
    # print(list(c))
    # print(list(d))
    # print(dict(e))
    # >>> ['a', 'b']
        # [2, 100]
        # {'b': 2}





# 通过某个关键字排序一个字典列表(sorted,倒序参数reverse=True)
    # rows = [
    #     {'fname':'Brian', 'lname': 'Jones', 'uid': 1003},
    #     {'fname':'David', 'lname': 'Beazley', 'uid': 1002},
    #     {'fname':'John', 'lname': 'Cleese', 'uid': 1001},
    #     {'fname':'Big', 'lname': 'Jones', 'uid': 1004},
    # ]
    #
    # print(sorted(rows, key=lambda x:x['uid']))






# 枚举方法创建字典(enumerate)

    # b = {}
    # a = ['a', 'b', 'c', 'd', 'e']
    # for i,j in enumerate(a):
    #     b.setdefault(j,i)
    # print(b)
    # >>> {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}






# 序列中出现的元素次数的计数
    # a = ['why','are','you','not','eyes','looking','in','my','eyes']
    #
    # dic = {}
    # for i in a :
    #     if not dic.get(i):
    #         dic[i] = 1
    #     else:
    #         dic[i] += 1
    # print(dic)
    # >>> {'why': 1, 'are': 1, 'you': 1, 'not': 1, 'eyes': 2, 'looking': 1, 'in': 1, 'my': 1}








# 向集合中添加元素(add)
    # a = {'a', 'b', 'c'}
    # a.add(99)
    # print(a)
    # >>> {'a', 99, 'b', 'c'}




# 随机弹出集合中的元素（pop）
    # a = {'a', 'b', 'c'}
    # b = a.pop()
    # print(b)
    # >>> a
    # >>> ...


# 修改集合中的元素(remove, add)
    # a = {'a', 'b', 'c'}
    # a.remove('c')
    # a.add(99)
    # print(a)
    # >>> {99, 'a', 'b'}



# 查询集合元素(in)
    # a = {'a', 'b', 'c'}
    # print('a' in a)
    # >>> True





# 求集合的交集(&)
    # a = {1,2,3,4,5,6}
    # b = {2,3,5,9,11}
    # print(a&b)
    # >>> {2, 3, 5}



# 求集合的并集（|）
    # a = {1,2,3,4,5,6}
    # b = {2,3,5,9,11}
    # print(a|b)
    # >>> {1, 2, 3, 4, 5, 6, 9, 11}




# 求集合的差集（-）
    # a = {1,2,3,4,5,6}
    # b = {2,3,5,9,11}
    # print(a-b)
    # print(b-a)
    # >>>{1, 4, 6}
    # >>>{9, 11}




# 求集合的反交集（^）
    # a = {1,2,3,4,5,6}
    # b = {2,3,5,9,11}
    # print(a^b)
    # >>> {1, 4, 6, 9, 11}






# 三元表达式
    # print(1) if 2>1 else print(2)
    # >>> 1



# 让函数实参变成可选
    # def f(a,b=""):
    #     if not b:
    #         return a
    #     return a +b
    # print(f(1))
    # print(f(1,2))
    # >>> 1
    # >>> 3




# 匿名函数lambda

    # a = lambda x:x+1
    # print(a(2))
    # >>> 3







# __setitem__
    # 触发条件 （对象[键]=[值]）
    # class A:
    #
    #     def __init__(self, a):
    #         self.a = a
    #
    #     def __setitem__(self, key, value):
    #         self.a[key]=value
    #         return self.a
    #
    # a = A([1,2,3,4])
    # print(a.a)
    # a[1] = 99
    # print(a.a)
    # >>> [1, 2, 3, 4]
    # >>> [1, 99, 3, 4]





# __delitem__
    # 触发条件 （del 对象[key]）
    # class A:
    #
    #     def __init__(self, a):
    #         self.a = a
    #
    #     def __delitem__(self, key):
    #
    #         self.a.pop(key)
    #         return self.a
    #
    # a = A(['a', 'b', 'c', 'd'])
    # del a[2]
    # print(a.a)
    # >>> ['a', 'b', 'd']








# 类的静态方法(@staticmethod)
    # class A:
    #
    #     @staticmethod
    #     def a():
    #         print('我是静态方法')
    # b = A()
    # b.a()
    # A.a()
    # >>> 我是静态方法
    # >>> 我是静态方法





# 创建类方法并通过类调用通过对象调用（@classmethod）
    # class A:
    #
    #     @classmethod
    #     def a(cls):
    #         print('我是类方法')
    #
    # b = A()
    # b.a()
    # A.a()
    # >>> 我是类方法
    # >>> 我是类方法





# 对对象进行反射查询静态变量值（getattr）
    # class A:
    #
    #     a = 123
    #
    # b = A()
    # s = getattr(b,"a")
    # print(s)
    # >>> 123





# 通过反射对类进行添加属性（setattr）
    # class A:
    #
    #     a = 123
    #
    # setattr(A, "b", 456)
    # b = A()
    # print(A.__dict__)






# 通过反射对类进行删除静态变量(delattr)

    # class A:
    #     a = 123
    #
    # delattr(A, "a")
    # print(A.__dict__)





# 创建对象把方法变成伪属性（property）并调用
    # class A:
    #
    #     def __init__(self, a):
    #         self._a = a
    #
    #     @property
    #     def b(self):
    #         return self._a
    # r = A(1)
    # print(r.b)
    # >>> 1





# 对伪属性进行修改@property
    # class A:
    #
    #     def __init__(self, a):
    #         self._a = a
    #
    #     @property
    #     def b(self):
    #         return self._a
    #
    #     @b.setter
    #     def b(self, s):
    #         self._a = s
    #         return self._a
    #
    # a = A(1)
    # a.b = 2
    # print(a.b)
    # >>> 2




# 对伪属性进行删除
    # class A:
    #
    #     def __init__(self, a):
    #         self._a = a
    #
    #     @property
    #     def b(self):
    #         return self._a
    #
    #     @b.deleter
    #     def b(self):
    #         del self._a
    #         return 0
    #
    # r = A(2)
    # del r.b
    # print(r.__dict__)
    # >>> {}





# 判断对象的所属类型（考虑继承关系isinstance,不考虑继承关系type)
#     class A:
#         pass
#     class B(A):
#         pass
#
#     class C(A):
#         pass
#
#     c = C()
#     print(type(c)==type(B))
#     print(isinstance(c, A))






# 判断一个类是不是另一个类的子类（issubclass

    # class A:
    #     pass
    #
    # class B(A):
    #     pass
    #
    # print(issubclass(B, A))
    # >>> True





# 返回当前位置的全部局部变量（locals）

    # c = 1
    # def a():
    #     a = 2
    #     b = 3
    #     print(locals())
    #     return a+b
    # a()




# 返回全部全局变量（globals）

    # c = 1
    # def f():
    #     a = 2
    #     b = 3
    #     return a+b
    # print(globals())
    # >>> {'__name__': '__main__', '__doc__': None, '__package__': None,
    # '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000000001EB06A0>,
    # '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins'
    #  (built-in)>, '__file__': 'test.py', '__cached__': None,
    #  'c': 1, 'f': <function f at 0x00000000005F1EA0>}





# 查看当前对象有哪些属性（dir）

    # class A:
    #     b = 1
    #     def __init__(self, d=''):
    #         self.c = 1
    #         self.d = d
    #
    # a = A()
    # print(dir(a))
    # >>> ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
    # '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
    # '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
    # '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
    # '__subclasshook__', '__weakref__', 'b', 'c', 'd']





# 判断所给的变量是不是可以被调用（callable）
    # def a():
    #     print(0)
    #
    # print(callable(a))
    # >>> True





# 定义借口或抽象基类(abc模块metaclass=ABCMeta,abstractmethod)
    # from abc import ABCMeta, abstractmethod
    # class A(metaclass=ABCMeta):
    # 	@abstractmethod
    # 	def read(self):
    # 		pass
    # 	@abstractmethod
    # 	def write(self):
    # 		pass
    # class B(A):
    # 	def read(self):
    # 		print('rrrr')
    # 	def write(self):
    # 		print('wwww')
    # b = B()


# 类()做的事情
    # 1 开辟一个属于对象的空间
    # 2 把对象空间传给self， 执行__init__方法
    # 3 将这个对象空间返回给调用者
    # class A:
    #     def __new__(cls, *args, **kwargs): # cls传递的类空间
    #         obj = super().__new__(cls)  # 创建了对象的空间
    #         print(obj)  # 内存地址和__init__中的地址相同
    #         return obj  # 返回给了 __init__的self
    #     def __init__(self):
    #         print(self) # 内存地址和__new__中的地址相同
    # 可以通过指针找到类的空间中的内存
    # 对象本身内部也存储了一些只属于对象的属性
    # A()


# 类名空间的查询顺序
    # 对象.属性
    # 先从对象空间查找，如果没找到，去类空间中去找，在找不到，去父类空间中查找
    # 通过对象，不能改变,只能引用类中的静态变量（不是绝对可变类型静态变量除外）
    # 对象与对象之间是互相独立的
    # 通过对象访问类中的静态变量原理
        # class Person:
    #
    #     animal = '高级动物'
    #     soup = '有灵魂'
    #
    #     def __init__(self, country, name):
    #
    #         self.country = country
    #         self.name = name
    #
    #     def eat(self):
    #
    #         print('{name}在吃饭...'.format(name=self.name))
    #
    #
    # p1 = Person('中国', 'alex')
    # 程序运行 1 走到 class Person  在内存中创建了名为Person的类空间内存
    #  2  走到 animal, soup 在Person类空间中创建了 变量animal = '高级动物' soup = '有灵魂'
    #  3 走到__init__ ,在Person类空间中创建了函数的内存地址
    #  4 走到 def eat 在Person类空间内存地址中创建了 eat函数地址
    #  5 走到p1 = Person('中国', 'alex') 先执行等号右边
    #     Person() 在内存中创建了Person的实例对象的空间，自动执行__init__方法
    #     ，将创建的空间地址self自动传入__init__中， 并在person的实例对象空间内存中，创建了
    #     属性， country='中国'， name='alex' 并且在实力对象空间内存中创建了
    #     指示牌（类对象指针），然后创建变量p1指向person实例对象空间
    #     正因为有了这个类对象指针，所以p1.mind 先在实例对象中查找，实例对象中没有，就通过类对象指针到类中查找, 所以能通过 对象.静态变量 能访问类中的静态变量






# 编辑手动遍历迭代器迭代

    # def a(n):
    #     b = (i for i in range(n))
    #     while True:
    #         try:
    #             s = next(b)
    #             print(s)
    #         except StopIteration:
    #             break
    # a(5)
    # >>> 0
        # 1
        # 2
        # 3
        # 4







# 判断是否存在该文件os.path.exists
    # import os
    # print(os.path.exists('test.py'))
    # >>> True




# 获取当前文件名sys.argv[0]
    # import sys
    # print(sys.argv[0])
    # >>> test.py




# 获取当前文件的绝对路径,不包括文件名os.getcwd()
    # import os
    # print(os.getcwd())
    # >>> D:\git-warehouse\learn_notes




# 获取文件绝对路径包括文件名os.path.abspath
    # import os
    # print(os.path.abspath('test.py'))
    # >>> D:\git-warehouse\learn_notes\test.py




# 获取绝对路径最后一项文件名os.path.basename
    # import os
    # path = "D:\\git-warehouse\\learn_notes\\test.py"
    # print(os.path.basename(path))
    # >>> test.py





# 判断是否是文件os.path.isfile
    # import os
    # print(os.path.isfile("test.py"))
    # >>> True



# 判断是否是目录os.path.isdir
    # import os
    # print(os.path.isdir("test.py"))
    # >>> True




# 获取文件当前文件大小os.path.getsize
    # import os
    # print(os.path.getsize("test.py"))
    # >>> 4824



# 获取文件的修改日期os.path.getmtime
    # import os
    # print(os.path.getmtime("test.py"))
    # >>> 1557472955.7581878





# 修改文件操作（打开文件将文件内容修改， 写入另一个文件，删除原文件，将另一个文件名字改成原文件名字）





# 将数据转换成json格式json.dumps
    # import json
    # a = {"a":"1"}
    # print(json.dumps(a))
    # >>> {"a": "1"}



# 读取json格式数据
    # import json
    # a = {"a":1}
    # b = json.dumps(a)
    # print(json.loads(b))
    # >>> {'a': 1}





# 对文件夹进行遍历

    # import os
    #
    # def test(file_path, n):
    #     file_list = os.listdir(file_path)
    #
    #     for filename in file_list:
    #
    #         if os.path.isdir(os.path.join(file_path, filename)):
    #             print('\t' * n, filename + '目录')
    #             test(os.path.join(file_path, filename), n+1)
    #
    #         else:
    #             print('\t'*n, filename + '文件')
    #
    #
    # test(os.getcwd(), 0)






# 万能的异常处理
    # try:
    #     print(1/0)
    # except:
    #     print("截获异常")
    # >>> 截获异常


# 主动抛出一个异常

    # class A(BaseException):
    #     pass
    #
    # raise A
    # >>> raise A







# json对字典进行dumps
    # import json
    # a = {"a": "1"}
    # print(json.dumps(a))
    # >>> {"a": "1"}



# json对列表进行dumps
    # a = [1, 2, 3]
    # print(json.dumps(a))
    # >>> [1, 2, 3]



# json对字符串进行dumps
    # a = "123abc"
    # print(json.dumps(a))
    # >>> "123abc"



# json对元祖进行dumps
    # a = ("a", "b")
    # print(json.dumps(a))
    # >>> ["a", "b"]



# json对True, False进行dumps
    # a = True
    # b = False
    # print(json.dumps(a))
    # print(json.dumps(b))
    # >>> true
    # >>> false



# json对False进行dumps

    # a = {"a":1,"b":[1,2,3],"c":(3,4,5),"d":True,"e":False,"f":"fff"}
    # import json
    # def test(s):
    # 	r = json.dumps(s)
    # 	return r
    # print(test(a))




# json对中文进行处理ensure_ascii=False
    # a = "您好"
    # print(json.dumps(a, ensure_ascii=False))
    # >>> "您好"




# 二分查找算法

    # a = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18]
    #
    # def test(n):
    #     head = 0
    #     end = len(a)-1
    #     while head <= end:
    #         mid =(end+head)// 2
    #         if n < a[mid]:
    #             end = mid-1
    #         elif n > a[mid]:
    #             head = mid + 1
    #         else:
    #             print('找到位置', n)
    #             break
    #     else:
    #         print('没找到')
    # test(17)







# 匹配配数字的表达式（\d [0-9]）
    # a = "123a"
    # b = re.match("\d+", a)
    # print(b.group())
    # >>> 123



# 匹配数字字母或下划线的表达式（\w [0-9A-Za-z_]）
    # a = "123_a$"
    # b = re.match("\w+", a)
    # print(b.group())
    # >>> 123_a



# 匹配回车或空格（\s）
    # a = "\n123\t333 444"
    # b = re.match("\s+", a)
    # print(b.group())
    # >>>



# 匹配非数字（\D）
    # a = "adb 132$fg"
    # b = re.match("\D+", a)
    # print(repr(b.group()))
    # >>>'adb '



# 匹配非数字字母下划线(\W)
    # a = "$&*#)#$_#$"
    # b = re.match("\W+", a)
    # print(repr(b.group()))
    # >>> '$&*#)#$'



# 匹配非空白（\S）
    # a = "$&*#)#$_#$"
    # b = re.match("\W+", a)
    # print(repr(b.group()))
    # >>> '$&*#)#$'





# 匹配字符串开始（^）
    # a = "abc123"
    # b = re.match("^a\w+", a)
    # print(repr(b.group()))
    # >>> 'abc123'




# 匹配字符串结尾（$）
    # a = "abc123c"
    # b = re.match("\w+$", a)
    # print(repr(b.group()))
    # >>>'abc123c'




# 匹配a或则b（|）
    # a = "abc123c"
    # b = re.match("b|a", a)
    # print(repr(b.group()))
    # >>> 'a'



# 非字符组的运用([^xxx])
    # a = "abc123c"
    # b = re.match("[^bc]", a)
    # print(repr(b.group()))
    # >>> a



# 转义字符的运用（\）
    # a = "[abc123c"
    # b = re.match("\[", a)
    # print(repr(b.group()))
    # >>> '['




# 使用量词{}运用匹配
    # a = "abfgf34"
    # b = re.match("\w{3}", a)
    # print(repr(b.group()))
    # >>> 'abf'




# 使用量词？ 匹配0次或者一次运用
    # a = "abfgf34"
    # b = re.match("\w?", a)
    # print(repr(b.group()))
    # 'a'




# 使用量词+ 匹配一次或多次运用
    # a = "abfgf34"
    # b = re.match("\w+", a)
    # print(repr(b.group()))
    # >>> 'abfgf34'




# 使用量词* 匹配0次或多次运用
    # a = "aft123z#$"
    # b = re.match("\w*", a)
    # print(repr(b.group()))
    # >>> 'aft123z'




# 取消贪恋匹配运用（量词？）
    # a = "aft123z#$"
    # b = re.match("\w*?", a)
    # print(repr(b.group()))
    # >>> ""




# .*?x 匹配任意字符串直到找到x的运用
    # a = '1324safw2334'
    # b = re.match('.*?w', a)
    # print(repr(b.group()))
    # >>> '1324safw'



# 分割字符串(re.split)
    # a = '1324sa fw2334\t'
    # b = re.split('\s', a)
    # print(repr(b))
    # >>> ['1324sa', 'fw2334', '']




# 捕获分组获取分组中值（()）
    # a = 'asdf fjdk; afed, fjek,asdf, foo'
    # b = re.split('(,|;|\s+)', a)
    # print(b)
    # ['asdf', ' ', 'fjdk', ';', '', ' ', 'afed', ',', '', ' ', 'fjek', ',', 'asdf', ',', '', ' ', 'foo']



# 不保留捕获分组（(?:)）
    # a = 'asdf fjdk; afed, fjek,asdf, foo'
    # b = re.split('(?:,|;|\s)\s*', a)
    # print(b)
    # >>> ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']






# startswith()
    # a = "qerzf"
    # print(a.startswith("q"))
    # >>> True





# endswith()
    # a = "qerzf"
    # print(a.endswith("f"))
    # >>> True





# 查找字符串 (find)
    # a = "fslagaglagpythonsafsfsdtw."
    # print(a.find("python"))
    # >>> 10




# 查找字符串 (re.findall)
    # a = "fslagaglagpythonsafsfsdtw."
    # b = re.findall("python", a)
    # print(b)
    # >>> python




# 匹配字符串中""中的内容1(.+)
    # a = 'a says "no."'
    # b = re.findall('\"(.+)\"', a)
    # print(b)
    # >>> ['no.']



# 匹配字符串中""中的内容2(.*?)
    # a = 'a says "no." b says "yes."'
    # b = re.findall('\"(.*?)\"', a)
    # print(b)
    # >>> ['no.', 'yes.']





# 对多行进行匹配(\n)
    # a = '''/* this is a
    # multiline comment */
    # '''
    # b = re.findall("\* ((?:.|\s)*) \*" , a)
    # print(b)
    # >>> ['this is a\nmultiline comment']




# 编译匹配模式匹配字符串(编译就是速度更快)
    # a = "abc123"
    # b = re.compile('[a-z]+')
    # print(b.match(a).group())
    # >>> 'abc'


# 替换字符串的内容（re.sub）
    # a = "python"
    # b = re.sub("o", r'999', a)
    # print(b)
    # >>> pyth999n




# 将字符串中的日期匹配进行捕获分组,然后进行模式替换(re.sub)
    # a = "2013/13/23"
    # b = re.sub('(\d+)/(\d+)/(\d+)', r'\3-\2-\1', a)
    # print(b)
    # >>> 23-13-2013




# 替换字符串返回之后的字符串和替换次数（re.subn）
    # a = 'abacbd'
    # b = re.subn("a", r'999', a)
    # print(b)
    # >>> ('999b999cbd', 2)



# 字符串忽略大小写,把字符串python替换成aaaa（flagS = re.IGNORECASE）
    # a = "abAb"
    # b = re.sub("a", r'999', a, flags=re.IGNORECASE)
    # print(b)
    # >>> 999b999b










# 创建包
# 创建普通目录 目录创建__init__.py文件 即构成包
# from ttt.t4 import t4
# t4()
# >>> 我是t4


# 限制from xxx import * 可以导入的函数
# 包的函数文件中 __all__['方法名', ...]
# from ttt.t4 import *
# t2()
# t4()
# >>> 我是t4
# >>> NameError: name 't4' is not defined


# 获取计算机最大整型范围（sys.maxsize）
# a = sys.maxsize
# print(a)
# >>> 9223372036854775807


# 获取python解释器版本信息（sys.version）
# print(sys.version)
# >>> 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)]


# 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值（sys.path）
# print(sys.path)
# >>> ['D:\\git-warehouse\\learn_notes', 'D:\\git-warehouse\\learn_notes\\notes\\Scripts\\python36.zip', 'C:\\Users\\Adm
# inistrator\\AppData\\Local\\Programs\\Python\\Python36\\DLLs', 'C:\\Users\\Administrator\\AppData\\Local\\Programs
# \\Python\\Python36\\lib',...']


# 显示当前环境加载了哪些模块(sys.modules)
# print(sys.modules)
# >>> {'builtins': <module 'builtins' (built-in)>, 'sys': <module 'sys' (built-in)>, '_frozen_importlib': <module '_froz
# en_importlib' (frozen)>, '_imp': <module '_imp' (built-in)>, '_warnings': <module '_warnings' (built-in)>, '_threa
# d': <module '_thread' (built-in)>, '_weakref': <module '_weakref' (built-in)>, '_frozen_importlib_external': <modu
# le '_frozen_importlib_external' (frozen)>, '_io': <module 'io' (built-in)>, 'marshal': <module 'marshal' (built-in
# ......}


# 返回操作系统平台名称(sys.platform)
# print(sys.platform)
# >>> win32


# 获取文件名和获取文件执行时候添加的参数(sys.argv)
# print(sys.argv)
# 执行命令为python test.py a
# >>> ['test.py', 'a']


# 退出程序（sys.exit(0)正常退出， 错误退出sys.exit(1)）
# sys.exit(0)
# sys.exit(1)


# 获取执行当前文件所在目录绝对路径（os.getcwd）
# print(os.getcwd())
# >>> D:\git-warehouse\learn_notes


# 改变当前文件的工作目录(os.chdir)
# os.chdir('..')
# print(os.getcwd())
# >>> D:\git-warehouse


# 创建多级目录（os.makedirs('xx', exist_ok=True)若目录存在则不创建）
# os.makedirs("a/b")


# 创建单级目录（os.mkdir）
# os.mkdir("c")


# 删除目录或文件 （os.rmdir 目录不为空不能删除）
# os.rmdir("a/b")


# 删除文件（os.remove）
# os.remove("111.txt")


# 重命名文件目录(os.rename)
# os.rename("a", "aa")


# 查看文件信息(os.stat)
# print(os.stat("aa"))
# >>> os.stat_result(st_mode=16895, st_ino=4503599627453343, st_dev=1277853839, st_nlink=1, st_uid=0, st_gid=0, st_size=
# 0, st_atime=1557636355, st_mtime=1557636355, st_ctime=1557636303)


# 查看当前系统的目录分隔符(os.sep)
# print(os.sep)
# >>> \


# 查看当前系统使用的行终止符文（os.linesep）
# print(repr(os.linesep))
# >>> '\r\n'


# 查看用于分割文件的字符串(os,pathsep)
# print(repr(os.pathsep))
# >>> ;


# 查看到那个前使用平台(os.name)
# print(os.name)
# >>> nt


# 查看环境变量(os.environ)
# print(os.environ)
# >>> environ({'NUMBER_OF_PROCESSORS': '4', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'SESSIONNAME': 'Con
# sole', 'COMPUTERNAME': 'USER-20190322AY', '__INTELLIJ_COMMAND_HISTFILE__': 'C:\\Users\\Administrator\\.PyCharm2019
# .1\\config\\terminal\\history\\history-1', 'SYSTEMDRIVE': 'C:', 'LOGONSERVER': '\\\\USER-20190322AY', 'USERDOMAIN'
# : 'USER-20190322AY', .....})






# 使用队列应用（queue.Queue qsize put get）
    # import queue
    # q = queue.Queue()
    # q.put(1111)
    # q.put(2222)
    # print(q.qsize())
    # print(q.get())
    # >>> 2
    # >>> 1111






# 获取当前时间戳 格林威治时间（time.time）
    # print(time.time())
    # >>> 1557638022.4267287




# 获取当前结构化时间(time.localtime())
    # print(time.localtime())
    # >>> time.struct_time(tm_year=2019, tm_mon=5, tm_mday=12, tm_hour=13, tm_min=14,
    #                  tm_sec=44, tm_wday=6, tm_yday=132, tm_isdst=0)








# 小校验文件的一致性（原理 对文件进行读取 进行加密 对加密后的文件进行比较）
    # import hashlib
    # def hash_file(path_file):
    #     h = hashlib.md5()
    #     with open(path_file, "r", encoding="utf-8") as f:
    #         s = f.read()
    #     h.update(s.encode("utf-8"))
    #     r = h.hexdigest()
    #     return r
    #
    # r1 = hash_file("a.txt")
    # r2 = hash_file("b.txt")
    #
    # print(r1==r2)
    # >>> True





# 超大文件一致性校验（对同一个字符串分段进行加密，最后得到结果跟一次性进行加密的结果一样）

    # import hashlib
    # def hash_file(path_file):
    #     h = hashlib.md5()
    #     with open(path_file, "r", encoding="utf-8") as f:
    #         [h.update(i.encode("utf-8")) for i in f]
    #     r = h.hexdigest()
    #     return r
    #
    # r1 = hash_file("a.txt")
    # r2 = hash_file("b.txt")
    # print(r1==r2)
    # >>> True






# 分别对日志的分级进行应用（
# # logging.debug('debug message')       # 调试信息
# # logging.info('info message')         # 基础信息模块
# # logging.warning('warning message')   # 警告
# # logging.error('error message')       # 错误
# # logging.critical('critical message') # 严重错误）




# 日志的对象配置型应用（原理：
# # 1 创建一个logger对象(导入logging模块 对象logging.getLogger())
# # 2 创建一个文件管理操作符（如果要输入文件中 logging.FileHandler('1111.log', encoding='utf-8')）
# # 3 创建一个屏幕管理操作符（如果钥输出到屏幕sh = logging.StreamHandler()）
# # 4 创建一个日志输出格式 format1 = logging.Formatter()
# # 5 给文件管理符绑定一个格式 sh.setFormatter(format1)
# # 6 给屏幕操作管理符绑定一个格式 fh.setFormatter(format1)
# # 7 给logger对象绑定文集管理操作符l.addHandler(fh)
# # 8 给logger对象绑定屏幕管理操作符l.addHandler(sh)
# # l.debug('logger debug message')
# # l.info('logger info message')
# # l.warning('logger warning message')
# # l.error('logger error message')
# # l.critical('logger critical message')
# # print('hahah')
# # 参数：logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有：
# # filename：用指定的文件名创建FiledHandler，这样日志会被存储在指定的文件中。
# # filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
# # format：指定handler使用的日志显示格式。
# # datefmt：指定日期时间格式。
# # level：设置rootlogger（后边会讲解具体概念）的日志级别
# # stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件(f=open(‘test.log’,’w’))，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。
# # format参数中可能用到的格式化串：
# # %(name)s Logger的名字
# # %(levelno)s 数字形式的日志级别
# # %(levelname)s 文本形式的日志级别
# # %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
# # %(filename)s 调用日志输出函数的模块的文件名
# # %(module)s 调用日志输出函数的模块名
# # %(funcName)s 调用日志输出函数的函数名
# # %(lineno)d 调用日志输出函数的语句所在的代码行
# # %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
# # %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
# # %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# # %(thread)d 线程ID。可能没有
# # %(threadName)s 线程名。可能没有
# # %(process)d 进程ID。可能没有
# # %(message)s用户输出的消息）






# 同时打开两个文件
# with open('a.txt', 'r') as f1, open('b.txt', 'r') as f2:
# 	print(f1.read())
# 	print(f2.read())





# 用json向文件中写入中文
# import json
# with open("a.txt", "w", encoding="utf-8")as f:
#     a = "哈啊"
#     json.dump(a, f, ensure_ascii=False)






# 多次dump数据到文件里，不能能用load读出来，若读不出来有什么办法(dumps write\n loads)
# import json
# with open("a.txt", "w", encoding="utf-8")as f:
#     a = "a1111"
#     b = "a2222"
#     a1 = json.dumps(a)
#     a2 = json.dumps(b)
#     f.write(a+"\n")
#     f.write(b+"\n")



# 生成0到1范围内均匀分布的浮点数（random.random）
    # import random
    # s = random.random()
    # print(s)
    # >>> 0.08932539466574718
    # >>> ...







# 删除字典中的元素（pop del）
    # a = {"a":1, "b":2, "c":3}
    # a.pop("b")
    # del a["c"]
    # print(a)
    # {'a': 1}





# 执行系统命令返回输入命令的结果(os.popen() .read())
    # import os
    # print(os.popen("dir").read())
    # >>> 2019/05/12  15:10    <DIR>          .
        # 2019/05/12  15:10    <DIR>          ..
        # ....




# 求绝对值 （abs）
    # a = -1
    # b = 1
    # print(abs(a))
    # print(abs(b))
    # >>> 1
    # >>> 1




# 求次幂(pow)
    # print(pow(2,3))
    # >>> 8






# __eq__

    # 触发条件(对象1=对象2)
    # class A:
    # 	def __eq__(self, s):
    # 		print('触发了__eq__')
    # a = A()
    # b = A()
    # a == b
    # >>> __eq__



# __hash__
    # 触发条件（把对象添加到集合字典等中触发）












# with 语句执行过程
    # 语句的时候,对象的 __enter__() 方法被触发,
    # 它返回的值 (如果有的话) 会被赋值给as 声明的变量。
    # 然后,with 语句块里面的代码开始执行。最后,__exit__() 方法被触发进行清理工作

    # class A:
    # 	def __enter__(self):
    # 		print("with 对象 触发__enter__方法")
    # 		return "haha"
    #
    #   # __exit__() 方法的第三个参数包含了异常类型、
    # 	# 异常值和追溯信息 (如果有的话)
    # 	def __exit__(self,c,d,e):
    # 		print(c,d,e)
    # 		print("最后的清理工作")
    #
    # a = A()
    # with a as b:
    # 	print(b)
    # >>> with 对象 触发__enter__方法
        # haha
        # None None None
        # 最后的清理工作





# __mro__
    # 查找 类的继承顺序
    # class A:
    # 	pass
    #
    # class B(A):
    # 	pass
    #
    # print(B.__mro__)
    # (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)











# 数据结构堆

# 堆就是用数组实现的二叉树，所有它没有使用父指针或者子指针。
# 堆根据“堆属性”来排序，“堆属性”决定了树中节点的位置
# import heapq
# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(3, nums)) # 获取列表最大值的3个之 按倒叙排列
# print(heapq.nsmallest(3, nums)) # 获取列表最笑值的3个之 按升序排列
#
# heapq.heapify(nums) # 获取队列中最小值
# print(nums[0])
# >>> [42, 37, 23]
# [-4, 1, 2]
# -4


# 不改变原序列，进行合并排序（序列必须是排过序的）

# 有一点要强调的是 heapq.merge() 需要所有输入序列必须是排过序的。特别的,
# 它并不会预先读取所有数据到堆栈中或者预先排序,也不会对输入做任何的排序检测。
# 它仅仅是检查所有序列的开始部分并返回最小的那个,这个过程一直会持续直到所有
# 输入序列中的元素都被遍历完。
# import heapq
# a = [1, 4, 7, 10]
# b = [2, 5, 6, 11]
# for i in heapq.merge(a,b):
# 	print(i)


# 把字符串按照换行符进行分割到列表中返回splitlines()
# text = """
# 1123
# fsdafgasg
# cszvvbb
#
# fasdfsdaf
# """
# print(text.splitlines())
# ['', '1123', 'fsdafgasg', 'cszvvbb', '', 'fasdfsdaf']


# 一个自定义分页的脚本

# import sys
# def more(text, numlines=10):
# 	lines = text.splitlines() # 返回一个在换行符处分割后得到的字符串组成的列表
# 	while lines:
# 		a = lines[:numlines]
# 		b = lines[numlines:]
# 		for line in a:
# 			print(line)
# 		if lines and input("显示更多?") not in ["y", "Y"]:
# 			break

# if __name__ == '__main__':
# 	more(open(sys.argv[1]).read(),10)


# 查看对象引用次数getrefcount(x)
# import sys
# a = "22222fsafsagas"
# print(sys.getrefcount(a))
# >>> 4


# 可执行程序内置模块名称
# import sys
# print(sys.builtin_module_names)
# >>> ('_ast', '_bisect', '_blake2', '_codecs', ......)


# 异常的详细信息exc_info[0],exc_info[1]
# import sys
#
# import traceback
# try:
# 	print(1/0)
# except:
# 	exc_info = sys.exc_info()
# 	print(exc_info[0]) # 异常类
# 	print(exc_info[1]) # # 异常
# 	traceback.print_tb(exc_info[2]) # 异常详细信息
# >>> <class 'ZeroDivisionError'>
# division by zero
#   File "test.py", line 104, in <module>
#     print(1/0)


# 获取终端窗口大小os.get_terminal_size()
# import os
# print(os.get_terminal_size())
# os.terminal_size(columns=114, lines=9)


# 获取 os,sys属性个数dir(sys),dir(os),dir(os.path)
# import sys, os
# print(len(dir(sys))) # 83个属性
# print(len(dir(os)))  # 152
# print(len(dir(os.path))) # 嵌套在os里的一个模块 57


# 负责程序间通信os.pipe()
# import os
# print(os.pipe())
# >>>(3, 4)


# 标准流输入输出接口（sys.stdin, sys.stdout, sys.stderr）
# import sys
# for i in (sys.stdin, sys.stdout, sys.stderr):
# 	print(i)
# >>> <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>
# <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
# <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>


# 输出标准流(sys.stdout.write)
# import sys
# print("haha")
# sys.stdout.write("haha")
# >>> haha
# haha


# 输入标准流sys.stdin.readline

# s = input("hello stdin world:")
# print(s)

# print("hello stdin world:")
# print(repr(sys.stdin.readline()))


# 重定向流到文件或程序
# def test():
# 	print("hello world")
# 	while True:
# 		try:
# 			s = input("输入一个数字:")
# 		except EOFError:
# 			break
# 		else:
# 			num = int(s)
# 			print("%d的平方是%d"%(num,num**2))
# 	print("bye!")
# test()


# 利用shell语法 <filename 把标准输入流重定向到文件输入
# 标准输出也可以利用shell语法 > filename 重定向到文件中
# 输入输出的重定向
# python xxx.py < input.txt > output.txt


# 用管道(pipe)链接程序
# 子啊两个命令间使用shell字符"|",可以将一个程序的标准
# 输出发送到另一个程序的标准输入
# def test():
# 	print("hello world")
# 	while True:
# 		try:
# 			s = input("输入一个数字:")
# 		except EOFError:
# 			break
# 		else:
# 			num = int(s)
# 			print("%d的平方是%d"%(num,num**2))
# 	print("bye!")
# test()
# python3 test.py < cats.txt | more
# 标准输入来自文件cats.txt, 输出被发送到另一个程序more
# 一个标准的命令行分页程序


# 一个python脚本的输出可以哟个管道发送作为另一个python脚本的输入
# cat cats.py
# print("我是cats.py文件")
# print(42)
# cat dogs.py
# import sys
# print("找到:%s"%input())
# data = sys.stdin.readline()[:-1]
# print("dogs.py", data, int(data)*2)

# python3 cats.py | python3 dogs.py
# dogs.py 从cats.py 得到输入


# 标准流上的排序和求和
# cats.py
# import sys
# lines = sys.stdin.readlines()
# print(lines)
# lines.sort()
# for i in lines:
# 	print(i, end="")

# dogs.py
# import sys
# s = 0
# while True:
# 	try:
# 		line = input()
# 	except EOFError:
# 		break
# 	else:
# 		s += int(line)
# print(s)

# data.py
# 123
# 000
# 999
# 042

# python3 cats.py < data.py ;
# ['123\n', '000\n', '999\n', '042\n']
# 000
# 042
# 123
# 999

# python3 dogs.py < data.py
# 1164

# 版本二
# for i in (123,0,999,42):
# 	print("%03d"%i)

# import sys
# for line in sorted(sys.stdin):
# 	print(line,end="")

# import sys
# print(sum(int(i) for i in sys.stdin))

# python3 write1.py | python3 cats.py | python3 dogs.py


# 重定向流到python对象?
# import sys

# class Output:

# 	def __init__(self):
# 		self.text = ""

# 	def write(self, string):
# 		self.text += string

# 	def writelines(self, lines):
# 		for line in lines:
# 			self.write(line)


# class Input:

# 	def __init__(self, input=""):
# 		self.text = input

# 	def read(self, size=None):
# 		if size == None:
# 			res, self.text = self.text, ""
# 		else:
# 			res, self.text= self.text[:size], self.text[size:]
# 		return res

# 	def readline(self):
# 		eoln = self.text.find("\n")
# 		if eoln == -1:
# 			res, self.text = self.text, ''

# 		else:
# 			res. self.text = self.text[:eoln+1], self.text[eoln+1:]
# 		return res
# def redirect():
# 	savestreams = sys.stdin,sys.stdout
# 	sys.stdin = Input(input)
# 	sys.stdout = Output()
# 	try:
# 		result = function(*pargs, **kargs):
# 		output = sys.stdout.text
# 	finally:
# 		sys.stdin, sys.sydout = savestreams
# 	return (result, output)


# print调用中的重定向语法
# print("xxxx", file=filename)


# 用os.popen重定向如数或输出
# import os
# a = os.popen("python3 cats.py")
# print(a.read())
# print(a.close()) # 推出状态:None是好的


# import os
# a = os.popen("python3 cats.py", "w")
# a.write("9999999\n")?
# a.close()
# print(open("dogs.py").read()) # output传送到某个文件


# 利用subprocess重定向输入输出
# from subprocess import Popen, PIPE, call

# 直接调用命令call方法
# s = call("python3 cats.py", shell=True)
# print(s)

# 输出
# p = Popen("python3 cats.py",shell=True, stdout=PIPE)
# print(p.communicate()) # stdout,stderr
# print(p.returncode)   # 退出状态


# p = Popen("python3 cats.py", shell=True,stdin=PIPE, stdout=PIPE)
# p.stdin.write(b"hahahahah\n") # 向管道中写入
# p.stdin.write(b"eeeeeeee\n")
# p.stdin.close()
# output = p.stdout.read() # 读取管道中的值
# print(output)
# cat cats.py
#
# import sys
# s1 = sys.stdin.readlines()
# print(s1)


# pickle模块
# import pickle
# f = open("cats.txt", 'wb')
# pickle.dump([1,2,3,4], f)
# pickle.dump("hello", f)
# pickle.dump({"a":1, "b":2},f)
# f.close()

# f1 = open("cats.txt", "rb")
# try:
# 	while True:
# 		print(pickle.load(f1))
# except:
# 	pass


# shelves模块
# 如果想用键来访问记录,python提供了更高层次的工具 shelves
# shelve系统自动分隔存储记录,并将值获取和更新被访问和修改的







# c / s架构以及优势（client和server
#     即客户端和服务器
#     优势：能够发挥pc性能）
#
#
# b / s架构以及优势（browser和server
#
#     浏览器和服务器
#     b / s架构隶属于c / s架构
#     优点： 统一了应用的接口）


# mac地址
#     (是一个物理地址，全球唯一(网卡))



# ipv4地址
# （是一个四位点分十进制，它表示了计算机在网络中的位置）



# 公网的ip作用
#     （连接外网）




# 内网作用
#     (因为ip地址不够)




# 交换机的通信方式
#     （广播：发送到网络中单播：
#     1对1发送组播：1对多发送）




# arp协议（
#     通过目标ip地址获取目标mac地址的一个协议）




# 端口
#     （操作系统为本机商每个运行的程序都随机分配一个端口，其他
#     电脑上的程序可以通过端口获取到这个程序）





# 确定电脑上运行程序
#     （通过ip地址 + 端口
#     能唯一找到电脑上的一个服务程序）





# 路由器
#     （连接不同的网段叫路由）




# 网关
#     （类似于一个局域网的出口和入口）




# 网段
#     （一个局域网内的ip地址范围网段 = ip（2进制） & 子网掩码（255, 255, 255, 0的2进制））
#




# 网桥
#     （跨网段传输数据）





# 回环地址
    #（127.0.0.1发送信息返回计算机计算机 - --------> 127.0.0.1 - -------->计算机）


# 路由器与交换机的区别（
#     路由器
#         路由器的主要功能是进行跨网段进行数据传输，
#         路由是动词：找寻最佳路径
#         如果你只有一个外网ip，但是有好多台电脑需要上网，用路由器即可
#     交换机
#         交换机的主要功能是组织局域网，经过交换机内部处理解析信息之后，将信息以点对点，点对多的形式，发送给固定端
#         如果需要将多态电脑链接到一根网线，用交换机即可）




# 互联网协议osi五层模型
    # 应用层
    #     http, https, ftp
    # 传输层
    #     tcp / udp
    #     四层交换机和四层路由器
    # 网络层
    #     ip协议
    #     路由器三层交换机
    # 数据链路层
    #     arp协议
    #     以太网交换机
    #     网卡
    #     网桥
    # 物理层
    #     传输电信号
    #     集线器
    #     网线
    #     光纤





# 通信的分类（
#     1同一台电脑程序通信：带来一个py文件
#     2两个电脑的通信：连一个网线
#     3多个电脑通信：电脑1要找电脑2, 先发送一个请求帧，交给交换机
#         交换机以广播形式给除了电脑1之外所有机器，电脑2接收到消息后，
#         以单播形式回复给交换机，在回复给电脑）





# socket
    # Socket是应用层与TCP/IP协议族通信的中间软件抽象层，它是一组接口。在设计模式中，
    # Socket其实就是一个门面模式，它把复杂的TCP/IP协议族隐藏在Socket接口后面，对用户来说，
    # 一组简单的接口就是全部，让Socket去组织数据，以符合指定的协议。
    # 套接字是计算机网络数据结构,它体现了上节中所描述的“通信端点”的概念
    # 在任何类型的通信开始之前,网络应用程序必须创建套接字





# socket的类型分类（
    # 基于文件的和面向网络的
    # 因为两个进程运行在同一台计算机上,所以这些套接字都是基于文件的,这意味着文件
    # 系统支持它们的底层基础结构
    # 第二种类型的套接字是基于网络的,它也有自己的家族名字 AF_INET,
    # 面向链接的套接字
        # 面向连接的,这意味着在进行通信之前必须先建立一个连接
        # 面向连接的通信提供序列化的、可靠的和不重复的数据交付,而没有记录边界。这基本
        # 上意味着每条消息可以拆分成多个片段,并且每一条消息片段都确保能够到达目的地,然后
        # 将它们按顺序组合在一起,最后将完整消息传递给正在等待的应用程序
        # 实现这种连接类型的主要协议是传输控制协议(更为人熟知的是它的缩写 TCP)。为 了
        # 创建 TCP 套接字 ,必须 使用 SOCK_STREAM 作 为套接 字类型
    # 面向无链接的套接字
        # 无连接的套接字。这意味着,在通信开始之前并不需要建立连接
        # 在数据传输过程中并无法保证它的顺序性、可靠性或重复性。
        # 然而,数据报确实保存了记录边界,这就意味着消息是以整体发送的
        # 实现这种连接类型的主要协议是用户数据报协议(更为人熟知的是其缩写 UDP)
        # 。为 了创建 UDP 套接字,必须使用 SOCK_DGRAM 作为套接字类型


# 进程池(同步做任务apply)

# 是指让进程池中的进程，同步的帮你做任务,
# 同步处理着100个任务，同步是值，哪怕进程池中有5个进程，也依旧是一个进程一个进程的取执行任务，

# from multiprocessing import Pool
# import time
#
# def func(num):
#     num += 1
#     return num
#
#
# if __name__ == '__main__':
#
#     p = Pool(5)
#
#     for i in range(100):
#         res = p.apply(func, args=(i,))
#         print(res)


# 进程池(异步做任务apply_async)

# 是指让进程中的进程，异步的帮你做任务进程池中有5个进程，
# 一次性就处理5个任务， 接下来哪个进程处理完任务了就马上取接受下一个任务异步处理任务时
# 进程池中的所有进程是守护进程异步处理任务时， 必须要加上close和join

# from multiprocessing import Pool
#
# def func(num):
#     num += 1
#     return num
#
# def test(n):
#     print(n)
# if __name__ == '__main__':
#
#     l = []
#
#     p = Pool(5)
#
#     for i in range(100):
#             res = p.apply_async(func, args=(i,), callback=test)  # 异步返回来的是对象，获取对象
#             print(res.get())
#             l.append(res)  # 中的值用 对象.get()


# GIL：全局解释锁
# （只有Cpython解释器才有）对于线程来说，因为有了GIL所以没有真正的并行计算机的执行单位以线程为单位，
# 计算机的最小可执行是线程进程是资源分配的基本单位，线程是可执行的基本单位，
# 是可被调度的基本单位线程不可以自己独立拥有资源，线程的执行，必须依赖于所属进程中的资源，
# 进程中必须至少有一个线程)
# GIL锁的限制（
# 线程会被强迫放弃cpu的原因，首先线程会收时间片影响，其次GIL会限制每个线程的执行时间，一般是5ms左右
# 或则限制线程执行固定数量的bytecode, GIL锁被限制在同一时间只能有一个线程在使用cpu（不论是单核还是多核））


# 线程的分类（线程又分为用户级线程和内核级线程（了解）
# 用户级线程：对于程序员来说，这样的线程完全被程序员控制执行，调度
# 内核级线程：对于计算机内核来说的，这样的线程完全被内核控制调度）


# 开启线程(不加锁也许会出现数据错乱问题)

# from threading import Thread
# a = 0
#
# def test():
#
#     global a
#     for i in range(100000):
#         a += 1
#     print(a)
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = Thread(target=test)
#         t.start()


# 类继承开启多线程(没加锁会产生数据错乱)

# from threading import Thread
#
# a = 0
#
# class A(Thread):
#
#     def run(self):
#         global a
#         for i in range(100000):
#             a += 1
#         print(a)
#
# if __name__ == '__main__':
#
#     for i in range(10):
#         t = A()
#         t.start()


# 守护线程

# 守护线程是根据主线程执行结束猜结束
# 守护线程不是根据主线程的代码执行结束而结束
# 主线程会等待普通线程执行结束，再结束
# 守护线程会等待主线程结束，再结束
# 所以，一般把不重要的事情设置为守护线程
# （守护进程）是根据主进程的代码先执行完毕，守护进程就结束


# 开启守护线程（t.daemon = True）

# from threading import Thread
#
# a = 0
# li = []
# def test1():
#     for i in range(100000000):
#         li.append(i)
#
# def test2():
#     global a
#     for i in range(10000):
#         a += 1
#     print(a)
# if __name__ == '__main__':
#
#     t1 = Thread(target=test2)
#     t2 = Thread(target=test2)
#     t3 = Thread(target=test2)
#     t4 = Thread(target=test1)
#     t4.daemon = True
#     t1.start()
#     t2.start()
#     t3.start()
#     t4.start()


# 防止多线程的数据错乱1（加锁Lock, l.acquire(), l.release()）
# from threading import Thread, Lock
# a = 0
#
# def test(l):
#     l.acquire()
#     global a
#     for i in range(1000000):
#         a += 1
#     l.release()
#     print(a)
#
#
# if __name__ == '__main__':
#     l = Lock()
#     for i in range(10):
#         t = Thread(target=test, args=(l,))
#         t.start()


# 多线程的多个锁(防止出现死锁,多个锁一把钥匙 Rlock l.acquire() l.release())

# from threading import Thread, RLock
#
# def test(l1, l2):
#
#     l1.acquire()
#     print("男的把第一道门上了锁")
#     l2.acquire()
#     print("男的把第二道门上了锁")
#
#     l2.release()
#     print("男的打开了第二道门")
#     l1.release()
#     print("男的打开了第一道门")
#
#
# if __name__ == '__main__':
#     l1 = l2 = RLock()
#     for i in range(10):
#         t = Thread(target=test, args=(l1, l2))
#         t.start()


# 多线程的信号量（from threading import Swmphore）

# 1 也是一把锁
# 2 与进程池类似，不同点是进程池从头到尾都是那几个进程在执行任务
#     信号量是产生多个线程，去执行任务
# from threading import Semaphore, Thread, currentThread
#
# def test(n):
#
#     print('男子锁住了厕所', n,currentThread())
#     s.acquire()
#     print('男字打开了厕所', n,currentThread())
#     s.release()
#
#
# if __name__ == '__main__':
#
#     s = Semaphore(5)
#     for i in range(20):
#         t = Thread(target=test, args=(i,))
#         t.start()


# 多线程的事件（from threading import Event）

# 可在线程设置信号， 等待某个事件的发生
# Event.isSet()  返回event的状态值
# Event.wait()  如果 event.isSet()==False将阻塞线程；
# Event.set()  设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
# Event.clear()  恢复

# from threading import Event, Thread
# import time
#
# def test1():
#     time.sleep(5)
#     print("test1")
#     print(e.isSet(), 't1-1')
#     e.set()
#     print(e.isSet(),'t1-2')
#
# def test2():
#     print(e.isSet(), 't2')
#     e.wait()
#     print("test2")
#
#
# if __name__ == '__main__':
#     e = Event()
#     for i in range(20):
#         t1 = Thread(target=test1())
#         t2 = Thread(target=test2())


# 条件（from threading import Condition


# c = Condition()  # 创建条件对象
# c.acquire()  # 加锁
# c.release()  # 解锁
# c.wait()  # 让线程阻塞
# c.notify(int)  # 是指给wait发送一个信号，让wait变成不阻塞
# # int是指，你要给多少个wait发信号）


# Timer模块（定时器from threading import Timer）（
# 语法
#     Timer(time, func)
#     参数
# time: 睡眠的时间，以秒为单位
# func: 睡眠之后，需要执行的任务


# 线程和进程的比较
# 组成
# 进程由，代码段，数据段，PCB组成 （process control block）
# 线程由，代码段，数据段，TCB组成 （thread control block）
# cpu切换
# cpu切换进程要比cpu切换线程慢很多在python中，如果IO操作过多的话，使用多线程最好
# 共享
# 在同一进程内，所有线程共享这个进程的pid， 也就是说所有线程共享所属进程的所有资源和内存地址
# 在同一个进程内，所有线程共享该进程中的全局变量
# 并行
# 因为有GIL锁的存在， 在Cpython中，没有真正的线程并行，
# 但是有真正的多进程并行当你的任务是计算密集的情况下，使用多进程好
# 守护线程和守护进程的事情
# 注意
# 代码执行结束并不代表程序结束
# 守护进程：要么自己正常结束，要么根据父进程的代码执行结束而结束
# 守护线程：要么自己正常结束， 要么根据父线程的执行结束而结束
# 总结
# 在cpython中， IO密集用多线程，计算密集用多进程


# 线程池(submit异步提交任务不阻塞立即返回，顺序乱)

# from concurrent.futures import ThreadPoolExecutor

# 这个模块是异步调用的机制
# 提交任务都是用 submit

# from concurrent.futures import ThreadPoolExecutor
#
# def test(n):
#     # print(n)
#     s = n+1
#     print(s)
#
# if __name__ == '__main__':
#     t = ThreadPoolExecutor(20)
#     for i in range(100):
#         t.submit(test, i)


# 线程池(map异步提交任务不阻塞立即返回，顺序乱, map知识取代了for循环)

# from concurrent.futures import ThreadPoolExecutor
#
# def test(n):
#     s = n+1
#     print(s)
#
# if __name__ == '__main__':
#     t = ThreadPoolExecutor(20)
#     # for i in range(100):
#     t.map(test, [i for i in range(100)]) # 取代了for循环


# 进程池和线程池的返回值
# 进程池
# 在Pool进程池中拿结果，是用get方法， 在ThreadPoolExcutor中拿结果用result方法
# i.result()
# 线程池
# 用map的方式提交多个任务，对应拿结果的方法是__next__()）


# 线程池的回调函数
# 线程池
# t.submit(fun, i).add_done_callback(func)


# 不管是ProcessPoolExeculor的进程池，还是Pool的进程池，回调函数都是父进程调用的
# 线程池里的回调函数不是父线程调用的，是子线程调用的
# 进程池中的回调函数是父进程调用的， 和子进程没有关系


# 套接字类型
#     面向字节流   协议类型
#         AF_INET， SOCK_STREAM


# 套接字中的方法

# 1 coonect()和connect_ex()（后者带返回值，错误会返回# 错误代码# 不会结束程序报错）
# 2 sendall() 尝试一次性把数据都发出去
# 3 getpeername() 获取连接的远端地址
# 4 getsockname() 获取当前套接字地址
# 5 setblocking() 设置accept和recv两个方法的阻塞与非阻塞状态，false 非阻塞 ，True阻塞
# 6 settimeout()      设置阻塞套接字操作的超时时间
# 7 gettimeout()      得到阻塞套接字操作的超时时间


# 全双工通信
# （双向互发消息）


# 端口的范围
# （端口的范围0 - 65535其中0～1023其他程序基本占用）
#


# tcp协议（可靠的，面向连接（前提条件连接）的协议
# 传输效率低双工通信，面向数据流SOCK_STREAM，应用到电子邮件，文件传输）


# tcp的三次握手
# ** ** ** ** ** ** *
# 1 客户端发送SYN（SEQ = x）报文给服务器端，进入SYN_SEND状态。
#
# 2 服务器端收到SYN报文，回应一个SYN （SEQ = y）ACK(ACK=x + 1）报文，进入SYN_RECV状态。
# 3 客户端收到服务器端的SYN报文，回应一个ACK(ACK=y + 1）报文，进入Established状态。
# 三次握手完成，TCP客户端和服务器端成功地建立连接，可以开始传输数据了。
# ACK的意识： 确认收到
# SYN的意识： 请求连接的一个标识
# FIN的意识： 请求断开链接的一个标识）


# tcp的四次挥手

# 第一次： 客户端发起一个请求，代表我没有数据继续发送了， 但是如果你有数据继续法，我可以继续接受
# 第二次： 服务器发送一个确认收到的ACK
# 第三次： 服务器再发送一个断开连接的请求，表示可以断开连接了
# 第四次： 客户端回复一个确认收到


# tcp的三次握手图文版
# 第一次： SYN(SEQ=X)
# 报文（发送连接请求）
# 客 - ----------------------------------------------------------------------------------->   服
# 第二次：服务端接受SYN报文，回应一个SYN（SEQ = y）ACK(ACK=x + 1）报文（服务器确认收到，连接客户端的请求）
# 户 < ------------------------------------------------------------------------------------   务
# 第三次：客户端收到服务器端的SYN报文，回应一个ACK(ACK=y + 1）报文（客户端回复收到请求，可以链接）
# 端 - ------------------------------------------------------------------------------------>  端
#


# tcp的四次挥手图文版
# 第一次：FIN分节（客户端发起一个请求，代表我没有数据继续发送了， 但是如果你有数据继续法，我可以继续接受）
# 客 - ----------------------------------------------------------------------------------------> 服
# 第二次：发送ACK（服务器发送一个确认收到的ACK）
# < -----------------------------------------------------------------------------------------
# 第三次：发送FIN（服务器再发送一个断开连接的请求，表示可以断开连接了）
# 户 < ----------------------------------------------------------------------------------------- 务
# 第四次：发送ack（客户端回复一个确认收到）
# 端 - ----------------------------------------------------------------------------------------> 端
#                                                                                               ** ** ** ** ** ** ** ** *
# (1) “通常”是指，某些情况下，步骤1的FIN随数据一起发送，另外，
# 步骤2和步骤3发送的分节都出自执行被动关闭那一端，有可能被合并成一个分节。[2]
# (2)
# 在步骤2与步骤3之间，从执行被动关闭一端到执行主动关闭一端流动数据是可能的，
# 这称为“半关闭”（half - close）。
# (3)
# 当一个Unix进程无论自愿地（调用exit或从main函数返回）
# 还是非自愿地（收到一个终止本进程的信号）终止时，所有打开的描述符都被关闭，
# 这也导致仍然打开的任何TCP连接上也发出一个FIN。
# 无论是客户还是服务器，任何一端都可以执行主动关闭。通常情况是，客户执行主动关闭，
# 但是某些协议，例如，HTTP / 1.0
# 却由服务器执行主动关闭。[2]


# 创建tcp服务端
# 步骤 1 创建套接字2绑定端口3监听客户请求4接受客户链接5接受和发送与客户端 6关闭套接字
# ）
# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('192.168.1.107', 10000))
# s.listen()
# conn, addr = s.accept()
# m = conn.recv(1024)
# print("收到客户端信息", m)
# conn.send(m)
# conn.close()
# s.close()


# 创建tcp客户端(步骤：1创建套接字2链接服务器3发送和接受4关闭套接字)
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("192.168.1.107", 10000))
# s.send('我是服务端'.encode("utf-8"))
# m = s.recv(1024)
# print(m)
# s.close()


# socketserver模块（tcp协议中，解决服务器不能同时连接多个客户端的问题
# import socketserver
#
# class Mysocket(socketserver.BaseRequestHandler):
#         def handle(self):  # 固定用法
#                 pass  # 收发逻辑代码
#                 # self.request == conn  客户端
#
#
# server = socketserver.TCPServer('192.168.1.110', 10000, Mysocket)  # 固定用法
# server.serve_forever()  # 开启永久性服务）


# 创建UDP服务端（步骤 1创建套接字2绑定端口3接受和发送recvfrom4关闭套接字）
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(("192.168.1.110", 10000))
# data, addr = s.recvfrom(1024)
# print(data)
# s.close


# 创建UDP客户端（步骤 1创建套接字2发送和接受sendto(b'xxx',(ip，端口)3关闭套接字）
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.sendto(b'hhhh11111',("192.168.1.110", 10000))
# s.close()


# 粘包
# 只有tcp协议才会发生粘包， udp不会发生粘包发送端发送数据，接受端不知道应该如何取接收，
# 造成的一句数据的混乱
# send(b'abc')
# send(b'123')
# recv(4) - --> abc1  # 有时候会收不到
# recv(4) - --> 123


# 合包机制的粘包
# 在tcp协议中，有一个合包机制（nagle算法）将多次连续发送且将各较小的数据，进行打包成一块数据传送）


# 拆包机制造成的粘包
# 还有一个拆包机制，在发送端因为收到网卡的MYU限制， 会将大的超过的MTU限制的数据进行拆分，
# 拆分成多个小数据，进行传输。当传输到目标主机的操作系统层时， 会重新将多个小数据合成并成原本的数据）


# udp协议不会发生粘包（ udp不会发生粘包，udp协议本层对一次收发数据大小的限制是
# 65535 - ip包头（20）-udb包（8） = 65507
# 字节
# 站在数据链路层，因为网卡的MTU一般限制在了1500, 所以对于链路层来说一次收发数据的大小被限制在
# 1500 - ip包头（20）-upd包头（8） = 1472
# 字节
# 如果sendto(num)
# num > 65507
# 会报错
# 如果
# 1472 < num < 65507
# 会在数据链路层拆包，而udp本身是不可靠协议，所以一旦拆包之后造成的多个小数据包在网络传输中，如果丢任何一个，那么此数据传输失败。
# 所以
# num < 1472
# 是比较理想的状态）


# int型变量
# 在32位操作系统中占4个字节，32
# 位
# 在64位操作系统中占4个字节，64
# 位
# int型变量范围
# -2147483648 <= a <= 2147483647）


# struct模块进行打包(把一个数字打包成一个4字节的bytes)
# import struct
# a = struct.pack("i", 1231231) # 是num的类型   'i' 是4个字节
# print(a)
# print(len(a))
# >>> b'\x7f\xc9\x12\x00'
# 4


# 使用sturct模块进行解包
# import struct
# a = struct.pack("i", 123123123)
# b = struct.unpack("i", a)
# print(b)
# >>> 返回(123123123,)


# 文件上传服务端
# 原理类型为字典
# 包括{要执行的功能, 文件名, 文件内容}传递为字节所以应该将字典转换成字符串然后
# 转换成字节，利用josn模块或piclke？模块）

# import socket
# import struct
# import os
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(("192.168.1.107", 10000))
# s.listen()
# conn, addr = s.accept()
#
# data_struct_size = conn.recv(4)
#
# data_size = struct.unpack("i", data_struct_size)[0]
#
# with open("aa.txt", "w", encoding="utf-8")as f:
#     x = 0
#     while x < data_size:
#         d = conn.recv(1024)
#         if d == b'':
#             break
#         x += len(d)
#         f.write(d.decode("utf-8"))
#     print(x)
# print(os.path.getsize("aa.txt"))
# conn.close()
# s.close()


# 文件上传服务端客户端
# import socket
# import struct
#
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("192.168.1.107", 10000))
#
# file_size = get_file_size()
# print(file_size)
# struct_size = struct.pack("i", file_size)
#
# s.send(struct_size)
#
# with open("a.txt", "r", encoding="utf-8")as f:
#     for con in f:
#         s.send(con.encode("utf-8"))
#         print(repr(con))
#
# s.close()


# 使用subprocess模块在python代码中调用操作系统的命令（
# r = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# 参数
#     cmd：系统命令
#     shell：代表这条命令是系统命令，告诉操作系统，将cmd当成系统命令执行
#     stdout：执行完系统命令之后，用于保存结果的管道
#     stderr：执行完系统命令之后，用于保存错误结果的管道
# import subprocess
# r = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(r.stdout.read())
# print(r.stderr.read())


# 有符号int和无符号int的区别（
# unsigned
# 代表无字符号
# 有符号int和无符号int的区别
# 有符号表示1个字节，8位，最高位是符号位， 所以有符号的变量，一个字节的表示范围 - 128～127
# 无符号表示1个字节，8位，所有位都是数值，所以无符号的变量，一个字节表示范围，0 - 255）


# float和double的区别（
# float和double
# float表示单精度，一般的操作系统中表示为，将数值准确到小数点后7～8位
# double表示双精度，一般操作系统中表示为，将数值准确到小数点后15～16位）


# 计算的硬件组成（
# 主板
# 固化(寄存器，是直接和cpu进行交互的一个硬件)
# cpu
# 中央处理器
# 计算（数字计算和逻辑计算）和控制(控制所有硬件的协调工作)
# 存储
# 硬盘 ， 内存
# 输入设备
# 键盘， 鼠标， 话筒
# 输出设备
# 显示器，音箱，打印机）


# 计算机的存储设备的运行速度
# 排序（读写速度越来越慢
# 价格越来越便宜
# 容量越来越大）
# cpu -->寄存器 -->高级缓存 -->内存 -->缓存 -->硬盘


# 计算机的发展（
# 计算机的发展核心：早期的计算机以计算为核心
# 现在的计算机以存储为核心
# 第一代计算机：电子管计算机，及其耗电，体积庞大，散热片特别高
# 第二代计算机：晶体管计算机
# 第三代计算机：集成电路计算机， 一个板子固化几十到几百个小硬件，白色大头计算机
# 第四代计算机：大型集成电路计算机， 一个板子可以达到固化十万个硬件
# 第五代计算机：甚大型继承电路计算机
# ）


# 计算机的操作系统
# 计算机的操作系统（软件直接能操作硬件）
# 操作系统的发展
# 作系统是一个软件，是一个能直接操纵硬件的一个软件，微软研发的windows操作系统
# 计算机刚开始使用的时候，还没有操作系统
# 人工时代：穿孔卡带
# 脱机时代：安全和将人和机器隔离开来
# 单道批处理系统：内存中只允许存放一道作业
# 多道批处理系统：内存中允许存放多道作业
# 操作系统的分类
# 分时系统将cpu的执行划分时间片，每个程序以时间片为单位去执行
# dos系统纯编程系统
# windows系统
# unix系统
# 实时系统一般比较少见，主要用于军事和工业生产上
# 操作系统的发展核心
# 无论什么时候，操作系统的目标是：让用户用起来更加的轻松，高可用，低耦合
# 操作系统的作用
# 1
# 封装所有硬件接口， 让各种用户使用电脑更加轻松
# 2
# 是对计算机内所有资源进行合理的调度和分配


# 计算机语言发展史
# 1计算机识别是二进制，机器语言由1和0组成
# 2汇编语言
# 3高级语言
# 面向过程语言（c, c + +），面向对象语言（c + +，java，python，.net, php）


# 进程（概念，组成，基本状态，特性，通信限制）
# 概念
# 进程是指正在执行的程序，是程序执行过程中的一次指令，数据集等集合，
# 也可以叫做程序的一次执行过程进程是一个动态的概念，进程是资源分配的基本单位）

# 进程的组成
# 代码段，数据段，PCB（进程管理控制块）

# 进程的基本状态

# 就绪状态： 已经获得运行需要的所有资源，除了cpu
# 执行状态： 已经获得了所有资源包括cpu，处于正在运行
# 阻塞状态： 因为各种原因，进程放弃了cpu，导致进程无法继续执行，此时进程处于内存中，继续等待获取cpu
# 特殊状态: 挂起状态： 是因为某种原因， 进程放弃了cpu，导致进程无法继续执行，此时进程被踢出内存

# 进程的特性（
# 动态性
# 并发型
# 独立性
# 异步性
# ）

# 进程之间的通信限制（
# 正常情况下，多进程之间是无法进行通信的，因为每个进程都有自己独立的内存空间
# ）


# 并行和并发

# 并行
# 两件事或多件事情，在同一时间点同时进行

# 并发
# 指两件事或多件事，在同一时间间隔内同时执行
# 早期单核cpu时候，没有并行的概念，只有并发（微观上串行， 宏观上并行
# 并发的本质：切换 + 保存状态


# 同步和异步

# 同步（某个任务的执行必须依赖于另一个任务的返回结果）
# 异步（某一个任务的执行，不需要依赖于另一个任务的返回，只需要告诉另一个任务一声）


# 阻塞和非阻塞

# 阻塞（程序因为类是与IO等待，等待时间等导致无法继续执行）
# 非阻塞（程序遇到类似于IO操作时候，不再阻塞等待，如果咩有及时的处理IO，就报错或则跳过等其他操作）


# 创建进程
# from multiprocessing import Process
# import time
#
# def test():
#     time.sleep(3)
#     print("子进程结束")
#     return 1
#
# if __name__ == '__main__':
#      p1 = Process(target=test)
#      p2 = Process(target=test)
#      p1.start()
#      p2.start()
#      print("主进程结束")
# >>> 主进程结束
# 子进程结束
# 子进程结束


# 进程的join方法(主进程等待子进程结束才结束)

# from multiprocessing import Process
# import time
#
#
# def test():
#     time.sleep(3)
#     print("子进程结束")
#
#
# if __name__ == '__main__':
#     p1 = Process(target=test)
#     p2 = Process(target=test)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print("主进程结束")
# >>> 子进程结束
# 子进程结束
# 主进程结束


# 进程Process中的其他方法

# p.is_alive()    判断进程是否存活
# p.terminate()   杀死p进程，让解释器告诉操作系统，请杀掉p进程
# os.getpid()   获取当前进程的pid号
# os.getppid()  获取当前进程的父进程pid号
# p.name        获取进程的名字
# p.pid         获取当前进程的pid号


# 守护进程及特性

# 1守护进程会随着父进程的终结而终结（主进程的代码执行结束时候也相当于父进程结束）
# 2不能再创建自己的子进程
# 3必须在p.start()之前设置
# 4若加上p.join 父进程还是会等着子进程结束猜结束）


# 创建守护进程（p.daemon）

# from multiprocessing import Process
# import time
#
# def test():
#     time.sleep(5)
#     print("子进程结束")
#
#
# if __name__ == '__main__':
#     p1 = Process(target=test)
#     p2 = Process(target=test)
#     p1.daemon = True
#     p2.daemon = True
#     p1.start()
#     p2.start()
#     time.sleep(3)
#     print("主进程结束")


# 继承类Process开启进程
# from multiprocessing import Process
# class A(Process):
#   def __init__(self):
#       super().__init__()
#   def run(self):
#       print('haha')
# if __name__ == '__main__':
#   p = A()
#   p.start()


# 生产者和消费者模型（JoinableQueue()，q.task_done()，q.join()）
# q = JoinableQueue()
# q.task_done()  # 用于消费者，是指每消费队列中的一个数据，就给join返回一个标识
# q.join()  # 用于生产着， 等待 q.task_done的返回结果，通过返回结果，
# # 生产者就能获得消费者当前消费了多少个数据
# from multiprocessing import Process, JoinableQueue
#
#
# def producer(q):
#     print('我是生产者')
#     for i in range(20):
#         print("生产者生产了", i)
#         q.put(i)
#     q.join()    # 用于生产着， 等待 q.task_done的返回结果，通过返回结果
#
#
# def taker(q):
#     while True:
#         s = q.get(1)
#         q.task_done()   # 用于消费者，是指每消费队列中的一个数据，就给join返回一个标识
#         print('消费者拿了', s)
#
#
# if __name__ == '__main__':
#     q = JoinableQueue(10)
#     p = Process(target=producer, args=(q, ))
#     t = Process(target=taker, args=(q, ))
#     t.daemon = True # 消费者设置为守护进程
#     p.start()
#     t.start()
#     p.join()


# 管道（了解）
# 缺点
# 管道是不安全。
# 作用
# 是用于多进程之间的通信的一种方式
# 使用方法
# 在单进程使用管道
# 就是con1收数据，con2发数据
# 如果con1发数据, con2收数据
# from multiprocessing import Pipe
# con1, con2 = Pipe()
# con1.send('aaa')
# print(con2.recv())
# con2.send('bbbb')
# print(con1.recv())


# 在多进程中使用管道
# 必须是父进程使用con1收，子进程必须使用con2发
# 父进程使用con1发，子进程必须使用con2收
# 父进程使用con2发，子进程必须使用con1收
# 父进程使用con2收，子进程必须使用con1发
#
# from multiprocessing import Pipe, Process
# def p1(con1, con2):
#         print(con2.recv())  # 主进程管道1发送消息做的事情
#         con1.close()
#
#         con2.send('heihei')  # 子进程管道1向主进程发送消息做的事情
#
# if __name__ == '__main__':
#         con1, con2 = Pipe()
#         p1 = Process(target=p1, args=(con1, con2))
#         p1.start()
#
#         con2.close()
#         con1.send('haha')
#
#         print(con1.recv())  # 子进程管道1向主进程发送消息做的事情
#         管道中著名的错误
#         管道中有一个著名的错误叫EOFError，是指，父进程中如果关闭了发送端，子进程还
# 继续就收数据，那么就会引发EOFError


# 进程之间的共享内存
# from multiprocessing import Manager
#
# m = Manager()
#
# num = m.dict({key: value})
#
# num = m.list([1, 2, 3, 4])）


# from multiprocessing import Manager, Process
#
# def test1(a1):
#
#     a1[2] = 999
#
# def test2(a2):
#     a2[3] = 888
#
#
# if __name__ == '__main__':
#     m = Manager()
#     a = m.list([1,2,3,4])
#     b = m.dict({"a":1, "b":1})
#     p1 = Process(target=test1, args=(a,))
#     p2 = Process(target=test2, args=(a,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print(a)
# >>> [1, 2, 999, 888]


# 电脑进程池的数量
# 适合电脑开进程最多数 多了影响性能
# 因为在实际业务中， 任务量是有多有少的， 如果任务量特别的多， 不肯能要开对应那么多的进程数
# 开启那么多进程首先就需要消耗大量的时间让操作系统来为你管里它。其次还需要消耗大量时间让cpu帮你
# 调度它进程池还会帮助程序管理池中的进程）
# print(os.cpu_count()+1)
# >>> 5














# 协程
# 是一个比线程更加轻量级的单位,是组成线程的各个函数,协程本身没有实体
# 想要在单线程内并发的效果
# 因为cpython有GIL锁， 限制了在同一个时间点，只能执行一个线程
# 所有想要在执行一个线程的期间，充分的利用cpu的性能
# 所有才有了项在单线程内实现并发的效果


# 并发的本质
# 切换 + 保存状态


# 协程的创建（yelid）

# def test():
#
#     while 1:
#         print('test')
#         yield 1
#
# def test1():
#     while 1:
#         print('test1')
#         next(a)
#
# a = test()
# b = test1()


# yield实现并发的假象
# 单某一个函数中遇到IO阻塞时候，程序自动的切换到另一个函数取执行如果能实现这个功能，那么
# 每个函数都是一个携程
# 在单线程中，入股存在多个函数，如果有某个函数发生IO操作，我项让程序马上切换到另一个函数取执行
# 以此来实现一个假的并发现象，提高单线程cpu利用率
# yield 只能实现单纯的切换函数和保存函数状态的功能，不能实现当某一个函数遇到io阻塞时，自动的
# 切换到另一个函数取执行
# 若果只是拿yield取单存的实现一个切换的现象，你会发现，根本没有程序串行执行效率高


# Greenlet模块（第三方组件 只是可以实现一个简单的切换功能，还是不能做到遇到IO就切换)

# 1 安装
# pip3 install greenlet
# 2 使用

# from greenlet import greenlet
# def test1():
#     while 1:
#         print('test1')
#         b.switch()
#
#
# def test2():
#     while 1:
#         print('test2')
#         a.switch()
#
# a = greenlet(test1)
# b = greenlet(test2)
# a.switch()


# gevent模块（第三方组件，实现智能化遇见IO就切换到另一个函数(只能识别自己认识的io操作)

# 1 安装
# pip3 install gevent

# 2 使用

# import gevent
#
# def test1():
#     while 1:
#         print('test1')
#         gevent.sleep(2)
#
#
# def test2():
#     while 1:
#         print('test2')
#         gevent.sleep(2)
#
# a = gevent.spawn(test1) # 注册一下函数func，返回一个对象a
# b = gevent.spawn(test2)
# a.join()   # 等待g1指向的任务执行结束


# gevent模块(第三方组件，实现智能化遇见IO就切换到另一个函数)
# import gevent
# from gevent import monkey
# import time
# monkey.patch_all()  # 可以让gevent识别大部分常用的io操作
#
#
# def test1():
#     while 1:
#         print('test1')
#         time.sleep(2)
#
#
# def test2():
#     while 1:
#         print('test2')
#         time.sleep(2)
#
# a = gevent.spawn(test1)
# b = gevent.spawn(test2)
# a.join()


# 线程和进程和协程
# 协程
# 是有用户自己取调度的
# 多进程和多线程
# 计算密集用多进程， 可以充分利用多核cpu的性能
# IO密集用多线程（注意，协程是在单线程的）
# 多线程和协程的区别
# 线程是有操作系统调度，控制的
# 协程是有程序员自己调度，控制）


# IO多路复用
# 异步IO
# python实现不了 ，但是有有tornado框架，天生自带异步


# select 和 poll 和epoll的区别
# select和poll有一个共同的机制，都是轮询的方式取询问内核，有没有数据准备好了
# select有一个最大监听事件的限制， 32位机限制1024, 64位机限制2048
# poll没有，理论上poll可以开启无线大，1g内存大概够开10万个事件去监听
# epoll是最好的，采用的是回调机制，解决了select和poll共同存在的问题（内核的消耗）
# 而且epoll理论上也可以开启无限多个监听事件

# select: 适用于windows / linus # 是监听事件有没有数据的到来
# poll：适用于linux# 也可以做select的工作
# epoll：适用于linux 也可以做类似的工作 （最好）


# socket用非阻塞io解决阻塞io(不推荐，循环造成cpu负担)
# import socket
# sk = socket.socket()
#
# sk.setblocking(False)
#
# sk.bind(('xxxxx', xxxx))
#
# l = []
# del_l = []
# while 1:
#
#     try:
#         conn, addr = sk.accept()  # 如果是阻塞IO模型，这里程序会一直等待
#         l.append(conn)  # 将每个请求链接的客户端conn添加到列表中
#     except BlockingIOError:
#
#         for conn in l:
#             try:
#                 info = conn.recv(1024).decode('utf-8')  # 看看列表中存在的conn是不是给我发数据了
#                 if not info:  # 客户正常关闭客户端会返回给服务端一个空
#                         del_l.append(conn)  # 已经结束的客户端conn， 添加到要删除的列表中
#                         conn.close()  # 因为客户端已经主动close，所以服务端的conn也要close
#                 else:
#                         print(info)
#                         conn.send(info.upper().encode('utf-8'))
#
#                 print(info)
#             except BlockingIOError:
#
#                 continue  # 没有接受到客户端发来的数据而报错
#
#             except ConnectionError:
#
#                 pass
#
#         if del_l:
#
#             for i in del_l:
#                     l.remove(i)
#             del_l = []  # 在删除完主动关闭的客户端的连接之后，应该把此列表清空）


# select解决非阻塞造成cpu负担（基于select的网络IO模型)
# import select
# import socket
# sk = socket.socket()
# sk.bind(('xxxxxx', xxxx))
# sk.listen()
# del_l = []
# rlist = [sk]  # 代表有客户端链接
# # [], [], []  依次为 接受数据（只放读的模型）， 只放写的模型， 只放修改的事件
# r, w, x = select.select(rlist, [], [])
#
# while 1:
#
# r, w, x = select.select(rlist, [], [])  # 把sk给了select去管理监听所有的接口
# if r:  # 如果有客户端连接
#     for i in r:  # 看有反映接口到底是sk，还是conn
#         if i == sk:  # 代表有新的客户端来连接
#                 conn, addr = i.accept()
#                 rlist.append(conn)  # 继续让select监视conn
#         else:  # 代表rlist中的conn发送来的数据
#             try:
#                 msg_r = i.recc(1024).decode('utf-8')
#
#                 if not msg_r:  # 客户端执行了close，客户端主动正常关闭链接
#
#                         del_l.append(i)
#                         i.close()
#                 else:
#                         print(msg_r)
#                         i.send(msg_r.upper().encode('utf-8'))
#             except ConnectionResetError:
#                     pass
#     if del_l:  # 删除那些主动端口链接的客户端的conn
#
#         for i in del_l:
#                 rlist.remove(i)
#         del_l.clear()


# 文件的类型
# .sh
# shell脚本文集
# .out
# linux系统中可执行文件
# .bat
# 批处理脚本文集
# .lib
# 库文件
# .dll
# 库文件
# .exe
# 可执行文件


# IPC
# inter process Communication进程间通信（锁不是进程间通信）
# IPC分类
# 管道，队列（锁, 信号量, 事件）


# 栈
# 先进后出（First In Last Out 简称FILO） 有墙）


# 队列（先进先出 （First In First Out 简称FILO）无墙）


# 共享资源
# 共享资源又叫临界资源享代码又叫临界代码，进行操作时， 一定要加锁


# ascii的比较
# 'abc'和'cef'
# 先比较字符串中第一位的大小，若不相等，就决定了字符串谁打谁小若相等再比较下一位）


# cpu的切换
# 1 因为某个程序阻塞了
# 2 因为某个程序用完了时间片
# 所以要钥实现单线程的并发，就要解决在单线程内，多个任务函数中，某个任务函数遇见io操作
# 马上自动切换到其他任务函数取执行。

