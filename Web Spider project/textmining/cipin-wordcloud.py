# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:07:40 2018

@author: rdfz-411
"""

# -*- encoding:utf-8 -*-
import jieba.analyse
from os import path
from scipy.misc import imread
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import imageio
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

if __name__ == "__main__":

    mpl.rcParams['font.sans-serif'] = ['FangSong']
    #mpl.rcParams['axes.unicode_minus'] = False

    content = open("huozhe.txt","rb").read()  ###!!!! 改文件名

    # tags extraction based on TF-IDF algorithm
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=False)
    text =" ".join(tags)
    text = unicode(text)
    print(text)
    # read the mask
    d = path.dirname(__file__)
    trump_coloring = imageio.imread(path.join(d, "trump.png"))
    stopwords = STOPWORDS.copy()
    stopwords.add("家珍")
    wc = WordCloud(font_path='simsun.ttc',
            background_color="white", max_words=1000, mask=trump_coloring,
            max_font_size=400, stopwords=stopwords,random_state=50)

    # generate word cloud 
    wc.generate(text)

    # generate color from image
    image_colors = ImageColorGenerator(trump_coloring)

    plt.imshow(wc)
    plt.axis("off")
    plt.show()

