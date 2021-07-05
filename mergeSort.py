def merge(arr,leftArray,rightArray):
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

def mergeSort(arr):
	if len(arr) == 1:
		return arr
	mid = len(arr)//2
	return merge(arr,mergeSort(arr[:mid]),mergeSort(arr[mid:]))

if __name__=="__main__":
	arr = []
	for i in range(10,0,-1):
		arr.append(i)
	mergeSort(arr)
	print(arr)
