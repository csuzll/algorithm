"""
树的非递归先序遍历：
先访问根结点，然后弹出根结点，并把根结点的右孩子和左孩子压入栈，再弹出左孩子，并把左孩子的子孙如上压入并弹出，最后弹出右孩子，如上压入右孩子的子孙并弹出。

栈的大小空间为O(h)，h为二叉树高度。时间方面，每个节点都被压入栈一次，弹出栈一次，访问一次，复杂度为O(n)。

树的非递归中序遍历：
先将根入栈，中序遍历需要最先访问左孩子，因此需要一直遍历到左孩子结点为空的结点才进行弹出，直到弹出根，然后再访问右孩子。

树的非递归后序遍历：
两个栈实现，第一个栈左右根，第二个栈根右左，再把第二个栈弹出。
"""
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# 循环先序遍历
def preorder(root):
	# 利用栈实现,根入栈出栈，然后右子树，左子树入栈，然后左先出，右再出
	if root == None:
		return None
	node_stack = [root]
	# res = []
	while len(node_stack) > 0:
		curnode = node_stack.pop()
		print(curnode.val, end = " ")
		# res.append(root.val)
		if curnode.right:
			node_stack.append(curnode.right)
		if curnode.left:
			node_stack.append(curnode.left)
	# return res

# 递归实现先序遍历
def pre_order(root):
	if root == None:
		return None
	print(root.val, end=" ")
	preorder(root.left)
	preorder(root.right)

# 循环实现中序遍历
def inorder(root):
	# 栈实现，根，左子树入栈，左出栈，根出栈，然后右入栈，右出栈
	if root == None:
		return None
	node_stack = []
	node = root
	while node or len(node_stack)>0:
		if node:
			node_stack.append(node)
			node = node.left
		else:
			node = node_stack.pop()
			print(node.val, end=" ")
			node = node.right

# 递归实现中序遍历
def in_order(root):
	if root == None:
		return None
	else:
		in_order(root.left)
		print(root.val, end=" ")
		in_order(root.right)

# 循环实现后序遍历
def postorder(root):
	if root == None:
		return None
	else:
		stack1 = [root] # 根，左，右
		stack2 = [] # 根 右，左
		while len(stack1) > 0: # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
			node = stack1.pop()
			stack2.append(node)
			if node.left:
				stack1.append(node.left)
			if node.right:
				stack1.append(node.right)
		# 将myStack2中的元素出栈，即为后序遍历次序
		while len(stack2) > 0:
			print(stack2.pop().val, end=" ")

# 递归实现后序遍历
def post_order(root):
	if root == None:
		return
	else:
		post_order(root.left)
		post_order(root.right)
		print(root.val, end=" ")

# 层次遍历
def breadorder(root):
	if root == None:
		return
	else:
		res = []
		node_queue = [root]
		while len(node_queue) > 0:
			node = node_queue.pop(0)
			res.append(node.val)
			if node.left:
				node_queue.append(node.left)
			if node.right:
				node_queue.append(node.right)
	return res