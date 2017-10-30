def change124(n):
    answer = ""
    while n > 0:
        n, a = divmod(n,3)
        if a == 0: n-=1
        answer = "412"[a]+answer
    return answer

print(1, change124(1))
print(2, change124(2))
print(3, change124(3))

print(4, change124(4))
print(5, change124(5))
print(6, change124(6))
print(7, change124(7))
print(8, change124(8))
print(9, change124(9))
"""
print(change124(10))

