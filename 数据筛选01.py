import pandas
file = pandas.read_csv("好友信息.csv",encoding='gbk')
##file.transpose()  转换表格 的行和列
##此文件 是qq好友信息
##具有姓名 性别 qq号 qq网址 星座 空间访问状态数据
##所有好友中性别的个数 男的个数  女的个数  为展示的个数
##file['列名']   获取当前列数据
##a = file.columns  #获得所有列名
##file['性别'].value_counts()  查看种类的个数
#gender_file = file[file['性别']=='无']
#open_file = gender_file[gender_file['open']==True]
#open_file.to_csv("open_file.csv",encoding='gbk')



#import pandas
#file = pandas.read_csv('好友信息.csv', encoding = 'gbk')
#xz = file['星座'].value_counts()
#for i in range(xz.count()):
    #xzname = xz.index[i]
    #xznum = xz.iloc[i]
    #print(xzname,xznum)



##1. 性别统计：人数+占比
#gender = file['性别'].value_counts()
#total = len(file)
#print("=====性别统计=====")
#for name,num in zip(gender.index,gender.values):
    #rate = num / total * 100
    #print(f"{name}：{num}人，占比{rate:.2f}%")



##2. 星座统计：去缺失，输出全部+前三
#xz = file['星座'].value_counts(dropna=True)
#print("\n=====各星座人数=====")
#for i in range(xz.count()):
    #xzname = xz.index[i]
    #xznum = xz.iloc[i]
    #print(xzname,xznum)
#print("\n=====人数前三星座=====")
#top3 = xz.head(3)
#for i in range(3):
    #print(top3.index[i],top3.iloc[i])



##3. open空间访问 True/False 人数+占比
#open_data = file['open'].value_counts()
#print("\n=====空间访问状态=====")
#for flag,num in zip(open_data.index,open_data.values):
    #rate = num / total * 100
    #print(f"open={flag}：{num}人，占比{rate:.2f}%")



#4. 年龄：均值、中位数、最大、最小
# 清理无效年龄
##1.清除年龄中的无和字符串岁
#age_clean=file['年龄'].replace('无',numpy.nan) 
#age_clean = age_clean.str.strip().str.replace('岁','')
#age = pandas.to_numeric(age_clean).dropna()
#print("\n=====年龄统计=====")
#print("平均值：", age.mean())
#print("中位数：", age.median())
#print("最大值：", age.max())
#print("最小值：", age.min())