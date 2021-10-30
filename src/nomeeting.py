import tkinter
root = tkinter.Tk()
root.title('AUTOZOOM2 --add URL--')


def quit():
    root.destroy()


label1 = tkinter.Label(text="You have no meeting now.",
                       font=("", "32", "bold"))
label1.grid(column=1, row=1, padx=20, pady=5)
label2 = tkinter.Label(text="Take a coffee break :-)", font=("", "28", "bold"))
label2.grid(column=1, row=2, padx=20, pady=10)


button = tkinter.Button(root, text="OK", command=quit)
button.grid(column=1, row=4)


root.mainloop()
