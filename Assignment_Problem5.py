def palrec(s,n):
    mat=[[0]*(n+1) for x in range(n+1)]
    # left->Start(y) 
    # top-> end(x)
    # substrings of len 1 is always palindome
    for diag in range(n+1):
        mat[diag][diag]=1

    # substrings from len 2 can be palidrome in 2 conditions
    # 1. first and last char is same
    # 2. rest of its inner chars are already palindorme
    last=[0,0]
    for tilt in range(1,n+1):
        y=0
        x=tilt
        while x <=n and y<=n:
            if x-y==1: #1st iteration
                if s[y]==s[x]:
                    mat[y][x]=1
                    last=[y,x]
            else:
                if s[y]==s[x] and mat[y+1][x-1]==1:
                    mat[y][x]=1
                    last=[y,x]
            x+=1
            y+=1

    return s[last[0]: last[1]+1]


s="cbbd"

print(palrec(s,len(s)-1))
