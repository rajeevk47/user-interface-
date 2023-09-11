from tkinter import*
import random
import tkinter.messagebox as tmsg
root=Tk()
root.title('REGISTRATION')
Label(root,text='REGISTRATION! ' ,bg='grey').grid()
Label(root,text='Generate pin to log in',bg='grey').grid(column=1,row=0)
root.config(background='grey')
root.geometry ('400x200')
Label(root,text='Username',font=('comicsansms',10,'bold'),fg='#fc033d',bg='grey').grid(row=1,column=0)
Label(root,text='password',font=('comicsansms',10,'bold'),fg='#fc033d',bg='grey').grid(row=2,column=0)
usere=StringVar()
userentry1=Entry(root,textvariable=usere,border=4,fg='white',bg='#297487')
userentry1.grid(row=1,column=1)
alo='`~!@#$%^&*(){|:"?>}<,./]23456789'
def register(): 
    global userentry1
    with open('record.txt','a') as f:
      f.write(f'{userentry1.get()}\n')
    with open('record.txt','a') as f:
      f.write(f'{b9}\n')

    # root.destroy()
    root2=Tk()
    root2.geometry('400x200')
    root2.config(bg='grey')
    Label(root2,text='LOGIN!',font=('comicsansms',20,'bold'),fg='#fc033d',bg='grey').grid(row=0,column=0)
    Label(root2,text='Username',font=('comicsansms',10,'bold'),fg='#fc033d',bg='grey').grid(row=1,column=0)
    Label(root2,text='password',font=('comicsansms',10,'bold'),fg='#fc033d',bg='grey').grid(row=2,column=0)
    def login():
       jk=userentry2.get()
       global db
       db=userentry1.get()
       df=passentry.get()
       if jk==db and df==b9 :
         root.destroy()
         root2.destroy()
         r=Tk()
         r.config(bg='#4da6ff')
         r.title('Calculator')
         r.geometry('400x500')
         screen = StringVar()
         screenv = Entry(textvariable=screen,font=("Arial",25))
         screenv.pack(fill=X,padx=12,pady=12)
         a= Frame(bg='#4da6ff')
         a.pack(pady=12)
         a= Frame(bg='#4da6ff')
         def click(event):
            global screen
            text= event.widget.cget('text')
            
            if text=='=':
               if screen.get().isdigit():
                     value=int(screen.get())
                     
               else:
                     value=eval(screen.get().lstrip('0'))
                     
            elif text=='c':
               screen.set('')
               screenv.update()
            else:
               screen.set(screen.get()+ text)
               screenv.update()
         b1=Button(a,text='1',padx=23,pady=20)
         b2=Button(a,text='2',padx=23,pady=20)
         b3=Button(a,text='3',padx=23,pady=20)
         b4=Button(a,text='+',padx=23,pady=20)
         b1.bind('<Button-1>',click)
         b2.bind('<Button-1>',click)
         b3.bind('<Button-1>',click)
         b4.bind('<Button-1>',click)
         b1.pack(side=LEFT,padx=8,pady=4)
         b2.pack(side=LEFT,padx=8,pady=4)
         b3.pack(side=LEFT,padx=8,pady=4)
         b4.pack(side=LEFT,padx=8,pady=4)
         a.pack()
         a= Frame(bg='#4da6ff')
         b1=Button(a,text='4',padx=23,pady=20)
         b2=Button(a,text='5',padx=23,pady=20)
         b3=Button(a,text='6',padx=23,pady=20)
         b4=Button(a,text='-',padx=23,pady=20)
         b1.bind('<Button-1>',click)
         b2.bind('<Button-1>',click)
         b3.bind('<Button-1>',click)
         b4.bind('<Button-1>',click)
         b1.pack(side=LEFT,padx=8,pady=4)
         b2.pack(side=LEFT,padx=8,pady=4)
         b3.pack(side=LEFT,padx=8,pady=4)
         b4.pack(side=LEFT,padx=8,pady=4)
         a.pack()
         a= Frame(bg='#4da6ff')
         b1=Button(a,text='7',padx=23,pady=20)
         b2=Button(a,text='8',padx=23,pady=20)
         b3=Button(a,text='9',padx=23,pady=20)
         b4=Button(a,text='*',padx=23,pady=20)
         b1.bind('<Button-1>',click)
         b2.bind('<Button-1>',click)
         b3.bind('<Button-1>',click)
         b4.bind('<Button-1>',click)
         b1.pack(side=LEFT,padx=8,pady=4)
         b2.pack(side=LEFT,padx=8,pady=4)
         b3.pack(side=LEFT,padx=8,pady=4)
         b4.pack(side=LEFT,padx=8,pady=4)
         a.pack()

         a= Frame(bg='#4da6ff')
         b1=Button(a,text='c',padx=23,pady=20)
         b2=Button(a,text='%',padx=23,pady=20)
         b3=Button(a,text='=',padx=23,pady=20)
         b4=Button(a,text='/',padx=23,pady=20)
         b1.bind('<Button-1>',click)
         b2.bind('<Button-1>',click)
         b3.bind('<Button-1>',click)
         b4.bind('<Button-1>',click)
         b1.pack(side=LEFT,padx=8,pady=4)
         b2.pack(side=LEFT,padx=8,pady=4)
         b3.pack(side=LEFT,padx=8,pady=4)
         b4.pack(side=LEFT,padx=8,pady=4)
         a.pack()










         r.mainloop()





       else:
          tmsg.showinfo('error','wrong password!!!')   
        
    usere=StringVar()
    userentry2=Entry(root2,textvariable=usere,border=4,fg='white',bg='#297487')
    userentry2.grid(row=1,column=1)
    passe=StringVar()
    passentry=Entry(root2,textvariable=passe,border=4,fg='white',bg='#297487')
    passentry.grid(row=2,column=1)
    Button(root2,text='Log in',command=login).grid(row=3,column=1)
    root2.mainloop()
def generate():
    mb= userentry1.get()
    if mb=='':
       tmsg.showinfo('error','please enter a valid username first')
   #  elif mb==db:
   #     tmsg.showinfo("ERROR","Username already taken")
    else:
        tmsg.showinfo('info', 'we are generating your password due to security reasons')
        global b9
        b1=random.choice(alo)
        b2=random.choice(alo)
        b3=random.choice(alo)
        b4=random.choice(alo)
        b5=random.choice(alo)
        b6=random.choice(alo)
        b7=random.choice(alo)
        b8=random.choice(alo)
        b9= b1+b2+b3+b4+b5+b6+b7+b8
        Label(root,text=f'your password is {b9} ').grid(row=2,column=1)
        Button(root,text='Register',command=register).grid(row=3,column=1)

Button(root,text='Generate',command=generate).grid(row=2,column=2)
root.mainloop()
