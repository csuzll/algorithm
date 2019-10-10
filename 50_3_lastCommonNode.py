# 多叉树结点类
class Node(object):
	def __init__(self, data, left=None, right=None):
		self.val = data
		self.child_list = [] # 子节点列表

	def add_child(self, node):
		self.child_list.append(node)

# 获取根结点到目标结点的路径
def getNodePath(cur, pnode, path=[]):
	if not cur or not pnode:
		return "no"
	path.append(cur.val) # 当前节点值添加路径列表
	if cur.val == pnode.val: # 如果找到目标 返回路径列表
		return path
	if cur.child_list == []: # 如果没有孩子列表 就 返回 no 回溯标记
		return "no"
	for node in cur.child_list:
		t_path = path[:]
		res = getNodePath(node, pnode, t_path)
		if res == "no": # 如果返回no，说明找到头没找到  利用临时路径继续找下一个孩子节
			continue
		else:
			return res
	return "no" # 如果所有孩子都没找到 则回溯

# 获取两个结点的最低公共祖先结点
def getLastCommonNode(root, node_p, node_q):
	path1 = getNodePath(root, node_p)
	path2 = getNodePath(root, node_q)
	if root is None or path1 == "no" or path2 == "no":
		return "无穷大", "无节点"

	len1, len2 = len(path1), len(path2)
	# if len1 <= len2:
	# 	length = len1
	# else:
	# 	length = len2
	# ret = None
	# index = 0
	# while index < length:
	# 	if path1[index] == path2[index]:
	# 		ret = path1[index]

	# 	index += 1
		
	# return ret
	for i in range(len1-1, -1, -1):
		if path1[i] in path2:
			return path1[i]


root = Node('A')
B = Node('B')
C = Node("C")
D = Node('D')
E = Node("E")
F = Node("F")
G = Node("G")
H = Node("H")
I = Node("I")
J = Node("J")
root.add_child(B)
root.add_child(C)
root.add_child(D)
B.add_child(E)
B.add_child(F)
B.add_child(G)
D.add_child(H)
D.add_child(I)
D.add_child(J)

n = getLastCommonNode(root, H, J)
print(n)