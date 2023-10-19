import tkinter as tk

def update_textbox(textbox, key):
    current_text = textbox.get()
    new_text = current_text + str(key)
    textbox.delete(0, tk.END)
    textbox.insert(0, new_text)

def handle_keypress(key):
    if key.isdigit():
        update_textbox(active_textbox, key)
    elif key == 'Clear':
        clear_textbox()
    elif key == 'OK':
        perform_action()

def clear_textbox():
    active_textbox.delete(0, tk.END)

def perform_action():
    value1 = textbox1.get()
    value2 = textbox2.get()
    # Perform your desired action with the values from the textboxes
    print("Textbox 1 value:", value1)
    print("Textbox 2 value:", value2)

def activate_textbox(textbox):
    global active_textbox
    active_textbox = textbox

# Create the GUI window
window = tk.Tk()

# Create the textboxes
textbox1 = tk.Entry(window)
textbox1.pack()
textbox1.bind("<Button-1>", lambda event: activate_textbox(textbox1))

textbox2 = tk.Entry(window)
textbox2.pack()
textbox2.bind("<Button-1>", lambda event: activate_textbox(textbox2))

# Create the keypad
keypad_frame = tk.Frame(window)
keypad_frame.pack()

keys = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['0', 'Clear', 'OK']
]

for i, row in enumerate(keys):
    for j, key in enumerate(row):
        button = tk.Button(
            keypad_frame,
            text=key,
            width=5,
            height=2,
            command=lambda key=key: handle_keypress(key)
        )
        button.grid(row=i, column=j, padx=5, pady=5)

# Run the GUI window
window.mainloop()