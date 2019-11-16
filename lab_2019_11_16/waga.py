def waga(li,n,p):
    if n==0: return True
    if p==len(li): return False
    return waga(li,n-li[p],p+1) or waga(li,n,p+1) or waga(li,n+li[p],p+1)
# end def

odw = [1,3,5,10,16,24]

for i in range(1,49):
    print(waga(odw, i, 0))
