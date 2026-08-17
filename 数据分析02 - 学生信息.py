#各科平均分	哪科平均分最高→说明这科学生普遍学得好；哪科最低→说明这科最难
#各科最高分/最低分	各科有没有满分？最低分在哪科？
#各科及格率	哪科及格率最高？哪科不及格的人最多？
#各科优秀率（≥90分）	哪科容易拿高分？哪科尖子生少？
#各科标准差	标准差大→说明这科学生两极分化严重；标准差小→说明大家水平差不多


#各科满分的学生名单

#各科不及格的学生名单（需要补考）

#各科前10名的学生名单

#各科后10名的学生名单


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



#作业

#import pandas
#info = pandas.read_csv('学生信息数据.csv', encoding='utf-8')
#a = ['数学', '语文', '英语', '物理', '化学', '生物']
#class_list = info['班级'].unique()

## 若CSV中没有总分列，则计算总分
#if '总分' not in info.columns:
    #info['总分'] = info[a].sum(axis=1)


### 哪个班偏科最严重（某一科平均分特别低，和其他科差距大）
## 思路：计算每个班各科平均分，找出最低分科目与各科平均分的差距，差距越大偏科越严重
#print('=====各班偏科情况=====')
#class_bias_gap = {}
#for c in class_list:
    #class_data = info[info['班级'] == c]
    #subject_avg = [class_data[a[i]].mean() for i in range(len(a))]
    #min_index = subject_avg.index(min(subject_avg))
    #min_subject = a[min_index]
    #min_score = subject_avg[min_index]
    #avg_of_all = sum(subject_avg) / len(subject_avg)
    #gap = avg_of_all - min_score
    #class_bias_gap[c] = gap
    #print('{}: 最低分科目={}({:.2f}), 各科平均={:.2f}, 差距={:.2f}'.format(
        #c, min_subject, min_score, avg_of_all, gap))
#most_biased_class = max(class_bias_gap, key=class_bias_gap.get)
#print('偏科最严重的班级：{}'.format(most_biased_class))


### 哪个班各科最均衡（各科平均分差距小）
## 思路：用各科平均分的标准差衡量，标准差越小说明各科越均衡
#print('\n=====各班各科均衡度=====')
#class_balance = {}
#for c in class_list:
    #class_data = info[info['班级'] == c]
    #subject_avg = [class_data[a[i]].mean() for i in range(len(a))]
    #std_of_avgs = pandas.Series(subject_avg).std()
    #class_balance[c] = std_of_avgs
    #print('{}: 各科平均分标准差={:.2f}'.format(c, std_of_avgs))
#most_balanced_class = min(class_balance, key=class_balance.get)
#print('各科最均衡的班级：{}'.format(most_balanced_class))


### 哪个班尖子生最多（总分≥某个分数的人数最多）
#score_threshold = 500   # 总分≥500视为尖子生，可按实际情况调整
#print('\n=====各班尖子生人数(总分≥{})====='.format(score_threshold))
#class_top_count = {}
#for c in class_list:
    #class_data = info[info['班级'] == c]
    #top_count = (class_data['总分'] >= score_threshold).sum()
    #class_top_count[c] = top_count
    #print('{}: 尖子生{}人'.format(c, top_count))
#most_top_class = max(class_top_count, key=class_top_count.get)
#print('尖子生最多的班级：{}'.format(most_top_class))


### 三、性别对比分析
## 可以计算什么 → 计算内容 → 能得出什么结论

### 男生/女生各科平均分 → 男生擅长理科还是文科？女生擅长理科还是文科？
#print('\n=====男生各科平均分=====')
#male_data = info[info['性别'] == '男']
#female_data = info[info['性别'] == '女']
#male_avg = {}
#female_avg = {}
#for i in range(len(a)):
    #male_avg[a[i]] = male_data[a[i]].mean()
    #female_avg[a[i]] = female_data[a[i]].mean()
    #print('{}: {:.2f}'.format(a[i], male_avg[a[i]]))
#print('\n=====女生各科平均分=====')
#for i in range(len(a)):
    #print('{}: {:.2f}'.format(a[i], female_avg[a[i]]))

## 对比男女各科平均分，判断优势科目
#print('\n=====男女各科优势对比=====')
#science = ['数学', '物理', '化学', '生物']
#arts = ['语文', '英语']
#male_science_avg = sum(male_avg[s] for s in science) / len(science)
#female_science_avg = sum(female_avg[s] for s in science) / len(science)
#male_arts_avg = sum(male_avg[s] for s in arts) / len(arts)
#female_arts_avg = sum(female_avg[s] for s in arts) / len(arts)
#for i in range(len(a)):
    #diff = male_avg[a[i]] - female_avg[a[i]]
    #if diff > 0:
        #print('{}: 男生比女生高 {:.2f}分'.format(a[i], diff))
    #elif diff < 0:
        #print('{}: 女生比男生高 {:.2f}分'.format(a[i], abs(diff)))
    #else:
        #print('{}: 男女持平'.format(a[i]))
#print('男生理科均分={:.2f}, 文科均分={:.2f}'.format(male_science_avg, male_arts_avg))
#print('女生理科均分={:.2f}, 文科均分={:.2f}'.format(female_science_avg, female_arts_avg))


### 男生/女生总分平均分 → 整体上男生成绩好还是女生成绩好？
#print('\n=====男女总分平均分=====')
#male_total_avg = male_data['总分'].mean()
#female_total_avg = female_data['总分'].mean()
#print('男生总分平均分: {:.2f}'.format(male_total_avg))
#print('女生总分平均分: {:.2f}'.format(female_total_avg))


### 男生/女生在各科的及格率 → 哪科男生及格率高？哪科女生及格率高？
#print('\n=====男生各科及格率=====')
#for i in range(len(a)):
    #pass_rate = (male_data[a[i]] >= 60).sum() / len(male_data) * 100
    #print('{}: {:.1f}%'.format(a[i], pass_rate))
#print('\n=====女生各科及格率=====')
#for i in range(len(a)):
    #pass_rate = (female_data[a[i]] >= 60).sum() / len(female_data) * 100
    #print('{}: {:.1f}%'.format(a[i], pass_rate))


### 可以筛选什么？→ 男生前10名 / 女生前10名
#print('\n=====男生总分前10名=====')
#male_top10 = male_data.sort_values('总分', ascending=False)[:10]
#print(male_top10[['姓名', '班级', '总分'] + a])

#print('\n=====女生总分前10名=====')
#female_top10 = female_data.sort_values('总分', ascending=False)[:10]
#print(female_top10[['姓名', '班级', '总分'] + a])



#info['物理'].corr(info['化学'])   计算物理和化学的相关性
#info.groupby('班级')['数学'].mean()   对班级进行分组，计算出每个班级的数学平均成绩