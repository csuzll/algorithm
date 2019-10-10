# 获得num从右往左数的第一个为1的位置
def get_first_bitis1(num):
	indexBit = 0
	while num & 1 ==0 and indexBit < 32:
		num = num >> 1
		indexBit += 1
	return indexBit

# 验证某个数的二进制中的t位是不是1
def is_one(num, t):
	if t < 0 or t > 31:
		return 
	num = num >> t
	# num&1为0则代表t位不是1，为1代表是1
	return num & 1

def get_only_one_number(nums):
	if not nums:
		return None
	# 数组中所有数的异或结果
	tmp_ret = 0
	for n in nums:
		tmp_ret = tmp_ret ^ n

	# 找到这个异或结果的第一位1，从右往左
	first_one_index = get_first_bitis1(tmp_ret)

	# 根据这个位置将数组分为两组，并分别异或得
	a_ret,b_ret = 0,0
	for n in nums:
		if is_one(n, first_one_index):
			a_ret = a_ret ^ n
		else:
			b_ret = b_ret ^ n
	return a_ret,b_ret

if __name__ == '__main__':
	test = [1, 2, 3, 4, 3, 1, -1, -1]
	print(get_only_one_number(test))