# Set doesn't allow duplicates
s = set()
print(type(s))
s.add(24)
s1 = s.union({32,42,36,24})
# s1 = s.intersection({32,42,36,24})
s1.remove(32)
print(s1,s)