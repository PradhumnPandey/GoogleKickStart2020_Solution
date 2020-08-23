tc=int(input())
for _ in range(tc):
    l=int(input())
    arr=list(map(int,input().split()))
    Diff=[]
    out=[]
    count=0
    match=arr[0]-arr[1]
    for i in range(1,l):
        Diff.append(arr[i-1]-arr[i])
        if Diff[i-1]==match:
            count+=1
        else:
            match=Diff[i-1]
            out.append(count)
            count=1
    out.append(count)
    print("Case #{}: {}".format(_+1,max(out)+1))
