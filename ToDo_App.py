import customtkinter 
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x1000")

root.title("To-Do App")
def ToDo():
    
    texte = "⦿  " + customtkinter.CTkEntry.get(entry1)
    
    todo1 = customtkinter.CTkLabel(master=frame, text= texte, font=("Roboto", 16))
    todo1.pack(pady=5, padx=30, anchor= tkinter.W)

    if texte == "⦿  ":
        todo1.destroy()
        
    entry1.delete(0, "end")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text= "To-Do App", font=("Roboto", 28))
label.pack(pady=20, padx=5)


entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="What do you wanna do? ", width= 350, height= 30)
entry1.pack(pady=12, padx=10, ipadx=2, ipady=2)

button = customtkinter.CTkButton(master=frame, text="Add", command=ToDo)
button.pack(pady=12, padx=10)

label2 = customtkinter.CTkLabel(master=frame, text= "To-Do List", font=("Roboto", 22))
label2.pack(pady=10, padx=30, anchor=tkinter.W)


#textbox = customtkinter.CTkTextbox(master=frame, width=350)
#textbox.pack(pady=12, padx=10)
#checkbox = customtkinter.CTkCheckBox(master=frame, text="Done")
#checkbox.pack(pady=12, padx=10)



root.mainloop()

