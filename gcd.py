b,c=list(map(int,input().split()))
for i in range(c,0,-1):
    if b%i==0 and c%i==0:
        print(i)
        break
