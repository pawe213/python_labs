from pprint import pprint

try:
  t={}
  f=open("tekst.txt","r",encoding="utf-8")
  for line in f:
    for x in line.strip().split():
      t.setdefault(x, 0)
      t[x] = t[x]+1
    print(line) #, end="")
  # end
  f.close()
  lp2 = sorted(t.items(), key=lambda x: x[1], reverse=True)
  print(lp2)
except:
  print("problem!")
# end



