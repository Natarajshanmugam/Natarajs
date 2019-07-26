a1=int(input())
l1=list(map(int,input().split()))
l2=[]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if(l1[i]==l1[j]):
            l2.append(l1[i])
            
if(l2==[]):
    print("unique")
else:
    l2.sort()
    print(*l2)
