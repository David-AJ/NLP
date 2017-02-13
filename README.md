# NLP   
个人项目中涉及到的NLP代码，包括但不限于分词、去除停用词、LDA使用等
## 文件及代码说明
* Using_jieba.py   
引用jieba,multiprocessing,numpy等模块实现多进程并发处理分词。
同时加入StopWord词典，实现分词同时去除停用词，利用set结构实现O(1)查找  

* readXML.py    
引入xml.etree.ElementTree模块的method实现从字符串中获取xml结构并解析    

* word_frequency.py    
利用字典结构实现单词计数，统计词频    

* StopWord.txt    
UTF8编码的中文停用词表
