#函数的作用：实现某种特定的功能
#函数分为 
#内置函数(已经实现具有特定意义函数) 
#常见的内置函数 max(),min(),pow(a,b),abs()....
#自定义函数 (还没有这个功能，是需要我们手动创建这个功能)
#计算多个数字的求和  
#判断奇偶数
#判断质数
#分解质因数

#数据类型概念
#存储数据的不同形式 用不同的容器存储不同的数据 
#[] 列表  list
#{} 字典  dict
#() 元组  tuple

#def sum(a):
    #s = 0
    #for i in range(len(a)):
        #s = s + a[i]
    #return s


#def odd_even(a):
    #if a%2==1:
        #return True
    #else:
        #return False

#def prime_num(a):
    ##质数定义1： 除2和它本身以外 没有其他因数 如果有其他因数 就不是质数
    ##质数定义2：只有两个因数
    #c = 0
    #for i in range(1,a+1):
        #if a%i==0:
            #c=c+1
    #if c==2:
        #return True
    #else:
        #return False

#文件读写
#r 读文件  
#w 写文件  会覆盖之前数据 
#如果在读取文件中存在中文汉字就需要写编码格式
#utf-8
#gbk
#open("文件路径+文件名","文件权限","文件的编码格式")

#file = open('数据分析第3课文件读写.txt','r',encoding='utf-8')
#info = file.readlines()  #获得文件信息
#for i in info:
    #print(i)

#file.close()


#with open('数据分析第3课文件读写.txt','a',encoding='utf-8') as file:
    #file.writelines("tom,女,20\n")


#import csv

#try:
    #with open('"C:\Users\93239\Desktop\脑电测试\22.csv"','r',encoding='gbk') as file:
        #info = csv.reader(file) # 用csv读取这个文件
        #for i in info:
            #print(i)
#except:
    #print('文件读取失败，请注意文件路径是否正确')









##### 课后作业


#1.
  #（1）12 28 56
  #（2）calc(12)的计算过程是：
       #n = 12，i = 1~13，不包含13的12个整数。用12（也就是n）以此除以 i 的值，如果商为0，那么result叠加得到的商。calc(12)得到的数是1,2,3,4,6,12，加在一起可得28
  #（3）calc(1)的结果是1
#def calc(n):
    #result = 0
    #for i in range(1, n + 1):
        #if n % i == 0:
            #result = result + i
    #return result
 
#a = 12
#b = calc(a)
#c = calc(b)
 
#print(a, b, c)


#2.
#def is_perfect(n):
    #sum_factor = 0
    #for i in range(1,n):
        #if n % i == 0:
            #sum_factor += i
    #return sum_factor == n

#print(is_perfect(6))
#print(is_perfect(12))
#print(is_perfect(28))


#3.
#def is_perfect(n):
    #sum_factor = 0
    #for i in range(1, n):
        #if n % i == 0:
            #sum_factor += i
    #return sum_factor == n

#perfect_list = []

#for num in range(1,100):
    #if is_perfect(num):
        #perfect_list.append(num)

#print(f"100以内的完数有：{perfect_list}")


#4.
#a = []  #代表所有数字
#b = []  #代表奇数数字
#c = []  #代表质数数字
#with open('C:/Users/m1861/Desktop/Python数据分析学习/numbers.txt','r',encoding='utf-8') as file:
    #info = file.readlines()
    #for i in info:
        #a.append(int(i.strip('\n')))
#print(a)
#print(len(a))

#def odd_even(c):
    #if c%2==1:
        #return True 
    #else:
        #return False
#def prime_num(k):
    #for i in range(2,k):
        #if k%i==0:
            #return False 
    #return True

#for i in a:
    #odd = odd_even(i)
    
    #prime = prime_num(i)
    
    #if odd==True:
        #b.append(i)
        
    #if prime==True:
        #c.append(i)
#print(b)
#print(len(b))
#print(c)
#print(len(c))