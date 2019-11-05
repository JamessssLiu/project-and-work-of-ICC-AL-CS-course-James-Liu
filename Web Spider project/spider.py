import urllib.request as urlrequest
from urllib import request
import requests
import random
import codecs
from bs4 import BeautifulSoup as bs
import collections
import numpy as np
import panda as pd
import jieba
import wordcloud
import operator
from functools import reduce
from PIL import Image
import matplotlib.pyplot as plt

def GetContent(url,headers):
	randdom_header=random.choice(headers)
	req=urlrequest.Request(url)
	req.add_header("User-Agent",randdom_header)
	req.add_header("Host","blog.csdn.net")
	req.add_header("Referer","http://blog.csdn.net/")
	req.add_header("GET",url)
	content=request.urlopen(req).read().decode('utf-8')
	return content


def getComments(pageNum):
    Comment=[]
    Date=[]
    if pageNum > 0:
        start=(pageNum-1) * 20
    else:
        return False
    url='https://movie.douban.com/subject/32659890/comments' + \
        '?start=' + str(start) + '&limit=20&sort=new_score&status=P'

    res=requests.get(url)
    res.encoding=('utf-8')
    html_data=res.text
    soup=bs(html_data, 'html.parser') 
    comment_div_lits=soup.find_all('div', class_='comment')
    for item in comment_div_lits:
        if item.find_all('p'):
            Comment.append(item.find_all('span', class_='short')[0].string)
            tmpDate=item.find_all('span')[-2].string
            Date.append(tmpDate)
    return Comment,Date


def textprocessing():
    commentList=[]
    dateList=[]
    for i in range(10):
        num=i + 1
        [commentList_temp, dateList_temp] = getComments(num)
        commentList.append(commentList_temp)
        dateList.append(dateList_temp)
    commentList=reduce(operator.add, commentList)
    dateList=reduce(operator.add, dateList)

    dataTmp={'comments': commentList[:], 'date': dateList[:]}
    df2=pd.DataFrame(dataTmp)
    pd.DataFrame(df2).to_excel("text-movie.xls",sheet_name="sheet1", index=False, header=True)

    comments=''
    for k in range(len(commentList)):
        comments=comments+(str(commentList[k])).strip()

    pattern=re.compile(r'[\u4e00-\u9fa5]+')
    filterdata=re.findall(pattern, comments)  # 过滤标点 用正则表达式
    cleaned_comments=''.join(filterdata)

    seg_list_exact=jieba.cut(cleaned_comments, cut_all = False) # 精确模式分词
    object_list=[]
    remove_words=pd.read_csv("stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],encoding='utf-8')


    for word in seg_list_exact: # 循环读出每个分词
        if word not in remove_words: # 如果不在去除词库中
            object_list.append(word) # 分词追加到列表

    # 词频统计
    word_counts=collections.Counter(object_list) # 对分词做词频统计
    word_counts_top10=word_counts.most_common(10) # 获取前10最高频的词
    print (word_counts_top10) # 输出检查

    # 词频展示
    mask=np.array(Image.open('background.jpg')) # 定义词频背景
    wc=wordcloud.WordCloud(
        background_color='white', # 设置背景颜色
        font_path='/System/Library/Fonts/Hiragino Sans GB.ttc', # 设置字体格式
        mask=mask, # 设置背景图
        max_words=200, # 最多显示词数
        max_font_size=100 , # 字体最大值
        scale=32  # 调整图片清晰度，值越大越清楚
    )

    wc.generate_from_frequencies(word_counts) # 从字典生成词云
    image_colors=wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
    wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
    wc.to_file("/Users/ownpro/Desktop/temp.jpg") # 将图片输出为文件
    plt.imshow(wc) # 显示词云
    plt.axis('off') # 关闭坐标轴
    plt.show() # 显示图像

textprocessing()