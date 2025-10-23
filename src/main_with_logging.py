#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import sys
import os
import traceback

# Setup file logging
def setup_logging():
    log_dir = "/tmp/technical-ops-suite"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "app.log")
    
    with open(log_file, "a") as f:
        f.write(f"\n=== Application Started ===\n")
        f.write(f"Python: {sys.version}\n")
        f.write(f"Working Dir: {os.getcwd()}\n")
    
    return log_file

def main():
    log_file = setup_logging()
    
    def write_log(message):
        with open(log_file, "a") as f:
            f.write(f"{message}\n")
    
    try:
        write_log("Initializing Tkinter...")
        root = tk.Tk()
        root.title("Technical Operations Suite")
        root.geometry("500x400")
        
        write_log("Creating GUI elements...")
        
        header = tk.Label(root, text="Technical Operations Suite", font=("Arial", 16, "bold"))
        header.pack(pady=20)
        
        subtitle = tk.Label(root, text="With File Logging", font=("Arial", 12))
        subtitle.pack(pady=5)
        
        log_info = tk.Label(root, text=f"Log file: {log_file}", font=("Arial", 8))
        log_info.pack(pady=5)
        
        def start_operations():
            write_log("Start Operations button clicked")
            try:
                messagebox.showinfo("Info", "Operations Started! Check log file for details.")
                write_log("Operations started successfully")
            except Exception as e:
                write_log(f"ERROR in start_operations: {e}")
                messagebox.showerror("Error", f"Operation failed: {e}")
        
        btn = tk.Button(root, text="Start Operations", width=15, height=2, command=start_operations)
        btn.pack(pady=20)
        
        write_log("Starting main loop...")
        root.mainloop()
        write_log("Main loop ended")
        
    except Exception as e:
        error_msg = f"CRITICAL ERROR: {e}\n{traceback.format_exc()}"
        write_log(error_msg)
        # Try to show error dialog
        try:
            tk.Tk().withdraw()
            messagebox.showerror("Critical Error", f"App failed to start. Check log: {log_file}")
        except:
            pass

if __name__ == "__main__":
    main()
