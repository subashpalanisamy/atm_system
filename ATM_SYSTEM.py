import tkinter as tk
from tkinter import messagebox, simpledialog, Label, Entry, Button

class ATM(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ATM SYSTEM")
        self.geometry("400x300")


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPasswordPage, OptionsPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPasswordPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class LoginPasswordPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="lightblue")

        self.controller = controller
        Label(self, text="ATM Authentication", font=("Arial", 16),bg="lightblue").pack(pady=20)
        
        Label(self, text="Account Number:",bg="lightblue").pack(pady=5)
        self.account_entry = Entry(self)
        self.account_entry.pack(pady=5)

        Label(self, text="Password:",bg="lightblue").pack(pady=5)
        self.password_entry = Entry(self, show="*")
        self.password_entry.pack(pady=5)

        Button(self, text="Login", command=self.login_attempt,bg="lightgreen").pack(pady=20)

    def login_attempt(self):
        acnt_num = 12345
        passw = 1234

        account_number = int(self.account_entry.get())
        password = int(self.password_entry.get())

        if account_number == acnt_num and password == passw:
            self.controller.show_frame(OptionsPage)
        else:
            messagebox.showerror("Error", "Incorrect account number or password!")
            self.controller.destroy()

class OptionsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="lightblue")
        self.controller = controller

        self.bal = 30000

        self.label = tk.Label(self, text="ATM Options", font=("Arial", 16),bg="lightblue")
        self.label.pack(pady=20)

        self.check_bal_btn = tk.Button(self, text="Check Balance", command=self.check_balance,bg="lightblue")
        self.check_bal_btn.pack(pady=10)

        self.withdraw_btn = tk.Button(self, text="Withdrawal", command=self.withdraw,bg="lightblue")
        self.withdraw_btn.pack(pady=10)

        self.deposit_btn = tk.Button(self, text="Deposit", command=self.deposit,bg="lightblue")
        self.deposit_btn.pack(pady=10)

        self.deposit_btn = tk.Button(self, text="Log Out", command=self.exit,bg="lightblue")
        self.deposit_btn.pack(pady=10)
    
    #def custom_messagebox(self, title, message, bg_color="white", fg_color="black"):
     #   msgbox = tk.Toplevel(self.controller)
      #  msgbox.title(title)

       # msgbox.config(bg=bg_color)
        #label = tk.Label(msgbox, text=message, bg=bg_color, fg=fg_color)
       # label.pack(pady=20, padx=20)

       # button = tk.Button(msgbox, text="OK", command=msgbox.destroy)
        #button.pack(pady=20)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your balance is: ${self.bal}")
        #self.custom_messagebox("Balance", f"Your balance is: ${self.bal}", bg_color="lightgreen", fg_color="white")

    def withdraw(self):
        try:
            amount = float(simpledialog.askfloat("Withdraw", "Enter the amount to withdraw:"))
            if amount > self.bal:
                messagebox.showerror("Error", f"Insufficient funds. Your balance is: ${self.bal}")
            else:
                self.bal =self.bal- amount
                messagebox.showinfo("Success", f"You withdrew: ${amount}\n Now Your Current Balance is {self.bal}")
        except ValueError:
            messagebox.showerror("Error", "Invalid Input")
        

    def deposit(self):
        try:
            dep_amount = float(simpledialog.askfloat("Deposit", "Enter the amount to deposit:"))
            self.bal =self.bal+ dep_amount
            messagebox.showinfo("Success", f"You deposited: ${dep_amount}\n Now Your Current Balance is {self.bal}")
        except ValueError:
            messagebox.showerror("Error", "Invalid Input")
       

    def exit(self):
        self.controller.destroy()

    

app = ATM()
app.mainloop()
