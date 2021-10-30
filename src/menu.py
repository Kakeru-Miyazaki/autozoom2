import tkinter
root = tkinter.Tk()
root.title('AUTOZOOM2')


def joinMeeting():
    print("join")
    root.destroy()


def addUrl():
    print("add")
    root.destroy()


def delUrl():
    print("del")
    root.destroy()


labelDay = tkinter.Label(text="AUTOZOOM2", font=("", "32", "bold"))
labelDay.grid(column=1, row=0, padx=5, pady=5)
buttonJoin = tkinter.Button(root, text="Join The Meeting", command=joinMeeting, width=20,
                            height=10, font=("", "20", ))
buttonJoin.grid(column=1, row=1, padx=20, pady=5)
buttonAdd = tkinter.Button(
    root, text="Add URL", command=addUrl, width=10, height=5, font=("", "20"))
buttonAdd.grid(column=0, row=1, sticky=tkinter.S, padx=20, pady=5)
buttonDel = tkinter.Button(root, text="Delete URL",
                           command=delUrl, width=10, height=5, font=("", "20"))
buttonDel.grid(column=2, row=1, sticky=tkinter.S, padx=20, pady=5)

root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

root.mainloop()
