# O(n)利用快排的partition的思想来找到前k个小的数
def partition(alist, first, last):
	base = alist[first]
	leftmark = first + 1
	rightmark = last

	while leftmark <= rightmark:
		while leftmark <= rightmark and alist[leftmark] <= base:
			leftmark += 1
		while alist[rightmark] >= base and rightmark >= leftmark:
			rightmark -= 1
		if leftmark < rightmark:
			alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
	
	alist[first], alist[rightmark] = alist[rightmark], alist[first]

	return rightmark

def findLeastKnums(alist, k):
	length = len(alist)
	if not alist or k <= 0 or k > length:
		return
	first = 0
	last = length - 1
	index = partition(alist, first, last)
	while index != k:
		if index > k:
			index = partition(alist, first, index-1)
		elif index < k:
			index = partition(alist, index+1, last)
	return alist[:k]


# 堆排序找到前K个小的数
# 堆调整
def heapify(alist, start, end):
	root = start
	while True:
		child = 2 * root + 1
		if child > end:
			break
		if child + 1 <= end and alist[child] < alist[child+1]:
			child = child + 1
		if alist[root] < alist[child]:
			alist[root],alist[child] = alist[child], alist[root]
			start = child
		else:
			break

def findLeastKnums2(alist, k):
	res = []
	length = len(alist)
	change = True
	if length <=0 or k <= 0 or k > length:
		return res
	res = alist[:k]

	# 遍历从索引k到最后一个元素
	for i in range(k, length):
		if change == True:
			# 构建最大堆
			for j in range(k//2-1, -1, -1):
				heapify(res, j, k-1)
			# 排序
			for j in range(k-1, 0, -1):
				res[0],res[j] = res[j],res[0]
				heapify(res, 0, j-1)
			change = False
		if res[k-1] > alist[i]:
			res[k-1] = alist[i]
			change = True
	return res

# 用数组的方法
def findLeastKnums3(alist, k):
	if len(alist) < k:
		return []
	tmp = sorted(alist[:k])
	for item in alist[k:]:
		index = k - 1
		flag = False
		while index >= 0 and tmp[index] > item:
			index -= 1
			flag = True
		if flag == True:
			tmp.insert(index+1, item)
			tmp.pop()
	return tmp

l = [4,5,1,6,2,7,3,8]
min_k = findLeastKnums(l, 4)
min_k2 = findLeastKnums2(l, 4)
min_k3 = findLeastKnums3(l, 4)
print(min_k)
print(min_k2)
print(min_k3)