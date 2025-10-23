#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import os

def main():
    root = tk.Tk()
    root.title("Technical Operations Suite")
    root.geometry("500x400")
    
    # Header
    header = tk.Label(root, text="🚀 Technical Operations Suite", font=("Arial", 16, "bold"))
    header.pack(pady=20)
    
    # Subtitle
    subtitle = tk.Label(root, text="Daily Technical Operations Application", font=("Arial", 12))
    subtitle.pack(pady=5)
    
    # Status
    status = tk.Label(root, text="Status: Ready", font=("Arial", 10))
    status.pack(pady=10)
    
    # Buttons
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=20)
    
    btn1 = tk.Button(btn_frame, text="Start Operations", width=15, height=2,
                    command=lambda: messagebox.showinfo("Info", "Operations Started!"))
    btn1.grid(row=0, column=0, padx=10, pady=5)
    
    btn2 = tk.Button(btn_frame, text="System Check", width=15, height=2,
                    command=lambda: messagebox.showinfo("System", "System Check Complete!"))
    btn2.grid(row=0, column=1, padx=10, pady=5)
    
    btn3 = tk.Button(btn_frame, text="Reports", width=15, height=2,
                    command=lambda: messagebox.showinfo("Reports", "Generating Reports..."))
    btn3.grid(row=1, column=0, padx=10, pady=5)
    
    btn4 = tk.Button(btn_frame, text="Settings", width=15, height=2,
                    command=lambda: messagebox.showinfo("Settings", "Opening Settings..."))
    btn4.grid(row=1, column=1, padx=10, pady=5)
    
    # Footer
    footer = tk.Label(root, text="© 2024 Technical Operations Team", font=("Arial", 8))
    footer.pack(side=tk.BOTTOM, pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
