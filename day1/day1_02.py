f=open("data.txt","r")
r1=f.read()
word = r1.split()
d={}
for i in word:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] =1

analyze = {}
for x in word:
    analyze[x] = analyze.get(x, 0) + 1

flist = sorted(analyze.items(), key=lambda kv: kv[1], reverse=True)
print("number of words is ", len(flist))

cnt = 0
for k, v in flist:
    print(k, v)
    if cnt > 100: break
    cnt += 1
