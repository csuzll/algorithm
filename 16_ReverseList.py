# 反转链表
class ListNode(object):
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

# 方法1:3个指针遍历反转，返回原始链表的尾结点
def reverseList(head):
	# 链表为空
	if head == None and head.next == None:
		return head

	pre = None
	cur = head
	while cur:
		tmp = cur.next # 下一个结点
		cur.next = pre # 反转
		# pre,cur向前推移
		pre = cur
		cur = tmp
	return pre

# 方法2：递归求解
def reverseList2(head):
	if not head or not head.next:
		return head
	newhead = reverseList2(head.next)
	head.next.next = head
	head.next = None
	return newhead


if __name__ == '__main__':
	head1 = ListNode(1)
	head1.next = ListNode(2)
	head1.next.next = ListNode(3)
	head1.next.next.next = ListNode(4)

	head2 = ListNode()

	head3 = ListNode(1)

	tail1 = reverseList2(head1)
	tail2 = reverseList2(head2)
	tail3 = reverseList2(head3)

	print(tail1.data, tail1.next.data, tail1.next.next.data, tail1.next.next.next.data)
	print(tail2.data)
	print(tail3.data)
