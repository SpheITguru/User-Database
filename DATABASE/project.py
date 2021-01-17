from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')

class App:
	def __init__(self):

		self.window = Tk()
		self.window.title("User Database")
		self.window.geometry("960x740")

		self.frame0 = Frame(self.window,bg = "red")
		self.frame0.pack(fill = BOTH)

		self.headF = Frame(self.frame0)
		self.headF.pack()

		self.headImg = PhotoImage(file = "head.png")
		self.headImgAtrib = Label(self.headF,image = self.headImg, bg = "red")
		self.headImgAtrib.pack(side = RIGHT, fill = BOTH)

		self.head = Label(self.headF, text = "USER DATABASE", height = 3,width = 20, font = "bold", bg = "red")
		self.head.pack(side = LEFT, fill = BOTH)
		self.head.configure(font=("Arial", 30, "bold"))

		self.frame1 = LabelFrame(self.window, text = "Employee Database")
		self.frame1.pack()

		self.name = Label(self.frame1, text = "First Name : ")
		self.nameEntry = Entry(self.frame1, width = 30)
		self.surname = Label(self.frame1, text = "Last Name : ")
		self.surnameEntry = Entry(self.frame1, width = 30)
		self.cell = Label(self.frame1, text = "Cell Number : ")
		self.cellEntry = Entry(self.frame1, width = 30)
		self.ID = Label(self.frame1, text = "Employee ID : ")
		self.IDEntry = Entry(self.frame1, width = 30)
		self.position = Label(self.frame1, text = "Employee Posistion : ")
		self.posEntry = Entry(self.frame1, width = 30)

		self.name.grid(row = 1, column = 1, sticky = E)
		self.nameEntry.grid(row = 1, column = 2, sticky = E)
		self.surname.grid(row = 2, column = 1, sticky = E)
		self.surnameEntry.grid(row = 2, column = 2, sticky = E)
		self.cell.grid(row = 3, column = 1,sticky = E)
		self.cellEntry.grid(row = 3, column = 2)
		self.ID.grid(row = 4, column = 1, sticky = E)
		self.IDEntry.grid(row = 4, column = 2, sticky = E)
		self.position.grid(row = 5, column = 1, sticky = E)
		self.posEntry.grid(row = 5, column = 2, sticky = E)

		self.var = StringVar()

		self.male = Radiobutton(self.frame1,variable = self.var, text = "Male", value = "Male")
		self.female = Radiobutton(self.frame1,variable = self.var, text = "Female", value = "Female")
		self.male.grid(row = 1, column = 3, sticky = W)
		self.female.grid(row = 2, column = 3, sticky = W)

		self.add = Button(self.frame1, text = "ADD", width =7, command = self.add_item)		
		self.clear = Button(self.frame1, text = "CLEAR", width =7, command = self.clear_text)
		self.delete = Button(self.frame1, text = "DELETE", width =7, command = self.delete_item)
		self.add.grid(row = 6, column = 2, sticky = W)
		self.clear.grid(row = 6, column = 2)	
		self.delete.grid(row = 6, column = 2, sticky = E)		

		self.frameBottom = Frame(self.window, height = 30, bg = "red")
		self.frameBottom.pack(side = BOTTOM, fill = BOTH)

		self.dbframe = LabelFrame(self.window,width =115, height = 440)
		self.dbframe.pack()

		self.scrollbar = Scrollbar(self.dbframe)
		self.scrollbar.pack(side=RIGHT, fill=Y)

		self.employee_list = Listbox(self.dbframe, width =115, height = 440, font = ('Arial',12,'bold'), yscrollcommand = self.scrollbar.set)
		self.employee_list.configure(yscrollcommand = self.scrollbar.set)
		self.employee_list.pack()
		self.scrollbar.configure(command = self.employee_list.yview)
		# Bind select	
		self.employee_list.bind("<<ListboxSelect>>", self.select_item)


		self.copyRight = Label(self.frameBottom, text = "designed by Siphephelo Mlungwana", fg = "white", bg = "red")
		self.copyRight.pack(side = RIGHT)

		#popupale data
		self.populate_list()	

	def populate_list(self):
		self.employee_list.delete(0,END)
		for row in db.fetch():
			self.employee_list.insert(END,row)

	def add_item(self):
		if(self.nameEntry.get() == '' or self.surnameEntry.get()== '' or self.cellEntry.get()== '' or self.IDEntry.get()== '' or self.posEntry.get()== '' or self.var.get()==''):
			messagebox.showerror('Required Fields', 'Please include all fields')
			return
		db.insert(self.nameEntry.get(), self.surnameEntry.get(), self.cellEntry.get(), self.IDEntry.get(), self.posEntry.get(), self.var.get())
		self.employee_list.delete(0,END)
		self.employee_list.insert(END, self.nameEntry.get(), self.surnameEntry.get(), \
			self.cellEntry.get(), self.IDEntry.get(), self.posEntry.get(), self.var.get())
		self.populate_list()
		self.clear_text()

	def select_item(self, event):
		try:		
			global selected_item 
			self.index = self.employee_list.curselection()[0]
			selected_item = self.employee_list.get(self.index)

			self.nameEntry.delete(0,END)
			self.nameEntry.insert(END, selected_item[1])
			self.surnameEntry.delete(0,END)
			self.surnameEntry.insert(END, selected_item[2])
			self.cellEntry.delete(0,END)
			self.cellEntry.insert(END, selected_item[3])
			self.IDEntry.delete(0,END)
			self.IDEntry.insert(END, selected_item[4])
			self.posEntry.delete(0,END)
			self.posEntry.insert(END, selected_item[5])	
		except IndexError:
			pass

	def delete_item(self):
		db.remove(selected_item[0])
		self.populate_list()
		self.clear_text()

	def clear_text(self):
		self.nameEntry.delete(0,END)
		self.surnameEntry.delete(0,END)
		self.cellEntry.delete(0,END)
		self.IDEntry.delete(0,END)
		self.posEntry.delete(0,END)
		
		mainloop()


if __name__ == '__main__':
	App()