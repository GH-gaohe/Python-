import requests,json
import os
import traceback
import pandas

url = 'https://datacenter.eastmoney.com/securities/api/data/v1/get?reportName=RPT_USF10_FN_GMAININDICATOR&columns=USF10_FN_GMAININDICATOR&quoteColumns=&filter=(SECUCODE%3D%22NVDA.O%22)(REPORT_TYPE%20in%20(%222025%2FFY%22%2C%222024%2FFY%22%2C%222023%2FFY%22%2C%222022%2FFY%22%2C%222021%2FFY%22%2C%222020%2FFY%22))&pageNumber=1&pageSize=6&sortTypes=-1&sortColumns=REPORT_DATE&source=SECURITIES&client=PC&v=039298222898451274'

try:
    page = requests.get(url)
    info = json.loads(page.text)
    for i in info['result']['data']:
        for j in i:
            with open("英伟达年报.csv", "a", encoding = 'gbk') as file:
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