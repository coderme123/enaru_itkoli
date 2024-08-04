
def linear_search(arr,x)
for i in range(len(arr)):
if arr[i]==x:
return i
return -1
arr = [10,20,30,40,50]
x=int(input ("Enter the search element:")
result=linear_search(arr,x)
if result ! = -1:
print ("Element is found at index ",result)
else:
print("Element is not found")
