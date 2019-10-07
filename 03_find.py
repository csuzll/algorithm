# 在一个行和列都递增的二维数组中找某个数是否存在

# 利用有行列有序性，算法时间复杂度为O(n+m)，n为行数，m为列数
def find(arr, num):
	rows = len(arr)
	cols = len(arr[0])

	found = False
	# 判断输入的数组是否为空
	if arr != None:
		# row,col初始设定为右上角位置
		row = 0
		col = cols - 1

		while (row < rows and col >=0):
			"""
			分3种情况
			1. 当前位置元素等于目标位置元素，已找到，返回
			2. 当前位置元素大于目标位置元素，位置左移一列(col-=1)
			3. 当前位置元素小于目标位置元素，位置下移一列(row+=1)
			"""
			if arr[row][col] == num:
				found = True
				break
			elif arr[row][col] > num:
				col -= 1
			else:
				row += 1
	return found

# 简单的循环
def find2(arr, num):
	find = False
	for i in range(len(arr)):
		if num in arr[i]:
			find = False
			break
	return find

if __name__ == '__main__':
	arr = [[1,2,8,9], [2,4,9,12], [4,7,10,13], [6,8,11,15]]
	print(find(arr,14))
