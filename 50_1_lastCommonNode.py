# 二叉搜索树的最低公共祖先
class Node(object):
	def __init__(self, data, left=None, right=None):
		self.val = data
		self.left = left
		self.right = right

# class BinaryTree(object):
# 	def __init__(self):
# 		self.root = None
# 		self.size = 0

# 	def __len__(self):
# 		return self.size

# 	def put(self, data):
# 		if self.root:
# 			self._put(data, self.root)
# 		else:
# 			self.root = Node(data)
# 			self.size += 1

# 	def _put(self, data, curNode):
# 		if data < curNode.val:
# 			if curNode.left:
# 				self._put(data, curNode.left)
# 			else:
# 				curNode.left = Node(data)
# 				self.size += 1
# 		elif data > curNode.val:
# 			if curNode.right:
# 				self._put(data, curNode.right)
# 			else:
# 				curNode.right = Node(data)
# 				self.size += 1
# 		else:
# 			pass
# 			# curNode.data = data

# 获取最低公共祖先
def getLastCommonNode(root, node_p, node_q):
	# 下面这个条件能把root为空，node_p为空，node_q为空，node_q或node_q不在树中的情况排除掉
	if root == None or node_p==None or node_q==None:
		return None
	if root.val > node_p.val and root.val > node_q.val:
		return getLastCommonNode(root.left, node_p, node_q)
	elif root.val < node_p.val and root.val <node_q.val:
		return getLastCommonNode(root.right, node_p, node_q)
	else:
		return root

node1 = Node(6)
node2 = Node(2)
node3 = Node(8)
node4 = Node(0)
node5 = Node(4)
node6 = Node(7)
node7 = Node(9)
node8 = Node(3)
node9 = Node(5)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node5.left = node8
node5.right = node9

node_p = Node(2)
node_q = Node(4)
n = getLastCommonNode(node1, node_p, node_q)
if n==None:
	print(n)
else:
	print(n.val)