def stackSort(array,size):
		stack=[]
		top=0
		flag=1
		stack=[0 for i in range(size+1)]
		i=0
		stack[top]=array[i]
		i+=1
		while top!=size:
			if stack[top] <= array[i]:
				stack[top+1]=array[i]
				top+=1
				i+=1
			else:
				while stack[top] > array[i] and top>=0 and (array[i] not in stack):
					stack[top]=0
					top-=1
					flag=0
				if flag==0:
					stack[top+1]=array[i]
					flag=1
					top+=1
				i+=1
			if i==size+1:
				i=0
		return stack

array=[9,8,7,6,5,3,2,10]
print(stackSort(array,len(array)-1))
