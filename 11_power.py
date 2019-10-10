def getPower(base, exp):
	"""
	:base: 浮点数
	:exp: 整数
	"""
	# 首先判断exp是否为0，任意数的0次方结果都为1
	if exp == 0:
		return 1
	# 然后判断底数base为0时，0的任何次方都为0
	if base == 0:
		return 0
	# 当底数不为0时，区分exp和0的关系
	flag = True # 设置一个指数是否小于0的标志，默认为True，即指数为正数。
	if exp < 0:
		exp = -exp
		flag = False
	# exp为偶数
	if exp % 2 == 0:
		res = getPower(base, exp//2)
		res *= res
	# exp为奇数
	else:
		res = getPower(base, exp//2)
		res *= res
		res *= base
	return res if flag else 1/res

"""
判断一个数是不是偶数：
用 >> 1 代替 // 2
用 & 0x1 == 1 为真代表奇数，
代替 % 2 == 1

"""