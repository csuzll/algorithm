class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def treeDepth(root):
	if root is None:
		return 0
	if not root.left and not root.right:
		return 1
	left_h = treeDepth(root.left)
	right_h = treeDepth(root.right)
	return max(left_h, right_h) + 1

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

	print(treeDepth(A1))