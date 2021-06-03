l = ["C","C++","Python","Java","C#"]
print(l)
print(l[0])
n = [24, 64, 19, 34]
# n.sort()
# n.reverse()
n.append(37)
n.insert(3, 155)
n.remove(24)
n.pop(2)
print(n)
print(l[:5])
print(len(l))
print(max(n))
print(min(n))
n[1] = 30
print(n)

# Mutable - can change, eg. list
# Immutable - cannot change, eg. tuple
t = (12,21,92)
# tp = (2,)
print(t)

n1 = 54
n2 = 24
n1, n2 = n2, n1
# temp = n1
# n1 = n2
# n2 = temp
print(n1, n2)