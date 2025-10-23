#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import sys
import os
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TechnicalOpsSuite:
    def __init__(self):
        self.root = None
        self.is_running = False
        
    def check_dependencies(self):
        """Check if all dependencies are available"""
        try:
            import tkinter
            return True
        except ImportError as e:
            logging.error(f"Tkinter not available: {e}")
            return False
    
    def safe_messagebox(self, title, message, type="info"):
        """Safely show messagebox without causing grab errors"""
        try:
            if type == "info":
                messagebox.showinfo(title, message)
            elif type == "error":
                messagebox.showerror(title, message)
            elif type == "warning":
                messagebox.showwarning(title, message)
        except Exception as e:
            logging.error(f"Messagebox error: {e}")
            # Fallback: print to console
            print(f"{title}: {message}")
    
    def start_operations(self, status_label):
        """Start technical operations"""
        try:
            logging.info("Start Operations button clicked")
            if status_label and status_label.winfo_exists():
                status_label.config(text="Status: Running", fg="orange")
            
            self.safe_messagebox("Operations", "Technical operations started successfully!")
            
        except Exception as e:
            logging.error(f"Error in start_operations: {e}")
            self.safe_messagebox("Error", f"Failed to start operations: {e}", "error")
    
    def system_check(self):
        """Perform system check"""
        try:
            logging.info("System Check button clicked")
            import platform
            system_info = f"""System Information:
OS: {platform.system()} {platform.release()}
Architecture: {platform.machine()}
Python: {platform.python_version()}
Working Directory: {os.getcwd()}"""
            
            self.safe_messagebox("System Check", system_info)
            
        except Exception as e:
            logging.error(f"Error in system_check: {e}")
            self.safe_messagebox("Error", f"System check failed: {e}", "error")
    
    def open_logs(self):
        """Open and manage logs"""
        try:
            logging.info("View Logs button clicked")
            # Create logs directory if not exists
            log_dir = "/tmp/technical-ops-suite"
            os.makedirs(log_dir, exist_ok=True)
            
            log_file = os.path.join(log_dir, "operations.log")
            with open(log_file, "a") as f:
                f.write(f"Log entry: Application accessed at {os.times()}\\n")
            
            self.safe_messagebox("Logs", f"Logs saved to: {log_file}")
            
        except Exception as e:
            logging.error(f"Error in open_logs: {e}")
            self.safe_messagebox("Error", f"Failed to access logs: {e}", "error")
    
    def on_closing(self):
        """Handle application closing"""
        logging.info("Application closing...")
        self.is_running = False
        if self.root:
            self.root.quit()
            self.root.destroy()
    
    def create_gui(self):
        """Create the main GUI"""
        try:
            self.root = tk.Tk()
            self.root.title("Technical Operations Suite v1.0")
            self.root.geometry("500x400")
            self.root.resizable(True, True)
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            
            # Header
            header_frame = tk.Frame(self.root)
            header_frame.pack(pady=20, fill=tk.X)
            
            header_label = tk.Label(header_frame, text="�� Technical Operations Suite", 
                                   font=("Arial", 18, "bold"), fg="#2c3e50")
            header_label.pack()
            
            subtitle_label = tk.Label(header_frame, text="Daily Technical Operations Application", 
                                     font=("Arial", 12), fg="#7f8c8d")
            subtitle_label.pack()
            
            # Status
            status_frame = tk.Frame(self.root)
            status_frame.pack(pady=10)
            
            status_label = tk.Label(status_frame, text="Status: Ready", 
                                   font=("Arial", 10, "bold"), fg="green")
            status_label.pack()
            
            # Buttons Frame
            buttons_frame = tk.Frame(self.root)
            buttons_frame.pack(pady=20)
            
            # Use lambda to pass status_label safely
            btn1 = tk.Button(buttons_frame, text="Start Operations", width=15, height=2,
                            command=lambda: self.start_operations(status_label), 
                            bg="#3498db", fg="white", font=("Arial", 10))
            btn1.grid(row=0, column=0, padx=10, pady=5)
            
            btn2 = tk.Button(buttons_frame, text="System Check", width=15, height=2,
                            command=self.system_check, 
                            bg="#2ecc71", fg="white", font=("Arial", 10))
            btn2.grid(row=0, column=1, padx=10, pady=5)
            
            btn3 = tk.Button(buttons_frame, text="View Logs", width=15, height=2,
                            command=self.open_logs, 
                            bg="#e74c3c", fg="white", font=("Arial", 10))
            btn3.grid(row=1, column=0, padx=10, pady=5)
            
            btn4 = tk.Button(buttons_frame, text="Exit", width=15, height=2,
                            command=self.on_closing, 
                            bg="#95a5a6", fg="white", font=("Arial", 10))
            btn4.grid(row=1, column=1, padx=10, pady=5)
            
            # Footer
            footer_label = tk.Label(self.root, text="© 2024 Technical Operations Team - Version 1.0", 
                                   font=("Arial", 8), fg="#bdc3c7")
            footer_label.pack(side=tk.BOTTOM, pady=10)
            
            return True
            
        except Exception as e:
            logging.error(f"Error creating GUI: {e}")
            return False
    
    def run(self):
        """Main application runner"""
        logging.info("Technical Operations Suite - Starting...")
        
        if not self.check_dependencies():
            self.safe_messagebox("Error", "Tkinter not available. Please install python3-tk", "error")
            return
        
        if not self.create_gui():
            self.safe_messagebox("Error", "Failed to create application interface", "error")
            return
        
        try:
            self.is_running = True
            logging.info("GUI setup completed, starting main loop...")
            self.root.mainloop()
            logging.info("Application closed successfully")
            
        except Exception as e:
            logging.error(f"Error in main loop: {e}")
            self.safe_messagebox("Error", f"Application error: {e}", "error")

def main():
    app = TechnicalOpsSuite()
    app.run()

if __name__ == "__main__":
    main()
