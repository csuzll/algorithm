# 假设不含序列不含重复的值

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


# 重建二叉树
def reConstructBinaryTree(preorder, inorder):
	prelen = len(preorder)
	inlen = len(inorder)

	if prelen == 0 or inlen == 0 or prelen != inlen:
		return None
	if prelen == 1:
		return TreeNode(preorder[0])
	# 前序遍历的第一个结点一定是根结点
	root = TreeNode(preorder[0])
	index = inorder.index(preorder[0])
	root.left = reConstructBinaryTree(preorder[1:index+1], inorder[:index])
	root.right = reConstructBinaryTree(preorder[index+1:], inorder[index+1:])
	return root

if __name__ == '__main__':
	# pre = [1,2,4,7,3,5,6,8]
	# mid = [4,7,2,1,5,3,8,6]
	# root = reConstructBinaryTree(pre, mid)
	# print(root.val,root.left.val,root.right.val)

	node1 = TreeNode(1)
	node2 = TreeNode(2)
	node3 = TreeNode(3)
	node4 = TreeNode(4)
	node5 = TreeNode(5)
	node6 = TreeNode(6)
	node7 = TreeNode(7)
	node8 = TreeNode(8)

	node1.left = node2
	node1.right = node3
	node2.left = node4
	node3.left = node5
	node3.right = node6
	node4.right = node7
	node6.left = node8

	preorder(node1)
	print("\n")
	pre_order(node1)
	print("\n")
	inorder(node1)
	print("\n")
	in_order(node1)
	print("\n")
	postorder(node1)
	print("\n")
	post_order(node1)
	print("\n")
	bo = breadorder(node1)
	print(bo)