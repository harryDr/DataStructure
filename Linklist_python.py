#coding=utf-8
class Node:
	'''定义链表节点，包含值和下一个节点'''
	def __init__(self,data):
		self.data = data
		self.nex = None

	def _print_(self):
		return (str(self.data))

class Linklist:
	'''链表的操作'''
	def __init__(self):
		'''初始化链表'''
		self.head = None
		self.length = 0

	def isEmpty(self):
		'''判断是否为空'''
		return (self.length==0)

	def addEnd(self,dataList):
		'''在末尾追加节点'''
		#判断dataList是否为Node类型
		if isinstance(dataList,Node):
			node = dataList
		else:
			node = Node(dataList)
		#是否为空链表
		if not self.head:
			self.head = node
			self.length += 1
		else:
			cur = self.head
			while cur.nex:  #并不会去比遍历最后一个节点
				cur = cur.nex
			cur.nex = node
			self.length += 1

	def delNode(self,index):
		'''删除任意节点'''
		if self.isEmpty():
			print('this Link is empty')
			return
		if index<0 or index>self.length:
			print ('error: out of index')
		if index == 0:
			#头节点
			self.head = self.head.nex
			self.length -=1
			return
		else:
			i,cur = 1,self.head  #i从1开始 找到要删除的节点的上一个节点 i从0开始就是要删除的节点
			while i < index and cur.nex:
				cur = cur.nex
			cur.nex= cur.nex.nex    #删除最后一个节点是一样的 找到前一个节点 赋下一个的下一个还是None
			self.length -=1

	def updata(self,index,data):
		'''修改一个节点'''
		if self.isEmpty() or index < 0 or index >= self.length:
			print ('error: out of index')
			return
		j = 0
		cur = self.head
		while j < index and cur.nex:
			cur = cur.nex
		cur.data = data

	def getNode(self,index):
		'''获取一个节点'''
		if self.isEmpty() or index < 0 or index >= self.length:
			print ('error: out of index')
			return
		j = 0
		cur = self.head
		while j < index and cur.nex:
			cur = cur.nex
		return cur.data

	def getIndex(self,data):
		'''获取某个节点的索引'''
		i,cur = 0,self.head
		while cur.nex:
			if cur.data == data:
				return i
			else:
				cur = cur.nex
			i+=1
		print('data is not in this List')
		return

	def insert(self,index,dataList):
		'''插入节点'''
		if self.isEmpty() or index < 0 or index >= self.length:
			print ('error: out of index')
			return
		# 判断dataList是否为Node类型
		if isinstance(dataList, Node):
			node = dataList
		else:
			node = Node(dataList)
		#在头部插入
		if index == 0:
			node.nex = self.head
			self.head = node
			self.length += 1
			return
		i,cur = 1,self.head
		while i<index and cur.nex:
			cur = cur.nex  #cur 为删除的上一个节点
		node.nex = cur.nex
		cur.nex = node
		self.length += 1
		return

	def clear(self):
		'''清空链表'''
		self.head = None
		self.length = 0

	def rever(self):
		'''反转链表'''
		cur = self.head
		per_node = None
		while cur:               #链表两两反转
			nex_node = cur.nex
			cur.nex = per_node   #最后一个节点的下一个节点为None per_node为当前节点
			per_node = cur
			cur = nex_node
		node = per_node
		print("Head -->", node.data)
		node = node.nex
		while node:
			print("-->", node.data)
			node = node.nex

	def print_linked(self):
		'''对整个链表的打印'''
		if self.isEmpty():
			print("Linked list's length is 0")
		else:
			node = self.head
			print("Head -->", node.data)
			while node.nex:
				node = node.nex
				print("-->", node.data)
				# print("--> None. Linked node finished")


if __name__ == '__main__':
	# 索引的值从0开始的
	node1 = Node(data='node1')
	node2 = Node(data='node2')
	node3 = Node(data='node3')
	node4 = Node(data='node4')
	link = Linklist()
	link.addEnd(node1)
	link.addEnd(node2)
	link.addEnd(node3)
	link.addEnd(node4)
	link.print_linked()
	# link.updata(1,'test')
	# link.print_linked()
	# link.delNode(1)
	# link.print_linked()
	# print(link.getIndex('node1'))
	# print(link.getNode(0))
	# link.insert(0,'insertNode')
	# link.print_linked()
	link.rever()
	# link.print_linked()
	# link.clear()
	# link.print_linked()