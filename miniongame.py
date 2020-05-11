#With Quadratic time complexity O(n^2)

a=input("")
def minion_game(n):
    l=[]
    s=[]
    j=0
    for i in n:
        if i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
            l.append(n[j:])
        j+=1
    for g in l:
        z=0
        for h in g:
            s.append(g[:(-1-z)])
            z=z+1
    for k in range(len(s)):
        for q in s:
            if q=="":
                s.remove(q)
    for i in s:
        l.append(i)
    print(len(l))
    k = []
    d = []
    j = 0
    for i in n:
        if i!="A" and i!="E" and i!="I" and i!="O" and i!="U":
            k.append(n[j:])
        j+=1
    for g in k:
        z=0
        for h in g:
            d.append(g[:(-1-z)])
            z=z+1
    for m in range(len(d)):
        for q in d:
            if q=="":
                d.remove(q)
    for i in d:
        k.append(i)
    print(len(k))
    if len(k)<len(l):
        print(f"Kevin {len(l)}")
    elif len(k)==len(l):
        print("Draw")
    else:
        print(f"Stuart {len(k)}")
minion_game(a)
