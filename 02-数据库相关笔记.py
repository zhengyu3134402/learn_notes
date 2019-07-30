
# -i https://pypi.douban.com/simple
# 此文档包含
    # 1 mysql-->mysqlmysql
    # 2 pymysql-->pymysql模块
    # 3 sqlalchemy-->sqlalchemy框架
    # 4 django的orm-->django的orm框架
    # 5 mongodb-->mongodbmongodb
    # 6 redis--> redisredis数据库
    # 7 sqlit3-->sqlit3sqlit3
	# 8 mariadb-->mariadbmariadb

# ===========================================
# mariadbmariadb
#   https://blog.csdn.net/zdyah/article/details/82354346
# 	1 linux安装
# 		sudo apt install mariadb-server
# 	2 初始化
# 		sudo mysql_secure_installation
# 		初始密码为空 ，按空格就行
# 		会提示设置密码
# 		会提示是否删除匿名用户 yes
# 		会提示不允许root远程登录 no
# 		是否删除测试数据库 yes
# 		是否立即刷新表  yes
# 	3 进入数据库
# 		sudo mysql -u root -p
# ===========================================

# ===========================================
# mysqlmysql
1
# 数据类型

    # 1 bit[(M)]
        # 二进制位（101001），m表示二进制位的长度（1 - 64），默认m＝1）

    # 2 tinyint[(m)][unsigned][zerofill]
        # 小整数，数据类型用于保存一些范围的整数数值范围：
        # 有符号：（创建字段的时候 singned）-128 ～ 127.
        # 无符号：（创建字段的时候 unsigned） ～ 255
        # 特别的： MySQL中无布尔值，使用tinyint(1)构造。）

    # 3 int[(m)][unsigned][zerofill]
        # 整数，数据类型用于保存一些范围的整数数值范围：
        # 有符号：-2147483648 ～ 2147483647
        # 无符号：～ 4294967295
        # 特别的：整数类型中的m仅用于显示，对存储范围无限制。例如： int(5), 当插入数据2时，select
        # 时数据显示为： 00002）


    # 4 bigint[(m)][unsigned][zerofill]
        # 大整数，数据类型用于保存一些范围的整数数值范围：
        # 有符号：-9223372036854775808 ～ 9223372036854775807
        # 无符号：～  18446744073709551615）

    # 5 decimal[(m[, d])][unsigned][zerofill]
        # 准确的小数值，m是数字总个数（负号不算），d是小数点后个数。 m最大值为65，d最大值为30。
        # 特别的：对于精确数值计算时需要用此类型
        # decaimal能够存储精确值的原因在于其内部按照字符串存储。

    # 6 FLOAT[(M, D)][UNSIGNED][ZEROFILL]
        # 单精度浮点数（非准确小数值），m是数字总个数，d是小数点后个数。
        # 无符号： -3.402823466E+38 to - 1.175494351E-38,
            # 1.175494351E-38 to 3.402823466E+38
        # 有符号：1.175494351E-38 to 3.402823466E+38
        # ** ** 数值越大，越不准确 ** ** ）

    # 7 DOUBLE[(M, D)][UNSIGNED][ZEROFILL]
        # 双精度浮点数（非准确小数值），m是数字总个数，d是小数点后个数。
        # 无符号：# -1.7976931348623157E+308 to - 2.2250738585072014E-308
        # 2.2250738585072014E-308 to 1.7976931348623157E+308
        # 有符号：2.2250738585072014E-308 to 1.7976931348623157E+308
        # ** ** 数值越大，越不准确 ** ** ）

    # 8 char(m)
        # char数据类型用于表示固定长度的字符串，可以包含最多达255个字符。其中m代表字符串的长度。
        # PS: 即使数据小于m长度，也会占用m长度）

    # 9 varchar(m)
        # varchars数据类型用于变长的字符串，可以包含最多达255个字符。
        # 其中m代表该数据类型所允许保存的字符串的最大长度，
        # 只要长度小于该最大值的字符串都可以被保存在该数据类型中。
        # 注：虽然varchar使用起来较为灵活，但是从整个系统的性能角度来说，char数据类型的处理速度更快，有时甚至可以超出varchar处理速度的50 %。因此，用户在设计数据库时应当综合考虑各方面的因素，以求达到最佳的平衡）

    # 10 text
        # text数据类型用于保存变长的大字符串，可以组多到65535(2 ** 16 − 1)个字符。）

    # 11 mediumtext
        # A TEXT column
        # with a maximum length of 16, 777, 215 (2 ** 24 − 1) characters.）

    # 12 longtext
        # A TEXT column with a maximum length of 4, 294, 967, 295 or 4GB (2 ** 32 − 1) characters.

    # 13 enum
        # 枚举类型 An ENUM column can have a maximum of 65, 535 distinct elements.(The
        # practical limit is less than 3000.)
        # 示例：
            # CREATE TABLE shirts(
                                # name
                                # VARCHAR(40),
                                # size
                                # ENUM('x-small', 'small', 'medium', 'large', 'x-large')
                                # ); INSERT INTO shirts(name, size) VALUES
                                # ('dress shirt', 'large'), ('t-shirt', 'medium'), ('polo shirt', 'small');)

    # 14 set
        # 集合类型
            # A SET column can have a maximum of 64 distinct members.
            #示例：
                # CREATE TABLE
                # myset(col SET('a', 'b', 'c', 'd')); INSERT INTO myset(col)
                # VALUES('a,d'), ('d,a'), ('a,d,a'), ('a,d,d'), ('d,a,d');)

    # 15 Date

        # YYYY - MM - DD（1000 - 01 - 01 / 9999 - 12 - 31）

    # 16 TIME
        # HH: MM:SS（'-838:59:59' / '838:59:59'）

    # 17 YEAR

        # YYYY（1901 / 2155）

    # 18 DATETIME
        # YYYY - MM - DD HH: MM:SS（1000 - 01 - 01
        # 00: 00:00 / 9999 - 12 - 31 23: 59:59

    # 19 TIMESTAMP
        # YYYYMMDDHHMMSS（1970 - 01 - 01 00: 00:00 / 2037# 年某时））


# mysql
    # 用于管理文件的一个软件服务端软件
    # socket服务端本地文件操作解析指令（sql语句）
    # 客户端软件socket客户端（）发送指令解析指令（sql语句）

# 是DBMS
    # 数据库管理系统


# 关系型数据库和非关系型数据库
    # 关系型数据库: sqlite, db2, oracle, access, sql, mysql
    # 非关系型数据库：MongoDB, redis

# 安装mysql

    # 1 sudo apt-get update
    # 2 sudo apt-get install mysql-server
    # 3 sudo apt install mysql-client
    # 4 sudo apt install libmysqlclient-dev

# windows安装说明
#     1 官网下载windows版5.7.18
#     2 一般会提示缺少依赖包（360会提示常用运行库合计下载）
#     3 需要手动下载Microsoft.NET Framework 4.0
#         去360软件管家下载即可
#     4 双击下载的mysql 下一步下一步其中注意选择只安装mysql服务器
#     5 下一步下一步
#     6 安装完成后点击开始中会出现mysql xxclient的终端
#         点击输入密码进入


# 配置mysql
    # sudo vi / etc / mysql / mysql.conf.d / mysqld.cnf
    # 注释掉  bind-address = 127.0.0.1：
    # 进入mysql文件设置：        
    # mysql -u root -p 
    # GRANT ALL PRIVILEGES ON *.* TO 'root' @ '%' IDENTIFIED BY '你的密码' WITH GRANT OPTION;（开启远程）
    # flush privileges; （刷新配置）
    # 重启mysql服务：
    # service mysql restart)

# 操作mysql命令
    # 1 连接数据库
            # mysql - uroot - p输入密码



# 操作数据库命令
    # 1 增
        # 1 创建数据库
            # create database 数据库名 default charset=utf8;

    # 2 删
        # 1 删除数据库
            # drop database 数据库名;
    # 3 改
        # 1 设置会话级步长
            # set session auto_increment_increment = 2;
    # 4 查
        # 1 显示数据库命令
            # show databases;
        # 2 进入某个数据库
            # user 数据库名;
        # 3 查看数据库的所有表
            # show tables;
        # 4 查看全局变量的步长
            # show variables like 'auto_inc%';
# 操作用户命令
    # 1 增
        # 1 创建用户
            # create user '用户名'@'%' identified by "密码"  # % 表示所有ip地址
        # 2 对用户进行授权
            # grant 权限 on 数据库名.表 to '用户名'@'ip'
                # grant all on *.* to 'lingling'@'%'
    # 2 删
        # 1 删除用户
            # drop user '用户名' @ 'IP地址';

    # 3 改
        # 1 修改用户名ip
            # rename user '用户名' @ 'IP地址' to '新用户名' @ 'IP地址';
        # 2 修改密码
            # set password for '用户名' @ 'IP地址' = Password('新密码')
        # 3 取消用户权限
            # revoke 权限 on 数据库.表 from '用户' @ 'IP地址'
    # 4 查
        # 1 查看当前用户
            # select user();
        # 2 查看用户权限
            # show grants for '用户' @ 'IP地址'


# 操作表命令
    # 1 增
        # 1 创建表(指定引擎为innodb,带自增,编码为utf8)
            # create table t5(id int auto_increment primary key, name char(10) null)
                # engine = innodb default charset = utf8;
        # 2 创建外键表（1对多）
            # create table 表名(
                # 字段,.., 外键字段 类型,
                # constrain 外键名 foreign key(外键字段名) references 关联表名(关联表字段id))
                # engine=innodb default charset = utf8

        # 3 创建唯一索引
            # create table 表名(id int auto_increment primary key,
                # 字段1,
                # 字段2,
                # unique 唯一索引名(唯一索引所加的字段名))engine = innodb default
                # charset = utf8
        # 4 创建联合唯一索引
            # create table 表名(id int auto_increment primary key,
                # 字段1,
                # 字段2,
                # unique 唯一索引名(字段1,字段2))engine = innodb default
                # charset = utf8
        # 5 创建外键表(1对1)
            # create table 表名(
            # id int auto_increment primary key,
            # 字段1,
            # 字段2,
            # constraint 外键名 foreign key(字段2) references 表名(id),
            # unique only_user(字段2)) engine = innodb
            # default charset = utf8;
        # 6 创建外键表（多对多）
            # 1 双向1对多
            # 2 第三张表
                # create table 表名(
                # id int auto_increment primary key,
                # 外键字段1 ,
                # 外键字段2,
                # constraint 外键名1 foreign key(外键字段1) references 关联表名1(id),
                # constraint 外键名2 foreign key(外键字段2) references 关联表名2(id),
                # unique only_user_computer(外键字段1, 外键字段2)) engine = innodb
                # default
                # charset = utf8;
        # 7 添加列
            # alter table 表名 add 列名 类型

        # 8 添加主键
            # alter table 表名 add primary key(列名);
        # 9 添加外键
            # alter table 外键所在表 add constraint 名 foreign key 外键所在表(外键字段) references 外键不在的表(主键字段);

    # 2 删
        # 1 删除表
            # drop table biao;
        # 2 删除列
            # alter table 表名 drop column 列名
        # 3 修改列
            # 1 修改列的类型
                # alter table 表名 modify column 列名 类型;

            # 2 修改列的列名和类型
                # alter table 表名 change 原列名 新列名 类型;
        # 4 删除主键
            # alter table 表名 drop primary key;

        # 5 删除外键
            # alter table 表名 drop foreign key 外键名称
	# 6 删除1行
	    # delete from 表名 where 条件
	# 7 删除多行
	    # delete form 表名 where xx in（值1，值2）
    # 3 改
        # 1 设定表的自增值（数据中不能有数据）
            # alter table 表名 auto_increment=值
    # 4 查
        # 1 查询表中的所有数据
            # select * form 表名;
        # 2 查看表结构
            # desc 表名
        # 3 查看表创建过程
            # show create table 表名 \G;

# 操作表中数据命令
    # 关键字的顺序
    #     where > group by > order

    # 1 增
        # 1 向表中插入数据
            # insert into 表名(列名1, 列名2) values(值1, 值2)）
        # 2 向表中插入多条数据
            # insert into 表名(列名1, 列名2) values(值1, 值2),(值3，值4)....;）
        # 3 将一个表中的部分数据插入到另一个表中
            # insert into 表名1(字段1, 字段2) select 字段a,字段b from 表名2;

    # 2 删
        # 1 清空表内容（不清空自增索引 慢 有记录）
            # delete from 表名;
        # 2 清空表内容（清空自增自增索引 快 没有记录）
            # truncate table 表明;
        # 3 添加删除表中内容
            # delete from 表名 where 条件;

    # 3 改
        # 1 修改表中数据
            # update 表名 set xxx (慎用, 全部修改)
            # update 表名 set xxx where 条件
    # 4 查
        # 1 查询部分字段数据内容
            # select 字段名1,字段名2 from 表名;
        # 2 更改查询结果字段表头
            # select 字段 as 名字 from 表名;

        # 3 额外增加一列数据且数据相等
            # select name,1 from biao1;

        # 4 条件where..in和where..not in查询
            # select * from 表名 where in (值1, 值2,...)

        # 5 条件 where..between.. and..查询
            # select * from 表名 where 字段 between 值1 and 值2

        # 6 select嵌套查询
            # select * from 表名1 where 字段 in (select 字段1 from 表名2)

        # 7 通配符查询where..like %匹配多个字符 _匹配单个字符

            # select * from 表名 where 字段 like 'l%';

        # 9 限制条件查询..limit
            # select * from 表名 limit 起始值,结束值;
            # select * from 表名 limit 显示数据个数值

        # 10 条件限制查询 .limit..offset
            # select * from 表名 limit 查询数据个数 offset 从第几行开始

        # 11 排序查询从大到小 order by ..desc （也可排序两个字段）
            # select * from 表名 order by 字段 desc;

        # 12 排序查询从小到大 order bt ..asc
            # select * from 表名 order by 字段 asc;

        # 13 分组查询
            # select * from 表名 group by 字段;

        # 14 查询有多少条数据
            # select count(id) from 表名;

        # 15 集合函数 min max sum avg count

            # 1 如果对聚合函数结果进行二次赛选 必须使用having代替where

        # 16 连表查询

            # 1 select 表1.字段1, 表2.字段2 from 表1, 表2 where 表1.id=表2.字段3; # 和2结果相同
            # 2 select * from 表1 inner join 表2 on 表1.id = 表2.字段; # 会显示两表共有的数据, 无对应关系则不显示
            # 3 select * from student left  join s_t on student.id = s_t.student_id; 会显示所有student中数据
            # 4 select * from student right  join s_t on student.id = s_t.student_id; 会显示s_t表中的所有数据

        # 17 处理重合
            # select 字段 from 表1 union select 字段 from 表2 #自动处理重和
            # select  字段 form 表1 union all select 字段 from 表2 # 不处理重合

        # 18 临时表
            # (select * from 表) as 名

        # 19 查看当前配置信息：
            # show variables like '%query%'

        # 20 查看最后一条数据

            # select * from 表名 order by id DESC limit 1;

        # 21 分页查询命令

            # select * from yingyong1_gupiao limit 0, 500;  # 从第1条到第500条数据

# 视图(开发中不常用)

    # 1 概念
        # 给某个查询语句设置别名, 如后方便使用, 创作别名叫创作试图
        # 视图表是从物理表动态创建的 视图表不能插入数据

    # 2 使用
        # 1 创建视图
            # create view 试图名 as sql语句;  # 会在tables表中显示

        # 2 使用视图
            # select * from 视图名

        # 3 修改视图
            # alter view 视图名 as sql语句

        # 4 删除视图
            # drop view 视图名称


# 触发器(不推荐使用)
    # 1 概念
        # 当对某张表做增删改时候, 可以使用触发器自定义关联操作
        # 相当于在执行某个sql语句前或后执行的动作

    # 2 创建触发器

        # 插入前 delimiter //
        # create trigger 触发器名 before insert on 表 for each row begin
            # insert into 表1(字段) values(new) end delimiter;

            # values中的NEW 表是新插入数据的一整行 NEW.字段名 取其他值
            # values(OLD) OLD表示删除的数据

            # 注意
            # 修改终止符;执行sql到结尾;终止符一下的语句就不执行了
            # 所以创建触发器之前要修改终止符, 修改之后要记得还原终止符, 以防其他表出现错误
            # delimiter // 将终止符改成 //delimiter;


# 内置函数

    # 1 使用地方
        # select 函数 from 表;

    # 2 函数

        # 1 length(x)
            # 返回字符串长度


        # 2 CONCAT(str1, str2, ...)
            # 字符串拼接


        # 3 CONV(N, from_base, to_base)
            # 进制转换

        # 4 FORMAT(X, D)
            # 将数字X 的格式写为'#,###,###.##', 以四舍五入的方式保留小数点后D位， 并将结果以字符串的形式返回。若
            # D为# 0, 则返回结果不带有小数点，或不含小数部分。

        # 5 INSERT(str, pos, len, newstr)
            # 在str的指定位置插入字符串 pos：要替换位置其实位置 len：替换的长度newstr：新字符串
            # 如果pos超过原字符串长度，则返回原字符串 如果len超过原字符串长度，则由新字符串完全替换

        # 6 LEFT(str, len)
            # 返回字符串str从开始的len位置的子序列字符。

        # 7 LOWER(str)
            # 变小写

        # 8 UPPER(str)
            # 变大写

        # 9 LTRIM(str)、RTRIM(str)
            # 返回字符串str ，其引导空格字符被删除。
        # ......

    # 3 自定义函数(有返回值)

        # 定义mysql中的终止符
            # delimiter 终止符


        # 1 创建
            # delimiter & # 定义终止符
            # create function hello()
            #     -> returns varchar(255)
            #     -> begin
            #     -> return 'hello11111111111111';
            #     -> end & 结束定义函数

        # 2 调用
            # delimiter ;  # 将终止符文复原
            # select hello()

# 存储过程
    # https://www.runoob.com/w3cnote/mysql-stored-procedure.html
    # 1 概念
        # 与视图类似，功能比视图多，视图只能查询，存储过程增删改查都能干
    # 2 存储过程的创建根据需要会有输入，输出，输入输出参数
        # in
            # in参数的值必须在调用存储过程时指定
        # out
            # 改值可在存储过程内部被改变，并可返回
        # inout
            # 调用时指定，并且可被改变和返回

    # 3 存储过程的创建in ou inout

        # delimiter &&
        # create procedure hello(in a int)
        #     -> begin
        #     -> select a;   # 显示a
        #     -> set a=2;    # 设置a
        #     -> select a;   # 显示a
        #     -> end &&

    # 4 存储过程的调用

        # delimiter ;
        # set @a=1;      # 设置a
        # call hello(@a); # 调用存储过程

    # 5 查看存储过程
        # show procedure status;

    # 6 删除存储过程
        # drop procedure 存储过程名;

    # 7 存储过程的事物

        # 1 概念
            # 事物处理可以用来维护数据的完整性, 保证成批的sql语句要么全部执行, 要么全部不执行
            # 事物管理用insert update delete语句
            #
            # commit 对书库进行的所有修改成为永久性的
            # rollback 撤销正在进行的所有未提交的修改
            # savepoint identifier 事物中创建一个保存点，可以有多个保存点
            # release savepoint identifier 删除一个事物保存点
            # rollback to identifier 把事物回滚到标记点
            # set transaction用来设置事物的隔离级别
                # innodb存储提供事物的隔离级别
                    # read uncommitied,read commmitied,repeatable read, derializable

            # 事物处理主要两种方法
                # begin 开始一个事物
                # rollback事物回滚
                # commit事物确认
            # 用set 来改变 mysql的自动提交模式
                # set autocommit=0禁止自动提交
                # set autocommit=1开启自动提交

        # 2 使用事物

            # 1 提交操作
                # 1 开始事物
                    # begin;
                # 2 向表中插入数据
                    # insert into test value(5);
                    # insert into test value(6);
                # 3 提交事物
                    # commit;
            # 2 回滚操作
                # 1 开始事物
                    # begin;
                # 2 插入数据
                    # insert into test value(7);
                # 3 回滚数据
                    # rollback;




# 索引

    # 1 概念
        # 作用:
            # 约束，加速查找
        # 分类:

            # 普通索引: 加速查找
            # 主键索引: 加速查找 + 不能为空 + 不能重复
            # 唯一索引: 加速查找 + 不能重复
            # 联合索引(多列)
            # 联合主键索引
            # 联合唯一索引
            # 联合普通索引

        # 无索引查找
            # 从前到后一次查找
        # 有索引查找
            # 创建额外文件(某种格式存储)

        # 索引种类:
            # hash索引:
                # 索引表(找单值速度快, 取范围速度慢)
        # btree索引(应用多):
            # 二叉树
    # 2 创建索引
        # 1 创建普通索引
            # create index 名字 on 表名(列名);

            # 1 删除索引
                # drop index 名字 on 表名

        # 2 创建唯一索引

            # create unique index 名字 on 表名(列名)

            # 1 删除唯一索引
                # drop index 名字 on 表名

        # 3 创建联合索引(联合唯一索引)
            # create unique index 名 on 表名(字段1,字段2);

            # 1 删除联合索引
                # drop index 名 on 表名;

        # 4 创建局部索引
            # create index 名 on 表(字段(16))    # 16？

    # 2 覆盖索引:
        # 在索引文件中直接获取数据的行为是覆盖索引


    # 3 索引合并:

        # 把多个单列索引合并使用
        # select * from user where name = "hah" and id = 3;

    # 索引的优化


        # 1 最左前缀匹配
            # create index xxxx on user(name, age)

            # 会利用索引文件查询
                # select * from user where name = "alex"
                # select * from user where name = "asl" and age = 12

            # 不会利用索引文件查询
                # select * from user where age = 12 and name = "asl"

        # 2 组合索引效率 > 索引合并

        # 3 频繁查找的列创建索引
    # 4 若数据量庞大避免使用like, 若想使用用第三方插件

    # 5 使用函数
        # select * from tb1 where reverse(name) = 'wupeiqi';
        # select * from tb1 where nid = 1 or email = 'seven@live.com';

    # 6 类型不一致
        # 如果列是字符串类型，传入条件是必须用引号引起来，不然...
        # select * from tb1 where name = 999;
    # 7 !=
        # select * from tb1 where name != 'alex'
        # 如果是主键，则还是会走索引
        # 特别的：如果是主键或索引是整数类型，则还是会走索引

    # 8 当根据索引排序时候，选择的映射如果不是索引，则不走索引
        # 特别的：如果对主键排序，则还是走索引：

    # 9 组合索引最左前缀
        # 如果组合索引为：(name, email)
            # name and email - - 使用索引
            # name - - 使用索引
            # email - - 不使用索引
    # 10 避免使用
        # 避免使用 select *
        # 使用 count(1) count(列)代替count(*)

    # 11 创建表时尽量时 char 代替 varchar

    # 12 其他
        # 表的字段顺序固定长度的字段优先
        # 组合索引代替多个单列索引（经常使用多个条件查询时）
        # 尽量使用短索引
        # 使用连接（JOIN）来代替子查询(Sub - Queries)
        # 连表时注意条件类型需一致
        # 索引散列值（重复少）不适合建索引，例：性别不适合
    # 13 参考时间
        # type
        # 查询时的访问方式，性能：all < index < range < index_merge < ref_or_null < ref < eq_ref < system / const

        # 1 ALL
            # 全表扫描，对于数据表从头到尾找一遍
            # select * from tb1 where

            # 使用limit

        # 2 INDEX
            # 全索引扫描，对索引从头到尾找一遍

        # 3 RANGE
            # 对索引列进行范围查找

        # 4 INDEX_MERGE
            # 合并索引，使用多个单列索引搜索

        # 5 REF
            # 根据索引查找一个或多个值

        # 6 EQ_REF
            # 连接时使用primary key 或 unique类型

        # 7 CONST
            # 常量表最多有一个匹配行, 因为仅有一行, 在这行的列值可被优化器剩余部分认为是常数,
            # const表很快, 因为它们只读取一次。

        # 8 SYSTEM
            # 系统表仅有一行( = 系统表)。这是const联接类型的一个特例

        # 9 DBA工作

            # 慢日志
            # 执行时间 > num
            # 未命中索引
            # 日志文件路径
            # 配置
            # slow_query_log = OFF
            # 是否开启慢日志记录
            # long_query_time = 2
            # 时间限制，超过此时间，则记录
            # slow_query_log_file = / usr / slow.log
            # 日志文件
            # log_queries_not_using_indexes = OFF
            # 为使用索引的搜索是否记录


# 开启日志
    # set global slow_query_log=on
    # 1 基于配置文件

        # 启动mysql
        # nmysqld - -defaults - file = 配置文件路径

    # 2 配置文件内容如:
        # slow_query_log = ON
        # slow_query_log_file = 文件完整路径

    # 修改配置文件之后, 需要重启服务



# 分页
    # 会随数值的增大, 查询数度变慢, 原理是取第3页的10条, 会扫描3页取十条

    # 解决
        # 记录查询数据
        # 比如查询数据10条记录数据当前页的最大id和最小id用于上翻页和下翻页
1
# ===========================================


# ===========================================
# pymysql模块（使用python sql语句脚本操作数据库）
1
# 1 通过python对数据库进行操作


# 2 安装
    # pip3 install pymysql

# 3 使用

    # import pymysql
    # conn = pymysql.connect(host="localhost",
    #                        user="root",
    #                        password="a3134402",
    #                        database="d1")
    # cursor = conn.cursor()
    # cursor.close()  # 关闭游标
    # conn.close()  # 关闭链接

    # 1 增
        # 1 向数据库添加一条数据 (此写法为了防止sql注入)
        # cursor.execute("insert into student(name, age) values(%s,%s)",["lingling2",33])
        # conn.commit()
    # 2 向数据库中添加多条数据
        # cursor.executemany("insert into student(name, age) values(%s,%s)",[("lingling55",33),("linglng66", 34)])
        # conn.commit()
    # 2 删
    # 3 改
    # 4 查
        # 1 查看返回操作的一条信息元祖
            # cursor.fetchone()
        # 2 查看返回操作结果的所有信息元祖
            # cursor.fetchall()
        # 3 返回操作后插入数据的结果
            # a = cursor.execute("select * from student") # 返回执行操作后的结果个数
            # print(a)
        # 4 返回最后插入数据的id
            # cursor.lastrowid
        # 5 获取数据类型的改变
            # 1 获取字典类型
                # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 6 pymysql调用存储过程
            # cursor.callproc("存储过程名")
1
# ===========================================


1
# ===========================================
# SQLAlchemy框架
1
    # 1 概念
        # SQLAlchemy是Python编程语言下的一款ORM框架，该框架建立在数据库API之上，
        # 使用关系对象映射进行数据库操作，简言之便是：将对象转换成SQL，然后使用数据API执行SQL并获取执行结果。

        # 作用:
            # 1 提供简单的规制
            # 2 自动转换成SQL语句

        # 限制

            # SQLAlchemy本身无法操作数据库，其必须以来pymsql等第三方插件，
            # Dialect用于和数据API进行交流，根据配置文件的不同调用不同的数据库API，从而实现对数据库的操作，如

            # MySQL - Python
                # mysql + mysqldb: // < user >: < password >

                # pymysql mysql + pymysql: // < username >: < password >

                # MySQL - Connector mysql + mysqlconnector: // < user >: < password >

        #内部处理

            # 使用Engine / ConnectionPooling / Dialect
            # 进行数据库操作，Engine使用ConnectionPooling连接数据库，然后再通过Dialect执行SQL语句。
    # 2 安装
        # pip3 install SQLAlchemy
        # pip3 install mysql-connector-python # 使用此模块连接数据库 pymysql模块有问题


# 3 连接数据库
        # from sqlalchemy import create_engine
        # engine = create_engine("mysql+mysqlconnector://root:a3134402@localhost:3306/d1")
        # print(engine)

    # 4 操作数据库(使用sql语句)
        # 1 增
            # 1 插入数据
                # engine.execute("insert into student(name, age) values('ling123', 213)")
        # 2 删
        # 3 改
        # 4 查
            # 1 获取1条数据
                # a = engine.execute("select * from student")
                # print(a.fetchone())
            # 2 获取n条数据
                # a = engine.execute("select * from student")
                # print(a.fetchmany(3))
            # 3 获取所有数据
                # a = engine.execute("select * from student")
                # print(a.fetchall())


    # 5 操作数据库(使用orm)
        # 1 增
            # 1 创建表
                # from sqlalchemy import create_engine
                # from sqlalchemy.ext.declarative import declarative_base
                # from sqlalchemy import Column, String, Integer
                # engine = create_engine("mysql+pymysql://root:a3134402@localhost:3306/d1")  # 创建连接
                #
                # Base = declarative_base()   # 创建关系映射模型基类
                # class Student(Base):    # 创建模型类继承关系映射模型基类
                #     __tablename__ = 'student'
                #     id = Column(Integer, primary_key=True)
                #     name = Column(String(20))
                #     age = Column(Integer)
                # Base.metadata.create_all(engine) # 根据模型创建表

            # 2 创建表(为字段创建索引)
                # .....
                # from sqlalchemy import Index
                # class Student(Base):  # 创建模型
                    # __tablename__ = 'student'
                    # id = Column(Integer, primary_key=True)
                    # name = Column(String(20))
                    # age = Column(Integer)
                    # __table_args__ = (Index("name"),)    # 索引
                # ......

            # 3 创建表(为字段创建唯一索引)
                # from sqlalchemy UniqueConstraint
                # ...
                # __table_args__ = (UniqueConstraint("name"),)
                # ...

            # 4 创建表(为字段创建联合唯一索引)
                # ...
                # __table_args__ = (UniqueConstraint("name","age", name="haha"), Index("haha"))
                # ...
            # 5 创建表(一对多)
                # from sqlalchemy import create_engine
                # from sqlalchemy.ext.declarative import declarative_base
                # from sqlalchemy import Column, String, Integer, Index, UniqueConstraint, ForeignKey
                # engine = create_engine("mysql+pymysql://root:a3134402@localhost:3306/d1")  # 创建连接
                #
                # Base = declarative_base()
                # class Person(Base):    # 创建模型
                #     __tablename__ = 'person'
                #     id = Column(Integer, primary_key=True)
                #     name = Column(String(20))
                #     age = Column(Integer)
                #
                # class Favor(Base):
                #     __tablename__ = 'favor'
                #     id = Column(Integer, primary_key=True)
                #     favor_name = Column(String(20))
                #     person_id = Column(Integer, ForeignKey(Person.id))
                #     favor = relationship("Person", backref='favor')  # 与生成表结构无关，仅用于查询方便
                # Base.metadata.create_all(engine) # 创建表
            # 6 创建表(多对多)
                # from sqlalchemy import create_engine
                # from sqlalchemy.ext.declarative import declarative_base
                # from sqlalchemy import Column, String, Integer, Index, UniqueConstraint, ForeignKey
                # engine = create_engine("mysql+pymysql://root:a3134402@localhost:3306/d1")  # 创建连接
                # Base = declarative_base()
                # class Group(Base):
                #     __tablename__ = 'group'
                #     id = Column(Integer, primary_key=True)
                #     name = Column(String(64), unique=True, nullable=False)
                #     port = Column(Integer, default=22)
                #
                #
                # class Server(Base):
                #     __tablename__ = 'server'
                #
                #     id = Column(Integer, primary_key=True, autoincrement=True)
                #     hostname = Column(String(64), unique=True, nullable=False)
                #
                #
                # class ServerToGroup(Base):
                #     __tablename__ = 'servertogroup'
                #     nid = Column(Integer, primary_key=True, autoincrement=True)
                #     server_id = Column(Integer, ForeignKey('server.id'))
                #     group_id = Column(Integer, ForeignKey('group.id'))
                # Base.metadata.create_all(engine) # 创建表
            # 7 添加一条数据
                # from sqlalchemy.orm import sessionmaker
                # maker = sessionmaker(bind=engine)  # 创建会话
                # session = maker()    # 实例化会话
                # a = Person(name='lingling', age=25)
                #
                # session.add(a)
                # session.commit()
                # session.close()  # 关闭会话
            # 8 添加多条数据
                # from sqlalchemy.orm import sessionmaker
                # maker = sessionmaker(bind=engine)
                # session = maker()
                # a = Person(name='lingling', age=25)
                # b = Person(name='yingying', age=23)
                # session.add_all([a,b])
                # session.commit()
                # session.close()
        # 2 删
            # 1 删除表
                # Base.metadata.drop_all(engine)
            # 2 删除数据
                # from sqlalchemy.orm import sessionmaker
                # maker = sessionmaker(bind=engine)
                # session = maker()
                #
                # a = session.query(Person).filter_by(id=2).delete()
                # session.commit()
                # session.close()
        # 3 改
            # 1 更新数据
                # from sqlalchemy.orm import sessionmaker
                # maker = sessionmaker(bind=engine)
                # session = maker()
                #
                # a = session.query(Person).filter_by(id=3).update({"name":"fhahhha"})
                # session.commit()
                # session.close()
        # 4 查（filter用于条件查询）
            # 1 获取所有数据
                # from sqlalchemy.orm import sessionmaker

                # maker = sessionmaker(bind=engine)
                # session = maker()

                # a = session.query(Person).all()
                # print(a)
                # session.close()

            # 2 查询一条数据
                # ...
                # a = session.query(Person).filter_by(id=3).first()
            # 3 排序（从小到大）
                # ret = session.query(Users).order_by(Users.name.desc()).all()
                # ret = session.query(Users).order_by(Users.name.desc(), Users.id.asc()).all()

            # 4 区间查找
                # session.query(Person).filter(Person.id.between(1,3)).all()
            # 5 in查找
                # session.query(Person).filter(Person.id.in_([1,3])).all()
            # 6 反向查找
                # session.query(Users).filter(~Users.id.in_([1, 3, 4])).all()
            # 7 and查找
                # session.query(Person).filter_by(name="lingling",age=25).all()
                # session.query(Users).filter(and_(Users.id > 3, Users.name == 'eric')).all()
            # 8 or查找
                # ret = session.query(Users).filter(or_(Users.id < 2, Users.name == 'eric')).all()
            # 9 通配符查找
                # session.query(Person).filter(Person.name.like('y%')).all()
            # 10 分组聚合

                # from sqlalchemy.sql import func
                #
                # ret = session.query(Users).group_by(Users.extra).all()
                # ret = session.query(
                #     func.max(Users.id),
                #     func.sum(Users.id),
                #     func.min(Users.id)).group_by(Users.name).all()
            # 11 连表查询

                # ret = session.query(Users, Favor).filter(Users.id == Favor.nid).all()
                # ret = session.query(Person).join(Favor).all()
                # ret = session.query(Person).join(Favor, isouter=True).all()

            # 12 组合
                # q1 = session.query(Users.name).filter(Users.id > 2)
                # q2 = session.query(Favor.caption).filter(Favor.nid < 2)
                # ret = q1.union(q2).all()
                #
                # q1 = session.query(Users.name).filter(Users.id > 2)
                # q2 = session.query(Favor.caption).filter(Favor.nid < 2)
                # ret = q1.union_all(q2).all()

        # 5 游标的移动
            # 注：在fetch数据时按照顺序进行，可以使用cursor.scroll(num,mode)来移动游标位置，如：
            # cursor.scroll(1,mode='relative')  # 相对当前位置移动
            # cursor.scroll(2,mode='absolute') # 相对绝对位置移动

1
# ===========================================







# =================================================
# mongodbmongodb
1
#     1 概念
#         非关系型数据库
#         结构
#
#                 {
#                     数据库1:{
#                         表名:[
#                             {"a":1},
#                             {"b":2},
#                         ]
#                     }
#                 }
#
#
#     2 安装
#
#         sudo apt-get install mongodb
#
#         根目录下创建只读目录 data/db
#
#         杀死mongodb进程
#
#         mongod 如果成功就成功了
#
#     3 查看是否安装成功
#
#         mongod --version
#
#     4 相关配置
#
#         1 修改数据存储路径（可选）
#
#             mongod --dbpath= 数据存储路径
#
#     5 连接数据库
#
#         mango
#
#     6 基本命令
#
#         1 show dbs
#
#             查看所有数据库
#
#         2 use 数据库名词
#
#             切换到指定的数据库（如果没有会创建）
#             执行命令show dbs 不会看到新建的数据库因为里面没有数据
#
#         3 db
#
#             查看当前操作数据库
#
#         4 db.表名.insertOne({"a":"b"})
#
#             向表中插入数据
#
#         5 show collections
#
#             显示当前数据库中的所有表
#
#         6 db.表名.find()
#
#             查询表中的所有数据
#
1

# =================================================



# =================================================
# redisredis数据库
1
#     redis与python交互文档  http://python.jobbole.com/87305/
#     学习视频网站
#         https://www.bilibili.com/video/av34392659/?p=11
#     1 概念
#         NoSQL:不是关系型数据库
#         不支持SQL语法
#         存储格式是kv格式
#         没有一种通用的操作语言
#         适用于关系不复杂的语言
#         基本不支持事务
#         c语言编写，支持网络，基于内存也可持久化的日执行，key value型数据库
#         持久化支持数据保存在磁盘中，重新启动可进行再加载使用
#     2 安装（windows版本）
#         https://github.com/MicrosoftArchive/redis/releases
#         下载 Redis-x64-3.2.100.msi
#         点击安装下一步下一步
#
#         系统环境安装regis
#             pip3 install redis
#     3 配置（默认即可）
#         redis.windows-service.conf文件
#         (可选)
#         安装目录（一般为c:\Program File\Redis）
#         用记事本打开redis.windows-service.conf文件
#         找到# requirepass foobared 下面 添加 requirepass 12345 添加密码
#
#         绑定ip
#             默认bind 127.0.0.1
#         绑定端口
#             默认port 6379
#         是否设置为守护进程
#             daemonize yes  windows默认 yes而且不支持no
#             daemonize no   linux默认no  推荐设置成yes
#         持久化文件存放的文件夹
#             默认dbfilename dump.rdb
#         持久化文件存储的路径
#             默认  dir ./
#         日志文件
#             （windows）默认 logfile "server_log.txt"
#             （linux）默认 logfile ""   需要填写
#         数据库 默认16个
#             databases 16
#         主从复制，类似于双击备份（主从配置的时候才使用）
#             默认没有配置
#
#         详细配置https://blog.csdn.net/ljphilp/article/details/52934933
#
#
#
#         （查看是否启动）
#            我的电脑右键属性---》管理---》服务和应用程序---查看redis是否启动
#     4 测试
#         进入一般为c:\Program File\Redis下
#             命令 redis-cli 连接服务器
#
#     5 命令
#         连接数据库
#             进入安装目录 redis-cli 连接服务器  （linux不用进入目录）
#             默认连接到0数据库
#         切换数据库
#             select n     默认有16个 从0~15
#         清空数据命令
#             flushall
#
#
#
#     6 string类型数据库操作
#         string类型
#             基础数据类型 key value
#         设置
#             设置键与值
#                 set key value  设置的键值如果不存在是添加，如果存在是修改
#             获取键对应的值
#                 get key
#             设置键与值待过期时间的
#
#                 setex key seconds value
#
#                 expire key seconds
#             设置多个键与值
#                 mset key1 value1 key2 value2...
#             对一个键追加值(是往对应键的之中添加（合并）)
#                 append key value
#         获取
#             根据键获取值
#                 get key
#             根据多个键获取多个值
#                 get key1 key2...
#         查找键 各种数据类型通用操作
#
#             支持正则查找
#                 keys 正则
#             查看所有键
#                 keys *
#             查看以a开头的键
#                 keys a*
#             查看键是否存在 存在返回1 不存在返回0
#                 exists key
#             查看键对应值得类型
#                 type key
#             查看键值得有效时间
#                 ttl key
#
#         删除
#
#             删除键对应的值,hash类型可用
#             del key1 key2...
#
#     8 hash哈希类型数据库操作命令（存储对象类型数据,值为字符串类型）
#
#         设置单个属性
#             hset key field value
#
#         设置多个属性
#             hmset key field1 value1 field2 value2...
#
#         获取指定键的所有属性
#             hkeys key
#         获取一个属性的值
#             hget key field
#         获取多个属性的值
#             hmget key field1 field2
#         获取所有属性的值
#             hvals key
#
#         删除属性，属性对应的值会被一起删除
#             hdel key field1 field2....
#
#         可能出现错方法
#         错误
#             MISCONF REDIS。。。。
#             强制关闭Redis快照导致不能持久化，解决方案
#                 运行命令 config set stop-writes-on-bgsave-error no
#                 解决问题
#
#     9 list列表类型操作命令（列表中元素类型为string）
#
#         从左侧向列表中插数据
#             lpush key value1 value2...
#         从右侧向列表中插入数据
#             rpush key value1 value2...
#         在指定元素的前或后插入新元素
#             linsert key before或after 现有元素 新元素
#
#         返回列表里指定范围内的元素(start, stop为元素的下标索引，索引可以为负)
#             lrange key start stop
#         查看列表所有元素
#             lrange key 0 -1
#
#         设置指定索引位置的元素值
#             lset key index value
#
#         删除指定的元素
#             count > 0 : 从头到尾删除指定值的相同的值 如2 就删除2次
#             count < 0 ：从尾往头删除指定值的相同的值
#             count = 0 : 删除列表中指定值的相同的值
#             lrem key count value
#
#     10 set集合类型数据操作命令（无序，元素为string类型，唯一性，不重复，没有修改操作）
#
#         向集合中添加元素
#             sadd key member1 member2...
#         获取集合中所有的元素
#             smembers key
#         删除集合当中指定元素
#             srem key member1 member2....
#
#     11 zset数据类型操作命令
#     （有序集合，元素为string类型，元素具有唯一性，不重复，
#     每个元素都会关联一个double类型的score，表示权重，通过权重
#      将元素从小到大排序）
#
#         向有序集合中添加元素
#             zadd key score1 member1 socre2 member2
#
#         返回有序集合指定范围内的元素(有索引与列表类似)
#             zrange key start stop
#
#         根据权重值score 返回范围元素 （类似列表索引范围取值）
#             zrangebyscore key  score1 socre2
#
#         获取元素的权重值
#             zscore key member
#
#         删除有序集合的指定元素
#             zrem key member1 member2 ....
#
#         删除根据权重范围删除指定元素
#             zremrangebyscore key score1 socre2
#
#     12 redig 与python的交互
#         文档  http://python.jobbole.com/87305/
#         python中使用redis
#
#             1 导入模块
#                         from redis import *
#             2 创建StrictRedis对象
#                         sr = StrictRedis(host='localhost', port=6379, db=0)
#                                     # 默认就是这三项 参数可以不写
#                                     # host 连接redis所在的ip
#                                     # port 连接redis所在的端口号
#                                     # db 连接redis数据库0
#                         与原命令不一样的命令
#                             清空数据库内容
#                                 sr.flushdb()
#
#                         sr对象的方法基本和redis命令一致
#                             string          keys            hash        list         set          zset
#                                 set             exists          hset        lpush       sadd        zadd
#                                 setex           type            hmset       rpush       smembers    zrange
#                                 mset            delete          hkeys       linsert     srem        zrangebyscore
#                                 append          expire          hget        lrange                  zscore
#                                 get             getrange        hmget       lset                    zrem
#                                 mget            ttl             hvals       lrem                    zremrangebyscore
#                                 key                             hdel
#
#     13 redis存储session
#         ？？？？
#     14 redis主从配置
#         ？？？？
#     15 redis主从概念
#         ？？？？
#     16 redis集群概念
#         ？？？？
#     17 redis集群配置
#         ？？？？
#     18 redis python和集群交互
#         ？？？？
#
#
#
#
#
#
1

# =================================================










# =================================================
# sqlit3sqlit3
1
    # 1 概念
    #
    #     sqlite3是Python3标准库不需要另外安装，只需要安装SQLAlchemy即可
    #
    #
    # 2 连接数据库
    #
    #     engine = create_engine('sqlite:///推荐绝对路径/xx.db')
    #
    # 3 创建连接使用到增删改查
    #
    #     from sqlalchemy import create_engine
    #     from sqlalchemy.ext.declarative import declarative_base
    #     from sqlalchemy.orm import sessionmaker
    #     from sqlalchemy import Column, String, Integer
    #
    #     import os
    #
    #     path = os.path.abspath(os.path.dirname(__name__))+'\\db\\test.db'
    #
    #
    #     # 建立连接
    #     engine = create_engine('sqlite:///%r'%(path))
    #
    #     # 创建映射类对象
    #     Base = declarative_base()
    #
    #     # 创建模型类
    #
    #     class User(Base):
    #
    #         __tablename__ = 'users'
    #         id = Column(Integer, primary_key=True)
    #
    #         name = Column(String(32))
    #
    #     # 创建表
    #     Base.metadata.create_all(engine)
    #
    #     # 建立会话
    #     Session = sessionmaker(bind=engine)
    #
    #     # 创建会话实例
    #     session = Session()
    #
    #     # 通过会话实例进行增删改查
    #
    #     # 创建模型类对象
    #     u1 = User(name="lingling")
    #
    #     # 将数据插入到表中
    #     session.add(u1)
    #
    #     # 一次性插入多个对象
    #     # session.add_all([u1,u2,u3...])
    #
    #     # 确认提交对象
    #     session.commit()
    #
    #     # 删除数据
    #     # session.delete(xx)
    #
    #     # 修改数据
    #     # user = session.query(User).filter_by(name='lingling').first()
    #     # user.name = "yingying"
    #     # session.commit()
    #
    #     # 查询数据
    #     # user = session.query(User).filter_by(name='lingling').first()
    #
    #     # 直接实行sql语句
    #
    #     # sql = "select * from users"
    #     # session.execute(sql)
1
# =================================================



# =================================================


# =================================================
# django的orm框架(使用模块pymysql)
1
# 1 概念

# 对象关系映射.ORM是通过使用描述对象和数据库之间映射的元数据，
# 将程序中的对象自动持久化到关系数据库中。
# ORM只是一种工具，工具确实能解决一些重复，简单的劳动

# ORM能做的事情和需要手动做的事情
# 1 操作数据表 创建/删除/修改表
# 2 操作数据行 数据的增删改查
# 3	不能创建数据库,自己动手创建数据库

# 使用django的ORM详细步骤:
# 1 自己手动创建数据库
# 2 在django项目中设置链接数据库相关配置(告诉django链接哪个数据库)
# 3 告诉django用什么链接数据库(用pymysql代替默认的mysqldb链接mysql数据库)
# 4 在app下面models.py文件中定义一个类,这个类必须继承models.Model
# 5 执行两个命令:
# python3 manage.py makemigrations
# python3 manage.py migrate

# 2 使用
# 使用模型
# class Person(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20)
#     age = models.IntegerField()

# class Book(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     price = models.IntegerField()
#     author = models.ForeignKey(Person)

# 1 增11111111111111111
# 1 增加一条数据
# Person.objects.create(id=1, name='lingling2',age=25)
# 2 删222222222222222222
# 1 删除一条数据
# Person.objects.filter(name="lingling").delete()

# 2删除数据库中的表

# 注释models.py的代码
# 执行命令
# python3 manage.py makemigrations
# python3 manage.py migrate
# 3 改3333333333333333333
# 1 修改一条数据
# Person.objects.filter(id=id).update(name=name, age=age)

# 2 修改数据库当中的表

# 即修改模型后
# 执行命令
# python3 manage.py makemigrations
# python3 migrate
# 4 查4444444444444444444444

# 1 双下划线查询

# 1 大于查询
# Person.objects.filter(age__gt=30)
# 2 小于查询
# Person.objects.filter(age__lt=40)
# 3 in查询
# Person.objects.filter(age__in=[22, 15, 43])
# 4 not in查询
# Person.objects.exclude(age__in=[22, 15, 43])
# 5 包含查询
# Person.objects.filter(name__contains="y")
# 6 忽律大小写查询
# Person.objects.filter(name__icontains="y")
# 7 范围查询
# Person.objects.filter(age__range=[40,50])
# 8 日起字段查询


# 2 获取所有数据
# Person.objects.all()

# 3 获取过滤数据
# Person.objects.filter(name='linglng')

# 4 获取数据的对象
# a = Person.objects.get(name="赵云")
# print(a.get().name)

# 5 通过外键所在表查找关联的数据
# b = Book.objects.filter(name="刚发的")
# b.author.字段

# 6 通过外键获取所有对象的字段信息(外键__字段)
# b = Book.objects.values_list("author__name")
# print(b)
# < QuerySet[('赵云',), ('曹超',), ('ZHENGYU',)] >

# 7 通过关联的数据表查找外键表(值)
# b = Person.objects.values_list("book__name")
# print(b)
# <QuerySet [('我的世界',), ('大草里',), ('刚发的',), ('我的哈哈',), ('我鸿飞',),
# (None,), (None,), (None,), (None,)]>

# 8 通过关联的表查找外键对应的对象
# b = Person.objects.first()
# c = b.book_set.all()
# print(c.values_list("name"))
# print(c)
# print(b)
# >>> <QuerySet[('发',)] >
# < QuerySet[ < Book: Book object >] >
# linglng
# 9 通过关联表创建外键对象
# person.book_set.create(name=name, price=price)

# 10 manytomany通过表所在外键添加多个对象
# person1  = Person.objects.get(id=7)
# person2  = Person.objects.get(id=8)
# person3 = Person.objects.get(id=9)
# persons = [person1, person2, person3]
# job = Job.objects.get(id=1)
# job.person_job.add(*persons)

# 11 manytomany通过表所在外键更新多个对象
# job = Job.objects.get(id=1)
# job.person_job.set([3,4])
# 12 manytomany通过表所在外键删除多个对象(对于ForeignKey对象，clear()和remove()方法仅在null=True时存在。)
# job = Job.objects.get(id=1)
# job.person_job.remove(3)
# 13 manytomany通过外键所在表删除所有对象(对于ForeignKey对象，clear()和remove()方法仅在null=True时存在。)
# job = Job.objects.get(id=1)
# job.person_job.clear()

# 14 聚合查找
# from django.db.models import Avg, Sum, Max, Min, Count
# a = Person.objects.all().aggregate(Count("id"))
# print(a)
# >>>> {'id__count': 7}

# 15 分组查找
# Person.objects.values("age","name").annotate(avg=Avg("age"))

# 16 分组连表查询
# Person.objects.annotate(avg=Avg("book__price")).values("name", "avg")
# Person.objects.annotate(count=Count("book__id")).filter(count__lt=1)

# 17 F查询(字段之间比较查询)
# from django.db.models import F
# a = Person.objects.filter(age__gt=F("id"))
# 18 Q查询(查询条件or and ~)
# from django.db.models import Q
# Person.objects.filter(Q(id=4)|Q(id=5))  # or如果都有都会返回
# Person.objects.filter(Q(id=4) & Q(name="zhengyu12")) # and
# Person.objects.filter(~Q(id=4)) # 反向查询
# 5 锁(select_for_update() 在事物内使用)
# 所有匹配的数据行将被锁定，直到事务结束。这意味着可以通过锁防止数据被其它事务修改。
# 参数:nowait=True # 查询不阻塞
# skip_locked=True # 忽略锁定的行
# from django.db import transaction
# with transaction.atomic():  # 开启事物
# Person.objects.select_for_update().get(id=4)

# 6 事物
# 开启事物
# from django.db import transaction
# try:
#     from django.db import transaction
#     with transaction.atomic():
#
# except Exception as e:
#     print(str(e))

# 7 使用原生mysql

# Person.objects.raw("select * from app_person") # 一般不用

# 使用pymysql模块操作数据库
# from django.db import connection
# cursor = connection.cursor()
# cursor.execute("sql语句")

# 8 QuerySet方法大全

#
#     def all(self)
#         # 获取所有的数据对象
#
#     def filter(self, *args, **kwargs)
#         # 条件查询
#         # 条件可以是：参数，字典，Q
#
#     def exclude(self, *args, **kwargs)
#         # 条件查询
#         # 条件可以是：参数，字典，Q
#
#     def select_related(self, *fields)
#         性能相关：表之间进行join连表操作，一次性获取关联的数据。
#
#         总结：
#         1. select_related主要针一对一和多对一关系进行优化。
#         2. select_related使用SQL的JOIN语句进行优化，通过减少SQL查询的次数来进行优化、提高性能。
#
#     def prefetch_related(self, *lookups)
#         性能相关：多表连表操作时速度会慢，使用其执行多次SQL查询在Python代码中实现连表操作。
#
#         总结：
#         1. 对于多对多字段（ManyToManyField）和一对多字段，可以使用prefetch_related()来进行优化。
#         2. prefetch_related()的优化方式是分别查询每个表，然后用Python处理他们之间的关系。
#
#     def annotate(self, *args, **kwargs)
#         # 用于实现聚合group by查询
#
#         from django.db.models import Count, Avg, Max, Min, Sum
#
#         v = models.UserInfo.objects.values('u_id').annotate(uid=Count('u_id'))
#         # SELECT u_id, COUNT(ui) AS `uid` FROM UserInfo GROUP BY u_id
#
#         v = models.UserInfo.objects.values('u_id').annotate(uid=Count('u_id')).filter(uid__gt=1)
#         # SELECT u_id, COUNT(ui_id) AS `uid` FROM UserInfo GROUP BY u_id having count(u_id) > 1
#
#         v = models.UserInfo.objects.values('u_id').annotate(uid=Count('u_id',distinct=True)).filter(uid__gt=1)
#         # SELECT u_id, COUNT( DISTINCT ui_id) AS `uid` FROM UserInfo GROUP BY u_id having count(u_id) > 1
#
#     def distinct(self, *field_names)
#         # 用于distinct去重
#         models.UserInfo.objects.values('nid').distinct()
#         # select distinct nid from userinfo
#
#         注：只有在PostgreSQL中才能使用distinct进行去重
#
#     def order_by(self, *field_names)
#         # 用于排序
#         models.UserInfo.objects.all().order_by('-id','age')
#
#     def extra(self, select=None, where=None, params=None, tables=None, order_by=None, select_params=None)
#         # 构造额外的查询条件或者映射，如：子查询
#
#         Entry.objects.extra(select={'new_id': "select col from sometable where othercol > %s"}, select_params=(1,))
#         Entry.objects.extra(where=['headline=%s'], params=['Lennon'])
#         Entry.objects.extra(where=["foo='a' OR bar = 'a'", "baz = 'a'"])
#         Entry.objects.extra(select={'new_id': "select id from tb where id > %s"}, select_params=(1,), order_by=['-nid'])
#
#      def reverse(self):
#         # 倒序
#         models.UserInfo.objects.all().order_by('-nid').reverse()
#         # 注：如果存在order_by，reverse则是倒序，如果多个排序则一一倒序
#
#
#      def defer(self, *fields):
#         models.UserInfo.objects.defer('username','id')
#         或
#         models.UserInfo.objects.filter(...).defer('username','id')
#         #映射中排除某列数据
#
#      def only(self, *fields):
#         #仅取某个表中的数据
#          models.UserInfo.objects.only('username','id')
#          或
#          models.UserInfo.objects.filter(...).only('username','id')
#
#      def using(self, alias):
#          指定使用的数据库，参数为别名（setting中的设置）
#
#
#     ##################################################
#     # PUBLIC METHODS THAT RETURN A QUERYSET SUBCLASS #
#     ##################################################
#
#     def raw(self, raw_query, params=None, translations=None, using=None):
#         # 执行原生SQL
#         models.UserInfo.objects.raw('select * from userinfo')
#
#         # 如果SQL是其他表时，必须将名字设置为当前UserInfo对象的主键列名
#         models.UserInfo.objects.raw('select id as nid from 其他表')
#
#         # 为原生SQL设置参数
#         models.UserInfo.objects.raw('select id as nid from userinfo where nid>%s', params=[12,])
#
#         # 将获取的到列名转换为指定列名
#         name_map = {'first': 'first_name', 'last': 'last_name', 'bd': 'birth_date', 'pk': 'id'}
#         Person.objects.raw('SELECT * FROM some_other_table', translations=name_map)
#
#         # 指定数据库
#         models.UserInfo.objects.raw('select * from userinfo', using="default")
#
#         ################### 原生SQL ###################
#         from django.db import connection, connections
#         cursor = connection.cursor()  # cursor = connections['default'].cursor()
#         cursor.execute("""SELECT * from auth_user where id = %s""", [1])
#         row = cursor.fetchone() # fetchall()/fetchmany(..)
#
#
#     def values(self, *fields):
#         # 获取每行数据为字典格式
#
#     def values_list(self, *fields, **kwargs):
#         # 获取每行数据为元祖
#
#     def dates(self, field_name, kind, order='ASC'):
#         # 根据时间进行某一部分进行去重查找并截取指定内容
#         # kind只能是："year"（年）, "month"（年-月）, "day"（年-月-日）
#         # order只能是："ASC"  "DESC"
#         # 并获取转换后的时间
#             - year : 年-01-01
#             - month: 年-月-01
#             - day  : 年-月-日
#
#         models.DatePlus.objects.dates('ctime','day','DESC')
#
#     def datetimes(self, field_name, kind, order='ASC', tzinfo=None):
#         # 根据时间进行某一部分进行去重查找并截取指定内容，将时间转换为指定时区时间
#         # kind只能是 "year", "month", "day", "hour", "minute", "second"
#         # order只能是："ASC"  "DESC"
#         # tzinfo时区对象
#         models.DDD.objects.datetimes('ctime','hour',tzinfo=pytz.UTC)
#         models.DDD.objects.datetimes('ctime','hour',tzinfo=pytz.timezone('Asia/Shanghai'))
#
#         """
#         pip3 install pytz
#         import pytz
#         pytz.all_timezones
#         pytz.timezone(‘Asia/Shanghai’)
#         """
#
#     def none(self):
#         # 空QuerySet对象
#
#
#     ####################################
#     # METHODS THAT DO DATABASE QUERIES #
#     ####################################
#
#     def aggregate(self, *args, **kwargs):
#        # 聚合函数，获取字典类型聚合结果
#        from django.db.models import Count, Avg, Max, Min, Sum
#        result = models.UserInfo.objects.aggregate(k=Count('u_id', distinct=True), n=Count('nid'))
#        ===> {'k': 3, 'n': 4}
#
#     def count(self):
#        # 获取个数
#
#     def get(self, *args, **kwargs):
#        # 获取单个对象
#
#     def create(self, **kwargs):
#        # 创建对象
#
#     def bulk_create(self, objs, batch_size=None):
#         # 批量插入
#         # batch_size表示一次插入的个数
#         objs = [
#             models.DDD(name='r11'),
#             models.DDD(name='r22')
#         ]
#         models.DDD.objects.bulk_create(objs, 10)
#
#     def get_or_create(self, defaults=None, **kwargs):
#         # 如果存在，则获取，否则，创建
#         # defaults 指定创建时，其他字段的值
#         obj, created = models.UserInfo.objects.get_or_create(username='root1', defaults={'email': '1111111','u_id': 2, 't_id': 2})
#
#     def update_or_create(self, defaults=None, **kwargs):
#         # 如果存在，则更新，否则，创建
#         # defaults 指定创建时或更新时的其他字段
#         obj, created = models.UserInfo.objects.update_or_create(username='root1', defaults={'email': '1111111','u_id': 2, 't_id': 1})
#
#     def first(self):
#        # 获取第一个
#
#     def last(self):
#        # 获取最后一个
#
#     def in_bulk(self, id_list=None):
#        # 根据主键ID进行查找
#        id_list = [11,21,31]
#        models.DDD.objects.in_bulk(id_list)
#
#     def delete(self):
#        # 删除
#
#     def update(self, **kwargs):
#         # 更新
#
#     def exists(self):
#        # 是否有结果

# 9 Django终端打印SQL语句

#
#     在Django项目的settings.py文件中，在最后复制粘贴如下代码：
#
#     复制代码
#     LOGGING = {
#         'version': 1,
#         'disable_existing_loggers': False,
#         'handlers': {
#             'console':{
#                 'level':'DEBUG',
#                 'class':'logging.StreamHandler',
#             },
#         },
#         'loggers': {
#             'django.db.backends': {
#                 'handlers': ['console'],
#                 'propagate': True,
#                 'level':'DEBUG',
#             },
#         }
#     }
#     复制代码
#     即为你的Django项目配置上一个名为django.db.backends的logger实例即可查看翻译后的SQL语句。

# 10 Django ORM 常用字段和参数

#     AutoField
#     int自增列，必须填入参数 primary_key=True。
#     当model中如果没有自增列，则自动会创建一个列名为
#     id的列。
#
#
#     IntegerField
#     一个整数类型,范围在 -2147483648 to 2147483647。
#
#
#     CharField
#     字符类型，必须提供max_length参数，
#     max_length表示字符长度
#
#
#     DateField
#     日期字段，日期格式  YYYY-MM-DD，
#     相当于Python中的datetime.date()实例。
#
#
#     DateTimeField
#     日期时间字段，格式
#     YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]，
#     相当于Python中的datetime.datetime()实例
#
#
#
#     AutoField(Field)
#             - int自增列，必须填入参数 primary_key=True
#
#     BigAutoField(AutoField)
#         - bigint自增列，必须填入参数 primary_key=True
#
#         注：当model中如果没有自增列，则自动会创建一个列名为id的列
#         from django.db import models
#
#         class UserInfo(models.Model):
#             # 自动创建一个列名为id的且为自增的整数列
#             username = models.CharField(max_length=32)
#
#         class Group(models.Model):
#             # 自定义自增列
#             nid = models.AutoField(primary_key=True)
#             name = models.CharField(max_length=32)
#
#     SmallIntegerField(IntegerField):
#         - 小整数 -32768 ～ 32767
#
#     PositiveSmallIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField)
#         - 正小整数 0 ～ 32767
#     IntegerField(Field)
#         - 整数列(有符号的) -2147483648 ～ 2147483647
#
#     PositiveIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField)
#         - 正整数 0 ～ 2147483647
#
#     BigIntegerField(IntegerField):
#         - 长整型(有符号的) -9223372036854775808 ～ 9223372036854775807
#
#     BooleanField(Field)
#         - 布尔值类型
#
#     NullBooleanField(Field):
#         - 可以为空的布尔值
#
#     CharField(Field)
#         - 字符类型
#         - 必须提供max_length参数， max_length表示字符长度
#
#     TextField(Field)
#         - 文本类型
#
#     EmailField(CharField)：
#         - 字符串类型，Django Admin以及ModelForm中提供验证机制
#
#     IPAddressField(Field)
#         - 字符串类型，Django Admin以及ModelForm中提供验证 IPV4 机制
#
#     GenericIPAddressField(Field)
#         - 字符串类型，Django Admin以及ModelForm中提供验证 Ipv4和Ipv6
#         - 参数：
#             protocol，用于指定Ipv4或Ipv6， 'both',"ipv4","ipv6"
#             unpack_ipv4， 如果指定为True，则输入::ffff:192.0.2.1时候，可解析为192.0.2.1，开启此功能，需要protocol="both"
#
#     URLField(CharField)
#         - 字符串类型，Django Admin以及ModelForm中提供验证 URL
#
#     SlugField(CharField)
#         - 字符串类型，Django Admin以及ModelForm中提供验证支持 字母、数字、下划线、连接符（减号）
#
#     CommaSeparatedIntegerField(CharField)
#         - 字符串类型，格式必须为逗号分割的数字
#
#     UUIDField(Field)
#         - 字符串类型，Django Admin以及ModelForm中提供对UUID格式的验证
#
#     FilePathField(Field)
#         - 字符串，Django Admin以及ModelForm中提供读取文件夹下文件的功能
#         - 参数：
#                 path,                      文件夹路径
#                 match=None,                正则匹配
#                 recursive=False,           递归下面的文件夹
#                 allow_files=True,          允许文件
#                 allow_folders=False,       允许文件夹
#
#     FileField(Field)
#         - 字符串，路径保存在数据库，文件上传到指定目录
#         - 参数：
#             upload_to = ""      上传文件的保存路径
#             storage = None      存储组件，默认django.core.files.storage.FileSystemStorage
#
#     ImageField(FileField)
#         - 字符串，路径保存在数据库，文件上传到指定目录
#         - 参数：
#             upload_to = ""      上传文件的保存路径
#             storage = None      存储组件，默认django.core.files.storage.FileSystemStorage
#             width_field=None,   上传图片的高度保存的数据库字段名（字符串）
#             height_field=None   上传图片的宽度保存的数据库字段名（字符串）
#
#     DateTimeField(DateField)
#         - 日期+时间格式 YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]
#	  参数auto_now 最后修改时间 自动更新
	      auto_now_add 创建时间 创建的时候自动更新 修改不更新
#     DateField(DateTimeCheckMixin, Field)
#         - 日期格式      YYYY-MM-DD
#
#     TimeField(DateTimeCheckMixin, Field)
#         - 时间格式      HH:MM[:ss[.uuuuuu]]
#
#     DurationField(Field)
#         - 长整数，时间间隔，数据库中按照bigint存储，ORM中获取的值为datetime.timedelta类型
#
#     FloatField(Field)
#         - 浮点型
#
#     DecimalField(Field)
#         - 10进制小数
#         - 参数：
#             max_digits，小数总长度
#             decimal_places，小数位长度
#
#     BinaryField(Field)
#         - 二进制类型

# 11 自定义char类型字段：

#     class FixedCharField(models.Field):
#         """
#         自定义的char类型的字段类
#         """
#         def __init__(self, max_length, *args, **kwargs):
#             super().__init__(max_length=max_length, *args, **kwargs)
#             self.length = max_length
#
#         def db_type(self, connection):
#             """
#             限定生成数据库表的字段类型为char，长度为length指定的值
#             """
#             return 'char(%s)' % self.length
#
#
#     class Class(models.Model):
#         id = models.AutoField(primary_key=True)
#         title = models.CharField(max_length=25)
#         # 使用上面自定义的char类型的字段
#         cname = FixedCharField(max_length=25)

# 12 字段参数

# null
# 用于表示某个字段可以为空。
#
# unique
# 如果设置为unique=True 则该字段在此表中必须是唯一的 。
#
# db_index
# 如果db_index=True 则代表着为此字段设置数据库索引。
#
# default
# 为该字段设置默认值。

# 时间字段独有
# DatetimeField、DateField、
# TimeField这个三个时间字段，都可以设置如下属性。

# auto_now_add
# 配置auto_now_add=True，
# 创建数据记录的时候会把当前时间添加到数据库。
#
# auto_now
# 配置上auto_now=True，
# 每次更新数据记录的时候会更新该字段。

# 关系字段
#
# ForeignKey
#
# 键类型在ORM中用来表示外键关联关系，
# 一般把ForeignKey字段设置在 '一对多'中'多'的一方。
# ForeignKey可以和其他表做关联关系同时也可以
# 和自身做关联关系。
#
# 字段参数
# to
# 设置要关联的表
#
# to_field
# 设置要关联的表的字段
#
# related_name
# 反向操作时，使用的字段名，
# 用于代替原反向查询时的'表名_set'。
#

#
# related_query_name
# 反向查询操作时，使用的连接前缀，用于替换表名。
#
# on_delete
# 当删除关联表中的数据时，当前表与其关联的行的行为。
#
# models.CASCADE
# 删除关联数据，与之关联也删除
#
#
# models.DO_NOTHING
# 删除关联数据，引发错误IntegrityError
#
#
# models.PROTECT
# 删除关联数据，引发错误ProtectedError
#
#
# models.SET_NULL
# 删除关联数据，与之关联的值设置为null（前提FK字段需要设置为可空）
#
#
# models.SET_DEFAULT
# 删除关联数据，与之关联的值设置为默认值（前提FK字段需要设置默认值）
#
#
# models.SET
#
# 删除关联数据，
# a. 与之关联的值设置为指定值，设置：models.SET(值)
# b. 与之关联的值设置为可执行对象的返回值，设置：models.SET(可执行对象)
#
#
# def func():
#     return 10
#
# class MyModel(models.Model):
#     user = models.ForeignKey(
#         to="User",
#         to_field="id"，
#         on_delete=models.SET(func)
#     )
#
# db_constraint
# 是否在数据库中创建外键约束，默认为True。

# OneToOneField

# 一对一字段。
#
# 通常一对一字段用来扩展已有字段。
#
# 示例
# 一对一的关联关系多用在当一张表的不同字段查询
# 频次差距过大的情况下，将本可以存储在一张表的
# 字段拆开放置在两张表中，然后将两张表建立一对
# 一的关联关系。
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=32)
#     info = models.OneToOneField(to='AuthorInfo')
#
#
# class AuthorInfo(models.Model):
#     phone = models.CharField(max_length=11)
#     email = models.EmailField()
#
#
# 字段参数
# to
# 设置要关联的表。
#
# to_field
# 设置要关联的字段。
#
# on_delete
# 同ForeignKey字段。

# ManyToManyField

# 用于表示多对多的关联关系。
# 在数据库中通过第三张表来建立关联关系。
#
# 字段参数
# to
# 设置要关联的表
#
# related_name
# 同ForeignKey字段。
#
# related_query_name
# 同ForeignKey字段。
#
# symmetrical
# 仅用于多对多自关联时，指定内部是否创建反向操作的字段。默认为True。
#
# 举个例子：
#
# class Person(models.Model):
#     name = models.CharField(max_length=16)
#     friends = models.ManyToManyField("self")
# 此时，person对象就没有person_set属性。
#
# class Person(models.Model):
#     name = models.CharField(max_length=16)
#     friends = models.ManyToManyField("self", symmetrical=False)
# 此时，person对象现在就可以使用person_set属性进行反向查询。
#
# through
# 在使用ManyToManyField字段时，Django将自动生成一张表来管理多对多的关联关系。
#
# 但我们也可以手动创建第三张表来管理多对多关系，此时就需要通过through来指定第三张表的表名。
#
# through_fields
# 设置关联的字段。
#
# db_table
# 默认创建第三张表时，数据库中表的名称。
#
# 多对多关联关系的三种方式
#
# 方式一：自行创建第三张表
#
# class Book(models.Model):
#     title = models.CharField(max_length=32, verbose_name="书名")
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=32, verbose_name="作者姓名")
#
#
# # 自己创建第三张表，分别通过外键关联书和作者
# class Author2Book(models.Model):
#     author = models.ForeignKey(to="Author")
#     book = models.ForeignKey(to="Book")
#
#     class Meta:
#         unique_together = ("author", "book")
#
#
# 方式二：通过ManyToManyField自动创建第三张表
# class Book(models.Model):
#     title = models.CharField(max_length=32, verbose_name="书名")
#
#
# # 通过ORM自带的ManyToManyField自动创建第三张表
# class Author(models.Model):
#     name = models.CharField(max_length=32, verbose_name="作者姓名")
#     books = models.ManyToManyField(to="Book", related_name="authors")
#
# 方式三：设置ManyTomanyField并指定自行创建的第三张表
#
# class Book(models.Model):
#     title = models.CharField(max_length=32, verbose_name="书名")
#
#
# # 自己创建第三张表，并通过ManyToManyField指定关联
# class Author(models.Model):
#     name = models.CharField(max_length=32, verbose_name="作者姓名")
#     books = models.ManyToManyField(to="Book", through="Author2Book", through_fields=("author", "book"))
#     # through_fields接受一个2元组（'field1'，'field2'）：
#     # 其中field1是定义ManyToManyField的模型外键的名（author），field2是关联目标模型（book）的外键名。
#
#
# class Author2Book(models.Model):
#     author = models.ForeignKey(to="Author")
#     book = models.ForeignKey(to="Book")
#
#     class Meta:
#         unique_together = ("author", "book")
#
#
#
# 注意：
#
# 当我们需要在第三张关系表中存储额外的字段时，
# 就要使用第三种方式。
#
# 但是当我们使用第三种方式创建多对多关联关系时，
# 就无法使用set、add、remove、clear方法来
# 管理多对多的关系了，需要通过第三张表的model
# 来管理多对多关系。
#
# 元信息
# ORM对应的类里面包含另一个Meta类，
# 而Meta类封装了一些数据库的信息。主要字段如下:
#
# db_table
# ORM在数据库中的表名默认是 app_类名，
# 可以通过db_table可以重写表名。
#
# index_together
# 联合索引。
#
# unique_together
# 联合唯一索引。
#
# ordering
# 指定默认按什么字段排序。
#
# 只有设置了该属性，我们查询到的结果才
# 可以被reverse()

# 13 ORM字段与数据库实际字段的对应关系


# 'AutoField': 'integer AUTO_INCREMENT',
# 'BigAutoField': 'bigint AUTO_INCREMENT',
# 'BinaryField': 'longblob',
# 'BooleanField': 'bool',
# 'CharField': 'varchar(%(max_length)s)',
# 'CommaSeparatedIntegerField': 'varchar(%(max_length)s)',
# 'DateField': 'date',
# 'DateTimeField': 'datetime',
# 'DecimalField': 'numeric(%(max_digits)s, %(decimal_places)s)',
# 'DurationField': 'bigint',
# 'FileField': 'varchar(%(max_length)s)',
# 'FilePathField': 'varchar(%(max_length)s)',
# 'FloatField': 'double precision',
# 'IntegerField': 'integer',
# 'BigIntegerField': 'bigint',
# 'IPAddressField': 'char(15)',
# 'GenericIPAddressField': 'char(39)',
# 'NullBooleanField': 'bool',
# 'OneToOneField': 'integer',
# 'PositiveIntegerField': 'integer UNSIGNED',
# 'PositiveSmallIntegerField': 'smallint UNSIGNED',
# 'SlugField': 'varchar(%(max_length)s)',
# 'SmallIntegerField': 'smallint',
# 'TextField': 'longtext',
# 'TimeField': 'time',
# 'UUIDField': 'char(32)',


# 14 orm性能优化
# 基本
# 查询一张表比查询跨表的速度快
#
# 1 两张关系表优化（取出的值是字典）
#     使用a = xx.objects.all() 获取表的queryset
#     使用若跨表获取字段会查询多次
#         解决办法
#             xxx.objects.all().values('字段1'，字段2) 只会查询一次
#             取出的值是字典形式
# 2 两张关系表优化（取出的值是对象）
#     1 适用于外键，1对1
#         使用a =xxx.obj.all().select_related('外键')
# 3 多张表的联表查询（多次查询）
#     查玩一个表没有，在去另一个表去查
#     a = xx.objects.all().prefetch_related('外键')
#
# 4 只拿对象当中的字段
#     a = xx.objects.all().only('字段名')
# 5 只拿除了填写参数意外的字段
#     a = xx.objects.all().only('字段名')
1
# =================================================


