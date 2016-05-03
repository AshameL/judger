
#以下是人员统计
'''思路：遍历文件内容，定义三个（裁判，计时，计分）dict
得到一个值就加一'''
filename=input("请输入记录文件名：(默认为test.txt)")
if filename == '':
	#这里修改默认文件
	filename = 'test.txt'
f = open(filename,'r')

f_line = f.readlines()
j = {}
t = {}
p = {}

for line in f_line:
	#裁判：
	if 'judge' in line:
		name = line[line.index(':')+1:-2]
		if name in j:
			j[name] = j[name] + 1
		else :
			j[name] = 1
	#计分：
	if 'point' in line:
		name = line[line.index(':')+1:-2]
		if name in p:
			p[name] = p[name] + 1
		else :
			p[name] = 1
	#计时：
	if 'time' in line:
		name = line[line.index(':')+1:-2]
		if name in t:
			t[name] = t[name] + 1
		else :
			t[name] = 1

f.close()
print("==================裁判==================")
for (k,v) in j.items():
	print('%s:%s次'%(k,v))
print("==================计分员==================")
for (k,v) in p.items():
	print('%s:%s次'%(k,v))
print("==================计时员==================")
for (k,v) in t.items():
	print('%s:%s次'%(k,v))

input("统计结束，按任意键结束.......")

