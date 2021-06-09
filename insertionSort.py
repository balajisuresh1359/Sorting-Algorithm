def orderInsert(array,start,end,key):
		i=start
		while array[i] < key:
			i+=1
		j=end-1
		k=i
		while j >= i:
			array[j+1]=array[j]
			j-=1
		array[k]=key

def insertionSort(array):
		size=len(array)
		for i in range(size):
			orderInsert(array,0,i,array[i])
		return array

array=[9,7,6,4,1,2,56]
print(insertionSort(array))
