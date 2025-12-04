from tkinter import*



def click(event):
    global scvalue    # it is a variavle that stores the text value from the screen
    text = event.widget.cget("text")  # widget has cget function the reads the value from the btn text
    print(text)

    if text == "=":   ## chech if the value of text is = then calculate the expression
        try:
            value = eval(scvalue.get())
            scvalue.set(str(value))  ## store the evaluated value again in the scvalue variable
        except Exception as e:
            scvalue.set("Error")
    elif text == "AC":
        scvalue.set("")
    elif(text=='Del'):
        scvalue.set(scvalue.get()[:-1])  
    else:
        scvalue.set(scvalue.get() + text)


win = Tk()

# 2. Set the window title
win.title("Student Management System")

# 3. Set the window size (geometry)
win.geometry("1000x1000")

scvalue=StringVar()
scvalue.set("")  # initialise with empty string

calculator_frame=LabelFrame(win, font=("Arial",20), bg="#353837",bd=2, fg='black')
calculator_frame.place(x=200, y=50, width=650,height=750)

## make two frames => Display,
entry=Entry(calculator_frame, textvariable=scvalue, font=("Arial",30), bg="#20D0A7",bd=2, fg='black')
entry.place(x=20, y=5, width=600,height=100)



## A BUTTON FRAME INSIDE THE calculator FRAME
btn_frame=LabelFrame(calculator_frame,font=("Arial",20), bg="black",bd=2, fg='black')
btn_frame.place(x=20, y=120, width=600,height=600)


b=Button(btn_frame, text="1", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=50, y=10, width=100, height=100)
b.bind("<Button-1>",click)

b=Button(btn_frame, text="2", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=180, y=10, width=100, height=100)
b.bind("<Button-1>",click)

b=Button(btn_frame, text="3", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=320, y=10, width=100, height=100)
b.bind("<Button-1>",click)

b=Button(btn_frame, text="+", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=450, y=10, width=100, height=100)
b.bind("<Button-1>",click)



b=Button(btn_frame, text="4", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=50, y=130, width=100, height=100)
b.bind("<Button-1>",click)

b=Button(btn_frame, text="5", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=180, y=130, width=100, height=100)
b.bind("<Button-1>",click)

b=Button(btn_frame, text="6", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=320, y=130, width=100, height=100)
b.bind("<Button-1>",click)

b=Button(btn_frame, text="-", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=450, y=130, width=100, height=100)
b.bind("<Button-1>",click)



b=Button(btn_frame, text="7", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=50, y=250, width=100, height=100)
b.bind("<Button-1>",click)

b=Button(btn_frame, text="8", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=180, y=250, width=100, height=100)
b.bind("<Button-1>",click)

b=Button(btn_frame, text="9", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=320, y=250, width=100, height=100)
b.bind("<Button-1>",click)


b=Button(btn_frame, text="*", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=450, y=250, width=100, height=100)
b.bind("<Button-1>",click)

b=Button(btn_frame, text=".", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=50, y=370, width=100, height=100)
b.bind("<Button-1>",click)


b=Button(btn_frame, text="%", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=180, y=370, width=100, height=100)
b.bind("<Button-1>",click)

b=Button(btn_frame, text="0", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=320, y=370, width=100, height=100)
b.bind("<Button-1>",click)

b=Button(btn_frame, text="/", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=450, y=370, width=100, height=100)
b.bind("<Button-1>",click)

b=Button(btn_frame, text="AC", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=50, y=490, width=100, height=100)
b.bind("<Button-1>",click)


b=Button(btn_frame, text="Del", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=180, y=490, width=100, height=100)
b.bind("<Button-1>",click)

b=Button(btn_frame, text="**", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=320, y=490, width=100, height=100)
b.bind("<Button-1>",click)

b=Button(btn_frame, text="=", bd=12, bg="lightblue", font=('areal',30, 'bold'), padx=5, pady=5)
b.place(x=450, y=490, width=100, height=100)
b.bind("<Button-1>",click)





entry.mainloop()


