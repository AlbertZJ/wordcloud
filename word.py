# -*- coding: utf-8 -*-
 
import jieba
import matplotlib.pyplot as plt 
import numpy as np 

from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator


def GetWordCloud():
    path_txt = 'F://ass.txt'  #添加文档
    path_img = r"C:\Users\ASUS\Desktop\照片/15.jpg"   #定义图片路径
    word = open(path_txt, 'r').read()  #以只读的方式打开文档
    background_image = np.array(Image.open(path_img)) 
    # 结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云 
    #Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。 
    cut_text = " ".join(jieba.cut(word,cut_all=False))  #引号中必须有一个空格
    wordcloud = WordCloud( 
        # 设置字体，不然会出现口字乱码 
        font_path = "C:/Windows/Fonts/simfang.ttf",
        background_color = "white",  #设置词云背景颜色为白色 
        # mask参数=图片背景，另外有mask参数再设定宽高是无效的
        scale=1.5,
        mask=background_image).generate(cut_text) 
        # 生成颜色值 
    image_colors = ImageColorGenerator(background_image)         
        # 下面代码用来绘制图片       
    plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear") 
    plt.axis("off") 
    plt.show() 
    
if __name__ == '__main__':
    GetWordCloud()