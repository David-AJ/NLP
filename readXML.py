import xml.etree.ElementTree as ET
import numpy as np

f = open('news_tensite_xml.dat','r')
t = f.readlines()
f.close()

urls = []
docs = []
for i in range(len(t)/6):
	try:
		tree = ET.fromstringlist(t[i*6:(i+1)*6])
		urls.append(tree.find('url').text)
		docs.append(tree.find('content').text)
	except ET.ParseError:
		urls.append(t[i*6+1][5:-7])
		docs.append(t[i*6+4][9:-11])
np.save('urls',np.array(urls))
np.save('docs',np.array(docs))

