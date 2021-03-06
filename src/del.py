import tkinter
import tkinter.ttk as ttk
from typing import Counter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title("AUTOZOOM2 --delete URL--")
root.minsize(width=600, height=500)
# bgcolor = "aquamarine1"
# root.configure(bg=bgcolor)
tree = ttk.Treeview(root)

v = tkinter.StringVar()
module_l = []

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
  module_l.append(counter)
  data.append(row)
  row = row.split()
  tree.insert("", "end", values=(
      str(counter), row[0], row[1][0:2] + ":" + row[1][2:], row[2:-1]))

file.close()

# tree.pack()

vbar1 = ttk.Scrollbar(root, orient='v', command=tree.yview)

tree.configure(yscrollcommand=vbar1.set)

s = ttk.Style()
s.configure('Treeview', rowheight=40)

# tree.pack(side=tkinter.LEFT)
tree.grid(column=0, row=1, columnspan=3, rowspan=30, padx=15,
          sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)
# tree.place(x=15, y=40, height=200)

# vbar1.pack(side=tkinter.LEFT, fill=tkinter.Y)
vbar1.grid(column=4, row=1, rowspan=30, sticky=tkinter.E + tkinter.N + tkinter.S)
# vbar1.place(x=570, y=40, height=200)


label = tkinter.Label(text="input the number you want to delete ->")
label.grid(column=0, row=0, padx=5, pady=5, sticky=tkinter.E)
toDel = tkinter.Entry(width=40)
# toDel.grid(column=1, row=0, sticky=tkinter.W)

module = tuple(module_l)
comboboxDel = ttk.Combobox(root, textvariable=v,
                           values=module, width=10, style="office.TCombobox")
comboboxDel.grid(column=1, row=0, sticky=tkinter.W)


def run():
  global counter
#   if int(toDel.get()) and 1 <= int(toDel.get()) <= counter:
  if int(comboboxDel.get()) and 1 <= int(comboboxDel.get()) <= counter:
    delnum = int(comboboxDel.get())
    counter = 0
    for row in data:
      counter += 1
      if (counter == delnum):
        continue
      print(row)
    root.destroy()


def quit():
  for row in data:
    print(row)
  root.destroy()


pDel = "../icon/button/delete.png"
pQuit = "../icon/button/quit.png"

imageDel = Image.open(pDel)
imageQuit = Image.open(pQuit)

imageDel = imageDel.resize((90, 35))
imageQuit = imageQuit.resize((90, 35))

imageDel = ImageTk.PhotoImage(imageDel)
imageQuit = ImageTk.PhotoImage(imageQuit)


button = tkinter.Button(root, text="delete", command=run, image=imageDel)
button.grid(column=2, row=0)

button = tkinter.Button(root, text="quit", command=quit, image=imageQuit)
button.grid(column=3, row=0)


# root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)
# root.grid_columnconfigure(2, weight=1)
# root.grid_columnconfigure(3, weight=1)
# root.grid_columnconfigure(4, weight=1)
# root.grid_rowconfigure(0, weight=1)
# root.grid_rowconfigure(1, weight=1)
# root.grid_rowconfigure(2, weight=1)
# root.grid_rowconfigure(3, weight=1)
# root.grid_rowconfigure(4, weight=1)
# root.grid_rowconfigure(5, weight=1)
# root.grid_rowconfigure(6, weight=1)
# root.grid_rowconfigure(7, weight=1)
# root.grid_rowconfigure(8, weight=1)
# root.grid_rowconfigure(9, weight=1)


root.protocol("WM_DELETE_WINDOW", quit)
root.mainloop()
