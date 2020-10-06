from Tkinter import *
from MySQLdb import *
from os import system
from delete_opr import E_rmove

def e_entry():
        root=Tk()
        root.title("Faculty Management System")
	root.config(bg='black')
        def ok():
		if cpwd.get() == pwd.get():
	
			conobj=connect('localhost','','')
			curobj=conobj.cursor()
			#curobj.execute('Create database Employee;')
			curobj.execute('use Employee;')
			#curobj.execute('Create table signup(name varchar(30),uid int(10),dept varchar(50),phno varchar(30),addr varchar(40),gender varchar(7),pwd varchar(30));')
			if var.get()==1:
				curobj.execute('insert into signup values("'+ename.get()+'","'+uid.get()+'","'+dept.get()+'","'+phn.get()+'","'+addr.get()+'","MALE","'+pwd.get()+'");')
			if var.get()==2:
				curobj.execute('insert into signup values("'+ename.get()+'","'+uid.get()+'","'+dept.get()+'","'+phn.get()+'","'+addr.get()+'","FEMALE","'+pwd.get()+'");')
			
			curobj.close()
			conobj.close()
			f10 = Frame()
			l10=Label(f10,text="Successfully Added!!",font=("bold",10),fg="green",bg='black')
			f10.config(bg='black')
			l10.pack(side=LEFT)
			f10.pack()
		else:
			f10 = Frame()
			l10=Label(f10,text="Passwords donot match!!",font=("bold",10),fg="red",bg='black')
			f10.config(bg='black')
			l10.pack(side=LEFT)
			f10.pack()

        def disp():
                root.destroy()
                e_display()
	def exit():
		root.destroy()

        f1=Frame()
        l1=Label(f1,text="Employee Management System",font=("bold",50),fg="BLUE",bg="black")
	f1.config(bg='black')
        l1.pack()
        f1.pack()

        f2=Frame()
        l2=Label(f2,text="Enter Name ",font=("bold",10),fg='white',bg='black').grid(row=0)
        ename=Entry(f2,font=("bold",10),width=30,bg='black',fg='white')
        ename.grid(row=0,column=2)

        l0=Label(f2,text="Enter User ID ",font=("bold",10),fg='white',bg='black').grid(row=1)
        uid=Entry(f2,font=("bold",10),width=30,bg='black',fg='white')
        uid.grid(row=1,column=2)

        l3=Label(f2,text="Enter Department ",font=("bold",10),fg='white',bg='black').grid(row=2)
        dept=Entry(f2,font=("bold",10),width=30,bg='black',fg='white')
       	dept.grid(row=2,column=2)

        l5=Label(f2,text="Enter Phone Number ",font=("bold",10),fg='white',bg='black').grid(row=3)
        phn=Entry(f2,font=("bold",10),width=30,bg='black',fg='white')
        phn.grid(row=3,column=2)

        l6=Label(f2,text="Enter Address ",font=("bold",10),fg='white',bg='black').grid(row=4)
        addr=Entry(f2,font=("bold",10),width=30,bg='black',fg='white')
        addr.grid(row=4,column=2)
 
 
        var=IntVar()
        Radiobutton(f2,text="Male",variable=var,value=1,fg='white',bg='black').grid(row=5,column=1)
        Radiobutton (f2, text = "Female", variable = var,value=2,fg='white',bg='black').grid(row=5,column=2)
        l4=Label(f2,text="Enter Gender: ",font=("bold",10),fg='white',bg='black').grid(row=5)

        l6=Label(f2,text="Enter Password ",font=("bold",10),fg='white',bg='black').grid(row=6)
        pwd=Entry(f2,font=("bold",10),width=30,bg='black',fg='white')
        pwd.grid(row=6,column=2)
	
        l7=Label(f2,text="Confirm Password ",font=("bold",10),fg='white',bg='black').grid(row=7)
        cpwd=Entry(f2,font=("bold",10),width=30,bg='black',fg='white')
        cpwd.grid(row=7,column=2)
        f2.config(bg='black')
        f2.pack()

        f7=Frame()
        f7.config(bg='black')
        ok=Button(f7,text="Save Entry",font=("bold",10),fg="green",bg='black',command=ok)
        ok.pack(side=LEFT)
        displ=Button(f7,text="Display Entries",font=("bold",10),bg='black',fg='pink',command=disp)
        displ.pack(side=LEFT)
        exit=Button(f7,text="Exit",font=("bold",10),fg="red",bg='black',command=exit)
        exit.pack(side=RIGHT)
        f7.pack()
	
	mainloop()

def e_display():
        root=Tk()
        root.title("Database Page")
	root.config(bg='black')
        def back():
                root.destroy()
		e_entry()
	def exit():
		root.destroy()
        def delete():
                root.destroy()
                E_rmove()
        conobj=connect('localhost','','')
        curobj=conobj.cursor()
        curobj.execute('use Employee;')
        f1=Frame()
        l1=Label(f1,text="Employee Record",font=("bold",20),fg="light blue",bg='black')
	root.config(bg='black')
        l1.pack()
        f1.pack()

        f2=Frame()
        f2.config(bg='black')
        l21=Label(f2,text="Employee Name",font=("bold",10),width=20,bg='black',fg='orange').grid(row=0)
        l22=Label(f2,text="User ID",font=("bold",10),width=10,bg='black',fg='white').grid(row=0,column=1)
        l22=Label(f2,text="Department",font=("bold",10),width=20,bg='black',fg='green').grid(row=0,column=2)
        l24=Label(f2,text="Phone Number ",font=("bold",10),width=13,bg='black',fg='pink').grid(row=0,column=3)
        l23=Label(f2,text=" Address",font=("bold",10),width=30,bg='black',fg='light blue').grid(row=0,column=4)
        l25=Label(f2,text="Gender",font=("bold",10),width = 8,bg='black',fg='red').grid(row=0,column=5)

        curobj.execute('select * from signup ')
        rows=curobj.fetchall()

        i=0
        curobj.execute('select * from signup ')
        while i<len(rows) :
                row=curobj.fetchone()
                j=0
                while j<len(row)-1:
                        data=row[j]
                        l=Label(f2,text=data,font=("bold",10),bg='black',fg='white').grid(row=i+1,column=j)
                        j+=1
                i+=1

        f2.pack()

        f3=Frame()
        ok=Button(f3,text="Back to Entry Page",font=("bold",10),fg="green",bg='black',command=back)
        ok.pack(side=LEFT)
        delete=Button(f3,text="Delete Entry(s)",font=("bold",10),bg='black',fg='white',command=delete)
        delete.pack(side=LEFT)
        exit=Button(f3,text="Exit",font=("bold",10),fg="red",bg='black',command=exit)
        exit.pack(side=RIGHT)
        f3.config(bg='black')
        f3.pack()

        curobj.close()
        conobj.close()
        mainloop()

e_entry()

