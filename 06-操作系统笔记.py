#
# 说明：
#
#     此文档包含操作系统相关
#     1 windows  --> windows
#     2 linux --> linuxlinux
#
# =================================================
# windows
1
# terminal
#     进入D盘  直接 输入  d:+回车
#
1
# =================================================




# =========================================================
# linuxlinux
1
#     1 版本的选择
#         linux 发行版（用的多）
#         redhat发行版，收费版的linux，提供了资格认证（用的多）
#         SUSElinux 德国版linux ，常用于电信，移动，支付服务器
#         ubuntu
#
#     2 linux支持7个终端
#         通过ctrl+alt  +f1-f7
#         f1是图形化 f2-f7是命令行终端
#
#     2.1 虚拟机的网络配置
#         1 模式分类
#
#             1 host only
#
#                 本机电脑和本机虚拟机通信
#
#             2 桥接模式
#
#                 局域网内添加一个电脑，占用局域网一个ip
#
#             3 NAT模式 （解决ip地址不够用，ip地址冲突的问题）
#
#                 在宿主机的ip网络中，通过网络地址转换技术（NAT），分配一个私有局域网（可自定义192.x.x.x, 10.x.x.x）
#
#         2 vmware设置
#
#             点击编辑--->wmnet8----NAT---勾上将主机虚拟适配器连接到此网络
#             --去掉勾选项使用本地DHCP服务器将IP地址分配给虚拟机--子网ip10.0.0.0
#             --NAT设置--网管ip10.0.0.254
#         3 概念
#
#             通过网络地址转换，分配一个10.0.0.x网段的ip
#             分配一个固定的ip地址，所有人都是10.0.0.10
#
#     3 更改网络配置的文件
#
#         1 使用NET配置  （有问题）
#             1 更改网卡配置文件
#
#                 /etc/sysconfig/network-scripts/ifcfg-ens33.....名字不一定一样
#
#                     更改成 BOOTPROTO=static      # 上网方式静态ip
#                     修改成 ONBOOT=yes            # 每次开机启动
#
#                     # 静态IP相关参数添加
#                     添加   IPADDR=10.0.0.10
#                     添加   NETMASK=255.255.255.0
#                     添加   GATEWAY=10.0.0.254
#                     添加   DNS1=114.114.114.114
#             2 重启网卡
#
#                 /etc/init.d/network restart
#
#
#         2 使用桥接配置
#
#             1 更改网卡配置文件
#
#                 /etc/sysconfig/network-scripts/ifcfg-ens33.....名字不一定一样
#
#
#                     修改成 ONBOOT=yes
#
#
#     4 远程连接
#         1 远程连接软件
#             Xshell或SecureCRT
#         2 远程连接命令
#             ssh 用户名@服务器ip
#         #3 (可能有的情况)在系统刚装好的时候，默认可能没有启动网卡
#            # 1 修改/etc/sysconfig/network-scripts/ifcfg-ens.....文本中的ONBOOT
#
#              #   改称 ONBOOT="yes"
#
#             #2 启动网卡
#              #   ifup   网卡名  （查看网卡名 ip addr,网卡名一般enp...）
#            # 3 关闭网卡
#               #  ifdown 网卡名
#
#
#     5 linux 基本命令
#
#         1 pwd
#
#             显示当前所在执行命令的据绝对路径
#
#         2 ls -l
#
#             显示目录下详细信息
#
#         2.1 ls -la
#
#             显示目录下所有目录和文件，包括隐藏文件
#
#         3 mkdir 名字
#
#             创建一个目录
#
#         3.1 mkdir -p a目录/b目录
#
#             创建递归目录
#
#         4 passwd 用户名
#
#             修改用户使用该系统的密码
#
#         5 touch 文件名
#
#             创建一个文件
#
#         6 rm 文件名
#
#             删除一个文件
#
#         7 rm -i 文件名
#
#             删除一个文件要提醒
#
#         8 rm -i 文件名*
#
#             删除所有以文件名开头的文件
#
#         9 rmdir 目录名
#
#             删除目录（只能删除空的目录）
#
#         10 rm -r 目录名
#
#             递归删除目录
#
#         11 man 命令
#
#             查看命令帮助
#
#         12 mv  文件名 新文件名
#
#             更改文件名
#
#         13 mv 文件名1 文件名2/
#
#             把文件名1移动到文件名2里
#
#         14 cp 文件名 新文件名
#
#             拷贝文件
#
#         15 cp -r  文件名 新文件名
#
#             递归复制文件
#
#         16 cat 文件
#
#             查看文本信息
#
#         17 w
#             查看有哪些用户登陆终端的命令
#
#         18 whoami
#
#             查看用户身份信息
#
#         19 tty
#
#             查看终端信息命令
#
#         20 hostnamectl set-hostname 名字
#
#             更改主机名
#
#         21 安装deb软件
#
#             sudo dpkg -i 文件名
#
#         22 安装deb软件依赖
#             sudo apt-get install -f
#
#         23 查看已经安装的软件
#
#             sudo dpkg -l
#
#         24 卸载软件
#
#             sudo dpkg -r 软件名
#
#         25 一个目录下创建多个同级目录
#
#             mkdir -p aaa/{a,b,c,d}
#
#         26 查看目录，文件状态命令
#
#             stat 目录或文件名
#
#         27 分页读文件
#
#             more 文件名
#
#         27.1 可向前翻页查看文件
#
#             less 文件名
#
#         28 带有行号现实文件内容
#
#             cat -n 文件名
#
#         29 显示指定前多少行数文件内容
#
#             head -5 文件名
#
#         30 显示指定后多少行文件内容
#
#             tail -5 文件名
#
#         31 统计磁盘空间大小
#
#             df -h
#
#         31.1 echo
#
#             1 取变量的值
#
#                  echo $变量名
#
#             2 打印
#
#                 echo "打印内容"
#
#
#         31.1 查看进程
#
#             ps -ef
#
#
#         32 查找命令
#
#             find  (目录)  -type（文件类型） -name（文件名）
#
#                 type参数
#                     b - 块设备文件。
#                     d - 目录。
#                     c - 字符设备文件。
#                     p - 管道文件。
#                     l - 符号链接文件。
#                     f - 普通文件。
#                     s - socket文件
#             例子
#
#                 find /tmp/ -type f -name "*.txt"
#
#         33 管道命令
#
#             1 概念
#
#                 Linux提供的管道符“|”讲两条命令隔开，管道符左边命令的输出会作为管道符右边命令的输入。
#
#         34 grep
#
#             1 概念
#
#                 过滤查找
#
#             2 使用
#
#                 grep "内容" 文件名
#
#                 grep -i "内容" 文件名 忽略大小写查找
#
#                 grep -i “内容” 文件名 -v  # 得到结果的反向结果
#
#         35 检查端口是否存活
#
#             netstat -tunlp | grep nginx
#
#         36 sed命令
#
#             1 概念
#
#                 替换文本命令
#
#             2 使用
#
#                 sed 's/“要改的地方”/"改成的内容"/' 文件 -i
#
#         37 持续刷新显示文本内容
#
#             tail -f 文件名
#
#         38 alias
#
#             1 作用
#
#                 改变命令的执行结果
#
#             2 实现功能
#
#                 1 改变命令的执行功能（如rm）
#
#                     alias rm="echo 禁止使用rm命令" # 字符串中为改变的rm命令结果
#
#                 2 还原命令最初的功能
#
#                     unalias rm
#
#         39 which
#
#             1 作用
#
#                 查询命令在环境变量中的位置
#
#             2 使用(如python3)
#
#                 which python3
#
#         40 scp
#
#             1 概念
#
#                 linux 基于ssh登陆进行安全的远程文件拷贝命令
#
#             2 作用
#
#                 linux 之间复制文件目录
#
#             3 使用
#
#                 1 传输一个文件
#                     scp 本机文件路径 对方的用户名@ip:路径  # 需要对方电脑密码
#
#                 2 递归传输目录
#
#                     scp -r 本机文件路径 对方的用户名@ip:路径
#
#                 3 把对方文件调过来
#
#                     scp -r 对方的用户名@ip:路径
#
#         41 du
#
#             1 作用
#
#                 显示文件或目录的大小
#
#             2 使用
#
#                 1 显示文件或目录大小
#
#                     du 文件 -h
#
#                 2 统计性质显示目录大小
#
#                     du 目录 -sh
#
#                 3 查看log日志目录大小
#
#                     du -sh /var/log/
#
#         42 top
#
#             1 作用
#
#                 用于动态的监视进程活动与系统负载等信息
#
#             1 使用
#
#                 1 命令
#
#                     top
#
#         43 free -m
#
#             查看内存大小
#
#         44 chattr
#
#             1 作用
#
#                 给文件加锁，只能写入数据，无法删除文件
#
#             2 使用
#
#                 1 给文件加锁
#
#                     chattr +a 文件
#
#                 2 给文件去锁
#
#                     chattr -a 文件
#         45 查看文件隐藏属性
#
#             lsattr 文件
#
#         46 date
#
#             查看有软件查出来的时间
#
#         47 显示硬件时间
#
#             hwclock
#
#         48 以系统时间为基准，修改硬件时间
#
#             hwclock -v
#
#         49 以硬件时间为基准，修改系统时间
#
#             hwclock - s
#
#         50 和服务器同步时间
#
#             ntpdate -u ntp.aliyun.com
#
#         51 在线网络下载
#
#             wget url路径
#
#         52 wget -r -p url路径
#
#             获取前端所有网络资源静态static等
#
#         53 查看系统版本
#
#             cat /etc/os-release
#
#         54 查看系统内和版本号
#
#             uname -r
#
#         55 查看系统是多少位机器
#
#             uname -m
#
#         56 切换用户
#
#             su - 用户名 # 要加 - 环境变量也变更为新用户的信息
#
#
#
#
#     5.1 除ubuntu命令
#
#         1 安装软件命令
#
#             yum install 软件名
#
#
#
#     6 vi命令
#
#         0 概念
#
#             1 三种模式
#
#                 命令模式
#                 输入模式  i   a   o
#                 底线命令模式  保存退出 q  wq  wq!  x
#
#         1 命令模式下的命令
#
#             1 移动光标到下一个单词
#
#                 w 或 e
#
#             2 移动光标到上一个单词
#
#                 b
#
#             3 移动光标到文本开头
#
#                 数字 0
#
#             4 移动光标到屏幕首行
#
#                 H
#
#             5 移动光标到中间一行
#
#                 M
#
#             6 移动光标到屏幕的尾行
#
#                 L
#
#             7 移动光标到文档首行
#
#                 gg
#
#             8 移动光标到文档尾行
#
#                 G
#
#             9 下一页
#
#                 ctrl + f
#
#             10 上一页
#
#                 ctrl + b
#
#             11 查找（从上向下找按n）
#
#                 /查找内容
#
#             12 查找（从下往上找n）
#
#                 ?查找内容
#
#             13 复制
#
#                 yy  # 拷贝光标所在的行
#
#             14 粘贴
#
#                 p   # 按几次p就粘贴几次
#
#             15 删除
#
#                 dd # 删除光标所在行
#
#             16 多行复制
#
#                 数字 yy
#
#             17 删除多行
#
#                 数字 dd
#
#             18 撤销
#
#                 u
#
#             19 删除光标所在字母
#
#                 x
#
#         2 底线命令模式
#
#             1 显示行数
#
#                 set nu
#
#             2 光标跳转到多少行上
#
#                 :数字
#
#
#
#     7 xshell命令
#
#         1 logout
#
#             退出linux登陆会话
#
#         2 clear
#
#             清屏
#
#         3 ctrl + d
#
#             快速退出
#
#         3 ctrl + sheift +r
#
#             快速登陆
#
#     8 linux 目录结构
#
#         /dev
#
#             存放抽象硬件
#
#         /boot
#
#             存放内核和启动文件
#
#         /lib
#
#             存放系统库文件
#
#         /bin
#
#             存放二进制文件（可执行命令）
#
#
#         /sbin
#
#             存放特权级二进制文件
#
#         /usr
#
#             存放安装程序（软件默认目录）
#
#         /var
#
#             存放经常变化的文件（日志）
#
#         /mnt
#
#             文件挂载目录（u盘，光驱）
#
#         /home
#
#             普通用户目录
#
#         /root
#
#             特权用户目录
#
#         /ect
#
#             存放配置文件目录
#
#         /opt
#
#             大型软件存放目录（非强制）
#
#
#     9 环境变量
#
#         1 作用
#
#             能从path里面定义的路径，去寻找我们输入的命令
#
#         1 输入命令执行顺序
#
#             1 找到当前path（目录）寻找是否有可执行文件
#
#             2 /usr/local/sbin:
#               /usr/local/bin:
#               /usr/sbin:
#               /usr/bin:
#               /sbin:
#               /bin:
#               /usr/games:
#               /usr/local/games:
#               /snap/bin
#
#
#         1 echo 查看环境变量
#
#             echo $PATH
#
#         2 echo 查看系统编码
#
#             echo $LANG
#
#     10 特殊符号
#
#         输入/输出 重定向符号
#             1.>>    追加重定向，把文字追加到文件的结尾
#             2.>     重定向符号，清空原文件所有内容，然后把文字覆盖到文件末尾
#             3.<     输入重定向
#             4.<<    将输入结果输入重定向
#             echo "oldboy-python666" > /tmp/oldboy.txt
#             echo "chaoge666" >> /tmp/oldboy.txt
#             cat >>/tmp/oldboy.txt << EOF   # 保留输入内容 类似input 结束输入 EOF
#             ------------------------------------
#             我想把命令执行的结果信息，写入到文件中
#             ip addr > /tmp/network.txt   #标准输出重定向 把命令执行结果信息，放入到文件中
#             3.通配符
#             ls -l /etc/us*
#
#     11 用户管理和文件权限
#
#         1 创建用户
#
#             useradd 用户名
#
#         2 查看用户权限
#
#             id 用户名
#
#         3 退出登陆用户
#
#             logout
#
#         4 存放用户身份信息的文件
#             /ect/passwd
#
#         5 存放用户组的文件
#
#             /ect/group
#
#         6 存放用户密码的文件
#
#             /etc/shadow
#
#         7 创建用户组
#
#             groupadd 用户组名
#
#         8 删除用户（用户用过的目录还在）
#
#             userdel 用户名
#
#         9 删除用户（删除用户所有相关信息）
#
#             userdel -fr 用户名
#
#         10 使用root身份去执行命令, 解决权限不够的问题
#
#             1 修改/ect/sudoers文件， 添加想要执行sodu命令的用户
#             2 打开sudoers文件
#                 找到  root  ALL=(ALL)  ALL  下添加
#                      用户名  ALL=(ALL) ALL
#         11 文件的权限
#             1
#             drwxr-xr-x   2        zhengyu zhengyu 4.0K  3月 18 15:06   src
#                权限      文件链接数  属主     属组     大小  文件修改日期    文件名
#
#             2
#              d rwx r-x  r-x      # r 可读     w 可写    x 可执行   -没权限
#
#              第一个位置代表文件类型    # -普通文件  d文件夹  l软连接
#
#              后面每3组 每一组代表身份的权限
#
#                 第一组 代表用户的权限 user
#                 第二组 代表组的权限   group
#                 第三组 其他人权限     other
#
#             3 更改文件权限
#
#                 r 4     w 2     x 1     rwx 4+2+1
#
#                 chmod u-w 文件名
#
#                 chmod g-wx 文件名
#
#                 chmod o-r 文件名
#
#                 chmod g+wx
#
#                 chmod 777 文件名
#
#                 chmod 666 文件名
#
#             4 修改文件所属用户所属组
#
#                 chown 用户 文件名    改变文件的所属用户
#                 chgrp 组   文件名    改变文件的所属组
#
#             5 修改用户所在的组
#
#                 usermod -g 组名 用户名
#
#         12 软连接
#
#             1 作用
#
#                 快捷方式
#
#             2 创建软连接
#
#                 ln -s 目标文件 想要创建软连接的文件路径
#
#         13 添加到path系统环境变量
#
#             注意：
#                 path环境变量放的是目录绝对路径
#
#         14 ps1变量
#
#             0 查看ps1 变量
#
#                 echo $ps1
#
#             1 作用
#
#                 命令提示符更改（改变 zhengyu@zhengyu-OEM 的显示）（默认退出绘画更改失效）
#
#             2 全剧配置
#
#                 1 文件位置
#
#                     /etc/profile    # 电脑每次启动都会加载它
#
#                 2
#
#             3 修改变量
#
#                 [root@oldboy_python ~]# echo $PS1
#                 [\u@\h \W]\$
#
#                 可以自行调整全局变量/etc/profile文件用于永久生效 PS1='[\u@\h \W\t]\$'
#                 \d　　日期
#                 \H　　完整主机名
#                 \h　　主机名第一个名字
#                 \t　　时间24小时制HHMMSS
#                 \T　　时间12小时制
#                 \A　　时间24小时制HHMM
#                 \u　　当前用户账号名
#                 \v　　BASH的版本
#                 \w　　完整工作目录
#                 \W　　利用basename取得工作目录名
#                 \#　　下达的第几个命令
#                 \$　　提示字符，root为#，普通用户为$
#                 PS1 > 变量名
#                 $PS1 > 查看变量内容
#                 PS1=新内容 重新赋值
#
#
#         15 tar解压命令
#
#             1 作用
#
#                 解压或压缩包
#
#             2 使用
#
#                 1 解压文件
#
#                     tar -xf 包名     # -x解包 f指定文件
#                     tar -cf  目录或文件名  # -c压缩
#                     tar -xvf 包名   # v 显示解压过程
#                     tar -cf 路径 文件  # 压缩文件到指定路径下
#
#         16 netstat命令
#
#             1 作用
#
#                 查看系统网络状态信息
#
#                 0.0.0.0 地址代表了 127.0.0.1和本机局域网ip地址
#
#             2 使用
#
#                 netstat -tunlp
#
#         17 ps命令
#
#             1 作用
#
#                 查看系统中的进程状态
#
#             2 使用
#
#                 ps -aux
#
#         18 kill命令
#
#             1 作用
#
#                 根据pid号杀死进程
#
#             2 使用
#
#                 kill 进程号
#
#                 kill -9 进程号 # 强制杀掉进程
#
#         19 kilall
#
#             1 作用
#
#                 根据名字杀死进程以及进程相关信息
#
#         20 SELinux
#
#             0 概念
#
#                 linux防火墙
#
#                     如果不关闭防火墙, 很可能运行django, nginx, mysql的时候，防火墙可能
#                     会阻挡端口流量的 出口，也会阻挡外来请求的入口
#
#             1 作用
#
#                 防火墙
#
#             2 使用
#
#                 0 查看防火墙状态
#
#                     getenforce
#
#                 1 临时关闭防火墙
#
#                     settenforce 0
#
#                 2 永久关闭防火墙
#
#                     配置 /ect/selinux/config
#
#                         SELINUX=disabled
#
#             3 关闭软件防火墙（iptables）
#
#                 1 查看防火墙
#
#                     iptables -L
#
#                 2 清空防火墙规则
#
#                     iptables -F
#
#                 3 关闭防火墙软件服务
#
#                     systemctl stop filewalld
#
#                 4 永久关闭防火墙服务
#
#                     systemctl disable firewalld
#
#             4 硬件防火墙（F5）
#
#         21 Linux中文显示设置（防止中文乱码）
#
#             1 修改配置文件/etc/locale.conf
#
#                 LANG=“zh_CN.UTF-8”
#
#             2 激活文件配置
#
#                 source /ect/locale.conf
#
#             2 查看系统语言变量命令
#
#                 locale
#
#         22 df命令
#
#             1 作用
#
#                 显示磁盘分区上的可使用的磁盘空间
#
#             2 使用
#
#                 df -h
#
#         23 更改主机名
#
#             hostnamectl set-hostname 名
#
#
#         24 DNS
#
#             1 概念
#
#                 域名系统
#                 万维网上作为域名和IP地址相互映射的一个分布式数据库
#
#             2 域名系统的文件位置
#
#                 /ect/resolv.conf
#
#                     nameserver 127.0.0.53 # 域名服务器
#
#             3 常见服务器域名
#
#                 8.8.8.8
#                 114.114.114.114
#                 223.5.5.5   # 阿里巴巴
#                 223.6.6.6
#                 119.29.29.29  # 腾讯
#
#             4 显示域名解析过程
#
#                 nslookup 网站名
#
#
#         25 crond服务
#
#             1 作用
#
#                 定时作任务， 到了预定的时间自动运行任务
#
#             2 使用
#
#                 1 文件设置
#
#                     /ect/crontab
#
#
#                         分（0-59） 时（0-23） 日（1-31） 月（1-12） 周（0-6） 命令
#
#                         取5个值的交集，5个条件都符合才能正确工作
#
#                 2 编辑任务
#
#                     crontab -e
#
#                         * * * * *  cat xxx文件   # 每分，每小时，每天，每月，每周查看xxx文件
#
#                         30 * * * *   # 表示每小时的第30分钟
#
#                         30,35 * * * *  # 表示每小时的第30分钟和第35分钟
#
#                         30-35 * * * *  # 表示每小时的第31分钟第32分钟第33分钟第34分钟第35分钟
#
#                         */2 * * * * # 表示每2分钟
#
#
#                 3 查看当前有那些定时任务
#
#                     crontab -l
#
#         26 软件包管理
#
#             1 概念
#
#                 程序(软件)组成部分：
#                     二进制程序  可执行命令
#                     库     .so文件
#                     配置文件    .conf
#                     帮助文件    readme    /usr/share/man
#
#             2 linux软件安装的方式
#
#                 1 rpm包安装（需要手动解决软件依赖关系）（一般不用）
#
#                     0 概念
#
#                         特点
#                             源码安装，可扩展第三方功能（可以指定目录安装，configure --prefix=目录路径）
#                             可以通过官网的最新代码，进行安装
#                     1 查询软件是否安装
#
#                         rpm -qi  软件名
#
#                     2 安装软件包
#
#                         rpm -ivh 软件包名
#
#                 2 yum安装（需要下载，自动解决依赖关系）
#
#                     注意：
#                         yum命令只在Fedora和RedHat 以及SUSE中才能使用，ubantu不能使用
#
#                     0 概念
#
#                         特点：
#                             快速，间接，高效，可能版本低，解决依赖关系，（自动安装到某个路径，不可控）
#
#                         yum源  yun软件管理目录在---> /etc/yum.repos.d # 这个目录下xx.repo文件，才会被识别是yum源
#                                                           才会被yum install 工具所调用
#
#                         通过yum 安装的软件, 都可以通过系统服务管理命令，来管理它的start/stop/restart
#
#                     1 配置yum源
#
#                         1 先备份原来的源
#
#                             /etc/yum.repos.d
#
#                         2 找到官方镜像源地址 https://opsx.alibaba.com/mirror
#
#                             找到系统对应版本 点击帮助 找到对应版本 复制命令，系统下执行命令
#
#                         3 清理软件源
#
#                             yum clean all
#
#                         4 生成新的yum仓库缓存
#
#                             yum makecache
#
#                         5 安装一个第三方额外仓库源（epel源）
#
#                             1 作用
#                                 如果上面配置的源找不到软件，就在这个第三方仓库中找
#                                 yum install -y epel-release
#                     2 例子 nginx软件控制命令
#
#                         1 启动nginx服务
#
#                             systemctl start nginx
#
#                         2 查看nginx服务状态
#
#                             systemctl status nginx
#
#                         3 停止nginx服务
#
#                             systemctl stop nginx
#
#                 3 源码编译安装（可自定制安装软件的需求，以及软件的功能扩展）
#
#         27 linux安装python3
#
#             1 下载 python3.* tgz包
#                 源代码
#
#             1.5 处理文件 去掉.xz
#
#                 xz -d 包名
#             2 解压
#
#                 tar -xf 包名
#
#             3 解决编译安装的python3所需的软件依赖
#
#                 yum install gcc patch libffi-devel python-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel -y
#
#             4 编译安装python3
#
#                 1 调用源码包路径下的configure脚本文件
#
#                     ./configure --prefix=/opt/python36/  # 把python3软件安装在/opt/python36目录下
#
#                 2 执行make指令，开始编译
#
#                     make
#
#                 3 make install 安装软件（此不才是安装软件过程）
#
#                     make install
#
#             5 配置环境变量
#
#                 1 配置python3的目录， 加入环境变量
#
#                     注意
#                         环境变量的查找顺序是有优先级顺序的，并且在配置virtualenv时， 优先
#                             以找到的python环境为base环境
#                         要将python3的目录放到环境变量的第一层
#
#                     1 查看环境变量
#
#                         echo $PATH
#
#                         # /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
#
#                     2 在文件 /ect/profile 中配置环境变量
#
#                         # 将python3的所在目录的绝对路径放到所查找的环境变量的最前面 写入文件中
#
#                         PATH=/opt/python36/bin/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
#
#                     3 激活配置文件
#
#                         source /ect/profile
#
#	  28.0 windows下安装虚拟环境
# 		
#		pip3 install virtualenv
#		pip3 install virtualenvwrapper-win 
#		设置WORKON_HOME环境变量
#		1 创建虚拟环境
#			mkvirtualenv 虚拟环境名
#		2 激活虚拟环境
#			workon 虚拟环境名
#		3 查看所有虚拟环境
#			workon
#		4 退出虚拟环境
#			deactivate
#		5 删除虚拟环境
#			rmvirtualenv 虚拟环境名
#         28 linux安装虚拟环境（推荐安第2个）
#
#             1 虚拟环境安装1
#
#                 0 概念
#
#                     以宿主机的python解释器为主体，然后复制多个虚拟环境
#
#                 1 安装
#
#                     pip3 install virtualenv
#
#                 2 创建虚拟虚拟环境
#
#                     # --no-site-packages # 创建一个干净，隔离宿主机环境的虚拟环境
#                     # --python=python3  # 指定虚拟环境，以哪个解释器为base环境
#
#                     virtualenv --no-site-packages --python=python3 虚拟环境名
#
#                 3 进入创建的虚拟环境目录，进入虚拟环境
#
#                     source activate
#
#                     退出虚拟环境
#
#                         deactivate
#
#
#
#             2 pip3 freeze
#                 0 概念
#                     一次性安装虚拟环境中所有的包
#
#                 1 收集项目中所有的包
#
#                     pip3 freeze > requirements.txt
#
#                 2 安装requirements.txt中所有的包
#
#                     pip3 install -r requirements.txt
#
#         3 虚拟环境安装2 virtualenvwrapper
#
#             1 安装
#                 pip3 install -i https://pypi.douban.com/simple virtualenvwrapper
#
#             2 配置用户环境变量
#
#                 编辑 ~/.bashrc
#                 写入
#                    export WORKON_HOME=~/Envs # 设置virtualenv的统一管理目录
#                    export VIRTUALENVWRAPPER_PYTHON_VIRTUALENV_ARGS='--no-site-packages' # 创建一个干净的跟宿主机没有依赖的虚拟环境
#                    export VIRTUALENVWRAPPER_PYTHON=/opt/python36/bin/python3.6  # 制定python解释器
#                    source /opt/python36/bin/virtualenvwrapper.sh # 执行virtualenvwrapper安装脚本
#
#                 重新登录linux
#
#             1 使用
#
#                 1 创建虚拟环境
#
#                     mkvirtualenv 名
#
#                 2 查看虚拟环境
#
#                     lsvirtualenv
#
#                 3 进入虚拟环境
#
#                     workon 名
#
#                 4 删除虚拟环境
#
#                     rmvirtualenv 名
#
#                 5 直接进入虚拟环境目录
#
#                     cdvirtualenv
#
#                 6 直接进入pip3软件包目录
#
#                     cdsitepackages
#
#
#         29 lrzsz（windows和linux文件上传和下载）
#
#            1 概念
#
#                 上传文件到服务器的软件
#
#            2 安装
#
#                 yum install lrzsz -y
#
#            3 下载文件
#
#                 1 sz 文件名    # 从linux往windows下载
#
#
#            4 上传文件
#
#                 1 rz+回车  # 从windows往linux上上传
#
#         30 xftp（推荐使用）
#
#
#         31 安装mariadb
#             0 windows安装
# 		下一步
#		配置环境变量 path变量中 配置mariadb安装路径
#             1 概念
#
#                 mysql已经被oracle收购，他即将闭源，马上就要开始收费
#                 因此还想免费使用开源的数据库mysql，就在centos7上，将
#                 mysql分支位mariadb，完全兼容mysql，包括API和命令行
#
#
#             2 安装（在centos7底下）
#
#                 1 安装方式一
#
#                     通过yum源去下载（可能第三方版本较低，软件不全）
#
#                         yum install mariadb-server
#                 2 安装方式二(推荐)
#
#                     通过mariadb官方的yum源去下载
#
#                         1 配置文件
#
#                             vi /etc/yum.repos.d/MariaDB.repo
#
#                         2 配置文件下写入
#                             [mariadb]
#                             name = MariaDB
#                             baseurl = http://yum.mariadb.org/10.1/centos7-amd64
#                             gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
#                             gpgcheck=1
#                         3 安装
#
#                             yum install MariaDB-server MariaDB-client
#
#                         4 启动
#
#                             通过yum安装的软件可使用通用命令
#
#                                 # systemctl start/stop/restart/status 软件名
#             3 启动数据库
#
#                 systemctl start mariadb
#
#             4 初始化数据库
#
#                 1 执行命令初始化
#
#                     mysql secure installation
#
#                     初始密码为空 ，按空格就行
#                     会提示设置密码
#                     会提示是否删除匿名用户 yes
#                     会提示不允许root远程登录 no
#                     是否删除测试数据库 yes
#                     是否立即刷新表  yes
#                 2 登录mysql对用户进行授权
#
#                     # # 对root用户授权所有权限root拥有的所有主机授权用密码验证（要不然windows连不上）
#                     grant all privileges on *.* to root@"%" identified by '密码' # 远端登录密码
#
#                 3 登录mysql刷新授权表
#
#                     flush privileges;
#
#             6 使用window登录linux段数据库
#                 1 windows 需要安装mysql （不需要启动mysql服务）
#                 2 linux 需要关闭防火墙规则
#                 3 连接
#                     mysql -uroot -p -h linuxip地址  # 在安装mysql的bin目录下执行
#
#             7 数据库操作
#
#                 1 进入数据库
#
#                     mysql -uroot -p
#
#                 2 修改本机登录密码
#
#                     set password = PASSWORD('新密码')
#
#                 3 创建普通用户
#
#                     create user 用户名@'ip地址' identified by '密码'
#
#                     如果密码简单数据库会提示不能使用，如果硬要使用简单密码
#
#                         set global validate_password_policy=0;  # 关闭密码策略可设置简单密码
#
#                 4 对普通用户授权
#
#                     grant 权限 on 数据库.表名 to 账户@ip
#                     grant 权限 on 数据库.* to 账户@ip
#                     grant all privileges on *.* to 账户@ip
#
#                     权限
#                         create, select, insert
#             8 数据库中文配置(以后创建数据库就不用指定编码格式了)
#
#                 1 查看数据库编码
#
#                     \s
#
#                 2 /etc/my.cnf
#
#                     写入
#                         [mysqld]
#                         character-set-server=utf8
#                         collation-server=utf8_general_ci
#                         log-error=/var/log/mysqld.log
#                         [client]
#                         default-character-set=utf8
#                         [mysql]
#                         default-character-set=utf8
#
#                 3 重启 mariadb
#
#                     systemctl restart mariadb
#
#             9 数据库备份与恢复
#
#                 1 备份数据库
#
#                     mysqldump -uroot -p --all-database > 路径/db.dump
#
#                 2 想数据库中导入信息
#
#                     第一种 mysql中
#                         source 备份的文件
#                     第二种 terminal中
#                         mysql -uroot -p < 备份的文件
#
#                 3 概念
#                     1 如果数据库启动不了
#
#                         mysql的数据文件都放在/var/lib/mysql/*中，所有的db新型，以及
#                         账号密码信息
#                         删除此目录下的所有文件(记住备份)
#
#             10 mysql主从复制
#
#                 1 概念
#
#                     通过binlog日制复制到需要同步的从服务器上
#                     在复制过程中，一台服务器充当主服务器，接受来自
#                     用户的内容更新，而一个或多个其他服务器充当从服务器，
#                     接受来之主服务器上的binlog文件的日制内容，重新
#                     更新到从服务器，使得主从服务器达到数据一致
#
#                     分类
#                         一主 一从
#                         一主 多从
#                         一主 一主
#
#                     流程
#
#                         1 主服务器写入数据，将变动的数据，写入sql语句到一个binlog中
#                         2 从服务器指定和谁同步，开启线程读取主服务器binlog记录
#                         3 从服务器将将变动削弱到自己的relaylog日志中，然后将
#                             变动的sql在自己的服务器中再执行一次
#
#                 1 使用
#
#                     1 修改配置文件/etc/my.cnf（作用是产生二进制log-bin文件）
#
#                         [mysqld]
#                         server-id=1         # 服务器的唯一标识（主从之间必须不同）
#                         log-bin=mysql-bin   # 执行生成日志文件的名字
#
#
#                     2 重启mariadb
#
#                         systemctl start mariadb
#
#
#                     3 可查看生成的logbin文件
#
#                         mysql下
#                             show master status
#
#                     4 创建主从同步的普通账号（因位root权限过大，有时候可能会发生问题）
#
#                         1 创建用户
#
#                             create user 'xx@ip' identified by '密码'
#
#                         2 授权
#
#                             grant replication slave on *.* to '用户@ip' # 授予从库的身份
#
#                         3 使连个数据库在同一个基准点（备份导入数据库）
#
#                         4 实现对主数据库锁表只读（防止数据写入，数据复制失败）
#
#                             flush table with read lock;
#
#                         5 解锁锁表
#
#                             unlock tables;
#
#                         6 设置从服务器
#
#                             1 配置文件
#
#                                 /etc/my.cnf中
#
#                                     [mysqld] 下写入
#                                     server-id=2
#                             2 重启数据库
#
#                                 systemctl restart maraidb
#
#                             3 查看从服务器的阐述
#
#                                 show variables like 'log_bin'
#                                 show variables like 'server_id'
#
#                             4 通过命令开启主从同步技术
#                                 mysql下
#                                     change master to master_host='ip地址',
#                                     master_user='创建的用于主从用户',
#                                     master_password='创建的用于主从用户的密码',
#                                     master_log_file='主服务器binlog的文件名',
#                                     master_log_pos=binlog文件新型的position的值;
#
#                             5 刷新权限
#
#                                 flush privileges;
#
#                             6 打开同步
#
#                                 mysql下
#
#                                     start slave;
#
#                             7 检查是否开启成功
#
#                                 show slave status\G
#
#                                 属性
#                                     Slave_IO_Runing:yes
#                                     Slave_SQL_Running:yes
#                                     说明开启成功
#         32 redis安装
#
#             1 安装
#                 通过源码安装rpm
#
#                     1 获取源码包
#
#                        wget http://download.redis.io/releases/redis-5.0.4.tar.gz
#
#                     2 解压包
#
#                         tar xzf redis-3.0.6.tar.gz
#
#                     3 cd到解压的目录下执行命令
#
#                         make && make install  # 编译且安装
#
#                     4 安装编译完成之后，redis会默认添加命令道环境变量/usr/local/bin下
#
#             2 配置
#
#                 1 修改redis目录中的redis.conf文件
#
#                     其中bind 127.0.0.1改成0.0.0.0 # 为了我的window能连上linux
#
#                     其他
#                         protected-mode yes  # redis的安全机制，如果不设置，不让远程连接
#                         daemonize no  # 代表后台启动
#
#                 2 自己配置redis文件
#                     1 处理原文件redis.conf
#                         1 备份
#                             redis.conf.bac
#                         2 过滤掉文件中的注释项
#                         3 过滤掉文件中的空行
#                         4 将过滤完的内容写入新文件
#                             grep -v '^#' redis.conf.bac |grep -v '^$' > redis.conf
#
#                     2 将redis.conf改成
#
#                         bind 0.0.0.0  #绑定ip
#                         port 6379 #端口号
#                         daemonize yes #后台运行redis
#                         pidfile /data/6379/redis.pid # 将redis进程的id写入到redis.pid这个文件
#                         loglevel notice # 日志级别
#                         logfile "/data/6379/redis.log" #写入log文件的位置
#                         protected-mode yes #redis3.0之后的安全模式可能会阻挡远程连接
#                         requirepass  密码 # 安全模式下设置的密码
#                                         设置requirepass后 虽然能连接数据库但是测试ping会出现
#                                         NOAUTH Authentication required
#                                         需要验证
#
#                                             auth 密码
#
#                     3 创建配置中的目录
#             3 启动
#
#                 指定配置文件启动
#
#                     redis-server redis.conf
#             4 进入redis
#                 redis-cli
#
#             5 直接用windows下的cmd连接linux（前提windows安装了redis）
#                 redis-cli -h ip地址
#
#             6 redis的可执行文件
#
#                 ./redis-benchmark //用于进行redis性能测试的工具
#                 ./redis-check-dump //用于修复出问题的dump.rdb文件
#                 ./redis-cli //redis的客户端
#                 ./redis-server //redis的服务端
#                 ./redis-check-aof //用于修复出问题的AOF文件
#                 ./redis-sentinel //用于集群管理
#
#             7 相关命令
#
#                 1 关闭redis
#                     redis-cli shutdown
#                 2 查询redis中设置的密码参数（redis下）
#                     CONFIG get requirepass
#
#                 3 进入带有密码的redis的另一种方式（省了 在redis下auth 密码 验证）
#
#                     redis-cli -a 密码
#             8 redis的多实例功能
#
#                 1 概念
#
#                     在一个机器上，启动多个redis服务端
#
#                 1 配置
#
#                     1 新配置文件
#                       xin_redis.conf
#                     2 文件配置中写入（改个端口，改个进程id写入文件，改个日志写入文件即可，其他一样）
#                         bind 0.0.0.0  #绑定ip
#                         port 6379 #端口号
#                         daemonize yes #后台运行redis
#                         pidfile /data/6379/redis.pid # 将redis进程的id写入到redis.pid这个文件
#                         loglevel notice # 日志级别
#                         logfile "/data/6379/redis.log" #写入log文件的位置
#                         protected-mode yes #redis3.0之后的安全模式可能会阻挡远程连接
#                         requirepass  密码 # 安全模式下设置的密码
#                                         设置requirepass后 虽然能连接数据库但是测试ping会出现
#                                         NOAUTH Authentication required
#                                         需要验证
#
#             9 发布订阅
#
#                 1 概念
#
#                     订阅者和发布者和频道名
#                 2 命令
#
#                     PUBLISH channel msg
#                         将信息 message 发送到指定的频道 channel
#
#                     SUBSCRIBE channel [channel ...]
#                         订阅频道，可以同时订阅多个频道
#
#                     UNSUBSCRIBE [channel ...]
#                         取消订阅指定的频道, 如果不指定频道，则会取消订阅所有频道
#                     PSUBSCRIBE pattern [pattern ...]
#                         订阅一个或多个符合给定模式的频道，每个模式以 * 作为匹配符，比如 it* 匹配所
#                         有以 it 开头的频道( it.news 、 it.blog 、 it.tweets 等等)， news.* 匹配所有
#                         以 news. 开头的频道( news.it 、 news.global.today 等等)，诸如此类
#                     PUNSUBSCRIBE [pattern [pattern ...]]
#                         退订指定的规则, 如果没有参数则会退订所有规则
#                     PUBSUB subcommand [argument [argument ...]]
#                         查看订阅与发布系统状态
#                     注意：使用发布订阅模式实现的消息队列，当有客户端订阅channel后只能收到后续发布到该频道的消息，之前发送的不会缓存，必须Provider和Consumer同时在线。
#                 3 使用
#
#                     1 一个发布者两个订阅者
#
#                         1 启动三个窗口连接redis服务端
#                         1 订阅电台
#                             2个窗口 都执行命令
#
#                                 SUBSCRIBE 电台名
#                         2 往电台发布消息
#
#                             在除了订阅的另一个窗口
#
#                                 PUBLISH 电台名 消息
#
#                     2 订阅一个或多个符合订阅模式的频道
#
#                         PSUBSCRIBE 正则
#                         如
#                           PSUBSCRIBE ling*   # 订阅带有ling的多个有电台名
#             10 redis持久化（线上一般两种方式都用）
#
#                 1 概念
#                     一旦服务器进程退出，数据库的数据就会丢失，为了解决这个问题，
#                     提出了数据库持久方案
#
#                 2 持久化方式
#
#                     1 RDB（速度快适合做备份）
#                         1 概念
#                             将redis在内存中的状态保存到硬盘中
#                             在执行的时间间隔内生成数据集的时间点快照
#                             持久化产生的RDB是一个经过压缩的二进制文件
#                         2 方法
#                             1 手动执行持久化
#                                 命令
#                                     save
#                             2 定期执行持久化
#
#                                 redis.conf文件中配置
#
#                                     dir /data/6379/      # 持久化文件存储目录
#                                     dbfilename dbmp.rdb  # rdb持久化文件
#                                     save 900 1     # 若果900秒内有1个修改操作，进行持久化
#                                     save 300 10    # 如果300秒内有10个修改操作，进行持久化
#                                     save 60 10000  # 如果60秒内有10000个修改操作，进行持久化
#
#
#                     2 AOF
#
#                         1 概念
#                             记录服务器执行的所有变更操作命令
#                             相对于与rdb最大程序保证数据不丢，但日志记录非常大
#
#                             流程
#                                 redis-cline 写入数据--> redis-server 同步命令 > AOF文件
#
#                         1 配置
#
#                             redis.conf文件中
#
#                                 appendonly yes
#                                 # appendfsync 有三个模式可写成（选择一个即可）
#                                   appendfsync always # 总是修改的操作
#                                   appendfsync everysec   # 美妙做一次持久化
#                                   appendfsync no # 依赖于系统自带的缓存大小机制（几乎不用）
#
#                 3 regis 切换RDB备份到AOF备份（此步重启后，rdb持久化完全切换aof持久化，且数据保持一致）
#
#                     1 配置redis.conf,确保开启rdb功能
#                     2 启动redis服务端
#                         redis-server redis.conf
#                     3 插入redis数据，通过save命令，强制写入持久化rdb文件
#                     4 通过命令，切换到aof持久化（此步临时生效，必须将AOF的配置，写入redis.conf）
#                         CONFIG set appendonly yes  # 开启AOF功能
#                         CONFIG set save ""  # 关闭RDB功能
#                     5 修改配置文件，添加aof参数
#                     6 重启redis服务
#
#             11 redis主从同步，身份切换
#
#                 1 主从同步
#                     1 概念
#
#                         redis集群中的数据库复制是通过主从同步来实现的
#                         原理
#                             1 从服务器向主服务器发送SYNC同步命令
#                             2 接受到SYNC命令的主服务器会调用BGSAVE命令，创建一个RDB文件，通过缓存区记录接下来执行的所有写命令
#                             3 当主服务器执行BGSAVE命令时， 它会向从服务器发送RDB文件，而从服务器则会接收并下载这个文件
#                             4 主服务器将缓冲区的所有写命令发送给从服务器执行
#                     2 配置
#
#                         1 主的服务
#                             默认属性为主服务器
#
#                         2 从的配置文件
#                             1 进入从服务器
#                                 redis-cli -p 端口
#                             2 指定为从服务
#                                 SLAVEOF ip地址 端口
#                     3 启动
#
#                     4 查看redis服务信息
#                         redis-cli -p 端口号 info Replication
#
#                 2 手动切换主从身份
#
#                     如果主身份的服务器挂掉了
#
#                     1 去掉从服务器的身份（就变成主服务）
#
#                         redis-cli -p 端口号 slaveof no one
#
#                     2 将其他从的服务器，的主人改变为上边的服务
#
#                         redis-cli -p 端口号 slaveof ip地址
#
#                 3 通过配置文件决定主从身份
#
#                     从的配置文件中
#
#                         slaveof IP地址 端口
#
#
#
#         33 nginx
#
#             1 概念
#
#                 web服务器
#
#                     nginx web server 服务端
#
#                     dns解析流程
#
#                         1 用户输入网址
#                         2 浏览器会寻找客户端机器上的hosts文件
#                         3 如果hosts中位没找到，就去客户端机器的dns的缓存中（LDNS）寻找解析记录
#                         4 如果LDNS中没有找到，就去客户端机器中指定的dns服务器中寻找解析记录
#                         5 如果找到 dns服务器会将查找到的ip和域名对应的记录，返回给浏览器就会访问域名对应的ip
#                             此时操作系统会将这条解析记录，写入到本地dns缓存中 LDNS
#                         linxdns服务器文件位置
#
#                             /ect/resolv.conf # 只能写两个
#
#                                 nameserver x.x.x.x # 主dns服务器
#                                 nameserver y.y.y.y # 备dns服务器
#                         相关命令
#
#                             nslookup  网址 # 域名服务器查找
#
#                     web服务端口
#
#                         web默认服务端口是80，https默认端口是443，用户预付 ，网银相关业务
#
#                     静态网页资源
#
#                         没有后台数据库，不包含程序，不可交互的网页
#                         纯文本文件 html htm xml js css
#                         图片等 jpg gif bmp txt ppt
#                         视频等 mp4 avi flv
#
#                     网站浏览术语
#
#                         IP
#                             公网ip相同ip地址的客户端访问网站页面一天内只会被计算一次
#                         pv
#                             页面浏览量，不管ip地址相不相同
#                         uv
#                             同一个客户端访问网站被计算为一个访客
#                         并发数
#                             炒作系统同时能处理的请求数量
#                         响应时间
#                             一个请求从开始到最后收到响应数据所花费的总体时间
#                         QPS
#                             每秒查阅数
#
#
#                 web服务器软件有
#                     IIS
#                         windows的web服务器软件
#                     Nginx
#                         linux下的软件
#                         Tengine
#                         新一代的高性能的web服务器
#                         反向代理
#                         负载均衡
#                         支持高并发，能支持几万并发连接
#                     Apache
#                         linux下的软件
#                         上个时代的，老企业会选择apache
#
#                 web服务器 处理静态资源的请求（jpg，MP3。。）
#                 不能处理动态资源请求（带有参数的请求）
#                 流程：
#                     1 浏览器发送获取图片的请求，
#                     2 通过dns解析到ip，这个ip对应者服务器
#                     3 服务器通过查询找到图片，将图片返回给浏览器（查询的事是nginx做的）
#
#                 web服务器和web框架的关系
#
#                     1 web服务器（nginx）：接受HTTP请求并返回数据
#                     2 web框架（django, flask）,开发web应用程序，处理接收到的数据
#
#
#
#             2 安装和启动
#
#                 1 安装依赖软件
#
#                     yum install gcc patch libffi-devel python-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel openssl openssl-devel -y
#
#                 2 下载源码包
#
#                     wget -c https://nginx.org/download/nginx-1.12.0.tar.gz
#
#                 3 解压源码包
#
#                     tar -zxvf nginx-1.12.0.tar.gz
#
#                 4 释放makefile（开启nginx状态监测功能）
#
#                     ./configure --prefix=/opt/nginx1-12/ --with-http_ssl_module --with-http_stub_status_module
#
#                 5 编译安装
#
#                     make && make install
#
#                 6 /opt/nginx1-12目录
#                     conf 配置文件目录
#                         nginx.conf  # nginx的主配置文件
#                     html # 存放网页跟目录文件
#                         *.html *.gif *.jpg
#                     logs # 日志目录
#                     sbin # nginx启动脚本目录
#
#                 7 在/opt/nginx1-12/sbin下 启动nginx服务
#
#                     ./nginx
#
#                 8 检查端口，进程，通过浏览器访问nginx页面
#                     192.168.1.108：80
#
#                     安装完nginx后源码文件包可删除nginx-1.12.0
#
#
#                 9 相关命令
#
#                    1 启动nginx
#
#                         ./nginx
#
#                    2 停止nginx
#
#                         ./nginx -s stop
#
#
#
#                    3 平滑重启(修改配置文件，不重启服务，就加载配置且生效)
#
#                         ./nginx -s reload
#
#                    4 检测nginx.conf语法的正确性
#
#                         ./nginx -t
#
#             3 nginx的配置文件
#
#                 #user  nobody;         # nginx进程所使用的用户
#                 worker_processes  1;   # nginx运行的work进程数量（建议与cpu数量一致）
#                 #error_log  logs/error.log;     # 指定错误日志的存放路径
#                 #error_log  logs/error.log  notice;
#                 #error_log  logs/error.log  info;
#                 #pid        logs/nginx.pid;     # 服务员运行后产生的pid进程号
#
#                 events {                        # 事件模块
#                     worker_connections  1024;   # 每个工作进程支持最大连接数
#                 }                               # 事件驱动也写在这里 入epoll
#
#                 http {                          # http内核模块
#                     include       mime.types;
#                     default_type  application/octet-stream;
#                     #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
#                     #                  '$status $body_bytes_sent "$http_referer" '
#                     #                  '"$http_user_agent" "$http_x_forwarded_for"';
#                     #access_log  logs/access.log  main;
#                     sendfile        on;
#                     #tcp_nopush     on;
#                     #keepalive_timeout  0;
#                     keepalive_timeout  65;
#                     #gzip  on;
#                     # 虚拟主机1
#                     server {                    # 使用server配置网站，每一个server｛｝代表一个网站（简称虚拟主机）
#                         listen       80;        # 监听端口 默认80
#                         server_name  localhost;     # 提供服务的域名或主机名或ip
#                         #charset koi8-r;
#                         #access_log  logs/host.access.log  main;  # 访问日志功能，能记录访客的记录
#                         location / {            # 控制网站访问路径
#                             root   html;        # 存放网站代码路径
#                             index  index.html index.htm; # 服务器返回的默认页面文件
#                         }
#                         #error_page  404              /404.html;
#                         # redirect server error pages to the static page /50x.html
#                         #
#                         error_page   500 502 503 504  /50x.html;  # 指定错误代码， 统一定义错误页面， 错误代码重定向到新的location
#                                                                   # /50x.html 是以nginx的root参数，指定的网页根目录
#                         location = /50x.html {
#                             root   html;
#                         }
#                         # proxy the PHP scripts to Apache listening on 127.0.0.1:80
#                         #
#                         #location ~ \.php$ {
#                         #    proxy_pass   http://127.0.0.1;
#                         #}
#                         # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
#                         #
#                         #location ~ \.php$ {
#                         #    root           html;
#                         #    fastcgi_pass   127.0.0.1:9000;
#                         #    fastcgi_index  index.php;
#                         #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
#                         #    include        fastcgi_params;
#                         #}
#                         # deny access to .htaccess files, if Apache's document root
#                         # concurs with nginx's one
#                         #
#                         #location ~ /\.ht {
#                         #    deny  all;
#                         #}
#                     }
#
#                     # another virtual host using mix of IP-, name-, and port-based configuration
#                     # 虚拟主机2
#                     #server {
#                     #    listen       8000;
#                     #    listen       somename:8080;
#                     #    server_name  somename  alias  another.alias;
#                     #    location / {
#                     #        root   html;
#                     #        index  index.html index.htm;
#                     #    }
#                     #}
#                     # HTTPS server
#                     #
#                     #server {
#                     #    listen       443 ssl;
#                     #    server_name  localhost;
#                     #    ssl_certificate      cert.pem;
#                     #    ssl_certificate_key  cert.key;
#                     #    ssl_session_cache    shared:SSL:1m;
#                     #    ssl_session_timeout  5m;
#                     #    ssl_ciphers  HIGH:!aNULL:!MD5;
#                     #    ssl_prefer_server_ciphers  on;
#                     #    location / {
#                     #        root   html;
#                     #        index  index.html index.htm;
#                     #    }
#                     #}
#                 }
#
#             4 nginx多虚拟主机，通过nginx.conf配置
#
#                 # 虚拟主机1
#                 server {                    # 使用server配置网站，每一个server｛｝代表一个网站（简称虚拟主机）
#                         listen       80;        # 监听端口 默认80
#                         server_name  www.test1.com;     # 提供服务的域名或主机名
#                         #charset koi8-r;
#                         #access_log  logs/host.access.log  main;  # 访问日志功能，能记录访客的记录
#                         location / {            # 控制网站访问路径
#                             root   html;        # 存放网站代码路径
#                             index  index.html index.htm; # 服务器返回的默认页面文件
#                         }
#                 # 虚拟主机2
#                 server {                    # 使用server配置网站，每一个server｛｝代表一个网站（简称虚拟主机）
#                         listen       80;        # 监听端口 默认80
#                         server_name  www.test2.com;     # 提供服务的域名或主机名
#                         #charset koi8-r;
#                         #access_log  logs/host.access.log  main;  # 访问日志功能，能记录访客的记录
#                         location / {            # 控制网站访问路径
#                             root   html;        # 存放网站代码路径
#                             index  index.html index.htm; # 服务器返回的默认页面文件
#                         }
#             5 域名解析本地化（骚操作）
#
#                 自己配置的nginx中的域名，用windows访问linux中配置的域名找不到
#                 所以在windows中的hosts文件中添加
#                 hosts 文件就是一个本地dns强制解析的文件 dns的解析顺序先去hosts文件中找，找不到去公网中找
#                 写入
#
#                     www.test1.com  192.168.1.107  # windows就能访问linux中nginx配置的域名了
#             6 nginx状态信息（status）配置
#
#                 1 配置
#                     server {                    # 使用server配置网站，每一个server｛｝代表一个网站（简称虚拟主机）
#                         listen       80;        # 监听端口 默认80
#                         server_name  www.test1.com;     # 提供服务的域名或主机名
#                         #charset koi8-r;
#                         #access_log  logs/host.access.log  main;  # 访问日志功能，能记录访客的记录
#                         location / {            # 控制网站访问路径
#                             root   html;        # 存放网站代码路径
#                             index  index.html index.htm; # 服务器返回的默认页面文件
#                         }
#                     写入 location /status{
#                         stub_status on;
#                     }
#                 2 进入 xxx/status
#
#                     会出现
#
#                         Active connections:700 # 正在处理活动连接的数量700个
#                         server accepts handled requests  # 服务器接收的请求数
#                             数字1  数字2  数字3           # 数字1 启动到现在处理的请求数字
#                                                         # 数字2 共同创建的捂手次数
#                                                         # 数字3 总共处理的请求数字
#                         Reading: 0 Writing: 1 Waiting:699 # reading 正在读取的请求数字
#                                                           # writing 正在执行的请求数
#                                                           # waiting 正在等待的请求数
#
#             7 nginx访问日志功能（access_log）
#
#                 1 配置 nginx.conf
#
#                     http{
#                         log_format main '$remote_addr - $remote_user [$time_local] "$request" '
#                                     　　 '$status $body_bytes_sent "$http_referer" '
#                                     　　 '"$http_user_agent" "$http_x_forwarded_for"';
#                         access_log logs/access.log main;
#                     }
#
#                     # 参数
#                         $remote_addr    记录客户端ip
#                         $remote_user    远程用户，没有就是 “-”
#                         $time_local 　　 对应[14/Aug/2018:18:46:52 +0800]
#                         $request　　　 　对应请求信息"GET /favicon.ico HTTP/1.1"
#                         $status　　　  　状态码
#                         $body_bytes_sent　　571字节 请求体的大小
#                         $http_referer　　对应“-”　　由于是直接输入浏览器就是 -
#                         $http_user_agent　　客户端身份信息
#                         $http_x_forwarded_for　　记录客户端的来源真实ip 97.64.34.118
#
#                 2 （可选） 拒绝ip访问
#                     http{
#                         deny ip地址
#                     }
#
#             8 配置文件中location语法
#
#                 1 匹配顺序
#
#                     匹配符 匹配规则 优先级
#
#                     =    精确匹配    1 # www.a.com/
#                     ^~    以某个字符串开头    2 # www.a.com/ss/
#                     ~    区分大小写的正则匹配    3 #
#                     ~*    不区分大小写的正则匹配    4 # www.a.com/xxx.gif
#                     !~    区分大小写不匹配的正则    5
#                     !~*    不区分大小写不匹配的正则    6
#                     /    通用匹配，任何请求都会匹配到    7
#
#             9 nginx代理
#
#                 1 概念
#
#                     1 正向代理
#
#                         代理的是客户端
#
#                         用户--通过互联网-->通过代理服务器a-->向服务器请求资源
#
#                         代理服务器将资源->返回给客户端
#
#                     2 反向代理
#
#                         代理的是服务端
#                             # django默认使用的是wsgigiref单机模块，性能很低，因此用户
#                                 # 不会直接请求django，通过uwsgi一个软件，支持高并发软件，
#                                 # 启动多进程处理请求，uwsgi不解析django的静态文件语法
#                                 # 因此通过nginx处理django项目的静态文件
#                             用户向django服务器请求数据--->nginx服务器-->django服务器
#                 2 配置
#
#                     location{
#                         proxy_pass 网址  #  直接向转发请求 向该 网址 请求资源
#                     }
#
#             10 nginx负载均衡
#
#                 1 概念
#
#                     集群
#                         一堆服务器合作做同一件事
#                         多个相互独立的计算机，每台计算机独立运行各自的服务，每台计算机
#                         彼此通信，向用户提供程序
#
#                         特点 高性能 价格有效性 可伸缩性 高可用性 透明性
#                     流程
#
#                         客户端发送请求-->通过nginx负载均衡器的反向代理池--向django服务请求数据
#
#                 2 配置（默认轮寻从上到下）
#
#                     nginx.conf > http区域中
#                         1 定义负载均衡池
#                             upstream 名{         # 和server同级
#                                 server 地址和端口1
#                                 server 地址和端口2
#                             }
#                         2 通过location匹配
#
#                             location / {
#
#                                 ....
#                                 proxy_pass http://名
#                                 include 文件1  # 文件1的配置加载到当前文件中
#                             }
#                         3 配置文件1 给方向代理加上参数功能，即设置请求头相关参数（注意路径）
#
#                             proxy_set_header Host $http_host; # 给代理请求头加上来自哪个主机
#                             proxy_set_header X-Real-IP $remote_addr; # 给代理请求头加上客户端真是id
#                             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; #
#
#                             proxy_connect_timeout 30; # 设置代理超时时间 秒
#                             proxy_send_timeout 60;
#                             proxy_read_timeout 60;
#
#                             proxy_buffering on;
#                             proxy_buffer_size 32k;
#                             proxy_buffers 4 128k;
#
#                 3 配置复制均衡池中的权重
#
#                     1 比例调度算法 weight
#                         upstream 名{
#                             server 地址和端口1 weight = 数字
#                             server 地址和端口2 weight = 数字
#                         }
#                     2 ip_hash 每个请求访问的ip的hash结果分配，同一ip固定访问一个后端服务器
#                         upstream 名{
#                             ip_hash
#                             server 地址和端口1
#                             server 地址和端口2
#                         }
#                     3 url_hash 按照访问的rul结果来分配请求
#                     4 least_conn 最少连接数，哪个机器链接数少就分发
#
#             8 ab压测命令
#
#                 1 概念
#                     测试网站能够经得起发送多少个请求
#
#                 2 安装
#                     ？？
#
#                 3 使用
#
#                     参数
#                         -n 数字  # 一共发起的请求数
#                         -c 数字  # 请求的并发数
#                         -k 长连接
#
#                     命令
#
#                         ab -kc 1000 -n 100000 网址
#
#         34 项目发布
#
#             1 概念
#
#                 WSGI
#                     是web服务器网管接口，描述了web服务器如何与web应用程序通信
#
#                     支持WSGI的服务器
#
#                         wsgiref
#                             python自带的web服务器
#
#                         Gunicorn
#                             用于linux python wsgi HTTP
#                             服务器，常用于各种django, flask结合部署服务器
#
#                         mode_wsgi
#
#                             实现了Apache与wsgi应用程序的结合
#
#                         uWSGI
#
#                             C语言开发，快速，自我修复 ，英语python web应用程序的专业部署和开发
#             2 配置开始
#
#                 1 准备python虚拟环境
#                 2 pip安装相关软件
#                 3 解决和数据库连接的相关配置
#                 4 更爱django中settings的ALLOWED_HOSTS = ['*']
#                 5 更改django中settings的DEBUG = False
#                 6 创建数据库，并更新项目模型到数据库中
#                 7 安装uwsgi
#                     pip3 install uwsgi
#                 8 通过uwsgi启动项目(uwsgi不会处理静态文件)
#                     1 普通启动
#                         uwsgi --http :端口号 --module 项目.wsgi
#                             参数
#                                 --http 指明http协议
#                                 --socket 启动一个socket链接
#                                 --wsgi-file 指明一个python应用文件
#
#                     2 热启动服务（不需要重新执行启动命令，使改过的代码生效）
#                         uwsgi --http :端口号 --modele mycrm.wsgi --py-autoreload=1
#
#                     3 通过配置文件启动项目
#
#                         1 概念
#                             uwsgi支持ini，xml多种配置方式
#
#                         2 配置
#
#                             1 创建配置文件xx.ini
#
#                                 [uwsgi]
#
#                                 chdir           = 路径  # 定位到项目第一层的绝对路径
#
#                                 module          = 路径 # 指明项目的wsgi文件路径（以上面定制的绝对路径为起点）
#
#                                 home            = 路径 # 指明虚拟环境的第一层路径
#                                 # process-related settings
#                                 # master
#                                 master          = true
#
#                                 processes       = 1 # 启动多少个进程
#
#                                 socket          = 0.0.0.0:8000 # 如果配置了nginx，使用改行可以
#                                 # http = 0.0.0.0：端口号  # 如果想通过uwsgi直接启动web服务，使用该配置
#                                 # ... with appropriate permissions - may be needed
#
#                                 vacuum          = true # 在退出uwsgi环境后 清空环境变量
#
#                             2 启动
#
#                                 uwsgi --ini uwsgi.ini
#                 9 收集项目中的静态文件(把静态文件放到指定目录)
#
#                     1 django的setting文件中配置
#
#                         STATIC_ROOT = '想放置文件目录的路径'
#                     2 执行命令
#
#                       python3 manage.py collectstatic
#                 10 配置nginx， 配置一个网站入口
#
#
#                     1 概念
#
#                         当用户访问网站ip时候，自动将请求转发给uwsgi
#                         uwsgi处理后，返回给nginx，返回给用户
#
#                     2 配置
#                         1 配置静态文件入口
#
#                             location /static{
#                                 alias /静态文件路径/;
#
#                             }
#
#                         2 配置静态文件入口
#
#                             location /{
#                                 uwsgi_pass xx
#                                 include /opt/nginx1-12/conf/uwsgi_params # 配置项文件路径
#                             }
#
#                 11 启动nginx
#                     uwsgi --ini uwsgi.ini
#                 12 启动nginx
#                     ./nginx
#
#                 13 配置supervisor(管理uwsgi进程)
#
#                     1 安装(不在虚拟环境下安装)
#                         yum install python-setuptools
#                         easy_install supervisor
#
#                     2 使用
#
#                         1 创建配置文件
#                             echo_supervisord_conf > 路径/supervisord.conf
#
#                         2 配置文件
#                             [program:任务名]
#                             command=/uwsgi启动文件路径 --ini /uwsgi的配置文件路径
#                             autorestart=true  # 开启服自动启动uwsgi
#                     3 启动
#
#                     4 相关命令
#
#                         1 启动服务
#
#                             syoervusird -c 配置文件
#
#                         2 管理文件
#
#                             supervisorctl start 任务名
#                             supervisorctl stop 任务名
#
#
#                             supervisorctl start all
#                             supervisorctl stop all
#
#         35 redis哨兵
#
#             1 概念
#
#                 redis-sentinel由于宕机自动主从身份切换
#                 原理就是自动修改配置文件
#                 是一个独立运行的进程，用于多个监控多个主从集群
#                     自动发现master宕机，自动切换slave到master
#
#                 功能
#                     监控redis运行状态，如果出现文件进行处理
#
#             2 相关命令
#
#                 1 查看 redis的哨兵信息
#
#                     redis-cli info sentinel
#
#                 2 启动
#
#                     redis-sentinel 配置文件名 # redis会一起启动
#
#
#
#             3 安装和配置
#
#                 1 配置
#                     可配置多个文件如不同redis端口使用不同的哨兵配置文件
#                     配置文件写入，其他哨兵文件仅为端口不同 日志文件名不同
#
#                         port 26379
#                         dir 路径
#                         logfile '日志文件名'
#                         sentinel monitor 名字 监控的ip地址和端口 2  # 监控哪个主机 2表示判断主节点失效至少多个哨兵监控
#                         sentinel down-after-millisecond 名字 30000 # 用ping来判断30秒内是否能连同，如果不能则去除主从身份
#                         sentinel parallel-syncs 名字 1 # 每次只让一个从节点去复制主的数据
#                         sentinel failover-timeout mymaster 180000 # 故障转移超时时间
#
#         36 redis-cluster配置
#
#             1 概念
#                 工作原理
#                     edis客户端任意访问一个redis实例，如果数据不在该实例中，通过重定向引导客户端访问所需要的redis实例
#
#                 处理内存不够用，用分布式，加机器 把数据分到不同位置
#
#                 数据分布规则
#                     顺序分布
#                         100个数据  1-33一个地方 34-。。一个地方
#                     节点取余分区
#                         hash(key)%3 根据余数是否相同放在一个地方 1 2 0
#                     一致性哈希分区
#                         根据客户端时间顺序表进行取余
#                     虚拟槽分区（redis-cluster）
#                         使用了哈希空间，使用分散度狼嚎的哈希函数把所有数据映射
#                             到一个固定内的整数集合
#                         redis-cluster 槽的范围0~16383
#                         槽是集群内数据管理和迁移的基本单位
#                             0-3276槽      一个地方
#                             。。。
#                             13108 - 16383 一个地方
#
#             2 安装
#
#                 1 条件
#
#                     3个主节点，3个从节点，数量为6个节点才能保证
#
#                 2 配置文件
#
#                     配置文件 6个 xx.conf  仅端口不同
#                     写入
#                         port 7000
#                         daemonize yes
#                         dir "/opt/redis/data"
#                         logfile "7000.log"
#                         dbfilename "dump-7000.rdb"
#                         cluster-enabled yes   #开启集群模式
#                         cluster-config-file nodes-7000.conf　　#集群内部的配置文件
#                         cluster-require-full-coverage no　　#redis cluster需要16384个slot都正常的时候才能对外提供服务，换句话说，只要任何一个slot异常那么整个cluster不对外提供服务。 因此生产环境一般为no
#
#
#                 4 配置ruby环境
#                     wget https://cache.ruby-lang.org/pub/ruby/2.3/ruby-2.3.1.tar.gz
#
#                     #安装ruby
#                     tar -xvf ruby-2.3.1.tar.gz
#                     ./configure --prefix=/opt/ruby/
#                     make && make install
#
#
#
#                     #拷贝ruby命令到path下/usr/local/ruby
#                     cp /opt/ruby/bin/ruby /usr/local/
#                     cp bin/gem /usr/local/bin
#
#
#                     wget http://rubygems.org/downloads/redis-3.3.0.gem
#
#                     gem install -l redis-3.3.0.gem
#
#                     #查看gem有哪些包
#                     gem list -- check redis gem
#                     安装redis-trib.rb命令
#                         配置环境变量
#                         cp /opt/redis/src/redis-trib.rb /usr/local/bin/
#                 5 启动
#                     每个主节点，有一个从节点，代表--replicas 1
#                     redis-trib.rb create --replicas 1 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005
#
#                     #集群自动分配主从关系  7000、7001、7002为 7003、7004、7005 主动关系
#
#                 6 查看
#
#                     redis-cli -p 7000 cluster info
#
#                     redis-cli -p 7000 cluster nodes  #等同于查看nodes-7000.conf文件节点信息
#
#                     集群主节点状态
#                     redis-cli -p 7000 cluster nodes | grep master
#                     集群从节点状态
#                     redis-cli -p 7000 cluster nodes | grep slave
#
#         37 docker
#
#             1 概念
#
#                 将应用程序与程序的依赖，打包在一个文件里，运行这个文件就会生产一个容器，程序
#                 运行在这个容器里，如同在正式物理机上运行一样，有个docker就不用担心环境问题了
#
#                 服务器环境第一代
#                     服务器+centos
#
#                 服务器第二代
#
#                     服务器+windows+wmware
#                     服务器+vmware esxi（企业板虚拟化）+linux
#
#                 服务器第三代
#
#                     服务器+openstatck 云虚拟化
#
#                 服务器第四代
#
#                     服务器+vmware + docker + django运用
#
#                 docker三大概念
#
#                     镜像  只读的魔板
#                     容器
#                     仓库
#
#             2 CentOS安装docker
#                 https://www.cnblogs.com/pyyu/p/9485268.html
#                 1 yum安装
#                     yum install docker* docker-* -y
#
#                 2 启动docker
#                     systemctl start docker
#
#                 3 查看
#                     docker version
#
#                 4 使用
#
#                     docler serrch xx
#                     docker pull xx
#                     docker image ls # 查看镜像
#                     docker ps # 查看docker进程
#                     docker ps -a # 查看所有运行过的docker容器记录
#                 5 Docker镜像加速器
#                     # 更改了docker源
#                     curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://95822026.m.daocloud.io
#
#                 5 相关命令
#
#                     1 增
#
#                         docker run 镜像id/镜像名 # 运行创建一个容器实例
#                         docker pull 下载 下载docker的镜像
#
#                         docker run -it 镜像id  # -i 交互式界面 -t 开启一个终端 会进入到容器空间内
#                         docker run -d centos /bin/sh -c "while true;do echo hello centos; slep 1;done"
#                                 -d 是后天运行
#                                 /bin/sh # 调用shell解释器
#                                 -c 指明一段shell语法
#                     2 删
#
#                         docker rm 容器id # 删除已经停止的容器id
#                         docker rmi 镜像id # 删除一个镜像记录
#
#                         `` # 反引号是取命令的运行结果
#
#                         docker rmi `docker images -aq` # 一次清删除所有镜像记录
#
#
#
#                     3 改
#
#                         docker commit # 提交容器记录，为新的镜像
#
#                         dcker stop 容器id   #
#                         docker start 容器id
#
#                     4 查
#
#                         docker image ls # 查看镜像记录
#                         docker images # 查看镜像记录
#
#                         docker ps # 查看容器记录（正在运行中的容器）
#                         docker ps -a # 查看停止的和在运行的容器记录
#
#
#                         docker logs -f 容器id # 查看正在运行中的 容器内日志
#                             -f 不间断打印
#
#
#                     5 导出docker镜像
#
#                         docker save centos > /opt/centos.tar.gz
#
#                     6 导入docker镜像
#                         docker load < /opt/centos.tar.gz
#
#                     7 不保存记录信息 运行镜像
#
#                         ddocker run -t --rm 镜像名
#
#                     8 进入正在运行的容器当中
#
#                         docker exec -it 镜像名 /bin/bash
#
#                     9 提交自定义镜像文件
#
#                         docker commit 进行id 自定义名字
#
#                     10 外部访问容器
#                         1 下载镜像
#                             docker pull training/webapp
#                         2 运行镜像
#                             docker run -d -P 进行id python app.py
#
#                         -p 宿主机端口：容器内端口
#                         -P 随机映射容器内端口
#
#                     11 利用dockerfile定制镜像
#
#                         1 概念
#
#                             定义每一层的配置，文件，如果可以吧每一层修改，安装，构建，操作的命令
#                             都可以写入到一个脚本，这个脚本就是dockerfile
#
#                             linux中执行xx.sh 文件中存放执行命令
#                                 用 sh xx.sh 执行文件中的命令
#
#
#                         2 使用
#                             FROM centos   # 引入一个centos镜像
#                             LABEL maintainer='xx'  # 作者信息
#                             ADD CentOS.Base.repo /etc/yum.repos.d/ # 添加本地的两个yum文件， 到容器的/etc/yum.repos.d/底下
#                             add epel.repo /etc/yum.repos.d/
#                             RUN yum clean all  # 清空yum缓存
#                             RUN yum install python-pip -y # 安装pip工具
#                             RUN pip install flask # 安装flask代码，到容器的/app/目录
#                             COPY myflask.py /app/ 拷贝本地的flask代码，到容器的/app/目录下
#                             WORKDIR /app  # 切换工作目录， 到/APP底下
#                             EXPOSE 8080 # 暴露8080端口 然后运行镜像的时候，加上-p参数，指定端口映射
#                             CMD ["python", 'myflask.py'] # 执行命令运行flask
#
#                             2 相关配置
#
#                                 FROM scratch #制作base image 基础镜像，尽量使用官方的image作为base image
#                                 FROM centos #使用base image
#                                 FROM ubuntu:14.04 #带有tag的base image
#
#                                 LABEL version=“1.0” # 代码注释， 镜像描述
#                                 LABEL maintainer=“yc_uuu@163.com" # 作者信息
#
#                                 #对于复杂的RUN命令，避免无用的分层，多条命令用反斜线换行，合成一条命令！
#                                 RUN yum update && yum install -y vim \
#                                     Python-dev #反斜线换行
#                                 RUN /bin/bash -c "source $HOME/.bashrc;echo $HOME”
#
#                                 WORKDIR /root #相当于linux的cd命令，改变目录，尽量使用绝对路径！！！不要用RUN cd
#                                 WORKDIR /test #如果没有就自动创建
#                                 WORKDIR demo #再进入demo文件夹
#                                 RUN pwd     #打印结果应该是/test/demo
#
#                                 ADD and COPY # Add 添加宿主机的文件到容器中，
#                                              # 还有一个解压缩功能，添加目录是以dockerfile文件所在目录为相对路径
#                                 ADD hello /  #把本地文件添加到镜像中，吧本地的hello可执行文件拷贝到镜像的/目录
#                                 ADD test.tar.gz /  #添加到根目录并解压
#
#                                 WORKDIR /root
#                                 ADD hello test/  #进入/root/ 添加hello可执行命令到test目录下，也就是/root/test/hello 一个绝对路径
#                                 COPY hello test/  #等同于上述ADD效果
#
#                                 ADD与COPY
#
#                                     -ADD除了COPY功能还有解压功能
#                                 添加远程文件/目录使用curl或wget
#
#                                 ENV #环境变量，尽可能使用ENV增加可维护性
#                                 ENV MYSQL_VERSION 5.6 #定义一个mysql常量
#                                 RUN yum install -y mysql-server=“${MYSQL_VERSION}”
#
#                                 ------这里需要稍微理解一下了-------中级知识---先不讲
#
#                                 VOLUME and EXPOSE
#                                 存储和网络
#
#                                 RUN and CMD and ENTRYPOINT
#                                 RUN：执行命令并创建新的Image Layer
#                                 CMD：设置容器启动后默认执行的命令和参数
#                                 ENTRYPOINT：设置容器启动时运行的命令
#
#                                 Shell格式和Exec格式
#                                 RUN yum install -y vim
#                                 CMD echo ”hello docker”
#                                 ENTRYPOINT echo “hello docker”
#
#                                 Exec格式
#                                 RUN [“apt-get”,”install”,”-y”,”vim”]
#                                 CMD [“/bin/echo”,”hello docker”]
#                                 ENTRYPOINT [“/bin/echo”,”hello docker”]
#
#
#                                 通过shell格式去运行命令，会读取$name指令，而exec格式是仅仅的执行一个命令，而不是shell指令
#                                 cat Dockerfile
#                                     FROM centos
#                                     ENV name Docker
#                                     ENTRYPOINT [“/bin/echo”,”hello $name”]#这个仅仅是执行echo命令，读取不了shell变量
#                                     ENTRYPOINT  [“/bin/bash”,”-c”,”echo hello $name"]
#
#                                 CMD
#                                 容器启动时默认执行的命令
#                                 如果docker run指定了其他命令(docker run -it [image] /bin/bash )，CMD命令被忽略
#                                 如果定义多个CMD，只有最后一个执行
#
#                                 ENTRYPOINT
#                                 让容器以应用程序或服务形式运行
#                                 不会被忽略，一定会执行
#                                 最佳实践：写一个shell脚本作为entrypoint
#                                 COPY docker-entrypoint.sh /usr/local/bin
#                                 ENTRYPOINT [“docker-entrypoint.sh]
#                                 EXPOSE 27017
#                                 CMD [“mongod”]
#
#                                 [root@master home]# more Dockerfile
#                                 FROm centos
#                                 ENV name Docker
#                                 #CMD ["/bin/bash","-c","echo hello $name"]
#                                 ENTRYPOINT ["/bin/bash","-c","echo hello $name”]
#
#                             3 构建docker镜像文件
#
#                                 docker build -t dockerhub账户名/镜像名 .
#
#                                     参数
#                                         -t tag参数，给镜像加上标记名
#
#                             4 查看镜像是否构建完成
#
#                                 docker images
#
#                             5 启动容器。映射一个端口供外部访问
#
#                                 docker run -d -p 8080:8080 账户名/镜像名
#                             6 检查运行的容器
#
#                                 docker container ls
#
#
#                     12 dockerhub，发布自己的docker镜像
#
#                         1 下载他人镜像
#                             docker pull xxxxx
#                         2 上传自己的docker镜像
#
#                             1 登录docker
#
#                                 docker login
#                             2 更改docker镜像名字
#
#                                 docker tag 现有镜像名 账户名/镜像名
#                             2 上传镜像
#
#                                 docker push xxx
#
#                     13 构建私有的docker仓库
#
#                         1 下载docker官方提供的私有仓库镜像
#                             docker pull registry
#
#                         2 实现共享文件夹启动私有仓库
#
#                             docker run -p 8000:8080 -v /opt/s14:/opt/data -d 镜像id
#
#                             事项容器内的/opt/data/文件夹，其实是访问宿主机的/opt/s14文件夹
#
#                         4 查看暴露端口是否连通
#
#                             telnet ip地址 端口
#
#                         5 修改本地镜像tag标签，标注要往哪传
#
#                             docker tag 镜像名 要传的ip地址:端口/自定义镜像名
#
#                         6 修改docker配置，允许非安全的传输
#
#                              1 /ect/docker/daemon.json 文件
#                                 写入 "insecure-registries":["仓库地址ip:端口"]
#
#                              2 /;on/systemd/system/docker.service
#                                 写入
#
#                                     [Service]
#                                     EnvironmentFile=/etc/docker/daemon.json
#
#                         7 重启docker,启动docker服务
#
#                             systemctl daemon-reload
#                             systemctl restart docker
#
#                         8 启动容器
#
#                             docker start 镜像名
#
#                         9 推送进行
#
#                             docker push ip地址:端口/文件名
#
#                 13 saltstack高效运维
#
#                     1 概念
#
#                         对大量的主机进行批量操作命令，快速远程执行命令
#
#                         运行方式
#
#                             local本地运行，交付管理
#                             Master/Minion（常用方式）
#                             Sall SSH 不需要客户端
#
#                         salt的命令直接输入，叫执行模块
#                         saltstack提供了自己的脚本语言 xxx.sls, 状态模块
#                     2 安装
#
#                         1 依赖包
#
#                             python
#                             zeromq
#                             pyzmp
#                             pycrypto
#                             msgpack-python
#                             yaml
#                             jinja2
#
#                         1 条件
#
#                             1 主1台 从多台
#                             2 主安装salt-master
#                                 yum install salt-master -y
#                             3 从安装salt-minion
#                                 yum install salt-minion -y
#
#                     3 配置
#
#                         1 /etc/salt/master
#
#                             interface: 0.0.0.0  #绑定到本地的0.0.0.0地址
#                             publish_port: 4505　　#管理端口，命令发送
#                             user: root　　　　　　#运行salt进程的用户
#                             worker_threads: 5　　#salt运行线程数，线程越多处理速度越快，不要超过cpu个数
#                             ret_port: 4506　　#执行结果返回端口
#                             pidfile: /var/run/salt-master.pid #pid文件位置
#                             log_file: /var/log/salt/master　　#日志文件地址
#
#                             # 自动接收minion的key
#                             auto_accept: True
#
#                         2 /etc/salt/minion
#                             master: ....
#                             master_port: 4506
#                             user: root
#                             id: slave
#                             acceptance_wait_time: 10
#                             log_file: /var/log/salt/minion
#
#                     4 相关命令
#
#                         查看秘钥通信key
#                             master端：salt-key -f 指明节点id  # 看看节点新型
#                             minion端：salt-call --local key.finger  # 查看节点的秘钥信息
#                         salt-key -L # 查看所有主机秘钥信息
#                         salt-key -a minion-id 指明接受一个minion
#                         salt-key -A # 接受所有minion的秘钥
#                         salt "*" test.ping # 匹配所有的已接受的主机，发送ping命令，会返回结果True 或 false
#                         salt "*" cmd.run # 对所有主机执行命令
#
#                         salt --summary '*' cmd.run '命令'
#                             参数
#                                 --summary 返回salt命令的执行成功状态
#                                 "*" 目标匹配字符串
#                                 cmd.run 模块函数，对所有匹配到的机器，执行后面的参数
#
#                         salt --out=json '*' cmd.run_all '命令'
#
#                             参数
#                                 --out=json # 返回执行结果为json格式
#
#
#
#                         pkg命令
#                         server命令
#
#                         命令执行结果，返回yaml语法格式
#
#                             salt --out=yaml "*" service.status nginx
#
#                     5 YAML语法
#
#                     6 采集静态数据Grains
#
#                         salt "*" grains.items # 采集所有minion机器的硬件信息
#                         salt "*" grains.item osfullname #  通过key返回单独的value
#                         salt "*" grains.item ipv4 os # 支持多key方式
#
#                     7 采集动态数据Pillar
#
1
# ===============================================