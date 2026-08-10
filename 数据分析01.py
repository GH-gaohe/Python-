#数据分析
#数据获取 requests
#数据整理和清洗  pandas    numpy
#数据展示   matplotlib    numpy

import matplotlib.pyplot as py  #选择数据可视化模块
import numpy   #python的数字库

#先创建一个画布
py.figure(figsize=(8,6))
x = numpy.linspace(-50,50,100) #在-50 到 50 之间选择一个100个点
y = 3 * x
y1 = 5 / x
y2 = 10 * x + 50


py.subplot(1,3,1)  #将画布分成(x,y,n)  x行y列 处于第n位
py.plot(x,y,color='red')
py.title('y = 3 * x')
py.grid()  #展示网格

py.subplot(1,3,2)  #将画布分成(x,y,n)  x行y列 处于第n位
py.plot(x,y1,color='red')
py.title('y1 = 5 / x')
py.grid()  #展示网格

py.subplot(1,3,3)  #将画布分成(x,y,n)  x行y列 处于第n位
py.plot(x,y2,color='red')
py.title('y2 = 10 * x + 50')
py.grid()  #展示网格

py.show()  #显示画布