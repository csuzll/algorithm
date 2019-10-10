def jumpFloor(n):
	if n < 1:
		return None
	else:
		return 2 ** (n-1)

def jumpFloor2(n):
	if n < 1:
		return None
	total = 1
	for _ in range(1, n):
		total *= 2
	return total

if __name__ == '__main__':
	print(jumpFloor(6))
	print(jumpFloor2(6))