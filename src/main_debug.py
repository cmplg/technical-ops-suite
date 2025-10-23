#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import sys
import os
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        logging.info("Starting Technical Operations Suite...")
        
        root = tk.Tk()
        root.title("Technical Operations Suite - Debug")
        root.geometry("600x500")
        
        # Header
        header = tk.Label(root, text="🚀 Technical Operations Suite (Debug)", font=("Arial", 16, "bold"))
        header.pack(pady=20)
        
        # Status info
        status_text = f"Python: {sys.version}\nPath: {os.getcwd()}"
        status_label = tk.Label(root, text=status_text, font=("Arial", 8), justify=tk.LEFT)
        status_label.pack(pady=10)
        
        # Buttons dengan fungsi yang lebih detail
        def start_operations():
            logging.info("Start Operations button clicked")
            try:
                messagebox.showinfo("Info", "Operations Started Successfully!")
                logging.info("Operations started successfully")
            except Exception as e:
                logging.error(f"Error in start_operations: {e}")
                messagebox.showerror("Error", f"Failed to start operations: {e}")
        
        def system_check():
            logging.info("System Check button clicked")
            try:
                # Simulate some system check
                import platform
                system_info = f"System: {platform.system()}\nVersion: {platform.version()}"
                messagebox.showinfo("System Info", system_info)
            except Exception as e:
                logging.error(f"Error in system_check: {e}")
        
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)
        
        btn1 = tk.Button(btn_frame, text="Start Operations", width=15, height=2, command=start_operations)
        btn1.grid(row=0, column=0, padx=10, pady=5)
        
        btn2 = tk.Button(btn_frame, text="System Check", width=15, height=2, command=system_check)
        btn2.grid(row=0, column=1, padx=10, pady=5)
        
        btn3 = tk.Button(btn_frame, text="Test Error", width=15, height=2,
                        command=lambda: [logging.warning("Test error triggered"), messagebox.showwarning("Test", "This is a test warning")])
        btn3.grid(row=1, column=0, padx=10, pady=5)
        
        btn4 = tk.Button(btn_frame, text="Exit", width=15, height=2, command=root.quit)
        btn4.grid(row=1, column=1, padx=10, pady=5)
        
        logging.info("Tkinter GUI setup completed")
        root.mainloop()
        
    except Exception as e:
        logging.critical(f"Critical error in main: {e}")
        # Fallback: try to show error in messagebox
        try:
            tk.Tk().withdraw()
            messagebox.showerror("Critical Error", f"Application failed to start:\n{e}")
        except:
            print(f"CRITICAL ERROR: {e}")

if __name__ == "__main__":
    main()
    logging.info("Application closed")
