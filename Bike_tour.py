tc=int(input())
for _ in range(tc):
    n=int(input())
    count=0
    Hills=list(map(int,input().split()))
    for i in range(n-2):
        if Hills[i+1]>Hills[i] and Hills[i+1]>Hills[i+2]:
            count+=1
    print("Case #{}: {}".format(_+1,count))
