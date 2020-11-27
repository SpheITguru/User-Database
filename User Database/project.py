from tkinter import *
import time
import datetime

class App:
	def __init__(self):
		window = Tk()
		window.title("User Database")
		window.geometry("960x740")

		frame0 = Frame(window,bg = "red")
		frame0.pack(fill = BOTH)

		headF = Frame(frame0)
		headF.pack()

		headImg = PhotoImage(file = "head.png")
		headImgAtrib = Label(headF,image = headImg, bg = "red")
		headImgAtrib.pack(side = RIGHT, fill = BOTH)

		head = Label(headF, text = "USER DATABASE", height = 3,width = 20, font = "bold", bg = "red")
		head.pack(side = LEFT, fill = BOTH)
		head.configure(font=("Arial", 30, "bold"))

		frame1 = LabelFrame(window, text = "Employee Database")
		frame1.pack()

		name = Label(frame1, text = "First Name : ")
		nameEntry = Entry(frame1, width = 30)
		surname = Label(frame1, text = "Last Name : ")
		surnameEntry = Entry(frame1, width = 30)
		cell = Label(frame1, text = "Cell Number : ")
		cellEntry = Entry(frame1, width = 30)
		ID = Label(frame1, text = "Employee ID : ")
		IDEntry = Entry(frame1, width = 30)
		position = Label(frame1, text = "Employee Posistion : ")
		posEntry = Entry(frame1, width = 30)


		name.grid(row = 1, column = 1, sticky = E)
		nameEntry.grid(row = 1, column = 2, sticky = E)
		surname.grid(row = 2, column = 1, sticky = E)
		surnameEntry.grid(row = 2, column = 2, sticky = E)
		cell.grid(row = 3, column = 1,sticky = E)
		cellEntry.grid(row = 3, column = 2)
		ID.grid(row = 4, column = 1, sticky = E)
		IDEntry.grid(row = 4, column = 2, sticky = E)
		position.grid(row = 5, column = 1, sticky = E)
		posEntry.grid(row = 5, column = 2, sticky = E)

		male = Radiobutton(frame1, text = "Male", value = 0)
		female = Radiobutton(frame1, text = "Female", value = 1)
		male.grid(row = 1, column = 3, sticky = W)
		female.grid(row = 2, column = 3, sticky = W)

		add = Button(frame1, text = "ADD", width =7)		
		update = Button(frame1, text = "UPDATE", width =7)
		delete = Button(frame1, text = "DELETE", width =7)
		add.grid(row = 6, column = 2, sticky = W)
		update.grid(row = 6, column = 2)	
		delete.grid(row = 6, column = 2, sticky = E)

		frameBottom = Frame(window, height = 30, bg = "red")
		frameBottom.pack(side = BOTTOM, fill = BOTH)

		dbframe = LabelFrame(window,width =115, height = 440)
		dbframe.pack()

		textArea1 = Text(dbframe, height = 1, width = 117)
		textArea1.pack()

		textArea = Text(dbframe, height = 22, width = 115)
		textArea.pack()

		S = Scrollbar(dbframe)
		S.pack(side=RIGHT, fill=Y)
		textArea.pack(side=LEFT, fill=Y)
		S.config(command=textArea.yview)
		textArea.config(yscrollcommand=S.set)

		textHeader = "USER ID  |  FIRST NAME   |  LAST NAME  | CELL NUMBER  |  GENDER  |  POSITION  | "
		textArea1.insert(END, textHeader)	


		copyRight = Label(frameBottom, text = "designed by Siphephelo Mlungwana", fg = "white", bg = "red")
		copyRight.pack(side = RIGHT)

		mainloop()

if __name__ == '__main__':
	App()