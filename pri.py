print("============欢迎使用场次记录软件============")
print("============verson 1.0============")
print("============dev by LiDongyuan============")
print("使用说明：请将记录文件放在程序文件同目录下...否则文件将找不到...=.=")
#date:2016/4/11


#这里是写文件
filename=input("请输入记录文件名：")
f = open(filename,'a')
match_date=input('比赛时间(yyyy-mm-dd):')
judge1=input('裁判一:')
judge2=input('裁判二:')
match_timer=input('记时员:')
match_pointer=input('记分员:')
d={
'date':match_date,
'judge1':judge1,
'judge2':judge2,
'timer':match_timer,
'point':match_pointer
}
f.write('-------------------------\n')
for (k,v) in d.items():
	f.write('%s:%s\n' %(k,v))
f.write('\n')
f.close()

#以下是人员统计
'''思路：遍历文件内容，定义三个（裁判，计时，计分）dict
得到一个值就加一'''
print('\n\n进行文件的读入统计---------------')
f = open(filename,'r')

f_line = f.readlines()
j = {}
t = {}
p = {}

for line in f_line:
	#裁判：
	if 'judge' in line:
		name = line[line.index(':')+1:]
		if name in j:
			j[name] = j[name] + 1
		else :
			j[name] = 1


f.close()
print("裁判：")
for (k,v) in j.items():
	print('%s:%s次\n'%(k,v))

