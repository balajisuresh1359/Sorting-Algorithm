import time
import random
class sorting(object):

	def __init__(self,arr):
		self.arr=arr
		self.size=len(arr)-1

	def swap(self,a,b):
		if a!=b:
			self.arr[a],self.arr[b] = self.arr[b] ,self.arr[a]

	def orderedInsert(self,start,postion):
		while self.arr[start] < self.arr[postion] :
			start+=1
		if start!=postion:
			last_element = self.arr[postion]
			while postion != start:
				self.arr[postion] = self.arr[postion-1]
				postion-=1
			self.arr[start] = last_element

	def partition(self,start,end):
		pivot = self.arr[start]
		pivot_index = start
		start+=1
		while start < end :
			while start<=self.size and self.arr[start] <= pivot :
				start+=1
			while self.arr[end] > pivot:
				end-=1
			if start < end:
				self.swap(start,end)
		self.swap(pivot_index,end)
		return end

	def merge(self,arr,leftArray,rightArray):
		i=j=k=0
		while i < len(leftArray) and j < len(rightArray):
			if leftArray[i] < rightArray[j]:
				arr[k]=leftArray[i]
				i+=1
			else:
				arr[k]=rightArray[j]
				j+=1
			k+=1
		while i<len(leftArray):
			arr[k]=leftArray[i]
			i+=1
			k+=1
		while j<len(rightArray):
			arr[k]=rightArray[j]
			j+=1
			k+=1
		return arr

	def bubbleSort(self):
		[self.swap(i,j) for i in range(self.size,0,-1) for j in range(i) if self.arr[i] < self.arr[j]]

	def selectionSort(self):
		[self.swap(i,self.arr.index(min(self.arr[i:]))) for i in range(self.size+1)]
		
	def insertionSort(self):
		[self.orderedInsert(0,i) for i in range(1,self.size+1)]
	
	def quickSort(self,start,end):
		if start < end :
			pivot_index = self.partition(start,end)
			self.quickSort(start,pivot_index-1)
			self.quickSort(pivot_index+1,end)

	def mergeSort(self,arr):
		if len(arr) == 1:
			return arr
		mid = len(arr)//2
		return self.merge(arr,self.mergeSort(arr[:mid]),self.mergeSort(arr[mid:]))

	def stackSort(self):
		stack=[]
		top=0
		flag=1
		size=self.size+1
		stack=[0 for i in range(size)]
		stack[top]=self.arr[0]
		i=1
		size-=1
		while top!=size:
			if stack[top] <= self.arr[i]:
				stack[top+1]=self.arr[i]
				top+=1
				i+=1
			else:
				while stack[top] > self.arr[i] and top>=0 and (self.arr[i] not in stack):
					stack[top]=0
					top-=1
					flag=0
				if flag==0:
					stack[top+1]=self.arr[i]
					flag=1
					top+=1
				i+=1
			if i==size+1:
				i=0
		size+=1
		for i in range(size):
			self.arr[i] = stack[i]

if __name__=="__main__":
	
	#Calling Bubble-sort
	arr=[random.randint(0,1000) for x in range(0,950)]
	sort = sorting(arr)
	start=time.time()
	sort.bubbleSort()
	print(f"Bubble sort    :{time.time()-start}")

	#Calling Selection-sort
	arr=[random.randint(0,1000) for x in range(0,950)]
	sort = sorting(arr)
	start=time.time()
	sort.selectionSort()
	print(f"Selection sort :{time.time()-start}")
	
	#Calling Insertion-sort
	arr=[random.randint(0,1000) for x in range(0,950)]
	sort = sorting(arr)
	start=time.time()
	sort.insertionSort()
	print(f"Insertion sort :{time.time()-start}")

	#Calling Quick-sort
	arr=[random.randint(0,1000) for x in range(0,950)]
	sort = sorting(arr)
	start=time.time()
	sort.quickSort(0,len(arr)-1)
	print(f"Quick sort     :{time.time()-start}")
	

	#Calling Merge-sort
	arr=[random.randint(0,1000) for x in range(0,950)]
	sort = sorting(arr)
	start=time.time()
	sort.mergeSort(arr)
	print(f"Merge sort     :{time.time()-start}")
	

	#Calling Stack-sort
	arr=[random.randint(0,1000) for x in range(0,950)]
	sort = sorting(arr)
	start=time.time()
	sort.stackSort()
	print(f"Stack sort     :{time.time()-start}")


'''
Input : Sorted-array(reversed order)
Bubble sort    :0.12500309944152832
Selection sort :0.04688286781311035
Insertion sort :0.18750882148742676
Quick sort     :0.15625929832458496
Merge sort     :0.01562881469726562
Stack sort     :15.8760290145874025
'''


'''
Input : Sorted-array
--------------------
Bubble sort    :0.12500333786010742
Selection sort :0.03125619888305664
Insertion sort :0.17188215255737305
Quick sort     :0.10938239097595215
Merge sort     :0.015629291534423828
Stack sort     :0.0
'''


'''
Input : Random-order
--------------------
Bubble sort    :0.18750858306884766
Selection sort :0.04688549041748047
Insertion sort :0.21875810623168945
Quick sort     :0.01562786102294922
Merge sort     :0.015626907348632812
Stack sort     :7.03008508682251
'''


'''
Overall:
---------
Bubble sort    :0.14583834012349447
Selection sort :0.04167485237121582
Insertion sort :0.19271636009216309
Quick sort     :0.09375651677449544
Merge sort     :0.01562833786010742
Stack sort     :7.63537136713663750
'''
