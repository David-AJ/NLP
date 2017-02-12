#-*-coding:utf-8-*- 
import jieba
from multiprocessing import Pool,cpu_count
import numpy as np
import codecs

def wordcont(wordlist):
	dic = {}
	for i in wordlist[:,1]:
		if i == None:
			continue
		for j in i:
			if j in dic:
				dic[j] = dic[j] + 1
			else:
				dic[j] = 1
	return sorted(dic.iteritems(),key=lambda a:a[1],reverse=True)

def cut(sentence):
		global StopWord
		if sentence[1]!=None:
			sentence[1] = jieba.lcut(sentence[1],cut_all=False)
		return [i for i in sentence if i not in StopWord]

if __name__ == '__main__':
	# 读取StopWord.txt获取停用词,标准格式为 word + '\r\n'
	f = codecs.open('StopWord.txt','r','utf8')
	StopWord  = f.read().split('\r\n')
	f.close()
	# 去除最后一个'\r\n' 
	StopWord.remove(StopWord[-1])
	
	path = raw_input("Enter the path: ")
	data = np.load(path)
	# 使用多进程编程提高分词速度  
	pool = Pool(cpu_count())
	data = pool.map(cut, data)
	pool.close()
	pool.join()	
	data = np.array(data)
	np.save(path,data)
	
