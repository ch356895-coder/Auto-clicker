import tkinter as tk
from tkinter import ttk, messagebox
from gui.main_window import AutoClickerApp

def main():
    root = tk.Tk()
    app = AutoClickerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
