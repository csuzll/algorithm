"""
由于python长整数类型可以表示无限位，所以需要人为设置边界，避免死循环。

31位1就是0x7FFFFFFF，二进制中第一位是符号位，所以只有31位，超了本来要溢出的，可是Python不溢出。

// int型的最大值
2147483647 
0x7fffffff 
//

越界检查：
& 0xFFFFFFFF，0xFFFFFFFF代表16进制下的边界，正数与边界数按位与&操作后仍得到这个数本身，
负数与边界数按位与&操作后得到的是对应二进制数的真值，

返回：
通过查看符号位（最高位，即与0x7FFFFFF比较大小）判断a为正数还是负数，正数则直接返回。
负数则返回~(a^0xFFFFFFFF)返回的是原来负数的值。 （注： ~ 表示按位取反）
"""

def bit_add(num1, num2):
	while num2!=0:
		num1,num2 = (num1 ^ num2),((num1 & num2)<<1)
		num1 = num1 & 0xffffffff
		num2 = num2 & 0xffffffff
	if num1 <= 0x7fffffff:
		return num1
	else:
		return ~(num1 ^ 0xffffffff)

def add(num1, num2):
	return sum([num1, num2])

if __name__ == '__main__':
	print(add(32,45))

	# python的直接交换
	a,b = "a",1
	a, b = b, a
	print(a,b)

	# 加法交换，只适用于数字类型
	a,b=3,5
	a = a + b
	b = a - b
	a = a - b
	print(a,b)

	# 位运算，只适用于数字类型
	a,b = -1,-2
	a = a ^ b
	b = a ^ b
	a = a ^ b
	print(a,b)