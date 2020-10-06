from Tkinter import *
from MySQLdb import *
from os import system
from time import sleep
flag =-1

def E_rmove():
        root=Tk()
        root.title("Database Page")
        def exit():
                root.destroy()
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
        l20=Label(f2,text="Select",font=("bold",10),bg='black',fg='blue').grid(row=0)
        l21=Label(f2,text="Employee Name",font=("bold",10),width=20,bg='black',fg='orange').grid(row=0,column=1)
        l22=Label(f2,text="User ID",font=("bold",10),width=10,bg='black',fg='white').grid(row=0,column=2)
        l22=Label(f2,text="Department",font=("bold",10),width=20,bg='black',fg='green').grid(row=0,column=3)
        l24=Label(f2,text="Phone Number ",font=("bold",10),width=13,bg='black',fg='pink').grid(row=0,column=4)
        l23=Label(f2,text=" Address",font=("bold",10),width=30,bg='black',fg='light blue').grid(row=0,column=5)
        l25=Label(f2,text="Gender",font=("bold",10),width = 8,bg='black',fg='red').grid(row=0,column=6)

        curobj.execute('select * from signup ')
        rows=curobj.fetchall()

        i=0
        curobj.execute('select * from signup ')
        var=IntVar()
        while i<len(rows) :
                row=curobj.fetchone()

                j=0
                Radiobutton(f2,variable=var,value=row[1],bg='black',fg='white').grid(row=i+1)
                while j<len(row)-1:
                        data=row[j]
                        l=Label(f2,text=data,font=("bold",10),bg='black',fg='white').grid(row=i+1,column=j+1)
                        j+=1
                i+=1

        f2.pack()
        curobj.close()
        conobj.close()
        def back():
                root.destroy()
                system("python emp_entry.py")

        def Delete() :
		global flag
                if var.get() != 0:
			root.destroy()
			loginid('e')
			if flag==1:	
				conobj=connect('localhost','','')
				curobj=conobj.cursor()
				curobj.execute('use Employee;')
				var1=str(var.get())
				strcamp = "delete from signup where uid = " + var1 + ';'
				curobj.execute(strcamp)
				curobj.close()
				conobj.close()
				flag=-1
				E_rmove()
                else:
                        f0=Frame()
                        l0=Label(f0,text="Please Select One Entry to Delete!!!", fg='red')
                        l0.pack()
                        f0.pack()

        f3=Frame()
        Delete=Button(f3,text="Delete Selected",font=("bold",10),fg="red",bg='black',command=Delete)

        Delete.pack(side=LEFT)
        ok=Button(f3,text="Back to Entry Page",font=("bold",10),bg='black',fg='pink',command=back)
        ok.pack(side=LEFT)

        exit=Button(f3,text="Exit",font=("bold",10),fg="red",bg='black',command=exit)
        exit.pack(side=RIGHT)
	f3.config(bg='black')
        f3.pack()

        mainloop()

def S_rmove():
        root=Tk()
        root.title("Database Page")
        def exit():
                root.destroy()
        conobj=connect('localhost','','')
        curobj=conobj.cursor()
	curobj.execute('use Students;')
        
        f1=Frame()
        l1=Label(f1,text="Student Record",font=("bold",20),fg="light blue",bg='black')
        root.config(bg='black')
        l1.pack()
        f1.pack()

        f2=Frame()
        f2.config(bg='black')
        l20=Label(f2,text="Select",font=("bold",10),bg='black',fg='blue').grid(row=0)
        l21=Label(f2,text="Student Name",font=("bold",10),width=20,bg='black',fg='orange').grid(row=0,column=1)
        l22=Label(f2,text="User ID",font=("bold",10),width=10,bg='black',fg='white').grid(row=0,column=2)
        l22=Label(f2,text="College",font=("bold",10),width=20,bg='black',fg='green').grid(row=0,column=3)
        l24=Label(f2,text="Phone Number ",font=("bold",10),width=13,bg='black',fg='pink').grid(row=0,column=4)
        l23=Label(f2,text=" Address",font=("bold",10),width=30,bg='black',fg='light blue').grid(row=0,column=5)
        l25=Label(f2,text="Gender",font=("bold",10),width = 8,bg='black',fg='red').grid(row=0,column=6)

        curobj.execute('select * from signup ')
        rows=curobj.fetchall()

        i=0
        curobj.execute('select * from signup ')
        var=IntVar()
        while i<len(rows) :
                row=curobj.fetchone()
                j=0
                Radiobutton(f2,variable=var,value=row[1],bg='black',fg='white').grid(row=i+1)
                while j<len(row):
                        data=row[j]
                        l=Label(f2,text=data,font=("bold",10),bg='black',fg='white').grid(row=i+1,column=j+1)
                        j+=1
                i+=1
 	f2.pack()
        curobj.close()
        conobj.close()

        def back():
                root.destroy()
                system("python student_entry.py")

        def Delete() :
		global flag
                if var.get() != 0:
                	root.destroy()
			loginid('s')
                      	if flag==1:
				conobj=connect('localhost','','')
        	                curobj=conobj.cursor()
                	        curobj.execute('use Students;')
                        	var1=str(var.get())
                 		strcamp = "delete from signup where uid = " + var1 + ';'
				curobj.execute(strcamp)
				curobj.close()
				conobj.close()
				flag=-1
				S_rmove()
                else:
                        f0=Frame()
                        l0=Label(f0,text="Please Select One Entry to Delete!!!", fg='red')
                        l0.pack()
                        f0.pack()
        f3=Frame()
        Delete=Button(f3,text="Delete Selected",font=("bold",10),fg="red",bg='black',command=Delete)

        Delete.pack(side=LEFT)
        ok=Button(f3,text="Back to Entry Page",font=("bold",10),bg='black',fg='pink',command=back)
        ok.pack(side=LEFT)

        exit=Button(f3,text="Exit",font=("bold",10),fg="red",bg='black',command=exit)
        exit.pack(side=RIGHT)
        f3.config(bg='black')
        f3.pack()

	mainloop()

def loginid(grp):
        def exit():
                rt.destroy()
		if grp=='s':
			S_rmove()
		if grp=='e':
			E_rmove()
        def check():
		global flag
		if grp=='s' :
			conobj=connect('localhost','','')
			curobj=conobj.cursor()
			curobj.execute('use Employee;')
			curobj.execute('select * from signup ')
			rows=curobj.fetchall()
			if len(rows)==0:
				f01=Frame()
				f01.config(bg='black')
				l01=Label(f01,text="No Staff!! Admin Login Required!!", fg='red',bg='black')
				l01.pack()
				f01.pack()
				if user.get() == "Admin" :
					if pswd.get() == "uttam" :
						flag=1
						rt.destroy()
					else:
						f0=Frame()
						f0.config(bg='black')
						l0=Label(f0,text="Incorrect Password!!", fg='red',bg='black')
						l0.pack()
						f0.pack()
				else :
					f0=Frame()
					f0.config(bg='black')
					l0=Label(f0,text="Unauthorized Access!!", fg='red',bg='black')
					l0.pack()
					f0.pack()
			else :				
				curobj.close()
				conobj.close()
				lu=[]
				lp=[]
				i=0
				while i<len(rows):
					lu.append(rows[i][1])
					lp.append(rows[i][6])
					i+=1
				if int(user.get()) in lu :
					uindex=lu.index(int(user.get()))
					if pswd.get() == lp[uindex] :
						rt.destroy()
						flag=1
					else:
						f0=Frame()
						f0.config(bg='black')
						l0=Label(f0,text="Incorrect Password!!", fg='red',bg='black')
						l0.pack()
						f0.pack()
				else:
					f0=Frame()
					f0.config(bg='black')
					l0=Label(f0,text="Invalid User!!", fg='red',bg='black')
					l0.pack()
					f0.pack()
		if grp=='e' :
			if user.get() == "Admin" :
				if pswd.get() == "uttam" :
					flag=1
					rt.destroy()
				else:
					f0=Frame()
					f0.config(bg='black')
					l0=Label(f0,text="Incorrect Password!!", fg='red',bg='black')
					l0.pack()
					f0.pack()
			else :
				f0=Frame()
				f0.config(bg='black')
				l0=Label(f0,text="Unauthorized Access!!", fg='red',bg='black')
				l0.pack()
				f0.pack()
			
				
        rt=Tk()
        rt.title("Login Page")
	rt.config(bg='black')

        f20=Frame()
	f20.config(bg='black')
        l20=Label(f20,text="Enter Login Details",font=("bold",10),bg='black',fg='light blue')
        l20.pack()
	f20.pack()

        f21=Frame()
	f21.config(bg='black')

        l21=Label(f21,text="Enter User ID",font=("bold",10),bg='black',fg='pink').grid(row=0)
        l211=Label(f21,text="       ",font=("bold",10),bg='black').grid(row=0,column=1)
        user=Entry(f21,font=("bold",10),bg='black',fg='white',width=15)
        user.grid(row=0,column=2)

        l22=Label(f21,text="Enter Password",font=("bold",10),bg='black',fg='light green').grid(row=1)
        l212=Label(f21,text="       ",font=("bold",10),bg='black').grid(row=1,column=1)
        pswd=Entry(f21,font=("bold",10),bg='black',fg='white',width=15)
        pswd.grid(row=1,column=2)

        f21.pack()

        f23=Frame()
	f23.config(bg='black')

        b20=Button(f23,text="Submit",font=("bold",10),bg='black',fg='green',command=check)
        b20.pack(side=LEFT)

        b21=Button(f23,text="Close",font=("bold",10),bg='black',fg='red',command=exit)
        b21.pack(side=RIGHT)

        f23.pack()

	mainloop()
