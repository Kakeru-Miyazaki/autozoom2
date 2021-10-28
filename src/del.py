import sys
num = int(sys.argv[1])
fname = "data.txt"
file = open(fname, encoding='utf-8')
counter = 0
for row in file:
  counter += 1
  if (counter == num):
    continue
  print(row)
