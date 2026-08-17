#import pandas
#weather = pandas.read_csv('城市天气数据.csv',encoding = 'utf-8')

#a = weather.groupby('城市')['最高温(℃)'].max()   #每个城市的最高温度的最大值
#b = weather.groupby('城市')['最低温(℃)'].min()   #每个城市的最低温度的最小值

##筛选出温度差小于15的城市
#for i in range(len(b)):
    #if (a.iloc[i] - b.iloc[i] < 15):
        #print(a.index[i], a.iloc[i] - b.iloc[i])

##根据近一周的降水量排序，降水量前五的城市有哪些
#c = weather.groupby('城市')['降水量(mm)'].sum()
#c = c.sort_values(ascending = False)   
#print(c[:5])


#方差计算公式：先算出平均数，然后用每一个数减去平均数，最终得到的结果算平方和，最后再算平方和的平均数
#标准差计算公式：根号下方差


#作业


import pandas as pd

weather = pd.read_csv('城市天气数据.csv', encoding='utf-8')

print("=" * 60)
print("【作业一】城市温度分析")
print("=" * 60)

# 计算每个城市的平均最高温和平均最低温
avg_max_temp = weather.groupby('城市')['最高温(℃)'].mean().sort_values(ascending=False)
avg_min_temp = weather.groupby('城市')['最低温(℃)'].mean().sort_values(ascending=True)

print("\n各城市平均最高温排名（从高到低）：")
print(avg_max_temp.round(1))

print("\n各城市平均最低温排名（从低到高）：")
print(avg_min_temp.round(1))

# (1) 平均最高温排名前三的"最热城市"
print("\n(1) 平均最高温排名前三的'最热城市'：")
top3_hot = avg_max_temp.head(3)
for city, temp in top3_hot.items():
    print(f"   {city}: {temp:.1f}℃")

# (2) 平均最低温排名后三的"最冷城市"
print("\n(2) 平均最低温排名后三的'最冷城市'：")
bottom3_cold = avg_min_temp.head(3)
for city, temp in bottom3_cold.items():
    print(f"   {city}: {temp:.1f}℃")

# (3) 日温差平均值最大的城市
weather['日温差'] = weather['最高温(℃)'] - weather['最低温(℃)']
avg_temp_diff = weather.groupby('城市')['日温差'].mean().sort_values(ascending=False)
max_diff_city = avg_temp_diff.index[0]
max_diff_value = avg_temp_diff.iloc[0]
print(f"\n(3) 日温差平均值最大的城市：{max_diff_city}，平均日温差为 {max_diff_value:.1f}℃")


print("\n" + "=" * 60)
print("【作业二】天气状况统计")
print("=" * 60)

# 统计各种天气状况出现次数
weather_count = weather['天气状况'].value_counts()
print("\n各天气状况出现次数：")
print(weather_count)

# (1) 出现次数最多的天气
most_common_weather = weather_count.index[0]
most_common_count = weather_count.iloc[0]
print(f"\n(1) 出现次数最多的天气：{most_common_weather}，出现了 {most_common_count} 次")

# (2) 出现次数最少的天气
least_common_weather = weather_count.index[-1]
least_common_count = weather_count.iloc[-1]
print(f"(2) 出现次数最少的天气：{least_common_weather}，出现了 {least_common_count} 次")

# (3) "晴"天占总记录数的百分比
sunny_days = weather_count.get('晴', 0)  # 如果'晴'不存在则返回0
total_days = len(weather)
sunny_percentage = sunny_days / total_days * 100
print(f"(3) '晴'天占总记录数的 {sunny_percentage:.1f}%")


print("\n" + "=" * 60)
print("【作业三】雨天与非雨天 AQI 对比")
print("=" * 60)

# 分为雨天和非雨天
rainy_data = weather[weather['降水量(mm)'] > 0]
non_rainy_data = weather[weather['降水量(mm)'] == 0]

# (1) 记录数统计
rainy_count = len(rainy_data)
non_rainy_count = len(non_rainy_data)
print(f"\n(1) 雨天记录数：{rainy_count} 条")
print(f"   非雨天记录数：{non_rainy_count} 条")

# (2) 平均 AQI
rainy_avg_aqi = rainy_data['AQI'].mean()
non_rainy_avg_aqi = non_rainy_data['AQI'].mean()
diff = non_rainy_avg_aqi - rainy_avg_aqi
print(f"\n(2) 雨天平均 AQI：{rainy_avg_aqi:.1f}")
print(f"   非雨天平均 AQI：{non_rainy_avg_aqi:.1f}")
print(f"   两者相差：{diff:.1f}（非雨天 - 雨天）")

# (3) 判断下雨是否有助于改善空气质量
print(f"\n(3) 判断：")
if diff > 0:
    print(f"   ✅ 下雨有助于改善空气质量。雨天 AQI 比非雨天低 {diff:.1f}，说明雨水可以冲刷空气中的污染物。")
elif diff < 0:
    print(f"   ❌ 下雨可能不利于空气质量。雨天 AQI 比非雨天高 {abs(diff):.1f}。")
else:
    print(f"   ⚠️ 雨天和非雨天 AQI 几乎相同，下雨对空气质量无明显影响。")