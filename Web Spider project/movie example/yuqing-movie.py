# -*- coding: utf-8 -*-
"""
Created on Tue May  1 14:09:32 2018

@author: rdfz-411

提示： 程序运行--
0. 在程序第26行，输入要进行舆情时间序列可视化的数据文件，默认是"text-movie.xls"
1. 点击工具栏 “运行” 绿色小箭头运行本程序

2. 请在右侧IPython console中 输入%pylab qt5，按回车键

3. 将下面的一行代码（本程序中的倒数第二行）粘贴到右侧IPython console中，
同时按下shift+回车，可以看到在新窗口中弹出图像，可以放大，可以保存,向前向后键可以撤回或者重做操作。
ggplot.ggplot(ggplot.aes(x="date", y="sentiment"), data=df) + ggplot.geom_point() + ggplot.geom_line(color = 'blue') + ggplot.scale_x_date(labels = ggplot.date_format("%Y-%m-%d"))

4. 将下面的一行代码（本程序中的倒数第二行）粘贴到右侧IPython console中，同时按下shift+回车，
df.sort_values(['sentiment'])[:5]
括号中的5可以修改，表示输入前多少个情感分析得分最低的影评
"""
#encoding:utf-8
import pandas as pd
from dateutil import parser
from snownlp import SnowNLP
import ggplot
import  matplotlib.pyplot   as plt
import pylab

#%pylab qt5   # 这行代码在右侧ipython console中输入

df = pd.read_excel("text-movie.xls")
df["date"] = df.date.apply(parser.parse)
print("#######################################")
print("打印所挖掘的文本文件 text-movie.xls 前几行")
print(df.head())

#text = df.comments.iloc[0]   单个影评情感分析实验， iloc中的index值表示第几个应用，编号从0开始
#s = SnowNLP(text)
#
#print(s.sentiments)

def get_sentiment_cn(text):
    s = SnowNLP(text)
    return s.sentiments


df["sentiment"] = df.comments.apply(get_sentiment_cn)
print("#######################################")
print("打印所挖掘的文本文件 text-movie.xls 部分影评及其情感分析值")
print(df)

print("#######################################")
print("重要信息")
print("所有影评的平均值为:", df.sentiment.mean())
print("所有影评的中位数为:",df.sentiment.median())

ggplot.ggplot(ggplot.aes(x="date", y="sentiment"), data=df) + ggplot.geom_point() + ggplot.geom_line(color = 'blue') + ggplot.scale_x_date(labels = ggplot.date_format("%Y-%m-%d"))

df.sort_values(['sentiment'])[:5]