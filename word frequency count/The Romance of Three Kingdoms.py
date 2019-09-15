'''
import re
import sys
text=open("D:\\刘荆琦\\ICC\\Senior 2\\CS\\Github Res\\project-and-work-of-ICC-AL-CS-course-James-Liu\\word frequency count\\三国演义人物.txt","r").read()
sys.maxunicode==0xffff is True
punctuation = '！，；：。-、“\'!,;:?.()-*&/"\'-_'

def removepunc(t):
    t = re.sub(r'[{}]+'.format(punctuation),'',text)
    return t.strip().lower()

l=removepunc(text).split()

'''

import wordcloud
