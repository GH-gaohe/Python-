import requests,json
import os
import traceback
import pandas

url = 'https://datacenter.eastmoney.com/securities/api/data/get?type=RPT_F10_US_DETAIL&params=NVDA.O&p=1&source=SECURITIES&client=SW&v=08457534151972169'

try:
    page = requests.get(url)
    info = json.loads(page.text)
    for i in info['data']:
        for j in i:
            for k in j:
                with open("英伟达公司大事.csv", "a", encoding = 'gbk') as file:
                    file.write('{},{}\n'.format(k, j[k]))
        
    
    print("文件已保存到文件夹")


except requests.exceptions.ConnectionError:
    print("错误：网络连接失败！无法访问股票数据接口")
    print("解决办法：切换手机热点/关闭代理加速器/更换网络重试")
except requests.exceptions.Timeout:
    print("错误：请求超时，网页加载太慢，请换网络")
except Exception as e:
    print("程序出错：", e)
    print("完整错误位置：")
    traceback.print_exc()