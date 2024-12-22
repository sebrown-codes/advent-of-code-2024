"""
Make a list of all the numbers in both columns, use the pop thingy to remove numbers from the list
Tell the computer to find the smallest number in each column and then remove it and then loop that process
Need to compare the two numbers in both columns and find the different between them (subtraction)
Add the distance between each pair together to find the total distance
ABSOLUTE VALUE IS COOL - makes a negative number a positive and a positive a positive wowwww
Make the lists by splitting them by \n and then by each number

1. Tell the computer to recognise that it's two different columns 
2. Tell the computer HOW to find the smallest number in each column 
3. Tell the computer to subtract left column number from the right column number
4. Remove the smallest number from each list (pop)
5. REPEAT (loop)
6. When the distance of all the pairs is found add them together
"""
with open("day1_input.txt", "r") as f:
    data = f.read()
allnumbers = data
#every number is under data in both columns seperated by /n (each row is seperated by \n)
pairs = allnumbers.split("\n")
# for var in lst:
# for i in range(len(lst)):
box = []
for pair in pairs: 
    indiv = pair.split("   ")
    box.extend(indiv)
left = box[::2]
right = box[1::2]
# the first variable is assigned in every iteration of the loop to the next thing in the list
for l in range(len(left)):
    left[l] = int(left[l])

for r in range(len(right)):
    right[r] = int(right[r])

totaldistance = 0
for small in range(len(left)):
    smallestleft = min(left)
    smallestright = min(right)
    distance = abs(smallestleft - smallestright)
    left.remove(smallestleft)
    right.remove(smallestright)
    totaldistance = totaldistance + distance
print(totaldistance)

#for sl in left:
    #smallestleft = min(left)
#for sr in right:
    #smallestright = min(right)