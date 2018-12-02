
class Heap:

 def __init__(self , items =[]):
 	self.heap_array = []

#Recieve data, will be appended to the heap and then percolate it up to its proper position

def extract_min(self):
	# the case where there are 2 values in the heap you first swap the 2 values 
	if len(self.heap_array) > 2:
		self.heap_array[1] , self.heap_array[len(self.heap_array) - 1] = self.heap[len(self.heap_array) - 1] , self.heap_array[1]
		min = self.heap.extract_min()

	#only 1 value in the heap 
	elif len(self.heap_array) == 2:
		min = self.heap.extract_min()

	# extracting a value from an empty heap 
	else:
		min = False 

	return min 

#Assuming the value is inserted at the bottom of the heap/ end of the list 
#want to percolate it up to the proper position
def percolate_up(self, index):

	parent = index //2   #finding the parent of the index that will be percolating up 

	#check if the index that has just passed in is 1 
	#passed index is 1 -- > no need to percolate up 
	if index <= 1: 
		return 
	# if the value passed in is less than it's parent then the two will be swaped 
	elif self.heap_array[index] < self.heap[parent]:
		self.heap_array[index] , self.heap_array[parent] = self.heap[parent] , self.heap_array[index]
		self._percolate_up(parent)

def percolate_down(self, index):

	left = index * 2 
	right = index * 2 + 1

	smallest = index 
	#compare index value to the left child and right child to determine wich one is the smallest 
	if (len(self.heap_array) < left) and (self.heap_array[smallest] > self.heap[left]):
		smallest = left
	if len(self.heap_array) < right and self.heap_array[smallest] > self.heap[left]:
		smallest = right

	if largest != index: 
		self.heap_array[index] , self.heap_array[smallest] = self.heap[smallest] , self.heap_array[index]
		self._percolate_down(smallest)

def insert(self, k):
	self.heap_array.append(k)
	self._percolate_up(len(self.heap) - 1)


def is_empty(self):
	return len(self.heap_array) == 0




m = Heap([95,3,21])
m.insert(10)
print(str(m.heap_array[0:len(m.heap_array)])) 
print(str(m.extract_min))










