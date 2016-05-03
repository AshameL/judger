name = input('请输入你的姓名：')
height = input('请输入你的身高cm：')
weight = input('请输入你的体重kg：')
a = int(height)
b = float(weight)
print(name,'你的身高是',a,'厘米，体重',b,'千克，\n你的体重状况为：')
print('%s,你的身高是%d厘米，体重是%.2f千克\n你的体重状况是：'%(name,a,b))
bmi = b/(a/100)**2
if bmi < 18.5:
	print('过轻')
elif bmi <=25:
	print('正常')
elif bmi <=32:
	print('肥胖')
elif bmi >32:
	print('严重肥胖')