def uglyNumber(n):
	ugly = [1]
	t2,t3,t5=0,0,0 # 分别标记乘以2，3，5的丑数索引

	while n > 1:
		while ugly[t2] * 2 <= ugly[-1]:
			t2 += 1
		while ugly[t3] * 2 <= ugly[-1]:
			t3 += 1
		while ugly[t5] * 2 <= ugly[-1]:
			t5 += 1
		ugly.append(min(ugly[t2]*2, ugly[t3]*3, ugly[t5]*5))
		n -= 1
	return ugly[-1]

if __name__ == '__main__':
	print(uglyNumber(1500))
