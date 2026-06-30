import time
import threading
from pynput.mouse import Mouse, Button

class AutoClicker:
    """
    Main AutoClicker class for performing automated mouse clicks.
    """
    
    def __init__(self, interval=0.1, clicks=100, button="left", start_delay=3, 
                 on_complete=None, on_status=None):
        """
        Initialize the AutoClicker.
        
        Args:
            interval (float): Time between clicks in seconds
            clicks (int): Total number of clicks to perform
            button (str): Mouse button - 'left', 'right', or 'middle'
            start_delay (int): Delay before starting in seconds
            on_complete (callable): Callback when clicking is complete
            on_status (callable): Callback for status updates
        """
        self.interval = interval
        self.clicks = clicks
        self.button = button
        self.start_delay = start_delay
        self.on_complete = on_complete
        self.on_status = on_status
        self.is_running = False
        self.mouse = Mouse()
    
    def get_button(self):
        """Convert button string to pynput Button object."""
        buttons = {
            "left": Button.left,
            "right": Button.right,
            "middle": Button.middle
        }
        return buttons.get(self.button, Button.left)
    
    def run(self):
        """Start the auto clicking process."""
        self.is_running = True
        button = self.get_button()
        
        # Countdown before starting
        if self.start_delay > 0:
            for i in range(self.start_delay, 0, -1):
                if self.on_status:
                    self.on_status(f"Status: Starting in {i} seconds...")
                time.sleep(1)
                if not self.is_running:
                    return
        
        # Perform clicks
        if self.on_status:
            self.on_status(f"Status: Clicking... 0/{self.clicks}")
        
        try:
            for i in range(self.clicks):
                if not self.is_running:
                    break
                
                self.mouse.click(button)
                
                if self.on_status and (i + 1) % max(1, self.clicks // 10) == 0:
                    self.on_status(f"Status: Clicking... {i+1}/{self.clicks}")
                
                if i < self.clicks - 1:
                    time.sleep(self.interval)
        
        except Exception as e:
            if self.on_status:
                self.on_status(f"Status: Error - {str(e)}")
        
        finally:
            self.is_running = False
            
            if self.on_complete:
                self.on_complete()
    
    def stop(self):
        """Stop the auto clicking process."""
        self.is_running = False
