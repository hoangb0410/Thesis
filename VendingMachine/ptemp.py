from tkinter import * #If you get an error here, try Tkinter not tkinter

# def SuccessfulDisplay():
#     Dialog1 = Toplevel(height=500, width=500) #Here
#     Label(Dialog1,text='Successful!', font=('Arial',50),fg='green3').pack(padx=30,pady=30)

# def FailedDisplay():
#     Dialog2 = Toplevel(height=1000, width=1000) #Here
#     Label(Dialog2,text='Not enough money!', font=('Arial',50),fg='red').pack(padx=30,pady=30)

# def RefundChangeDisplay():
#     Dialog3 = Toplevel(height=1000, width=1000) #Here
#     Label(Dialog3,text='Not enough money!', font=('Arial',50),fg='red').pack(padx=30,pady=30)

code = '001'
money = '15000'
if code=='001' or code=='002' or code =='003' or code =='004' :
    p_money='10000'
else:
    p_money='5000'

notice=Tk()
notice.title("Notice")
LabelText=StringVar()
LabelText.set("Product Code")
labelDir=Label(notice, textvariable=LabelText, font=("Arial",22),bg='seashell2')
labelDir.pack(side="left")
entry_text1 = StringVar()
textbox1 = Entry(notice,width=15,bg='aquamarine1',font=('Arial 22'),justify=CENTER,textvariable=entry_text1)
textbox1.pack(side="left")


notice.configure(background='mintcream')
if int(money)<int(p_money):
    Label(notice,text='Not enough money!', font=('Arial',50),fg='red',bg='mintcream').pack(padx=30,pady=30)
elif money==p_money:
    Label(notice,text='Successful!', font=('Arial',50),fg='green3',bg='mintcream').pack(padx=30,pady=30)
else:
    du=int(money)-int(p_money)
    Label(notice,text='Tiền thừa: '+str(du)+'Đ', font=('Arial',50),fg='#FF6103',bg='mintcream').pack(padx=30,pady=30)

notice.mainloop()