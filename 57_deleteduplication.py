class Node(object):
	def __init__(self, x):
		self.val = x
		self.next = None		

def deleteDuplication(pHead):
	# 指向当前结点前最晚访问过的不重复结点
	pPre = None
	# 当前结点
	pCur = pHead
	# 当前结点后面的结点
	pNext = None

	while pCur:
		# 如果当前结点与下一个结点相同
		if pCur.next and pCur.val == pCur.next.val:
			pNext = pCur.next
			# 找到重复的最后一个结点的位置
			while pNext.next and pNext.next.val == pCur.val:
				pNext = pNext.next
			# 如果当前结点指向链表中的第一个元素，pCur -> ... -> pNext ->... 
			# 要删除pCur到pNext, 将指向链表第一个元素的指针pHead指向pNext->next。
			if pCur == pHead:
				pHead = pNext.next
			# 如果pCur不指向链表中第一个元素，pPre -> pCur ->...->pNext ->... 
			# 要删除pCur到pNext，即pPre->next = pNext->next
			else:
				pPre.next = pNext.next
			# 向前移动
			pCur = pNext.next

		else:
			# 如果当前结点与下一个结点不相同
			pPre = pCur
			pCur = pCur.next
	return pHead