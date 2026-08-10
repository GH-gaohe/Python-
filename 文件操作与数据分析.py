#1. 
#scores = []
#with open("scores.txt","r",encoding="utf-8") as f:
    #for i in f:
        #name,score = i.strip().split(",")
        #scores.append(int(score))

#total = sum(scores)
#avg = total/len(scores)
#high = max(scores)
#low = min(scores)

#with open("score_report.txt","w",encoding="utf-8") as f:
    #f.write(f"总分: {total}.0\n平均分: {avg:.2f}\n最高分: {high}\n最低分: {low}")
    
#print("文件已保存")



2. 
def read_sale(filename):
    with open(filename,"r",encoding="utf-8") as f:
        return [int(i.strip().split(",")[1]) for i in f.readlines()[1:]]

s24 = read_sale("sales_2024.txt")
s25 = read_sale("sales_2025.txt")
sum24,sum25 = sum(s24),sum(s25)

with open("sales_total.csv","w",encoding="gbk") as f:
    f.write("月份,2024年销售额,2025年销售额,两年合计\n")
    for i in range(12):
        total = s24[i]+s25[i]
        f.write(f"{i+1},{s24[i]},{s25[i]},{total}\n")
    f.write(f"总计,{sum24},{sum25},{sum24+sum25}")
    
print("文件已保存")



#3. 
#cnt = 0
#stat = {"200":0,"404":0,"500":0}
#total_byte = 0
#max_data = [0,"",""]

#with open("server.log","r",encoding="utf-8") as f:
    #for line in f.readlines()[1:]:
        #ip,t,_,code,b = line.strip().split(",")
        #b = int(b)
        #cnt += 1
        #if code in stat:
            #stat[code] += 1
        #total_byte += b
        #if b > max_data[0]:
            #max_data = [b,ip,t]

#kb = total_byte / 1024

#res = f"""========== 日志分析报告 ==========
#总请求数: {cnt}
#状态码统计:
  #200: {stat['200']} 次
  #404: {stat['404']} 次
  #500: {stat['500']} 次
#总响应大小: {total_byte} 字节 ({kb:.2f} KB)
#最大响应请求:
  #IP: {max_data[1]}
  #时间: {max_data[2]}
  #响应大小: {max_data[0]} 字节
#==================================="""

## 写入文件
#with open("analysis_report.txt","w",encoding="utf-8") as f:
    #f.write(res)
#print(res)