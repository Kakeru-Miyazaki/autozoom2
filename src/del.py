import tkinter as tk
import tkinter.ttk as ttk
from typing import Counter


main_win = tk.Tk()
main_win.title("AUTOZOOM2 --delete URL--")
main_win.geometry("800x400")

tree = ttk.Treeview(main_win)

# 列を作成（３列）
tree["columns"] = (1, 2, 3, 4)
# ヘッダーの設定
tree["show"] = "headings"
tree.heading(1, text="Number")
tree.heading(2, text="Day")
tree.heading(3, text="Time")
tree.heading(4, text="Name")
# 各列の幅設定

tree.column(1, width=50)
tree.column(2, width=50)
tree.column(3, width=50)
tree.column(4, width=400)
# データ挿入
fname = "data.txt"
file = open(fname, encoding='utf-8')
counter = 0
data = []
for row in file:
  counter += 1
  data.append(row)
  row = row.split()
  tree.insert("", "end", values=(str(counter), row[0], row[1][0:2] + ":" + row[1][2:], row[2]))
tree.pack()

vbar1 = ttk.Scrollbar(main_win, orient='v', command=tree.yview)

tree.configure(yscrollcommand=vbar1.set)

tree.pack(side=tk.LEFT)
tree.place(x=15, y=40, height=200)

vbar1.pack(side=tk.LEFT, fill=tk.Y)
vbar1.place(x=570, y=40, height=200)


label = tk.Label(text="input the numbe you want to delete ->")
label.grid(column=0, row=9, padx=5, pady=5, sticky=tk.E)
toDel = tk.Entry(width=40)
toDel.grid(column=1, row=9, sticky=tk.W)


def run():
  global counter
  if int(toDel.get()) and 1 <= int(toDel.get()) <= counter:
    delnum = int(toDel.get())
    counter = 0
    for row in data:
      counter += 1
      if (counter == delnum):
        continue
      print(row)
    main_win.destroy()


button = tk.Button(main_win, text="delete", command=run)
button.grid(column=2, row=9)

main_win.mainloop()


# import sys
# num = int(sys.argv[1])
# fname = "data.txt"
# file = open(fname, encoding='utf-8')
# counter = 0
# for row in file:
#   counter += 1
#   if (counter == num):
#     continue
#   print(row)
