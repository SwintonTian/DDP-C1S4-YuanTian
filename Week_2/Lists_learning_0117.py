# 新建列表[] 有序、可变、异构
example_list=["iphone","airpods","ipad","apple watch"] 

# 嵌套列表
lists=[[0,1,2],[3,4,5],[6,7,8]]  
print(example_list)  

# 通过正负索引访问列表元素
print(example_list[0])  
print(example_list[-1])
print(lists[1][0])

# 通过索引确定元素计算&字符串格式化 f"{list[1]}"
sum = lists[1][1] + lists[2][2]
print(sum)
message = f"your gift is {example_list[1]}"
print(message)

# 查看列表长度 len
print(len(example_list))

# 1-6均改变了原列表
# 1.通过索引更改列表元素
example_list[1]= "macbook"
print(example_list)

# 2.在末尾新增元素
example_list.append("airpods pro")
print(example_list)

# 3.增加元素在特定索引处
example_list.insert(1,"joker")
print(example_list)

# 4.将新列表加在原列表末尾
other_list=["apple","mango"]
example_list.extend(other_list)
print(example_list)

# 5.删除列表元素
example_list.remove("apple")
print(example_list)

# 6.通过索引删除特定元素
del example_list[1]
print(example_list)

# 排序列表中的元素（数字&字符串）
numbers=[3,1,4,1,5,9,2,6]
sorted_numbers=sorted(numbers) # sorted() 不改变原列表
print(sorted_numbers)
numbers.sort() #.sort() 改变原列表
print(numbers)
sorted_example_list=sorted(example_list,reverse=False)
print(sorted_example_list)
example_list.sort()
print(example_list)

# 反转列表顺序
numbers.reverse()
print(numbers)

# 自定义排序列表
example_list.sort(key=len)
print(example_list)

# 清空列表
example_list.clear()
print(example_list)
