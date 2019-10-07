# 1
def replaceSpace(astr):
	return astr.replace(" ", "%20")

# 2
def replaceSpace2(astr):
	return "%20".join(s.split(" "))

# 3 时间复杂度为o(n)
def replaceSpace3(astr):
	# 计算空格个数
	num_space = 0
	for i in astr:
		if i == " ":
			num_space += 1

	# 新的长度
	new_len = len(s) + 2 * num_space

	index_origin = len(s) - 1 # 原始串的最右索引
	index_new = new_len - 1   # 新串的最右索引
	new_astr = [None for i in range(new_len)] # 初始化新串

	while index_origin >=0 and (index_new > index_origin):
		if s[index_origin] == " ":
			# 空格的话，新串索引逐步向前将3个字符赋值，最后向前挪动一步
			new_astr[index_new] = "0"
			index_new -= 1
			new_astr[index_new] = "2"
			index_new -= 1
			new_astr[index_new] = "%"
			index_new -=1
		else:
			# 其他情况直接赋值，并向前一步
			new_astr[index_new] = astr[index_origin]
			index_new -= 1
		# 原始串索引向前1步
		index_origin -= 1
	# 返回字符串
	return "".join(new_astr)