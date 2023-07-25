from tkinter import*

tii= Tk()
tii.geometry('455x455')
def hello():
    print(f'{k.get(),r.get(),q.get()}')
    
    
    with open('record.txt','a') as f:
        f.write(f'{k.get(),r.get(),q.get()}\n')
        
user=Label(text='username')
password=Label(text='password')
user.grid()
password.grid(row=1)

k=StringVar()
r=StringVar()

kentry=Entry(textvariable=k)
rentry=Entry(textvariable=r)
kentry.grid(row=0,column=1)
rentry.grid(row=1,column=1)
b1=Button(text='submit',command=hello)
b1.grid(row=4,column=1)

q=IntVar()
fe=Checkbutton(text= 'sign up',variable=q)
fe.grid(row=3 ,column=1)

tii.mainloop()
