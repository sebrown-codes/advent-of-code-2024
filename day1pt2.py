with open("day1_input.txt", "r") as f:
    data = f.read()
allnumbers = data

pairs = allnumbers.split("\n")

box = []
for pair in pairs: 
    indiv = pair.split("   ")
    box.extend(indiv)
left = box[::2]
right = box[1::2]

for l in range(len(left)):
    left[l] = int(left[l])

for r in range(len(right)):
    right[r] = int(right[r])

# lst_var.count(some_num) -> number of times some_num appears in lst_var
simscore = 0
for numb in left:
    sim = right.count(numb) * numb
    simscore = simscore + sim
print(simscore)