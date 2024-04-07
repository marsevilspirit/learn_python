from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba

# 打开文本
with open("test.txt", encoding="utf-8") as f:
    s = f.read()

# 中文分词
text = ' '.join(jieba.cut(s))

# 生成对象
mask = np.array(Image.open('bird.png'))
mask = np.uint8(mask)  # 将遮罩图像转换为无符号字节类型

stopwords = ["我", "你", "她", "的", "是", "了", "在", "也", "和", "就", "都", "这"]
wc = WordCloud(font_path="/usr/share/fonts/sarasa-gothic/Sarasa-ExtraLightItalic.ttc",
               mask=mask,
               width=1066,
               height=1280,
               max_words=200,
               background_color="white",
               contour_color = 'steelblue',
               stopwords=stopwords).generate(text)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

# 保存到文件
wc.to_file("test.png")
