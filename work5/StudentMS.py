#DataEntryFrame ke button ka kaam
def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobval.get()
        email = emailval.get()
        address = addval.get()
        gender = genderval.get()
        dob = DOBval.get()
        addedtime= time.strftime('%H:%M:%S')
        addeddate= time.strftime('%d/%m/%Y')
        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addedtime,addeddate))
            con.commit()
            res = messagebox.askyesnocancel('Notification','Id {} Name {} Added succesfully and do you want to clean the form'.format(id,name),parent=addroot)
            if res == True:
                id = idval.set('')
                name = nameval.set('')
                mobile = mobval.set('')
                email = emailval.set('')
                address = addval.set('')
                gender = genderval.set('')
                dob = DOBval.set('')
        except:
            messagebox.showerror('Notification','Id already exist try another Id',parent=addroot)
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for i in datas:
            vr = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studentTable.insert('',END,values=vr)
        
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+140+120')
    addroot.title("Stud Manage Sys")
    addroot.config(bg='green')
    addroot.iconbitmap('1.ico')
    addroot.resizable(False,False)
    
    #menu in add student option
    idlabel1= Label(addroot,text="enter id:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel1.place(x=10,y=10)
    namelabel1= Label(addroot,text="enter name:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel1.place(x=10,y=70)
    moblabel1= Label(addroot,text="enter mobile:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    moblabel1.place(x=10,y=130)
    emaillabel1= Label(addroot,text="enter email:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel1.place(x=10,y=190)
    addlabel1= Label(addroot,text="enter address:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addlabel1.place(x=10,y=250)
    genderlabel1= Label(addroot,text="enter gender:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel1.place(x=10,y=310)
    DOBlabel1= Label(addroot,text="enter DOB:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    DOBlabel1.place(x=10,y=370)

    idval= StringVar()
    nameval= StringVar()
    mobval= StringVar()
    emailval= StringVar()
    addval= StringVar()
    genderval= StringVar()
    DOBval= StringVar()
    
    a1=Entry(addroot,font=('roamn',15,'bold'),bd=5,textvariable=idval)
    a1.place(x=230,y=10)

    a2=Entry(addroot,font=('roamn',15,'bold'),bd=5,textvariable=nameval)
    a2.place(x=230,y=70)

    a3=Entry(addroot,font=('roamn',15,'bold'),bd=5,textvariable=mobval)
    a3.place(x=230,y=130)

    a4=Entry(addroot,font=('roamn',15,'bold'),bd=5,textvariable=emailval)
    a4.place(x=230,y=190)

    a5=Entry(addroot,font=('roamn',15,'bold'),bd=5,textvariable=addval)
    a5.place(x=230,y=250)

    a6=Entry(addroot,font=('roamn',15,'bold'),bd=5,textvariable=genderval)
    a6.place(x=230,y=310)

    a7=Entry(addroot,font=('roamn',15,'bold'),bd=5,textvariable=DOBval)
    a7.place(x=230,y=370)

    submit2 = Button(addroot,text='SubmiT',font=('roman',15,'bold'),
            width=20,activebackground='black',activeforeground='grey',bd=5
                     ,command=submitadd)
    submit2.place(x=150,y=417)
    
    addroot.mainloop()
def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobval.get()
        email = emailval.get()
        address = addval.get()
        gender = genderval.get()
        dob = DOBval.get()
        addeddate= time.strftime('%d/%m/%Y')
        if id != '':
            strr= 'select * from studentdata1 where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vr = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studentTable.insert('',END,values=vr)
        elif name != '':
            strr= 'select * from studentdata1 where name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vr = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studentTable.insert('',END,values=vr)
        elif mobile != '':
            strr= 'select * from studentdata1 where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vr = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studentTable.insert('',END,values=vr)
        elif email != '':
            strr= 'select * from studentdata1 where email=%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vr = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studentTable.insert('',END,values=vr)
        elif address != '':
            strr= 'select * from studentdata1 where address=%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vr = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studentTable.insert('',END,values=vr)
        elif gender != '':
            strr= 'select * from studentdata1 where gender=%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vr = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studentTable.insert('',END,values=vr)
        elif dob != '':
            strr= 'select * from studentdata1 where dob=%s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vr = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studentTable.insert('',END,values=vr)
        elif addeddate != '':
            strr= 'select * from studentdata1 where addeddate=%s'
            mycursor.execute(strr,(addeddate))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vr = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studentTable.insert('',END,values=vr)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+140+100')
    searchroot.title("Stud Manage Sys")
    searchroot.config(bg='gold')
    searchroot.iconbitmap('1.ico')
    searchroot.resizable(False,False)
    
    #menu in add student option
    idlabel1= Label(searchroot,text="enter id:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel1.place(x=10,y=10)
    namelabel1= Label(searchroot,text="enter name:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel1.place(x=10,y=70)
    moblabel1= Label(searchroot,text="enter mobile:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    moblabel1.place(x=10,y=130)
    emaillabel1= Label(searchroot,text="enter email:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel1.place(x=10,y=190)
    addlabel1= Label(searchroot,text="enter address:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addlabel1.place(x=10,y=250)
    genderlabel1= Label(searchroot,text="enter gender:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel1.place(x=10,y=310)
    DOBlabel1= Label(searchroot,text="enter DOB:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    DOBlabel1.place(x=10,y=370)
    datelabel1= Label(searchroot,text="enter date:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel1.place(x=10,y=430)

    idval= StringVar()
    nameval= StringVar()
    mobval= StringVar()
    emailval= StringVar()
    addval= StringVar()
    genderval= StringVar()
    DOBval= StringVar()
    dateval= StringVar()
    
    a1=Entry(searchroot,font=('roamn',15,'bold'),bd=5,textvariable=idval)
    a1.place(x=230,y=10)

    a2=Entry(searchroot,font=('roamn',15,'bold'),bd=5,textvariable=nameval)
    a2.place(x=230,y=70)

    a3=Entry(searchroot,font=('roamn',15,'bold'),bd=5,textvariable=mobval)
    a3.place(x=230,y=130)

    a4=Entry(searchroot,font=('roamn',15,'bold'),bd=5,textvariable=emailval)
    a4.place(x=230,y=190)

    a5=Entry(searchroot,font=('roamn',15,'bold'),bd=5,textvariable=addval)
    a5.place(x=230,y=250)

    a6=Entry(searchroot,font=('roamn',15,'bold'),bd=5,textvariable=genderval)
    a6.place(x=230,y=310)

    a7=Entry(searchroot,font=('roamn',15,'bold'),bd=5,textvariable=DOBval)
    a7.place(x=230,y=370)

    a8=Entry(searchroot,font=('roamn',15,'bold'),bd=5,textvariable=dateval)
    a8.place(x=230,y=430)

    submit3 = Button(searchroot,text='search',font=('roman',15,'bold'),
            width=20,activebackground='black',activeforeground='grey',bd=5
                     ,command=search)
    submit3.place(x=150,y=485)
    
    searchroot.mainloop()
    
def deletestudent():
    d = studentTable.focus()
    content = studentTable.item(d)
    main = content['values'][0]
    strr= 'delete from studentdata1 where id=%s'
    mycursor.execute(strr,(main))
    con.commit()
    messagebox.showinfo('Notifications','ID {} deleted successfully'.format(main))
    strr= 'select * from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for i in datas:
        vr = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studentTable.insert('',END,values=vr)
        
def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobval.get()
        email = emailval.get()
        address = addval.get()
        gender = genderval.get()
        dob = DOBval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications','Id {} data updated successfully'.format(id),parent=updateroot)
        strr= 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for i in datas:
            vr = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studentTable.insert('',END,values=vr)
                         
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x580+140+80')
    updateroot.title("Stud Manage Sys")
    updateroot.config(bg='pink')
    updateroot.iconbitmap('1.ico')
    updateroot.resizable(False,False)
    
    #menu in add student option
    idlabel1= Label(updateroot,text="enter id:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel1.place(x=10,y=10)
    namelabel1= Label(updateroot,text="enter name:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel1.place(x=10,y=70)
    moblabel1= Label(updateroot,text="enter mobile:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    moblabel1.place(x=10,y=130)
    emaillabel1= Label(updateroot,text="enter email:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel1.place(x=10,y=190)
    addlabel1= Label(updateroot,text="enter address:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addlabel1.place(x=10,y=250)
    genderlabel1= Label(updateroot,text="enter gender:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel1.place(x=10,y=310)
    DOBlabel1= Label(updateroot,text="enter DOB:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    DOBlabel1.place(x=10,y=370)
    datelabel1= Label(updateroot,text="enter date:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel1.place(x=10,y=430)
    timelabel1= Label(updateroot,text="enter time:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timelabel1.place(x=10,y=490)

    idval= StringVar()
    nameval= StringVar()
    mobval= StringVar()
    emailval= StringVar()
    addval= StringVar()
    genderval= StringVar()
    DOBval= StringVar()
    dateval= StringVar()
    timeval= StringVar()
    
    a1=Entry(updateroot,font=('roamn',15,'bold'),bd=5,textvariable=idval)
    a1.place(x=230,y=10)

    a2=Entry(updateroot,font=('roamn',15,'bold'),bd=5,textvariable=nameval)
    a2.place(x=230,y=70)

    a3=Entry(updateroot,font=('roamn',15,'bold'),bd=5,textvariable=mobval)
    a3.place(x=230,y=130)

    a4=Entry(updateroot,font=('roamn',15,'bold'),bd=5,textvariable=emailval)
    a4.place(x=230,y=190)

    a5=Entry(updateroot,font=('roamn',15,'bold'),bd=5,textvariable=addval)
    a5.place(x=230,y=250)

    a6=Entry(updateroot,font=('roamn',15,'bold'),bd=5,textvariable=genderval)
    a6.place(x=230,y=310)

    a7=Entry(updateroot,font=('roamn',15,'bold'),bd=5,textvariable=DOBval)
    a7.place(x=230,y=370)

    a8=Entry(updateroot,font=('roamn',15,'bold'),bd=5,textvariable=dateval)
    a8.place(x=230,y=430)
    
    a9=Entry(updateroot,font=('roamn',15,'bold'),bd=5,textvariable=timeval)
    a9.place(x=230,y=490)

    submit4 = Button(updateroot,text='update',font=('roman',15,'bold'),
            width=20,activebackground='black',activeforeground='grey',bd=5
                     ,command=update)
    submit4.place(x=150,y=530)

    u= studentTable.focus()
    content = studentTable.item(u)
    main = content['values']
    print(main)
    if len(main) != 0:
        idval.set(main[0])
        nameval.set(main[1])
        mobval.set(main[2])
        emailval.set(main[3])
        addval.set(main[4])
        genderval.set(main[5])
        DOBval.set(main[6])
        dateval.set(main[7])
        timeval.set(main[8])
    
    updateroot.mainloop()
def showstudent():
        strr= 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for i in datas:
            vr = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studentTable.insert('',END,values=vr)
def exportstudent():
    f=filedialog.asksaveasfilename()
    c = studentTable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in c:
        o = studentTable.item(i)
        pp= o['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),
        address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),
        addedtime.append(pp[8])
            
    head=['id','name','mobile','email','address','gender','dob','added date','added time']
    df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=head)
    paths = r'{}.csv'.format(f)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications','Student Data is saved at {} successfully'.format(paths))
    
def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do You Want To Exit')
    if res == True:
        root.destroy()
    



#Connecting DB
def connectDB():
    def submitDB():
##        host= hostval.get()
##        user= userval.get()
##        psw = pswval.get()
        global con,mycursor
        host = 'localhost'
        user = 'root'
        psw = 'timeline1'
        try:
            con = pymysql.connect(host=host, user=user, password=psw)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications','Data is incorrect')
            return
        try:
            strr = 'create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int, name varchar(20), mobile varchar(30),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr= 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Database created & now you are connected to the DB',parent=dbroot)

        except:
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the DB',parent=dbroot)
        dbroot.destroy()
            
        
    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+120')
    dbroot.iconbitmap('1.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='green')
    #PLACEHOLDER FOR DB
    hostLabel=Label(dbroot,text="enter host:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hostLabel.place(x=10,y=10)
    userLabel=Label(dbroot,text="enter user:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    userLabel.place(x=10,y=70)
    pswLabel=Label(dbroot,text="enter psw:",bg='orange',font=('times',20,'bold'),
              relief=GROOVE,borderwidth=3,width=12,anchor='w')
    pswLabel.place(x=10,y=130)
    
    #PLACEHOLDER ENTRIES FOR DB
    hostval = StringVar()
    userval = StringVar()
    pswval = StringVar()
    #pswval.set("HELLO")
    hostentery=Entry(dbroot,font=('roamn',15,'bold'),bd=5,textvariable=hostval)
    hostentery.place(x=230,y=10)
    userentery=Entry(dbroot,font=('roamn',15,'bold'),bd=5,textvariable=userval)
    userentery.place(x=230,y=70)
    pswentery=Entry(dbroot,font=('roamn',15,'bold'),bd=5,textvariable=pswval)
    pswentery.place(x=230,y=130)

    #submit btn
    submit = Button(dbroot,text='SubmiT',font=('roman',15,'bold'),
            width=20,activebackground='black',
                    activeforeground='white',bd=5,command=submitDB)
    submit.place(x=150,y=190)
    dbroot.mainloop()
#main header
import random
colors=['green','blue','red','purple','brown','black']
def tick():
    global count,c 
    if(count>=len(t)):
        count= 0
        c=''
        header.config(text=c)
    else:
        c = c + t[count]
        header.config(text=c)
        count +=1
    header.after(200,tick)
def colTick():
    fg = random.choice(colors)
    header.config(fg=fg)
    header.after(2,colTick)
    
#time header    
def tick2():
    timeStr = time.strftime('%H:%M:%S')
    dateStr = time.strftime('%d/%m/%Y')
    clk.config(text='Date :' +dateStr+'\n'+ 'Time:'+timeStr)
    clk.after(200,tick2)
  
from tkinter import *
import time
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import pandas 


root = Tk()
root.title("Student Management System")
root.config(bg="blue")
root.geometry('1174x700+90+1')
root.iconbitmap('1.ico')
root.resizable(False,False)

## MAKING FRAMES ##
#FRAME IS A CONTAINER IN OUR MAIN SCREEN
#WE LL MAKE TWO FRAMES ONE FOR DISPLAYING DATA AND THE
#OTHER FOR PERFORMING OP OON THE DB
DataEntryFrame= Frame(root,bg='blue2',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)

p="********* W E L C O M E *********"
framehead= Label(DataEntryFrame,text=p,
                font=('arial',20,'bold'),bg='blue2')
framehead.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame,text='Add Student',font=('chiller',20,'bold'),
            width=25,activebackground='black',activeforeground='white',bd=6,command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='Search Student',font=('chiller',20,'bold'),
            width=25,activebackground='black',activeforeground='white',bd=6,command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='Delete Student',font=('chiller',20,'bold'),
            width=25,activebackground='black',activeforeground='white',bd=6,command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='Update Student',font=('chiller',20,'bold'),
            width=25,activebackground='black',activeforeground='white',bd=6,command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showbtn = Button(DataEntryFrame,text='Show All Students',font=('chiller',20,'bold'),
            width=25,activebackground='black',activeforeground='white',bd=6,command=showstudent)
showbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='Export Data',font=('chiller',20,'bold'),
            width=25,activebackground='black',activeforeground='white',bd=6,command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='Exit',font=('chiller',20,'bold'),
            width=25,activebackground='black',activeforeground='white',bd=6,command=exitstudent)
exitbtn.pack(side=TOP,expand=True)

#this frame is for showing data

ShowDataFrame= Frame(root,bg='blue2',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)

style1=ttk.Style()
style1.configure('Treeview.Heading',font=('times',18,'bold'),foreground='purple')
style1.configure('Treeview',font=('Arial',15,'bold'),foreground='black',background='cyan')
sx=Scrollbar(ShowDataFrame,orient=HORIZONTAL)
sy=Scrollbar(ShowDataFrame,orient=VERTICAL)





studentTable = Treeview(ShowDataFrame,columns=('Id','name','mobile No','Email',
                                              'Address','Gender','D.O.b','Added Date',
                                              'Added Time'),yscrollcommand=sy.set,xscrollcommand=sx.set)
sx.pack(side=BOTTOM,fill=X)
sy.pack(side=RIGHT,fill=Y)
sx.config(command=studentTable.xview)
sy.config(command=studentTable.yview)
studentTable.heading('Id',text='Id')
studentTable.heading('name',text='name')
studentTable.heading('mobile No',text='mobile No')
studentTable.heading('Email',text='Email')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.b',text='D.O.b')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')
studentTable.pack(fill=BOTH,expand=1)
studentTable['show']= 'headings'
studentTable.column('Id',width=100)
studentTable.column('name',width=200)
studentTable.column('mobile No',width=200)
studentTable.column('Email',width=300)
studentTable.column('Address',width=200)
studentTable.column('Gender',width=100)
studentTable.column('D.O.b',width=150)
studentTable.column('Added Date',width=150)
studentTable.column('Added Time',width=150)


#making header
t='Welcome to Student Management System'
count=0
c = ''
header = Label(root,fg='brown',text=t,relief=RIDGE,borderwidth=5,font=('chiller',30,'bold'),bg='green')
header.place(x=260,y=0,width=600)
tick()
colTick()


#time
clk =Label(root,relief=RIDGE,borderwidth=5,font=('time',16,'bold'),bg='cyan' )
clk.place(x=0,y=0)
tick2()

#db button
connect1=Button(root,text="COnnect TO Database",borderwidth=5,width=20,relief=RIDGE,font=('chiller',20,'bold'),bg='cyan'
                 ,activebackground='black',activeforeground='white',command=connectDB)
connect1.place(x=939,y=0 )


root.mainloop()


