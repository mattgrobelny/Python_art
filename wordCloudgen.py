
#!/usr/bin/env python
"""
Kmer Word Cloud 
===============
Generating a square wordcloud from the raw kmer count list.
"""

from os import path
from wordcloud import WordCloud
import getopt
import sys


file_name = ""

argv = sys.argv[1:]
try:
	opts, args = getopt.getopt(argv, "hf:")
except getopt.GetoptError:
	print 'wordCloudgen.py -f <inputfile>'
	sys.exit(2)
for opt, arg in opts:
	if opt == '-h':
        	print 'wordCloudgen.py -f <inputfile> \n'
		sys.exit()
	elif opt in ("-f"):
        	file_name = arg

print "Input file:", file_name

text_all =""
text =""

import csv
tsvfile= open(file_name, "r")
next(tsvfile)
tsvreader = csv.reader(tsvfile, delimiter="\t")
for line in tsvreader:
	text= (line[0]+" ")* int(line[1])
	text = text + "\n"
	text_all =  text_all + text
	


# Generate a word cloud image
#wordcloud = WordCloud().generate(text_all)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
#plt.imshow(wordcloud)
#plt.axis("off")

# take relative word frequencies into account, lower max_font_size
wordcloud = WordCloud(max_words=200,max_font_size=1000, relative_scaling=.5, width=4000, height=2000, prefer_horizontal=1).generate(text_all)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")

file_name_out= file_name[:-4]+"_wc_plot.png"
plt.savefig(file_name_out,dpi=500)

# The pil way (if you don't have matplotlib)
#image = wordcloud.to_image()
#image.show()
