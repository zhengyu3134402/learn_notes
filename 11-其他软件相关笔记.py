#
#
#
# ====================================================
# fiddlerfiddler
#
#     1 概念
#
#         抓包工具
#
#         <>  表示get请求
#         框—> 表示post请求
#
#     2 配置
#         1 是软件能够抓取HTTPS协议的数据
#             Tools---Telerik Fiddler Options--
#             HTTPS-Decrypt HTTPS traffic打上勾，
#             check for certificate revocation打上勾
#
#     3 使用
#         1 查看ruquest response先关点击Inspectors
# ====================================================
#
#
#
#
# =========================================================
# vmwarevmware
#
# 	1 概念
#
# 		虚拟机
#
# 	2 安装
#
# 		1 创建新的虚拟机
#
# 			1 稍后安装操作系统
# 			2 linux
# 			3 起名
# 			4 处理器配置 2 2 4
# 			5 分配内存 1
# 			6 网络类型 NAT
# 			7 I/O控制类型 下一步
# 			8 磁盘类型 下一步
# 			9 选择磁盘下一步
# 			10 指定磁盘容量 将虚拟磁盘拆分成多个文件
# 			11 制定磁盘文件 下一步
# 			12 已经准备好创建虚拟机
# 				自定义硬件
# 					新CD.DVD(IDE)
# 						使用ios映像文件
# 					声卡移除
# 					打印机移除
# 		2 开启虚拟机
# 			Install CentOS 7
#
# 			SOFTWARE SELECTION
# 				Basic Web Server
# =========================================================
#
#
#
# =========================================================
# jupyter nptebook
#
#
#
#     1 安装
#
#         pip3 install -i https://pypi.douban.com/simple jupyter
#
#     2 进入ipython设置密码
#
#         from IPython.lib import passwd
#
#         passwd()
#
#     3 配置
#
#         1 终端输入命令
#             jupyter notebook --generate-config --allow-root
#
#         2 根据生成的配置文件编辑文件
#
#             查找文件中的内容 修改成下面的内容
#             c.NotebookApp.ip = '0.0.0.0'
#             c.NotebookApp.open_browser = False
#             #先不改c.NotebookApp.password = 'sha1:923fba4c6267:d4820c83cff0a6bdcc511b0e4843cb68f412337d'
#             c.NotebookApp.port = 8000
#     3 启动
#         jupyter notebook --allow-root
#
#     3 进入jupyter
#
#         1 通过配置的ip端口通过浏览器进入
#         2 根据启动时候出现的token粘贴到下面的Token设置密码
#
#     4 使用
#
#         1 创建ipython环境
#
#             点击new 点击python3
#
#         2 创建笔记模式markdown（笔记模式）
#             选择模式点击+
#
#         3 概念创建ipython3的名字
#             点击头部的Untitled
#     5 markdown相关
#
#         1 控制字体大小
#             #xx
#         2 控制字体颜色
#             <font color="red">xx</font>
#     6 快捷键
#         a       # 在选择框下方插入code模式
#         b       # 在选择框上方插入code模式
#         x       # 删除一个框
#         m       # 切换成markdown模式
#         y       # 切换成code模式
#         shift+enter         #执行代码
#         tab     #自动补全
#         shift+tab       #弹出帮助文档
#     5 相关方法
#
#         %time 一行代码   计算当前行的运行时长
#         %%time 多行代码  计算多行代码的运行时长
#         %timeit 多行代码 计算代码执行1000次的平均耗时
#         %run xx.py 可以运行外部的一个路径名称源文件
#
# ====================================================