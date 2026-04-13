tup=(1,2,3,1,2,4)
seen=[]
repeat=[]
for i in tup:
   if i in seen and i not in repeat:
      repeat.append(i)
   seen.append(i)
print(repeat)
