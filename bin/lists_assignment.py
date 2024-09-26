fname = input("Enter file name: ")
fhand = open(fname)
lst = list()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)