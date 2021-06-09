def minimum(array,start,end):
		minimum_val= start
		# print("array : ",array[start:end+1])
		while start <= end:
			if array[minimum_val] > array[start]:
				minimum_val =start
			start+=1
		return minimum_val

def  selectionSort(array):
	size=len(array)
	for i in range(0,size-1):
		pos=minimum(array,i,size-1)
		array[i] ,array[pos] =array[pos],array[i]
	return array


array=[9,7,6,4,1,2,56]
print(selectionSort(array))
