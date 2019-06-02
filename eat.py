from tkinter import *
from datetime import datetime
from csv import DictReader

def total():
    f = open('menu.csv', 'r')
    r = DictReader(f)
    l=[]
    
    for row in r:
        l1 = []
        l1.append(row['name'])
        l1.append(row['price'])
        l.append(l1)

    for i in l:
        if i[0] == 'mosrilla':
            global mos_price
            mos_price = int(i[1])

        if i[0] == 'aloo tikki burger':
            global aloo_price
            aloo_price = int(i[1])

        if i[0] == 'non-veg burger':
            global non_price
            non_price = int(i[1])

        if i[0] == 'smokey burger':
            global smokey_price
            smokey_price = int(i[1])

        if i[0] == 'chicken popcorn':
            global chicken_price
            chicken_price =int(i[1])

        if i[0] == 'eat up special':
            global eat_price
            eat_price = int(i[1])

    aloo_q = aloo_var.get()
    
    bur_q = bur_var.get()
    pop_q = pop_var.get()
    smoke_q = smoke_var.get()
    eat_q = eat_var.get()
    mos_q = mos_var.get()
    

    cash = (aloo_q * aloo_price) + (bur_q * non_price) + (mos_q * mos_price) + (eat_q * eat_price) + (pop_q * chicken_price) + (smoke_q * smokey_price)
    to_l.configure(text='Your Total Is :\nRs.'+str(cash))

    aloo_var.set('0')
    bur_var.set('0')
    pop_var.set('0')
    smoke_var.set('0')
    eat_var.set('0')
    mos_var.set('0')
    
    

#------------------------------


    


#------------------------------

root = Tk()
root.title('EAT UP')
root.geometry('435x590')
root.resizable(0,0)

label_1 = Label(root, text='EAT UP', font=('Arial', 20,'bold'), bg='light green', width=50)
label_1.pack(side=TOP)

f_la = LabelFrame(root, text='Menu',width=50)
f_la.place(x=5,y=40)

# dishes---------------------------------------------------------------------------------------------------
#aloo------------------------------

aloo = Label(f_la, text='Aloo Tikki Burger', font=('Arial', 13,'bold') )
aloo.pack()

aloo_var = IntVar()

aloo_e = Entry(f_la, width=10, justify='right',bd=5,bg='light green', font=('Arial Black', 10,'bold'),textvariable=aloo_var)
aloo_e.pack()


Label(f_la, text='').pack()
#bur--------------------------------

bur = Label(f_la, text='Non-Veg Burger', font=('Arial', 13,'bold') )
bur.pack()

bur_var = IntVar()

aloo_e = Entry(f_la, width=10, justify='right',bd=5,bg='light green', font=('Arial Black', 10,'bold'),textvariable=bur_var)
aloo_e.pack()


Label(f_la, text='').pack()
#pop----------------------------------

pop = Label(f_la, text='Chicken Popcorn', font=('Arial', 13,'bold') )
pop.pack()

pop_var = IntVar()

pop_e = Entry(f_la, width=10, justify='right',bd=5,bg='light green', font=('Arial Black', 10,'bold'),textvariable=pop_var)
pop_e.pack()



Label(f_la, text='').pack()
#smoke-----------------------------------

smoke = Label(f_la, text='Smokey Burger', font=('Arial', 13,'bold') )
smoke.pack()

smoke_var = IntVar()

smoke_e = Entry(f_la, width=10, justify='right',bd=5,bg='light green', font=('Arial Black', 10,'bold'),textvariable=smoke_var)
smoke_e.pack()



Label(f_la, text='').pack()
#eat-----------------------------------

eat = Label(f_la, text='Eat Up Special Burger', font=('Arial', 13,'bold') )
eat.pack()

eat_var = IntVar()

eat_e = Entry(f_la, width=10, justify='right',bd=5,bg='light green', font=('Arial Black', 10,'bold'),textvariable=eat_var)
eat_e.pack()



Label(f_la, text='').pack()
#mos-------------------------------------

mos = Label(f_la, text='Mosrilla', font=('Arial', 13,'bold') )
mos.pack()

mos_var = IntVar()

mos_e = Entry(f_la, width=10, justify='right',bd=5,bg='light green', font=('Arial Black', 10,'bold'),textvariable=mos_var)
mos_e.pack()



Label(f_la, text='').pack()

#-------------------------------------------


total = Button(f_la, text='Total', bd=5,bg='light green',font=('Arial', 15,'bold'), command=total)
total.pack()

Label(f_la, text='').pack()

#---------------------------------------------------------

to_l = Label(root, text='', font=('Arial Black', 20,'bold'))
to_l.place(x=200,y=350)

#-------------------------------------------------------------

time_l = LabelFrame(root, text='Date')
time_l.place(x=200,y=500)

pt = datetime.now()
pt=pt.strftime('%d-%m-%Y')


Label(time_l,text= pt,font=('Arial', 30,'bold')).pack()

win = LabelFrame(root, text='Calculator')
win.place(x=200,y=50)

num = StringVar()

operator = ''

entry = Entry(win, width=13,bd=10,bg='light green',font=('arial',20), textvariable = num, justify='right')
entry.grid(row=0,columnspan=4,pady=7)

#--------------func for buttn--------------

def button(number):
    global operator
    operator += str(number)
    num.set(operator)

def equal():
    global operator
    
    sum_up = int(eval(operator))
    num.set(sum_up)
    operator = ''
        
def clear():
    num.set('')
    global operator
    operator = ''
    

        
#------------------row 1------------------
b7 = Button(win, width=5,height=2,text='7',bd=5,command = lambda: button(7),bg='light green',font=('arial',10))
b7.grid(row=1,column=0)

b8 = Button(win, width=5,height=2,text='8',bd=5,command = lambda: button(8),bg='light green',font=('arial',10))
b8.grid(row=1,column=1)

b9 = Button(win, width=5,height=2,text='9',bd=5,command = lambda: button(9), bg='light green',font=('arial',10))
b9.grid(row=1,column=2)

bplus = Button(win, width=5,height=2,text='+',bd=5,command = lambda: button('+'),bg='light green',font=('arial',10))
bplus.grid(row=1,column=3)

#-------------------row 2-------------------

b4 = Button(win, width=5,height=2,text='4',bd=5,command = lambda: button(4),bg='light green',font=('arial',10))
b4.grid(row=2,column=0)

b5 = Button(win, width=5,height=2,text='5',bd=5,command = lambda: button(5),bg='light green',font=('arial',10))
b5.grid(row=2,column=1)

b6 = Button(win, width=5,height=2,text='6',bd=5,command = lambda: button(6),bg='light green',font=('arial',10))
b6.grid(row=2,column=2)

bmin = Button(win, width=5,height=2,text='-',bd=5,command = lambda: button('-'),bg='light green',font=('arial',10))
bmin.grid(row=2,column=3)


#-------------------row 3-------------------

b1 = Button(win, width=5,height=2,text='1',bd=5,command = lambda: button(1),bg='light green',font=('arial',10))
b1.grid(row=3,column=0)

b2 = Button(win, width=5,height=2,text='2',bd=5,command = lambda: button(2),bg='light green',font=('arial',10))
b2.grid(row=3,column=1)

b3 = Button(win, width=5,height=2,text='3',bd=5,command = lambda: button(3),bg='light green',font=('arial',10))
b3.grid(row=3,column=2)

bmul = Button(win, width=5,height=2,text='*',bd=5,command = lambda: button('*'),bg='light green',font=('arial',10))
bmul.grid(row=3,column=3)


#-------------------row 4-------------------

b0 = Button(win, width=5,height=2,text='0',bd=5,command = lambda: button(0),bg='light green',font=('arial',10))
b0.grid(row=4,column=0)

bclear = Button(win, width=5,height=2,text='C',bd=5, command = clear,bg='light green',font=('arial',10))
bclear.grid(row=4,column=1)

beq = Button(win, width=5,height=2,text='=',bd=5, command = equal,bg='light green',font=('arial',10))
beq.grid(row=4,column=2)

bdiv = Button(win, width=5,height=2,text='/',bd=5,command = lambda: button('/'),bg='light green',font=('arial',10))
bdiv.grid(row=4,column=3)




            


root.mainloop()
