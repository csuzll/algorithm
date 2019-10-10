class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Tree(object):
	def __init__(self):
		self.root = None

	# 添加1个元素
	def put(self, x):
		if self.root:
			self._put(x, self.root)
		else:
			self.root = TreeNode(x)
	def _put(self, x, tree):
		if x < tree.val:
			if tree.left:
				self._put(x, tree.left)
			else:
				tree.left = TreeNode(x)
		elif x > tree.val:
			if tree.right:
				self._put(x, tree.right)
			else:
				tree.right = TreeNode(x)
		else:
			tree.val = x

	# 列表构建一个二叉排序树
	def construct_tree(self, values):
		for v in values:
			self.put(v)

"""
将二叉搜索树转换为双向链表
"""
def convert(tree):
	# 获取这个链表的头结点
	if not tree:
		return None
	p_last = convertNode(tree, None)
	while p_last and p_last.left:
		p_last = p_last.left
	return p_last

def convertNode(tree, last):
	"""
	tree: 输入的树的根结点
	last: 指向已经转换好的链表的最后一个结点
	返回转换好的链表的最后一个结点
	"""
	if not tree:
		return None

	if tree.left:
		last = convertNode(tree.left, last)
	# 指针转换
	if last:
		last.right = tree
	tree.left = last
	last = tree

	if tree.right:
		last = convertNode(tree.right, last)
	return last

def print_nodes(tree):
	# 正序打印链表
	ret = []
	while tree:
		ret.append(tree.val)
		tree = tree.right
	print(ret)


if __name__ == '__main__':
	r = Tree()
	r.construct_tree([10,6,14,4,8,12,16])
	t = convert(r.root)
	print_nodes(t)