#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
#两者乘积
num1=input('输入数字1:')
num2=input('输入数字2:')
print('%s*%s='%(num1,num2),int(num1)*int(num2))
'''
'''
#两者乘积
s1=72
s2=85
r=(s2-s1)/s1
#print('{0}成绩提升了{1:.1f}%'.format('小明',r*100))
print('%s成绩提升了%.1f%%'%('小明',r*100))
'''
'''
height=float(input('输入身高[m]:'))
weight=float(input('输入体重[kg]:'))
BMI=weight/(height*height)
if BMI>32:
	print('你的BMI为%.1f,严重肥胖'%BMI)
elif BMI>28 and BMI<=32:
	print('你的BMI为%.1f,肥胖'%BMI)
elif BMI>25 and BMI<=28:
	print('你的BMI为%.1f,过重'%BMI)
elif BMI>=18.5 and BMI<=25:
	print('你的BMI为%.1f,正常'%BMI)
elif BMI<18.5:
	print('你的BMI为%.1f,过轻'%BMI)
else:
	print('输入错误，请重新输入')
'''
'''
L = ['Bart', 'Lisa', 'Adam']
#for name in L:
#	print('Hello,%s'%name)
i=len(L)
while i>0:
	i=i-1
print('Hello,%s'%L[i])
'''
'''
#计算二元一次方程的解
import math
def quadratic(a,b,c):
	#函数中不使用print方法，每种结果都有返回return
	data = b * b - 4 * a * c
	if data < 0:
		return 'none'
	elif data == 0:
		x = -b / (2 * a)
		return x
	else:
		x1 = (-b +math.sqrt(data)) /(2 * a)
		x2 = (-b -math.sqrt(data)) /(2 * a)
		return x1, x2
'''
'''
#使用print进行输出，return值为空
	if not (isinstance(a,(int,float))
			and isinstance(a,(int,float))
			and isinstance(a,(int,float))):
		raise TypeError('bad operand type')
	data=b*b-4*a*c
	if data < 0:
		print('no result!')
	elif data==0:
		x1=-b/(2*a)
		print('x1=x2=%.2f'%x1)
	else:
		x1=(-b+math.sqrt(data))/2*a
		x2=(-b-math.sqrt(data))/2*a
		print('x1=%.2f,x2=%.2f'%(x1,x2))
	return
'''
'''
i=0
def hanoi(n,a,b,c): #n表示a柱盘子个数，a,b,c分别代表三个柱子
	if(n==1):
		move(1,a,c)  #当n=1时，直接将盘子放到c柱上
		return 0
	else:
		hanoi(n-1,a,c,b)  #n-1个在A上的盘子通过c移动到b柱上
		move(n,a,c)
		hanoi(n-1,b,a,c)  #b柱上n-1个盘子，通过a柱移动到c柱上
def move(num, first, next):  #打印移动方式：编号，从哪个盘子移动到哪个盘子
	global i
	i+=1
	print('step%d:move %d from %c-->%c'%(i,num,first,next))
hanoi(3,'A','B','C')
'''
'''
def trim(s):  #去除字符串的首尾空格
	if(len(s)==0):  #字符串为空
		return ''
	while s[:1]==' ':  #字符串前端是否有空格判断
		s=s[1:]
	while s[-1:]==' ':  #字符串末尾是否有空格判断
		s=s[:-2]
	return s
'''
'''
def findMinAndMax(L):  #查找一个list中最小和最大值，并返回一个tuple
	if not isinstance(L,list):
		raise TypeError
	if (len(L)==0):
		return None,None
	min=L[0]
	for m in L:   #查找最小值
		if min>m:
			min=m   
	max=L[0]
	for n in L:   #查找最大值
		if max<n:
			max=n
	return min,max
print(findMinAndMax([1,2,3,4]))
'''
#代码优化：
def findMinAndMax(L):  #查找一个list中最小和最大值，并返回一个tuple
	if not isinstance(L,list):
		raise TypeError
	if (len(L)==0):
		return None,None
	max=min=L[0]
	for m in L:
		if min>m:
			min=m
		else:
			if max<m:
				max=m
	return min,max
if __name__ == "__main__":
	L=[1,2,3,4,5,6,7]
	print(findMinAndMax(L))
#L1=['Hello','world',18,'apple',None]
#L2=[x.lower() for x in L1 if isinstance(x,str)]#将L1中的字符串小写输出到新的列表
'''
def triangles(n):
	global i
	L=[]
	while i<=n:
		if i==0:
			L.append(1)
		elif i>0 and i<n:
			#L[i]=L[i]+L[i-1]
			pass
		elif i==n:
			L.append(1)
'''
