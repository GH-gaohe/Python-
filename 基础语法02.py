#a = {
    #"zhangsan": {"gender": "male",   "height": 180, "weight": 60, "score": None, "class": 3},
    #"lisi":     {"gender": "female", "height": 160, "weight": 50, "score": 270, "class": 1},
    #"wangwu":   {"gender": "female", "height": 170, "weight": 65, "score": "250", "class": 2},
    #"zhaoliu":  {"gender": "male",   "height": 175, "weight": 70, "score": 295, "class": 1},
    #"sunqi":    {"gender": "male",   "height": 168, "weight": 58, "score": 260, "class": 3},
#}
    

#（5）【高阶挑战】按总分从高到低排序，打印出排名前三的学生姓名和分数
#a_name=[]
#a_score=[]
#for i in a:
    #a_name.append(i)
    #a_score.append(a[i]['score'])

#a_new = []
#for i in a:
    #a_new.append([a[i]['score'],i])

#a_new_sort = sorted(a_new,reverse = True)   #默认是降序

#a_new_sort.sort(reverse=True)

#print(a_new_sort[0:3])  #默认[开始 的位置: 结束的位置+1] 默认取不到结束位置本身
#for i in a_new_sort[0:3]:
    #print(i[1],i[0])
    
    




#数据分析第二课： 
#函数  的作用： 减少代码的重复，提高程序的复用性

#异常处理：对于一些无法避免的错误进行解释说明的过程
#try:
    #可能发生错误的地方
#except:
    #如果发生错误了，就对错误解释说明，按照我指定的规矩来
#else:
    #如果没有发生错误 ，就会去执行后面程序

#while True:
    #try:
        #a = float(input("请输入:"))
    #except:
        #print('输入 的不是一个数字，你必须输入一个数字才可以')
    #else:
        #print(a)
        #break

#题目描述  现在有5个班 ，每个班分为5个小组，分别有不同的人数，我们要计算每个班级的总人数

#函数思路：我们可以创建自定义一个功能体，这个功能体实现的就是根据给定不同班级的信息，就可以计算出这个班级有多少人  函数用def定义


#class1=[10,20,30,40,50]
#class2=[50,20,50,80,50]
#class3=[10,20,50,40,80]
#class4=[60,50,30,40,10]
#class5=[100,80,30,90,50]

#s1 = 0
#for i in range(len(class1)):
    #s1=s1+class1[i]
#print(s1)
#s1 = 0
#for i in range(len(class1)):
    #s1=s1+class1[i]
#print(s1)
#s1 = 0
#for i in range(len(class1)):
    #s1=s1+class1[i]
#print(s1)
#s1 = 0
#for i in range(len(class1)):
    #s1=s1+class1[i]
#print(s1)
#s1 = 0
#for i in range(len(class1)):
    #s1=s1+class1[i]
#print(s1)



#def cal_classnum(info):
    #s = 0
    #for i in range(len(info)):
        #s=s+info[i]
    #return s

#ans1 = cal_classnum(class1)
#print(ans1)
#ans2 = cal_classnum(class2)
#print(ans2)
#ans3 = cal_classnum(class3)
#print(ans3)









###### 课后作业


#1.
#def mystery(a, b):
    #result = 0
    #for i in range(a, b + 1):
        #if i % 3 == 0 or i % 5 == 0:
            #result = result + i
    #return result
 
#print(mystery(1, 20))

  #（1）输出数字为98
  #（2）10 + 12 + 15 = 37


#2.
  #（1）程序会报错，错误类型是builtins.TypeErrorz，因为字符串不能和整数比较大小
  #（2）
#def get_grade(score):
    #if score >= 90:
        #return 'A'
    #if score >= 80:
        #return 'B'
    #if score >= 70:
        #return 'C'
    #if score >= 60:
        #return 'D'
    #if score < 60:
        #return 'F'
 
#s = input('请输入成绩：')
#grade = get_grade(int(s))
#print(f'等级是：{grade}')
  #（3）程序会返回F，因为 -5 < 60 ，但是不合理，因为分数一般不会是负数


#3.
#students = [
    #['张三', 175, 'male', 15],
    #['李四', 165, 'female', 18],
    #['Tom', 162, 'male', 13],
    #['Cindy', 180, 'female', 20],
#]

#def filter_students(data, gender, min_age):
    #result_list = []
    #for student in data:
        #if student[2] == gender and student[3] >= min_age:
            #result_list.append(student)
    #return result_list
#result = filter_students(students, 'female', 18)
#print(result)


#4.
#def get_top_n(data, n, key):
    #all_list = []
    #for name in data:
        #info = data[name]
        #value = info[key]
        #if value is None:
            #continue
        #try:
            #if type(value) == str:
                #value = int(value)
        #except:
            #continue
        #if type(value) == int:               
            #all_list.append([name, value])
    #def take_score(item):
        #return item[1]
    #all_list.sort(key = take_score, reverse = True)
    #top_stu = all_list[:n]
    #return top_stu
    
#a = {
    #"zhangsan": {"gender": "male", "height": 180, "weight": 60, "score": None, "class": 3},
    #"lisi":     {"gender": "female", "height": 160, "weight": 50, "score": 270, "class": 1},
    #"wangwu":   {"gender": "female", "height": 170, "weight": 65, "score": "250", "class": 2},
    #"zhaoliu":  {"gender": "male", "height": 175, "weight": 70, "score": 295, "class": 1},
    #"sunqi":    {"gender": "male", "height": 168, "weight": 58, "score": 260, "class": 3},
#}
#result = get_top_n(a, 3, "score")
#print (result)


#5.
#def safe_calc(operator, num1, num2):
    #support_ops = ["+", "-", "*", "/"]
    #if operator not in support_ops:
        #return "不支持的运算符"
    #try:
        #n1 = float(num1)
        #n2 = float(num2)
        #if operator == '+':
            #res = n1 + n2
        #elif operator == '-':
            #res = n1 - n2
        #elif operator == '*':
            #res = n1 * n2
        #elif operator == '/':
            #res = n1 / n2
        #return res
    #except ZeroDivisionError:
        #return "除数不能为0"
    #except (ValueError, TypeError):
        #return "参数必须是数字"

#print(safe_calc('+', 10, 5))
#print(safe_calc('/', 10, 0))
#print(safe_calc('%', 10, 5))
#print(safe_calc('+', 'hello', 5))