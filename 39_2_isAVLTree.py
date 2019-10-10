class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def isBalaced_tree(root):
	global flag
	flag = True
	isBalanced(root)
	return flag

def isBalanced(root):
	# 为None,表示空结点，深度为0，也算平衡二叉树
	if root is None:
		d = 0
		return d
	left_h =  isBalanced(root.left)
	right_h = isBalanced(root.right)
	if abs(left_h - right_h) > 1:
		flag = False
		return 0
	d = 1 + max(left_h, right_h)
	return d

if __name__ == '__main__':
	A1 = TreeNode(1)
	A2 = TreeNode(2)
	A3 = TreeNode(3)
	A4 = TreeNode(4)
	A5 = TreeNode(5)
	A6 = TreeNode(6)

	A1.left=A2
	A1.right=A3
	A2.left=A4
	A2.right=A5
	A4.left=A6

	print(isBalaced_tree(A1))