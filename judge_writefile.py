print("============欢迎使用场次记录软件============")
print("============verson 1.0============")
print("============dev by LiDongyuan============")
print("使用说明：请将记录文件放在程序文件同目录下...否则文件将找不到...=.=")
#date:2016/4/11


#这里是写文件
filename=input("请输入记录文件名：(默认为test.txt)")
if filename == '':
	#这里修改默认文件
	filename = 'test.txt'

f = open(filename,'a')
flag = 'y'
while flag == 'y' :

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
	flag = input('输入y则继续输入，输入其他则跳出录入文件')

f.close()