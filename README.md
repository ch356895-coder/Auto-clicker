# Auto Clicker Application

A professional, feature-rich auto clicker application built with Python and Tkinter.

## 🎯 Features

- ✅ **Adjustable Click Interval** - Set time between clicks (0.01s - 10s)
- ✅ **Customizable Click Count** - Perform 1 to 100,000 clicks
- ✅ **Multiple Mouse Buttons** - Support for left, right, and middle buttons
- ✅ **Start Delay** - Countdown before clicking (allows window switching)
- ✅ **Real-time Status Updates** - Monitor clicking progress
- ✅ **Stop Button** - Cancel clicking anytime
- ✅ **Professional GUI** - Clean and intuitive interface
- ✅ **Threading Support** - Responsive UI during clicking
- ✅ **Error Handling** - Input validation and error recovery
- ✅ **Cross-platform** - Windows, macOS, Linux support

## 📋 Requirements

- Python 3.6 or higher
- pynput library
- Tkinter (usually comes with Python)

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/ch356895-coder/auto-clicker.git
cd auto-clicker
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Run the application
```bash
python main.py
```

### How to use:

1. **Set Click Interval** - Choose time between clicks (e.g., 0.1 seconds)
2. **Set Number of Clicks** - Enter how many times to click (e.g., 100)
3. **Select Mouse Button** - Choose left, right, or middle button
4. **Set Start Delay** - Set delay before clicking starts (e.g., 3 seconds)
5. **Click Start** - Begin the auto clicking
6. **Switch Window** - Move to your target application during the delay
7. **Clicking Begins** - Automatic clicking will start after the delay
8. **Stop Anytime** - Click the Stop button to cancel

## 📁 Project Structure

```
auto-clicker/
├── main.py                 # Entry point
├── gui/
│   ├── __init__.py
│   ├── main_window.py      # Main GUI window
│   └── widgets.py          # GUI components
├── core/
│   ├── __init__.py
│   └── auto_clicker.py     # Core clicking logic
├── requirements.txt        # Dependencies
├── README.md              # Documentation
└── .gitignore             # Git ignore file
```

## ⚙️ Configuration

### Default Settings
- **Interval**: 0.1 seconds
- **Clicks**: 100
- **Button**: Left
- **Delay**: 3 seconds

All settings can be modified through the GUI.

## 🔍 Troubleshooting

### Problem: Clicks not working
**Solution**: 
- Run the application as Administrator
- Check if the target application blocks automation
- Ensure pynput is installed correctly

### Problem: High CPU usage
**Solution**:
- Increase the click interval
- Reduce the number of clicks
- Check for background processes

### Problem: ImportError for pynput
**Solution**:
```bash
pip install --upgrade pynput
```

### Problem: Application frozen during clicking
**Solution**:
- This is normal behavior - the app will respond after clicking completes
- Click Stop button to cancel immediately

## ⚠️ Important Notes

### Use Responsibly
This tool automates mouse clicks and should only be used for:
- ✅ Personal productivity automation
- ✅ Testing automation
- ✅ Repetitive task automation in your own applications
- ✅ Form filling
- ✅ Game automation (with permission)

### Do NOT use for:
- ❌ Unauthorized system access
- ❌ Gaming exploits or cheating
- ❌ Any illegal or malicious purposes
- ❌ Violating terms of service of any application

## 🔐 Security

- This application only controls your local mouse
- No data is collected or transmitted
- No internet connection required
- All processing is done locally

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📞 Support

If you encounter issues:
1. Check the Troubleshooting section
2. Review the requirements
3. Check GitHub issues
4. Create a new issue with details

## 🚀 Future Features

- [ ] Hotkey support (e.g., F6 to toggle)
- [ ] Click recording and playback
- [ ] Click pattern creation
- [ ] Multiple click sequences
- [ ] GUI theme customization
- [ ] Click statistics
- [ ] Auto-save settings
- [ ] Scheduled clicking

## 📊 Version History

### v1.0 (Current)
- Initial release
- Basic auto clicking functionality
- GUI interface
- Settings configuration

---

**Made with ❤️ for automation enthusiasts**
