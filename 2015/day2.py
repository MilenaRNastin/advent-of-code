file = open("day2.txt")
paper = 0
ribbon = 0
for box in file:
    box = box.strip()
    dimensions = box.split("x")
    a = int(dimensions[0])
    b = int(dimensions[1])
    c = int(dimensions[2])
    side1 = a*b
    side2 = b*c
    side3 = a*c
    paper += 2*(side1+side2+side3)
    paper += min(side1,side2,side3)
    biggest = max(a,b,c)
    volume = a*b*c
    ribbon+=volume
    if(biggest==a):
        ribbon+=2*b+2*c 
    elif(biggest==b):
        ribbon+=2*a+2*c
    else:
        ribbon+=2*a+2*b
    
#part1
print(paper)
print(ribbon)