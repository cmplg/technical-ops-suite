#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import sys

print("=== Starting Minimal Test ===")

try:
    # Test basic tkinter
    root = tk.Tk()
    root.title("Minimal Test")
    root.geometry("300x150")
    
    label = tk.Label(root, text="Hello! If you see this,\nTkinter is working!")
    label.pack(pady=20)
    
    def on_click():
        print("Button clicked!")
        messagebox.showinfo("Success", "It works!")
    
    btn = tk.Button(root, text="Click Me", command=on_click)
    btn.pack(pady=10)
    
    print("Starting mainloop...")
    root.mainloop()
    print("Mainloop ended")
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
    
    # Try to write error to file
    with open("/tmp/tkinter_error.txt", "w") as f:
        f.write(str(e) + "\n")
        f.write(traceback.format_exc())
