def number1between1andn(n):
	count = 0
	i = 1
	while i <= n:
		a = n // i
		b = n % i
		count += (a+8) // 10 * i + (a % 10 == 1)*(b+1)
		i *= 10
	return count


# 常规方法(非常慢)
def test_n(n):
	ret = 0
	for n in range(1, n+1):
		for s in str(n):
			if s == "1":
				ret += 1
	return ret

print(number1between1andn(9923446))
print(test_n(9923446))