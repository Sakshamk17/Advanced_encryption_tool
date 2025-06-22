import tkinter as tk
from tkinter import filedialog, messagebox
from encryption_tool import EncryptionTool

class EncryptionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Encryption Tool")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        self.file_path = tk.StringVar()

        tk.Label(root, text="File:").pack(pady=5)
        tk.Entry(root, textvariable=self.file_path, width=50).pack(pady=5)
        tk.Button(root, text="Browse", command=self.browse_file).pack(pady=5)

        tk.Button(root, text="Encrypt", command=self.encrypt_file, width=15, bg="#8BC34A").pack(pady=10)
        tk.Button(root, text="Decrypt", command=self.decrypt_file, width=15, bg="#FF9800").pack(pady=5)

    def browse_file(self):
        file = filedialog.askopenfilename()
        if file:
            self.file_path.set(file)

    def ask_password(self):
        pwd_win = tk.Toplevel(self.root)
        pwd_win.title("Enter Password")
        pwd_win.geometry("300x120")
        pwd_win.resizable(False, False)

        tk.Label(pwd_win, text="Enter Password:").pack(pady=5)
        pwd_entry = tk.Entry(pwd_win, show='*', width=30)
        pwd_entry.pack(pady=5)

        result = {"password": None}

        def submit():
            result["password"] = pwd_entry.get()
            pwd_win.destroy()

        tk.Button(pwd_win, text="Submit", command=submit).pack(pady=5)
        self.root.wait_window(pwd_win)
        return result["password"]

    def encrypt_file(self):
        path = self.file_path.get()
        if not path:
            messagebox.showerror("Error", "Please select a file.")
            return

        password = self.ask_password()
        if not password:
            return

        try:
            tool = EncryptionTool(password)
            output_path = path + ".enc"
            tool.encrypt_file(path, output_path)
            messagebox.showinfo("Success", f"File encrypted:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Encryption Failed", str(e))

    def decrypt_file(self):
        path = self.file_path.get()
        if not path:
            messagebox.showerror("Error", "Please select a file.")
            return

        password = self.ask_password()
        if not password:
            return

        try:
            tool = EncryptionTool(password)
            output_path = path + ".dec"
            tool.decrypt_file(path, output_path)
            messagebox.showinfo("Success", f"File decrypted:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Decryption Failed", str(e))

def launch_gui():
    root = tk.Tk()
    app = EncryptionGUI(root)
    root.mainloop()
