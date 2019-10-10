def numberOf1(n):
	"""
	在Python中，由于负数使用补码表示的，对于负数，最高位为1，而负数在计算机是以补码存在的，往右移，符号位不变，符号位1往右移，最终可能会出现全1的情况，导致死循环。与0xffffffff相与，就可以消除负数的影响。
	"""
	count = 0
	if n < 0:
		n = n & 0xffffffff
	while n:
		count += 1
		n = n & (n-1)
	return count

if __name__ == '__main__':
	print(bin(100).count("1")==numberOf1(100))