import requests,json
import os
import traceback
import pandas

url = 'https://push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery35105522835829774964_1784527219688&secid=0.002594&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&end=20500101&lmt=120&_=1784527219697'

c = {'cookie' : 'qgqp_b_id=5859821f8b071d285cbb7284c522ff5e; st_nvi=5QRb0vxFLr5vMODMbxIngb2d8; nid18=00363af0e7b106483ee978d823fdff2f; nid18_create_time=1783920107321; gviem=r7_IxwVNUmY8KZSiKkmd179d5; gviem_create_time=1783920107321; st_si=19963365809425; fullscreengg=1; fullscreengg2=1; st_asi=delete; st_pvi=40213891693717; st_sp=2026-07-13%2001%3A21%3A47; st_inirUrl=https%3A%2F%2Fcn.bing.com%2F; st_sn=45; st_psi=20260720020002572-113200301201-1845288898'}

h = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0'}

column = '日期,今开, 今收, 今天最高, 今天最低, 成交量, 成交额, 振幅,涨跌百分比开始值, 涨跌百分比的结束值, 换手率'

try:
    
    with open("比亚迪日K线.csv", "w", encoding = 'gbk') as file:
        file.write('{}\n'.format(column))    
    
    
    
    page = requests.get(url, cookies = c, headers = h)
    info = json.loads(page.text[41:-2])
    
    for i in info['data']['klines']:
        with open("比亚迪日K线.csv", "a", encoding = 'gbk') as file:
            file.write('{}\n'.format(i))
        
    
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