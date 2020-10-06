from Tkinter import *
from MySQLdb import *
from os import system

def main():
	root=Tk()
	root.title("Institute of Tech")
	root.config(bg='black')
	f1=Frame()
	l1=Label(f1,text="Welcome!! to Institute of Tech ",font=("Verdana bold",30),fg="blue",bg='black')
	l1.pack()
	f1.pack()

	def exit():
		root.destroy()
	def student():
		root.destroy()
		system('python student_entry.py')
		main()
	def staff():
		root.destroy()
		system('python emp_entry.py')
		main()
	f100=Frame()
	l100=Label(f100,text="Select The option where you want to be navigated: ",font=("bold",10),fg="green",bg='black')
	l100.configure(background='black')
	f100.configure(bg='black')
	l100.pack()
	f100.pack()


	f2=Frame()
	l2=Label(f2,text="Students Portal ",font=("bold",10),bg='black',fg='white').grid(row=1)
	b1=Button(f2,text="Click Here",font=("bold",10),fg="light blue",bg="black",command=student).grid(row=1,column=2)
	l3=Label(f2,text="Staff Portal ",font=("bold",10),fg='white',bg='black').grid(row=2)
	b2=Button(f2,text="Click Here",font=("bold",10),fg="pink",bg="black",command=staff).grid(row=2,column=2)
	f2.config(bg='black')
	f2.pack()


	f4=Frame()
	l6=Label(f4,text="                          ",font=("bold",10),bg='black').pack(side=TOP)
	exit=Button(f4,text="Exit",font=("bold",10),fg="red",bg='black',command=exit)
	exit.config(bg='black')
	f4.config(bg='black')
	exit.pack(side=BOTTOM)
	f4.pack()

	mainloop()
main()

