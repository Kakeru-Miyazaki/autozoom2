import tkinter
root = tkinter.Tk()
root.title('AUTOZOOM2 --add URL--')
root.geometry("800x400")


class dataset:
  def __init__(self):
    self.day = "noinput"
    self.time = "noinput"
    self.name = "noinput"
    self.url = "noinput"

  def printData(self):
    print(self.day, self.time, self.name, self.url)

  def setDay(self, day):
    self.day = day

  def setTime(self, time):
    self.time = time

  def setName(self, name):
    self.name = name

  def setUrl(self, url):
    self.url = url


newData = dataset()


def register():
  flag = True
  if inputDay.get() != "":
    newData.setDay(inputDay.get())
  else:
    flag = False
  if inputTime.get() != "":
    newData.setTime(inputTime.get())
  else:
    flag = False

  if inputName.get() != "":
    newData.setName(inputName.get())
  else:
    flag = False

  if inputUrl.get() != "":
    newData.setUrl(inputUrl.get())
  else:
    flag = False
  if (flag):
    newData.printData()
    root.destroy()


button = tkinter.Button(root, text="register", command=register)
button.grid(column=0, row=9)

labelDay = tkinter.Label(text="the Day (Sun, Mon, Tue, Wed, Thu, Fri, Sat)")
labelDay.grid(column=0, row=0, padx=10, pady=5, sticky=tkinter.W)
inputDay = tkinter.Entry(width=40)
inputDay.grid(column=0, row=1, sticky=tkinter.W)

labelTime = tkinter.Label(text="the meeting time. (10-15 minute before of start is best. ex: 8:30 -> 0830, 13:07 -> 1307)")
labelTime.grid(column=0, row=3, padx=10, pady=5, sticky=tkinter.W)
inputTime = tkinter.Entry(width=40)
inputTime.grid(column=0, row=4, sticky=tkinter.W)

labelName = tkinter.Label(text="the meeting name")
labelName.grid(column=0, row=5, padx=10, pady=5, sticky=tkinter.W)
inputName = tkinter.Entry(width=40)
inputName.grid(column=0, row=6, sticky=tkinter.W)

labelURL = tkinter.Label(text="the meeting URL")
labelURL.grid(column=0, row=7, padx=10, pady=5, sticky=tkinter.W)
inputUrl = tkinter.Entry(width=40)
inputUrl.grid(column=0, row=8, sticky=tkinter.W)


root.mainloop()
