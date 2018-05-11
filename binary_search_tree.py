# #coding=utf-8
# #二叉查找树的实现
class Node:
	def __init__(self,data):
		self.data = data
		self.lchild = None
		self.rchild = None

class Binary_search_tree:
	def __init__(self):
		self.root = None

	def insert(self,data):
		'''插入'''
		#将第一个点设置为根节点
		if self.root == None:
			self.root = Node(data)
		else:
			current = self.root   #使用self.root 就不行？
			while True:
				if data < current.data:
					if current.lchild:
						current = current.lchild
					else:
						current.lchild = Node(data)
						break
				else:
					if current.rchild:
						current = current.rchild
					else:
						current.rchild = Node(data)
						break

	# 先序遍历
	def preOrderTraverse(self, node):
		if node is not None:
			print (node.data)
			self.preOrderTraverse(node.lchild)
			self.preOrderTraverse(node.rchild)

	#中序遍历
	def inOrderTraverse(self,node):
		if node is not None:
			self.inOrderTraverse(node.lchild)
			print (node.data)
			self.inOrderTraverse(node.rchild)

	#后序遍历
	def postOrderTraverse(self,node):
		if node is not None:
			self.postOrderTraverse(node.lchild)
			self.postOrderTraverse(node.rchild)
			print(node.data)

	#先序遍历 堆栈实现
	def pre_stack(self, root):
		"""利用堆栈实现树的先序遍历"""
		if root == None:
			return
		myStack = []
		node = root
		while node or myStack:
			while node:		 # 从根节点开始，一直找它的左子树
				print (node.data)
				myStack.append(node)
				node = node.lchild
			node = myStack.pop()	 # while结束表示当前节点node为空，即前一个节点没有左子树了
			node = node.rchild

	#中序遍历 堆栈实现
	def in_stack(self,root):
		'''利用堆栈实现树的中序遍历'''
		if root == None:
			return
		myStack = []
		node = root
		while node or myStack:
			while node:		 # 从根节点开始，一直找它的左子树
				myStack.append(node)
				node = node.lchild
			node = myStack.pop()	 # while结束表示当前节点node为空，即前一个节点没有左子树了
			print (node.data)
			node = node.rchild

	def post_stack(self,root):
		'''利用堆栈实现树的后序遍历'''
		if root == None:
			return
		myStack1 = []
		myStack2 = []
		node = root
		myStack1.append(node)
		while myStack1:  # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
			node = myStack1.pop()
			if node.lchild:
				myStack1.append(node.lchild)
			if node.rchild:
				myStack1.append(node.rchild)
			myStack2.append(node)
		while myStack2:  # 将myStack2中的元素出栈，即为后序遍历次序
			print (myStack2.pop().data)

	def level_queue(self, root):
		"""利用队列实现树的层次遍历"""
		if root == None:
			return
		myQueue = []
		node = root
		myQueue.append(node)
		while myQueue:
			node = myQueue.pop(0)
			print (node.data)
			if node.lchild != None:
				myQueue.append(node.lchild)
			if node.rchild != None:
				myQueue.append(node.rchild)

if __name__ == "__main__":
	array = [15,5,3,12,16,20,23,13,18,10,6,7]
	bst = Binary_search_tree()
	for item in array:
		bst.insert(item)
	bst.preOrderTraverse(bst.root)
	print ()
	bst.pre_stack(bst.root)
	print ()
	bst.inOrderTraverse(bst.root)
	print ()
	bst.in_stack(bst.root)
	print ()
	bst.postOrderTraverse(bst.root)
	print()
	bst.post_stack(bst.root)
	print ()
	bst.level_queue(bst.root)
