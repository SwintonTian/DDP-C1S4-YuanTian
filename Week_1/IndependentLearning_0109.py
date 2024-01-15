# The following are my notes from some python courses on a Chinese video app (bilibili), so there are lots of Chinese notes and code commands. 
# Please forgive me！：）

# print
print("爸!!")
# +加号将几个字符相加
print('爸'+ '，'+'我回来了！')
# 单双引号互换
print('He said "good!"')
# \n 换行
print("hello!\nworld!")
# ''' 三个单引号换行
print('''床前明月光
疑是地上霜
举头望明月
低头思故乡''')
# ______________

# 变量
greet = "您好，吃了吗？"
greet_chinese = greet
greet_english = "hi!"
greet = greet_english
print(greet+"张三")
print(greet+"李四")
print(greet+"王五")
# 储存中文
print(greet_chinese+"张三")
# 变量命名：字母、下划线、数字（不能开头）
# 变量名大小写不同，不用关键字命名，如print
# ______________

# 数学运算
print(1+2*3/5)
import math # 引入math函数
result = math.sin(0)
print(result)

# 多重赋值
x,y,z=1,2,3
print(y)
x,z=z,x
print(z)
# ______________

# 注释方法1:用#
# 注释方法2:多行注释-选中 command+/
# ______________

# 数据类型
# 字符串 str   “hello”
# 整数 int   6  -32
# 浮点数 float  6.0  -32.0
# 布尔 bool  True False
# None

# 对字符串求长度
length=(len('hello'),len('hi!'),len('你 好'))
print(length)
# 通过索引获取单个字符
print("hello"[1]) #python中的第一个字符为0号

b0="hello"
b1= True
b2= False
b3= None
b4= 4.0
print(type(b0))
print(type(b1))
print(type(b3))
print(type(b4))
# ______________

# 用户输入input
user_age=int(input("your age: ") )
# input 用户输入的内容默认为字符串str
# 在下面做数学比较前，需要将用户输入的内容变成整数int
if user_age <= 24:
    print("原来你是个"+str(user_age)+"岁的小笨蛋")  # print的是字符串，因此需要将上面的整数变成字符串str
else:
    print("恭喜！" + str(user_age) + "岁的你已经比我老了")


item = "Swinton"
print(item.upper())  # 输出全部大写 upper()
print(item)
# _____________

# 条件语句 if,elif,else
# == 比较相等符号
mood_index = int(input("宝贝今天的心情指数是："))
if mood_index >= 60:
    print("恭喜！你可以打游戏了！")
    print("（但别玩太久...")
else:
    print("别了别了！")

# 嵌套条件语句
# 多个条件判断elif，会执行第一个满足条件的语句
# BMI = 体重 / （身高 ** 2）
user_weight = float(input("请输入您的体重（单位：kg）："))
user_height = float(input("请输入您的身高（单位：m）："))  # 身高是小数，所以要转化成浮点数float
user_bmi = user_weight / (user_height ** 2)
print("您的BMI指数是：", str(user_bmi))

if user_bmi <= 18.5:
    print("你也太瘦了！")
elif user_bmi <= 25:
    print("你是一个正常人")
elif user_bmi <= 30:
    print("稍微有一点点点胖哦")
else:
    print("减肥吧亲！")
# _____________

# 逻辑运算 and,or,not   优先级：not>and>or
housework_count = int(input("请输入您本月完成的的家务数量："))
money = int(input("请输入您本月转给宝贝的红包金额："))
angry = int(input("宝贝现在心情如何（生气输入0，开心输入1）："))

if housework_count >= 10 and money >= 520 and angry == 1:
    print("恭喜你有礼物了！")
else:
    print("拜拜了您嘞。")
# _____________

# 列表（可变）list
shopping_list = []  # 定义一个空的列表
shopping_list.append("无人机")  # 在特定列表里加东西
shopping_list.append("电脑")
shopping_list.append("鼠标")
shopping_list.append("充电器")
shopping_list.append("养生杯")
shopping_list.append("耳机")
shopping_list.remove("鼠标")  # 在特定列表里删东西，这个东西必须真实存在在列表中
shopping_list[4] = "咖啡"  # 通过索引直接替换列表里的原元素
# 变量.方法名（...） 如shopping_list.append 加入或删除东西后的list会代替原来的list
print(shopping_list)
print(len(shopping_list))  # len函数求长度，元素的数量
print(shopping_list[0])  # 元素的索引

num_list = [1, 20, 666, -520, -17, 121]
print(max(num_list))  # max为输出列表中的最大值
print(min(num_list))  # min为输出列表中的最小值
print(sorted(num_list))  # 为输出排序好的列表
# _____________
