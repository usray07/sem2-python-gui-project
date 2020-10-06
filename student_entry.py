from Tkinter import *
from MySQLdb import *
from delete_opr import S_rmove



def entry():
        root=Tk()
        root.title("Student Management System")
	root.config(bg='black')
        def ok():
                conobj=connect('localhost','','')
                curobj=conobj.cursor()
                #curobj.execute('Create database Students;')
                curobj.execute('use Students;')
                #curobj.execute('Create table signup(name varchar(40),uid int(40),college varchar(40),phno varchar(40),addr varchar(40),gender varchar(7));')
                if var.get()==1:
                        curobj.execute('insert into signup values("'+sname.get()+'","'+uid.get()+'","'+cname.get()+'","'+phn.get()+'","'+addr.get()+'","MALE");')
                if var.get()==2:
                        curobj.execute('insert into signup values("'+sname.get()+'","'+uid.get()+'","'+cname.get()+'","'+phn.get()+'","'+addr.get()+'","FEMALE");')

                curobj.close()
                conobj.close()

        def disp():
                root.destroy()
                display()
        def exit():
                root.destroy()

        f1=Frame()
        l1=Label(f1,text="Student Management System",font=("bold",50),fg="BLUE",bg='black')
        l1.pack()
        f1.config(bg='black')
        f1.pack()


        f2=Frame()
        l2=Label(f2,text="Enter Name ",font=("bold",10),fg='white',bg='black').grid(row=0)
        sname=Entry(f2,font=("bold",10),width=40,bg='black',fg='white')
	sname.grid(row=0,column=2)

        l0=Label(f2,text="Enter User ID ",font=("bold",10),fg='white',bg='black').grid(row=1)
        uid=Entry(f2,font=("bold",10),width=40,bg='black',fg='white')
	uid.grid(row=1,column=2)

        l3=Label(f2,text="Enter College Name ",font=("bold",10),fg='white',bg='black').grid(row=2)
        cname=Entry(f2,font=("bold",10),width=40,bg='black',fg='white')
	cname.grid(row=2,column=2)

        l5=Label(f2,text="Enter Phone Number ",font=("bold",10),fg='white',bg='black').grid(row=3)
        phn=Entry(f2,font=("bold",10),width=40,bg='black',fg='white')
	phn.grid(row=3,column=2)

        l6=Label(f2,text="Enter Address ",font=("bold",10),fg='white',bg='black').grid(row=4)
        addr=Entry(f2,font=("bold",10),width=40,bg='black',fg='white')
	addr.grid(row=4,column=2)
       
 
        var=IntVar()
        Radiobutton(f2,text="Male",variable=var,value=1,fg='white',bg='black').grid(row=5,column=1)
        Radiobutton (f2, text = "Female", variable = var,value=2,fg='white',bg='black').grid(row=5,column=2)
        l4=Label(f2,text="Enter Gender: ",font=("bold",10),fg='white',bg='black').grid(row=5)
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

def display():
        root=Tk()
        root.title("Database Page")
	root.config(bg='black')
        def exit():
                root.destroy()
        def back():
                root.destroy()
		entry()
        def delete():
                root.destroy()
                S_rmove()
        conobj=connect('localhost','','')
        curobj=conobj.cursor()
        curobj.execute('use Students;')
        f1=Frame()
        l1=Label(f1,text="Students Record",font=("bold",20),fg="blue",bg='black')
	f1.config(bg='black')
        l1.pack()
        f1.pack()

        f2=Frame()
	f2.config(bg='black')
        l21=Label(f2,text="Student Name",font=("bold",10),width=20,bg='black',fg='orange').grid(row=0)
        l22=Label(f2,text="User ID",font=("bold",10),width=10,bg='black',fg='white').grid(row=0,column=1)
        l22=Label(f2,text="College Name",font=("bold",10),width=20,bg='black',fg='green').grid(row=0,column=2)
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
                while j<len(row):
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


entry()

