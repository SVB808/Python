l=[]
n=int(input("\nEnter the number of elements: "))
for i in range(n):
  l.append(int(input()))
  
#Mean
mean = sum(list1)/len(list1)

# Median
l.sort()
if n % 2 == 0:
    median = (l[n//2] + l[n//2 - 1])/2
else:
    median = l[n//2]

# Mode
frequency = {}
for i in l:
    frequency.setdefault(i, 0)
    frequency[i]+=1
frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print("\nMean: "+mean+"\nMedian: "+median+"\nMode: "+mode)        
