import tkinter
from tkinter import ttk
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
  if comboboxDay.get() != "":
    newData.setDay(comboboxDay.get())
  else:
    flag = False
  if comboboxTimeHour.get() != "" and comboboxTimeMin != "":
    newData.setTime(comboboxTimeHour.get() + comboboxTimeMin.get())
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
# inputDay = tkinter.Entry(width=40)
# inputDay.grid(column=0, row=1, sticky=tkinter.W)

labelTime = tkinter.Label(text="the meeting time. (10-15 minute before of start is best.)")
labelTime.grid(column=0, row=3, padx=10, pady=5, sticky=tkinter.W)
# inputTime = tkinter.Entry(width=40)
# inputTime.grid(column=0, row=4, sticky=tkinter.W)

labelName = tkinter.Label(text="the meeting name")
labelName.grid(column=0, row=5, padx=10, pady=5, sticky=tkinter.W)
inputName = tkinter.Entry(width=40)
inputName.grid(column=0, row=6, sticky=tkinter.W, padx=10)

labelURL = tkinter.Label(text="the meeting URL")
labelURL.grid(column=0, row=7, padx=10, pady=5, sticky=tkinter.W)
inputUrl = tkinter.Entry(width=40)
inputUrl.grid(column=0, row=8, sticky=tkinter.W, padx=10)


moduleDay = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
moduleTimeHour = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')
moduleTimeMin = ('00', '05', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55')

# def select_combo(event):
#   print(combobox.get())


vDay = tkinter.StringVar()
vTimeHour = tkinter.StringVar()
vTimeMin = tkinter.StringVar()
comboboxDay = ttk.Combobox(root, textvariable=vDay, values=moduleDay, width=10, style="office.TCombobox")
comboboxDay.grid(column=0, row=1, sticky=tkinter.W, padx=10)
comboboxTimeHour = ttk.Combobox(root, textvariable=vTimeHour, values=moduleTimeHour, width=10, style="office.TCombobox")
comboboxTimeHour.grid(column=0, row=4, sticky=tkinter.W, padx=10)
comboboxTimeMin = ttk.Combobox(root, textvariable=vTimeMin, values=moduleTimeMin, width=10, style="office.TCombobox")
comboboxTimeMin.grid(column=0, row=4, padx=10)


def quit():
  root.destroy()


button = tkinter.Button(root, text="quit", command=quit)
button.grid(column=1, row=9)

root.protocol("WM_DELETE_WINDOW", quit)
root.mainloop()
