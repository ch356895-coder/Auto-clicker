import tkinter as tk
from tkinter import ttk

class SettingsFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Settings", padding=15)
        
        # Click Interval
        ttk.Label(self, text="Click Interval (seconds):", font=("Arial", 10)).pack(anchor="w", pady=5)
        self.interval_var = tk.DoubleVar(value=0.1)
        interval_spinbox = ttk.Spinbox(self, from_=0.01, to=10, textvariable=self.interval_var, width=20)
        interval_spinbox.pack(fill="x", pady=5)
        ttk.Label(self, text="Time between each click", font=("Arial", 8, "italic")).pack(anchor="w")
        
        # Number of Clicks
        ttk.Label(self, text="Number of Clicks:", font=("Arial", 10)).pack(anchor="w", pady=(15, 5))
        self.clicks_var = tk.IntVar(value=100)
        clicks_spinbox = ttk.Spinbox(self, from_=1, to=100000, textvariable=self.clicks_var, width=20)
        clicks_spinbox.pack(fill="x", pady=5)
        ttk.Label(self, text="Total clicks to perform", font=("Arial", 8, "italic")).pack(anchor="w")
        
        # Mouse Button
        ttk.Label(self, text="Mouse Button:", font=("Arial", 10)).pack(anchor="w", pady=(15, 5))
        self.button_var = tk.StringVar(value="left")
        button_combo = ttk.Combobox(self, textvariable=self.button_var, 
                                     values=["left", "right", "middle"], 
                                     state="readonly", width=20)
        button_combo.pack(fill="x", pady=5)
        ttk.Label(self, text="Which mouse button to click", font=("Arial", 8, "italic")).pack(anchor="w")
        
        # Start Delay
        ttk.Label(self, text="Start Delay (seconds):", font=("Arial", 10)).pack(anchor="w", pady=(15, 5))
        self.delay_var = tk.IntVar(value=3)
        delay_spinbox = ttk.Spinbox(self, from_=0, to=60, textvariable=self.delay_var, width=20)
        delay_spinbox.pack(fill="x", pady=5)
        ttk.Label(self, text="Wait time before starting (allows window switching)", font=("Arial", 8, "italic")).pack(anchor="w")
    
    def get_settings(self):
        """Get current settings."""
        return {
            'interval': self.interval_var.get(),
            'clicks': self.clicks_var.get(),
            'button': self.button_var.get(),
            'delay': self.delay_var.get()
        }


class ButtonsFrame(ttk.Frame):
    def __init__(self, parent, on_start, on_stop):
        super().__init__(parent)
        
        self.start_button = ttk.Button(self, text="▶ Start", command=on_start)
        self.start_button.pack(side="left", padx=5, fill="x", expand=True)
        
        self.stop_button = ttk.Button(self, text="⏹ Stop", command=on_stop, state="disabled")
        self.stop_button.pack(side="left", padx=5, fill="x", expand=True)
    
    def set_running(self, running):
        """Update button states based on running status."""
        if running:
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")
        else:
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")


class StatusFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Status & Information", padding=10)
        
        # Status label
        self.status_label = ttk.Label(self, text="Status: Ready", font=("Arial", 11, "bold"), foreground="blue")
        self.status_label.pack(pady=10)
        
        # Info text
        info_text = tk.Text(self, height=12, width=50, state="disabled", wrap="word")
        info_text.pack(fill="both", expand=True, pady=5)
        
        self.info_text = info_text
        
        # Insert initial info
        info_content = """📋 HOW TO USE:

1. Set Click Interval (time between clicks)
2. Set Number of Clicks
3. Choose Mouse Button (left/right/middle)
4. Set Start Delay (time before clicking starts)
5. Click 'Start' button
6. Switch to your target application
7. Clicking will begin automatically
8. Click 'Stop' to cancel anytime

⚠️  IMPORTANT NOTES:

• Use this tool responsibly
• Only for legitimate automation tasks
• Keep Stop button ready to cancel
• Some apps may block automation
• Run as Administrator if needed

✅ Compatible with most Windows applications"""
        
        info_text.config(state="normal")
        info_text.insert("1.0", info_content)
        info_text.config(state="disabled")
    
    def update_status(self, message, status_type="info"):
        """Update status message."""
        color_map = {
            "info": "blue",
            "success": "green",
            "error": "red",
            "warning": "orange"
        }
        
        color = color_map.get(status_type, "black")
        self.status_label.config(text=message, foreground=color)
