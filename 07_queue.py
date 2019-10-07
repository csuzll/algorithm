# 两个栈实现队列（入队和出队复杂度都为O（1）
class Queue(object):
	def __init__(self):
		self.instack = []
		self.outstack = []

	def enqueue(self, item):
		self.instack.append(item)

	def dequeue(self):
		if self.outstack == []:
			while self.instack != []:
				self.outstack.append(self.instack.pop())
		if self.outstack == []:
			return "队列为空"
		else:
			return self.outstack.pop()

# 两个队列实现栈()
class Stack(object):
	def __init__(self):
		self.queue1 = []
		self.queue2 = []

	def push(self, item):
		if self.queue1 == [] and self.queue2 == []:
			self.queue1.append(item)
		elif self.queue1 != []:
			self.queue1.append(item)
		else:
			self.queue2.append(item)

	def pop(self):
		if self.queue1==[] and self.queue2==[]:
			return "栈为空"
		elif self.queue2 == []:
			while len(self.queue1) > 1:
				self.queue2.append(self.queue1.pop(0))
			return self.queue1.pop()
		else:
			while len(self.queue2) > 1:
				self.queue1.append(self.queue2.pop(0))
			return self.queue2.pop()

if __name__ == '__main__':
	# queue = Queue()
	# queue.enqueue(1)
	# queue.enqueue(2)
	# queue.enqueue(3)
	# print(queue.dequeue())
	# print(queue.dequeue())
	# print(queue.dequeue())
	# print(queue.dequeue())

	stack = Stack()
	stack.push(1)
	stack.push(2)
	stack.push(3)
	print(stack.pop())
	print(stack.pop())
	stack.push(4)
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())