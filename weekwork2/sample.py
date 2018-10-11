"""
实验输入为一个含有标点符号的英文文献。其中，将所有连续的英文字母视作一个单词，仅以句号“.”、问号“?”、感叹号“!”结尾的才视作一个完整的句子。例如：“fdafa”、“a”、“b”均是一个单词，而“I‘m a boy.”是一个句子，它含有“I”、“m”、“a”、“boy”四个单词；但“I am a boy,”则不是一个完整的句子，因为其以逗号“,”结尾。若最后一句话没有结束符号，则视为不完整的句子，不计入结果。
实验中所有的单词字母不区分大小写，“Single”和“single”视为同一个单词。
为保证实验公平性，所有实验程序均使用python3编写，不允许使用诸如python中内置dict等哈希表扩展。
要求能够从命令行读取文本文件名，代码中以文件的方式读取文献文件document.txt和查询文件query.txt。如若待分析文件名为document.txt，查询文件名为query.txt，程序应能够以 python3 sample.py document.txt query.txt 的形式运行，其中sample.py是提交的python程序文件名。
待分析文件中包含完整的英文文献。查询文件中每行一个单词，要求输出这个单词在文献中出现的所有句子的次序以及在该句子中出现的位置。两个数以“/”号隔开，例如第一个句子第二个单词，输出应为1/2。每一个这样的数对之间以逗号隔开，每个单词的所有出现位置输出一行。
若待查询单词在文献中没有出现，则输出字符串“None”。
"""
import sys

def main():
	text=[]
	query=[]
	with open(sys.argv[1]) as file:
		ftmp=file.read().lower()
		eof=('.','?','!')
		sentence=""
		for e in ftmp:
			if e in eof:
				text.append(sentence.split())
				sentence=""
			else:
				sentence+=e if e.isalpha() else " "
	#print(text)
	with open(sys.argv[2]) as file:
		query=file.read().lower().splitlines()
	#print(query)
	for word in query:
		res=[]
		for i in range(len(text)):
			for (j,value) in enumerate(text[i]):
				#print("value=",value,"word=",word)
				if value==word:
					res.append("{}/{}".format(i+1,j+1))
		if res:
			print(','.join(res))
		else:
			print("None")

"""
def KMP(s,t):
	assert t!=""
	len_s=len(s)
	len_t=len(t)
	next=[0]*len_t
	j=next[0]=-1
	for i in range(1,len_t):
		while j>=0 and t[j]!=t[i-1]:
			j=next[j]
		j+=1
		next[j]=j
	def kmp(start,res):
		if start==len_s:
			return
		j=0
		for i in range(start,len_s):
			while j>=0 and s[i]!=t[j]:
				j=next[j]
			j+=1
			if j==len_t:
				res.append(i-len_s+1)
				return kmp(i-len_s+2,res)
	tmp=kmp(0,[])
"""
if __name__ == '__main__':
	main()
