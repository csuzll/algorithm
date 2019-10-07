# 实现常见的各种排序算法

# 冒泡排序
def bubblesort(alist):
	n = len(alist)
	for passnum in range(n-1, 0, -1):
		# passnum表示每趟比较的次数
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
	# n = len(alist)
	# # 每遍历一次只排好1个数字，则需要遍历n-1次
	# # 每一次遍历需要比较的次数为n-1-i，i为已经排好序的i位数字
	# for i in range(n-1):
	# 	for j in range(n-1-i):
	# 		if alist[j] > alist[j+1]:
	# 			alist[j],alist[j+1]= alist[j+1],alist[j]

# 改进冒泡排序，设置flag，当没有交换发生时，即可停止
def bubblesort2(alist):
	passnum = len(alist)-1
	flag = True
	while passnum > 0 and flag:
		flag = False
		for j in range(passnum):
			if alist[j] > alist[j+1]:
				flag = True
				alist[j],alist[j+1] = alist[j+1], alist[j]
		passnum -= 1

# 改进冒泡排序，双向冒泡排序
def bubblesort3(alist):
	length = len(alist) // 2
	i = 0 # 控制循环次数
	flag = True
	while i < length // 2 and flag:
		flag = False
		# 从左向右，大值后移
		for j in range(i, length-1-i):
			if alist[j] > alist[j+1]:
				alist[j],alist[j+1] = alist[j+1],alist[j]
				flag = True
		# 判断是否需要逆向遍历
		if flag:
			# 从右向左，小值前移
			for j in range(length-2-i, i, -1):
				if alist[j] < alist[j-1]:
					alist[j],alist[j-1] = alist[j-1],alist[j]
					flag = True
		i += 1

# 选择排序,记录最大元素位置，直接交换
def selectsort(alist):
	length = len(alist)-1
	for i in range(length, 0, -1):
		maxpos = 0
		for j in range(1, i):
			if alist[j] > alist[maxpos]:
				maxpos = j
		alist[maxpos],alist[i] = alist[i],alist[maxpos]

# 插入排序
def insertsort(alist):
	for index in range(1, len(alist)):
		# 当前要确定的数
		currentvalue = alist[index]
		pos = index

		while pos > 0 and currentvalue < alist[pos-1]:
			alist[pos] = alist[pos-1]
			pos -= 1

		alist[pos] = currentvalue

# 希尔排序,这个增量序列几乎都是互斥的。
def shellsort(alist):
	# 将gap的最大值找到，从此最大值开始递减
	gap = 1
	while gap < len(alist) // 2:
		gap = gap*2 + 1

	while gap > 0:
		for i in range(gap, len(alist)):
			currentvalue = alist[i]
			preindex = i-gap
			while preindex >=0 and currentvalue < alist[preindex]:
				alist[preindex+gap] = alist[preindex]
				preindex = preindex - gap
			alist[preindex+gap] = currentvalue
		gap = gap // 2 



