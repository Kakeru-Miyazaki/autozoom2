import subprocess
import tkinter
from tkinter.constants import FLAT
from PIL import Image, ImageTk
root = tkinter.Tk()
root.title('AUTOZOOM2')
root.geometry("950x500")
bgcolor = "black"
root.configure(bg=bgcolor)
# root.wm_attributes("-transparentcolor", "snow")


def joinMeeting():
  print("join")
  root.destroy()


def addUrl():
  print("add")
  root.destroy()


def delUrl():
  print("del")
  root.destroy()


pJoin = "../icon/button/join.png"
pAdd = "../icon/button/add.png"
pDel = "../icon/button/del.png"


# imageJoin = tkinter.PhotoImage(file=pJoin)
# imageAdd = tkinter.PhotoImage(file=pAdd)
# imageDel = tkinter.PhotoImage(file=pDel)

imageJoin = Image.open(pJoin)
imageAdd = Image.open(pAdd)
imageDel = Image.open(pDel)

imageJoin = imageJoin.resize((300, 300))
imageAdd = imageAdd.resize((300, 300))
imageDel = imageDel.resize((300, 300))


imageJoin = ImageTk.PhotoImage(imageJoin)
imageAdd = ImageTk.PhotoImage(imageAdd)
imageDel = ImageTk.PhotoImage(imageDel)

labelDay = tkinter.Label(text="AUTOZOOM2", font=("", "40", "bold"), fg="LightCyan", bg=bgcolor)
# labelDay.place(x=400, y=10)
labelDay.pack()
# labelDay.grid(column=1, row=0, padx=5, pady=5)
buttonJoin = tkinter.Button(root, text="Join The Meeting", command=joinMeeting, width=20,
                            height=10, font=("", "20", ), image=imageJoin, bg=bgcolor, relief=FLAT)
buttonJoin.place(x=330, y=60, width=300, height=300)
# buttonJoin.grid(column=1, row=1, padx=20, pady=5,width=100, height=140)
buttonAdd = tkinter.Button(
    root, text="Add URL", command=addUrl, width=10, height=5, font=("", "20"), image=imageAdd, bg=bgcolor, relief=FLAT)
buttonAdd.place(x=20, y=60, width=300, height=300)
# buttonAdd.grid(column=0, row=1, sticky=tkinter.S, padx=20, pady=5,width=100, height=140)
buttonDel = tkinter.Button(root, text="Delete URL",
                           command=delUrl, width=10, height=5, font=("", "20"), image=imageDel, bg=bgcolor, relief=FLAT)
buttonDel.place(x=640, y=60, width=300, height=300)

# buttonDel.grid(column=2, row=1, sticky=tkinter.S, padx=20, pady=5,width=100, height=140)

# root.grid_rowconfigure(1, weight=1)
# root.grid_rowconfigure(0, weight=1)

root.mainloop()
