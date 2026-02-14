import tkinter as tk
from tkinter import messagebox
import secrets
import pyperclip

# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x450")
root.resizable(False, False)
root.configure(bg="#1e1e2f")

#  Character Sets
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_+-=?"

#  Functions
def generate_password():
    try:
        length = int(length_var.get())
        if length < 4:
            messagebox.showwarning("Warning", "Minimum length is 4")
            return
    except:
        messagebox.showerror("Error", "Enter valid length")
        return

    chars = ""
    if lower_var.get(): chars += lower
    if upper_var.get(): chars += upper
    if digit_var.get(): chars += digits
    if symbol_var.get(): chars += symbols

    if not chars:
        messagebox.showwarning("Warning", "Select at least one option")
        return

    password = ''.join(secrets.choice(chars) for _ in range(length))
    password_var.set(password)
    update_strength(password)
    copy_btn.config(state="normal")

def update_strength(pwd):
    score = 0
    if len(pwd) >= 8: score += 1
    if any(c.islower() for c in pwd): score += 1
    if any(c.isupper() for c in pwd): score += 1
    if any(c.isdigit() for c in pwd): score += 1
    if any(not c.isalnum() for c in pwd): score += 1

    levels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    colors = ["#ff4d4d", "#ff944d", "#ffd11a", "#66ff66", "#00ffcc"]

    strength_label.config(text=levels[min(score,4)], fg=colors[min(score,4)])

def copy_password():
    pyperclip.copy(password_var.get())
    messagebox.showinfo("Copied", "Password copied!")

#  Title
tk.Label(root, text="🔐 Password Generator",
         font=("Segoe UI", 18, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=15)

#  Length
tk.Label(root, text="Password Length",
         bg="#1e1e2f", fg="white").pack()

length_var = tk.StringVar(value="12")
tk.Entry(root, textvariable=length_var,
         font=("Segoe UI", 12),
         justify="center",
         bg="#2b2b3c", fg="white",
         insertbackground="white").pack(pady=5)

#  Options
lower_var = tk.BooleanVar(value=True)
upper_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

options_frame = tk.Frame(root, bg="#1e1e2f")
options_frame.pack(pady=10)

for text, var in [
    ("Lowercase", lower_var),
    ("Uppercase", upper_var),
    ("Numbers", digit_var),
    ("Symbols", symbol_var)
]:
    tk.Checkbutton(options_frame, text=text, variable=var,
                   bg="#1e1e2f", fg="white",
                   selectcolor="#2b2b3c").pack(anchor="w")

#  Password Display
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var,
         font=("Consolas", 14, "bold"),
         justify="center",
         state="readonly",
         readonlybackground="#12121c",
         fg="#00ffcc").pack(pady=15, fill="x", padx=40)

strength_label = tk.Label(root, text="Strength",
                          bg="#1e1e2f", font=("Segoe UI", 10, "bold"))
strength_label.pack()

#  Buttons
tk.Button(root, text="Generate",
          command=generate_password,
          bg="#00c853", fg="white",
          font=("Segoe UI", 12, "bold"),
          width=15).pack(pady=10)

copy_btn = tk.Button(root, text="Copy",
                     command=copy_password,
                     bg="#2962ff", fg="white",
                     font=("Segoe UI", 12, "bold"),
                     width=15, state="disabled")
copy_btn.pack()

root.mainloop()