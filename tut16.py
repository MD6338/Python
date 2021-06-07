# f = open("ch.txt", "w")
# f = open("ch.txt", "a")
f = open("ch.txt", "r+") # Read and Write
print(f.read())
x = f.write("\nI am picking python very fast")
print(x)
f.close()