fname = input("Enter file name: ")
try:
   fhand = open(fname)
except:
   print('Error: Cannot open {fname}')
   exit()

count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[1])
    count += 1

print("There were", count, "lines in the file with From as the first word")
