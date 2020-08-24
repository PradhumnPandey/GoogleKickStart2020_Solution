tc=int(input())
for _ in range(tc):
    N,D=map(int,input().split())
    routes=list(map(int,input().split()))
    routes.reverse()
    for i in routes:
        if D%i==0:
            temp=D
        else:
            temp=int(D/i)*i
            while(temp>D):
                temp-=i
            D=temp
    print("Case #{}: {}".format(_+1,D))