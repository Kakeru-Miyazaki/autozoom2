import tkinter
import tkinter.ttk as ttk
from typing import Counter


root = tkinter.Tk()
root.title("AUTOZOOM2 --delete URL--")

tree = ttk.Treeview(root)

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
    tree.insert("", "end", values=(
        str(counter), row[0], row[1][0:2] + ":" + row[1][2:], row[2]))
file.close()

tree.pack()

vbar1 = ttk.Scrollbar(root, orient='v', command=tree.yview)

tree.configure(yscrollcommand=vbar1.set)

tree.pack(side=tkinter.LEFT)
tree.place(x=15, y=40, height=200)

vbar1.pack(side=tkinter.LEFT, fill=tkinter.Y)
vbar1.place(x=570, y=40, height=200)


label = tkinter.Label(text="input the numbe you want to delete ->")
label.grid(column=0, row=9, padx=5, pady=5, sticky=tkinter.E)
toDel = tkinter.Entry(width=40)
toDel.grid(column=1, row=9, sticky=tkinter.W)


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
        root.destroy()


def quit():
    for row in data:
        print(row)
    root.destroy()


button = tkinter.Button(root, text="delete", command=run)
button.grid(column=2, row=9)

button = tkinter.Button(root, text="quit", command=quit)
button.grid(column=3, row=9)


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
# root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)
root.grid_rowconfigure(8, weight=1)
root.grid_rowconfigure(9, weight=1)


root.protocol("WM_DELETE_WINDOW", quit)
root.mainloop()
