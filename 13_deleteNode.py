class Node(object):
	def __init__(self, x):
		self.val = x
		self.next = None		

def deleteNode(link, node):
	if link is None or node is None:
		return
	if node == link:
		del node
	if node.next is None:
		while link:
			if link.next == node:
				link.next = None
			link = link.next
	else:
		node.val = node.next.val
		n_node = node.next
		node.next = n_node.next
		del n_node

if __name__ == '__main__':
	node1 = Node(1)
	node1.next = Node(2)
	node1.next.next = Node(3)
	deleteNode(node1, Node(4))
	print(node1.val, node1.next.val)