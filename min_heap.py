class Heap:
    def __init__(self):
        self.heap_array =[]

    ''' 
    Method that simply inserts a value to the Heap utilizing the percolate_up
    method to traverse the heap to insert to the appropriate position. 
    '''      
    def insert (self,k):
        self.heap_array.append(k)
        self.percolate_up(len(self.heap_array) - 1)


    ''' 
     Method that removes the last value from the heap in support of 
     another method to swap (percolate_down) and position the values 
     where they should be. 
    '''   
    def extract_min(self):
        if self.is_empty():
            return None

        min_elem = self.heap_array[0]   #last value of the heap would be in index 0 
        min = self.heap_array.pop()
        
        if len(self.heap_array)>0:
            self.heap_array[0] = min
            self.percolate_down(0)
        return min_elem
    
    def is_empty(self):
        return len(self.heap_array)==0
    
        
    ''' 
    Auxiliary methods to maintain the properties of a min heap 
    	 - percolate_up to insert a new value in the heap
    	 - percoulate_down to remove a value from the heap 
	'''
    def percolate_up(self, i):
        while i > 0:

            parent_i = (i - 1) // 2	 # computes the parent node's index

            #checks the value of the index and its's parent to see if there is no violation 
            if self.heap_array[i] >= self.heap_array[parent_i]:
                return
            else:
            	#swaps the two values 
            	self.heap_array[i] , self.heap_array[parent_i] = self.heap_array[parent_i] , self.heap_array[i]      
            	#continue to loop from the parent node
            	i = parent_i           
    ''' 
	 Method that traverses until violation is found and then it fixes it 
	'''
    def percolate_down(self, node_i):
        child_index = 2 * node_i + 1
        value = self.heap_array[node_i]

        while child_index < len(self.heap_array):
            # Find the min among the node and all the node's children
            min_value = value
            min_i = -1
            i = 0
            while i < 2 and i + child_index < len(self.heap_array):
                if self.heap_array[i + child_index] < min_value:
                    min_value = self.heap_array[i + child_index]
                    min_i = i + child_index
                i = i + 1

            # check for a violation of the min heap property
            if min_value == value:
                return
            else:
            	self.heap_array[node_i] , self.heap_array[min_i] = self.heap_array[min_i] , self.heap_array[node_i]
                #continue loop from the min index node
            node_i = min_i
            child_index = 2 * node_i + 1

    '''
    Heap sort implementation 
    '''            
    def heap_sort(self):
        heap_sorted = Heap()
        while len(self.heap_array)>0:
            min_dummy = self.extract_min()
            heap_sorted.insert(min_dummy)
        return heap_sorted
    

'''
Creation of the heap along with reading a txt file to obtain numbers 
to work with the different operations 
'''
unsorted_heap = Heap()

g = open("numbers.txt")
num_list = g.readlines()


#reading the list to the Heap 
for ln in num_list:
    ln = int(ln.replace('\n',''))	#numbers will be sepearated by a space
    unsorted_heap.insert(ln)		# insert the numbers(ln) into the heap 

print("Unsorted Heap ")
print(unsorted_heap.heap_array)

unsorted_heap = unsorted_heap.heap_sort()

print("Heap Sort: ")
print(unsorted_heap.heap_array)
 



