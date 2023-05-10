import tkinter as tk
bharti = tk.Tk()
bharti.title('Calculater By Bharti')
bharti.geometry("570x600+100+200")
bharti.resizable(False,False)
bharti.configure(bg="#17161b")
equation=""
def show(value):
    global equation
    equation+=value
    bharti_label.config(text=equation)
def clear():
    global equation
    equation=""
    bharti_label.config(text=equation) 
def calculate():
    global equation
    ans=""
    if equation !="":
        try:
            ans= eval(equation)
        except:
            ans="error"
            equation=""
    bharti_label.config(text=ans)                  
bharti_label= tk.Label(bharti,width=25,height=2,text="",font=("arial",30))
bharti_label.pack()
tk.Button(bharti,text="clear",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=10,y=100)
tk.Button(bharti,text="(",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show("(")).place(x=150,y=100)
tk.Button(bharti,text=")",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show(")")).place(x=290,y=100)
tk.Button(bharti,text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show("%")).place(x=430,y=100)

tk.Button(bharti,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show("7")).place(x=10,y=200)
tk.Button(bharti,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show("8")).place(x=150,y=200)
tk.Button(bharti,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show("9")).place(x=290,y=200)
tk.Button(bharti,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show("/")).place(x=430,y=200)

tk.Button(bharti,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show("4")).place(x=10,y=300)
tk.Button(bharti,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show("5")).place(x=150,y=300)
tk.Button(bharti,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show("6")).place(x=290,y=300)
tk.Button(bharti,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show("*")).place(x=430,y=300)

tk.Button(bharti,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show("1")).place(x=10,y=400)
tk.Button(bharti,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show("2")).place(x=150,y=400)
tk.Button(bharti,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show("3")).place(x=290,y=400)
tk.Button(bharti,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show("-")).place(x=430,y=400)

tk.Button(bharti,text="0",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show("0")).place(x=10,y=500)
tk.Button(bharti,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show(".")).place(x=150,y=500)
tk.Button(bharti,text="=",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:calculate()).place(x=290,y=500)
tk.Button(bharti,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#17161b",command=lambda:show("+")).place(x=430,y=500)

bharti.mainloop()


