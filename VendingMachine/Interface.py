from tkinter import *
from tkinter import messagebox
import PIL as p
import PIL.ImageTk as ptk
import os
from subprocess import Popen
import sys

from datetime import datetime
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
tagline=Label(Heading,text="Shopping made easier!",font="arial 16",fg="gold",bg="black").grid(row=0,column=2,padx=280)

# Button Frame
Button_frame=LabelFrame(root,bd=2,relief="groove",text="Button",font="arial 16 bold",fg="dark blue",bg='seashell1')
Button_frame.place(x=2,y=60,width=350,height=620)

# Product Frame
Products_frame=LabelFrame(root,bd=2,relief="groove",text="Products",font="arial 16 bold",fg="dark blue",bg='seashell1')
Products_frame.place(x=355,y=60,width=843,height=620)

# Grocery
grocery1_image=ptk.PhotoImage(p.Image.open("E:\VSCODE\Thesis\VendingMachine\Images\coca_cola.jpg"))
grocery2_image=ptk.PhotoImage(p.Image.open("E:\VSCODE\Thesis\VendingMachine\Images\pepsi.jpg"))
grocery3_image=ptk.PhotoImage(p.Image.open("E:\VSCODE\Thesis\VendingMachine\Images\lfanta.png"))
grocery4_image=ptk.PhotoImage(p.Image.open("E:\VSCODE\Thesis\VendingMachine\Images\mirinda_orange.png"))
grocery5_image=ptk.PhotoImage(p.Image.open("E:\VSCODE\Thesis\VendingMachine\Images\Snack_1.png"))
grocery6_image=ptk.PhotoImage(p.Image.open("E:\VSCODE\Thesis\VendingMachine\Images\Snack_2.jpg"))
grocery7_image=ptk.PhotoImage(p.Image.open("E:\VSCODE\Thesis\VendingMachine\Images\Snack_3.jpg"))
grocery8_image=ptk.PhotoImage(p.Image.open("E:\VSCODE\Thesis\VendingMachine\Images\Snack_4.jpg"))

# Function Hide all Frame
def HideAllFrames():
    for widget in Products_frame.winfo_children():
        widget.destroy()

# Grocery //cach nhau 210
# row 1
lf_grocery1=LabelFrame(Products_frame,bd=2,relief="groove",bg='rosybrown1')
lf_grocery1.place(x=5,y=10,width=200,height=286)
lf_grocery2=LabelFrame(Products_frame,bd=2,relief="groove",bg='rosybrown1')
lf_grocery2.place(x=215,y=10,width=200,height=286)
lf_grocery3=LabelFrame(Products_frame,bd=2,relief="groove",bg='rosybrown1')
lf_grocery3.place(x=425,y=10,width=200,height=286)
lf_grocery4=LabelFrame(Products_frame,bd=2,relief="groove",bg='rosybrown1')
lf_grocery4.place(x=635,y=10,width=200,height=286)
# row 2
lf_grocery6=LabelFrame(Products_frame,bd=2,relief="groove",bg='rosybrown1')
lf_grocery6.place(x=5,y=300,width=200,height=286)
lf_grocery7=LabelFrame(Products_frame,bd=2,relief="groove",bg='rosybrown1')
lf_grocery7.place(x=215,y=300,width=200,height=286)
lf_grocery8=LabelFrame(Products_frame,bd=2,relief="groove",bg='rosybrown1')
lf_grocery8.place(x=425,y=300,width=200,height=286)
lf_grocery5=LabelFrame(Products_frame,bd=2,relief="groove",bg='rosybrown1')
lf_grocery5.place(x=635,y=300,width=200,height=286)

# Product code
code_grocery1=Label(lf_grocery1,text="001",font="arial 15",bg='aqua',fg='red',justify="center",padx=79).grid(row=0,column=0)
code_grocery2=Label(lf_grocery2,text="002",font="arial 15",bg='aqua',fg='red',justify="center",padx=79).grid(row=0,column=0)
code_grocery3=Label(lf_grocery3,text="003",font="arial 15",bg='aqua',fg='red',justify="center",padx=79).grid(row=0,column=0)
code_grocery4=Label(lf_grocery4,text="004",font="arial 15",bg='aqua',fg='red',justify="center",padx=79).grid(row=0,column=0)
code_grocery5=Label(lf_grocery5,text="005",font="arial 15",bg='aqua',fg='red',justify="center",padx=79).grid(row=0,column=0)
code_grocery6=Label(lf_grocery6,text="006",font="arial 15",bg='aqua',fg='red',justify="center",padx=79).grid(row=0,column=0)
code_grocery7=Label(lf_grocery7,text="007",font="arial 15",bg='aqua',fg='red',justify="center",padx=79).grid(row=0,column=0)
code_grocery8=Label(lf_grocery8,text="008",font="arial 15",bg='aqua',fg='red',justify="center",padx=79).grid(row=0,column=0)

# Product image
label_grocery_1=Label(lf_grocery1,image=grocery1_image,bd=2).grid(row=1,column=0)
label_grocery_2=Label(lf_grocery2,image=grocery2_image,bd=2).grid(row=1,column=0)
label_grocery_3=Label(lf_grocery3,image=grocery3_image,bd=2).grid(row=1,column=0)
label_grocery_4=Label(lf_grocery4,image=grocery4_image,bd=2).grid(row=1,column=0)
label_grocery_5=Label(lf_grocery5,image=grocery5_image,bd=2).grid(row=1,column=0)
label_grocery_6=Label(lf_grocery6,image=grocery6_image,bd=2).grid(row=1,column=0)
label_grocery_7=Label(lf_grocery7,image=grocery7_image,bd=2).grid(row=1,column=0)
label_grocery_8=Label(lf_grocery8,image=grocery8_image,bd=2).grid(row=1,column=0)

# Product name
# name_grocery1=Label(lf_grocery1,text="Coca Cola",font="arial 12",bg='yellow').grid(row=3,column=0,padx=20)
# name_grocery2=Label(lf_grocery2,text="Pepsi",font="arial 12",justify="center",bg='yellow').grid(row=3,column=0,padx=15)
# name_grocery3=Label(lf_grocery3,text="Fanta",font="arial 12",justify="center",bg='yellow').grid(row=3,column=0)
# name_grocery4=Label(lf_grocery4,text="Mirinda",font="arial 12",justify="center",bg='yellow').grid(row=3,column=0,padx=9)
# name_grocery5=Label(lf_grocery5,text="Snack Ostar",font="arial 12",justify="center",bg='yellow').grid(row=3,column=0,padx=9)
# name_grocery6=Label(lf_grocery6,text="Snack Pumpkin",font="arial 12",justify="center",bg='yellow').grid(row=3,column=0,padx=15)
# name_grocery7=Label(lf_grocery7,text="Snack Indochips",font="arial 12",justify="center",bg='yellow').grid(row=3,column=0)
# name_grocery8=Label(lf_grocery8,text="Snack Maize",font="arial 12",justify="center",bg='yellow').grid(row=3,column=0,padx=20)

# Product price
price_grocery1=Label(lf_grocery1,text="10000Đ",font="arial 15",bg='yellow',padx=60).grid(row=3,column=0)
price_grocery2=Label(lf_grocery2,text="10000Đ",font="arial 15",bg='yellow',padx=60).grid(row=3,column=0)
price_grocery3=Label(lf_grocery3,text="10000Đ",font="arial 15",bg='yellow',padx=60).grid(row=3,column=0)
price_grocery4=Label(lf_grocery4,text="10000Đ",font="arial 15",bg='yellow',padx=60).grid(row=3,column=0)
price_grocery5=Label(lf_grocery5,text="5000Đ",font="arial 15",bg='yellow',padx=66).grid(row=3,column=0)
price_grocery6=Label(lf_grocery6,text="5000Đ",font="arial 15",bg='yellow',padx=66).grid(row=3,column=0)
price_grocery7=Label(lf_grocery7,text="5000Đ",font="arial 15",bg='yellow',padx=66).grid(row=3,column=0)
price_grocery8=Label(lf_grocery8,text="5000Đ",font="arial 15",bg='yellow',padx=66).grid(row=3,column=0)

# Product remain
remain_grocery1=Label(lf_grocery1,text="20 can",font="arial 15",bg='azure2',padx=65).grid(row=4,column=0)
remain_grocery2=Label(lf_grocery2,text="20 can",font="arial 15",bg='azure2',padx=65).grid(row=4,column=0)
remain_grocery3=Label(lf_grocery3,text="20 can",font="arial 15",bg='azure2',padx=65).grid(row=4,column=0)
remain_grocery4=Label(lf_grocery4,text="20 can",font="arial 15",bg='azure2',padx=65).grid(row=4,column=0)
remain_grocery5=Label(lf_grocery5,text="20 pack",font="arial 15",bg='azure2',padx=60).grid(row=4,column=0)
remain_grocery6=Label(lf_grocery6,text="20 pack",font="arial 15",bg='azure2',padx=60).grid(row=4,column=0)
remain_grocery7=Label(lf_grocery7,text="20 pack",font="arial 15",bg='azure2',padx=60).grid(row=4,column=0)
remain_grocery8=Label(lf_grocery8,text="20 pack",font="arial 15",bg='azure2',padx=60).grid(row=4,column=0)

#Recognize
entry_text2 = StringVar()
def Recognize():
    import cv2
    import numpy as np
    from keras.applications.vgg16 import VGG16
    from keras.layers import Input, Flatten, Dense, Dropout
    from keras.models import Model
    cap = cv2.VideoCapture(0)
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
    my_model.load_weights("E:\VSCODE\Thesis\weights-31-0.98.hdf5")
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
    entry_text2.set(money_value)
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

# Create the textboxes
entry_text1 = StringVar()
textbox1 = Entry(Button_frame,width=15,bg='aquamarine1',font=('Arial 25'),justify=CENTER,textvariable=entry_text1)
textbox1.pack()
textbox1.place(x=35,y=10)
textbox1.bind("<Button-1>", lambda event: activate_textbox(textbox1))
# textbox2 = Entry(Button_frame,width=15,bg='aquamarine1',font=('Arial 25'))
# textbox2.pack()
# textbox2.place(x=35,y=58)
# textbox2.bind("<Button-1>", lambda event: activate_textbox(textbox2))

btn = Button(Button_frame, text="Input\nCash", bg="Orange", fg="Black",height=3,width=7, font=('arial 18'),command=Recognize)
btn.place(x=0,y=482)

textbox2 = Entry(Button_frame,width=15,bg='aquamarine1',font=('Arial 25'),textvariable=entry_text2,justify=CENTER)
textbox2.pack()
textbox2.place(x=35,y=58)
# entry_text2.set('Hello')
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

# Button
# def run1():
#     Popen([sys.executable,'E:\VSCODE\Thesis\Test.py'])



def run2():
    entry_text1.set('')
    entry_text2.set('')

btn = Button(Button_frame, text="Cancel", bg="Orange", fg="Black",height=3,width=7,font=('arial 18'),command=run2)
btn.place(x=237,y=482)

def Xuly():
    code = textbox1.get()
    money = textbox2.get()
    if code=='001' or code=='002' or code =='003' or code =='004' :
        p_money='10000'
    else:
        p_money='5000'
    if money<p_money:
        op=messagebox.showinfo('Notice','Not enough money')
    elif money==p_money:
        op = messagebox.showinfo('Notice', 'Successful')
    else:
        du=int(money)-int(p_money)
        op = messagebox.showinfo('Notice', 'Tiền thừa: '+str(du))
root.mainloop()