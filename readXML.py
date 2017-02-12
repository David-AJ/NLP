import xml.etree.ElementTree as ET
import numpy as np

# data.xml代表需要读取的xml文件,本例中XML包含节点名为'url' 及 'content'
f = open('data.xml','r')
t = f.readlines()
f.close()


urls = []
docs = []

try:
	# create tree from string list	
	tree = ET.fromstringlist(t)
	urls.append(tree.find('url').text)
	docs.append(tree.find('content').text)
except ET.ParseError:
	exceptcode
	
np.save('urls',np.array(urls))
np.save('docs',np.array(docs))

