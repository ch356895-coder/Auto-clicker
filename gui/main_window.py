import tkinter as tk
from tkinter import ttk, messagebox
from core.auto_clicker import AutoClicker
from gui.widgets import SettingsFrame, StatusFrame, ButtonsFrame
import threading

class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Clicker Application")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        
        self.auto_clicker = None
        self.is_running = False
        self.click_thread = None
        
        self.setup_ui()
        self.setup_style()
    
    def setup_style(self):
        """Configure the application style."""
        style = ttk.Style()
        style.theme_use('clam')
    
    def setup_ui(self):
        """Setup the user interface."""
        # Header
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill="x", padx=10, pady=10)
        
        title_label = ttk.Label(header_frame, text="🖱️ Auto Clicker", font=("Arial", 18, "bold"))
        title_label.pack()
        
        version_label = ttk.Label(header_frame, text="v1.0", font=("Arial", 8))
        version_label.pack()
        
        # Main content
        content_frame = ttk.Frame(self.root)
        content_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Settings Frame
        self.settings_frame = SettingsFrame(content_frame)
        self.settings_frame.pack(fill="x", pady=10)
        
        # Buttons Frame
        self.buttons_frame = ButtonsFrame(content_frame, self.start_clicking, self.stop_clicking)
        self.buttons_frame.pack(fill="x", pady=10)
        
        # Status Frame
        self.status_frame = StatusFrame(content_frame)
        self.status_frame.pack(fill="both", expand=True, pady=10)
    
    def start_clicking(self):
        """Start the auto clicking process."""
        if self.is_running:
            messagebox.showwarning("Warning", "Clicking is already in progress!")
            return
        
        # Get settings
        settings = self.settings_frame.get_settings()
        
        # Validate settings
        if not self.validate_settings(settings):
            return
        
        self.is_running = True
        self.buttons_frame.set_running(True)
        
        self.auto_clicker = AutoClicker(
            interval=settings['interval'],
            clicks=settings['clicks'],
            button=settings['button'],
            start_delay=settings['delay'],
            on_complete=self.on_complete,
            on_status=self.update_status
        )
        
        self.click_thread = threading.Thread(target=self.auto_clicker.run, daemon=True)
        self.click_thread.start()
    
    def stop_clicking(self):
        """Stop the auto clicking process."""
        if self.auto_clicker:
            self.auto_clicker.stop()
            self.is_running = False
            self.buttons_frame.set_running(False)
            self.status_frame.update_status("Status: Stopped", "error")
    
    def update_status(self, message):
        """Update status display."""
        self.status_frame.update_status(message, "info")
        self.root.update()
    
    def on_complete(self):
        """Called when clicking is complete."""
        self.is_running = False
        self.buttons_frame.set_running(False)
        self.status_frame.update_status("Status: Completed!", "success")
        messagebox.showinfo("Success", "Auto clicking completed successfully!")
    
    def validate_settings(self, settings):
        """Validate user settings."""
        if settings['interval'] <= 0:
            messagebox.showerror("Error", "Click interval must be greater than 0")
            return False
        
        if settings['clicks'] <= 0:
            messagebox.showerror("Error", "Number of clicks must be greater than 0")
            return False
        
        if settings['delay'] < 0:
            messagebox.showerror("Error", "Start delay cannot be negative")
            return False
        
        return True
