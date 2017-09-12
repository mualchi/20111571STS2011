"""
f=open("data.txt","r")
print(f.read(1)) # 한바이트만 읽어옴
print("")

f=open("data.txt","r")
print(f.read())
print("")

f=open("data.txt","r")
print(f.readlines())
print("")

f=open("data.txt","r")
r=f.readlines()
print(r[2])

f=open("data.txt","r")
r=f.readlines()
for x in range (0,4):
    print(r[x])


f=open("data.txt","r")
r=f.readlines()

for line in r:
    words=line.split()
    print(words)
"""
import collections as c
f=open("data.txt","r")
r1=f.read()
word = r1.split()
"""
for i in range(0, 20):
    print(i+1, word[i])
d={} # 딕셔너리 선언
for i in range(0, 20):
    print(i+1,word[i])
    d[word[i]] = 1 #모든 key값을 1로 지정
    
print(d)
"""

d={}
for i in word:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] =1

print(d)


