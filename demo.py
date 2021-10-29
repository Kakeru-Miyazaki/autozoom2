# 関数を紐づけたボタンを配置
# --------------------------

import tkinter
root = tkinter.Tk()
root.title('AUTOZOOM2 --add URL--')
root.geometry("800x400")


# コンソールに"Button is clicked."を出力する関数


def newtxt_func(dataset):
  datafile = open("newtxt.txt", "w")
  test = "ok?"
  datafile.write(test)
  datafile.close()


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
button.grid(column=1, row=4)

labelDay = tkinter.Label(text="Day")
labelDay.grid(column=0, row=0, padx=5, pady=10)
inputDay = tkinter.Entry(width=40)
inputDay.grid(column=1, row=0)

labelTime = tkinter.Label(text="Time")
labelTime.grid(column=0, row=1, padx=5, pady=10)
inputTime = tkinter.Entry(width=40)
inputTime.grid(column=1, row=1)

labelName = tkinter.Label(text="Name")
labelName.grid(column=0, row=2, padx=5, pady=10)
inputName = tkinter.Entry(width=40)
inputName.grid(column=1, row=2)

labelURL = tkinter.Label(text="URL")
labelURL.grid(column=0, row=3, padx=5, pady=10)
inputUrl = tkinter.Entry(width=40)
inputUrl.grid(column=1, row=3)


root.mainloop()
