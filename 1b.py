
def binary_search (arr,x):
low=0
high=len(arr)-1
mid=0
while low<=high:
mid=(high+low)//2
if arr[mid]<x:
low=mid+1
elif arr[mid]>x:
high=mid -1
else:
return mid
return -1
arr=[2,3,4,8,9,1]
x=int(input("Enter element to search "))
result=binary_search(arr,x)
if result ! =-1:
print("Element is found at index",result)
else:
print("Element is not found")
