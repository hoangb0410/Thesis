from tkinter import messagebox

code = 7
money = 2
if code==1 or code==2 or code ==3 or code ==4 :
    p_money=10000
else:
    p_money=5000

messagebox.showinfo('Notice', 'Tien thua '+str(p_money))
print(p_money)
p_money='123'
a=int(p_money)
print(a)