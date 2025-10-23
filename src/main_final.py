#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import sys
import os
import logging
from datetime import datetime

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
    
    def write_log(self, action):
        """Write clean log entries"""
        try:
            log_dir = "/tmp/technical-ops-suite"
            os.makedirs(log_dir, exist_ok=True)
            
            log_file = os.path.join(log_dir, "operations.log")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            with open(log_file, "a") as f:
                f.write(f"[{timestamp}] {action}\\n")
                
            return log_file
            
        except Exception as e:
            logging.error(f"Log writing error: {e}")
            return None
    
    def start_operations(self, status_label):
        """Start technical operations"""
        try:
            logging.info("Start Operations button clicked")
            if status_label and status_label.winfo_exists():
                status_label.config(text="Status: Running", fg="orange")
            
            self.write_log("Operations started")
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
            
            self.write_log("System check performed")
            self.safe_messagebox("System Check", system_info)
            
        except Exception as e:
            logging.error(f"Error in system_check: {e}")
            self.safe_messagebox("Error", f"System check failed: {e}", "error")
    
    def open_logs(self):
        """Open and manage logs"""
        try:
            logging.info("View Logs button clicked")
            log_file = self.write_log("Logs viewed")
            
            if log_file and os.path.exists(log_file):
                with open(log_file, "r") as f:
                    log_contents = f.read()
                
                log_display = f"Log file: {log_file}\\n\\nRecent entries:\\n{log_contents[-500:]}"  # Last 500 chars
                self.safe_messagebox("Application Logs", log_display)
            else:
                self.safe_messagebox("Logs", "No log entries yet.")
            
        except Exception as e:
            logging.error(f"Error in open_logs: {e}")
            self.safe_messagebox("Error", f"Failed to access logs: {e}", "error")
    
    def on_closing(self):
        """Handle application closing"""
        logging.info("Application closing...")
        self.write_log("Application closed")
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
            
            header_label = tk.Label(header_frame, text="🚀 Technical Operations Suite", 
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
            
            # Write initial log
            self.write_log("Application started")
            
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
