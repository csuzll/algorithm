class Node(object):
	def __init__(self, val, parent=None):
		self.val = val
		self.parent = parent

# 设置2个指针
# p1，p2分别遍历l1,l2。当p1遍历完l1，p1从头遍历l2，当p2遍历完l2，p2从头遍历l1。
def getLastCommonNode1(root, node_p, node_q):
	if root == None or node_p==None or node_q==None:
		return None
	p1 = node_p
	p2 = node_q
	while p1 != p2:
		p1 = node_q if p1 is None else p1.parent
		p2 = node_p if p2 is None else p2.parent
	return p1

# 设置2个栈
def getLastCommonNode2(root, node_p, node_q):
	if root == None or node_p==None or node_q==None:
		return None
	stack1 = []
	stack2 = []
	p1 = node_p
	while p1 is not None:
		stack1.append(p1)
		p1 = p1.parent
	p2 = node_q
	while p2 is not None:
		stack2.append(p2)
		p2 = p2.parent
	res = None
	while len(stack1) > 0 and len(stack2) > 0:
		v1 = stack1.pop()
		v2 = stack2.pop()
		if v1 == v2:
			res = v1
		else:
			break
	return res

node1 = Node(6)
node2 = Node(2)
node3 = Node(8)
node4 = Node(0)
node5 = Node(4)
node6 = Node(7)
node7 = Node(9)
node8 = Node(3)
node9 = Node(5)
node2.parent = node1
node3.parent = node1
node4.parent = node2
node5.parent = node2
node6.parent = node3
node7.parent = node3
node8.parent = node5
node9.parent = node5

node_p = node2
node_q = node5
n = getLastCommonNode1(node1, node_p, node_q)
if n == None:
	print(n)
else:
	print(n.val)

m = getLastCommonNode2(node1, node_p, node_q)
if m == None:
	print(m)
else:
	print(m.val)
