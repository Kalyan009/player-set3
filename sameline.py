q,w=list(map(int,input().split()))
e,r=list(map(int,input().split()))
t,y=list(map(int,input().split()))
if q==w or e==r or t==y or q==e==y or w==r==t:
    print('yes')
else:
    print('no')
