class Node(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def firstCommonNode(pHead1, pHead2):
	if not pHead1 or not pHead2:
		return
	s1 = []
	s2 = []

	p1 = pHead1
	while p1:
		s1.append(p1.val)
		p1 = p1.next

	p2 = pHead2
	while p2:
		s2.append(p2.val)
		p2 = p2.next

	res = None
	while len(s1) > 0 and len(s2) > 0:
		v1 = s1.pop()
		v2 = s2.pop()
		if v1 == v2:
			res = v1
		else:
			break
	return res

def firstCommonNode2(pHead1, pHead2):
	if not pHead1 or not pHead2:
		return
	len1 = len2 = 0
	p1, p2 = pHead1, pHead2

	while p1:
		len1 += 1
		p1 = p1.next

	while p2:
		len2 += 1
		p2 = p2.next

	while len1 > len2: # 长链表先走多的长度
		len1 -= 1
		pHead1 = pHead1.next

	while len2 > len1:
		len2 -= 1
		pHead2 = pHead2.next

	while pHead1:
		if pHead2 == pHead1:
			return pHead1
		pHead1,pHead2 = pHead1.next, pHead2.next
	return None
