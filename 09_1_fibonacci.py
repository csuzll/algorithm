def fibonacci(n):
	if n <= 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2(n):
	if n <= 0:
		return 0
	if n == 1:
		return 1
	first, second = 0,1
	for i in range(2, n+1):
		first, second = second, first + second
	return second

# 直接使用生成器
def fib(n):
	if n < 0:
		return None
	a, b = 0, 1
	for i in range(n):
		yield b
		a, b = b, a+b

if __name__ == '__main__':
	print(fibonacci(10))
	print(fibonacci2(10))
	print(fib(10))