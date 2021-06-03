# Dictionary is nothing but key value pairs
d = {"Chinmay":"8th sep", "Rohit":"3rd nov", "Samartha":"5th july", "Aseem":{"B":"20th april", "FavGame":"Minecraft"}}
print(d)
# print(d["Samartha"])
d["Dakshes"] = "17th"
del d["Dakshes"]
print(d)
print(d["Aseem"]["B"])
d2 = d.copy()
# print(d2)
print(d.get("Rohit"))
# d.update({"Rohit":"3rd November"})
d.update({"Varad":"20th"})
print(d)
print(d.keys())
print(d.items())
print(d.values())