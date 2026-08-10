#import requests as r 
#import json  #将字符串的字典外观转换成字典数据类型
#url = 'https://push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery351040199561996985234_1783662436507&secid=105.NVDA&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&end=20500101&lmt=120&_=1783662436514'

##网页传输原理：请求+响应的过程 
#page = r.get(url)  #发送请求
##因为page.text是一个字符串类型  所以我们需要把数据转换成字典的格式类型 就可以进行数据分析了 
##1.获取数据 
##2.对数据进行处理，删掉不用的脏数据
#info = page.text
#info = info[42:-2]
#info = json.loads(info)

#name = info['data']['name']
#klines = info['data']['klines']









##### 课后作业


import requests,json
import os
import traceback

url = 'https://push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery351040199561996985234_1783662436507&secid=105.NVDA&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&end=20500101&lmt=30&_=1783662436514'

try:
    page = requests.get(url, timeout=10)
    page.raise_for_status()

    info = page.text[42:-2]
    info = json.loads(info)
    klines = info['data']['klines'][-30:]  # 只保留近30个交易日
    name = info['data']['name']


    desktop = os.path.expanduser("~/Desktop")
    save_path = os.path.join(desktop, name+'日k数据表.txt')


    with open(save_path,'w',encoding='utf-8') as file:
        for i in klines:
            m = i.split(',')
            file.write('日期: {} ,今开: {}, 今收: {}, 今天最高: {}, 今天最低: {}, 成交量: {}, 成交额: {}, 振幅: {},涨跌百分比开始值: {}, 涨跌百分比的结束值: {}, 换手率: {}\n'.format(m[0],m[1],m[2],m[3],m[4],m[5],m[6],m[7],m[8],m[9],m[10]))

    print("文件已保存到桌面")

except requests.exceptions.ConnectionError:
    print("错误：网络连接失败！无法访问股票数据接口")
    print("解决办法：切换手机热点/关闭代理加速器/更换网络重试")
except requests.exceptions.Timeout:
    print("错误：请求超时，网页加载太慢，请换网络")
except Exception as e:
    print("程序出错：", e)
    print("完整错误位置：")
    traceback.print_exc()