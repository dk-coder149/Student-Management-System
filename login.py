import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # only needed if you are using images
# import Student_management_sys

name="dileep"
psd="123"
def login():
    # get the text from the Entry widgets
    u_name=username.get()
    p=password.get()
    
    if u_name == '' or p == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif(name==u_name and psd==p):
        w.destroy()
        import Student_management_sys

    else:
        messagebox.showerror('Error', 'wrong username or password')
    
        
        
        
# Create main window
w = tk.Tk()
w.title("Student Management System - Login")
w.geometry("1000x600")


##### ----------- user image -----------
pil_img=Image.open('C:/Users/HP/OneDrive/Desktop/student management/user_icon.png')

resize_img=pil_img.resize((200,230),Image.LANCZOS)

img=ImageTk.PhotoImage(resize_img)

img_lael=tk.Label(w, image=img)
img_lael.place(x=400,y=0)






# Username label & entry

user_label = tk.Label(w, text="Username", font=("Arial",25), pady=10)
user_label.place(x=300, y=250)

username = tk.Entry(w, font=("Arial",20))
username.place(x=500, y=260)

# Password label & entry
password_label = tk.Label(w, text="Password", font=("Arial",25), pady=10)
password_label.place(x=300, y=300)

password= tk.Entry(w, font=("Arial",20), show="*")
password.place(x=500, y=310)

# Login button
login_btn = tk.Button(w, text="Login", bg="blue", pady=15, width=25, font=('arial',15,'bold'),
                    activebackground="cornflowerblue", command=login)
login_btn.place(x=450, y=380)

# Run the GUI main loop
w.mainloop()
