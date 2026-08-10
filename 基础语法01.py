#数据分析
#1.获取数据  requests  获取网页上可显示的数据
#2.读取数据，筛选数据，计算数据     pandas + numpy 
#3.数据可视化 ，  pygal , matplotlib


#python存储数据的容器：  []    {}

#场景练习1   成绩计算
#a = [10,20,30,50,99,100,60,80]
##1.总成绩 2.及格人数  3.不及格人数，4.平均分
#s = 0  
#b = 0
#p = 0
#for i in range(len(a)):
    #s = s + a[i]
    #if a[i] >= 60:
        #b = b + 1
    #else:
        #p = p + 1
        
#print(s)
#print(b)
#print(p)
#print(s/len(a))


#场景练习2   身高计算
#a=[
    #['zhangsan',175,'male',15],
    #['lisi',165,'female',18],
    #['Tom',162,'male',13],
    #['Cindy',180,'female',20],
#]

##性别为男的，年龄18岁以上的姓名
#for i in range(len(a)):
    #if a[i][2]=='female' and a[i][3]>=18:
        #print(a[i][0],a[i][1])
        

##性别为男的,height 180以上的姓名
#a={
    #'zhangsan':{
        #'gender':'male',
        #'Phone':'13311111',
        #'height':180,
        #'weight':60,
        #'math_score':98,
        #'english_score':98,
        #'chinese_score':98,
    #},
    #'lisi':{
        #'gender':'female',
        #'Phone':'1888',
        #'height':160,
        #'weight':50,
        #'math_score':80,
        #'english_score':90,
        #'chinese_score':100,
    #},
    #'wangwu':{
        #'gender':'female',
        #'Phone':'9999',
        #'height':170,
        #'weight':65,
        #'math_score':100,
        #'english_score':80,
        #'chinese_score':70,
    #},   
#}
#for i in a:
    #if a[i]['math_score']>=80 and a[i]['english_score']>=80 and a[i]['chinese_score']>=80:
        #print(i)
        
        
        
        
        
        
        
        
        
###### 课后作业


### 一、阅读程序题


#1.
  #（1）18,10,14
  #（2）
#data = [3, 8, 1, 9, 5, 2, 7]
#result = []
#for i in range(len(data)):
    #if data[i] % 2 == 0 and data[i] < 5:
        #result.append(data[i])
#print (result)


#2.
  #（1）业务逻辑错误，因为钱二本身的数学成绩是45，不符合三科>60的成绩，所以钱二本就不应该出现在结果里
  #（2）
#students = {
    #"赵一": {"math": 85, "english": 58, "chinese": 92},
    #"钱二": {"math": 45, "english": 73, "chinese": 68},
    #"孙三": {"math": 91, "english": 86, "chinese": 79},
#}
#for name in students:
    #s = students [name]
    #m,e,c = s ["math"], s ["english"], s ["chinese"]
    #if (m >= 80 and e >= 80) or (m >= 80 and c >= 80) or (e >= 80 and c >= 80):
        #print(name + "合格")
  #（3）可能是单词拼写不一致，或者中英文引号混用


#3.
  #（1）李四，王五，赵六
  #（2）根据德摩根定律，not (A and B) 是 not A or not B 的意思（两者至少有一个不成立）
  #（3）
#a = [
    #["张三", 170, "男", 16],
    #["李四", 165, "女", 17],
    #["王五", 180, "男", 15],
    #["赵六", 158, "女", 18],
#]
#for i in range(len(a)):
    #if (a[i][2] == "男" or a[i][3] >= 17):
        #print(a[i][0])


### 二、写程序题


#1.
#scores = [56, 78, 92, 45, 83, 67, 91, 38, 74, 88]
#names  = ["赵一", "钱二", "孙三", "李四", "周五", "吴六", "郑七", "王八", "冯九", "陈十"]
#print ("(1)每位同学的姓名和成绩：")
#for name, score in zip (names, scores):
    #print (f"{name}: {score}分")
#excellent = 0
#fail = 0
#for i in scores: 
    #if i >= 80:
        #excellent += 1
    #elif i < 60:
        #fail += 1
#print ("\n(2)优秀&不及格人数统计：")
#print (f"成绩≥80的优秀人数：{excellent}")
#print (f"成绩<60的不及格人数：{fail}")
#max_score = -1
#max_name = ""
#for name, score in zip (names, scores):
    #if score > max_score:
        #max_score = score
        #max_name = name
#print ("\n(3)最高分同学：")
#print (f"{max_name}: {max_score}分")
#average_score = sum (scores) / len (scores)
#print (f"\n(4)平均分：{average_score}, 低于平均分的同学：")
#for name, score in zip (names, scores):
    #if score < average_score:
        #print (name)
        
        
#2.
#employees = {
    #"A001": {"name": "张伟", "dept": "技术部", "salary": 8500, "age": 28},
    #"A002": {"name": "李娜", "dept": "市场部", "salary": 7200, "age": 32},
    #"A003": {"name": "王强", "dept": "技术部", "salary": 9300, "age": 25},
    #"A004": {"name": "赵敏", "dept": "人事部", "salary": 6800, "age": 35},
    #"A005": {"name": "陈晨", "dept": "技术部", "salary": 8100, "age": 29},
#}
#print ("=====(1)技术部所有员工姓名和工资=====")
#for emp_info in employees.values ():
    #if emp_info ["dept"] == "技术部":
        #print (f"姓名：{emp_info['name']}, 工资：{emp_info ['salary']}")
#print ("=====(2)市场部&人事部平均工资=====")
#market_salaries = []
#hr_salaries = []
#for emp_info in employees.values ():
    #if emp_info ["dept"] == "市场部":
        #market_salaries.append (emp_info ["salary"])
    #elif emp_info ["dept"] == "人事部":
        #hr_salaries.append (emp_info ["salary"])
#average_market = sum (market_salaries) / len (market_salaries)
#average_hr = sum (hr_salaries) / len (hr_salaries)
#print (f"市场部平均工资：{average_market:.2f}")
#print (f"人事部平均工资：{average_hr:.2f}")
#print ("=====(3)工资最高的员工=====")
#max_salary = -1
#max_emp = None
#for emp_info in employees.values ():
    #if emp_info ["salary"] > max_salary:
        #max_salary = emp_info ["salary"]
        #max_emp = emp_info
#print (f"姓名：{max_emp['name']}, 部门：{max_emp['dept']}")
#print ("=====(4)工资高于本部门平均工资的员工=====")
#dept_sal = {}
#for emp_info in employees.values ():
    #dept = emp_info ["dept"]
    #sal = emp_info ["salary"]
    #if dept not in dept_sal: 
        #dept_sal [dept] = []
    #dept_sal [dept].append (sal)
#dept_avg = {}
#for dept, sal_list in dept_sal.items ():
    #dept_avg [dept] = sum (sal_list) / len (sal_list)
#for emp_info in employees.values ():
    #dept = emp_info ["dept"]
    #sal = emp_info ["salary"]    
    #if sal > dept_avg [dept]:
        #print (emp_info ["name"])
        

#3.
#nums = [12, 5, 8, 21, 3, 17, 9, 14, 6, 11]
#print ("（1）大于10的数：", [x for x in nums if x > 10])
#print ("\n（2）能被3整除的数：", [x for x in nums if x % 3 == 0])
#print ("\n（3）每个数的平方：", [x*x for x in nums])
#print ("\n（4）大于10且是偶数的数：", [x for x in nums if x > 10 and x % 2 == 0])


#4.
#students = {
    #"zhangsan": {"gender": "male",   "height": 180, "weight": 60, "score": 285, "class": 3},
    #"lisi":     {"gender": "female", "height": 160, "weight": 50, "score": 270, "class": 1},
    #"wangwu":   {"gender": "female", "height": 170, "weight": 65, "score": 250, "class": 2},
    #"zhaoliu":  {"gender": "male",   "height": 175, "weight": 70, "score": 295, "class": 1},
    #"sunqi":    {"gender": "male",   "height": 168, "weight": 58, "score": 260, "class": 3},
#}
#class_count =  {1 : 0, 2 : 0, 3 : 0}
#class_total =  {1 : 0, 2 : 0, 3 : 0}
#for name, info in students.items ():
    #cls = info ["class"]
    #score = info ["score"]
    #class_count [cls] += 1
    #class_total [cls] += score
#print ("（1）各班人数")
#print (f"1班：{class_count [1]}人")
#print (f"2班：{class_count [2]}人")
#print (f"3班：{class_count [3]}人")
#avg1 = class_total [1] / class_count [1]
#avg2 = class_total [2] / class_count [2]
#avg3 = class_total [3] / class_count [3]
#class_avg = {1 : avg1, 2 : avg2, 3 : avg3}
#print ("\n（2）各班平均分")
#print (f"1班平均分：{avg1:.1f}")
#print (f"2班平均分：{avg2:.1f}")
#print (f"3班平均分：{avg3:.1f}")
#max_score = -1
#top_name = ""
#for name, info in students.items ():
    #if info ["score"] > max_score:
            #max_score = info ["score"]
            #top_name = name
#print ("\n（3）全校最高分")
#print (f"{top_name}，分数：{max_score}")
#print ("\n（4）高于本班平均分的学生")
#for name, info in students.items ():
    #cls = info ["class"]
    #if info ["score"] > class_avg [cls]:
        #print (name)
#rank = sorted (students.items(), key = lambda x : x[1]["score"], reverse = True)
#print ("\n（5）总分排名前三")
#for i in range (3):
    #name, info = rank [i]
    #print (f"第{i + 1}名：{name}，分数：{info ['score']}")


### 三、代码改错题
        
        
#1.
  #（1）因为用了三个独立的if，而不是互斥判断，这样当第一个if成立时，第二个if不成立，就会执行后面的else，导致zero也跟着加一。应该用if-elif-else来分支
  #（2）
#numbers = [3, -1, 0, 5, -2, 0, 8, -4]
#pos = 0
#neg = 0
#zero = 0
#for i in range(len(numbers)):
    #if numbers[i] > 0:
        #pos = pos + 1
    #elif numbers[i] < 0:
        #neg = neg + 1
    #else:
        #zero = zero + 1
#print (pos, neg, zero)
  #（3）
#numbers = [3, -1, 0, 5, -2, 0, 8, -4]
#pos = 0
#neg = 0
#zero = 0
#for i in numbers:
    #if i > 0:
        #pos += 1
    #elif i < 0:
        #neg += 1
    #else:
        #zero += 1
#print (pos, neg, zero)


#2.
  #（1）IndexError
  #（2）当循环到最后一次，i等于5的时候，i+1等于6，而列表下标只有5，超出了索引范围
  #（3）
#data = [4, 7, 2, 9, 5, 8]
#max_sum = 0
#for i in range(len(data)-1):
    #s = data[i] + data[i+1]
    #if s > max_sum:
        #max_sum = s
#print (max_sum)


### 四、加分彩蛋题


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (sum (x*x for x in nums if x % 2 == 1))
print ([x for x in nums if x % 3 == 0 or x % 5 == 0])