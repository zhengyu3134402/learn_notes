# pip3 install -i https://pypi.douban.com/simple 软件名
# ============================================
# 数据分析(推荐使用jupyter)
#
#     提取数据，分析
#     数据分析三剑客Numpy Pandas Matplotlib
#
#
# NumPy
#
#     1 概念
#
#         支持大量的维度数组与矩阵运算
#
#     2 创建维数据
#
#         0 注意
#             默认数组所有元素类型相同
#             如果传进来的类型不同，则自动统一为统一类型，优先级 str>float>int
#
#         1 一维数据
#             # import numpy
#             # a = numpy.array([1,2,3,4,5])
#             # print(a)
#             # >>> [1 2 3 4 5]
#
#         2 二维数组创建
#             # import numpy
#             #
#             # a = numpy.array([[1,2,3],[4,5,6],[6,7,8]])
#             # print(a)
#             # >>> [[1 2 3]
#                 #  [4 5 6]
#                 #  [6 7 8]]
#
#     3 获取图片中的数组
#         import matplotlib.pyplot as plt
#
#         a = plt.imread("aa.jpg")
#         print(a)
#         # >>> [[[ 25   3   6]
#         #   [ 25   3   6]
#         #   [ 25   3   6]
#         #   ...
#         #   [ 18 209 238]
#         #   [ 40 241 255]
#         #   [ 22 228 252]]
#         #
#         #  [[ 25   3   6]
#         #   ....
#         #   [137 141 142]]]
#
#
#
#     4 操作数组改变图片
#
#         1 根据数组显示图片
#             plt.imshow(a)
#         2 获取数组的形状
#             print(a.shape)
#             (313, 500, 3) # 前俩个表示图片的像素 ，最后一个是颜色
#
#     5 创建数组常用函数
#
#         1 numpy.ones # 数组元素都是1
#             import numpy
#             a = numpy.ones(shape=(20, 30)) # 20行，30列
#
#         2 numpy.zeros(shape) # 数组元素都是0
#             a = numpy.zeros(shape=(20, 30))
#             print(a)
#
#         3 numpy.full  # 能改变填充的元素创建数组
#             import numpy
#             a = numpy.full(shape=(5, 6), fill_value=100)
#             print(a)
#             # >>> [[100 100 100 100 100 100]
#                 #  [100 100 100 100 100 100]
#                 #  [100 100 100 100 100 100]
#                 #  [100 100 100 100 100 100]
#                 #  [100 100 100 100 100 100]]
#
#         4 numpy.linspace # 创建等差数列(一维)
#
#             import numpy
#             a = numpy.linspace(1, 20, num=10)
#             print(a)
#             # >>> [ 1.          3.11111111  5.22222222  7.33333333
#                 # 9.44444444 11.55555556
#                 # 13.66666667 15.77777778 17.88888889 20.        ]
#
#         5 numpy.arange # 平均等差数列（一维）
#
#             import numpy
#             a = numpy.arange(1, 20, step=2)
#             print(a)
#             # >>>[ 1  3  5  7  9 11 13 15 17 19]
#
#         6 numpy.random.randint # 生产随机整数数组
#             import numpy
#
#             numpy.random.seed(10)  # 时随机数组固定，即使多次运行
#
#             a = numpy.random.randint(1,50, size=(3,5))
#             # >>> [[42 15 47 47 12]
#                 #  [31  8 16 20 35]
#                 #  [ 8 30  4 15 10]]
#
#         7 numpy.random.randn  # 生产标准正太分布数组
#
#             import numpy
#             a = numpy.random.randn(2,4)
#             print(a)
#             # [[ 0.43646328  0.22035996  0.06767324 -0.95844809]
#             #  [ 0.89201479 -1.33556497  0.56265823 -0.8222877 ]]
#
#         8 numpy.random.random # 生产0到1之间数组
#
#             import numpy
#             a = numpy.random.random(size=(3, 4))
#             print(a)
#
#             # >>> [[0.38106001 0.62423657 0.22771515 0.76801192]
#             #     [0.98463833 0.47753113 0.78799038 0.69614544]
#             #     [0.84380187 0.72620189 0.27030569 0.80435681]]
#
#     6 数组的属性
#
#         x.ndim  # 维度
#         x.shape # 形状
#         x.size  # 总长度
#         x.dtype # 元素类型
#
#     7 操作ndarray（数组）
#
#         1 索引
#             和python列表同理
#
#         2 切片
#
#            arr = [[ 96 108 111 100]
#                   [ 76 113  80  82]
#                   [ 71 106  89 104]
#                   [110  85 110  99]
#                   [117 103  80  85]
#                   [ 86 116  75  91]]
#
#            1 获取二维数组前两列
#                 a[:, 0:2]   # 第一个是行，第二个是列
#                 # >>> array([[ 96, 108],
#                              [ 76, 113],
#                              [ 71, 106],
#                              [110,  85],
#                              [117, 103],
#                              [ 86, 116]])
#
#            2 数组行倒叙
#                 a[::-1]
#                 array([[ 86, 116,  75,  91],
#                        [117, 103,  80,  85],
#                        [110,  85, 110,  99],
#                        [ 71, 106,  89, 104],
#                        [ 76, 113,  80,  82],
#                        [ 96, 108, 111, 100]])
#            3 数组列倒叙
#                 a[:, ::-1]
#                 array([[100, 111, 108,  96],
#                        [ 82,  80, 113,  76],
#                        [104,  89, 106,  71],
#                        [ 99, 110,  85, 110],
#                        [ 85,  80, 103, 117],
#                        [ 91,  75, 116,  86]])
#
#            4 全部倒叙
#                 a[:, ::-1]
#                 array([[ 91,  75, 116,  86],
#                        [ 85,  80, 103, 117],
#                        [ 99, 110,  85, 110],
#                        [104,  89, 106,  71],
#                        [ 82,  80, 113,  76],
#                        [100, 111, 108,  96]])
#            5 将图片进行全倒置操作
#                 import matplotlib.pyplot as plt
#                 a = plt.imread("aa.jpg")
#                 plt.imshow(a[::-1, ::-1])
#
#
#
#         3 变形
#              array([[73, 85, 60, 79, 83, 66],
#                    [63, 73, 82, 93, 86, 82],
#                    [78, 87, 85, 81, 85, 83],
#                    [50, 67, 69, 81, 50, 61],
#                    [92, 74, 81, 98, 76, 51]])
#
#             1 将多维数组变形成一维数组
#                 a.reshape(30)   # 因为有30个元素
#                 array([74, 56, 53, 67, 76, 69,
#                 61, 61, 97, 64, 60, 63, 78, 78,
#                 66, 51, 88, 78, 57, 96, 71, 69,
#                 65, 83, 79, 66, 83, 50, 68, 99])
#
#             2 将一维数组变成多维数组
#                 b.reshape(6,5)  # 保持形状相同（即30个元素）
#                 array([[68, 69, 71, 58, 79],
#                        [77, 89, 81, 71, 75],
#                        [97, 72, 84, 78, 62],
#                        [56, 90, 78, 76, 54],
#                        [60, 55, 70, 88, 84],
#                        [81, 98, 63, 84, 91]])
#
#             3 reshape的参数
#                 b.reshape(-1:5)  # -1表示自动计算行数或列数
#
#             4 图片倒置
#                 1 获取图片形状
#                 2 将3维图片变成1维
#                 3 对1维数组中所有元素倒置
#                 import matplotlib.pyplot as plt
#                 a = plt.imread("aa.jpg")
#                 print(a.shape)
#                 plt.imshow(a)
#                 b = a.reshape(313*500*3)
#                 c = b[::-1]
#                 plt.imshow(c.reshape(313,500,3))
#
#         4 级联
#
#             合并数组
#             合成成功条件
#                 1 维度相同的两个数组才能级联
#                 2 形状相符数组横向或纵向有一个相同
#
#             1 多维数组中的合并（numpy.concatenate(数组1， 数组2, axis=1)）
#                 参数axis=0 表示竖直的轴向  axis=1 表示水平的轴向 axis=2 z轴（3为数组）
#
#                 1 水平轴向合并数组
#                     import numpy
#                     a = numpy.random.randint(20, 50,(3,4))
#                     numpy.concatenate((a, a), axis=1)
#
#                 2 竖直轴向合并数组
#                     import numpy
#                     a = numpy.random.randint(20, 50,(3,4))
#                     numpy.concatenate((a, a), axis=0)
#                     array([[34, 33, 42, 23],
#                            [39, 49, 41, 21],
#                            [30, 20, 48, 35],
#                            [34, 33, 42, 23],
#                            [39, 49, 41, 21],
#                            [30, 20, 48, 35]])
#
#                 3 合并两张照片
#                     import numpy
#                     import matplotlib.pyplot as plt
#                     a = plt.imread("aa.jpg")
#                     c = numpy.concatenate((a ,a), axis=0)
#                     plt.imshow(c)
#
#         5 切分
#
#             array([[90, 83, 80, 97, 62],
#                    [64, 99, 86, 70, 61],
#                    [93, 89, 95, 52, 92],
#                    [79, 69, 64, 97, 63]])
#
#             1 将数组横切
#
#                 numpy.split(a, [2], axis=0)  # 参数1：数组 参数2：切的位置 参数3：横切竖切
#                 [array([[68, 69, 98, 76, 71],
#                         [99, 97, 95, 94, 94]]),
#                  array([[55, 96, 81, 91, 93],
#                         [71, 59, 96, 99, 56]])]
#
#             2 将数组竖切
#                 [array([[68, 69],
#                         [99, 97],
#                         [55, 96],
#                         [71, 59]]),
#                  array([[98, 76, 71],
#                         [95, 94, 94],
#                         [81, 91, 93],
#                         [96, 99, 56]])]
#
#             3 切分照片
#                 import numpy
#                 import matplotlib.pyplot as plt
#                 a = plt.imread("aa.jpg")
#                 c,d = numpy.split(a, [150], axis=0)  # 参数2若有多个元素 则意味着多切的刀数
#                 plt.imshow(c)
#
#
#         6 副本
#
#             就是用copy创建副本
#
#         7 数组的聚合操作
#
#             1 求和
#
#                 import numpy
#                 a = numpy.random.randint(50, 100, (4,3))
#                 a.sum()  # 所有元素的和
#                 # >>> 872
#
#                 # a.sum(axis=1) # 横向求和
#                 # >>> array([223, 229, 207, 243])
#
#         8 广播机制
#
#             规则
#
#                 1 为缺失维度补1（进行运算的两个数组之间只能相差一个维度）
#                 2 缺失的元素用已有的值填充
#                 3 缺失维度的数组只能有一行或者一列
#
#
#             不同维数的数组运算
#
#             import numpy
#             a = numpy.random.randint(50, 100, (2,3))
#             b = numpy.random.randint(50, 100,(3))
#
#             # a
#                 array([[70, 55, 57],
#                        [58, 79, 94]])
#             # b
#                 array([91, 69, 71])
#
#             # a+b
#                 array([[161, 124, 128],
#                        [149, 148, 165]])
#
#         9 数组的排序
#
#             1 不改变数组的排序
#                 a = numpy.array([4,7,2,9,3])
#                 b = numpy.sort(a)
#                 print(a)
#                 print(b)
#                 # array([2, 3, 4, 7, 9]
#                 # array([4, 7, 2, 9, 3])
#
#             2 改变数组的排序
#
#                 import numpy
#                 a = numpy.array([4,7,2,9,3])
#                 a.sort()
#                 print(a)
#                 # array([2, 3, 4, 7, 9]
#
#             3 部分排序
#
#                 将最小或最大的一部分数放在前或后面
#
#                 import numpy
#                 a = numpy.array([4,7,2,9,3])
#                 b = numpy.partition(a, kth=-1) # 当kth为正，得到最小的kth个数
#                                                # 当kth为负，得到最大的kth个数
#
# Pandas
#
#     1 数据结构
#
#         Series(一维)
#             一种类似与一维数组的对象， 有两部分组成
#             values:一组数据（ndarray类型）
#             index: 相关的数据索引标签（隐式索引，显式索引）
#         DataFrame
#             表格型数据结构
#
#     2 Series的创建
#
#         1 列表创建Series(隐式索引)
#             from pandas import Series, DataFrame
#             a = Series(data=[1,2,3,4])
#             print(a)
#             # >>> 0    1
#                 # 1    2
#                 # 2    3
#                 # 3    4
#                 # dtype: int64
#
#         2 列表创建Series(显式索引)
#             from pandas import Series, DataFrame
#             a = Series(data=[1,2,3,4], index=["a","b","c","d"], name="haha")  # name参数是唯一标识
#             print(a)
#             # >>> a    1
#                 # b    2
#                 # c    3
#                 # d    4
#                 # Name: haha, dtype: int64
#
#         3 使用numpy创建Series
#             a = Series(data=numpy.arange(1,10,2))
#             print(a)
#             # >>> 0    1
#                 # 1    3
#                 # 2    5
#                 # 3    7
#                 # 4    9
#                 # dtype: int32
#
#         4 字典创建Series
#
#             dic = {"a":1, "b":2}
#             a = Series(data=dic)
#             print(a)
#             # >>> a    1
#                 # b    2
#                 # dtype: int64
#
#     3 Series的索引和切片
#
#         1 使用显式索引 和隐式索引 True和False也也已作为索引
#             a = Series(data=[1,2,3,4], index=["a","b","c","d"])
#             print(a.loc["a"])   # 显式索引
#             print(a.iloc[0])  # 隐式索引
#             # >>> 1
#             # >>> 1
#
#
#
#         2 切片
#
#             a = Series(data=[1,2,3,4], index=["a","b","c","d"])
#             print(a.loc["a":"c"])  # 显式切
#             print(a.iloc[0:3])  # 隐式切
#             # >>>
#             # a    1
#             # b    2
#             # c    3
#             # dtype: int64
#             # a    1
#             # b    2
#             # c    3
#             # dtype: int64
#
#         3 添加元素
#
#             a = Series(data=[1,2,3,4], index=["a","b","c","d"])
#             a["fff"] = 999
#             print(a)
#             # >>>
#             # a        1
#             # b        2
#             # c        3
#             # d        4
#             # fff    999
#             # dtype: int64
#
#         4 获取索引，如果有显式，显示显式索引，如果没有，显示隐式索引
#
#             a = Series(data=[1,2,3,4], index=["a","b","c","d"])
#             print(a.index)
#             # >>> Index(['a', 'b', 'c', 'd'], dtype='object')
#
#         5 获取值
#             a = Series(data=[1,2,3,4], index=["a","b","c","d"])
#             print(a.values)
#             # >>> [1 2 3 4]
#
#         4 获取前n个值 和后n个值
#
#             a = Series(data=[1,2,3,4], index=["a","b","c","d"])
#             print(a.head(2))
#             print(a.tail(2))
#
#             # >>> a    1
#                 # b    2
#                 # dtype: int64
#             # >>> c    3
#                 # d    4
#                 # dtype: int64
#
#         4 去重
#             a = Series(data=[1,1,2,2,3,3,4])
#             print(repr(a.unique()))
#             # >>> array([1, 2, 3, 4], dtype=int64)
#
#         5 检测和过滤缺失数据
#             a = Series(data=[1,2,3,4,5], index=["a","b","c","d","e"])
#             b = Series(data=[1,2,3,4,5], index=["a","b","f","g","h"])
#             c = a+b
#             print(c)
#             # >>> a    2.0
#                 # b    4.0
#                 # c    NaN
#                 # d    NaN
#                 # e    NaN
#                 # f    NaN
#                 # g    NaN
#                 # h    NaN
#                 # dtype: float64
#
#             1 判断为null的数据, 判断不是null数据 c.notnull()
#                 print(c.isnull())
#                 # >>>
#                     # a    False
#                     # b    False
#                     # c     True
#                     # d     True
#                     # e     True
#                     # f     True
#                     # g     True
#                     # h     True
#                     # dtype: bool
#
#             2 过滤显示不是null的项
#                 print(c.loc[c.notnull()])
#                 # >>> a    2.0
#                     # b    4.0
#                     # dtype: float64
#
#         6 运算
#
#             在运算中自动对齐的不同索引的数据
#             如果索引不对应，则补NaN
#
#     4 DataFrame
#
#         表格型数据结构，按一定顺序排列多列数据组成，将Series的使用
#         场景从一维拓展到二维
#         结构
#             行索引:index
#             列索引:coulums
#             值:values
#
#         1 DataFrame创建(隐式索引)
#
#             from pandas import DataFrame
#             a = DataFrame(data=numpy.random.randint(60, 100, size=(3,3)))
#             print(a)
#             # >>>     0   1   2   3   4
#                 # 0  99  93  93  67  88
#                 # 1  62  68  69  82  78
#                 # 2  81  93  69  80  72
#                 # 3  93  94  93  79  82
#                 # 4  70  91  65  68  76
#
#         2 DataFrame创建(显式索引)
#
#             a = DataFrame(data=numpy.random.randint(60, 100, size=(3,3)), index=["a","b","c"],columns=["d","e","f"])
#             print(a)
#             # >>>    d   e   f
#                 # a  83  76  79
#                 # b  96  73  93
#                 # c  74  67  74
#
#         3 DataFrame相关属性
#             # 1 获取二维数组
#                 print(repr(a.values))
#                 # >>>
#                 # array([[72, 88, 89],
#                        # [82, 83, 93],
#                        # [69, 99, 71]])
#             # 2 获取列索引
#                 print(repr(a.columns))
#                 # >>>Index(['d', 'e', 'f'], dtype='object')
#
#             # 3 获取行索引
#                 print(repr(a.index))
#                 # >>> Index(['a', 'b', 'c'], dtype='object')
#
#             # 4 获取数组形状
#                 print(repr(a.shape))
#                 # >>> (3, 3)
#
#         4 使用字段创建DataFrame
#
#             div = {"a":[1,2,3], "b":[4,5,6]}
#             a = DataFrame(data=div)
#             print(a)
#             # >>>    a  b
#                 # 0  1  4
#                 # 1  2  5
#                 # 2  3  6
#
#         5 操作DateFrame
#             a = DataFrame(data=numpy.random.randint(2,10, (3,3)), index=["a","b","c"], columns=["e", "f", "g"])
#                e  f  g
#             a  7  6  3
#             b  7  4  7
#             c  6  5  2
#
#             1 获取列元素
#                 print(a['g'])
#                 # >>> a    3
#                       b    7
#                       c    2
#                       Name: g, dtype: int32
#             2 修改列元素
#                 a["g"]=[999,888,777]
#                 print(a)
#                 # >>>    e  f  g
#                       a  7  6  999
#                       b  7  4  888
#                       c  6  5  777
#             3 获取前两列元素
#
#                 print(a[['e','f']])
#                 # >>>    e  f
#                       a  7  6
#                       b  7  4
#                       c  6  5
#             4 获取行元素
#
#                 print(a.loc['a']) 或a.iloc[1]
#                 # >>>e    7
#                      f    6
#                      g    3
#                      Name: a, dtype: int32
#
#             5 获取某一个元素
#
#                 print(a.loc['b', 'f']) # 第一个元素是行，第二个元素是列
#                 # >>> 4
#
#             6 切片
#
#                 1 行切片
#                     print(a['a':'b'])
#                        e  f  g
#                     a  7  6  3
#                     b  7  4  7
#
#                 2 列裂片
#                     print(a.loc[:,'f':'g'])
#                        f  g
#                     a  6  3
#                     b  4  7
#                     c  5  2
#
#             7 运算
#
#                 同Series一样
#
#
#             8 处理丢失数据
#
#                 isnull ->any
#                 notnull ->all
#
#                 dropna(axis=xx) 过滤丢失数据
#                 drop(labels="xx", axis=xx) # 对某一行或列删除索引
#                 fillna(value=10) # 填充nan的值为10
#                 fillna(method="ffill") # 根据前面的值填充nan
#
#             9 创建多级索引
#                 1 多层列索引
#                     1
#                         a = DataFrame(data=numpy.random.randint(2,10, (3,3)), index=["a","b","c"], columns=[["e", "f", "g"],['j','k','l']])
#                            e  f  g
#                            j  k  l
#                         a  2  7  6
#                         b  6  3  2
#                         c  3  4  4
#                     2
#                         s = pandas.MultiIndex.from_product([['e','f','g'],['aa', 'bb', 'cc']])
#                         a = DataFrame(data=numpy.random.randint(2,10, (3,9)), index=["a","b","c"], columns=s)
#                         print(a)
#
#                 2 多层索引的查询
#                     不能夸索引操作，必须让二级索引变成一级索引后才能进行索引操作
#
#             10 聚合
#                 a.mean() # 平均数
#
#             11 级联
#                 a = DataFrame(numpy.random.randint(0, 100,(4,4)), index=['a','b','c','d'], columns=['A','B','C','D'])
#                 b = DataFrame(numpy.random.randint(0, 100,(3,4)), index=['a','b','c'], columns=['A','B','C','D'])
#
#                     A   B   C   D
#                 a  82  74  42  45
#                 b  13  55  94  35
#                 c  45  54  14  63
#                 d  92  69  87  29
#
#                     A   B   C   D
#                 a   7  93  88  41
#                 b  27  12  74  29
#                 c  37  82  22  47
#
#                 1 c = pandas.concat([a,b], axis=0)
#                     # 其他参数 ignore_index 忽律索引 keys=['x']给a，b命名
#                     # join='outer' 对所有的项进行级联（忽律匹配和不匹配）
#                     # join='inner' 而inner只会将匹配的项级联到一起，不匹配的不级联
#                     # >>>     A   B   C   D
#                           a  82  74  42  45
#                           b  13  55  94  35
#                           c  45  54  14  63
#                           d  92  69  87  29
#                           a   7  93  88  41
#                           b  27  12  74  29
#                           c  37  82  22  47
#
#                 2 a.append()只能列项合并
#
#                 3 pandas.merge()合并（需要依据共同的列进行合并,和mysql联合查找类似）
#
#
#             12 可读取表格
#                 pandas.read_excel()
#
#             13 映射
#             14 分组
#
# matplotlib
#
#     1 画一条直线
#         import matplotlib.pyplot as plt
#
#         x = [1,2,3,4,5]
#         y = [1,2,3,4,5]
#         a = plt.plot(x,y)  # 绘制2位图 直线
#
#     2 画多条直线
#
#         x = [1,2,3,4,5]
#         y = [1,2,3,4,5]
#         a = plt.plot(x,y)  # 绘制2位图 直线
#         b = plt.plot(x,y)  # 绘制2位图 直线
#
#     3 绘制多个图像(会出现3个图像)
#
#         a = plt.subplot(1,2,1)
#         b = plt.subplot(1,2,2)
#         c = plt.subplot(1,2,3)
#
#     4 绘制带有网格的图像
#
#         plt.plot(x, y)
#         plt.grid()
#
#     5 绘制坐标轴刻度
#
#         plt.axis([X轴最小值, X轴最大值,Y轴最小值,Y轴最大值])
#
#         关闭坐标轴
#             plt.axis('off')
#
#         设置画布比例 plt.figure(figsize=(a,b))
#
#
# 近邻算法（KNN）应用于手写识别
