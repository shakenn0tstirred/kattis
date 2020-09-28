# Brute force method used to keep track of adjustments made to maintain a full chess set.
k, q, r, b, kn, p = map(int, input().split())
kcount, qcount, rcount, bcount, kncount, pcount = 0, 0, 0, 0, 0, 0

while k != 1 or q != 1 or r != 2 or b != 2 or kn != 2 or p != 8:
    if k > 1:
        k-=1
        kcount -=1
    elif k < 1:
        k+=1
        kcount+=1
    elif q > 1:
        q-=1
        qcount -=1
    elif q < 1:
        q+=1
        qcount +=1
    elif r > 2:
        r-=1
        rcount -=1
    elif r < 2:
        r+=1
        rcount +=1
    elif b > 2:
        b-=1
        bcount -=1
    elif b < 2:
        b+=1
        bcount +=1
    elif kn > 2:
        kn-=1
        kncount -=1
    elif kn < 2:
        kn+=1
        kncount +=1
    elif p > 8:
        p-=1
        pcount -=1
    elif p < 8:
        p+=1
        pcount +=1

print(kcount,qcount,rcount,bcount,kncount,pcount)
