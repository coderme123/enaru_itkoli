stack = []

n = int(input("Enter number of elements: "))

print("Enter elements:")

for i in range(n):
    ele = input(f"Element {i + 1}: ")
    stack.append(ele)
    print("Initial stack:")
    print(stack)

print("Popping elements from the stack:")
while stack:
    print("Element popped from stack:")
    print(stack.pop())
    print("Stack after element popped:")
    print(stack)
