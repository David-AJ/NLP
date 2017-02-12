import jieba
from multiprocessing import Pool,cpu_count
import numpy as np

StopWord


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
	path = raw_input("Enter the path: ")
	data = np.load(path)
	pool = Pool(cpu_count()-1)
	data = pool.map(cut, data)
	pool.close()
	pool.join()	
	data = np.array(data)
	np.save(path,data)