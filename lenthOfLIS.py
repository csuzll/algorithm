# 最长上升子序列（输出长度）
import sys
import bisect

# O(n2)
def findMaxUpSublist(arr):
    n = len(arr)
    # dp存储到每个位置的最大上升子序列长度，初始化为1，长度最短为自身
    dp = [1 for i in range(n)]
    
    for i in range(1, n):
        for j in range(0, i):
        	# 状态转移方程
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+1)

    # dp中的最大值即为整个列表中最长上升子序列长度
    maxlen = max(dp)
    return maxlen

# 贪心法
# 利用贪心的思想，对于一个上升子序列，显然当前最后一个元素越小，越有利于添加新的元素，这样LIS长度自然更长。 
# def findMaxUpSublist2(arr):
# 	# 长度为i+1的LIS结尾元素的最小值
# 	dp = []
# 	for v in arr:
# 		pos = bisect.bisect_left(dp, v)
# 		# 大于则添加到末尾
# 		if (pos == len(dp)):
# 			dp.append(v)
# 		# 否则，v替换pos位置的值
# 		else:
# 			dp[pos] = v
# 	maxlen = len(dp)
# 	return maxlen

def findMaxUpSublist2(arr):
	dp = []

	for v in arr:
		pos = ()
		if (pos == len(dp)):
			dp.append(v)
		else:
			dp[pos] = v

	return len(dp)

def binarySearch(arr, v, left, right):
	if left == right:
		return left
	while left < right:
		mid = (left + right) // 2
		if mid == left or mid == right:
			



# line = sys.stdin.readline().strip()
# arr = list(map(int, line.split()))
arr = [1, -1, 2, -2, 3, -3, 4]
maxlen = findMaxUpSublist(arr)
maxlen2 = findMaxUpSublist2(arr)
print(maxlen, maxlen2)