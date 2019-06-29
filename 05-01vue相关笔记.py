


# =======================================================
# vuevue
1
# 1 介绍
    # 1 介绍
        1
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
        1
    # 2 中间件
        1
        # 1 created
            # 	实例创建完成后调用,此阶段完成了数据的观测等,但尚未挂载
            # 	$el 还不可用,需奥初始化处理一些数据时比较游泳

        # 2 mounted
        # 	el挂载到实例上后调用

        # 3 beforeDestroy
        # 	实例销毁之前调用

        # 4 例子
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
        1
    # 计算属性
        1
        # 用于模板内的表达式频繁的切换变量,使用计算属性

        # 所有计算属性都以函数的形式写在Vue实例内的computed选项内
        # 最总返回计算后的结果

        # 每一个计算属性都包含一个getter和一个setter

        # 例子
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

        # 计算属性的setter例子

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
        1
    # 计算属性缓存
        1
        # 计算属性是基于它的依赖缓存的.一个计算属性所依赖的数据发生
        # 变化时,它才会重新取值,所以text只要不便,计算属性也就不更新
        # 计算属性和侦听属性
        1
    # 计算属性和侦听属性公有的作用
        1
        # 观察和相应Vue实例上的数据变动,通常更好的做法是
        # 使用计算属性而不是watch侦听属性
        1
    # 侦听属性(watch)
        1
        # 作用:

        # 	wath选项提供了一个更通用的方法,来相应数据表话,
        # 	当需要在数据变化时执行异步或开销较大的操作时使用

        # 计算属性无法做到 侦听器能做到的事情

        # 设置中间状态 执行异步操作 限制操作频率

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
        1

# 2 使用

    # 1 安装
        1
        # 开发环境版本
        # <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
        1
    # 2 Vue实例与数据绑定
        1
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
        1

    # 3 数据更新
        1
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
        1
    # 4 不让对象数据更新
        1
        # 使用 Object.freeze(obj)
        #
        1
    # 5 Vue的属性获取
        1
        # var test = {a:1}
        # # var vm = new Vue({
        # # 	el:"#app",
        # # 	data:test
        # # })
        #
        # # console.log(vm.$data === test) //true
        # # console.log(vm.$el === document.getElementById('app')) // true
        1
    # 6 通过Vue 指定 默认建立了双向绑定
        1
        # Vue实例本身也代理了data对象里的所有属性
        # var ddd = {s:1}
        # var app = new Vue({
        # 	el: "#app",

        # 	data:ddd
        # })
        # console.log(app.s) # 返回1
        # app.s = 2
        # console.log(ddd.s) # 返回2
        1
    # 7 插值与表达式
        1
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
        1
    # 8 过滤器
        1
        # {{ | }}

        # 可窜联
        # {{ arg|filterA|filterB }}

        # 可接收参数
        # {{ arg|filterA('arg1', 'arg2') }}
        1
    # 9 指令

        # 1 条件渲染指令 v-if  v-else-if  v-else
            1
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
            1
        # 2 v-on
            1
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
            1
        # 3 语法糖
            1
            # v-bind  ---->   :
            # v-on    ---->	  @
            1
        # 4 v-once
            1
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
            1
        # 5 v-show
            1
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
            1
        # 6  v-if 与 v-show
            1
            # v-if 更适合经常改变的场景,因为它切换开销相对较大而 v-show适用于频繁切换条件
            #
            1
        # 7 列表渲染指令v-for
            1
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
            1
        # 8 表单与v-model

            # 1 单选按钮
                1
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
                1
            # 2 单个复选框
                1
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
                1

            # 3 多个复选框
                1
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
                1

            # 4 下拉框
                1
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
                1
            # 5 v-bind下拉框
                1
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
                1
            # 6 绑定值(复选)
                1
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
                1
            # 7 绑定值(选择列表)
                1
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
                1
            # 8 自定义指令

                # 1 全局注册
                    1
                    # 	Vue.directive('foucs'.{
                    # 		选项
                    # 		})
                    1
                # 2 局部注册
                    1
                    # 	var app = new Vue({
                    # 		el: '#xx',
                    # 		derectives:{
                    # 			focus:{
                    # 				选项
                    # 			}
                    # 		}
                    # 	})
                    1
                # 3 自定义指令的选项
                    1
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
                    1
                # 4 钩子函数的参数
                    1
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
                    1

            # 9 插入节点时调用指令(inserted)

                1
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
                1
            # 10 v-for的可选参数前项索引
                1
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
                1

            # 11 对象的v-for 值的展现
                1
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
                1

            # 12 对象的v-for 值-键的展现
                1
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
                1

            # 13 对象的v-for 值-键-索引
                1
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
                1

            # 14 使用v-for 推荐加上 v-bind:key
                1
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
                1
    # 10 事件
        # 1 阻止默认事件的发生
            1
            # v-on:click.prevent

            # a标签不跳转
            # <div id="app">
            # 	<a href="http://www.baidu.com" v-on:click.prevent>11</a>
            # </div>

            # var app = new Vue({

            # 	el:'#app',

            # })
            1
        # 2 添加事件监听器使用事件捕获模式,在捕获模式下触发
            1
            # v-on:click.capture

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
            1
        # 3 当前元素自身触发才会触发函数, 冒泡事件不是触发此元素的函数
            1
            # v-on:click.self

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
            1
        # 4 滚动事件的默认行为,滚动立即触发，提供移动端性能
            1
            # v-on:click.passive

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
            1
        # 5 事件处理系统修饰键

            1
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
            1
        # 6 事件处理修饰键与常规按键
            1
            # 1 在和 keyup 一起使用时, 时间触发时修饰键必须处于按下状态
            # ,只有在按住ctrl的情况下, 才能触发keyup.ctrl

            # 2 如果项只按ctrl 触发时间 使用keyCode:keyup.17
            1
        # 7 事件触发.exact修饰符

                # 作用

                    # 	精确触发按键

                # 1 按住ctrl和其他键 点击鼠标都能触发事件
                    1
                    # <button @click.ctrl="onClick">A</button>

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
                    1
                # 2 有且只有按住ctrl,点击鼠标的时才能触发事件
                    1
                    # <button @click.ctrl.exact="onCtrlClick">A</button>
	                #
                    1

                # 3 不按系统修饰符的按键,点击都能触发
                    1
                    # <button @click.exact="onClick">A</button>
                    #
                    1

                # 4 事件触发鼠标按键修饰符
                    1
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
                    1
    # 11 表单输入绑定

        # 1 v-model作用及特性
            1
            # 	1 在<input>、<textarea> 及 <select> 元素上创建双向数据绑定

            # 	2 v-model会忽略所有表单的元素 value, checked,selected属性
            # 		而总是将Vue实例的数据作为数据来源

            # 	3 v-model 不会在输入法组合文字过程中得到更新.
            # 		如果项处理这个过程,使用input事件
            1

        # 2 表单输入绑定v-model 文本
            1
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
            1

        # 3 表单输入绑定v-model 多行文本

            1
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
            1
        # 4 v-model 和 v-bind
            1
            # v-model

                # 绑定的值通常是静态字符串(复选框也可以是布尔值)

            # v-bind

                # 可以绑定Vue实例的一个动态属性上,绑定html中的标签属性
            1



        # 5 绑定class
            1
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
            1
        # 6 绑定数组语法
            1
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
            1

        # 7 列表渲染有些数组的变动不能被检测到(因为js的限制)

            1
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
            1

        # 8 对象更改检测注意事项
            1
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
            1

        # 9 绑定内联样式
            1
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
            1

    # 12 数组方法
        1
        # push()
        # pop()
        # shif()
        # splice()
        # sort()
        # reverse()
        1

    # 13 修饰符

        # 1 修饰符(.lazy)
            1
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
            1
        # 2 修饰符(.number)
            1
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
            1
        # 3 修饰符(.trim) 自动过滤首尾空格
            1
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
            1
        # 4 按键修饰符

            1
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
            1


        # 5 自动匹配按键修饰符

            1
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
            1


    # 14 组件

        # 1 概念
            1
            # Vue的组件就是提高重用性的 让代码可以复用
            #
            1
        # 2 使用
            # 1 注册
                1
                # 1 全局注册
                    1
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
                    1
                # 2 局部注册
                    1
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
                    1

        # 3 Vue组件特殊情况
            1
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
            1

        # 4 Vue组件注册component的其他选项(data)

            # 1 data使用和实例稍有区别,data必须是函数,将数据return
                1
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
                1
            # 2 组件data选项引用外部同一个对象,同步共享
                1
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
                1
            # 3 组件data选项直接返回对象,不同步共享
                1
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
                1

            # 4 使用props传递数据
                1
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
                1
            # 5 props与data 区别:
                1
                # props的数据来之父级
                # data是组件自己的数据
                1

            # 6 props命名规制
                1
                # 使用DOM模板 驼峰命名的props名词为短横分割命名

                # <my-haha warking-test="xx"><my-haha>

                # props:[warningText]

                # 如果使使用的是字符串模板, 可以互绿这些限制
                1
            # 7 props传递动态数据
                1
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
                1

            # 8 单项数据流
                1
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
                1
            # 9 props的数据验证
                1
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
                1
            # 10 自定义一个验证函数
                1
                # 	propF:{
                # 		validator : function (value)
                # 			return value > 10;
                # 			}
                # 		}
                # 	}
                # })
                1
            # 11 自定义事件
                1
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
                1
            # 12 自定义组件上使用v-model指令
                1
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
                1
            # 13 非父子组件通信(中央事件bus)
                1
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
                1

            # 14 父链(不推荐使用,使得组件紧耦合)
                1
                # 在子组件中,使用this.$parent可以直接访问改组件的父实例或组件,
                # 父组件也可以通过this.$children访问它所有的子组件
                1

            # 15 子组件索引
                1
                # 用特殊的属性 $refs来为子组件指定一个索引名称

                # 在父组件模板中,子组件标签上使用 ref 指定一个名称,
                # 井在父组件内通过 this.$refs 来访问指定名称的子组件
                1

    # 15 使用slot分发内容
        1
        # 1 概念
            1
            # 当需要让组件组合使用,混合父组件的内容与子组件的模板时,
            # 就会用到slot,这个过程叫内容分发

            # pros传递数据,events触发事件和slot内容分发就构成了Vue
            # 组件的3个API来源
            1

        # 2 slot作用域
            1
            # 父组件模板内容是在父组件作用域内编译,子组件模板的内容是在
            # 子组件作用域内编译
            1
        # 3 slot用法
            1
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
            1
        # 4 具名Slot
            1
            # 给<slot>元素制定一个name后可以分发多个内容>

            # 作用域插槽

            # 作用域插槽是一种特殊的slot,使用一个可以复用的模板替换已
            # 渲染的元素
            1
        # 5 访问slot
            1
            # $slots 访问被slot分发的内容方法
            #
            1

    # 16 Render函数
        1
        # Virtual Dom

        # Virtual Dom 并不是真正意义上的 DOM ,而是一个轻
        # 量级 的 JavaScript 对象,在状态发生变化时,
        # Virtual Dom 会进行 Diff 运算,来更新只需要被替
        # 换的 DOM ,而不是全部重绘。

        # 与 DOM 操作相比, Virtual Dom 是基于 JavaScript
        # 计算的,所以开销会小很多
        1
    # 17 使用钩子函数
        1
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
    # 18 vue中操作cookie
        1
        # 建议使用工具js-cookie 网址https://www.npmjs.com/package/js-cookie
        # 引用方式使用
            # <script src="https://cdn.jsdelivr.net/npm/js-cookie@2/src/js.cookie.min.js"></script>

        # 使用
        #     1 增
        #         Cookies.set("name","ling")
        #         Cookies.set('name', 'value', { expires: 7 }); # 设置过期时间
        #     2 查
        #         Cookies.get("xx")
        #         Cookies.get() # 读取所有cookie
        #     3 删
        #         Coolies.remove("xx")
        1
# =======================================================



# =================================================
# vuexvuex
9999999999999999
    # 1 vuex 与v-model的双向绑定
            1
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
            1
    # 2 vuex中给对象添加或更改属性
            1
    #     Vue.set(obj, key, value);
    #
    #     return obj   # 为了浏览前相应
            1
    # 3 概念
        1
        # 	状态管理 用来管理全局的变量
        #
        1
    # 4 安装
        1

        # 		下载源码 引入文件
        #
        1
    # 5 使用
        1
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
        1
    # 6 操作数据
        1
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
# 注意：
#   vue使用axios的回调函数中this不指向vue实例，为undefined
#     解决方法：
#         使用匿名函数的语法糖 => 即
#           .....
#           .then((response) =>{
#               ....
#             })
#           .catch((error) =>{
#              .....
#           })
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
# axios发送post请求
    # axios.post('/user', {
    #     firstName: 'Fred',
    #     lastName: 'Flintstone'
    #   })
    #   .then(function (response) {
    #     console.log(response);
    #   })
    #   .catch(function (error) {
    #     console.log(error);
    #   });

1
# =================================================
