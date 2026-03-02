queue = []

while True:
    number = input("Enter the number and will break if entered character : ")
    try:
        number = int(number)
        queue.append(number)
        if len(queue) > 5:
            queue.pop(0)
    except:
        break

print(queue)
