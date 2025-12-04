

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector as connector

import database
# import ttkthemes




def delete():
    pass



def selection(event):
    selected_items=student_table.selection()
    # print(selected_items)
    if selected_items:
        row=student_table.item(selected_items)['values']
        # print(row)
        clear()
        id_ent.insert(0,row[0])
        name_ent.insert(0,row[1])
        fname_ent.insert(0,row[2])
        gender.set(row[5])
        dob_ent.insert(0,row[3])
        email_ent.insert(0,row[4])
        class_opt.set(row[6])
        sec_opt.set(row[7])
        con_ent.insert(0,row[8])
        add_ent.insert("1.0", row[9])   # because it is text widget not entry 


###  make slider
count=0
text=''
def slider():
    global text, count
    if count==len(txt):
        count=0
        text='' 
    text+=txt[count]
    heading.config(text=text)
    count+=1
    heading.after(300, slider)
    # time.sleep(5)




# // using connect button

def clear(val=False):
    if val:
        student_table.selection_remove(student_table.focus())
    id_ent.delete(0, tk.END)
    name_ent.delete(0, tk.END)
    fname_ent.delete(0, tk.END)
    gender.set("Male")
    class_opt.set("BCA")
    sec_opt.set("BCA")
    dob_ent.delete(0, tk.END)
    email_ent.delete(0, tk.END)
    con_ent.delete(0, tk.END)
    add_ent.delete("1.0", tk.END)
    

def treeViewData():
    records=database.fetch_records()
    student_table.delete(*student_table.get_children())
    for record in records:
        student_table.insert("",'end', values=record)



def add():
    # Check mandatory fields (use .get() on all)
    if (id_ent.get() == '' or
        name_ent.get() == '' or
        fname_ent.get() == '' or
        dob_ent.get() == '' or
        email_ent.get() == '' or
        gender.get() == '' or
        class_opt.get() == '' or
        sec_opt.get() == '' or
        con_ent.get() == '' or
        add_ent.get("1.0", "end-1c").strip() == ''):
        messagebox.showerror('Error', 'All fields are mandatory')
        return

    # Check duplicate ID
    if database.id_exists(id_ent.get()):
        messagebox.showerror('Error', 'This ID already exists')
        return

    # Insert the record
    database.insert(
        id_ent.get(),
        name_ent.get(),
        fname_ent.get(),
        dob_ent.get(),
        email_ent.get(),
        gender.get(),
        class_opt.get(),
        sec_opt.get(),
        con_ent.get(),
        add_ent.get("1.0", "end-1c")
    )
    # Refresh tree view or display updated data
    treeViewData()
    # Clear the input fields
    clear()
    # Show success message
    messagebox.showinfo('Success', "Record added successfully")



  ## ------------ UPDATE ---------------
def update():
    selected_item=student_table.selection()    # it will return the id of student
    if not selected_item:
        messagebox.showerror('Error','Select data to update')
    else:
        database.update(
        id_ent.get(),
        name_ent.get(),
        fname_ent.get(),
        dob_ent.get(),
        email_ent.get(),
        gender.get(),
        class_opt.get(),
        sec_opt.get(),
        con_ent.get(),
        add_ent.get("1.0", "end-1c")
        )

        treeViewData()
        clear()
        messagebox.showinfo('successfull', 'Record updated successfully')


## -------------- Delete -------------------
def delete():   #   add new student
    selected_item=student_table.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select record to delete')
    else:
        database.delete(id_ent.get())
        clear()
        messagebox.showerror('Error','Data is deleted')
        treeViewData()
  

def search_record():
    if search_entry=='':
        messagebox.showerror('Error', 'Enter the value to search')
    elif search_box.get()=='Search By':
        messagebox.showerror("Error",'Please select an option')
    else:
        data=database.search(search_box.get(),search_entry.get())
        # print(data)
        student_table.delete(*student_table.get_children())
        for record in data:
            student_table.insert("",'end', values=record)


def show_all():
    treeViewData()
    search_entry.delete(0,tk.END)
    search_box.set('Search By')




def delete_all():
    result=messagebox.askyesno('Confirm'," Do you realy want to delete all the records ?")
    if result:
        database.delete_all()
    else:
        pass




##    -----------  create window ------------

win=tk.Tk()
win.geometry("1520x780")


### --------- give the window title ------------
win.title("Student Management System")


###  ------------ set date and time  on head ------------
dateTimeL=tk.Label(win,text="Hello", font=('arial',25,'bold'),bg="green" )
dateTimeL.place(x=5,y=25)


### -----------------  main heading Student management System -----------------
txt="Students Management System"
heading=tk.Label(win, text=txt, font=("arial", 25,"bold"), border=12, relief=tk.GROOVE, bg="blue", fg="yellow")
# title.place(side=tk.TOP,fill="x")
heading.place(x=400, y=10, width=720)
slider()


## --------- logo image -------------

from PIL import Image,ImageDraw, ImageTk 

# 1. Image.open() का उपयोग करके PNG/JPG इमेज को लोड करें (PIL ऑब्जेक्ट)
pil_img = Image.open(r"C:\Users\HP\OneDrive\Desktop\student management\a.jpg")

resised_img=pil_img.resize((110,90),Image.LANCZOS)

# 2. ImageTk.PhotoImage() का उपयोग करके PIL ऑब्जेक्ट को Tkinter ऑब्जेक्ट में बदलें
img = ImageTk.PhotoImage(resised_img) 

# 3. Tkinter Label में इमेज का उपयोग करें
logo = tk.Label(win, image=img)
logo.place(x=1300, y=0, )




#  detail or form frame
detail_frame=tk.LabelFrame(win,text="Enter Details", font=("Arial",20), bg="lightgray",bd=12)
detail_frame.place(x=20, y=90, width=400,height=600)

##  entry
id_lbl=tk.Label(detail_frame,text="ID. :", font=("areal", 13), bg="lightgray")
id_lbl.grid(row=0, column=0)
id_ent=tk.Entry(detail_frame, bd=2, font=("arial", 13), width=25)
id_ent.grid(row=0, column=1,  padx=2, pady=4)

name=tk.Label(detail_frame,text="Name :", font=("areal", 13), bg="lightgray")
name.grid(row=1, column=0)
name_ent=tk.Entry(detail_frame, bd=2, font=("arial", 13), width=25)
name_ent.grid(row=1, column=1,  padx=2, pady=4)

fname=tk.Label(detail_frame,text="Father's Name :", font=("areal", 13), bg="lightgray")
fname.grid(row=2, column=0)
fname_ent=tk.Entry(detail_frame, bd=2, font=("arial", 13), width=25)
fname_ent.grid(row=2, column=1,  padx=2, pady=4)


dob=tk.Label(detail_frame,text="D.O.B. :", font=("areal", 13), bg="lightgray")
dob.grid(row=3, column=0)
dob_ent=tk.Entry(detail_frame, bd=2, font=("arial", 13), width=25)
dob_ent.grid(row=3, column=1,  padx=2, pady=4)


gender=tk.Label(detail_frame,text="Gender",font=("areal", 13), bg="lightgray")
gender.grid(row=5, column=0)
gender=ttk.Combobox(detail_frame, font=("areal", 13), width=23, state="readonly")   # state read only means we can not write something in this field only can read
gender['values']=("Male","Female","Other")
gender.set("Male")
gender.grid(row=5, column=1)

clas=tk.Label(detail_frame, text="Class",font=("arial", 13), bg="lightgray")
clas.grid(row=6, column=0)
class_opt=ttk.Combobox(detail_frame, font=("areal", 13), width=23, state="readonly")   # state read only means we can not write something in this field only can read
class_opt['values']=("BCA",'BBA', 'B.Tech', 'BSC CS')
class_opt.set("BCA")
class_opt.grid(row=6, column=1,  padx=2, pady=4)



sec=tk.Label(detail_frame,text="Section :", font=("arial", 13), bg="lightgray")
sec.grid(row=7, column=0)
sec_opt=ttk.Combobox(detail_frame,text="Gender", font=("areal", 13), width=23, state="readonly")   # state read only means we can not write something in this field only can read
sec_opt['values']=('A','B', 'C', 'D','E')
sec_opt.set('B')
sec_opt.grid(row=7, column=1,  padx=2, pady=4)

con=tk.Label(detail_frame,text="Contact :", font=("arial", 13), bg="lightgray")
con.grid(row=8, column=0)
con_ent=tk.Entry(detail_frame, bd=2, font=("arial", 13), width=25)
con_ent.grid(row=8, column=1,  padx=2, pady=4)


email=tk.Label(detail_frame,text="Email :", font=("areal", 13), bg="lightgray")
email.grid(row=4, column=0)
email_ent=tk.Entry(detail_frame, bd=2, font=("arial", 13), width=25)
email_ent.grid(row=4, column=1,  padx=2, pady=4)

Address=tk.Label(detail_frame,text="Address. :", font=("areal", 13), bg="lightgray")
Address.grid(row=9, column=0)
add_ent=tk.Text(detail_frame, width=25, height=3, bd=2, font=("arial", 13))
add_ent.grid(row=9, column=1,  padx=2, pady=4)



##  ----------------  button Frame  --------------------
btn_frame=tk.Frame(detail_frame, bg="lightgray", bd=10, relief=(tk.GROOVE))
btn_frame.place(x=20, y=380,width=330, height=150 )

##  --------------- create buttons  ----------------
add_btn=tk.Button(btn_frame,text="Add", bg="lightblue", width=15, bd=2, font=("arial",12), command=add)
add_btn.grid(row=0, column=1, padx=2,pady=10)

delete_btn=tk.Button(btn_frame,text="Delete", bg="lightblue", bd=5,width=15, font=("arial",12), command=delete)
delete_btn.grid(row=0, column=2, padx=2,pady=10)

update_btn=tk.Button(btn_frame,text="Update" , bg="lightblue", bd=5,width=15, font=("arial",12), command=update)
update_btn.grid(row=1, column=1,padx=2, pady=10)

clear_btn=tk.Button(btn_frame,text="New Field", bg="lightblue", bd=5,width=15, font=("arial",12), command=lambda:clear(True))
clear_btn.grid(row=1, column=2,padx=2, pady=10)








#  Database frame  =>  record frame
data_frame=tk.LabelFrame(win, font=("Arial",20), bg="lightgray",bd=2, relief="groove")
data_frame.place(x=450, y=90, width=1050,height=600)

## search

search_box=ttk.Combobox(data_frame, font=("areal", 13), width=15, state="readonly", )   
search_box['values']=("ID","clas","Name", 'Gender','section')
search_box.set("Search By")
search_box.place(x=10, y=5)

search_entry=tk.Entry(data_frame,font=("Arial",15), width=10, bd=1)
search_entry.place(x=170, y=5)

search_btn=tk.Button(data_frame, text="Search",font=("areal", 13), height=1, command=search_record)
search_btn.place(x=360, y=5)


show_all=tk.Button(data_frame, text="Show All",font=("areal", 13), height=1, command=show_all)
show_all.place(x=700, y=5)


delete_all=tk.Button(data_frame, text="Delete All",font=("areal", 13), height=1, command=delete_all)
delete_all.place(x=900, y=5)


 ##   ---------  make scrolbar   -------------
scrollbarY=tk.Scrollbar(data_frame,orient= 'vertical')
scrollbarH=tk.Scrollbar(data_frame,orient="horizontal")



record_frame=tk.Frame(data_frame, relief="groove", bg="red")
record_frame.place(x=10, y=40, width=1000, height=520)

student_table=ttk.Treeview(record_frame,columns=('ID', "Name","Father's Name",'D.O.B','Email','Gender','Class','Section','Contact No.',"Address"),xscrollcommand=scrollbarH.set, yscrollcommand=scrollbarY.set )

### -----------  config scrolbar table headings  -------------
scrollbarH.config(command=student_table.xview)
scrollbarY.config(command=student_table.yview)
scrollbarH.pack(side="bottom", fill="x")
scrollbarY.pack(side="right", fill="y")

####  ----------  pack student Table Headings  To show ------------
student_table.pack( fill="both", expand=1)

student_table.heading('ID',text='ID')
student_table.heading('Name',text='Name')
student_table.heading("Father's Name",text="Father's Name")
student_table.heading('Gender',text='Gender')
student_table.heading('Email',text='Email ')
student_table.heading('D.O.B',text='D.O.B')
student_table.heading('Class',text='Class')
student_table.heading('Section',text='Section')
student_table.heading('Contact No.',text='Contact No.')
student_table.heading('Address',text='Address')

student_table.config(show="headings")


##  --------  style the heading and text  ---------
style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',15,'bold'))
style.configure('Treeview',font=('arial',13))
## create search grame



treeViewData()  ## to show the records already

win.bind("<ButtonRelease>",selection)
win.mainloop()






