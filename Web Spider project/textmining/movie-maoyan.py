import requests
import json
import time
import random

#下载一页数据
def get_one_page(url):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:  #页面正常响应
        return response.text # 返回页面源代码
    return None

#解析一页数据
def parse_ono_page(html):
    data = json.loads(html)['cmts'] #评论以json形式存储,故以json形式截取
    for item in data:
        yield{ #该方法返回一个字典
               'comment':item['content'],
               'date':item['time'].split(' ')[0],
               'rate':item['score'],
               'city':item['cityName'],
               'nickname':item['nickName']
              }

#保存数据到文本文档
def save_to_txt():
    for i in range(1, 3):
        url='http://m.maoyan.com/mmdb/comments/movie/341516.json?_v_=yes&offset=' + str(i)
        html = get_one_page(url)
        print('正在保存第%d页.'% i)
        for item in parse_ono_page(html):
            with open('狄仁杰.txt','a',encoding='utf-8') as f:
                f.write(item['date'] + ',' + item['nickname'] + ',' + item['city'] + ',' +str(item['rate'])+','+item['comment']+'\n')
 #反爬
        time.sleep(5 + float(random.randint(1,100)) /20) 

# 获取的评论可能有重复，为了最终统计的真实性，需做去重处理
def delete_repeat(old,new):
    oldfile = open(old,'r',encoding='UTF-8')
    newfile = open(new,'w',encoding='UTF-8')
    content_list = oldfile.readlines() #读取的数据集
    content_alreadly_ditinct = [] #存储不重复的评论数据
    for line in content_list:
        if line not in content_alreadly_ditinct: #评论不重复
            newfile.write(line+'\n')
            content_alreadly_ditinct.append(line)

if __name__ =='__main__':
    save_to_txt()
    delete_repeat(r'狄仁杰.txt', r'狄仁杰_new.txt')

from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import jieba
import matplotlib.pyplot as plt
import seaborn as sns
from pyecharts import Geo

f = open('狄仁杰_new.txt',encoding='UTF-8')
data = pd.read_csv(f,sep=',',header=None,encoding='UTF-8',names=['date','nickname','city','rate','comment'])

city = data.groupby(['city'])
rate_group = city['rate']
city_com = city['city'].agg(['count'])
city_com.reset_index(inplace=True)
data_map = [(city_com['city'][i],city_com['count'][i]) for i in range(0,city_com.shape[0])]
geo = Geo("狄仁杰",title_color="#fff",title_pos="center",width=1200,
          height=600,background_color="#404a59")

while True: 
    try:
        attr, val = geo.cast(data_map)
        geo.add("", attr, val, visual_range=[0, 50], visual_text_color="#fff", is_geo_effect_show=False,
                is_piecewise=True, visual_split_number=6, symbol_size=15, is_visualmap=True)
    except ValueError as e:
        e = str(e)
        e = e.split("No coordinate is specified for ")[1]  # 获取不支持的城市名称
        for i in range(0,len(data_map)):
            if e in data_map[i]:
                data_map.pop(i)
                break
            else:
                break
geo.render('狄仁杰.html')

#评分分析
rate = data['rate'].value_counts()

sns.set_style("darkgrid")
bar_plot = sns.barplot(x=rate.index,y=(rate.values/sum(rate)),palette="muted")
plt.xticks(rotation=90)
plt.show()
#分词
comment = jieba.cut(str(data["comment"]),cut_all=False)
wl_space_split= " ".join(comment)
#导入背景图
backgroud_Image = plt.imread('xuke.jpg')
stopwords = STOPWORDS.copy()
print(" STOPWORDS.copy()",help(STOPWORDS.copy()))
#可以自行加多个屏蔽词，也可直接下载停用词表格
stopwords.add("电影")
stopwords.add("一部")
stopwords.add("一个")
stopwords.add("没有")
stopwords.add("什么")
stopwords.add("有点")
stopwords.add("这部")
stopwords.add("这个")
stopwords.add("不是")
stopwords.add("真的")
stopwords.add("感觉")
stopwords.add("觉得")
stopwords.add("还是")
stopwords.add("特别")
stopwords.add("非常")
stopwords.add("可以")
stopwords.add("因为")
stopwords.add("为了")
stopwords.add("比较")
print (stopwords)
#设置词云参数
#参数分别是指定字体/背景颜色/最大的词的大小,使用给定图作为背景形状
wc =WordCloud(width=1024,height=768,background_color='white',
              mask = backgroud_Image,font_path='C:/Windows/Fonts/simkai.ttf',
              stopwords=stopwords,max_font_size=400,
              random_state=50)
#将分词后数据传入云图
wc.generate_from_text(wl_space_split)
plt.imshow(wc)
plt.axis('off')#不显示坐标轴
plt.show()
#保存结果到本地
wc.to_file(r'xuke_wordcloud.jpg')