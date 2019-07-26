a=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
if (l==[i*0 for i in range(len(l))]):
    print('0')
else:
    print(*l,sep="")
