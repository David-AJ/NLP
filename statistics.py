#-*-coding:utf-8-*- 
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

	