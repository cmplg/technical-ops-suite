#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import sys

print("Application starting...")  # This will show if console is available

try:
    root = tk.Tk()
    root.title("Technical Ops - Simple")
    root.geometry("300x200")
    
    label = tk.Label(root, text="Technical Operations Suite\nSimple Version", font=("Arial", 12))
    label.pack(pady=20)
    
    def show_message():
        messagebox.showinfo("Success", "Application is working!")
    
    btn = tk.Button(root, text="Test", command=show_message)
    btn.pack(pady=10)
    
    root.mainloop()
    
except Exception as e:
    print(f"ERROR: {e}")
    # Write error to file
    with open("/tmp/technical_ops_error.txt", "w") as f:
        f.write(str(e))
