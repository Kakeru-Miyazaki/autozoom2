import sys
import copy
youbi = sys.argv[1]
now = sys.argv[2]
mydict = {'Mon': '月', 'Tue': '火', 'Wed': '水', 'Thu': '木', 'Fri': '金', 'Sat': '土', 'Sun': '日'}
ans = ["first" for _ in range(3)]
fname = 'data.txt'
file = open(fname, encoding='utf-8')

for row in file:
  new = list(row.split())
  if ((new[0] == youbi or mydict[new[0]] == youbi) and int(new[1]) <= int(now)):
    ans = copy.copy(new)
if (ans[0] != "first"):
  print(ans[-1])
else:
  print("You have no meeting today.")
  sys.exit(1)
