l = [["Memer","Good"], ["Gamer","Good"], ["Programmer","Better"]]
d = dict(l)

for items, rating in l:
    print(items, rating)

for items, rating in d.items():
    print(items, rating)

for keys in d:
    print(keys)


# Quiz
l2 = ["Chinmay","Programmer",24,1,3,45,6]
for items in l2:
    if type(items) == int:
        if items>=6:
            print(items)