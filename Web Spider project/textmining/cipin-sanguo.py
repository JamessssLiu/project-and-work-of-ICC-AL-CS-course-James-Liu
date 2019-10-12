# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:00:45 2018
reference: https://www.cnblogs.com/A9kl/p/9311246.html 
@author: rdfz-411
"""

import jieba

content = open('三国演义.txt', 'r',encoding='utf-8').read()
words =jieba.lcut(content)#分词
excludes={"将军","却说","二人","后主","上马","不知","天子","大叫","众将","不可","主公","蜀兵","只见","如何","商议","都督","一人","汉中","不敢","人马","陛下","魏兵","天下","今日","左右","东吴","于是","荆州","不能","如此","大喜","引兵","次日","军士","军马"}#排除的词汇
words=jieba.lcut(content)
counts={}

for word in words:
    if len(word) == 1: # 排除单个字符的分词结果
        continue
    elif word == '孔明' or word == '孔明曰':
       real_word = '孔明'
    elif word == '关公' or word == '云长':
       real_word = '关羽'
    elif word == '孟德' or word == '丞相':
       real_word = '曹操'
    elif word == '玄德' or word == '玄德曰':
       real_word = '刘备'
    else:
        real_word =word
        counts[word] = counts.get(word, 0) + 1



for word in excludes:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))