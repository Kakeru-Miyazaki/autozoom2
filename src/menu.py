# 関数を紐づけたボタンを配置
# --------------------------

import tkinter
root = tkinter.Tk()
root.title('AUTOZOOM2')
root.geometry("800x400")


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
button = tkinter.Button(root, text="Join The Meeting", command=joinMeeting, width=20,
                        height=10, fg="blue", font=("", "20", ))
button.grid(column=1, row=1)
button = tkinter.Button(root, text="Add URL", command=addUrl, width=10, height=5, font=("", "20"))
button.grid(column=0, row=1, sticky=tkinter.S)
button = tkinter.Button(root, text="Delete URL", command=delUrl, width=10, height=5, font=("", "20"))
button.grid(column=2, row=1, sticky=tkinter.S)


root.mainloop()
