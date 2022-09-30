l=[]
n=int(input('Enter number of elements: '))
print('Enter the numbers: ')
for i in range(n):
    l.append(int(input()))
#mean
mean=sum(l)/len(l)
#mode
freq={}
for i in l:
    freq.setdefault(i,0)
    freq[i]+=1
frequent=max(freq.values())
for i,j in freq.items():
    if(j == frequent):
        mode = i
#median
l.sort()
if(len(l)%2 == 0):
    median = (l[n//2]+l[(n//2)-1])/2
else:
    median = l[n//2]
#printing values
print('\nMean: '+str(mean)+'\nMode: '+str(mode)+'\nMedian: '+str(median))