def swap(a,b,arr):
	if a!=b:
		arr[a],arr[b] = arr[b] ,arr[a]

def partition(arr,start,end,size):
	pivot = arr[start]
	pivot_index = start
	start+=1
	while start < end :
		while start<=size and arr[start] <= pivot :
			start+=1
		while arr[end] > pivot:
			end-=1
		if start < end:
			swap(start,end,arr)
	swap(pivot_index,end,arr)
	return end


def quickSort(arr,start,end):
	if start < end :
		pivot_index = partition(arr,start,end,len(arr)-1)
		quickSort(arr,start,pivot_index-1)
		quickSort(arr,pivot_index+1,end)

if __name__=="__main__":
	arr = []
	for i in range(10,0,-1):
		arr.append(i)
	quickSort(arr,0,len(arr)-1)
	print(arr)
