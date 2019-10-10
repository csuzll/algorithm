# 假设不含重复的值
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

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