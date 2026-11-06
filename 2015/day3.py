file = open("day3.txt")
input = file.readline()
input = input.strip()
houses = dict()
x = 0
y = 0
houses["0,0"]=1
for char in input:
    if char == '<':
        x -= 1
    if char == '>':
        x += 1
    if char == '^':
        y += 1
    if char == "v":
        y -= 1
    coords = str(x)+","+str(y)
    if coords in houses:
        houses[coords] = houses[coords] + 1
    else:
        houses[coords] = 1

#part1
print(len(houses))

houses2 = dict()
x1 = 0
y1 = 0
x2 = 0
y2 = 0
realturn = True
houses2["0,0"]=1
for char in input:
    if char == '<':
        if realturn==True:
            x1 -= 1
        else:
            x2 -= 1
    if char == '>':
       if realturn==True:
            x1 += 1
       else:
            x2 += 1
    if char == '^':
        if realturn==True:
            y1 += 1
        else:
            y2 +=1
    if char == "v":
        if realturn==True:
            y1 -= 1
        else:
            y2 -= 1

    if realturn==True:
        coords = str(x1)+","+str(y1)
        realturn = False
    else:
        coords = str(x2)+","+str(y2)
        realturn = True

    if coords in houses2:
        houses2[coords] = houses2[coords] + 1
    else:
        houses2[coords] = 1

#part 2
print(len(houses2))
