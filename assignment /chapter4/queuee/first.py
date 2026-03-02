# First Assignment
Q1 = []

while True:
    num = input("Enter the number that you want to add: ")
    try:
        if num == "":
            break
        else:
            num = int(num)
            Q1.append(num)
    except:
        print(f"Enter a number")
stack = []
Q2 = []
for i in range(len(Q1)):
    if i <= 2:
        stack.append(Q1[i])
    else:
        Q2.append(Q1[i])
print(Q2)
reversed_queue = []

while stack:
    reversed_queue.append(stack.pop())
for i in Q2:
    reversed_queue.append(i)

print(reversed_queue)
