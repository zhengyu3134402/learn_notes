
# 目录
# Bootstrap-->搜索bootstrap前端框架
# css-->搜索csscss
# Es6-->搜索ES6ES6
# html-->搜索htmlhtml
# jquery-->搜索jqueryjquery
# javasprit-->搜索javaspritjavasprit
# vue-->搜索vuevue
# webpack-->搜索webpackwebpack
# VueRuter-->搜索VueRuter
# node.js-->搜索node.js
# vuex--># 搜索vuexvuex
# less --> 搜索 lessless
# JinJa2 --> 搜索jinja2jinja2
# AJAX --> 搜索AJAXAJAX
# Axios --> 搜索AxiosAxios
# vue—cli--> 搜索vue—cli
# =========================================================
# Bootstrap前端框架
1
# 1 介绍

# Bootstrap是Twitter开源的基于HTML、CSS、JavaScript的前端框架。
# 它是为实现快速开发Web应用程序而设计的一套前端工具包。
# 它支持响应式布局，并且在V3版本之后坚持移动设备优先。
# Bootstrap的某些组件依赖于jQuery，所以请确保下载对应版本的jQuery文件，来保证Bootstrap相关组件运行正常
# 响应式开发
# 随着移动设备的流行，网页设计必须要考虑到移动端的设计。同一个网站为了兼容PC端和移动端显示，就需要进行响应式开发。
# 利用媒体查询，让同一个网站兼容不同的终端（PC端、移动端）呈现不同的页面布局。
# 用于查询设备是否符合某一特定条件，这些特定条件包括屏幕尺寸、是否可触摸、屏幕精度、横屏竖屏等信息。

# 2 下载

# 官方地址：https ://getbootstrap.com
# 中文地址：http ://www.bootcss.com/

# 3 使用
# 1 样式

# 1 标题
# h1~h6
# <div class="h1">一级标题36px</div>

# 2 副标题
# small
# <div class="small">2222</div>
# 3 倒三角
# <div class="caret"></div>

# 2 文本

# 1 文本对齐
# text-left text-right text-center
# <div class="text-center">4444444444</div>
# 2 文本大小写
# text-lowercase text-uppercase text-capitalize
# <div class="text-lowercase">ERFresaf</div>
# 3 颜色
# text-muted
# text-primary
# text-success
# text-info
# text-warning
# text-danger

# 3 表格

# 1 表格样式
# .table - striped
# 条纹状表格
# .table - bordered
# 带边框的表格
# .table - hover
# 鼠标悬停变色的表格
# .table - condensed
# 紧缩型表格
# .table - responsive

# 4 按钮

# 1 按钮样式
# btn-default btn-primary btn-success btn-info btn-warning btn-danger btn-link
# <a href="" class="btn btn-default">111</a>
# <button class="btn btn-default">222</button>
# <input type="submit" class="btn btn-default" value="333">
# 2 按钮大小
# btn-lg
# btn-sm
# btn-xs
# 3 按钮不可用
# <button  class ="close">111</button>

# 5 图片

# 1 图片自适应大小
# img-responsive
# 2 图片形状
# img-rounded
# img-circle

# 3 img-thumbnail


# 6 背景

# 1 背景颜色
# bg-primary
# bg-success
# bg-info
# bg-warning
# bg-danger

# 7 浮动

# 1 左右浮动
# pull-left
# pull-right
# 2 块居中
# center-block

# 3 清楚浮动
# clearfix

# 8 显示和隐藏

# 1 显示
# show
# 2 隐藏
# hidden


# 4 常用Bootstrap组件

# 字体图标
# 下拉菜单
# 按钮组
# 输入框俎
# 导航
# 分页
# 标签和徽章
# 页头
# 缩率图
# 进度条
# 模拟滚动的进度条：
# 模拟滚动的进度条

# 5 Bootstrap设置

# 常见属性：
# device - width, device - height
# 屏幕宽、高
# width, height
# 渲染窗口宽、高
# orientation
# 设备方向
# resolution
# 设备分辨率
# 语法：
# @media

# mediatype and | not | only(media
# feature) {
#     CSS - Code;
# }
# 不同的媒体使用不同的stylesheet
#
# < link
# rel = "stylesheet"
# media = "mediatype and|not|only (media feature)"
# href = "mystylesheet.css" >
# viewport
#
# 手机浏览器是把页面放在一个虚拟的
# "窗口"（viewport）中，通常这个虚拟的
# "窗口"（viewport）比屏幕宽，这样就不用把每个网页挤到很小的窗口中（这样会破坏没有针对手机浏览器优化的网页的布局），用户可以通过平移和缩放来看网页的不同部分。

# 6 设置viewport

# 一个常用的针对移动网页优化过的页面的
# viewport
# meta
# 标签大致如下：
#
# < meta
# name =”viewport” content =”width = device - width, initial - scale = 1, maximum - scale = 1″ >
# width：控制
# viewport
# 的大小，可以指定的一个值，如果
# 600，或者特殊的值，如
# device - width
# 为设备的宽度（单位为缩放为
# 100 % 时的
# CSS
# 的像素）。
# height：和
# width
# 相对应，指定高度。
# initial - scale：初始缩放比例，也即是当页面第一次
# load
# 的时候缩放比例。
# maximum - scale：允许用户缩放到的最大比例。
# minimum - scale：允许用户缩放到的最小比例。
# user - scalable：用户是否可以手动缩放。
# Bootstrap的栅格系统
#
# container
# row
# column
1
# =========================================================


# =========================================================
# csscss
1
# 1 选择器

# 1 id选择器
# #a1{
# color: red;
# }
# 2 class选择器
# .a1
# {
# color: blue;
# }
# 3 通用选择器(body内的标签)
# *{
#     color: pink;
# }
# 4 元素选择器
# div
# {
#     color: green;
# }
# 5 后代选择器
# .a li
# {
#     border: 2px solid red;
# }
# 6 儿子选择器
# .a > li
# {
#     border: 2px solid red;
# }
# 7 毗邻选择器
# div + p
# {
#     color: pink;
# }
# 8 弟弟选择器
# div ~p
# {
#     color: green;
# }
# 9 属性选择器
# div[a]
# {
#     color: red;
# }

# div[b = "hehe"]{
#     color: green;
# }
# 10 分组选择器
# .a,.b
# {
#     color: blue;
# }
# 11 选择器的优先级
# 1000 > id100 > 类10 > 元素1 > 继承0，!important方式来强制让样式生效，
# 但并不推荐使用。因为如果过多的使用!important会使样式文件混乱不易维护

# 2 a标签相关样式

# 1 a标签，指定未访问链接的颜色
# a: link
# {
#     color: pink;
# };
# 2 a标签，指定以访问标签的颜色
# a: visited
# {
#     color: yellow;
# }
# 3 a标签，指定鼠标移动到标签上的标签颜色
# a: hover
# {
#     color: red;
# }
# 4 a标签，指定点击链接之后链接的颜色
# a: active
# {
#     color: green;
# }


# 3 input输入框相关样式

# 1 nput输入框，获得聚焦时候的样式
# .a: focus
# {
#     border: 2px solid red;
# }

# 2 input输入框，指定鼠标移动到input框商时的样式
# .a: hover
# {
#     border: 3px solid red;
# }

# 3 input默认文本提示内容
# placeholder="提示内容"

# 4 文本相关样式

# 1 标签文本最前方添加 **
# .a: before
# {
#     content: "**";
# }

# 2 标签文本最后方添加 **
# .a: after
# {
#     content: "**";
# }
# 3 标签文本头字样式
# .a: first - letter
# {
#     color: red;
# }
# 4 文本字体属性
# .a
# {
#     font - family: SimHei;
# }
# 5 字体粗细
# .a
# {
#     font - weight: bold;
# }
# .b
# {
#     font - weight: 1000;
# }
# 6 字体颜色
# .a
# {
#     color: red;
# }
# .a
# {
#     color: rgb(212, 233, 5);
# }
# .a
# {
#     color: rgba(222, 222, 222, 0.4);
# }
# .a
# {
#     color:  # 000;
# }
# 7 文本对齐方式
# text - align
# center
# left
# right
# 8 文本下有一条直线
# .a
# {
#     text - decoration: underline;
# }
# 9 穿过文本一条直线
# .a
# {
#     text - decoration: line - through;
# }
# 10 默认的文本样式
# .a
# {
#     text - decoration: none;
# }
# 11 文本的首行缩进
# .a
# {
#     text - indent: 20px;
# }
# 12 文本垂直居中
# line-height = 父标签高度

# 5 清除浮动

# .clearfix: after
# {
#     content: "";
# clear: both;
# display: block;
# }

# 6 块级标签

# 1 块级标签的宽和高
# .a
# {
#     width: 100px;
# height: 100
# }
# 2 上下左右移动盒子
# .a
# {
#     width: 100px;
# height: 100 px;
# margin - top: 100px;
# margin - left: 100px;
# margin - bottom: 100px;
# margin - right: 100px;
# }
# 3 让盒子水平居中浏览器
# .a
# {
# margin: 0 auto;
# }
# 4 上下左右移动文本距离
# .a
# {
# padding - top: 50px;
# padding - left: 50px;
# padding - bottom: 50px;
# padding - right: 50px;
# }
# 5 盒子的边框
# .a
# {
# border: 2px solid red;
# }
# 6 盒子左右浮动
# .a
# {
#     float: left;
# }

# .b
# {
#     float: right;
# }

# 7 无定位的盒子（默认static）
# .a
# {
#     position: static;
# }
# 8 相对定位的盒子
# .a
# {
#     position: relative;
# }

# 9 绝对定位的盒子
# .a
# {
#     position: absolute;
# }
# 10 固定定位的盒子
# .a
# {
#     position: fixed;
# }
# 11 盒子层叠顺序
# .b
# {
# z - index: 999;
# }
# 12 透明效果
# .a
# {
# opacity: 0.4;
# }
# 13 文本内容使其溢出盒子(默认)
# .a
# {
# overflow: visible;
# }
# 14 修剪溢出的盒子内容
# .a
# {
# overflow: hidden;
# }
# 15 修建内容使其溢出的内容滚动滚动条显示
# .a
# {
# overflow: auto;
# (scroll)
# }
# 16 不占用空间，不显示元素
# .a
# {
#     display: none;
# }
# 17 指定为块级元素
# .a
# {
#     display: block;
# }
# 18 指定为行内元素
# .a
# {
# display: inline;
# }
# 19 指定为行内块元素
# .a{
# display: inline - block;
# }
# 20 占用空间隐藏元素
# .a
# {
# visibility: hidden;
# }

# 7 背景

# 1 标签放入背景图片
# .a
# {
# background - image: url("png1.jpeg");
# }

# 2 背景图片不平铺
# .a
# {
# background - image: url("png1.jpeg");
# background - repeat: no - repeat;
# }

# 3 背景图片平铺排满
# .a
# {
# background - image: url("png1.jpeg");
# background - repeat: repeat;
# }
# 4 背景图在水平方向上平铺
# .a
# background - image: url("png1.jpeg");
# background - repeat: repeat - x;
# }
# 5 垂直方向上平铺
# .a
# {
# background - image: url("png1.jpeg");
# background - repeat: repeat - y;
# }
# 6 调整背景图片位置
# .a
# {
# background - image: url("png1.jpeg");
# background - repeat: no - repeat;
# background - position: 50 % 50 %;
# (right top)
# }


# 8 边框

# 1 点虚线边框
# .a
# {
# border: 2px dotted
# }
# 2 矩形虚线边框
# .a
# {
# border: 2px dashed
# }

# 3 实线边框
# .a
# {
# border: 2px solid
# }

# 4 边框圆角
# .a
# {
# border: 2px solid
# border - radius: 40 % 40 %;
# }

1
# =========================================================


# ==============================================
# ES6ES6
1
# 1 概念
# ECMAScript和Javascript关系
# 前者是后者的规格, 后者是前者的一种实现

# ES6 与 ECMAScript2015 的关系
# ES6 既是一个历史名词,也是一个泛指,含义是 5.1 版本以后的
# JavaScript 的下 一代标准,涵盖了 ES2015 、 ES2016 、
#  ES2017 等,而 ES2015 则是正式名称,特指当年发布的正式版本的语言标准

# 作用域
# let声明变量只有在代码let所在代码快中有效
# 内无let声明 受外部影响以及影响外部
# 不存在变量的提升
# var 调用之后声明 输出为 undefined
# let 调用之后声明 会报错
# 块级作用域允许函数声明条件

# 顶层对象的属性
# 顶层对象属性和全局变量是等价的
# var a =1 等同于 window.a=1
# let 声明的变量不属于不属于顶层对象变量
# 2 使用

# 1 声明变量
# {
# 	var a = 10;
# 	let b = 15;
# }

# 2 const
# const声明一个只读常量,一旦声明,常量值就不能改变,
# 其他用法和let一样

# 3 数组的解构赋值
# let [a,b,c] = [1,2,3]

# 4 解构赋值允许制定默认值
# let [a=1] = []
# console.log(a) # 1
# let [c,b=3] = [5]
# console.log(c) # 5
# console.log(b) # 3


# 5 ===
# ES6内部使用严格相等运算符(===)判断一个位置是否有值,
# 如果一个数组成员不严格等于undefined 默认值是不会生效的
# let[x=1] = [undefined]
# let[y=2] = [null]
# console.log(x) # 1
# console.log(y) # null

# 6 对象结构赋值
# let {a,b}={a:"haha",b:"hehe"}
# 内部机制
# 先找到同名属性,然后再赋值给对应的变量
# 真正复制的是后者,而不是前者

# 7 字符串的解构
# const [a,b,c] = "hel"
# console.log(a)
# console.log(b)
# console.log(c)

# 8 数值和布尔值的解构赋值
# 只要等号右边的不是对象或数组,就先将其转为对象
# undefined和null无法转换为对象
# let {toString:s} = 123
# let {toString:a} = true

# 9 函数参数的解构赋值
# function add([x,y]){
# 	return x+y
# }

# 10 解构的用途
# 1 交互变量值
# let x = 1;
# let y = 2;
# [x,y] = [y,x];

# 2 从函数返回多个值
# function test(){
# 	return [1,2,3]
# };
# let [a,b,c] = test();

# 3 函数参数的定义
# function test([x,y,z]){
# 	...
# }
# test([1,2,3])
# test({z:1,y:2,x:3})

# 4 提取JSON数据
# let jsonData = {id:42,data:[111,222]}
# let {id,data:num} = jsonData


# 5 函数参数的默认值
# function test(a,b=2){
# 	return a+b;
# }
# r = test(1)


# 11 字符串方法
# 1 charAt() 根据字符串给定位置返回字符

# console.log("abcd".charAt(2))

# 2 是否包含了字符串
# let t = "abc".includes("a")

# 3 字符串是否以xx结尾

# let e = "abc".endsWith("c")

# 4 表示将字符串重复参数的次数(小数取整向下取整,负数报错,参数是Infinity会报错)
# let a = "haha";
# console.log(a.repeat(4))

# 5 补全字符串
# let a = "a"
# console.log(a.padStart(5,"|"))

# let b = "b"
# console.log(a.padEnd(5,"|"))

# 6 模板字符串
# 1 换行
# let a = `ha\nha`
# console.log(a)

# 2 多行
# let b = `aaaaa
# aaaaa bbb`
# console.log(b)
# 3 带有变量
# let c = "cccc"
# let d = `i am love ${c}`
# console.log(d)


# 4 引用模板字符串本身
# let a = "return"+"`Hello ${name}`";
# let b = new Function("name", a);
# console.log(b("zhengyu"))

# 7 用来充当模板字符串的处理函数,返回一个反斜线都被转义
# let t= String.raw `Hi\n$(2+3)!`;
# console.log(t) 返回Hi\n$(2+3)!

# 8 转换字符串为整数
# parseInt()
# 9 转换字符串为小数
# parseFloat()

# 10 判处一个值是否为整数
# isInteger()
# 12 函数
# 1 函数的name属性
# function test(){}
# f = test
# console.log(f.name)

# 2 =>定义函数
# var f = () => 5
# console.log(f())

# var a = () => {
# 	return 5
# }
# console.log(a())

# var b = (a,b) => {
# 	return a+b
# }
# console.log(b(2,2))

# 箭头函数注意事项
# 1.函数体内的this对象就是定义时所在的对象,而不是使用时
# 所在的对象
# 2.不可以当作构造函数.也就是说, 不可以使用new命令
# 3.不可以使用argumets对象,使用rest代替
# 4.不可以使用yield命令

# 13 Symbol
# 一种新的原始数据类型Symbol,表示独一无二的值,是js语言
# 的第7中数据类型

# let s = Symbol()
# console.log(s)


# Symbol的参数是一个对象,调用改对象的toString方法,将
# 其转换为字符串,然后才生成一个Symobol值
# const obj = {
# 	toString(){
# 		return "abc"
# 	}
# }
# const s = Symbol(obj)
# console.log(s)
# 返回Symbol(abc)

# 14 Set
# 类似数组,成员唯一不重复

# 可接收数组并初始化
# const set = new Set([1,2,3,4,5,6,4,5,6])
# console.log([...set])
# 返回[1, 2, 3, 4, 5, 6]

# set.size() 返回成员总数
# add(value): 添加某个值,返回Set结构本身
# delete(x):删除某个值,返回一个布尔值,表示删除是否成功
# has(x):返回一个布尔值, 表示参数是否是Set成员
# clear():清除所有成员,没有返回值

# keys() 返回键名的遍历器
# values() 返回键值的遍历器
# entries() 返回键值对的遍历器
# forEach() 使用回调函数遍历每个成员

# 15 WeakSet
# 与Set类是不重复值的集合,但成员只能是对象

# const a = new WeakSet();

# 任何有iterable接口的对象都可以作为WeakSet的参数,所有
# 成员都会自动称为WeakSet实例对象成员

# add(x)
# delete(x)
# has(x)

# WeakSet不能遍历,因为成员都是弱引用,随时可能消失
# 用途为 存储DOM节点,而不用担心节点从文档移除时会引发
# 内存泄漏

# 16 Map
# 类似于对象,也是键值对集合,但键的范围不限于字符串
# const m = new Map();
# const o = {a:"hello"};
# m.set(o,"sssss")
# console.log(m.get(o))
# 返回sssss

# 1 WeakMap
# 与Map结构类是也用于生成键值对的集合

# WeakMap与Map区别:
# 	1 WeakMap只接受对象作为键名(null除外),不接受其他
# 		类型的值作为键名
# 	2 WeakMap的键名所指向的对象不计入垃圾回收机制

# 用途
# 以DOM节点作为键名
# 部署私有属性

# 17 Promise对象
# Promise是异步编程的一种解决方案,比传统的解决方案(回调
# 	函数和时间)更合理而且强大
# 简单来说就是一个容器,里面保存在某个未来才会结束的时间(
# 	通常是一个异步操作)的结果,语法上来说,Promise是一个
# 	对象,从他可以获取异步操作的消息
# 特点
# 	对象的状态不受外界影响,Promise对象代表一个异步操作
# 	有3中状态Pending进行中,Fulfilled已成功,Rejected
# 	(已失败)
# 	一旦状态改变就不会在变,任何时候都可以得到这个结果.
# 	Promise对象的状态改变只有两种可能,从Pending变为
# 	Fulfilled和Pending变为Rejected

# 18 Iterator
# Iterator(遍历器)是一种接口,为各种不同的数据结构提供
# 同一的访问机制,只要部署Iterator接口,就可以完成遍历操作

# Iterator的作用
# 	同一访问的接口
# 	使得数据结构的成员能够按某种次序排列
# 	创造了一种新的遍历命令for ...of

# Iteratord的遍历过程:
# 	1 创建一个指针对象,指向当前数据结构的起始位置.
# 		遍历器对象本质上就是一个指针对象
# 	2 第一次调用指针对象的next方法,可以将指针指向
# 		数据结构的第一个成员
# 	3 第二次调用指针对象的next方法,指针就指向数据
# 		结构的第二个成员
# 	4 不断调用指针对象的next方法,直到它指向数据结构的
# 		结束位置
# 	每次调用next方法都会返回数据结构但前成员的信息,
# 	就是返回一个包含value和done两个属性的对象
# 	value属性是当前成员的值
# 	done属性是一个布尔值,便是遍历是否结束


# Iterator接口

# 	数据结构只要部署了Iterator接口,就成这中数据结构为
# 	可遍历的
# 	ES6规定,默认的Iterator接口部署在数据结构的
# 	Symbol.iterator属性,或者说一个数据结构只要具有
# 	Symbol.iterator属性,就可以认为是可遍历的

# 	let a = ["a", "b", "c"];
# 	调用这个属性就会得到遍历器对象(即指针)
# 	let iter = a[Symbol.iterator]();
# 	console.log(iter.next())

# 19 Generator函数
# Generator函数函数是ES6提供的一种异步编程解决方案,语法行为
# 与传统函数完全不同

# 从语法商理解首先可以把它理解成一个状态机,封装了多个内部状态

# 执行Generator函数会返回一个遍历器对象

# 形式上Generator函数是一个普通函数,一是function命令与函数
# 名之间有一个星号,二是函数体内部使用yield语句定义不同的内部状态

# function* test(){
# 	yield 'hello'
# 	yield 'world'
# 	return 'ending'
# }
# var a = test()
# console.log(a.next()) # {value: "hello", done: false}
# console.log(a.next()) # {value: "world", done: false}
# console.log(a.next()) # {value: "ending", done: true}
# console.log(a.next()) # {value: undefined, done: true}
# 调用Generator函数后,改函数并不执行,返回的也不是函数运行结果
# 而是一个指向内部的指针对象

# 20 async函数
# Generator函数的语法糖

# 21 class的基本语法
# 类的数据类型就是函数,类本身就指向够找函数
# 定义类(传统方法)

# class Test{
# 	constructor(x,y){
# 		this.x = x;
# 		this.y = y;
# 	}

# 	toString(){
# 		return this.x,this.y
# 	}

# }
# var a = new Test(11,22)
# console.log(a.x)

# 22 class继承
1
# ==============================================


# ============================================================
# htmlhtml
1
# 1 跳转（3之后，跳转到百度页面）
# <meta http-equiv="refresh" content="3;URL=https://www.baidu.com">

# 2 列表
# 1 创建一个有序列表
# <ol>
# 	<li>1111</li>
# 	<li>2222</li>
# 	<li>3333</li>
# </ol>
# 2 创建一个无序列表
# <ul>
# 	<li>111</li>
# 	<li>222</li>
# 	<li>333</li>
# </ul>

# 3 标题列表格式如下（dl dt dd）
# 第一
# 	你好
# 第而
# 	再见
# <dl>
# 	<dt>第一</dt>
# 	<dd>你好</dd>
# 	<dt>第二</dt>
# 	<dd>再见</dd>
# </dl>

# 3 浏览器

# 1 创建超链接标签，点击标签后，另开一个网页显示内容(target="_blank")
# <a href="http://www.baidu.com" target="_blank">a</a>

# 2 创建超链接标签，点击标签后，在当前页面现实网页(targe="_self")
# <a href="http://www.baidu.com">a</a>
# 默认targe="_self" 不写也可

# 4 动态
# 1 在页面上显示图片，鼠标移动到图片上后显示提示信息（title=""）
# <img src="html_css_js_jquery/html/png1.jpeg" title="我是提示信息">

# 5 特殊符号

# 在html页面上显示 3个空格 大于号 小于号 与号 元 版权 注册 字符
# <div>空格测试&nbsp&nbsp&nbsp空格测试</div>
# <div>&gt</div>
# <div>&lt</div>
# <div>&amp</div>
# <div>&yen</div>
# <div>&copy</div>
# <div>&reg</div>


# 6 表格
# 创建一个表格格式如下 (table thear tr th tbody tr td)
# 序号 姓名 爱好
# 1	狗	  骨头
# 2   猫	  鱼
# 3   马	  草
# <table>
# 	<thead>
# 		<tr>
# 			<th>序号</th>
# 			<th>姓名</th>
# 			<th>爱好</th>
# 		</tr>
# 	</thead>
# 	<tbody>
# 		<tr>
# 			<td>1</td>
# 			<td>狗</td>
# 			<td>骨头</td>
# 		</tr>
# 		<tr>
# 			<td>2</td>
# 			<td>猫</td>
# 			<td>鱼</td>
# 		</tr>
# 		<tr>
# 			<td>3</td>
# 			<td>马</td>
# 			<td>草</td>
# 		</tr>
# 	</tbody>
# </table>


# 8 文本

# 1创建创建字体大小标签标签（h1~h6）
# <h1>1</h1>
# <h2>1</h2>
# <h3>1</h3>
# <h4>1</h4>
# <h5>1</h5>
# <h6>1</h6>

# 9 标签

# 1 创建段路标签（p）
# <p>111111111</p>


# 2 创建常用容器标签（div）
# <div>1111</div>
# <div>2222</div>
# <div>3333</div>

# 3 创建横线标签（hr）
# <hr>

# 4 创建分段行内标签(span)
# 111<span>hhhh</span>111	<span>hehehe</span>111

# 5 创建插入图片的标签（img）
# <img src="png1.jpeg">

# 6 创建粗体文本标签（b）
# <b>我我我我我</b>

# 7 创建斜体文本标签 (i)
# <i>我我我我我</i>

# 8 创建添加文本下划线标签（u）
# <u>我我我我我</u>

# 9 创建删除文本标签（s）
# <s>我我我我我</s>


# 10 创建上传文件的form标签 制定传输方式post（entype ="multipart/form-data" method="POST"）
# <form method="POST" enctype="multipart/form-data">
# </form>

# 10 input标签

# 1 创建文本标签（text）
# <input type="text" name="">

# 2 创建文本密码标签 （password）
# <input type="password" name="">

# 3 创建日期输入框 (date)
# <input type="date" name="">

# 4 创建单选框（radio）
# <input type="radio" name="">

# 5 创建表单提交按钮（submit）
# <input type="submit" name="" value="提交">

# 6 创建重置按钮（reset）
# <input type="reset" name="" value="重置">

# 7 创建普通按钮（button）
# <input type="button" name="" value="普通按钮">

# 8 创建隐藏输入框（hidden）
# 隐藏输入框<input type="hidden">隐藏输入框

# 9 创建文件上传选择框（file）
# <input type="file" name="">

# 10 创建复选框并使用默认选中属性（checked）
# <input type="checkbox" name="">1
# <input type="checkbox" name="" checked="">2

# 11 创建下拉输入框 并使用默认选中属性 和多选属性 和进行属性（select option selected multiple disabled）
# <select multiple>
# 	<option>1111</option>
# 	<option disabled>2222</option>
# 	<option>3333</option>
# 	<option selected>4444</option>
# </select>

# 12 创建多行文本框 并设置宽高 和禁用属性（textarea cols rows disabled）
# <textarea cols=4 rows=10></textarea>

# 13 设置标签为只读标签，选中不了输入不了(readonly input使用)
# <input type="text" name="" readonly>
1
# ============================================================



# ===============================================================
# jqueryjquery
    1
    # 1 选择器

        # 1 使用id选择器选择标签（$("#id")）
        # 2 使用标签选择器选择标签（$("xx")）
        # 3 使用class选择器选择标签（$(".tagName")）
        # 4 使用通用选择器选择标签（$("*")）
        # 5 使用组合选择器选择标签（$("#id,.className,tagName")）
        # 6 选择x标签的所有后代y标签（$("x y")）
        # 7 选择x的锁偶儿子y标签（$("x>y")）
        # 8 选择所有紧挨着x标签后的y标签（$("x+y")）
        # 9 选择x标签之后所有的y标签($(x~y))
        # 10 选择第一个标签（:first）
        # 11 选择最后一个标签（:last）
        # 12 选择索引等于index的标签(:eq(index))
        # 13 匹配所有索引为偶数的元素（从0开始:even）
        # 14 匹配所有索引值为基数的元素（从0开始:odd）
        # 15 匹配所有大于制定索引值的元素（:gt(index)）
        # 16 匹配所有小于索引值给定索引值的元素（:lt(index)）
        # 17 溢出所有满足not条件的标签（:not(元素选择器)）
        # 18 选择所有包含一个或镀铬标签在其内的标签（指从后代元素找 :has(xx)）
        # 19 选择属性等于值的标签（[属性=值]）#}
        # 20 选择属性不等于值的标签([属性不等于])#}
        # 21 选择表单属性为text的input框（:text）
        # 22 选择表单属性为password的input框（:password）
        # 23 选择表单属性为file的input框(:file)
        # 24 选择表单属性为submit的intput框(:submit)
        # 25 选择表单属性为reset的input框(:reset)
        # 26 选择当前标签的下一个元素(.next())
        # 27 选择当前标签下的所有元素(.nextAll())
        # 28 选择当前标签下的所有新元素直到另一个标签（.nextUntil(xx)）#}
        # 29 选择当前标签的上一个元素（.prev()）
        # 30 选择当前标签的上面的所有元素(.prevAll())
        # 31 选择当前标签的上面的所有元素知道另一个标签（.prevUntil(xxx)）#}
        # 32 选择当前标签的父元素（.parent()）
        # 33 选择当前标签的所有父元素(.parents())

    # 2 方法

        # 1 添加制定的css类明（.addClass()）
        # 2 移除指定的css类名(.removeClass())
        # 3 判断样式存在不存在(.hasClass())
        # 4 将所有p标签的字体设置为红色（$("p").css("color","red")）
        # 5 获取匹配元素在当前窗口的相对偏移或设置元素位置（.offset()）
        # 6 获取匹配元素相对父元素的偏移（.position()）
        # 7 获取匹配元素相对滚动条顶部的偏移（.scrollTop()）
        # 8 .offset方法和.position方法区别
                # .offset()方法允许我们检索一个元素相对于文档（document）的当前位置。和 .position()的差别在于：
                # .position()是相对于相对于父级元素的位移。

        # 9 获取尺寸(.height())
            # 获取尺寸(.width())
            # 获取尺寸(.innerHeight())
            # 获取尺寸(.innerWidth())
            # 获取尺寸(.outerHeight())
            # 获取尺寸(.outerWidth())
        # 10 获取第一个匹配元素的html内容(.html())
        # 11 设置所有匹配元素的html内容（.html(val)）
        # 12 获取所有匹配元素的内容(.text())
        # 13 设置所有匹配元素的内容（.text(val)）
        # 14 取得第一个匹配元素的当前值（.val()）
        # 15 设置所有匹配元素的值（.val(xx)）
        # 16 返回第一个匹配元素的属性值（.attr(attrName)）
        # 17 为所有匹配元素设置一个属性值（.attr(attrName,attrValue)）
        # 18 为匹配元素设置多个属性值（.attr({k1:v1,k2:v2})）
        # 19 从每一个匹配元素中删除一个属性(.removeAttr())
        # 20 获取checkbox和radio的属性，移除属性(prop()获取属性 ，removeProp()移除属性)
        # 21 prop和attr的区别
            #（虽然都是属性，但他们所指的属性并不相同，attr所指的属性是HTML标签属性，
            # 而prop所指的是DOM对象属性，可以认为attr是显式的，而prop是隐式的
            # 对于标签上有的能看到的属性和自定义属性都用attr
            # 对于返回布尔值的比如checkbox、radio和option的是否被选中都用prop。）

        # 22 在一个标签的里面添加另一个标签（内部$(A).append(B)）
        # 23 把A标签的里面的最前面添加B标签（内部$(A).prepend(B)）
        # 24 标签后面添加B标签（外部$(A).after(B)）
        # 25 标签的前面添加B标签 （外部$(A).before(B)）
        # 26 从DOM中删除所有匹配的元素（.remove()）
        # 27 删除匹配的元素集合中所有的子节点(.empty())
        # 28 替换节点 (.replaceWith())
        # 29 替换 （.replaceAll()）
        # 30  eplaceAll() 与 replaceWith() 作用相同。
        #        差异在于语法：内容和选择器的位置，
        #         以及 replaceWith() 能够使用函数进行替换。
        # 31 克隆（.clone()）

    # 3 事件

        # 1 绑定事件 处理 click事件（.on( events [, selector ],function(){})
        #     参数：events： 事件
        #     {#selector: 选择器（可选的）
        #     {#function: 事件处理函数）
        # 2 绑定 hover事件
        # 3 绑定blur事件
        # 4 绑定focus事件
        # 5 绑定change事件
        # 6 绑定keyup事件
        # 7 实时监听input输入值变化
        # 8 移除事件（.off( events [, selector ][,function(){}]) 参数：events：
            # {#selector: 选择器（可选的）#}
            # {#function: 事件处理函数）#}
            # 使用`.on()`方法来绑定事件，


        # 9 事件冒泡（<!DOCTYPE html>#}
            # 事件冒泡就是当父元素和子元素存在同一事件时在子元素的事件处理程序中会自动调用其父级元素的事件处理程序。
            # $(function () {
            #     $("#aa").click(function () {
            #         $(this).text("我是div");
            #     });
            #     $("#bb").click(function () {
            #         $(this).parent().css("border", "1px solid red");
            #     });
            # })
            # <div id="aa">1111
            #     <div id="bb">hehe</div>
            # </div>

            # 阻止事件冒泡(event.stopPropagation();)
                # $(function () {
                #     $("#aa").click(function () {
                #         $(this).text("我是div");
                #     });
                #     $("#bb").click(function () {
                #         $(this).parent().css("border", "1px solid red");
                #         event.stopPropagation();
                #     });
                # })
                # <div id="aa">1111
                #     <div id="bb">hehe</div>
                # </div>
        # 10 文档加载完绑定时间，并且阻止默认事件发生（$(document).ready(function(){xxxx})
                # 可简写成$(function(){xxxx})）
                # $(function){xxx} 与 window.onload的区别
                # （window.onload()函数有覆盖现象，必须等待着图片资源加载完成之后才能调用
                # jQuery的这个入口函数没有函数覆盖现象，文档加载完成之后就可以调用（建议使用此函数））

        # 11实现事件委托（事件委托是通过事件冒泡的原理，利用父标签去捕获子标签的事件例子：
            # $(function(){
            #     $("#aa").on("click","li",function(event){
            #         var target = $(event.target);
            #         target.css("background-color","red");
            #     })
            # })
            # <ul id = "aa">
            #      <li>列表1</li>
            #      <li>列表2</li>
            #      <li>列表3</li>
            #      <li>列表4</li>
            #      <li>列表5</li>
            #      <li>列表6</li>
            #  </ul>

    # 4 动画

        # 1 实现动画效果（show([s,[e],[fn]])）
        # 2 实现动画效果（hide([s,[e],[fn]])）
        # 3 实现动画效果（toggle([s],[e],[fn])）
        # 4 实现滑动动画效果（slideDown([s],[e],[fn])
        # 5 实现滑动动画效果（slideUp([s,[e],[fn]])）
        # 6 实现滑动动画效果（slideToggle([s],[e],[fn])）
        # 7 实现淡入淡出动画效果（fadeIn([s],[e],[fn])）
        # 8 实现东如淡出动画效果（fadeOut([s],[e],[fn])）
        # 9 实现东如淡出动画效果（fadeTo([[s],o,[e],[fn]])）
        # 10 实现东如淡出动画效果（fadeToggle([s,[e],[fn]])）

    # 5 函数

        # 1 each函数无缝迭代
            # $(function(){
            #     $("#button").click(function () {
            #         $("li").each(function () {
            #             var a = $(this).text();
            #             $(this).text(a+"haha")
            #         })
            #     })
            # })

    # 2 data()函数
        # 在匹配的元素集合中的所有元素上存储任意相关数据或返回匹配的元素集合中的第
        # 一个元素的给定名称的数据存储的值。（.date()）#}
        # 在匹配的元素上存储任意相关数据(.data(key, value) #}
        # 移除存放在元素上的数据，不加key参数表示移除所有保存的数据。（.removeData(key)
        # $(function(){
        #     $("#button1").click(function () {
        #         $("#aa").data("s",1);
        #     });
        #     $("#button3").click(function () {
        #         var a = $('#aa').data("s");
        #         $("#aa").text(a);
        #     });
        #     $("#button2").click(function () {
        #         $("#aa").removeData("s");
        #     })
        # })
        # <input type="button" id="button1" value="添加数据">
        # <input type="button" id="button2" value="删除数据">
        # <input type="button" id="button3" value="查看数据">
        # <div id="aa"></div>
    1
# ===============================================================


# ==========================================================
# javaspritjavasprit
    1
    # 1 声明变量
        # var a = 1;

    # 2 NaN属性
        # NaN属性是代表非数字值的特殊值。该属性用于指示某个值不是数字。

    # 3 字符串方法

        # 1 创建返回字符串长度 x.length
        # 2 去除字符串两端的空格 x.trim()
        # 3 去除字符串右边的空格 x.trimLeft() x.trimRight()
        # 4 返回字符串的第2个字符 x.charAt(int)
        # 5 返回字符串在字符串中的索引位置 x.indexOf(yy)
        # 6 创建两个字符串拼接 a.concat(x, y)
        # 7 根据索引范围获取元素中的一部分 x.substring(start, end) x.slice(start, end)
        # 8 将字符串转化成小写 a.toLowerCase
        # 9 将字符串转换为大写 a.toUpperCase
        # 10 对字符串进行分割 a.split(x)

    # 4 js的布尔值（true false)
    # 5 null和undefined

        # null表示变量的值是空，undefined则表示只声明了变量，但还没有赋值null
        # null表示值是空，一般在需要指定或清空一个变量时才会使用，如
        # name = null;
        # undefined
        # 表示当声明一个变量但未初始化时，该变量的默认值是undefined。
        # 还有就是函数无明确的返回值时，返回的也是undefined

    # 6 数组

        # 1 定义一个数组获取数组的长度 x.length
        # 2 向数组尾部添加元素 x.push(yy)
        # 3 删除数组尾部元素 x.pop()
        # 4 删除数组头部元素 x.shift()
        # 5 获取部分数组元素 x.slice(start, end)
        # 6 将数组变成字符串 x.join(yy)
        # 7 合并数组(被合并数组不变) x.concat(yy))
        # 8 对数组进行遍历（for (var i in a){} i是索引）
        # var a =[1, 2, 3, 4, 5, 6, 7, 8, 9]
        # for (var i in a){
        # console.log(a[i]);
        # }


    # 7 对象

        # 1 对对象类型查询(typeof(x)
        # 2 创建对象, 并给兑现添加属性
        # 本质上是键值对的集合类似python字典结构
        # var a = new Object()
        # a.name='xxx'

    # 8 流程控制if else, if else if else, switch, for,

    # 9 函数

        # 1 定义一个函数调用
        # function
        # test()
        # {
        #     console.log("haha");
        # }
        # test();
        # 2 定义一个带参数的函数
        # function
        # test(a, b)
        # {
        #     console.log(a + b);
        # }
        # test(2, 2);
        # 3 定义一个带返回值的函数
        # function
        # test(a, b)
        # {
        # return a - b;
        # }
        # var
        # s = test(3, 2);
        # console.log(s);
        # 4 定义一个匿名函数
        # var a = function(b, c)
        # {
        # return b + c;
        # };
        # console.log(a(2, 3));
        # 5 定义一个立即执行的函数
        # (function(a, b){
        # console.log(a+b);
        # })(1, 2);
        # 6 定义一个闭包函数
        # function test(){
        # b = 5;
        # function test1(){
        # console.log(b * 10);
        # }
        # return test1;
        # }
        # test()();


    # 10 Math

        # 1 返回一个数的绝对值（Math.abs）
        # 2 对一个数进行下舍入（Math.floor）
        # 3 返回最大值（Math.max）
        # 4 返回最小值（Math.min）
        # 5 返回一个数的n次幂（Math.pow）
        # 6 返回0到1之间的随机数（Math.random）
        # 7 四舍五入（Math.round）

    # 11 Date

        # 1 获取当前日期
        # var d = new
        # Date();
        # d.toLocaleString()）
        # 2 获取字符串参数指定的日期
        # 3 获取毫秒参数指定的日期
        # 4 获取数字参数指定的日期
        # 5 获取当前日数（d.getDate()）
        # 6 获取当前星期（d.getDay()）
        # 7 获取当前月份 （d.getMonth() + 1）
        # 8 获取完整年份（d.getFullYear()）
        # 9 获取小时（d.getHours()
        # 10 获取分钟（d.getMinutes()）
        # 11 获取秒(d.getSeconds())
        # 12 获取毫秒（d.getMilliseconds()）
        # 13 返回格林威治时间到累计的毫秒数（d.getTime())


    # 12 Json
    # 1 用json数值字符串转换成数字对象对象再转换成字符串 JSON.parse(xx), JSON.stringify(xx)


    # 13 浏览器

        # 1 获取浏览器窗口内部高度window.innerHeight
        # 2 获取浏览器窗口内部宽度window.innerWidth
        # 3 获取浏览器全称navigator.appName
        # 4 获取浏览器厂商和版本的详细字符串navigator.appVersion
        # 5 获取客户端绝浏览器大部分信息navigator.userAgent
        # 6 获取浏览器运行所在操作系统navigator.platform
        # 7 获取当前页面的URLlocation.href
        # 8 跳转到制定页面location.href="url"
        # 9 重新加载页面location.reload()
        # 10 获取可用屏幕的宽度（screen.availWidth）
        # 11 获取可用屏幕的高度（screen.availHeight）
        # 12 打开浏览器新窗口 （window.open()）
        # 13 关闭当前窗口 （window.close()）

    # 14 弹框

        # 1 弹出警告框（alert）
        # 2 弹出确认框（confirm 返回true或false）
        # 3 弹出提示框（prompt（"提示"，“提示”） 返回出入框中的值或null）

    # 15 选择器

        # 1 根据id获取标签（document.getElementById）
        # 2 根据class获取标签（document.getElementsByClassName
        # 3 根据标签名获取标签（document.getElementsByTagName不能设置style）
        # 4 获取本节点包括父节点标签元素（parentElement）
        # 5 获取所有子标签（children）
        # 6 获取第一个子标签元素（firstElementChild）
        # 7 获取最后一个子元素（lasElementChild）
        # 8 获取下一个兄弟标签元素（nextElementSibling）
        # 9 获取上一个兄弟标签元素(previousElementSibling)


    # 16 节点

        # 1 获取文本节点的值(x.innerText | innerHTML)
        # 2 设置文本节点的值（x.innerText = y | innerHtml = z）
        # 3 设置节点的属性（x.setAttribute(键, 值)）
        # 4 获取节点的属性值或值？(x.getAttribute(键))
        # 5 删除节点的属性（x, removeAttribute(键)）
        # 6 获取input标签，select标签，textarea标签的值(xx.value)

    # 17 事件

        # 1 实现onclick事件（步骤创建html获取节点绑定事件节点.onclick = function(){做的事情}）
        # 2 实现双击事件（ondblclick）
        # 3 实现元素获得焦点事件(onfocus)
        # 4 实现元素数取焦点事件(onblur)
        # 5 实现select标签改变事件(onchange)
        # 6 实现按下键盘事件(onkeydown)
        # 7 实现按下键盘并松开事件(onkeypress)
        # 8 实现某个键盘案件被松开事件(onkeyup)
        # 9 实现一张页面或一副图像完成加载事件(onload)
        # 10 实现鼠标按钮被按下事件(onmusedown)
        # 11 实现鼠标移动实事件(onmousemove)
        # 12 实现鼠标从某元素移开事件（onmouseout）
        # 13 实现鼠标移动到某元素之上的事件（onmouseover）
        # 14 实现在本文中文本被选中时发送事件（onselect）
        # 15 实现确认按钮被点击事件（使用对象是form）(onsubmit)


    # 18 方法

        # 1 sort排序
        # 需要注意：
        # 如果调用该方法时没有使用参数，将按字母顺序对数组中的元素进行排序，说得更精确点，是按照字符编码的顺序进行排序。要实现这一点，首先应把数组的元素都转换成字符串（如有必要），以便进行比较。
        # 如果想按照其他标准进行排序，就需要提供比较函数，该函数要比较两个值，然后返回一个用于说明这两个值的相对顺序的数字。比较函数应该具有两个参数


        # 2 降数组的每个元素传递给回调函数（.forEach没有返回值

        # a = [12, 23, 24, 42, 1];
        # a.forEach(function(item, index, input)
        # {
        #     input[index] = item * 10;
        # })
        # document.write(res); // --> undefined;
        # document.write(ary); // --> 通过数组索引改变了原数组

        # 3 删除元素

        # 删除元素，并项数组中添加新元素（.splice()
        # var
        # a = [11, 22, 33, 44, 55, 66];
        # a.splice(2, 0, 9999);
        # document.write(a);

        # 4 返回一个数组元素调用函数处理后的值的新数组（.map()）
        # var
        # a = [11, 22, 33, 44, 55, 66]
        # function
        # test(s)
        # {
        # return s + 1;
        # }
        # document.write(a.map(test))


    # 19 正则

        # 1 创建正则表达式对象方式一（var a = new RegExp("")）
        # 2 创建正则表达式对象方式二(var a = / xxx /)
        # 3 匹配字符串o(se.match( / o / g))
        # 4 查找字符串h在字符串中的索引位置（a.search( / h / g)）
        # 5 对字符串进行切割（a.split( / 0 / g)）
        # 6 对字符o替换成999 （a.replace( / o / g, "999")）
        # 7 匹配一次（s1.replace( / a /, 'sss')）
        # 8 部分大小写的全局匹配(s1.replace( / a / gi, 'ssss'))
    1
# ==========================================================




# =======================================================
# vuevue
1
# 1 介绍

# 简单小巧的核心,渐进式技术栈
# 解耦视图与数据
# 可复用的组件
# 前端路由
# 状态管理
# 虚拟DOM
# MVVM模式
# view 和 viewMolde来之间通过双向绑定建立联写
# 生命周期
# 每个Vue实例创建时,都会经历一系列的初始化过程,同时也会
# 调用相应的声明周期钩子,利用这些钩子,在何时的时机执行
# 我们的业务逻辑

# created
# 	实例创建完成后调用,此阶段完成了数据的观测等,但尚未挂载
# 	$el 还不可用,需奥初始化处理一些数据时比较游泳

# mounted
# 	el挂载到实例上后调用

# beforeDestroy
# 	实例销毁之前调用

# var app = new Vue({
# 	el: "#app",

# 	data:{
# 		a:2
# 	},
# 	created:function(){
# 		console.log(this.a); # 2
# 	},
# 	mounted:function(){
# 		console.log(this.$el) #<div id="app">...<div id="app">
# 	}
# })
# 计算属性
# 模板内的表达式常用于简单的运算,当期过长或逻辑复杂时,难以
# 维护,使用计算属性解决该问题

# 所有计算属性都以函数的形式写在Vue实例内的computed选项内
# 最总返回计算后的结果

# 每一个计算属性都包含一个getter和一个setter

# 计算属性缓存
# 计算属性是基于它的依赖缓存的.一个计算属性所依赖的数据发生
# 变化时,它才会重新取值,所以text只要不便,计算属性也就不更新
# 计算属性和侦听属性

# 计算属性和侦听属性公有的作用

# 观察和相应Vue实例上的数据变动,通常更好的做法是
# 使用计算属性万恶不是watch侦听属性

# 侦听属性(watch)

# 	<div id="aa">{{ fullName }}</div>

# 	var vm = new Vue({
# 	el:'#aa',
# 	data:{
# 		firstName: 'li',
# 		lastName: 'lingling',
# 		fullName: 'li lingling'
# 	},
# 	watch:{
# 		firstName:function(val){
# 			this.fullName = val +' '+this.lastName
# 		},
# 		lastName:function(val){
# 			this.fullName = this.firstName+' '+val
# 		}
# 	}
# })

# 计算属性

# 	<div id="aa">{{ fullName }}</div>

# 	var vm = new Vue({
# 	el: '#aa',
# 	data:{
# 		firstName:'li',
# 		lastName:'lingling'
# 	},
# 	computed:{
# 		fullName:function(){
# 			return this.firstName+' '+this.lastName
# 		}
# 	}
# })


# 计算属性的setter

# fullName变动会自动触发set

# <div id="aa">{{ fullName }}</div>

# var vm = new Vue({

# 	el:'#aa',
# 	data:{
# 		firstName: "li",
# 		lastName: 'lingling'
# 	},
# 	computed:{
# 		fullName:{
# 			get:function(){
# 				return this.firstName+' '+this.lastName
# 			},
# 			set:function(newValue){
# 				var names = newValue.split(' ')
# 				console.log(names)
# 				this.firstName = names[0]
# 				this.lastName = names[names.length-1]
# 			}
# 		}
# 	}
# })

# vm.fullName = 'li yingying'


# 侦听器(watch)

# 作用:

# 	wath选项提供了一个更通用的方法,来相应数据表话,
# 	当需要在数据变化时执行异步或开销较大的操作时使用

# 计算属性无法做到 侦听器能做到的事情

# 设置中间状态 执行异步操作 限制操作频率


# 2 使用

# 安装
# 开发环境版本
# <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

# 1 Vue实例与数据绑定

# <div id="app">
# 	<input type="text" v-model="name" placeholder="你的名字">
# 	<h1>你好, {{ name }}</h1>
# </div>

# <script type="text/javascript">
# 	var app = new Vue({
# 		el: "#app",
# 		data:{
# 			name :''
# 			a:2
# 		}
# 	})
# </script>


# 数据更新

# 当Vue实例被创建时,将一个对象加入Vue的响应式系统中即data:obj
# 通过Vue实例能找到被加入对象的所有属性,当属性发生改变,数据也更新

# var aa = {a:1}

# var vm = new Vue({
# 	data:aa
# })

# console.log(vm.a) // # 1
# console.log(vm.a == aa.a) //true

# vm.a = 2
# console.log(aa.a) //2

# aa.a = 5
# console.log(vm.a) //5

# 不让对象数据更新

# 使用 Object.freeze(obj)

# Vue的属性

# var test = {a:1}
# var vm = new Vue({
# 	el:"#app",
# 	data:test
# })

# console.log(vm.$data === test) //true
# console.log(vm.$el === document.getElementById('app')) // true

# 2 通过Vue 指定 默认建立了双向绑定

# Vue实例本身也代理了data对象里的所有属性
# var ddd = {s:1}
# var app = new Vue({
# 	el: "#app",

# 	data:ddd
# })
# console.log(app.s) # 返回1
# app.s = 2
# console.log(ddd.s) # 返回2

# 3 插值与表达式

# {{  }} 最基本的文本插值方法,自动将双向绑定的文本的数据实时显示出来

# <div id="aa">
# 	{{ arg }}
# </div>
# var app = new Vue({
# 	el:'#aa',
# 	data:{
# 		arg:"我的世界"
# 	}
# })

# 4 过滤器

# {{ | }}

# 可窜联
# {{ arg|filterA|filterB }}

# 可接收参数
# {{ arg|filterA('arg1', 'arg2') }}

# 5 指令与事件

# 1 条件渲染指令 v-if  v-else-if  v-else

# <div id="aa">
# 	<p v-if="ss === 1">if  当ss为1时</p>
# 	<p v-else-if="ss ===2">else if 当ss为2时</p>
# 	<p v-else>else  否则显示改行</p>
# </div>

# var aa = new Vue({
# 	el: '#aa',
# 	data:{
# 		ss:3
# 	}
# })

# 2 v-on
# 绑定事件监听器
# <div id="aa">
# 	<p v-if="show">哈哈哈啊哈</p>
# 	<button v-on:click="h">点击隐藏</button>
# </div>
# var aa = new Vue({
# 	el: '#aa',
# 	data:{
# 		show:true
# 	},
# 	methods:{
# 		h:function(){
# 			this.show = false
# 		}
# 	}
# })

# 3 语法糖
# v-bind  ---->   :
# v-on    ---->	  @

# 4 v-once

# 是定义它的元素或组件只渲染一次,包括元素或组件的所有字节点

# <div id="aa">
# 	<span v-once>{{ mes }}</span>
# 	<div v-once>
# 		<span>{{ mes }}</span>
# 	</div>
# </div>

# var aa = new Vue({
# 	el: '#aa',
# 	data:{
# 		mes: '文本'
# 	}
# })
# 5 v-show

# v-show的用法与v-if基本一致, 只不过v-show是改变元素的css
# 属性display, v-show不能在template上使用

# <div id="aa">
# 	<p v-show="status === 1"> 1111</p>
# </div>

# var a = new Vue({
# 	el: '#aa',
# 	data:{
# 		status:1
# 	}
# })
# 6  v-if 与 v-show

# v-if 更适合经常改变的场景,因为它切换开销相对较大而 v-show适用于频繁切换条件
# 7 列表渲染指令v-for

# 表达式需结合in来使用
# <div id="aa">
# 	<ul>
# 		<li v-for="i in books">{{ i.name }}</li>
# 	</ul>
# </div>

# var aa = new Vue({
# 	el:'#aa',
# 	data:{
# 		books:[
# 			{name:"1111"},
# 			{name:"2222"},
# 			{name:"3333"}
# 		]
# 	}
# })
# 8 表单与v-model

# 1 单选按钮
# <div id="aa">
# 	<input type="radio" v-model="picked" value="html" >
# 	<label>HTML</label>
# 	<br>
# 	<input type="radio" v-model="picked" value="js" >
# 	<label>JS</label>
# 	<br>
# 	<input type="radio" v-model="picked" value="css" >
# 	<label>CSS</label>
# 	<br>
# 	<p>{{ picked }}</p>
# </div>
# var aa = new Vue({
# 	el: '#aa',
# 	data:{
# 		picked:'js'
# 	}
# })
# 2 单个复选框
# <div id="aa">
# 	<input type="checkbox" v-model="picked" name="" value="haha">
# 	<label>{{ picked }}</label>
# </div>

# var a = new Vue({
# 	el:'#aa',
# 	data:{
# 		picked:true
# 	}
# })

# 3 多个复选框

# <div id="aa">
# 	<input type="checkbox" v-model="picked" name="" value="aaaa">
# 	<label>aaaa</label>
# 	<input type="checkbox" v-model="picked" value="bbbb">
# 	<label>bbbb</label>
# 	<input type="checkbox" v-model="picked" value="cccc">
# 	<label>cccc</label>

# 	<p>{{ picked }}</p>
# </div>

# var aa = new Vue({
# 	el: '#aa',
# 	data:{
# 		picked:[]
# 	}
# })

# 4 下拉框

# <div id="aa">
# 	<select v-model="selected">
# 		<option v-for="i in selected1" :value="i.a">{{ i.a }}</option>
# 	</select>
# 	<p>{{ selected }}</p>
# </div>

# var aa = new Vue({
# 	el: '#aa',
# 	data:{
# 		selected:"aaaa",
# 		selected1:[
# 		{a:"aaaa"},
# 		{a:"bbbb"},
# 		{a:"cccc"}
# 		]
# 	}
# })

# 9 v-bind下拉框

# <div id="aa">
# 	<select v-model="selected">
# 		<option v-for="i in selected1" :value="i.a">{{ i.a }}</option>
# 	</select>
# 	<p>{{ selected }}</p>
# </div>

# var aa = new Vue({
# 	el: '#aa',
# 	data:{
# 		selected:"aaaa",
# 		selected1:[
# 		{a:"aaaa"},
# 		{a:"bbbb"},
# 		{a:"cccc"}
# 		]
# 	}
# })

# 10 绑定值(复选)

# 1 进入页面 分别显示 {{ toggle }}  -> false
# 				  {{ value1 }}  -> a
# 				  {{ value2 }}  -> b

# 2 点击复选框 分别显示{{ toggle }}  -> a
# 				  {{ value1 }}  -> a
# 				  {{ value2 }}  -> b

# 3 取消复选框 分别显示 {{ toggle }}  -> b
# 				    {{ value1 }}  -> a
# 				    {{ value2 }}  -> b
# <div id="aa">
# 	<input type="checkbox" v-model="toggle" :true-value="value1" :false-value="value2">
# 	<label>复选</label>
# 	<p>{{ toggle }}</p>
# 	<p>{{ value1 }}</p>
# 	<p>{{ value2 }}</p>
# </div>

# var aa = new Vue({
# 	el: '#aa',
# 	data:{
# 		toggle:false,
# 		value1:'a',
# 		value2:'b'
# 	}
# })
# 11 绑定值(选择列表)

# 1 进入页面 下拉框为空
# 2 选择点击下拉框123 出现值123

# <div id="app">
# 	<select v-model="selected">
# 		<option :value="{ number:123 }">123</option>
# 	</select>
# 	{{ selected.number }}
# </div>

# var app = new Vue({
# 	el: '#app',
# 	data:{
# 		selected:''
# 	}
# })
# 12 自定义指令

# 全局注册

# 	Vue.directive('foucs'.{
# 		选项
# 		})

# 局部注册

# 	var app = new Vue({
# 		el: '#xx',
# 		derectives:{
# 			focus:{
# 				选项
# 			}
# 		}
# 	})

# 自定义指令的选项

# 自定义指令的选项是由几个钩子函数组成的,每个都是可选的。

# • bind :
# 	只调用一次,指令第一次绑定到元素 时调用,用这个钩子
# 	函数可以定义一个在绑定时执行一次的初始化动作.

# • inserted :
# 	被绑定元素插入父节点时调用(父节点存在即可调用,
# 	不必存在于 document 中) .

# • update :
# 	被绑定元素所在的模板更新时调用,而不论绑定值是否变化。通过比较更新前后

# • componentUpdated :
# 	被绑定元素所在模板完成一次更新周期时调用.

# • unbind :
# 	只调用一次,指令与元素解绑时调 用 。的绑定值,
# 	可以忽略不必要的模板更新。

# 钩子函数的参数

# el
# 	指令所绑定的元素,可以用来直接操作 DOM

# binding: 	一个对象,包含以下属性

# 	name		指令名,不包括 v-前缀。
# 	value 		指令的绑定值,例如 v-my-directive="1+ 1", value 的值是 2
# 	oldValue	指令绑定的前一个值,仅在 update 和
# 				componentUpdated 钩子中可用.无论值是否改变都可用
# 	expression	绑定值的字符串形式 。 例如 v-my-directive=" 1 + 1 ”, expression 的值是” 1 +1 ”.
# 	arg 		传给指令的参数。例如 v-my-directive:foo, arg 的值是 foo
# 	modifiers	一个包含修饰符的对象 。 例如 v-my-directive.foo.bar ,修饰符对象 modifiers
# 				的值是{ foo: true, bar: true }
# vnode 			Vue 编译生成的虚拟节点

# oldVnode 		一个虚拟节点仅在 update 和 componentUpdated 钩子中可用


# 插入节点时调用指令(inserted)


# 刚进入页面 input输入框就自动获得了焦点
# <div id="app">
# 	<input type="text" v-focus>
# </div>

# Vue.directive('focus',{
# 	inserted:function(el){
# 		el.focus();
# 	}
# })

# var app = new Vue({
# 	el:'#app'
# })

# v-for的可选参数前项索引

# <div id="app">
# 	<li v-for="(i,index) in aa">
# 		{{ index }}-{{ i.name }}
# 	</li>
# </div>

# var app = new Vue({

# 	el:'#app',
# 	data:{
# 		aa:[
# 			{name:"zhengyu"},
# 			{name:"lingling"},
# 			{name:"yingying"}
# 		]
# 	}
# })


# 对象的v-for 值的展现

# <div id="app">
# 	<li v-for="i in aa">
# 		{{ i }}
# 	</li>
# </div>

# var app = new Vue({
# 	el:'#app',
# 	data:{
# 		aa:{
# 			name:"lingling",
# 			age:"24",
# 			hobby:"sweem"
# 		}
# 	}

# })


# 对象的v-for 值-键的展现


# <div id="app">
# 	<div v-for="(value, key) in aa">
# 		{{ key }}  ----> {{ value }}
# 	</div>
# </div>

# var app = new Vue({
# 	el:'#app',
# 	data:{
# 		aa:{
# 			name:"yingying",
# 			age:18,
# 			hobby:"basketball"
# 		}
# 	}
# })


# 对象的v-for 值-键-索引

# <div id="app">
# 	<li v-for="(value,key,index) in aa">
# 		{{index}}--{{ key }}--->{{ value }}
# 	</li>
# </div>

# var app = new Vue({
# 	el:'#app',
# 	data:{
# 		aa:{
# 			name:'dcxmyao',
# 			age:'18',
# 			hobby:'football'
# 		}
# 	}
# })


# 使用v-for 推荐加上 v-bind:key

# 格式

# <div v-for="item in items" :key="item.id">

# 作用:

# 不加 :key的时候 data项下对象items中的属性顺序调换
# v-for 的时候 不会有所改变
# 解析:
# 添加对象到所列对象最前面,顺序出现下移,若有chenck
# box,经过上向绑定实时更新的数据 选上的checkbox会
# 取消,引顺序混乱,会选择商改checkbox的下一个checkbox

# 加上 :key 则会改变 推荐加上


# ===============================================
# v-on:click.prevent

# 阻止默认事件的发生

# a标签不跳转
# <div id="app">
# 	<a href="http://www.baidu.com" v-on:click.prevent>11</a>
# </div>

# var app = new Vue({

# 	el:'#app',

# })
# ===============================================


# ===============================================
# v-on:click.capture

# 添加事件监听器使用事件捕获模式,在捕获模式下触发

# 下列说明:

# 若不加上事件修饰符.capture,若点击a4

# 	按照向上冒泡顺序,弹出框顺序 a4,a3,a2,a1

# 若将a3 加上.capture ,点击a4

# 	顺序为 捕捉事件,冒泡时间,即 a3,a4,a2,a1

# 若将a3加上.capture,点击a2,

# 	不触发捕捉事件, 顺序为 a2,a1


# <div id="app">
# 	<div id="a1" v-on:click="aa">a1111111111
# 		<div id="a2" v-on:click="aa">
# 			a222222222
# 			<div id="a3" v-on:click.capture="aa">
# 				a3333333333
# 				<div id="a4" v-on:click="aa">a4444444444</div>
# 			</div>
# 		</div>
# 	</div>
# </div>

# var app	= new Vue({

# 	el:'#app',
# 	data:{

# 	},
# 	methods:{
# 		aa:function(){
# 			this.id = event.currentTarget.id
# 			alert(this.id)
# 		}
# 	}
# })
# ===============================================


# ===============================================
# v-on:click.self

# 当前元素自身触发才会触发函数, 冒泡事件不是触发此元素的函数

# 下列说明

# 若不加.self, 点击a2

# 	向上冒泡 a2执行aa, a1执行aa

# 若加.self, 点击a2

# 	向上冒泡 a2执行aa, a1不执行aa

# <div id="app">
# 	<div v-on:click.self="aa" id="a1">a111111111111
# 		<div v-on:click="aa" id="a2">a222222222222</div>
# 	</div>
# </div>


# var aa = new Vue({

# 	el:'#app',
# 	methods:{
# 		aa:function(){
# 			this.id = event.currentTarget.id
# 			alert(this.id)
# 		}
# 	}
# })

# ===============================================
# ===============================================
# v-on:click.passive

# 作用:
# 	1 滚动事件的默认行为,滚动立即触发
# 	2 提供移动端性能

# 在a跳转之前触发事件
# <div id="app">
# 		<a v-on:click.passive="aa" href="http://www.baidu.com">11</div>
# </div>

# var app = new Vue({
# 	el:'#app',
# 	methods:{
# 		aa:function(){
# 			alert("haha")
# 		}
# 	}
# })
# ===============================================

# ===============================================
# 事件处理系统修饰键


# .ctrl
# .alt
# .shift
# .meta


# <div id="app">
# 	<input type="text" v-on:keyup.alt.67="aa">
# 	{{  num }}
# </div>

# var app = new Vue({

# 	el:'#app',
# 	data:{
# 		num:0

# 	},
# 	methods:{
# 		aa:function(){
# 			this.num += 1
# 		}
# 	}

# })
# ===============================================


# ===============================================
# 修饰键与常规按键

# 1 在和 keyup 一起使用时, 时间触发时修饰键必须处于按下状态
# ,只有在按住ctrl的情况下, 才能触发keyup.ctrl

# 2 如果项只按ctrl 触发时间 使用keyCode:keyup.17
# ===============================================


# ===============================================
# 事件触发.exact修饰符

# 作用

# 	精确触发按键


# 1 <button @click.ctrl="onClick">A</button>
# 	按住ctrl和其他键 点击鼠标都能触发事件


# 		<div id="app">
# 			<button v-on:click.ctrl.exact="aa">按住vtrl+鼠标点击触发事件</button>
# 			{{  num }}
# 		</div>

# 		var app = new Vue({
# 		el:'#app',
# 		data:{
# 			num:0
# 		},
# 		methods:{
# 			aa:function(){
# 				this.num += 1
# 			}
# 		}
# 	})

# 2 <button @click.ctrl.exact="onCtrlClick">A</button>
# 	有且只有按住ctrl,点击鼠标的时才能触发事件


# 3 <button @click.exact="onClick">A</button>
# 	不按系统修饰符的按键,点击都能触发
# ===============================================


# ===============================================
# 事件触发鼠标按键修饰符

# left
# right
# middle

# div id="app">
# 	<button v-on:click.middle="aa">鼠标点击触发事件</button>
# 	{{  num }}
# </div>

# var app = new Vue({
# 	el:'#app',
# 	data:{
# 		num:0
# 	},
# 	methods:{
# 		aa:function(){
# 			this.num += 1
# 		}
# 	}
# })
# ===============================================
# ===============================================
# 表单输入绑定

# v-model作用及特性

# 	1 在<input>、<textarea> 及 <select> 元素上创建双向数据绑定

# 	2 v-model会忽略所有表单的元素 value, checked,selected属性
# 		而总是将Vue实例的数据作为数据来源

# 	3 v-model 不会在输入法组合文字过程中得到更新.
# 		如果项处理这个过程,使用input事件
# ===============================================


# ===============================================
# 表单输入绑定v-model 文本

# <div id="app">
# 	<input type="text" v-model="num">
# 	<p>{{ num }}</p>
# </div>

# var app = new Vue({
# 	el:'#app',
# 	data:{
# 		num:''
# 	}
# })
# ===============================================


# ===============================================
# 表单输入绑定v-model 多行文本


# 说明:

# 	像这样在<textarea>1111</textarea>插入值并不会生效

# <div id="app">
# 	<textarea v-model="num"></textarea>
# 	<div>{{ num }}</div>
# </div>

# var app = new Vue({
# 	el:'#app',
# 	data:{
# 		num:''
# 	}
# })
# ===============================================
# ===============================================
# v-model 和 v-bind

# 1 v-model

# 	绑定的值通常是静态字符串(复选框也可以是布尔值)

# 2 v-bind

# 	可以绑定Vue实例的一个动态属性上,绑定html中的标签属性

# ===============================================


# 6 绑定class

# :class 可以与class共存
# 当 isActive:true 时候 class属性中会加载值active

# <div id="aa">
# 	<div :class="{'active': isActive}">1</div>
# </div>

# var aa = new Vue({
# 	el: '#aa',
# 	data:{
# 		isActive:true
# 	}
# })
# 绑定class 用在组件上

# <div id="aa">
# 	<my-com class="dd"></my-com>
# </div>

# Vue.component('my-com',{
# 	template:'<p class="bb cc">hhhh</p>'
# })
# var aa = new Vue({
# 	el: '#aa',
# })

# 被渲染成
# <div id="aa">
# 	<p class="bb cc dd">hhhh</p>
# </div>

# 7 绑定数组语法

# <div id="aa">
# 	<div class="bb" :class="[cc,dd]">1</div>
# </div>
# var aa = new Vue({
# 	el: '#aa',
# 	data:{
# 		cc:'cc',
# 		dd:'dd'
# 	}
# })


# 列表渲染有些数组的变动不能被检测到(因为js的限制)


# 1 利用索引设置一个项
# 2 修改数组的长度

# <div id="app">
# 	<li v-for="i in aa">
# 		{{ i }}
# 	</li>
# </div>

# var app = new Vue({
# 	el:'#app',
# 	data:{
# 		aa:[1,2,3,4],
# 	}
# })

# app.aa[1]=9999
# app.aa.length = 100


# 解决利用索引添加项,修改数组的长度不能被检测更新的问题


# <div id="app">
# 	<li v-for="i in aa">
# 		{{ i }}
# 	</li>
# </div>

# var app = new Vue({
# 	el:'#app',
# 	data:{
# 		aa:[1,2,3,4],
# 	}
# })

# // app.$set(app.aa, 1,9999)
# // app.aa.splice(100)


# 对象更改检测注意事项

# 1 Vue不能检测Vue对象属性的添加或删除
# 对于已经创建的实例，Vue 不能动态添加根级别的响应式属性
# <div id="app">
# 	<li v-for="i in obj">
# 		{{ i }}
# 	</li>
# </div>

# var app = new Vue({
# 	el:'#app',
# 	data:{
# 		obj:1
# 	}
# })
# app.b = 2


# 8 绑定内联样式

# 多重值

# style 绑定中的属性提供一个包含多个值的数组，常用于提供多个带前缀的值，例如：

# <div :style="{ display: ['-webkit-box', '-ms-flexbox', 'flex'] }"></div>
# 这样写只会渲染数组中最后一个被浏览器支持的值。在本例中
# ，如果浏览器支持不带浏览器前缀的 flexbox，那么就只会渲染 display: flex。
# <div id="aa" :style="styles">文本</div>

# var aa = new Vue({
# 	el: '#aa',
# 	data:{
# 		styles:{
# 			color:'red',
# 			fontSize:14+'px'
# 		}
# 	}
# })


# 9 数组方法

# push()
# pop()
# shif()
# splice()
# sort()
# reverse()


# 10 修饰符

# 1 修饰符(.lazy)

# 与事件修饰符类似,v-model 也有修饰符,用于控制数据同步时机

# 1 进入页面显示输入框

# 2 点击输入框 输入数据 {{ message }} 什么都不显示,
#   当失去焦点或按回车时候 {{ message }} 显示输入框
#   中输入的数据


# <div id="app">
# 	<input type="text" v-model.lazy="message">
# 	<p>{{ message }}</p>
# </div>

# var app = new Vue({
# 	el:'#app',
# 	data:{
# 		message:''
# 	}
# })
# 2 修饰符(.number)
# 1 进入页面 输入框内显示123 {{ message }} 显示123
# 	{{ typeof message }} 显示 number

# 2 点击输入框 删除123之后 ,{{ typeof message }} 显示
# 	上string,并且不无法输入数字意外的字符(除e科学记数法)
# 	若输入数字科学定义商无意义 则{{ typeof message }}
# 	会变成 string


# <div id="app">
# 	<input type="number" v-model.number="message">
# 	<p>{{ message }}</p>
# 	<p>{{ typeof message }}</p>
# </div>

# var app = new Vue({
# 	el: '#app',
# 	data:{
# 		message:123
# 	}
# })

# 3 修饰符(.trim) 自动过滤首尾空格

# <div id="app">
# 	<input type="text" v-model.trim="message">
# 	<p>{{ message }}</p>

# </div>

# var app = new Vue({
# 	el: '#app',
# 	data:{
# 		message:''
# 	}
# })
# 按键修饰符


# 格式:

# 	v-on:keyup.按键别名="xx"

# 常用的按键别名

# enter
# tab
# delete  删除和退格键
# esc
# up
# down
# left
# right

# 可通过全局 config.keyCodes 自定义按键修饰名

# Vue.config.keyCodes.f1 = 112


# 例子 点击 up键数字增加1
# <div id="app">
# 	<input v-on:keyup.up="aa">{{ num }}
# </div>

# var app = new Vue({

# 	el: '#app',
# 	data:{
# 		num:0
# 	},
# 	methods:{
# 		aa:function(){
# 			this.num += 1
# 		}
# 	}

# })


# ===============================================


# ===============================================
# 自动匹配按键修饰符


# <div id="app">
# 	<input type="text" v-on:keyup.page-down="aa">{{ num }}
# </div>

# var app = new Vue({

# 	el:'#app',
# 	data:{
# 		num:0

# 	},
# 	methods:{
# 		aa:function(){
# 			this.num += 1
# 		}
# 	}

# })
# ===============================================

# 11 组件

# 1 概念
# Vue的组件就是提高重用性的 让代码可以复用
# 2 使用
# 1 注册
# 1 全局注册

# <div id="app">
#     <my-haha></my-haha>
# </div>
#
# Vue.component('my-haha',{
#     template:'<b>hhhhhhh</b>'
# });
#
# var app = new Vue({
#     el:'#app'
# })
# 2 局部注册
# 注册后的组件只有在该实例作用域下有效
# <div id="app">
#     <my-haha></my-haha>
# </div>
# var aa = {
#     template:"<h1>jjjjjjjjj</h1>"
# }
#
# var app = new Vue({
#     el: '#app',
#     components:{
#         'my-haha':aa
#     }
# })


# 3 Vue组件特殊情况

# 	Vue组件的模板在某些情况下HTML限制,如<table>规定
# 	只允许 <tr> <td> <th>,其他常见限制元素<ul> <ol>
# 	<select>直接使用组件是无效的,可以使用特殊的is属性来挂载组件


# 	<div id="app">
# 		<table>
# 			<tbody is="my-haha"></tbody>
# 		</table>
# 	</div>

# 	Vue.component('my-haha',{
# 		template:'<h1>ccccccccc</h1>'
# 	})

# 	var app = new Vue({
# 		el: '#app'
# 	})

# 4 Vue组件注册component的其他选项(data)

# 1 data使用和实例稍有区别,data必须是函数,将数据return

# <div id="app">
# 	<my-haha></my-haha>
# </div>

# Vue.component('my-haha', {
# 	template: '<h1>{{ message }}</h1>',
# 	data:function(){
# 		return {
# 			message:'yyyyy'
# 		}
# 	}
# });

# var app = new Vue({
# 	el: '#app'
# })
# 2 组件data选项引用外部同一个对象,同步共享

# <div id="app">
# 	<my-haha></my-haha>
# 	<my-haha></my-haha>
# 	<my-haha></my-haha>
# </div>

# var data = {
# 	num:0
# }

# Vue.component('my-haha',{
# 	template:'<button @click="num++">{{ num }}</button>',
# 	data:function(){
# 		return data
#  	}
# })

# var app = new Vue({
# 	el:'#app'
# })

# 3 组件data选项直接返回对象,不同步共享

# <div id="app">
# 	<my-haha></my-haha>
# 	<my-haha></my-haha>
# 	<my-haha></my-haha>
# </div>

# Vue.component('my-haha',{
# 	template:'<button @click="num++">{{ num }}</button>',
# 	data:function(){
# 		return {num:0}
#  	}
# })

# var app = new Vue({
# 	el:'#app'
# })


# 5 使用props传递数据

# 组件间的通信,父组件钥正向的项子组件传递数据或参数,子组件
# 接受到后根据参数的不同内容或执行操作,正向传递的过程
# 是通过props来实现的

# <div id="app">
# 	<my-haha message="jjjjjjjj"></my-haha>
# </div>

# Vue.component('my-haha',{
# 	props:['message'],
# 	template:'<h1>{{ message }}</h1>'
# });

# var app = new Vue({
# 	el: '#app'
# })

# props与data 区别:

# props的数据来之父级
# data是组件自己的数据


# props命名规制

# 使用DOM模板 驼峰命名的props名词为短横分割命名

# <my-haha warking-test="xx"><my-haha>

# props:[warningText]

# 如果使使用的是字符串模板, 可以互绿这些限制


# props传递动态数据

# 注意直接官邸数字,布尔,数组,对象,而不使用v-bind,传递的
# 仅是字符串

# <div id="app">
# 	<input type="text" v-model="parentMessage">
# 	<my-haha :message="parentMessage"></my-haha>
# </div>

# Vue.component('my-haha',{
# 	props:['message'],
# 	template:'<h1>{{ message }}</h1>'
# });

# var app = new Vue({
# 	el: '#app',
# 	data:{
# 		parentMessage:''
# 	}
# })


# 单项数据流

# Vue2.x props传递数据是单向的,也就是父组件数据变化时会
# 传递给子组件,但是反过来不行,为了解耦

# 一种情况

# 父组件传递初始值进来,子组件将它作为初始值保存起来,
# 在自己作用域下可以随意使用和修改
# 了一在组件data内在声明一个数据,应用父组件的prop

# <div id="app">
# 	<my-haha :init-count="1"></my-haha>
# </div>

# Vue.component('my-haha',{

# props:['initCount'],
# template: '<h1>{{ count }}</h1>',
# data:function(){
# 	# // 在组件初始化会获取来自父组件的initCount,之后就
# 	# // 与之无关只用维护count,这样就可以避免直接操作
# 	# // initCount
# 	return {count:this.initCount}
# 	}
# })

# var app = new Vue({
# 	el: '#app'
# })

# 第二种情况

# props作为需要被专版的原始值传入,使用计算属性
# props是对象和数组时,在子组件内改变会影响父组件

# <div id="app">
# 	<my-haha :width="100"></my-haha>
# </div>

# Vue.component('my-haha',{
# props:['width'],
# template: '<h1 :style="style">jjjjjjj</h1>',
# computed:{
# 	style:function(){
# 		return {width:this.width+'px'}
# 	}
# }
# })

# var app = new Vue({
# 	el: '#app'
# })

# props的数据验证

# Vue.component('my-haha',{
# 	props : {

# 	//必须是数字类型
# 	propA : Number ,

# 	//必须是字符串或数字类型
# 	propB : [String , Number] ,

# 	//布尔值 ,如果没有定义,默认值就是 true
# 	propC:{
# 		type : Boolean ,
# 		default : true
# 	},

# 	//数字,而且是必传
# 	propD:{
# 		type: Number ,
# 		required : true
# 	},

# 	//如果是数组或对象,默认值必须是一个函数来返回
# 	propE:{
# 		type : Array ,
# 		default : function(){
# 			return [];
# 	}

# 	//自定义一个验证函数
# 	propF:{
# 		validator : function (value)
# 			return value > 10;
# 			}
# 		}
# 	}
# })

# 自定义事件

# 当子组件项父组件传递数据时,用到自定义事件
# 子组件用$emit()来触发事件,
# 父组件用$on()来仅听子组件的事件

# 父组件也可以直接在子组件的自定义标签上使用v-on来监听
# 子组件触发的自定义事件

# <div id="app">
# 	<p>总数:{{ total }}</p>
# 	<!-- 子组件+1 -1效果 -->
# 	<my-haha @increase="handleGetTotal" @reduce="handleGetTotal"></my-haha>
# </div>

# Vue.component('my-haha',{
# 	template:'<div> <button @click="handleIncrease">+1</button>
# <button @click="handleReduce">-1</button></div>',
# 	data:function(){
# 		return {counter:0}
# 	},
# 	methods:{
# 		handleIncrease:function(){
# 			this.counter++;
# 			// 改变组件的时候 通过$emit()传递给父组件
# 			this.$emit('increase', this.counter);
# 		},
# 		handleReduce:function(){
# 			this.counter--;
# 			this.$emit('reduce',this.counter);
# 		}
# 	}
# });

# var app = new Vue({
# 	el: '#app',
# 	data:{
# 		total:0
# 	},
# 	methods:{
# 		handleGetTotal:function(total){
# 			this.total = total;
# 		}
# 	}
# })

# 自定义组件上使用v-model指令

# 这次组件$emit()的事件名是特殊的 input , 在使用组件的父
# 级,井没有在<my-component>上使用@input= “ handler”,
# 是直接用了 v-model 绑定的一个数据total 。
# 这也可以称作是一 个语法糖

# <div id="app">
# 	<p>总数:{{ total }}</p>
# 	<my-haha v-model="total"></my-haha>
# </div>

# Vue.component('my-haha',{
# 	template: '<button @click="handleClick">+1</button>',
# 	data:function(){
# 		return {counter:0}
# 	},
# 	methods:{
# 		handleClick:function(){
# 			this.counter++;
# 			this.$emit('input', this.counter)
# 		}
# 	}
# });

# var app = new Vue({
# 	el:'#app',
# 	data:{
# 		total:0
# 	}
# })

# 非父子组件通信(中央事件bus)

# <div id="app">
# 	{{ message }}
# 	<my-haha></my-haha>
# </div>

# var bus = new Vue();

# Vue.component('my-haha',{
# 	template:'<button @click="handleEvent">传递事件</button>',
# 	methods:{
# 		handleEvent:function(){
# 			bus.$emit('on-message','来自组件my-haha的内容');
# 		}
# 	}
# });

# var app = new Vue({
# 	el:'#app',
# 	data:{
# 		message:''
# 	},
# 	mounted:function(){
# 		var _this = this;
# 		bus.$on('on-message', function(msg){
# 			_this.message = msg;
# 		});
# 	}
# })


# 父链(不推荐使用,使得组件紧耦合)

# 在子组件中,使用this.$parent可以直接访问改组件的父实例或组件,
# 父组件也可以通过this.$children访问它所有的子组件


# 子组件索引

# 用特殊的属性 $refs来为子组件指定一个索引名称

# 在父组件模板中,子组件标签上使用 ref 指定一个名称,
# 井在父组件内通过 this.$refs 来访问指定名称的子组件


# 12 使用slot分发内容

# 当需要让组件组合使用,混合父组件的内容与子组件的模板时,
# 就会用到slot,这个过程叫内容分发

# pros传递数据,events触发事件和slot内容分发就构成了Vue
# 组件的3个API来源


# slot作用域

# 父组件模板内容是在父组件作用域内编译,子组件模板的内容是在
# 子组件作用域内编译

# slot用法

# 单个slot,开启一个slot插槽

# <div id="app">
# 	<child-c>
# 		<p>分发内容</p>
# 		<p>更多分发内容</p>
# 	</child-c>
# </div>

# Vue.component('child-c',{
# 	template:'\
# 		<div>\
# 			<slot>\
# 				<p>如果父组件没有插入内容,我将作为默认出现</p>\
# 			</slot>\
# 		</div>'
# })

# var app = new Vue({
# 	el: '#app'
# })

# 具名Slot

# 给<slot>元素制定一个name后可以分发多个内容>

# 作用域插槽

# 作用域插槽是一种特殊的slot,使用一个可以复用的模板替换已
# 渲染的元素

# 访问slot

# $slots 访问被slot分发的内容方法


# 13 Render函数

# Virtual Dom

# Virtual Dom 并不是真正意义上的 DOM ,而是一个轻
# 量级 的 JavaScript 对象,在状态发生变化时,
# Virtual Dom 会进行 Diff 运算,来更新只需要被替
# 换的 DOM ,而不是全部重绘。

# 与 DOM 操作相比, Virtual Dom 是基于 JavaScript
# 计算的,所以开销会小很多

# 14 使用钩子函数

# 实例声明周期钩子(created及其他)

# 代码执行的不同阶段处

# created
# 实例被创建之后执行的代码
# 	new Vue({
# 	data:{
# 		a:1
# 	},
# 	created:function(){
# 		console.log(this.a)
# 	}
# })
1
# =======================================================



# ===============================================
# VueRuter
1
# 1 实现原理

# 	利用window.onhashchange

# 		<div id="app">

# 		</div>


# 		let oDiv = document.getElementById("app")

# 		window.onhashchange = function(){
# 			switch(location.hash){
# 		case '#/login':
# 			oDiv.innerHTML = `<h1>这是登录页面</h1>`;
# 			console.log(location.hash);
# 			break;
# 		case '#/register':
# 			oDiv.innerHTML = `<h1>这是注册页面</h1>`;
# 			console.log(location.hash);
# 			break;
# 		default:
# 			oDiv.innerHTML = `<h1>这是首页</h1>`;
# 			console.log(location.hash);
# 			break;
# 	}
# }

# 2 安装使用

# 	安装
# 		1 下载
# 		2 script引入(前提条件引入vue.js)

# 	使用

# 		1 在vue根实例中使用,VueRouter

# 			Vue.use(VueRouter)

# 		2 实例化一个router对象,编写绑定关系(本质上是将路径和页面内容绑定了对应关系)

# 			let router = VueRouter({
# 				routes:[
# 					{
# 						path:'/',
# 						component:Home,
# 					},
# 				]
# 			})

# 		3 在根实例中注册router对象

# 			new Vue({

# 				el:"app",
# 				router: router,
# 			})

# 		4 编写页面内容
# 			let Home = {
# 				template:`
# 					<div>这是Home</div>
# 				`
# 			}

# 		5 创建根组件,使用根组件渲染


# 			#
# 			let App = {
# 				template:`
# 					<div>
# 						# 内容会渲染成 a标签 to会渲染成href to后面是router中定义的路径
# 						<router-link to="/">首页</router-link>

# 						# 是页面内容的渲染出口
# 						<router-view></router-view>
# 					</div>
# 					`

# 			}

# 		6 在根实例中 注册根组件
# 			new Vue({
# 				el:"#app",
# 				template:`<App></App>`,
# 				router: router,
# 				components:{
# 					App,
# 				}
# 			})

# 3 命名路由

# 	1 命名路由
# 	let router = VueRouter({
# 				routes:[
# 					{
# 						name:'home',
# 						path:'/',
# 						component:Home,
# 					},
# 				]
# 			})
# 	2 使用命名路由

# 		let App = {
# 			template:`
# 				<div>
# 					# 注意对to进行了绑定
# 					<router-link :to="{ name:'home' }">首页</router-link>

# 					<router-view></router-view>
# 				</div>
# 				`
# 		}


# 4 路由参数

# 	两种路由参数形式

# 		1   xxx/111  关键字 params

# 			1 <router-link :to="{ name:'user',params:{userId:1} }"></router-link>

# 			2 {
# 			name:'user',
# 			path:'/user/:userId',
# 			component:User,
# 				},

# 		2	xxx/?userId=1   关键字 query

# 			1 <router-link :to="{ name:'user1',query:{userId:2} }"></router-link>

# 			2{
# 			name:'user1',
# 			path:'/user',
# 			component:User1,
# 				},

# 5 路由参数的实现原理

# 	路由相关信息组件挂载之后都会自动放在 对象 $route 中,通关 $route 找到参数 然后自动拼接起来

# 6 子路由(嵌套路由)

# 	子路由也是组件

# 	1 创建父路由对象,子路由对像

# 		let Father = {
# 		template:`
# 			<div>
# 				<h1> 这是父路由 </h1>
# 			</div>
# 		`
# 		};


# 		let Children1 = {
# 		template:`
# 			<div>我是子路由1</div>

# 		`

# 	2 建立与父路由的关系

# 		{
# 			name:'father',
# 			path:'/father',
# 			component:Father,
# 			children:[
# 			{	name:'children1',
# 				path:'children1',
# 				component:Children1,
# 			},
# 			]
# 		};

# 	3 使用子路由

# 		let Father = {
# 		template:`
# 			<div>
# 				<router-link :to="{ name:'children1' }" append>子路由1</router-link>

# 				<router-view></router-view>
# 			</div>

# 		`
# 		};


# 8 路由重定向

# 		1 第一种方法

# 		{
# 			name:'red',
# 			path:'/red',
# 			redirect:'/',
# 			component:Red,
# 		},

# 		2 钩子函数

# 9 路由的钩子函数(beforeEach)

# 	路由重定向的第二种方法

# 		原理 向对象中添加标记 根据标记的值进行操作跳转

# 		通过router对象的beforeEach(function(to,from,next))
# 			参数: to 去哪  from 从哪来  next 自己指定下一步去哪

# 		{
# 			name:'beforeeach2',
# 			path:'/beforeeach2',
# 			meta:{required_login:true},
# 			component:Beforeeach2,
# 		},


# 		router.beforeEach(function(to, from,next){
# 			console.log(to)
# 			console.log(from)
# 			if(to.meta.required_login){
# 				next('beforeeach1');
# 			}else{
# 				next();
# 			}
# 		})

# 10 去掉url中的#号
# 	创建路由对象的时候 加入mode:'history'

# 		let router = new VueRouter({
# 			mode:'history',
# 			routes:[
1
# ===============================================



# =================================================
# node.js
1
# 0 安装（ubuntu）
#     sudo apt update -y
#     sudo apt install -y nodejs nodejs-legacy npm
#     sudo npm config set registry https://registry.npm.taobao.org
#     sudo npm install n -g
#     sudo n stable
#
#     n是一个Node工具包，它提供了几个升级命令参数
#         n                              显示已安装的Node版本
#         n latest                       安装最新版本Node
#         n stable                       安装最新稳定版Node
#         n lts                          安装最新长期维护版(lts)Node
#         n <version>                    根据提供的版本号安装Node
#
# ps:require 和 import 区别
#
#     1 require是amd规范引入方式
#       import是es6的一个语法标准
#     2 require是运行时调用
#       import是编译时调用
#
#
#
#
# 1 概念
#     1 什么是node.js
#         node.js 不是一门语言, 不是库,不是框架
#         node.js 是一个javaScript运行时环境，可以解析和执行JavaScript代码
#         以前只有浏览器可以解析执行javascript代码
#         现在javascript可以完全脱离浏览器来运行
#         构建于chrome的V8引擎之上
#             代码只有具有特定格式的字符串
#             引擎可以认识他，解析和执行
#             工人google chrome的v8引擎执行javascript最快
#
#     2 浏览器中的javaScript和node.js中的javaScript区别
#         1 浏览器中的javaScript
#             EcmaScript ：基本的语法 if var 。。。。
#             BOM
#             DOM
#         2 node.js中的javaScript
#             没有BOM,DOM
#             只有EcmaScript
#             提供了一些服务器级别的操作API
#                 文件读写
#                 网络服务构建
#                 网络通信
#                 http服务器等
#     3 node.js特性
#         事件驱动
#         非阻塞IO模型（异步）
#         轻量和高效
#     4 基于node.js开发的npm
#         npm是世界上最大的开源库生态系统
#         绝大多数javaScript相关的包都放在了npm上，好处
#         是让开发人方便下载和使用
#     5 Node的作用域
#         Node中没有全局的作用域，只有模块作用域
#         外部访问不到内部
#         内部访问不到外部
# 2 node.js能做的事情
#     web服务器后台，命令行工具（npm，hexo...）
#
#     B/S编程模型
#     模块化编程
#         可以引用加载js脚本文件
#     异步编程
#         回调函数
#         Promise
#         async
#         generator
#
# 3 node.js执行js脚本文件
#
#     1 在js文件中写代码
#     2 执行脚本文件
#         node 脚本文件名字
#
#     注意：文件名不要命名为node.js
#           因为没有BOM,和DOM，console.log(window),console.log(document)会报错
#
# 4 node.js读取文件
#     1 使用require方法加载fs核心模块
#         var fs = require('fs')
#     2 使用fs的readFile()方法读取文件
#         fs.readFile('文件路径', function(error, data){})
#
#             # 回调函数中的参数
#                 # 读取文件成功
#                 #    data 读出的数据
#                 #    error null
#                 # 读取文件失败
#                 #    data undefined没有数据
#                 #    error 错误对象
#     3 对读取到的文件内容进行转换（toString（））
#         readFile方法读取到的文件是16进制
#             data.toString()
#
# 5 node.js写文件
#     1 使用require方法加载fs核心模块
#         var fs = require('fs')
#     2 使用fs的writeFile()方法读取文件
#         fs.writeFile('文件路径', '写入文件内容',function(error){})
#
#             # 回调函数的参数
#             # 写入文件成功
#             #   error 是null
#             # 写入文件失败
#             #   error 是错误对象
#
# 6 使用node.js创建服器相关
#     1 加载http核心模块
#         var http = require('http')
#     2 使用http.createServer()方法创建一个Web服务器实例
#         var server = http.createServer()
#     3 接收请求，返回响应(当客户端发送请求，就会自动触发服务器的request请求事件，执行回调函数)
#         server.on('request', function(request, response){
#
#             # 获取客户端请求的请求路径
#                 request.url
#             # 返回响应两种方法
#                 1 # 返回响应，注意结束响应end
#                     1 response.write('返回内容')
#                     2 response.end()
#                 2 # 返回响应直接用end
#                     response.end('响应的内容')
#             # 返回响应必须是字符串或二进制
#                 转换成字符串
#                     JSON.stringify(xx)
#         })
#
#             # 回调函数的参数
#                 request请求对象
#                     获取客户端的一些请求信息
#                 response响应对象
#                     给客户端发送响应消息
#
#
#     4启动服务器,绑定端口号(当启动成功会执行函数)
#         server.listen(端口号， function(){
#             console.log('服务器启动成功')
#         })
#
#     马上用例子
#         1
#         var http = require('http');
#         var server = http.createServer();
#         server.on('request', function (req, rep) {
#             rep.end('我收到了您的信息')
#         });
#         server.listen(8000, function () {
#            console.log('服务器已经启动，等待客户连接')
#         });
#
#         2 简写
#             var http = require('http')
#             var fs = require('fs')
#             http.createServer(function(req, res){
#                 res.end('xxxxx')
#             })
#             .listen(8000, function(){
#                 console.log('running....')
#             })
#
#
#
#     5 处理响应中文乱码问题
#         1 乱码的原因
#             服务端默认发送utf8编码内容，但浏览器按照当前系统默认编码（windowsGBK）去解析
#             发送来的内容
#         2 解决方法
#             告诉浏览器用的编码格式是utf-8
#             res.setHeader('Content-Type', 'text/plain; charset=utf-8')
#
#     6 处理响应发送文本文件（html，text，jpg等）
#         1解决原理
#             读取文本中内容发送
#         2 解决方法1
#             fs.readFile('xx', function(err, data){
#                 if(err){
#                     res.setHeader('Content-Type', 'text/plain;charset=utf8')
#                     res.end('查找内容不存在')
#                     }else{
#                         res.setHeader('Content-Type', 'text/html;charset=utf8')
#                         res.end(data)
#                     }
#             })
#         3 解决方法2
#             html 文件中 用meta标签生命编码格式，浏览器也会识别
#
#     7 node.js匹配路径
#
#         if (req.url !== '/') {
#         console.log(req.url)
#     }
#
#     8 node.js处理静态资源
#     为了统一管理静态资源，把静态资源都放在public目录中
#     判断路径是否已public开头
#         if (url.indexOf('/public/') === 0) {xxxx}
#
#     9 node.js get请求获取提交内容
#         var url = require('url')
#
#         var obj = url.parse('路径+get提交的参数' ,true) # 将路径解析为一个方便操作的对象，true便是直接查询字符串转为一个对象
#
#         obj.pathname # 可获取不包含查询字符串的路径部分
#
#         obj.query # 获取提交保单内容的对象
#
#     10 node.js 服务器让客户端重定向
#         1 状态码设置为302 临时重定向
#             res.statusCode = 302
#         2 响应头中通过Location告诉客户端往哪重定向
#             res.setHeader('Location', '/跳转的url')
#
#
# 7 node.js的核心模块
#     1 概念
#         Node为javaScript提供了服务器级别的API，这些API都被包装到了一个具名的核心模块中
#     2 种类
#         1 文件操作
#             fs
#                 fs.readdir   获取文件目录列表
#                 fs.readFile  读取文件
#                 fs.writeFile 写入文件
#         2 服务器构建
#             http
#         3 路径操作
#             path
#         4 操作系统
#             os
#         5 ........
#     3 核心模块的加载
#         var xx = require('核心模块名')
#
#
# 8 node.js的模块化（文件的导入）
#
#     1 导入另一个文件
#         require('另一个文件的路径')  # 可以省略文件后缀名
#
#     2 Node的作用域（默认导入一个模块不能使用模块中的内容）
#         Node中没有全局的作用域，只有模块作用域
#         外部访问不到内部
#         内部访问不到外部
#         默认都是封闭的
#     3 模块中的通信（使用导入模块中的内容）
#         1 概念
#             require 方法的两个作用
#                 1 加载文件模块并执行里面的代码
#                 2 拿到被加载文件模块导出的接口对象 exports
#                     （node在每个文件模块中提供了一个对象：exports）
#
#         2 通信原理
#             把所有需要被外部访问的成员挂载到exports的对象成员中
#
#         3 例子
#             a.js文件
#                 exports.a = 111;
#                 exports.b = 222;
#             b.js文件
#                 res = require('./a.js'); # res就是通过require方法得到b文件中的exports
#                 res.a   # 就是b文件中的111
#                 res.b   # 就是b文件中的222
#
#
# 9 node中的模板引擎
#
#     js模板引擎art-template
#
#     1 安装
#         npm install art-template --save
#     2 在node中的中使用模板引擎
#         1 加载art-template
#             var template = require('art-template')
#     3 渲染模板
#         1 template.render('模板字符串', 替换对象)
#             例子
#                 var ret = template('aaaa {{ name }}', {
#                     name: 'zhengyu'
#                 })
#
# 10 node.js的模块系统
#     1 概念
#         1 模块化
#             1 文件作用域
#             2 通信规则
#                 1加载
#                 2到处
#         2 CommonJS模块规范
#             在node中的JavaScript的模块系统
#                 1 模块作用域
#                 2 使用require方法用来加载模块
#                 3 使用exports接口对象用来到处模块中的成员
#
#         3 require加载
#
#             1 var xx = require('模块名称')
#
#                 作用
#                     1 执行被加载模块的代码
#                     2 得到被加载模块中的exports导出接口对象
#
#             2 require方法加载规则
#
#                 1 优先从缓存加载
#                 2 判断模块标识
#                     核心模块（fs， http等）
#                     第三方模块（node_modules）
#                         1 既不是核心模块， 也不是路径形式的模块
#                         2 先找到当前文件所处目录中的 node_modules目录
#                         3 如果有再去找该node_modules/xxx/package.json文件
#                         4 再去找package.json的main属性
#                         5 main属性中记录了xxx的入口模块
#                         6 然后加载使用这个入口模块文件
#
#                         如果package.json不存在，或main指定的入口模块也没有，则会默认加载
#                         xxx文件下的index.js文件
#
#                         如果以上条件都不成立，会跳转到上一级目录node_modules中查找，如果没有
#                         直到查找该脚本的根目录，就会报错：找不到
#
#                 3 自己写的模块
#
#
#
#         4 exports导出
#             1 概念
#                 Node中是模块作用域，默认文件中所有的成员只在当前文件模块有效
#                 exports可以被其他模块访问成员，只需要把这些公开的成员都挂载到exports接口对象中
#
#                 1 导出多个成员（必须在对象中）
#                     exports.a = 123
#                     exports.b = function(){xxx}
#                     或
#                     module.exports = {
#                         a="1", b="2"
#                     }
#
#
#                 2 导出单个成员（拿到的是函数或字符串）
#                     module.exports = 'hello'
#
#
#             2 原理
#                 在node中，每个模块内部都有一个自己的module对象
#                 在module中有一个成员叫exports ,也是一个对象，是空对象
#                 默认在代码最后一句 return module.exports
#                 还有依据代码  var exports = module.exports # 为了导出成员方便，所以exports.a也可以导出对象
#                 谁来require，谁就得到module.exports对象，既底层代码：
#
#                     var module = {
#                         exports:{
#
#                         }
#                     }
#
#                     return module.exports
#
#
#
# 11 node.js的npm
#
#     1 概念
#         全称 node package manager
#
#         网站 包的存储网站
#
#     2 npm的 --save
#
#         安装包时候
#             1 加上 --save
#                 package.json 中 dependencies属性中会有安装包的记载
#             2 不加 --save
#                 package.json 中 dependencies属性中不会有安装包的记载
#         安装包的时候 如果加上--
#
#     3 常用命令
#
#
#         1 npm install
#
#             自动安装package.json中 的dependencies 的所有依赖的包
#
#         2 npm --version
#
#             查看npm版本
#
#         3 npm install --global npm
#
#             升级npm的版本
#
#         4 npm init
#
#             生成package.json文件
#
#         5 npm init -y
#
#             跳过向导 快速生成package.json文件
#
#         7 npm install 包名
#
#             安装包 并且package.json 中 dependencies属性中不会有安装包的记载
#
#         8 npm install --save 包名 （npm5.1版本之后自动添加依赖项，不加--save也可）
#
#             安装包 并且package.json 中 dependencies属性中会有安装包的记载
#
#         9 npm uninstall 包名
#
#             删除包 如果package.json 中 dependencies有记载 依然会存在
#
#         10 npm uninstall --save 包名
#
#             删除包 如果package.json 中 dependencies有记载 会被删除
#
#         11 npm help
#
#             查看使用帮助
#
#         12 npm 命令 --help
#
#             查看指定命令的使用帮助
#
#     4 解决npm被墙问题
#
#         第一种方式
#
#             1 安装cnpm
#
#                 npm install --global cnpm
#
#                 然后以后安装包 都使用cnpm install 包名， 走的是淘宝的源
#
#             2 配置 执行npm命令获取源变为淘宝的源
#
#                 npm config set registry https://registry.npm.taobao.org
#
#                 检验是否配置成功
#
#                     npm config list 查看是否有配置的地址
#
# 12 node.js的package.json
#
#     1 概念
#         可理解为当前项目包的说明说
#     2 创建
#         npm init
#
#
# 12.1 node.js的package-lock.js
#
#     1 作用
#         1 存放包的所有以来信息
#         2 执行npm install 的速度可以提升
#         3 锁定版本
#
#
#
#
#
# 13 node.js的Express
#
#     1 概念
#
#         框架 提高开发效率，让代码高度统一
#
#     2 安装
#
#         1 生成package.json
#             npm init
#         2 npm install express --save
#
#     3 引包
#
#         1 创建一个js文件
#         2 在js文件中引包
#             var express = require('express')
#
#     4 基本使用
#         //1 创建服务器应用程序
#             var app = express()
#
#         //2 接受get请求返回 (路由)
#             app.get('/', function(req, res){
#                 res.send('hhhhh')
#             })
#         //3 启动服务器
#             app.listen(8000, function(){
#                 console.log('server running at 8000.....')
#             })
#
#     5 处理公开目录
#         第一种写法（请求的url为:127.0.0.1：8000/public/xxx）(推荐)
#             app.use('/public/', express.static('./public/'))
#         第二种写法（请求的url为：127.0.0.1：8000/xxx）
#             app.use(express.static('./public/'))
#         第三种写法（请求的url为：127.0.0.1:8000/aaa/xxx）
#             app.use('/aaa/', express.static('./public/'))
#
#     6 修改完代码让服务器自动重启
#
#         1 使用第三方工具 nodemon
#
#             1 npm install --global nodemon
#         2 使用
#
#             nodemon 文件
#
#     7 配置atr-template模板引擎
#
#         1 安装
#
#             npm install --save art-template
#             npm install --save express-art-template
#
#         2 配置
#
#             app.engine('html', require('express-art-template'))
#
#                 参数解析，当渲染以.html结尾的文件的时候，使用art-template模板引擎
#
#         3 使用
#
#             res.render('views目录中的模板名',{模板数据})
#
#                 参数解析 第一个参数不能写路径，默认会去项目中views目录中查找
#
#             (可选)改变默认模板路径views
#
#                 如果想改变默认views的模板路径
#
#                     app.set('views', '路径')
#
#     8 get和post获取请求数据
#
#         1 get请求
#
#             req.query  # 只能拿get请求参数
#
#         2 post请求
#
#             1 安装插件
#
#                 npm install --save body-parser
#             2 配置
#
#                 1 引包
#
#                     var bodyParser = require('body-parser')
#
#                 2 配置
#
#                     app.use(bodyParser.urlencoded({extended：false}))
#                     app.use(bodyParser.json())
#
#             3 获取post数据
#
#                 req.body
#
#     9 提取路由为模块
#         第一种方法
#             1 创建文件 router.js
#
#             2 router.js下写路由
#
#             3 router.js下 把所有路由导出(传入参数app)
#
#                 module.exports = function(app){
#
#                     路由...
#                 }
#
#             4 app.js文件中， 导入router 执行router方法
#
#                 var router = require('./router')
#
#                 router(app)
#
#         第二种方法（推荐）
#
#             1 创建 router.js 文件
#
#             2 导入 express
#
#                 var express = require('express')
#
#             3 创建路由容器
#
#                 var router = express.Router()
#
#             4 写路由
#
#                 router.get(......)
#
#             5 导出router
#
#                 module.exports = router
#
#             6 app.js文件中，导入router模块
#
#                 var router = require('./router')
#
#             7 app.js文件中，把路由容器挂载到app服务中
#
#                 app.use(router)
#
#             注意： app文件中 配置模板引擎，boy-parser一定要在挂载路由之前
#
#
# 14 node.js中操作mongodb数据库
#
#     第一种方式
#
#         官方提供的方式（一般不用）
#
#     第二种方式, 使用第三方工具mongoose来操作
#
#         1 安装
#             npm i mongoose --save
#
#         2 基本使用
#
#             1 创建js文件
#             2 js文件中
#
#                 1 引包
#
#                     const mongoose = require('mongoose');
#
#                 2 连接 mongodb数据库
#
#                     mongoose.connect('mongodb://localhost:27017/test', {useNewUrlParser: true});
#
#                 3 设计表结构（mongoose.model('表名', { 字段名: 字段类型 });）
#
#                     const Cat = mongoose.model('Cat', { name: String });
#
#                 4 实例化表，插入数据
#                     const kitty = new Cat({ name: 'Zildjian' });
#
#                 5 保存操作
#
#                     kitty.save().then(() => console.log('meow'));
#
#         3 扩展
#
#             1 设计表结构
#
#                 1 实例化Schema
#
#                     var Schema = mongoose.Schema
#
#                 2 设计表结构
#                     var xx = new Schema({
#
#                         a:String,
#                         b:[{c:String, d:Date}]
#                         e:Boolean
#                         f:{g:Number, h:Number}
#
#                     });
#
#                 3 将表结构发布为模型
#
#                     参数解释mongoose.model('第一个字母大写的数据库名称（到数据库中会变成小谢复数名称）', xx)
#
#                         var yy = mongoose.model('yy', xx)  # 返回模型构造函数
#
#                 4 使用构造函数yy
#
#                     1 插入数据
#
#                         var ss = new yy({
#
#                             a:'123',
#                             b:'qqq',
#                             ...
#
#                         })
#
#                         保存操作
#
#                             ss.save(function(err, ret){         #ret为插入的数据
#                                 if(err){
#                                     console.log('存储失败')
#                                 }else{
#                                     console.log('存储成功')
#                                 }
#                             })
#
#                     2 查询数据
#
#                         1 查询所有数据
#
#                             yy.find(function(err, ret){
#                                 if (err){
#                                     console.log('查询失败')
#                                 }else{
#                                     console.log(ret)   # 返回的ret是数组
#                                 }
#
#                             })
#
#                         2 条件查询
#
#                             1 根据字段查询
#                                 yy.find({字段:'a'}, function(err, ret){
#                                     if (err){
#                                         console.log('查询失败')
#                                     }else{
#                                         console.log(ret)   # 返回的ret是数组
#                                     }
#
#                                 })
#
#                         3 只找到匹配的第一个
#
#                             yy.findOne({})
#
#
#                     3 删除数据
#
#                         1 根据字段删除数据
#
#                             yy.remove({字段:'a'}, function(err, ret){
#                                         if (err){
#                                             console.log('删除失败')
#                                         }else{
#                                             console.log(ret)   # 返回的ret删除信息
#                                         }
#
#                                     })
#
#                         2 根据字段删除一个数据
#
#                             yy.findOneAndRemove(...)
#
#                         3 根据id删除一个数据
#
#                             yy.findByIdAndRemove(id, ...)
#
#
#                     4 更新数据
#
#                         1 根据id号，更改字段
#
#                             yy.findByIdAndUpdate('id号上数据库中查找',{'a':222}, function(err, ret){
#                                 ....
#                             })
#
#                         2 根据条件更新所有
#
#                             yy.update(....)
#
#                         3 根据条件更新一个
#
#                             yy.update(....)
#
#
#
#             2 字段的约束
#
#                 var xx = new Schema({
#
#                     a:{
#                         b:String;
#                         required: true // 必须有
#                     },
#
#
#                 })
#
#
# 15 node.js操作 mysql数据库
#
#     1 安装
#
#         npm -i mysql --save
#
#     1 使用
#
#         1 导入包
#             var mysql      = require('mysql');
#
#         2 创建连接
#             var connection = mysql.createConnection({
#               host     : 'localhost',
#               user     : 'me',
#               password : 'secret',
#               database : 'my_db'
#             });
#
#         3 连接数据库
#             connection.connect();
#
#         4 执行数据库操作
#             connection.query('sql语句', function (error, results, fields) {
#               if (error) throw error;
#               console.log('The solution is: ', results[0].solution);
#             });
#
#         5 关闭数据库
#             connection.end();
#
#
# 16 node.js 的 Promise
#
#     1 概念
#
#         Es6中的新增API，一个构造函数,promise本身不是异步
#         因为是异步无法保证顺序，使用Promise可以保证指定顺序
#         promise 是一个容器，存放了一个异步任务，有三种状态默认是pending，resolved(成功),rejected（失败）
#
#
#     2 问题 ：（读取3个文件使用异步函数fs.readFile, 使读取顺序从上到下）
#
#     3 解决问题
#
#         解决原理 回调嵌套
#
#             1 创建promise容器实例 (创建了3个异步函数readFile)
#
#                 var p1 = new Promise(function(resolve, reject){
#
#                     fs.readFile('a.txt', function(err, data){
#                         if(err){
#
#                             reject(err) # 把容器的Pending状态 变为Rejected状态
#                         }else{
#
#
#                             resolve(data) # 把容器的pending状态改为成功
#                         }
#                     })
#                 })
#
#                 var p2 = new Promise(function(resolve, reject){
#
#                     fs.readFile('b.txt', function(err, data){
#                         if(err){
#
#                             reject(err) # 把容器的Pending状态 变为Rejected状态
#                         }else{
#
#
#                             resolve(data) # 把容器的pending状态改为成功
#                         }
#                     })
#                 })
#                 var p3 = new Promise(function(resolve, reject){
#
#                     fs.readFile('c.txt', function(err, data){
#                         if(err){
#
#                             reject(err) # 把容器的Pending状态 变为Rejected状态
#                         }else{
#
#
#                             resolve(data) # 把容器的pending状态改为成功
#                         }
#                     })
#                 })
#
#             2 判断pending的状态 进行操作
#
#                1 如果成功了
#                     // then方法接收两个函数
#                     //        第一个的function就是容器中的resolve函数
#                     //        第二个的function就是容器中的reject函数
#                     p1.then(function(data){
#
#                         return p2  # 这里return的结果在后面的then中function接收到
#
#                     }, function(err){
#                         ...
#                     })
#                     .then(function(data){
#
#                         return p3
#                     }).
#                     then(function(data){
#
#                         console.log(data)
#                     })
#
#
# 17 node.js的核心模块path
#
#     1 作用
#         操作路径的模块
#
#     2 使用
#
#         0 导入模块
#
#             var path = require('path')
#
#         1 只得到路径下的文件名(包括文件后缀)
#
#             path.basename('路径')
#
#         2 只得到路径下的文件名(不包括文件后缀)
#
#             path.basename('路径', ‘.后缀名’)
#
#         3 只获取路径部分（不包括文件）
#
#             path.dirname('路径')
#
#         4 获取文件扩展名
#
#             path.extname(’路径‘)
#
#         5 判断路径是否是绝对路径
#
#             path.isAbsolute('路径')
#
#         6 得到路径的对象，对象中有 根目录，路径，路径下文件,文件后缀名,文件名（不带后缀名）
#
#             path.parse('路径')
#
#         7 路径的拼接
#
#             path.join('c:/a', 'b')
#         8 将当前参数（目录或文件）解析成绝对路径
#
#             path.resolve('xx')
#
# 18 node.js中的非模块成员
#
#     1 __dirname
#
#         获取当前文件所属目录的绝对路径(不包括文件)
#
#     2 __filename
#
#         可以用来获取当前文件的绝对路径(包括文件)
#
#     注意
#
#         文件操作路径中，相对路径设计的就是相对于执行node命令所处的路径
1
# =================================================



# =================================================
# vuexvuex
1
# vuex 与v-model的双向绑定
#
#     template=`<span>{{ username }}</span><input type="text" v-model="username">`
#     # vue
#     computed:{
#       username:{
#           get(){
#
#               return this.$store.state.head.username
#           },
#           set(value){
#               console.log(value);
#               this.$store.commit("update_username", value)
#           }
#       }
#
#       # vuex
#       mutations: {
#         update_username:function (state, payload) {
#             state.head.username = payload
#         },
#
#       # state
#       state: {
#         flag_num:1,
#
#         head:{
#             username:'',
#         }
# vuex中给对象添加或更改属性
#
#     Vue.set(obj, key, value);
#
#     return obj   # 为了浏览前相应
#
#
#
#
#
# 	状态管理 用来管理全局数
#
# 	安装
#
# 		下载源码 引入文件
#
# 	使用
# 			Vue.use(Vuex);  		# 1 使用Vuex
#
# 			const myStore = new  	# 2 创建 store对象
# 			Vuex.Store({
# 				state: { 				# 用来存放组件之间共享的数据
# 					name: "Alex",
# 				},
# 				mutations: {}, 		# 修改数据对象mutations
# 				getters: {}, 		# 处理过滤数据getters
# 				actions: {} 		# 带有上下文的修改原数据
# 			});
#
# 			let App = {
# 				template: `
# 					<div>
# 						<p> {{name}} </p>
# 				  	< / div >
# 					  `,
# 				computed: {
# 					name: function() {
# 						return this.$store.state.name;
# 						},
# 				}
# 			};
#
# 			new Vue({
# 				el: "#app",
# 				store: myStore, 					# 3 将store对象注册到vue根实例
# 				template: ` <app> </app> `,
# 				components: {
# 					'app': App,
# 				},
# 			})
#
#             总结：基本使用
#                 Vue.use(Vuex);
#
#                 const myStore = new Vuex.Store({
#                     state: {
#                         name: "Alex",
#                     },
#                     mutations: {},
#                     getters: {},
#                     actions: {}
#                 });
#
#                 let App = {
#                     template: `
#                         <div>
#                             <p> {{name}} </p>
#                         </div>
#                           `,
#                     computed: {
#                         name: function() {
#                             return this.$store.state.name;
#                             },
#                     }
#                 };
#
#                 new Vue({
#                     el: "#app",
#                     store: myStore,
#                     template: `<app></app>`,
#                     components: {
#                         'app': App,
#                     },
#                 })
#
#
#
#
#
# 		4 操作数据
#
# 			getters 和 mutations
#
# 				getters 不修改原数据
# 				mutations 修改原数据 ,需要通过事件修改
#
# 			2.1 通过计算属性访问数据 state $store
#
# 					let App = {
# 					template:`
# 						<div>
# 							<h1>{{ name }}</h1>
# 						</div>
# 					`,
# 					computed:{
# 						name:function(){
# 							return this.$store.state.name;
# 						}
# 					}
# 				}
#
# 			2.2 过滤数据(不改变原数据) getters
#
# 				Vue.use(Vuex);
#
# 				const store = new
# 				Vuex.Store({
# 						state: {
# 							age: 22,
# 					},
# 				getters: {
# 					getAge: function(state){
# 						return state.age + 20;
# 						}
# 					}
# 				});
#
# 				let App = {
# 					template: `
# 						< div >
# 							< span > {{age}} < / span >
# 					  	< / div >
# 						  `,
# 						  computed: {
# 								age: function() {
# 									return this.$store.getters.getAge;
# 								}
# 							},
# 						};
#
# 				new Vue({
# 					el: "#app",
# 					template: ` < App > < / App > `,
# 					store: store,
# 					components: {
# 						App
# 					}
# 				});
#
# 			2.3 修改数据(改变原数据,需要事件触发)
# 				Vue.use(Vuex);
# 				const store = new
# 				Vuex.Store({
# 					state: {
# 						age: 22,
# 						},
# 				mutations: {
# 					changeage: function(state, payload){
# 						return state.age -= payload
# 						}
# 				}
# 				});
# 				let App = {
# 				  template: `
# 						< div >
# 							< span > {{age}} < / span >
# 							< button @ click = "change" > 点击 + 1 < / button >
# 						< / div >
# 														   `,
# 				  computed: {
# 						age: function() {
# 							return this.$store.state.age;
# 							}
# 					},
# 				  methods: {
# 					change: function() {
# 						this.$store.commit('changeage', 1)
# 						}
# 					}
# 					};
#
# 				new Vue({
# 						el: "#app",
# 						template: ` < App > < / App > `,
# 						store: store,
# 						components: {
# 							App
# 							}
# 					});
#
# 			2.4 actions(带有上下文的修改原数据,带有异步的也就是说可以利用settimeout5秒之后进行修改)
# 					let App = {
# 						template:`
# 							<div>
#
# 								<h1>{{ score }}</h1>
# 								<button @click="addscore">点击增加分数</button>
# 							</div>
# 						`,
# 						computed:{
#
# 							score:function(){
# 								return this.$store.state.score;
# 							},
# 						},
# 						methods:{
#
# 							addscore:function(){
# 								this.$store.dispatch("addscore", 1) # 提交给actions中的函数
# 							}
# 						}
#
# 					}
#
#
1
# =================================================



# =================================================
# AxiosAxios
1
# 作用：
#     前后端交互工具
#
# 安装：
#     方式一
#         npm install axios
#
#     方式二
#         <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
#
# 定义
#
#     一个类库，居于PROMISE管理AJAX库
#         1 提供了对应请求方式的方法（get/post/head/delete/put/options）
#             axios.get() 向服务器发送一个请求，基于的是GET方式
#         2 支持的参数配置
#             axios.get([url], [options])
#
#         3 基于GET或者POST方法请求，返回的结构都是PROMISE实例
#         4 语法例子
#         axios.get('xxxxxxx.com/xx/x/', {
#             params:{             GET请求中，会把PARAMS中的键值对拼接成URLENCODE格式的字符串
#                                     然后以问好传递参数的方式，传递给服务器，类似于jquery中的data（
#                                     或者自己基于URL后面拼接也可以，不用PARAMS）
#             }
#         })
#
#         axios.post('xxxxxxx.com/xx/x/', {
#             params:{             传递的内容都详单与请求主体传递给服务器，但是传递给服务器的内容
#                                     格式是RAW(JSON格式的子字符串)，不是X-WWW-FORM-URLENCODED
#             }
#         })
#
#         5 实例
#             axios.get('/user?ID=12345')
#                   .then(function (response) {
#                     console.log(response);
#                   })
#                   .catch(function (error) {
#                     console.log(error);
#                   });
#
#
#                 result对象的属性
#
#                     data: 从服务器获取的相应主体内容
#                     headers： 从服务器获取的响应头信息
#                     request: 创建AJAX实例
#                     status:状态码
#                     statusText: 状态码描述
#                     config：基于AXIOS发送请求的时候做的配置项
#
# axios一次性并发多个请求
#
#     let = sendAry = [
#         axios.get('XXXXXX'),    # 请求1
#         axios.get('yyyy'),      # 请求2
#     ];
#     axios.all(sendAry.then(result =>{
#
#         console.log(result)   # result现在是一个数组
#     }))
#
#
# axios中的设置配置项
#
#     1 设置公用配置项用
#         axios.defaults.xxxxx
#         axios.defaults.timeout = 3000;
#
#
#     2 配置项
#         params = ｛name:"zzzz"｝， 参数
#         headers: {xxx:'xxxxx'}   请求头
#         url：'xxx',
#         method: 'get',  默认
#         baseURL: 'yyy' 基础地址如‘http://127.0.0.1:8000’
#         responseType: 'json'  默认
#         vilidateStatus :function(status){  # 验证状态码
#
#             return /^(2|3)\d{2}$/.text(status)
#         }
#
#         # 设置在POST请求中基于请求主体向发服务器发送内容的格式，默认是RAM，项目
#             # 中常用的是URL-ENCODEED格式
#         headers.post['Content-Type'] ='application/x-ww-form-urlencoded'
#
# 配置响应拦截器即（中间件）
#
#
#     axios.interceptors.response.use(); 增加响应拦截器
#     例子
#         # 分别在响应成功和失败的时候做一些拦截处理
#         axios.interceptors.response.use(funxtion success(result){
#             console.log(result)
#         }),function error(result){
#             console.log(result)
#         }
#
# axios获取服务器返回值
#
#     axios.get('http://127.0.0.1:8000/put_database?ARGS=delete_database')
#               .then(function (response) {
#                   let {data} = response;
#
#                   console.log({data}.data.键名);
#
#
#               })
1
# =================================================


# =========================================================
# lessless
1
#     1 概念
#
#         预处理语言
#         变量 延迟加载
#             一个作用域中的代码都执行完毕之后才会进行变量加载
#
#     2 注释
#
#         //    # 不会编译到css文件中
#         /**/  # 会被编译到css文件中
#
#     3 变量
#
#         1 @变量名: 值
#
#         2 属性名
#
#             @m:margin
#
#             调用
#                 @{m}:0
#
#         2 选择器
#
#             @selector: #aa
#
#             调用
#
#                 @{selector}{...}
#
#
#     4 嵌套规则
#
#         1 父与子
#
#             <div class="father">
#                 <div class="son">
#
#
#                 </div>
#             </div>
#
#             less写法
#
#                 #father{
#                     ....
#                     .son{
#                         ....
#                     }
#                 }
#         2 &的用法
#
#             成为同等级
#
#
#     5 less中混合
#
#         1 普通混合（定义的混合，会输出到css文件中，）bu
#
#             1 作用
#
#                 代码的重用
#
#             2 使用
#                 .变量名{
#                     ....
#                 }
#
#                 # father{
#
#                     .son1{
#                         .变量名;
#                     }
#                     .son2{
#                         .变量名;
#                     }
#                 }
#
#         2 不输出混合（定义的混合，不会输出在css文件中,混合后加括号）
#
#             1 作用
#
#                 代码的重用
#
#             2 使用
#                 .变量名(){
#                     ....
#                 }
#
#                 # father{
#
#                     .son1{
#                         .变量名;
#                     }
#                     .son2{
#                         .变量名;
#                     }
#                 }
#
#         3 带参数的混合（类是函数）
#
#             1 作用
#
#                 代码重用可传参数
#
#             2 使用
#
#                 .变量名(@a, @b){
#
#                     width:@a;
#                     height:@b;
#
#                 }
#
#                 # father{
#
#                     .son1{
#                         .变量名(100, 50);
#                     }
#                     .son2{
#                         .变量名(200, 100);
#                     }
#                 }
#
#         4 带有默认值的混合
#
#             1 作用
#
#                 代码重用可传参数,可使用默认值
#
#             2 使用
#
#                 .变量名(@a:100px, @b){
#
#                     width:@a;
#                     height:@b;
#
#                 }
#
#                 # father{
#
#                     .son1{
#                         .变量名(50);
#                     }
#                     .son2{
#                         .变量名(200, 100);
#                     }
#                 }
#
#         5 命名传参数混合
#
#             1 作用
#
#                 代码重用指定参数传参
#
#             2 使用
#
#                 .变量名(@a:100px, @b){
#
#                     width:@a;
#                     height:@b;
#
#                 }
#
#                 # father{
#
#                     .son1{
#                         .变量名(50px);
#                     }
#                     .son2{
#                         .变量名(@b:100px);
#                     }
#                 }
#
#         6 匹配模式
#
#             1 作用
#
#                 动态的调用，代码重用, 匹配相同代码,在选取不同代码,参数中带有标记参数，用来挑选不同的代码
#
#             2 使用
#
#                 .aa(@_){
#                     color:red;
#                 }
#
#                 .aa(Q, @c){
#
#                     border-color:red red red @c
#                 }
#                 .aa(R, @c){
#                     border-color:@c red red red
#                 }
#
#                 调用
#
#                     .aa(R)    就会选择混合中的R
#
#         8 arguments变量
#
#             1 作用
#
#                 形参的聚合
#
#             2 使用
#
#                 .aa(@a, @b, @c){
#                     border:@arguments;
#                 }
#
#                 调用
#
#                     #s{
#                         .aa(1px, solid, black)
#                     }
#
#         9 less运算
#
#             只需一方有1个单位既可
#
#             #a{
#
#                 width:(100+100px)
#             }
#
#
#         10 less继承
#
#             1 作用
#
#                 提取css相同的部分，为一个 #a{}
#
#
#             2 使用
#
#                 1 定义一个类（有公共代码）不能有参数
#
#                     .aa{
#                         提取的公共代码
#                     }
#
#                 2
#
#                 # father{
#                     ....
#                     .son{
#
#                         &:extend(.aa)
#                         ...
#                     }
#                 }
#
#                 3 其他语法
#
#                     1 将继承的类所有相关全部继承
#                         &:extend(.aa all)
#
#         11 less避免编译
#
#             1 作用
#
#                 不让less编译
#
#             2 使用
#
#                 ~"内容"
#
#         12 混合的模块化
#
#             1 作用
#
#                 可将混合写入单个文件，然后进行导入
#
#             2 导入
#
#                 @import "路径"
#
#         13 混合和类编译
#
#             混合 灵活
#             类 性能高
1
# =========================================================




# ==============================================
# jinja2jinja2
1
#
# jinja2模板中的 csrf_token
#     <input type ="hidden" name="csrfmiddlewaretoken" value={{csrf_token}}">
#     或
#     {{ csrf_input }}
#
# 模板渲染有个现成的工具： jinja2
#
#
#     import socket
#
#     from wsgiref.simple_server import make_server
#     from jinja2 import Template
#
#
#     def home():
#         s1 = "这是home页面".encode('utf-8')
#         return [s1,]
#
#
#     def index():
#         f = open("index.html","r")
#         s = f.read()
#         template = Template(s) # 生存模板文件
#         ret = template.render({"name":"zhengyu"}) # 把数据填充到模板里
#         f.close()
#         return [ret.encode("utf-8"),]
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
#         # print(environ)
#         # print(start_response)
#         func=None
#         for i in list1:
#             if i[0] == url:
#                 func = i[1]
#                 break
#         if func:
#             return func()
#         else:
#             return [b"fuck off",]
#
#
#
#     if __name__ == '__main__':
#         httpd = make_server("127.0.0.1", 10000, run_server)
#
#         print("111111111111111")
#         httpd.serve_forever()
#
# 常用语法
#     两种特殊符号
#     变量相关的用{{}}，
#     逻辑相关的用{%%}。
#
#     变量
#
#     {{ 变量名 }}
# 点（.）在模板语言中有特殊的含义。
#     当模版系统遇到点(".")，它将以这样的顺序查询：
#         字典查询（Dictionary lookup）
#         属性或方法查询（Attribute or method lookup）
#         数字索引查询（Numeric index lookup）
#
#
#     注意事项：
#     如果计算结果的值是可调用的，它将被无参数的调用。
#      调用的结果将成为模版的值。
#     如果使用的变量不存在，
#     模版系统将插入 string_if_invalid 选项的值，
#     它被默认设置为'' (空字符串) 。
#
#     例子
#     view中代码：
#     def template_test(request):
#         l = [11, 22, 33]
#         d = {"name": "alex"}
#
#         class Person(object):
#             def __init__(self, name, age):
#                 self.name = name
#                 self.age = age
#
#             def dream(self):
#                 return "{} is dream...".format(self.name)
#
#         Alex = Person(name="Alex", age=34)
#         Egon = Person(name="Egon", age=9000)
#         Eva_J = Person(name="Eva_J", age=18)
#
#         person_list = [Alex, Egon, Eva_J]
#         return render(request, "template_test.html", {"l": l, "d": d, "person_list": person_list})
#
#
#     模板中支持的写法
#     {# 取l中的第一个参数 #}
#     {{ l.0 }}
#     {# 取字典中key的值 #}
#     {{ d.name }}
#     {# 取对象的name属性 #}
#     {{ person_list.0.name }}
#     {# .操作只能调用不带参数的方法 #}
#     {{ person_list.0.dream }}
#
# Filters（过滤器）
#
#     在Django的模板语言中，通过使用 过滤器 来改变变量的显示。
#
#     过滤器的语法： {{ value|filter_name:参数 }}
#
#     使用管道符"|"来应用过滤器。
#
#     例如：{{ name|lower }}会将name变量应用lower过滤器之后再显示它的值。
#     lower在这里的作用是将文本全都变成小写。
#
#     注意事项：
#
#         1.过滤器支持“链式”操作。即一个过滤器的输出作为另一个过滤器的输入。
#         2.过滤器可以接受参数，例如：{{ sss|truncatewords:30 }}，
#             这将显示sss的前30个词。
#         3.过滤器参数包含空格的话，必须用引号包裹起来。
#             比如使用逗号和空格去连接一个列表中的元素，如：{{ list|join:', ' }}
#         4.'|'左右没有空格没有空格没有空格
#
# Django的模板语言中提供了大约六十个内置过滤器。
#
#     default
#     如果一个变量是false或者为空，使用给定的默认值。
#     否则，使用变量的值。
#     {{ value|default:"nothing"}}
#     如果value没有传值或者值为空的话就显示nothing
#
#
#
#     length
#     返回值的长度，作用于字符串和列表。
#     {{ value|length }}
#     返回value的长度，如 value=['a', 'b', 'c', 'd']的话，就显示4.
#
#
#
#     filesizeformat
#     将值格式化为一个 “人类可读的” 文件尺寸 （
#     例如 '13 KB', '4.1 MB', '102 bytes', 等等）
#     。例如：
#     {{ value|filesizeformat }}
#     如果 value 是 123456789，输出将会是 117.7 MB。
#
#
#
#     slice
#     切片
#     {{value|slice:"2:-1"}}
#
#     date
#     格式化
#     {{ value|date:"Y-m-d H:i:s"}}
#
#     格式化字符	描述	示例输出
#     a	'a.m.'或'p.m.'（请注意，这与PHP的输出略有不同，
#             因为这包括符合Associated Press风格的期间）	'a.m.'
#     A	'AM'或'PM'。	'AM'
#     b	月，文字，3个字母，小写。	'jan'
#     B	未实现。
#     c	ISO 8601格式。 （注意：与其他格式化程序不同，
#             例如“Z”，“O”或“r”，如果值为naive datetime，
#             则“c”格式化程序不会添加时区偏移量（请参阅datetime.tzinfo）
#             2008-01-02T10:30:00.000123+02:00或
#             2008-01-02T10:30:00.000123如果datetime是天真的
#     d	月的日子，带前导零的2位数字。	'01'到'31'
#     D	一周中的文字，3个字母。	“星期五”
#     e	时区名称 可能是任何格式，或者可能返回一个空字符串，
#             具体取决于datetime。	''、'GMT'、'-500'、'US/Eastern'等
#     E	月份，特定地区的替代表示通常用于长日期表示。
#         'listopada'（对于波兰语区域，而不是'Listopad'）
#     f	时间，在12小时的小时和分钟内，如果它们为零，则分钟停留。
#             专有扩展。	'1'，'1:30'
#     F	月，文，长。	'一月'
#     g	小时，12小时格式，无前导零。	'1'到'12'
#     G	小时，24小时格式，无前导零。	'0'到'23'
#     h	小时，12小时格式。	'01'到'12'
#     H	小时，24小时格式。	'00'到'23'
#     i	分钟。	'00'到'59'
#     I	夏令时间，无论是否生效。	'1'或'0'
#     j	没有前导零的月份的日子。	'1'到'31'
#     l	星期几，文字长。	'星期五'
#     L	布尔值是否是一个闰年。	True或False
#     m	月，2位数字带前导零。	'01'到'12'
#     M	月，文字，3个字母。	“扬”
#     n	月无前导零。	'1'到'12'
#     N	美联社风格的月份缩写。 专有扩展。
#             'Jan.'，'Feb.'，'March'，'May'
#     o	ISO-8601周编号，对应于使用闰年的ISO-8601周数（W）。
#             对于更常见的年份格式，请参见Y。	'1999年'
#     O	与格林威治时间的差异在几小时内。	'+0200'
#     P	时间为12小时，分钟和'a.m。'/'p.m。'，
#             如果为零，分钟停留，特殊情况下的字符串“午夜”和“中午”。
#             专有扩展。	'1 am'，'1:30 pm' / t3>，'midnight'，'noon'，'12：30 pm' / T10>
#     r	RFC 5322格式化日期。	'Thu, 21 Dec 2000 16:01:07 +0200'
#     s	秒，带前导零的2位数字。	'00'到'59'
#     S	一个月的英文序数后缀，2个字符。	'st'，'nd'，'rd'或'th'
#     t	给定月份的天数。	28 to 31
#     T	本机的时区。	'EST'，'MDT'
#     u	微秒。	000000 to 999999
#     U	自Unix Epoch以来的二分之一（1970年1月1日00:00:00 UTC）。
#     w	星期几，数字无前导零。	'0'（星期日）至'6'（星期六）
#     W	ISO-8601周数，周数从星期一开始。	1，53
#     y	年份，2位数字。	'99'
#     Y	年，4位数。	'1999年'
#     z	一年中的日子	0到365
#     Z	时区偏移量，单位为秒。 UTC以西时区的偏移量总是为负数，对于UTC以东时，它们总是为正。
#
#     safe
#
#         Django的模板中会对HTML标签和JS等语法标签进行自动转义，
#         原因显而易见，这样是为了安全
#
#         关闭HTML的自动转义
#         比如：
#         value = "<a href='#'>点我</a>"
#         {{ value|safe}}
#
#     truncatechars
#         如果字符串字符多于指定的字符数量，那么会被截断。
#         截断的字符串将以可翻译的省略号序列（“...”）结尾。
#
#         参数：截断的字符数
#
#         {{ value|truncatechars:9}}
#
#     cut
#         移除value中所有的与给出的变量相同的字符串
#
#         {{ value|cut:' ' }}
#         如果value为'i love you'，那么将输出'iloveyou'.
#
#     join
#         使用字符串连接列表，例如Python的str.join(list)
#
#     timesince
#         将日期格式设为自该日期起的时间（例如，“4天，6小时”）。
#
#         采用一个可选参数，它是一个包含用作比较点的日期的
#         变量（不带参数，比较点为现在）。 例如，
#         如果blog_date是表示2006年6月1日午夜的日期实例，
#         并且comment_date是2006年6月1日08:00的日期实例
#         ，则以下将返回“8小时”：
#
#         {{ blog_date|timesince:comment_date }}
#         分钟是所使用的最小单位，对于相对于比较
#
#     timeuntil
#         似于timesince，除了它测量从现在开始直到给定日期
#         或日期时间的时间。 例如，如果今天是2006年6月1日，
#         而conference_date是保留2006年6月29日的日期实例，
#         { conference_date | timeuntil }}将返回“4周”。
#
#         使用可选参数，它是一个包含用作比较点的日期（
#         而不是现在）的变量。
#         如果from_date包含2006年6月22日，
#         则以下内容将返回“1周”：
#
#         {{ conference_date|timeuntil:from_date }}
#
#     自定义filter
#
#         自定义过滤器只是带有一个或两个参数的Python函数:
#
#         变量（输入）的值 - -不一定是一个字符串
#         参数的值 - 这可以有一个默认值，或完全省略
#         例如，在过滤器{{var | foo:'bar'}}中，
#         过滤器foo将传递变量var和参数“bar”。
#
# Tags
#
#     for循环
#     普通for循环
#     <ul>
#     {% for user in user_list %}
#         <li>{{ user.name }}</li>
#     {% endfor %}
#     </ul>
#     for循环可用的一些参数：
#     Variable	Description
#     forloop.counter	当前循环的索引值（从1开始）
#     forloop.counter0	当前循环的索引值（从0开始）
#     forloop.revcounter	当前循环的倒序索引值（从1开始）
#     forloop.revcounter0	当前循环的倒序索引值（从0开始）
#     forloop.first	当前循环是不是第一次循环（布尔值）
#     forloop.last	当前循环是不是最后一次循环（布尔值）
#     forloop.parentloop	本层循环的外层循环
#
#
#     for ... empty
#     <ul>
#     {% for user in user_list %}
#         <li>{{ user.name }}</li>
#     {% empty %}
#         <li>空空如也</li>
#     {% endfor %}
#     </ul>
#
#             自定义filter代码文件摆放位置：
#             记得setting.py 文件中
#             INSTALLED_APPS = [
#                 "yingyong1.templatetags"
#             ]中注册
#             app01/
#                 __init__.py
#                 models.py
#                 templatetags/  # 在app01下面新建一个package package
#                     __init__.py
#                     app01_filters.py  # 建一个存放自定义filter的文件
#                 views.py
#
#
#
#
#             编写自定义filter
#             from django import template
#             register = template.Library()
#
#             @register.filter(name="cut")
#             def cut(value, arg):
#                 return value.replace(arg, "")
#
#             @register.filter(name="addSB")
#             def add_sb(value):
#                 return "{} SB".format(value)
#
#
#             使用自定义filter
#             {% load app01_filters %}
#
#             {# 使用我们自定义的filter #}
#             {{ somevariable|cut:"0" }}
#             {{ d.name|addSB }}
#
# if判断
#     if,elif和else
#
#     {% if user_list %}
#       用户人数：{{ user_list|length }}
#     {% elif black_list %}
#       黑名单数：{{ black_list|length }}
#     {% else %}
#       没有用户
#     {% endif %}
#
#
#
#     当然也可以只有if和else
#     {% if user_list|length > 5 %}
#       七座豪华SUV
#     {% else %}
#         黄包车
#     {% endif %}
#
#     if语句支持 and 、or、==、>、<、!=、<=、>=、in、not in、is、is not判断。
#
# with
#     定义一个中间变量，多用于给一个复杂的变量起别名。
#     注意等号左右不要加空格。
#
#
#     {% with total=business.employees.count %}
#         {{ total }} employee{{ total|pluralize }}
#     {% endwith %}
#     或
#
#     {% with business.employees.count as total %}
#         {{ total }} employee{{ total|pluralize }}
#     {% endwith %}
#
# csrf_token
#     这个标签用于跨站请求伪造保护。
#
#     在页面的form表单里面写上{% csrf_token %}
#
# 注释
#     {# ... #}
# 注意事项
#     1. Django的模板语言不支持连续判断，即不支持以下写法：
#
#     {% if a > b > c %}
#     ...
#     {% endif %}
#
#
#     2. Django的模板语言中属性的优先级大于方法
#
#     def xx(request):
#         d = {"a": 1, "b": 2, "c": 3, "items": "100"}
#         return render(request, "xx.html", {"data": d})
#     如上，我们在使用render方法渲染一个页面的时候，
#     传的字典d有一个key是items并且还有默认的 d.items() 方法，此时在模板语言中:
#
#     {{ data.items }}
#     默认会取d的items key的值。
#
# 母板
#
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#       <meta charset="UTF-8">
#       <meta http-equiv="x-ua-compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width, initial-scale=1">
#       <title>Title</title>
#       {% block page-css %}
#
#       {% endblock %}
#     </head>
#     <body>
#
#     <h1>这是母板的标题</h1>
#
#     {% block page-main %}
#
#     {% endblock %}
#     <h1>母板底部内容</h1>
#     {% block page-js %}
#
#     {% endblock %}
#     </body>
#     </html>
#     注意：我们通常会在母板中定义页面专用的CSS块和JS块，方便子页面替换。
#
# 继承母板
#     在子页面中在页面最上方使用下面的语法来继承母板。
#
#     {% extends 'layouts.html' %}
#     块（block）
#     通过在母板中使用{% block  xxx %}来定义"块"。
#
#     在子页面中通过定义母板中的block名来对应替换母板中相应的内容。
#
#     {% block page-main %}
#       <p>世情薄</p>
#       <p>人情恶</p>
#       <p>雨送黄昏花易落</p>
#     {% endblock %}
#
# 组件
#     可以将常用的页面内容如导航条，页尾信息等组件保存在单独的文件中，然后在需要使用的地方按如下语法导入即可。
#
#     {% include 'navbar.html' %}
#
# 静态文件相关
#
#     {% static %}
#     {% load static %}
#     <img src="{% static "images/hi.jpg" %}" alt="Hi!" />
#     引用JS文件时使用：
#
#     {% load static %}
#     <script src="{% static "mytest.js" %}"></script>
#     某个文件多处被用到可以存为一个变量
#
#     {% load static %}
#     {% static "images/hi.jpg" as myphoto %}
#     <img src="{{ myphoto }}"></img>
#
# {% get_static_prefix %}
#     {% load static %}
#     <img src="{% get_static_prefix %}images/hi.jpg" alt="Hi!" />
#     或者
#
#     {% load static %}
#     {% get_static_prefix as STATIC_PREFIX %}
#
#     <img src="{{ STATIC_PREFIX }}images/hi.jpg" alt="Hi!" />
#     <img src="{{ STATIC_PREFIX }}images/hi2.jpg" alt="Hello!" />
#
# simple_tag
#     和自定义filter类似，只不过接收更灵活的参数。
#
#     定义注册simple tag
#     @register.simple_tag(name="plus")
#     def plus(a, b, c):
#         return "{} + {} + {}".format(a, b, c)
#
#
#     使用自定义simple tag
#
#     {% load app01_demo %}
#     {# simple tag #}
#     {% plus "1" "2" "abc" %}
#
# inclusion_tag
#
#     多用于返回html代码片段
#     示例：
#
#     templatetags/my_inclusion.py
#
#     from django import template
#
#     register = template.Library()
#
#
#     @register.inclusion_tag('result.html')
#     def show_results(n):
#         n = 1 if n < 1 else int(n)
#         data = ["第{}项".format(i) for i in range(1, n+1)]
#         return {"data": data}
#
#
#
#     templates/snippets/result.html
#     <ul>
#       {% for choice in data %}
#         <li>{{ choice }}</li>
#       {% endfor %}
#     </ul>
#
#
#
#
#     templates/index.html
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#       <meta charset="UTF-8">
#       <meta http-equiv="x-ua-compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width, initial-scale=1">
#       <title>inclusion_tag test</title>
#     </head>
#     <body>
#
#     {% load inclusion_tag_test %}
#
#     {% show_results 10 %}
#     </body>
#     </html>
1
# ==============================================



# =================================================
# AJAXAJAX
1
# 基础知识
#
#     1 async javascript and xml 异步的js和xml
#         1 async异步是局部刷新，异步获取数据不会阻塞代码执行
#         2 xml是一种文件格式（是html的一种，可扩展标记语言）
#             特点是：用自己写的标签来存储数据和内容，现在某些
#             项目中，还在使用。
#         3 起初 ajax当初从服务器获取数据，服务器为了清晰表达
#            数据结构，丢失返回xml格式的内容，经过发展，用JSON
#            格式内容替代了xml格式内容，json操作更方便
# 1 xml
#
#     使用xml
#
#         创建xml结尾的文件
#             开头 <?xml version="1.0" encoding="utf-8" ?> 配置文件
#
#     文本例子
#         <?xml version="1.0" encoding="utf-8" ?>
#         <root>
#             <student>
#                 <name>lingling</name>
#                 <age>25</age>
#             </student>
#             <student>
#                 <name>yingying</name>
#                 <age>22</age>
#             </student>
#         </root>
#
#
# 1 服务器端渲染和前端渲染的区别
#
#     1 服务器端渲染的好处，有利于SEO优化（有助于搜索引擎的收录）
#     只要服务器并发（抗压能力）给力 页面加载，页面加载速度会比
#     客户端渲染更快
#         例子： 京东淘宝等首页内容都是基于服务器端渲染的，客户端
#         获取xml数据后直接呈现，增加页面第一次打开速度，而剩下
#         的内容都是基于AJAX获取数据，在客户端进行数据拼劲渲染的
#
# 局部刷新
#
#     服务器只把需要的数据返回（JSON格式字符串）
#     客户端接收数据自己做渲染
#
# AJAX 基本使用
#
#     1 创建ajax实力
#         let xhr = new XMLHttpRequest();
#
#     2 配置发送请求
#         xhr.open([http method], [url], [async],[user-name], [user-pass])
#             参数解析
#                 http method 请求方式GET,DELETE,HEAD,OPTIONS,TRACE,CONNECT
#                                     POST/PUT
#                 url  向服务器发送的api接口地址
#                 async  设置ajax请求的同步异步，默认异步（TRUE）
#                 user-name,use-pass 用户名密码：一般不用
#     3 事件监听
#
#         一般监听的嗾使 READY-STATE-CHANGE事件（AJAX状态改变事件），
#         可以获取服务器返回的响应头相应主体
#
#         xhr.onreadystatechange=()=>{
#             if(xhr.readyState===4 && xhr.status===200){
#                 xhr.responseText;
#             }
#         };
#
#     4 发送ajax请求
#
#         xhr.send([请求主题内容]);
#
#     总结
#         let xhr = new XMLHttpRequest();
#         xhr.open([http method], [url], [async],[user-name], [user-pass])
#         xhr.onreadystatechange=()=>{
#             if(xhr.readyState===4 && xhr.status===200){
#                 xhr.responseText;
#             }
#         };
#         xhr.send([请求主题内容]);
#
#
# 用ajax向服务端请求get数据
#     1 服务端
#         准备好url返回json数据
#         def json_get_test(request):
#             from django.http import HttpResponse
#             import json
#             result = {"status":"错误","data":"","city":"北京"}
#             #json返回为中文
#             return HttpResponse(json.dumps(result,ensure_ascii=False), content_type="application/json,charset=utf-8")
#
#     2 客户端
#         网页写代码例：
#             <script>
#                 let xhr = new XMLHttpRequest();
#                 xhr.open('GET','http://127.0.0.1:8000/json_get_test');
#                 xhr.onreadystatechange = () => {
#                     if (xhr.readyState ===4 && xhr.status === 200){
#                         console.log(JSON.parse(xhr.responseText));
#                     }
#                 }
#                 xhr.send(null)
#             </script>
#
# 用ajax向服务端post数据
#     1 服务端
#         准备好接收并解析数据
#         def json_post_test(request):
#             import json
#             print(request.method)
#             if request.method == "POST":
#                 # print(request.body)
#                 print(json.loads(request.body))
#                 return HttpResponse('haha')
#     2 客户端
#         注意
#             1 发送的网站和自己设定django网站url一直 注意/
#             2 一般send数据发送的文件格式为URL-ENCODE格式的字符串即："aa=100&bb=200"
#         let xhr = new XMLHttpRequest();
#         xhr.open('POST','http://127.0.0.1:8000/json_post_test/');
#         xhr.onreadystatechange = () => {
#             if (xhr.readyState ===4 && xhr.status === 200){
#                 {#console.log(JSON.parse(xhr.responseText));#}
#             }
#         };
#         xhr.send(JSON.stringify({"aa":11, "bb":22}))
#
# # -------------------------------------------------
# ajax的5状态（READY-STATE）
#
#     UNSENT 0
#         创建实例，还没发送
#     OPENED 1
#         执行了open操作
#     HEADES_RECEIVED 2
#         已经发送ajax请求，响应头信息已经被客户端接收
#         （响应头中包含了：服务器的时间，返回的HTTP状态码）
#     LOADING 3
#         响应主体内容正在返回
#     DONE 4
#         响应主体内容已经被客户端接收
#
#         let xhr = new XMLHttpRequest();
#         xhr.open('POST','http://127.0.0.1:8000/json_post_test/');  此时状态是1
#         xhr.onreadystatechange = () => {
#             if (xhr.readyState ===4 && xhr.status === 200){         # xhr.status===200可以写成/^(2|3)\d{2}$/.text(xhr.status)
#                 {#console.log(JSON.parse(xhr.responseText));#}
#             }
#         };
#         xhr.send(JSON.stringify({"aa":11, "bb":22}))
#
# AJAX准备知识：JSON
#
#     什么是 JSON ？
#     JSON 指的是 JavaScript 对象表示法（JavaScript Object Notation）
#     JSON 是轻量级的文本数据交换格式
#     JSON 独立于语言 *
#     JSON 具有自我描述性，更易理解
#     * JSON 使用 JavaScript 语法来描述数据对象，但是 JSON 仍然独立于语言和平台。JSON 解析器和 JSON 库支持许多不同的编程语言。
#
#      啥都别多说了，上图吧！
#
#
#
#     合格的json对象：
#
#     ["one", "two", "three"]
#     { "one": 1, "two": 2, "three": 3 }
#     {"names": ["张三", "李四"] }
#     [ { "name": "张三"}, {"name": "李四"} ]　
#      不合格的json对象：
#
#     复制代码
#     { name: "张三", 'age': 32 }  // 属性名必须使用双引号
#     [32, 64, 128, 0xFFF] // 不能使用十六进制值
#     { "name": "张三", "age": undefined }  // 不能使用undefined
#     { "name": "张三",
#       "birthday": new Date('Fri, 26 Aug 2011 07:13:10 GMT'),
#       "getName":  function() {return this.name;}  // 不能使用函数和日期对象
#     }
#     复制代码
#     stringify与parse方法
#     JavaScript中关于JSON对象和字符串转换的两个方法：
#
#     JSON.parse(): 用于将一个 JSON 字符串转换为 JavaScript 对象　
#
#     JSON.parse('{"name":"Q1mi"}');
#     JSON.parse('{name:"Q1mi"}') ;   // 错误
#     JSON.parse('[18,undefined]') ;   // 错误
#     JSON.stringify(): 用于将 JavaScript 值转换为 JSON 字符串。　
#
#     JSON.stringify({"name":"Q1mi"})
#     和XML的比较
#     JSON 格式于2001年由 Douglas Crockford 提出，目的就是取代繁琐笨重的 XML 格式。
#
#     JSON 格式有两个显著的优点：书写简单，一目了然；符合 JavaScript 原生语法，可以由解释引擎直接处理，不用另外添加解析代码。所以，JSON迅速被接受，已经成为各大网站交换数据的标准格式，并被写入ECMAScript 5，成为标准的一部分。
#
#     XML和JSON都使用结构化方法来标记数据，下面来做一个简单的比较。
#
#     用XML表示中国部分省市数据如下：
#
#
#     复制代码
#     <?xml version="1.0" encoding="utf-8"?>
#     <country>
#         <name>中国</name>
#         <province>
#             <name>黑龙江</name>
#             <cities>
#                 <city>哈尔滨</city>
#                 <city>大庆</city>
#             </cities>
#         </province>
#         <province>
#             <name>广东</name>
#             <cities>
#                 <city>广州</city>
#                 <city>深圳</city>
#                 <city>珠海</city>
#             </cities>
#         </province>
#         <province>
#             <name>台湾</name>
#             <cities>
#                 <city>台北</city>
#                 <city>高雄</city>
#             </cities>
#         </province>
#         <province>
#             <name>新疆</name>
#             <cities>
#                 <city>乌鲁木齐</city>
#             </cities>
#         </province>
#     </country>
#     复制代码
#     用JSON表示如下：
#
#
#     复制代码
#     {
#         "name": "中国",
#         "province": [{
#             "name": "黑龙江",
#             "cities": {
#                 "city": ["哈尔滨", "大庆"]
#             }
#         }, {
#             "name": "广东",
#             "cities": {
#                 "city": ["广州", "深圳", "珠海"]
#             }
#         }, {
#             "name": "台湾",
#             "cities": {
#                 "city": ["台北", "高雄"]
#             }
#         }, {
#             "name": "新疆",
#             "cities": {
#                 "city": ["乌鲁木齐"]
#             }
#         }]
#     }
#     复制代码
#     由上面的两端代码可以看出，JSON 简单的语法格式和清晰的层次结构明显要比 XML 容易阅读，并且在数据交换方面，由于 JSON 所使用的字符要比 XML 少得多，可以大大得节约传输数据所占用得带宽。
#
#     AJAX简介
#     AJAX（Asynchronous Javascript And XML）翻译成中文就是“异步的Javascript和XML”。即使用Javascript语言与服务器进行异步交互，传输的数据为XML（当然，传输的数据不只是XML）。
#
#     AJAX 不是新的编程语言，而是一种使用现有标准的新方法。
#
#     AJAX 最大的优点是在不重新加载整个页面的情况下，可以与服务器交换数据并更新部分网页内容。（这一特点给用户的感受是在不知不觉中完成请求和响应过程）
#
#     AJAX 不需要任何浏览器插件，但需要用户允许JavaScript在浏览器上执行。
#
#     同步交互：客户端发出一个请求后，需要等待服务器响应结束后，才能发出第二个请求；
#     异步交互：客户端发出一个请求后，无需等待服务器响应结束，就可以发出第二个请求。
#
#
#     示例
#     页面输入两个整数，通过AJAX传输到后端计算出结果并返回。
#
#
#     复制代码
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#       <meta charset="UTF-8">
#       <meta http-equiv="x-ua-compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width, initial-scale=1">
#       <title>AJAX局部刷新实例</title>
#     </head>
#     <body>
#
#     <input type="text" id="i1">+
#     <input type="text" id="i2">=
#     <input type="text" id="i3">
#     <input type="button" value="AJAX提交" id="b1">
#
#     <script src="/static/jquery-3.2.1.min.js"></script>
#     <script>
#       $("#b1").on("click", function () {
#         $.ajax({
#           url:"/ajax_add/",
#           type:"GET",
#           data:{"i1":$("#i1").val(),"i2":$("#i2").val()},
#           success:function (data) {
#             $("#i3").val(data);
#           }
#         })
#       })
#     </script>
#     </body>
#     </html>
#     复制代码
#
#     复制代码
#     def ajax_demo1(request):
#         return render(request, "ajax_demo1.html")
#
#
#     def ajax_add(request):
#         i1 = int(request.GET.get("i1"))
#         i2 = int(request.GET.get("i2"))
#         ret = i1 + i2
#         return JsonResponse(ret, safe=False)
#     复制代码
#
#     urlpatterns = [
#         ...
#         url(r'^ajax_add/', views.ajax_add),
#         url(r'^ajax_demo1/', views.ajax_demo1),
#         ...
#     ]
#     AJAX常见应用情景
#     搜索引擎根据用户输入的关键字，自动提示检索关键字。
#
#     还有一个很重要的应用场景就是注册时候的用户名的查重。
#
#     其实这里就使用了AJAX技术！当文件框发生了输入变化时，使用AJAX技术向服务器发送一个请求，然后服务器会把查询到的结果响应给浏览器，最后再把后端返回的结果展示出来。
#
#     整个过程中页面没有刷新，只是刷新页面中的局部位置而已！
#     当请求发出后，浏览器还可以进行其他操作，无需等待服务器的响应！
#
#
#
#
#     当输入用户名后，把光标移动到其他表单项上时，浏览器会使用AJAX技术向服务器发出请求，服务器会查询名为lemontree7777777的用户是否存在，最终服务器返回true表示名为lemontree7777777的用户已经存在了，浏览器在得到结果后显示“用户名已被注册！”。
#
#     整个过程中页面没有刷新，只是局部刷新了；
#     在请求发出后，浏览器不用等待服务器响应结果就可以进行其他操作；
#     AJAX的优缺点
#     优点：
#     AJAX使用JavaScript技术向服务器发送异步请求；
#     AJAX请求无须刷新整个页面；
#     因为服务器响应内容不再是整个页面，而是页面中的部分内容，所以AJAX性能高；
#     jQuery实现的AJAX
#     最基本的jQuery发送AJAX请求示例：
#
#     复制代码
#     <!DOCTYPE html>
#     <html lang="zh-CN">
#     <head>
#       <meta charset="UTF-8">
#       <meta http-equiv="x-ua-compatible" content="IE=edge">
#       <meta name="viewport" content="width=device-width, initial-scale=1">
#       <title>ajax test</title>
#       <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
#     </head>
#     <body>
#     <button id="ajaxTest">AJAX 测试</button>
#     <script>
#       $("#ajaxTest").click(function () {
#         $.ajax({
#           url: "/ajax_test/",
#           type: "POST",
#           data: {username: "Q1mi", password: 123456},
#           success: function (data) {
#             alert(data)
#           }
#         })
#       })
#     </script>
#     </body>
#     </html>
#     复制代码
#     views.py：
#     def ajax_test(request):
#         user_name = request.POST.get("username")
#         password = request.POST.get("password")
#         print(user_name, password)
#         return HttpResponse("OK")
#     $.ajax参数
#     data参数中的键值对，如果值值不为字符串，需要将其转换成字符串类型。
#
#     复制代码
#       $("#b1").on("click", function () {
#         $.ajax({
#           url:"/ajax_add/",
#           type:"GET",
#           data:{"i1":$("#i1").val(),"i2":$("#i2").val(),"hehe": JSON.stringify([1, 2, 3])},
#           success:function (data) {
#             $("#i3").val(data);
#           }
#         })
#       })
#     复制代码
#     JS实现AJAX
#
#     复制代码
#     var b2 = document.getElementById("b2");
#       b2.onclick = function () {
#         // 原生JS
#         var xmlHttp = new XMLHttpRequest();
#         xmlHttp.open("POST", "/ajax_test/", true);
#         xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
#         xmlHttp.send("username=q1mi&password=123456");
#         xmlHttp.onreadystatechange = function () {
#           if (xmlHttp.readyState === 4 && xmlHttp.status === 200) {
#             alert(xmlHttp.responseText);
#           }
#         };
#       };
#     复制代码
#
#
#     AJAX请求如何设置csrf_token
#     方式1
#     通过获取隐藏的input标签中的csrfmiddlewaretoken值，放置在data中发送。
#
#     复制代码
#     $.ajax({
#       url: "/cookie_ajax/",
#       type: "POST",
#       data: {
#         "username": "Q1mi",
#         "password": 123456,
#         "csrfmiddlewaretoken": $("[name = 'csrfmiddlewaretoken']").val()  // 使用jQuery取出csrfmiddlewaretoken的值，拼接到data中
#       },
#       success: function (data) {
#         console.log(data);
#       }
#     })
#     复制代码
#     方式2
#     通过获取返回的cookie中的字符串 放置在请求头中发送。
#
#     注意：需要引入一个jquery.cookie.js插件。
#
#     复制代码
#     $.ajax({
#       url: "/cookie_ajax/",
#       type: "POST",
#       headers: {"X-CSRFToken": $.cookie('csrftoken')},  // 从Cookie取csrftoken，并设置到请求头中
#       data: {"username": "Q1mi", "password": 123456},
#       success: function (data) {
#         console.log(data);
#       }
#     })
#     复制代码
#     或者用自己写一个getCookie方法：
#
#     复制代码
#     function getCookie(name) {
#         var cookieValue = null;
#         if (document.cookie && document.cookie !== '') {
#             var cookies = document.cookie.split(';');
#             for (var i = 0; i < cookies.length; i++) {
#                 var cookie = jQuery.trim(cookies[i]);
#                 // Does this cookie string begin with the name we want?
#                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
#                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
#                     break;
#                 }
#             }
#         }
#         return cookieValue;
#     }
#     var csrftoken = getCookie('csrftoken');
#     复制代码
#     每一次都这么写太麻烦了，可以使用$.ajaxSetup()方法为ajax请求统一设置。
#
#     复制代码
#     function csrfSafeMethod(method) {
#       // these HTTP methods do not require CSRF protection
#       return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
#     }
#
#     $.ajaxSetup({
#       beforeSend: function (xhr, settings) {
#         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
#           xhr.setRequestHeader("X-CSRFToken", csrftoken);
#         }
#       }
#     });
#     复制代码
#     注意：
#
#     如果使用从cookie中取csrftoken的方式，需要确保cookie存在csrftoken值。
#
#     如果你的视图渲染的HTML文件中没有包含 {% csrf_token %}，Django可能不会设置CSRFtoken的cookie。
#
#     这个时候需要使用ensure_csrf_cookie()装饰器强制设置Cookie。
#
#     django.views.decorators.csrf import ensure_csrf_cookie
#
#
#     @ensure_csrf_cookie
#     def login(request):
#         pass
#     更多细节详见：Djagno官方文档中关于CSRF的内容
#
#     AJAX上传文件
#     XMLHttpRequest 是一个浏览器接口，通过它，我们可以使得 Javascript 进行 HTTP (S) 通信。XMLHttpRequest 在现在浏览器中是一种常用的前后台交互数据的方式。2008年 2 月，XMLHttpRequest Level 2 草案提出来了，相对于上一代，它有一些新的特性，其中 FormData 就是 XMLHttpRequest Level 2 新增的一个对象，利用它来提交表单、模拟表单提交，当然最大的优势就是可以上传二进制文件。下面就具体
#
#     首先看一下formData的基本用法：FormData对象，可以把所有表单元素的name与value组成一个queryString，提交到后台。只需要把 form 表单作为参数传入 FormData 构造函数即可：
#
#     介绍一下如何利用 FormData 来上传文件。
#
#     复制代码
#     // 上传文件示例
#     $("#b3").click(function () {
#       var formData = new FormData();
#       formData.append("csrfmiddlewaretoken", $("[name='csrfmiddlewaretoken']").val());
#       formData.append("f1", $("#f1")[0].files[0]);
#       $.ajax({
#         url: "/upload/",
#         type: "POST",
#         processData: false,  // 告诉jQuery不要去处理发送的数据
#         contentType: false,  // 告诉jQuery不要去设置Content-Type请求头
#         data: formData,
#         success:function (data) {
#           console.log(data)
#         }
#       })
#     })
#     复制代码
#     或者使用
#
#     var form = document.getElementById("form1");
#     var fd = new FormData(form);
#     这样也可以直接通过ajax 的 send() 方法将 fd 发送到后台。
#
#     注意：由于 FormData 是 XMLHttpRequest Level 2 新增的接口，现在 低于IE10 的IE浏览器不支持 FormData。
#
#     练习（用户名是否已被注册）
#     功能介绍
#     在注册表单中，当用户填写了用户名后，把光标移开后，会自动向服务器发送异步请求。服务器返回这个用户名是否已经被注册过。
#
#     案例分析
#     页面中给出注册表单；
#     在username input标签中绑定onblur事件处理函数。
#     当input标签失去焦点后获取 username表单字段的值，向服务端发送AJAX请求；
#     django的视图函数中处理该请求，获取username值，判断该用户在数据库中是否被注册，如果被注册了就返回“该用户已被注册”，否则响应“该用户名可以注册”。
#     序列化
#     Django内置的serializers
#     def books_json(request):
#         book_list = models.Book.objects.all()[0:10]
#         from django.core import serializers
#         ret = serializers.serialize("json", book_list)
#         return HttpResponse(ret)
#     补充一个SweetAlert插件示例
#
#
#
#
#     点击下载Bootstrap-sweetalert项目。
#
#     复制代码
#     $(".btn-danger").on("click", function () {
#       swal({
#         title: "你确定要删除吗？",
#         text: "删除可就找不回来了哦！",
#         type: "warning",
#         showCancelButton: true,
#         confirmButtonClass: "btn-danger",
#         confirmButtonText: "删除",
#         cancelButtonText: "取消",
#         closeOnConfirm: false
#         },
#         function () {
#           var deleteId = $(this).parent().parent().attr("data_id");
#           $.ajax({
#             url: "/delete_book/",
#             type: "post",
#             data: {"id": deleteId},
#             success: function (data) {
#               if (data.status === 1) {
#                 swal("删除成功!", "你可以准备跑路了！", "success");
#               } else {
#                 swal("删除失败", "你可以再尝试一下！", "error")
#               }
#             }
#           })
#         });
#     })
#     复制代码
# # -------------------------------------------------
# ajax的属性和方法
#
# xhr.response        相应主体内容
# xhr.responseText    相应的内容是字符串（JSON或者XML格式字符串都可以）
# xhr.responseXML     相应主体的内容是XML文档
#
# xhr.status 返回的HTTP状态码
# xhr.statusText 状态码的描述
# xhr.timeout 设置请求超时的时间
# xhr.withCreadentials 是否允许跨域（FALSE）
#
# xhr.abort() 强制中断ajax请求
# xhr.getAllResponseHeaders() 获取所有响应头信息
# xhr.getResponseHeader([key]) 获取KEY对应的响应头信息
#
# xhr.open() 打开URL请求
# xhr.overrideMimeType 重写MIME类型
# xhr.send() 发送ajax请求
# xhr.setRequestHeader() 设置请求头 不能出现中文 在xhr.open之后
# # -------------------------------------------------
#
#
# # -------------------------------------------------
# 案例：基于服务器时间做倒计时
#
#     从服务器获取时间会存在一个问题： 由于服务器端返回数据需要时间，
#     所以客户端拿到的时间和服务器会有误差
#
#     如何减少误差
#         1从响应头获取时间，在ajax状态为2的时候就从响应头获取信息
#         2 请求方式设置为HEAD：值获取响应头信息即可，相应主体内容不需要
#         3 即使向服务器发送一个不存在的请求地址，返回的是404状态码，但是响应头
#             信息中都会存在“data”信息
# promise ？？？？
# # -------------------------------------------------
#
#
# # -------------------------------------------------
# 利用ajax向服务器发送请求次数过多或搞蹦服务器的解决方案（倒计时获取服务器时间）
#
#     创建一个全局变量，记录第一次从后台获取服务器时间，没一秒刷新的时候
#     都是在第一次夺得基础上一直累加1秒，而不是重新从服务器获取（尽情服务器压力）
#
# # -------------------------------------------------
#
#
# # -------------------------------------------------
# jquery中的ajax
#
# 使用方法
#
#     $.ajax([url],[options])
#     或者
#     $.ajax([options])  # 在options中有一个url字段代表请求的url地址
#
# 例子
#      $.ajax({
#         url:'xxxxxxxxxxx',  # 请求api接口地址
#         method:'get',       # 请求方式
#         data:null,          # 传递给服务器的信息可以放到data中，
#                                 # 如果是get请求是基与问号传参，如果
#                                 # 是post是基于请求主体传递的，data值，
#                                 # 可以是对象也可以使字符串（一般常用对象）
#         dataType:'json',    # 预设置获取结果的数据格式 TEXT/JSON/JSONP/NTML/SCRIPT ...
#                                 # 服务器返回给客户端的相应主体中内容一般都是字符串（JSON格式居多）,
#                                 # 而设置DATA-TYPE='JSON',jquery会内部吧字符串转换为json格式的对象
#         async:true,         # 设置同步或者异步（TRUE 为异步）
#         cache:true,         # 设置GET请求下是否建立缓存（默认是true-建立缓存，false-不建立缓存）
#         success:() =>{      # 回调函数，当ajax请求成功执行，jq执行回调函数的时候会把从相应主体中获取结果
#                                 #（可能二次处理了） 当做参数传递给回调函数
#
#         },
#         error:() =>{        # 请求失败后执行的回调函数
#
#         }
#      })
#
#
#
# # -------------------------------------------------
#
# # -------------------------------------------------
#
#
1
# =================================================



# =================================================
# vue—cli
1
# 安装
#     npm install -g @vue/cli
#     npm install -g @vue/cli-service-global
#
# 创建项目
#     vue create 项目名
#
# 安装插件
#     vue add 插件名
#
# 安装router插件
#
#     vue add router
1
# =================================================




# =================================================
# webpackwebpack
1
# 总结:
#     1 初始化目录
#
#         npm init -y
#     2 安装包
#         npm install mini-css-extract-plugin webpack webpack-cli webpack-dev-server html-webpack-plugin css-loader style-loader less less-loader npm install vue vuex babel-loader -D @babel/core @babel/preset-env -D
#
#     3 创建目录和文件
#
#         src/
#         webpack.config.js
#
#     3 配置文件(多页面应用，分目录保存文件，启动服务手动切换页面)
#
#         1 package.json
#             "scripts": {
#                 "build": "webpack",
#                 "dev": "webpack-dev-server",
#               },
#         2 webpack.config.js
#
#             let htmlWebpackPlugin = require('html-webpack-plugin');
#             let MiniCssExtractPlugin = require('mini-css-extract-plugin');
#
#             module.exports = {
#                 mode:"development",
#                 entry: {
#                     register: './src/js/register.js',
#                     index: './src/js/index.js'
#                 },
#                 output: {
#                     filename: "js/[name].js"
#                 },
#                 plugins: [
#                     new htmlWebpackPlugin({
#                         template: "./src/templates/register.html",
#                         filename: "templates/register.html",
#                         chunks: ['register']
#                     }),
#                     new htmlWebpackPlugin({
#                         template: "./src/templates/index.html",
#                         filename: "templates/index.html",
#                         chunks: ['index']
#                     }),
#                     new MiniCssExtractPlugin({
#                         filename:'css/[name].css'
#                     })
#                 ],
#                 module: {
#                     rules: [
#                         {
#                             test:/\.less$/,
#                             use:[MiniCssExtractPlugin.loader, 'css-loader', 'less-loader']
#                         }
#
#                     ]
#                 }
#
#             };
#
#         3 配置vue
#             1 js文件
#                 import Vue from 'vue'
#                 import Vuex from 'vuex'
#
#                 import createStore from '../lib/register_store'
#
#                 Vue.use(Vuex);
#                 const myStore = createStore();
#
#
#                 let App = {
#                     template: `
#                         <div>
#                             {{name}}
#                         </div>
#                           `,
#                     computed: {
#                         name: function() {
#                             return this.$store.state.name;
#                             },
#                     }
#                 };
#
#                 new Vue({
#                     el: "#app",
#                     store: myStore,
#                     template: `<app></app>`,
#                     components: {
#                         'app': App,
#                     },
#                 });
#             2 抽离的vuex文件
#                 import Vuex from 'vuex'
#
#                 function createStore() {
#                     return new Vuex.Store({
#                     state: {
#                         name: "index",
#                     },
#                     mutations: {},
#                     getters: {},
#                     actions: {}
#                     });
#                 }
#
#                 export default createStore;
#
# 详细：
#     0 概念
#
#         打包工具 --输出结果 js模块
#         支持模块化
#
#
#
#     1 安装本地
#
#         npm init -y     # 初始化项目
#         npm install webpack -D
#         npm install webpack-cli -D
#
#
#
#     1 创建目录
#
#         项目/
#             src/            # 源码文件夹
#                 index.js    # 入口文件
#             dist/
#                 index.html  #
#
#     1.2(暂时没安) 安装lodash（生产依赖包）
#
#         npm install lodash --save
#
#
#
#     2 配置
#
#         1 创建配置文件
#
#             默认名字 webpack.config.js
#
#         2 导入核心模块
#             let path = require('path')
#
#
#         3 导出配置文件
#
#             module.exports = {}
#
#         4 配置入口文件
#
#             module.exports = {
#
#                 entry:'路径'  # 入口
#
#             }
#
#         5 配置出口文件
#             module.exports = {
#
#                 output:{    # 出口
#
#                     filename:'bundle.js' # 打包后的文件名
#                                          # 若写成 filename:'bundle.[hash].js' 则每次打包的时候都生成带有hash戳的bundle.js文件
#                                             # [hash] 写成 [hash:8]  生成8位哈希戳
#                     path:path.resolve(__dirname, 'xx')    # 路径必须是一个绝对路径
#
#                 }
#
#             }
#
#         6 配置模式
#
#             module.exports = {
#
#                 mode:'development', # 有两种模式 production development
#             }
#
#         7 开发服务器配置(可以不写，默认8080)
#
#             module.exports = {
#
#                 devServer:{
#
#                     port:8000,      # 端口
#                     progress:true   # 可选 显示进度条
#
#                 }
#
#             }
#
#         8 配置打包命令
#
#             1 package.json文件的scripts属性中
#
#                 "scripts": {
#
#                     "build": "webpack"
#
#                   },
#
#         9 启动打包命令
#
#             npm run build
#
#
#
#         10 配置启动webpack 开发服务器
#
#             1 安装
#
#                 npm install webpack-dev-server -D
#
#             2 配置开发服务（可以不写默认8080）
#
#                 1 webpack.config.js文件下
#
#                     module.exports={
#
#                         devServer:{
#
#                             port:8000  # 指定端口
#                             contentBase:'./dist' # 指定服务文件
#                             cpmpress:true # 直接压缩（可选）
#
#                         }
#
#                     }
#
#             3 配置服务启动命令package.json
#
#                 "scripts": {
#
#                     "dev": "webpack-dev-server"
#
#                   },
#
#         11 配置html-webpack-plugin（省去手动在dist目录下创建html测试生成的js）
#
#             1 作用
#
#
#                 自动把js放到html文件中
#                 并且把结果输出到dist目录下
#                 源码html文件可放到src编辑
#                 不会在dist目录下创建编译的html文件
#                 执行 npm run build 命名后才会在dist目录下生成编译的html文件
#
#             2 安装
#
#                 npm install html-webpack-plugin -D
#
#             3 使用
#
#                 webpack.config.js中
#
#                     let HtmlWebpackPlugin = require('html-webpack-plugin')
#
#                     module.exports = {
#
#                         plugins:[                       # 插件属性 数组类型
#
#                             new HtmlWebpackPlugin({
#
#                                 template：'./src/index.html',  # 指定模板
#                                 filename:'index.html'          # 打包出来的文件名
#
#                                 minify:{            # 可选，用来压缩html文件
#
#                                     removeAttributeQuotes:true   # 删除html文件中属性的双引号
#                                     collapseWhitespace:true     # 代码压缩成一行
#
#                                 }
#                                 hash：true           # 可选， 生成hash戳（script等src属性的值生成hash戳）
#
#                         })]
#                     }
#
#         12 配置css样式(配置成不用link引入，自动引入的模块)
#
#             0 安装
#
#                 npm install css-loader -D
#                 npm install style-loader -D
#
#             0.5 index.js中引入css文件
#
#                 require('./index.css')
#
#             1 在webpack.config.js中配置模块module，module中配置rules规则数组
#
#                 module.exports = {
#                     ....
#                     plugins:[..],
#
#                     module:{
#
#                         rules:[
#                         ]
#
#                     }
#
#             2  rules中 写规则
#                 module.exports = {
#
#                     module:{
#
#                         rules:[
#
#                             # 用正则匹配的方法，匹配src文件中以css结尾的文件
#                             # 使用css-loader 用来解析css文件中的@import这种语法
#                             3 使用style-loader 用来把css插入到head标签中
#                             # use的数组执行顺序从右向左，从下到上，所以先执行css-loader,然后在执行style-loader
#                             # loader的值可以写成字符串，数组，对象（好处能传入参数）
#                             {test:/\.css$/， use:[{loader:'style-loader'}, 'css-loader']}
#
#                         ]
#
#                     }
#
#                 }
#
#             3 若想在html中直接写样式，并使样式生效，需要改变html样式的优先级options:{}
#
#                 module: {
#                     rules: [
#                         {
#                             test:/\.css$/,
#                             use:[
#                                 {
#                                     loader: "style-loader",
#                                     options:{
#                                         insertAt:'top'
#                                     }
#                                 },
#                                 'css-loader'
#                             ]
#                         }
#                     ]
#                 }
#
#             4 把css打包后生成单独的文件到dist目录中
#
#                 0 安装
#
#                     npm install mini-css-extract-plugin -D
#
#                 1 webpack.config.js中引入
#
#                     let MiniCssExtractPlugin = require('mini-css-extract-plugin')
#
#                 2 plugins中使用
#
#                     module.exports = {
#
#                         plugins:[
#
#                             new MiniCssExtractPlugin({
#
#                                 filename:'index.css'  # 生成到dist目录中的名字
#                             })
#                         ]
#                     }
#
#                 3 改变rules规则
#
#                     module: {
#                         rules: [
#                             {
#                                 test:/\.css$/,
#                                 use:[
#                                     MiniCssExtractPlugin.loader, # 处理完css-loader，扔到标签里去 # less也同样处理
#                                     'css-loader'
#                                 ]
#                             },
#                             {
#                                 test:/\.less$/,
#                                 use:[
#                                     MiniCssExtractPlugin.loader,
#                                     'css-loader',
#                                     'less-loader'
#                                 ]
#                             }
#                         ]
#                     }
#
#                 5 js文件中引入css
#                     require('./xx.css')
#
#
#                 6 执行npm run build 之后 dist目录中会有打包成结果的css文件
#
#             5 添加浏览器前缀
#
#                 1 安装
#
#                     npm install autoprefixer -D
#                     npm install postcss-loader -D
#
#                 2 webpack.conf.js中 less的规则中 css规则中
#
#                     {
#                         test:/\.css$/,
#                         use:[
#                             {
#                                 loader: "style-loader",
#                                 options: {
#                                     insertAt:'top',
#                                 }
#                             },
#
#                             'css-loader',
#                             'postcss-loader'  # 在处理css文件之前
#                         ]
#                     },
#
#                     {
#                         test:/\.less$/,
#                         use:[
#                             {
#                                 loader: "style-loader",
#
#                             },
#                             'css-loader',
#                             'postcss-loader',  # 在生成css之前添加
#                             'less-loader'
#                         ]
#                     }
#
#                 3 项目目录下创建postcss.config.js配置文件
#
#                 4 配置postcss.config.js
#
#                     module.exports = {
#                         plugins:[require('autoprefixer')]
#                     }
#
#             6 css文件的打包压缩(如果使用了该插件 js 就不会被压缩，需要另一个插件)
#
#                 1 安装
#
#                     npm install optimize-css-assets-webpack-plugin -D
#
#                 2 webpack.config.js中导入
#
#                     let optimizeCss = require('optimize-css-assets-webpack-plugin')
#
#                 3 module.exports加入
#
#                     module.exports = {
#                         optimization:{
#
#                             minimizer:[
#
#                                 new OptimizeCss()
#
#                             ]
#                         },
#                     }
#
#                 4 处理此插件导致js不别压缩问题
#
#                     1 安装
#
#                         npm install uglifyjs-webpack-plugin -D
#
#                     2 webpack.config.js中导入
#
#                         let UglifyJsPlugin = require('uglifyjs-webpack-plugin')
#
#                     3 minimizer中添加
#
#                         module.exports = {
#                         optimization:{
#
#                             minimizer:[
#
#                                 new UglifyJsPlugin({
#
#                                     cache:true,  # 是否使用缓存
#                                     parallel: true, # 是否并发打包
#                                     sourceMap: true # 是否需要编码调试es6，es5
#
#                                 })
#                                 new OptimizeCss()
#
#                             ]
#                         },
#                     }
#
#         13 配置less
#
#             0 安装
#
#                 npm install less -D
#                 npm install less-loader -D
#
#             1 src 下创建less文件
#
#             2 js中导入less文件
#                 require('./index.less')
#
#             3 webpack.config.js中module的rules中添加
#
#                 module: {
#                     rules: [
#                         {
#                             test:/\.css$/,
#                             use:[
#                                 {
#                                     loader: "style-loader",
#                                     options:{
#                                         insertAt:'top'
#                                     }
#                                 },
#                                 'css-loader',
#                             ]
#                         },
#                         {
#                             test:/\.less$/,
#                             use:[
#                                 {
#                                     loader: "style-loader",
#                                     options:{
#                                         insertAt:'top'
#                                     }
#                                 },
#                                 'css-loader',
#                                 'less-loader' # 注意loader加载顺序从下到上，从右到左
#
#                             ]
#                         },
#                     ]
#                 }
#
#         13.1 配置vue
#
#                 1 安装
#                     npm install vue -D
#                     npm install vuex -D
#
#
#                 3 使用
#                     1 js文件中引入
#
#                         import Vue from 'vue'
#                         import Vuex from 'vuex'
#
#                         ..... #vue代码
#                 4 纠正出现的错误
#
#                     浏览器错误提示[Vue warn]: You are using the runtime-only build of Vu。。。
#                     错误原因 webpack引入vue目录错误
#                     解决
#
#                         resolve:{
#                             alias:{
#                                 'vue': 'vue/dist/vue.js'
#                             }
#                         }
#
#                 5 代码分离抽取store
#
#                     1 创建store.js
#                     2 store.js中创建函数返回 Vuex
#                         import Vuex from 'vuex'
#
#                         function createStore() {
#                             return new Vuex.Store({
#                             state: {
#                                 name: "2ddd",
#                             },
#                             mutations: {},
#                             getters: {},
#                             actions: {}
#                         });
#                         }
#                     3 暴露函数（是其他模块能够导入）
#                         export default createStore;
#                     4 index.js中导入store.js内容,调用函数
#                         import createStore from './store'
#                         const myStore = createStore();
#
#                 7 其他内容的抽离，同上
#                     带有 new 的用 函数return，其他直接暴露导出即可
#
#
#
#
#                 8 文件配置总览
#
#                     const HtmlWebpackPlugin = require('html-webpack-plugin');
#                     module.exports = {
#                         mode:"development",
#                         entry: "./src/index.js",
#                         plugins: [
#                             new HtmlWebpackPlugin({
#                                 template: "./src/index.html",
#                             })
#                         ],
#                         resolve:{
#                             alias:{
#                                 'vue': 'vue/dist/vue.js'
#                             }
#                         }
#
#                     };
#
#
#         14 配置sass stylus
#
#             0 安装
#                 sass  ->  npm install node-sass sass-loader -D
#                 stylus -> npm install stylus stylus-loader -D
#
#
#         15 将es6 语法转换成es5
#
#             1 安装
#
#                 npm install babel-loader -D
#                 npm install @babel/core -D
#                 npm install @babel/preset-env -D
#
#             2 webpack.json中rules中
#                 module: {
#                     rules: [
#
#                         {
#                         test:/\.js$/,
#                         use:[
#                             {
#                                 loader: 'babel-loader',
#                                 options:{
#                                     presets:[‘@babel/preset-env’]   # 指定查询库，放着es6转成es5的模块
#                                 }
#                             }
#
#                         ]
#
#                         }
#                     ]
#
#                     }
#
#             3 执行 npm run build 进行打包
#
#
#         16 图片的配置
#
#             1 js中引用，less，css中引用图片的配置
#
#                 1 安装
#                     # file-loader 默认在内部生成一张图片到dist目录中
#                         # 并返回生成图片的名字
#                     npm install file-loader -D
#
#                 2 webpack.config.js下rules配置
#
#                     module:{
#                         rules:[
#
#                             {test:/\.(png|jpg|git)$/,use:'file-loader'}
#
#                         ]
#                     }
#
#                 3 执行命令 npm run build命令 目录dist下会生成图片
#
#             2 html中引用图片的配置
#
#                 1 安装
#
#                     npm install html-withimg-loader -D
#
#                 2 配置
#                     module:{
#                         rules:[
#
#                             {test:/\.html$/,use:'html-withimg-loader'}
#
#                         ]
#                     }
#
#             3 url-loader
#
#                 概念
#                     作一个限制 当图片小于多少k 用base64来转化，否州用file-loader产生
#                     真实的图片
#
#                     module:{
#                         rules:[
#
#                             {test:/\.(png|jpg|git)$/,
#                             use:{loader: 'url-loader',options:{
#                                 limit:200*1024
#                             }}
#                             }
#
#                         ]
#                     }
#         17 静态资源在dist输出目录的分配
#             1 图片
#                 module:{
#                     rules:[
#
#                         {
#                         test:xxxx,
#                         use:{loader: 'xxxx,
#
#                             options:{
#                                 outputPath:"/img/"    # 输出到img目录下
#                         }}
#                         }
#
#                     ]
#                 }
#             2 css
#
#                 plugins: [
#
#
#                     new MiniCssExtractPlugin({
#
#                         filename:'css/index.css'
#                     })
#                 ],
#
#             3 给引用资源统一加上路径publicPath
#
#                 output:{
#                     filename: "bundle.js",
#                     path:path.resolve(__dirname, 'dist'),
#                     publicPath: 'http://www.xxx.com'
#                 },
#
#             4 只想给图片统一加上路径
#
#                 use:{loader: 'xxxx,
#
#                             options:{
#                                 outputPath:"/img/"，
#                                 publicPath:"http://www.xxx.com"
#                         }}
#
#         18 多页应用
#
#             1 打包出多个js
#                 1 配置 webpack.config.js
#
#                     module.exports = {
#
#                         entry:{         #多入口
#
#                             index:'./src/index.js'  # 指定一个文件
#                             other:'./src/other.js'  # 指定一个文件
#
#                         },
#                         output:{
#
#                             filename:'[name].js'  # 根据多入口的文件多出口也打包出多个文件
#                             path:path.resolve(__dirname, 'dist')
#                         }
#
#                     }
#
#             2 打包出多个html
#
#                 module.exports = {
#
#                     plugins:[
#
#                         new HtmlWebpackPlugin({
#
#                             template: "./src/index.html",
#                             filename: "index.html",
#                             chunks: ['index']        # 使用index.js
#                         }),
#                         new HtmlWebpackPlugin({
#                             template: "./src/login.html",
#                             filename: "login.html",
#                             chunks: ['login']        # 使用login.js
#                         })
#
#                     ]
#
#                 }
#         19 配置source-map(调试)
#
#             1 source-map(会生成单独的xxx.map文件)
#
#                 1 概念
#                     源码映射 会单独生成一个sourcemap文件，可以帮助调试代码
#                     出错了会标识当前报错的列和行
#
#                 2 配置
#                     1 安装
#
#                         npm install babel-loader -D
#                         npm install @babel/core -D
#                         npm install @babel/preset-env -D
#
#                     2 配置
#
#                         module.exports = {
#
#                             devtool:'source-map'
#
#                         }
#             2 eval-source-map(不会生成单独的xx.map文件)
#
#                 配置同上
#
#             3 cheap-module-source-map(不会产生列， 但是是一个单独的映射文件)
#
#                 配置同上
#             4 cheap-module-eval-source-map（不会产生文件 集成在打包的文件中，不会产生列）
#
#                 配置同上
#
#         20 使webpack实现实时打包
#
#             1 配置
#
#                 module.exports = {
#
#                     watch:true,  # 监控文件 ，实现实时打包
#
#                 }
#
#         21 webpack中的插件
#
#             1 cleanWebpackPlugin（需要安装）
#
#                 1 概念
#
#                     每次打包 自动删除dist下的文件
#
#                 2 安装
#
#                     npm install clean-webpack-plugin -D
#
#                 3 配置
#
#                     let cleanWebpackPlugin = require('clean-webpack-plugin')
#
#                     module.export = {
#
#                         plugins:[
#
#                             new cleanWebpackPlugin(想清空的目录路径)
#                         ]
#                     }
#
#             2 copyWebpackPlugin（需要安装）
#
#                 1 概念
#
#                     想把某文件一起输出到dist目录下
#
#                 2 安装
#
#                     npm install copy-webpack-plugin -D
#
#                 3 配置
#
#                     let copyWebpackPlugin = require('copy-webpack-plugin')
#
#                     module.exports = {
#
#                         plugins:[
#
#                             new copyWebpackPlugin(
#                                 {from:'目录', to:'./'} # 把xx目录中的内容拷贝到dist目录
#                             )
#                         ]
#
#                     }
#
#             3 bannerPlugin   (内置)
#
#                 1 概念
#
#                     压缩的代码中会有注释版权声明（在每个打包js文件头部添加）
#
#                 2 配置
#
#                     let webpack = require('webpack');
#
#
#                     module.exports = {
#
#                         plugins:[
#
#                             new webpack.BannerPlugin('写的声明内容') # 会插在每个到包完文件头部
#                         ]
#
#                     }
#
#         22 webpack跨域问题？？？？？？？？？？？？？？？？？？？？？？？？？？？？
#
#         23 resolve
#
#             1 概念
#
#                 规定 webpack查找目录位置
#                 定义别名
#
#             2 配置
#
#                 module.exports = {
#
#                    resolve {
#
#                         modules:[path.resolve('目录')] # 指定查找目录
#                         alias:{
#                             名字：‘引用文件路径’  # 引用的时候直接 import 名字 即可
#                         }
#
#                         mainFields:['style', 'main']  # 先去找style属性，再去找mian属性
#                    }
#
#                 }
#
#         24 生产环境和开发环境的分离
#
#
#                 1 安装
#
#                     npm install webpack-merge -D
#
#                 2 配置
#
#                     1 建立两个配置文件
#
#                         0 基础文件（生产和开发都有的配置项）
#
#                             webpack.base.js
#
#                         1 生产文件
#
#                             webpack.prod.js
#
#                         2 开发文件
#
#                             webpack.dev.js
#
#                     2 配置两个文件
#
#
#                         let {smart} = require('webpack-merge')
#                         let base = require('webpack.base.js')
#                         module.exports = smart(base,{   # 继承webpack.base.js的基本配置
#
#                             ·配置
#                         })
#
#                     3 打包想要的配置文件
#
#                         如 npm run build -- --webpack.dev.js
#
#
#
# webpack安装包后拿来就用
#
#     var path = require('path');
#     var htmlWebpackPlugin = require('html-webpack-plugin');
#     var miniCssExtractPlugin = require('mini-css-extract-plugin');
#
#     module.exports = {
#
#         devServer: {
#             port:8000,
#             contentBase: './dist'
#         },
#         mode: "development",
#         entry:{
#
#             register: './src/register.js'
#         },
#         output: {
#
#             filename: "[name].js",
#             path: path.resolve(__dirname, 'dist')
#         },
#         plugins: [
#
#             new htmlWebpackPlugin({
#                 template: "./src/register.html",
#                 filename: "register.html",
#                 chunks: ['register']
#             }),
#             new miniCssExtractPlugin({
#                 filename:"[name].css"
#             })
#         ],
#         module: {
#             rules: [
#                 {
#                     test:/\.css$/,
#                     use: [
#                         miniCssExtractPlugin.loader,
#                         'css-loader'
#                     ]
#                 },
#                 {
#                     test: /\.less$/,
#                     use: [
#                         miniCssExtractPlugin.loader,
#                         'css-loader',
#                         'less-loader'
#                     ]
#                 },
#                 {
#                     test: /\.(png|jpg|gif)$/,
#                     use: [
#                         {
#                             loader: "file-loader",
#                             options:{outputPath:"/static/img/"}
#                         }
#                     ]
#                 }
#             ]
#         },
#
#     };
1
# =================================================