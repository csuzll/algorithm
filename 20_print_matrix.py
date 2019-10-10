def print_matrix(matrix):
	"""
	:param matrix: [[]]
	"""
	rows = len(matrix)
	cols = len(matrix[0]) if matrix else 0

	ret = []
	start = 0
	while rows > start*2 and cols > start*2:
		print_circle(matrix, start, rows, cols, ret)
		start += 1
	print(ret)

def print_circle(matrix, start, rows, cols, ret):
	row = rows - start - 1
	col = cols - start - 1

	# 从左到右打印一行
	for c in range(start, col+1):
		ret.append(matrix[start][c])

	# 从上到下打印一列
	if row > start:
		for c in range(start+1, row+1):
			ret.append(matrix[c][col])

	# 从右到左打印一行
	if row > start and col > start:
		for c in range(col-1, start-1, -1):
			ret.append(matrix[row][c])

	# 从下到上打印一列
	if row - start >=2 and col > start:
		for c in range(row-1, start, -1):
			ret.append(matrix[c][start])

if __name__ == '__main__':
	mat = [[1, 2, 3],
			[5, 6, 7],
			[9, 10, 11]]
	print_matrix(mat)
	mat = [[]]
	print_matrix(mat)
	mat = [[1]]
	print_matrix(mat)
	mat = [[1, 2, 3, 4]]
	print_matrix(mat)
	mat = [[1], [2], [3], [4]]
	print_matrix(mat)
	mat = [[1, 2],
			[5, 6]]
	print_matrix(mat)