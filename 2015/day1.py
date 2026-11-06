file = open("day1.txt")
input = file.readline().strip()
file.close()
floor = 0
position = 1
found = False
for char in input:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    if floor<0:
        found = True
    if found == False:
        position+=1
#part 1
print(floor)
#part 2
print(position)


