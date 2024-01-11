import customtkinter as ctk
import random

#methods
def check_number():
    global selected_num
    input_var = int(input_field.get())
    if input_var == selected_num:
        selected_num = random.randint(1,100)
        hint_var.set("You Guessed It Right!")
        restart.place(relx = 0.5, rely = 0.9, anchor = "center")
        submit.configure(state = "disabled")
        hint.configure(font = ("Helvetica",20,"bold"))

    elif input_var < selected_num + 5 and input_var > selected_num - 5:
        hint_var.set("You Are Quite Close..")
        hint.configure(font = ("Helvetica",20,"bold"))
    elif input_var < selected_num + 10 and input_var > selected_num - 10:
        hint_var.set("You Are Close...")
        hint.configure(font = ("Helvetica",20,"bold"))
    else:
        hint_var.set("Try Again :(..")
        hint.configure(font = ("Helvetica",20,"bold"))

def reset():
   input_field.delete(0, ctk.END)
   submit.configure(state = "normal")
   hint_var.set("(No Hint Yet...Start Guessing To Get Hints)")
   hint.configure(font = ("Helvetica",15,"bold"))
   restart.place_forget()

#choosing random number
selected_num = random.randint(1, 100)

#window setup
window = ctk.CTk()
window.title("Guess The Number")
window.geometry("400x300")
window.resizable(False, False)

#this icon is optional, if u dont want it you can remove this line or comment it out
window.iconbitmap("icon.ico")

#window heading
window_text = ctk.CTkLabel(window, text = '''
Guess The Number From 1-100''', font = ("Helvetica",25, "bold"))
window_text.pack()

#hint
hint_var = ctk.StringVar(value = "(No Hint Yet..Start Guessing To Get Hints)")
hint = ctk.CTkLabel(window, text = "Sample", textvariable = hint_var, 
                    font = ("Helvetica",15,"bold"), text_color = "yellow")
hint.place(relx = 0.5, rely = 0.3, anchor = "center")

#input field
input_field = ctk.CTkEntry(window, justify = "center",
                           placeholder_text = "Enter A Number...")
input_field.place(relx = 0.5, rely = 0.5, anchor = "center")

#binding enter event
window.bind("<KeyPress-Return>", lambda event : check_number())



#submit button
submit = ctk.CTkButton(window, text = "Submit", font = ("Helvetica", 20, "bold"),
                       command = check_number)
submit.place(relx = 0.5, rely = 0.7, anchor = "center")

# #restart button
restart = ctk.CTkButton(window, text = "Restart", font = ("Helvetica", 20, "bold"),
                        command = reset)
restart.place_forget()

if __name__ == "__main__":
   #mainloop
    window.mainloop()