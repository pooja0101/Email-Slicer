from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
import tkinter as tk

window = Tk()
window.title("EMAIL SLICER")
window.minsize(700,500)
window.maxsize(700,500)

FONT = font.Font(family ="Bernard MT Condensed", size ="10", weight ="bold")
background_image = ImageTk.PhotoImage(Image.open("email.jpg"))
background_label = Label(window, image = background_image)
background_label.place(relwidth = 1, relheight =1)

def result():
    try:
        email = entry.get()
        inp_email = email.strip()
        username = inp_email[0:inp_email.index('@')]
        domain = inp_email[inp_email.index('@') + 1:]
        text_box.delete('1.0', tk.END)
        msg = ' Email id   : {}\n\n Email username : {}\n Domain server : {}'
        msg_formatted = msg.format(email, username, domain)
        text_box.insert(tk.END, msg_formatted)
        entry.delete(0, 'end')
    except:
        text_box.delete('1.0', tk.END)
        text_box.insert(tk.END, "ERROR!")


def reset_all():
    text_box.delete('1.0', tk.END)
    entry.delete(0, 'end')


# Labels
greeting = tk.Label(text=" Email Slicer", font=("Engravers MT",20), foreground="white", background="#383838")

entry_label = tk.Label(foreground="white", font=(8), background="#383838", text="Enter Your Email Id: ")

# Entry
e1 = tk.StringVar()
entry = tk.Entry(font=(11), width=28,  textvariable=e1,bg="BLACK",fg="white")

# Buttons
button = tk.Button(text="Done!", command=result, font=("Engravers MT",11),bd=6,bg="#808080",fg="BLACK")
reset = tk.Button(text="Reset!", command=reset_all, font=("Engravers MT",11),bd=6,bg="#808080",fg="BLACK")

# Result
text_box = tk.Text(height=5, width=50,bg="BLACK",fg="white")
text_box.place(relx=0.38,rely=0.79)
# Packing Everything Together
# empty_label0.pack()
greeting.place(relx=0.3,rely=0.05)

# empty_label1.pack()
entry_label.place(relx=0.06,rely=0.22)
#empty_label4.pack()
entry.place(relx=0.06,rely=0.28,height=30)
#empty_label2.pack()
button.place(relx=0.5,rely=0.65)
#empty_label5.pack()
reset.place(relx=0.7,rely=0.65)
#empty_label3.pack()



window.mainloop()