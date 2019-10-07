# 单链表，K>0，尾结点为倒数第1个结点。

class Node(object):
	def __init__(self, data):
		self.val = data
		self.next = None

def findKthToTail(head, k):
	if k <= 0:
		return None

	# 设置快慢指针
	fast = slow = head

	# 快指针先走到正数第K个结点（走K-1步）
	for i in range(k-1):
		# 如果链表长度小于K则返回None
		if fast == None:
			return None
		fast = fast.next

	# 快慢指针同时向前走
	while fast.next != None:
		fast = fast.next
		slow = slow.next

	return slow



