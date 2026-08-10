#各科平均分	哪科平均分最高→说明这科学生普遍学得好；哪科最低→说明这科最难
#各科最高分/最低分	各科有没有满分？最低分在哪科？
#各科及格率	哪科及格率最高？哪科不及格的人最多？
#各科优秀率（≥90分）	哪科容易拿高分？哪科尖子生少？
#各科标准差	标准差大→说明这科学生两极分化严重；标准差小→说明大家水平差不多
#可以筛选什么？

#各科满分的学生名单

#各科不及格的学生名单（需要补考）

#各科前10名的学生名单

#各科后10名的学生名单

#可以判断什么？

#哪个班偏科最严重（某一科平均分特别低，和其他科差距大）

#哪个班各科最均衡（各科平均分差距小）

#哪个班尖子生最多（总分≥某个分数的人数最多）

#三、性别对比分析
#可以计算什么？
#计算内容	能得出什么结论
#男生/女生各科平均分	男生擅长理科还是文科？女生擅长理科还是文科？
#男生/女生总分平均分	整体上男生成绩好还是女生成绩好？
#男生/女生在各科的及格率	哪科男生及格率高？哪科女生及格率高？
#可以筛选什么？
#男生前10名 / 女生前10名

#男生各科最高分 / 女生各科最高分

#可以筛选什么？
#按姓名找某个学生的所有信息

#按学号找某个学生的所有信息

#按班级找某个班的所有学生

#按性别找所有男生/女生

#可以判断什么？
#某学生各科成绩怎么样？

#某学生总分在全年级什么水平？

#某学生哪科强、哪科弱？

import pandas
info = pandas.read_csv('学生信息数据.csv', encoding = 'utf-8')
a = ['数学', '语文', '英语', '物理', '化学', '生物']
##各科平均分，最高分，最低分，标准差
#for i in range(len(a)):   
    #subject_avg = info[a[i]].mean()
    #subject_max = info[a[i]].max()
    #subject_min = info[a[i]].min()
    #standard = info[a[i]].std()
    #print('{}:avg = {}  max = {}  min={}  standard={:.2f}'.format(a[i],subject_avg,subject_max,subject_min,standard))

##各科及格率
#for i in range(len(a)):
    #pass_rate = (info[a[i]]>=60).sum()/len(info)*100
    #print('{}: pass_rate = {}%'.format(a[i], pass_rate))

##各科优秀率（≥90分）
#for i in range(len(a)):
    #excellence_rate = (info[a[i]]>=90).sum()/len(info)*100
    #print('{}: excellence_rate = {}%'.format(a[i], excellence_rate))

##数学最高分的学生名单
#info['姓名'][info[a[0]].max() == info[a[0]]]
#数学最高分的学生人数
#len(info['姓名'][info[a[0]].max() == info[a[0]]])

##各科满分的学生名单
#info['姓名'][info[a[i]] == 100]

##各科不及格的学生名单（需要补考）
#info['姓名'][info[a[i]] < 60]

##各科前10名的学生名单
#info.sort_values(a[0],ascending = False)[:10]   #False是降序
#info.sort_values(a[0],ascending = False)['姓名'][:10]


##各科后10名的学生名单
#info.sort_values(a[0],ascending = True)['姓名'][:10]
