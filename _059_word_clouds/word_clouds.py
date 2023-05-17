
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-w','--words',help='the words to generate the word cloud with')
parser.add_argument('-o','--output_file',help='filename to output image to')
args = parser.parse_args()

wc = WordCloud().generate(args.words)
wc.to_file(args.output_file)

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
