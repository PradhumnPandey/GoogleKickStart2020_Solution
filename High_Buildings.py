def fill_common(arr,A,B,C,N):
    if C==1:
        if A==1:
            arr[0]=N
        elif B==1:
            arr[N-1]=N
        else:
            index=min(A,N-B)
            arr[index]=N
        N-=1
    else:
        f=0
        for i in range(A-C+1,N-B+2):
            arr[i]=N
            f+=1
        N-=f
    return arr,A-C,B-C,N
tc=int(input())
for _ in range(tc):
    N,A,B,C=map(int,input().split())
    outline=[0]*N
    temp=N
    k=1
    if (A==B and A==N and C!=A) or (A==N and B!=N) or(B==N and A!=N):
        print("Case #{}: IMPOSSIBLE".format(_+1))
        continue
    outline,A,B,N=fill_common(outline,A,B,C,N)
    
    for j in range(2):
        if k==1:
            A=B
            outline.reverse()
        while(A>0):
            A-=1
            outline[A]=N
            N-=1
        k=0
    outline.reverse()
    for i in range(temp):
        if outline[i]==0:
            outline[i]=N
            N-=1
    print("Case #{}: {}".format(_+1,outline))