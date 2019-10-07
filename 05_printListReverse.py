# 从尾到头打印链表

# 结点类
class ListNode(object):
	def __init__(self, data):
		self.data = data
		self.next = None

# 链表类
class Single_LinkList(object):
	def __init__(self, node=None):
		self.head = node

	# 在头部添加结点
	def add(self, item):
		node = ListNode(item)
		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			self.head = node

# 打印
def printListReverse(linkedlist):
	stack = []
	cur = linkedlist.head
	if cur == None:
		print("链表为空")
	else:
		while cur:
			stack.append(cur.data)
			cur = cur.next
		while stack:
			print(stack.pop(), "<--", end=" ")

# 第二种
def printListReverse2(head):
	result = []
	cur = head
	while cur:
		result.insert(0, cur.data)
		cur = cur.next
	return result

if __name__ == '__main__':
	linkedList = Single_LinkList()
	for i in range(5, -1, -1):
		linkedList.add(i)
	printListReverse(linkedList)
