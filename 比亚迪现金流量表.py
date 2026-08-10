import requests,json
import os
import traceback
import pandas

url = 'https://datacenter.eastmoney.com/securities/api/data/get?type=RPT_F10_FINANCE_GBALANCE&sty=F10_FINANCE_GBALANCE&filter=(SECUCODE%3D%22002594.SZ%22)(REPORT_DATE%20in%20(%272025-12-31%27%2C%272024-12-31%27%2C%272023-12-31%27%2C%272022-12-31%27%2C%272021-12-31%27))&p=1&ps=5&sr=-1&st=REPORT_DATE&source=HSF10&client=PC&v=09721681446909681'

try:
    page = requests.get(url)
    info = json.loads(page.text)
    for i in info['result']['data']:
        for j in i:
            with open("比亚迪现金流量表.csv", "a", encoding = 'gbk') as file:
                file.write('{},{}\n'.format(j, i[j]))
        
    
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





