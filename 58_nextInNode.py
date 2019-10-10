class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.parent = None
		self.left = None
		self.right = None

def findSuccessor(pnode):
	if not pnode:
		return None
	if pnode.right:
		pnode = pnode.right
		while pnode.left:
			pnode = pnode.left
		return pnode
	else:
		while pnode.parent:
			if pnode == pnode.parent.left:
				return pnode.parent
			pnode = pnode.parent
		return None

if __name__ == '__main__':
	A1 = TreeNode(1)
	A2 = TreeNode(2)
	A3 = TreeNode(3)
	A4 = TreeNode(4)
	A5 = TreeNode(5)
	A6 = TreeNode(6)

	A1.left=A2
	A1.right=A3
	A2.parent = A1
	A3.parent = A1
	A2.left=A4
	A4.parent = A2
	A3.right=A5
	A5.parent = A3
	A5.left=A6
	A6.parent = A5

	nodelist = [A1,A2,A3,A4,A5,A6]
	for n in nodelist:
		s = findSuccessor(n)
		if s:
			print(s.val)
		else:
			print(s)