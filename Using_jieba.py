#-*-coding:utf-8-*- 
import jieba
from multiprocessing import Pool,cpu_count
import numpy as np
import codecs

# 读取StopWord.txt获取停用词,标准格式为 word + '\r\n'
f = codecs.open('StopWord.txt','r','utf8')
StopWord  = f.read().split('\r\n')
f.close()
# 去除最后一个'\r\n' 
StopWord.remove(StopWord[-1])
StopWord  = set(StopWord)

def cut(sentence):
		global StopWord
		if sentence[1]!=None:
			sentence[1] = [word for word in jieba.lcut(sentence[1],cut_all=False) if word not in StopWord]
		return [i for i in sentence]

if __name__ == '__main__':	
	path = raw_input("Enter the path: ")
	data = np.load(path+'npy')
	# 使用多进程编程提高分词速度  
	pool = Pool(cpu_count())
	data = pool.map(cut, data)
	pool.close()
	pool.join()	
	data = np.array(data)
	np.save(path+'_cut.npy',data)
	
