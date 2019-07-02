import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
from os import path
from PIL import Image

d = path.dirname('/Users/mayue/Desktop/')
alice_coloring = np.array(Image.open(path.join(d, '11845036_979767725407141_3470810865801502118_o.png')))
wc = WordCloud(background_color="white", max_words=1000,min_font_size=10,max_font_size=150,mask=alice_coloring, random_state=10)
wc.fit_words(words_freq)
image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()

# plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()
wc.to_file('hehe.png')