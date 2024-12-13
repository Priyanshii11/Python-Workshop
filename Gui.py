from tkinter import *
root=Tk()
root.title("Welcone to the GFG")
root.geometry('550x200+250+250')
label1 = Label(root,text="USER ID" ,foreground="white",background="black")
label1.grid(row=0, column=0, padx=10, pady=10)
ent=Entry(root,width=30)
ent.grid(row=1, column=0, padx=10, pady=10)
label1.grid()

#
label2 = Label(root,text="PASSWORD" ,foreground="white",background="black")
label2.grid(row=2, column=0, padx=10, pady=10)
ent2=Entry(root,width=30)
ent2.grid(row=3, column=0, padx=10, pady=10)
label2.grid()

def click():
    myLabel=Label(root,text="Thank you")
    myLabel.grid()
button=Button(root,text="sumbit",command=click)
button.grid(row=4, column=0, padx=10, pady=10)


root.mainloop()
