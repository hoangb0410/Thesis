from tkinter import *
import PIL as p
import PIL.ImageTk as ptk
import os

# Create the GUI window
root=Tk()
root.title("Vending Machine UI")
root.geometry("1200x680")
# Heading
Heading=LabelFrame(root,bd=2,relief="groove",bg="light yellow")
Heading.place(x=0,y=0,width=1200,height=55)
image_logo=p.Image.open("E:\VSCODE\Thesis\VendingMachine\Images\Logo.png")
image_logo_1=ptk.PhotoImage(image_logo)
label_logo=Label(Heading,image=image_logo_1)
label_logo.grid(row=0,column=0)
name=Label(Heading,text="Vending Machine",font="arial 20 bold",bg="light pink",fg="blue").grid(row=0,column=1)

# Button Frame
Button_frame=LabelFrame(root,bd=2,relief="groove",text="Operation",font="arial 16 bold",fg="dark blue",bg='seashell1')
Button_frame.place(x=2,y=60,width=350,height=620)

# Product Frame
Products_frame=LabelFrame(root,bd=2,relief="groove",text="Products",font="arial 16 bold",fg="dark blue",bg='seashell1')
Products_frame.place(x=355,y=60,width=843,height=620)

# product
product1_image=ptk.PhotoImage(p.Image.open("E:\VSCODE\Thesis\VendingMachine\Images\coca_cola.jpg"))
product2_image=ptk.PhotoImage(p.Image.open("E:\VSCODE\Thesis\VendingMachine\Images\pepsi.jpg"))
product3_image=ptk.PhotoImage(p.Image.open("E:\VSCODE\Thesis\VendingMachine\Images\lfanta.png"))
product4_image=ptk.PhotoImage(p.Image.open("E:\VSCODE\Thesis\VendingMachine\Images\mirinda_orange.png"))
product5_image=ptk.PhotoImage(p.Image.open("E:\VSCODE\Thesis\VendingMachine\Images\Snack_1.png"))
product6_image=ptk.PhotoImage(p.Image.open("E:\VSCODE\Thesis\VendingMachine\Images\Snack_2.jpg"))
product7_image=ptk.PhotoImage(p.Image.open("E:\VSCODE\Thesis\VendingMachine\Images\Snack_3.jpg"))
product8_image=ptk.PhotoImage(p.Image.open("E:\VSCODE\Thesis\VendingMachine\Images\Snack_4.jpg"))

# Function Hide all Frame
def HideAllFrames():
    for widget in Products_frame.winfo_children():
        widget.destroy()

# product //cach nhau 210
# row 1
lf_product1=LabelFrame(Products_frame,bd=2,relief="groove",bg='rosybrown1')
lf_product1.place(x=5,y=10,width=200,height=286)
lf_product2=LabelFrame(Products_frame,bd=2,relief="groove",bg='rosybrown1')
lf_product2.place(x=215,y=10,width=200,height=286)
lf_product3=LabelFrame(Products_frame,bd=2,relief="groove",bg='rosybrown1')
lf_product3.place(x=425,y=10,width=200,height=286)
lf_product4=LabelFrame(Products_frame,bd=2,relief="groove",bg='rosybrown1')
lf_product4.place(x=635,y=10,width=200,height=286)
# row 2
lf_product5=LabelFrame(Products_frame,bd=2,relief="groove",bg='rosybrown1')
lf_product5.place(x=5,y=300,width=200,height=286)
lf_product6=LabelFrame(Products_frame,bd=2,relief="groove",bg='rosybrown1')
lf_product6.place(x=215,y=300,width=200,height=286)
lf_product7=LabelFrame(Products_frame,bd=2,relief="groove",bg='rosybrown1')
lf_product7.place(x=425,y=300,width=200,height=286)
lf_product8=LabelFrame(Products_frame,bd=2,relief="groove",bg='rosybrown1')
lf_product8.place(x=635,y=300,width=200,height=286)

# Product code
code_product1=Label(lf_product1,text="001",font="arial 15",bg='aqua',fg='red',justify="center",padx=79).grid(row=0,column=0)
code_product2=Label(lf_product2,text="002",font="arial 15",bg='aqua',fg='red',justify="center",padx=79).grid(row=0,column=0)
code_product3=Label(lf_product3,text="003",font="arial 15",bg='aqua',fg='red',justify="center",padx=79).grid(row=0,column=0)
code_product4=Label(lf_product4,text="004",font="arial 15",bg='aqua',fg='red',justify="center",padx=79).grid(row=0,column=0)
code_product5=Label(lf_product5,text="005",font="arial 15",bg='aqua',fg='red',justify="center",padx=79).grid(row=0,column=0)
code_product6=Label(lf_product6,text="006",font="arial 15",bg='aqua',fg='red',justify="center",padx=79).grid(row=0,column=0)
code_product7=Label(lf_product7,text="007",font="arial 15",bg='aqua',fg='red',justify="center",padx=79).grid(row=0,column=0)
code_product8=Label(lf_product8,text="008",font="arial 15",bg='aqua',fg='red',justify="center",padx=79).grid(row=0,column=0)

# Product image
label_product_1=Label(lf_product1,image=product1_image,bd=2).grid(row=1,column=0)
label_product_2=Label(lf_product2,image=product2_image,bd=2).grid(row=1,column=0)
label_product_3=Label(lf_product3,image=product3_image,bd=2).grid(row=1,column=0)
label_product_4=Label(lf_product4,image=product4_image,bd=2).grid(row=1,column=0)
label_product_5=Label(lf_product5,image=product5_image,bd=2).grid(row=1,column=0)
label_product_6=Label(lf_product6,image=product6_image,bd=2).grid(row=1,column=0)
label_product_7=Label(lf_product7,image=product7_image,bd=2).grid(row=1,column=0)
label_product_8=Label(lf_product8,image=product8_image,bd=2).grid(row=1,column=0)

# Product price
price1 = 8000
price2 = 10000
price3 = 15000
price4 = 20000
price5 = 5000
price6 = 7000
price7 = 10000
price8 = 15000
price_product1=Label(lf_product1,text=' '+str(price1)+'Đ ',font="arial 15",bg='yellow',padx=60).grid(row=3,column=0)
price_product2=Label(lf_product2,text=str(price2)+'Đ',font="arial 15",bg='yellow',padx=60).grid(row=3,column=0)
price_product3=Label(lf_product3,text=str(price3)+'Đ',font="arial 15",bg='yellow',padx=60).grid(row=3,column=0)
price_product4=Label(lf_product4,text=str(price4)+'Đ',font="arial 15",bg='yellow',padx=60).grid(row=3,column=0)
price_product5=Label(lf_product5,text=str(price5)+'Đ',font="arial 15",bg='yellow',padx=66).grid(row=3,column=0)
price_product6=Label(lf_product6,text=str(price6)+'Đ',font="arial 15",bg='yellow',padx=66).grid(row=3,column=0)
price_product7=Label(lf_product7,text=str(price7)+'Đ',font="arial 15",bg='yellow',padx=60).grid(row=3,column=0)
price_product8=Label(lf_product8,text=str(price8)+'Đ',font="arial 15",bg='yellow',padx=60).grid(row=3,column=0)

# Product remain
quantity_product1 = 20
quantity_product2 = 10
quantity_product3 = 0
quantity_product4 = 7
quantity_product5 = 20
quantity_product6 = 1
quantity_product7 = 10
quantity_product8 = 15

remain_product1=Label(lf_product1,text=str(quantity_product1)+" can",font="arial 15",bg='azure2',padx=65)
remain_product1.grid(row=4,column=0)
remain_product2=Label(lf_product2,text=str(quantity_product2)+" can",font="arial 15",bg='azure2',padx=65)
remain_product2.grid(row=4,column=0)
remain_product3=Label(lf_product3,text="0"+str(quantity_product3)+" can",font="arial 15",bg='azure2',padx=65)
remain_product3.grid(row=4,column=0)
remain_product4=Label(lf_product4,text="0"+str(quantity_product4)+" can",font="arial 15",bg='azure2',padx=65)
remain_product4.grid(row=4,column=0)
remain_product5=Label(lf_product5,text=str(quantity_product5)+" pack",font="arial 15",bg='azure2',padx=60)
remain_product5.grid(row=4,column=0)
remain_product6=Label(lf_product6,text="0"+str(quantity_product6)+" pack",font="arial 15",bg='azure2',padx=60)
remain_product6.grid(row=4,column=0)
remain_product7=Label(lf_product7,text=str(quantity_product7)+" pack",font="arial 15",bg='azure2',padx=60)
remain_product7.grid(row=4,column=0)
remain_product8=Label(lf_product8,text=str(quantity_product8)+" pack",font="arial 15",bg='azure2',padx=60)
remain_product8.grid(row=4,column=0)

#Recognize
entry_text2 = StringVar()
def Recognize():
    import cv2
    import numpy as np
    from keras.applications.vgg16 import VGG16
    from keras.layers import Input, Flatten, Dense, Dropout
    from keras.models import Model
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    # Dinh nghia class
    class_name = ['00000', '10000', '100000', '20000', '5000', '50000']
    def get_model():
        model_vgg16_conv = VGG16(weights='imagenet', include_top=False)
        # Dong bang cac layer
        for layer in model_vgg16_conv.layers:
            layer.trainable = False
        # Tao model
        input = Input(shape=(128, 128, 3), name='image_input')
        output_vgg16_conv = model_vgg16_conv(input)
        # Them cac layer FC va Dropout
        x = Flatten(name='flatten')(output_vgg16_conv)
        x = Dense(4096, activation='relu', name='fc1')(x)
        x = Dropout(0.5)(x)
        x = Dense(4096, activation='relu', name='fc2')(x)
        x = Dropout(0.5)(x)
        x = Dense(6, activation='softmax', name='predictions')(x)
        # Compile
        my_model = Model(inputs=input, outputs=x)
        my_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return my_model
    # Load weights model da train
    my_model = get_model()
    my_model.load_weights("E:\VSCODE\Thesis\weights-47-0.99.hdf5")
    # stuff to run always here such as class/def
    while (True):
        # Capture frame-by-frame
        ret, image_org = cap.read()
        if not ret:
            continue
        image_org = cv2.resize(image_org, dsize=None, fx=1, fy=1)
        # Resize
        image = image_org.copy()
        image = cv2.resize(image, dsize=(128, 128))
        image = image.astype('float') * 1. / 255
        # Convert to tensor
        image = np.expand_dims(image, axis=0)
        # Predict
        predict = my_model.predict(image)
        print("This picture is: ", class_name[np.argmax(predict[0])], (predict[0]))
        print(np.max(predict[0], axis=0))
        if (np.max(predict) >= 0.8) and (np.argmax(predict[0]) != 0):
            # Show image
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (50, 50)
            fontScale = 1.5
            color = (0, 255, 0)
            thickness = 2
            cv2.putText(image_org, class_name[np.argmax(predict)], org, font,
                        fontScale, color, thickness, cv2.LINE_AA)
        cv2.imshow("Picture", image_org)
        # press q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Final Value
    global money_value
    money_value = class_name[np.argmax(predict)]
    code1 = textbox1.get()
    money1 = textbox2.get()
    if money1=="" or code1=="":
        entry_text2.set(money_value)
    else:
        if code1=='001':
            if (int(money1)<price1):
                entry_text2.set(str(int(money_value)+int(money1)))
            else:
                entry_text2.set(money_value)
        elif code1=='002':
            if (int(money1)<price2):
                entry_text2.set(str(int(money_value)+int(money1)))
            else:
                entry_text2.set(money_value)
        elif code1=='003':
            if (int(money1)<price3):
                entry_text2.set(str(int(money_value)+int(money1)))
            else:
                entry_text2.set(money_value)
        elif code1=='004':
            if (int(money1)<price4):
                entry_text2.set(str(int(money_value)+int(money1)))
            else:
                entry_text2.set(money_value)
        elif code1=='005':
            if (int(money1)<price5):
                entry_text2.set(str(int(money_value)+int(money1)))
            else:
                entry_text2.set(money_value)
        elif code1=='006':
            if (int(money1)<price6):
                entry_text2.set(str(int(money_value)+int(money1)))
            else:
                entry_text2.set(money_value)
        elif code1=='007':
            if (int(money1)<price7):
                entry_text2.set(str(int(money_value)+int(money1)))
            else:
                entry_text2.set(money_value)
        elif code1=='008':
            if (int(money1)<price8):
                entry_text2.set(str(int(money_value)+int(money1)))
            else:
                entry_text2.set(money_value)
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

# Create the textboxes
LabelText=StringVar()
LabelText.set("Product Code ")
labelDir=Label(Button_frame, textvariable=LabelText, font=("Arial",15),bg='lightpink')
labelDir.pack()
labelDir.place(x=3,y=10)
entry_text1 = StringVar()
textbox1 = Entry(Button_frame,width=13,bg='aquamarine1',font=('Arial 22'),justify=CENTER,textvariable=entry_text1)
textbox1.pack()
textbox1.place(x=131,y=7)
textbox1.bind("<Button-1>", lambda event: activate_textbox(textbox1))

btn = Button(Button_frame, text="Input\nCash", bg="Orange", fg="Black",height=3,width=7, font=('arial 18'),command=Recognize)
btn.place(x=0,y=482)

LabelText=StringVar()
LabelText.set("Money Input")
labelDir=Label(Button_frame, textvariable=LabelText, font=("Arial",17),bg='lightpink')
labelDir.pack()
labelDir.place(x=3,y=58)
textbox2 = Entry(Button_frame,width=13,bg='aquamarine1',font=('Arial 22'),textvariable=entry_text2,justify=CENTER)
textbox2.pack()
textbox2.place(x=131,y=56)
textbox2.bind("<Button-1>", lambda event: activate_textbox(textbox2))

def update_textbox(textbox, key):
    current_text = textbox.get()
    new_text = current_text + str(key)
    textbox.delete(0, END)
    textbox.insert(0, new_text)

# Keypad
keypad_frame = Frame(Button_frame,background='bisque1')
keypad_frame.pack()
keypad_frame.place(x=63,y=130)

keys = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['OK', '0', 'Clear']
]

for i, row in enumerate(keys):
    for j, key in enumerate(row):
        button = Button(
            keypad_frame,
            text=key,
            width=4,
            height=2,
            font=('arial 18'),
            command=lambda key=key: handle_keypress(key),
            background='azure2'
        )
        button.grid(row=i, column=j, padx=2, pady=2)

def handle_keypress(key):
    if key.isdigit():
        update_textbox(textbox1, key)
    elif key == 'Clear':
        clear_textbox()
    elif key == 'OK':
        Process()
        perform_action()

def clear_textbox():
    textbox1.delete(0, END)

def perform_action():
    value1 = textbox1.get()
    value2 = textbox2.get()
    # Perform your desired action with the values from the textboxes
    print("Textbox 1 value:", value1)
    print("Textbox 2 value:", value2)

def activate_textbox(textbox):
    global active_textbox
    active_textbox = textbox

def restart():
    entry_text1.set('')
    entry_text2.set('')

btn = Button(Button_frame, text="Cancel", bg="Orange", fg="Black",height=3,width=7,font=('arial 18'),command=restart)
btn.place(x=237,y=482)

def Process():
    notice=Tk()
    notice.title("Notice")
    notice.configure(background='mintcream')
    code = textbox1.get()
    money = textbox2.get()
    if money=='':
        Label(notice, text='Please Input Cash!', font=('Arial', 30), fg='red', bg='mintcream').pack(padx=30, pady=30)
    elif code=='':
        Label(notice, text='Please Input Product Code!', font=('Arial', 30), fg='red', bg='mintcream').pack(padx=30, pady=30)
    else:
        if code=='001':
            global quantity_product1
            if quantity_product1<=0:
                Label(notice, text='Sold out!\n Please choose another product!', font=('Arial', 30), fg='red', bg='mintcream').pack(padx=30, pady=30)
                entry_text1.set('')
            else:
                if int(money)<price1:
                    Label(notice,text='Not enough money!\n Please choose another product or Input extra money!', font=('Arial',30),fg='red',bg='mintcream').pack(padx=30,pady=30)
                elif money==str(price1):
                    Label(notice,text='Successful!', font=('Arial',50),fg='green3',bg='mintcream').pack(padx=30,pady=30)
                    restart()
                    quantity_product1=quantity_product1-1
                    if quantity_product1<10:
                        remain_product1.config(text='0'+str(quantity_product1)+' can')
                    else:
                        remain_product1.config(text=str(quantity_product1)+' can')
                else:
                    du=int(money)-price1
                    Label(notice,text='Successful! Refund: '+str(du)+'Đ', font=('Arial',50),fg='#FF6103',bg='mintcream').pack(padx=30,pady=30)
                    restart()
                    quantity_product1=quantity_product1-1
                    if quantity_product1<10:
                        remain_product1.config(text='0'+str(quantity_product1)+' can')
                    else:
                        remain_product1.config(text=str(quantity_product1)+' can')
        elif code=='002':
            global quantity_product2
            if quantity_product2<=0:
                Label(notice, text='Sold out!\n Please choose another product!', font=('Arial', 30), fg='red', bg='mintcream').pack(padx=30, pady=30)
                entry_text1.set('')
            else:
                if int(money)<price2:
                    Label(notice,text='Not enough money!\n Please choose another product or Input extra money!', font=('Arial',30),fg='red',bg='mintcream').pack(padx=30,pady=30)
                elif money==str(price2):
                    Label(notice,text='Successful!', font=('Arial',50),fg='green3',bg='mintcream').pack(padx=30,pady=30)
                    restart()
                    quantity_product2=quantity_product2-1
                    if quantity_product2<10:
                        remain_product2.config(text='0'+str(quantity_product2)+' can')
                    else:
                        remain_product2.config(text=str(quantity_product2)+' can')
                else:
                    du=int(money)-price2
                    Label(notice,text='Successful! Refund: '+str(du)+'Đ', font=('Arial',50),fg='#FF6103',bg='mintcream').pack(padx=30,pady=30)
                    restart()
                    quantity_product2=quantity_product2-1
                    if quantity_product2<10:
                        remain_product2.config(text='0'+str(quantity_product2)+' can')
                    else:
                        remain_product2.config(text=str(quantity_product2)+' can')
        elif code=='003':
            global quantity_product3
            if quantity_product3<=0:
                Label(notice, text='Sold out!\n Please choose another product!', font=('Arial', 30), fg='red', bg='mintcream').pack(padx=30, pady=30)
                entry_text1.set('')
            else:
                if int(money)<price3:
                    Label(notice,text='Not enough money!\n Please choose another product or Input extra money!', font=('Arial',30),fg='red',bg='mintcream').pack(padx=30,pady=30)
                elif money==str(price3):
                    Label(notice,text='Successful!', font=('Arial',50),fg='green3',bg='mintcream').pack(padx=30,pady=30)
                    restart()
                    quantity_product3=quantity_product3-1
                    if quantity_product3<10:
                        remain_product3.config(text='0'+str(quantity_product3)+' can')
                    else:
                        remain_product3.config(text=str(quantity_product3)+' can')
                else:
                    du=int(money)-price3
                    Label(notice,text='Successful! Refund: '+str(du)+'Đ', font=('Arial',50),fg='#FF6103',bg='mintcream').pack(padx=30,pady=30)
                    restart()
                    quantity_product3=quantity_product3-1
                    if quantity_product3<10:
                        remain_product3.config(text='0'+str(quantity_product3)+' can')
                    else:
                        remain_product3.config(text=str(quantity_product3)+' can')
        elif code=='004':
            global quantity_product4
            if quantity_product4<=0:
                Label(notice, text='Sold out!\n Please choose another product!', font=('Arial', 30), fg='red', bg='mintcream').pack(padx=30, pady=30)
                entry_text1.set('')
            else:
                if int(money)<price4:
                    Label(notice,text='Not enough money!\n Please choose another product or Input extra money!', font=('Arial',30),fg='red',bg='mintcream').pack(padx=30,pady=30)
                elif money==str(price4):
                    Label(notice,text='Successful!', font=('Arial',50),fg='green3',bg='mintcream').pack(padx=30,pady=30)
                    restart()
                    quantity_product4=quantity_product4-1
                    if quantity_product4<10:
                        remain_product4.config(text='0'+str(quantity_product4)+' can')
                    else:
                        remain_product4.config(text=str(quantity_product4)+' can')
                else:
                    du=int(money)-price4
                    Label(notice,text='Successful! Refund: '+str(du)+'Đ', font=('Arial',50),fg='#FF6103',bg='mintcream').pack(padx=30,pady=30)
                    restart()
                    quantity_product4=quantity_product4-1
                    if quantity_product4<10:
                        remain_product4.config(text='0'+str(quantity_product4)+' can')
                    else:
                        remain_product4.config(text=str(quantity_product4)+' can')
        elif code=='005':
            global quantity_product5
            if quantity_product5<=0:
                Label(notice, text='Sold out!\n Please choose another product!', font=('Arial', 30), fg='red', bg='mintcream').pack(padx=30, pady=30)
                entry_text1.set('')
            else:
                if int(money)<price5:
                    Label(notice,text='Not enough money!\n Please choose another product or Input extra money!', font=('Arial',30),fg='red',bg='mintcream').pack(padx=30,pady=30)
                elif money==str(price5):
                    Label(notice,text='Successful!', font=('Arial',50),fg='green3',bg='mintcream').pack(padx=30,pady=30)
                    restart()
                    quantity_product5=quantity_product5-1
                    if quantity_product5<10:
                        remain_product5.config(text='0'+str(quantity_product5)+' pack')
                    else:
                        remain_product5.config(text=str(quantity_product5)+' pack')
                else:
                    du=int(money)-price5
                    Label(notice,text='Successful! Refund: '+str(du)+'Đ', font=('Arial',50),fg='#FF6103',bg='mintcream').pack(padx=30,pady=30)
                    restart()
                    quantity_product5=quantity_product5-1
                    if quantity_product5<10:
                        remain_product5.config(text='0'+str(quantity_product5)+' pack')
                    else:
                        remain_product5.config(text=str(quantity_product5)+' pack')
        elif code=='006':
            global quantity_product6
            if quantity_product6<=0:
                Label(notice, text='Sold out!\n Please choose another product!', font=('Arial', 30), fg='red', bg='mintcream').pack(padx=30, pady=30)
                entry_text1.set('')
            else:
                if int(money)<price6:
                    Label(notice,text='Not enough money!\n Please choose another product or Input extra money!', font=('Arial',30),fg='red',bg='mintcream').pack(padx=30,pady=30)
                elif money==str(price6):
                    Label(notice,text='Successful!', font=('Arial',50),fg='green3',bg='mintcream').pack(padx=30,pady=30)
                    restart()
                    quantity_product6=quantity_product6-1
                    if quantity_product6<10:
                        remain_product6.config(text='0'+str(quantity_product6)+' pack')
                    else:
                        remain_product6.config(text=str(quantity_product6)+' pack')
                else:
                    du=int(money)-price6
                    Label(notice,text='Successful! Refund: '+str(du)+'Đ', font=('Arial',50),fg='#FF6103',bg='mintcream').pack(padx=30,pady=30)
                    restart()
                    quantity_product6=quantity_product6-1
                    if quantity_product6<10:
                        remain_product6.config(text='0'+str(quantity_product6)+' pack')
                    else:
                        remain_product6.config(text=str(quantity_product6)+' pack')
        elif code=='007':
            global quantity_product7
            if quantity_product7<=0:
                Label(notice, text='Sold out!\n Please choose another product!', font=('Arial', 30), fg='red', bg='mintcream').pack(padx=30, pady=30)
                entry_text1.set('')
            else:
                if int(money)<price7:
                    Label(notice,text='Not enough money!\n Please choose another product or Input extra money!', font=('Arial',30),fg='red',bg='mintcream').pack(padx=30,pady=30)
                elif money==str(price7):
                    Label(notice,text='Successful!', font=('Arial',50),fg='green3',bg='mintcream').pack(padx=30,pady=30)
                    restart()
                    quantity_product7=quantity_product7-1
                    if quantity_product7<10:
                        remain_product7.config(text='0'+str(quantity_product7)+' pack')
                    else:
                        remain_product7.config(text=str(quantity_product7)+' pack')
                else:
                    du=int(money)-price7
                    Label(notice,text='Successful! Refund: '+str(du)+'Đ', font=('Arial',50),fg='#FF6103',bg='mintcream').pack(padx=30,pady=30)
                    restart()
                    quantity_product7=quantity_product7-1
                    if quantity_product7<10:
                        remain_product7.config(text='0'+str(quantity_product7)+' pack')
                    else:
                        remain_product7.config(text=str(quantity_product7)+' pack')
        elif code=='008':
            global quantity_product8
            if quantity_product8<=0:
                Label(notice, text='Sold out!\n Please choose another product!', font=('Arial', 30), fg='red', bg='mintcream').pack(padx=30, pady=30)
                entry_text1.set('')
            else:
                if int(money)<price8:
                    Label(notice,text='Not enough money!\n Please choose another product or Input extra money!', font=('Arial',30),fg='red',bg='mintcream').pack(padx=30,pady=30)
                elif money==str(price8):
                    Label(notice,text='Successful!', font=('Arial',50),fg='green3',bg='mintcream').pack(padx=30,pady=30)
                    restart()
                    quantity_product8=quantity_product8-1
                    if quantity_product8<10:
                        remain_product8.config(text='0'+str(quantity_product8)+' pack')
                    else:
                        remain_product8.config(text=str(quantity_product8)+' pack')
                else:
                    du=int(money)-price8
                    Label(notice,text='Successful! Refund: '+str(du)+'Đ', font=('Arial',50),fg='#FF6103',bg='mintcream').pack(padx=30,pady=30)
                    restart()
                    quantity_product8=quantity_product8-1
                    if quantity_product8<10:
                        remain_product8.config(text='0'+str(quantity_product8)+' pack')
                    else:
                        remain_product8.config(text=str(quantity_product8)+' pack')
        else:
            Label(notice,text='Invalid product code!\nEnter another one!', font=('Arial',30),fg='red',bg='mintcream').pack(padx=30,pady=30)
            entry_text1.set('')
root.mainloop()