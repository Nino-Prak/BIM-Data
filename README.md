# 🚀 Python Multi-Tool Suite

A comprehensive desktop application built with Python and tkinter that combines multiple useful utilities in one beautiful, modern interface.

## ✨ Features

### 🌤️ Weather Information
- Get weather data for any city
- Clean, formatted display with emojis
- Threaded API calls for responsive UI
- Note: Currently shows simulated data (easily extensible with real API)

### 🔒 Secure Password Generator
- Generate cryptographically secure passwords
- Customizable length (4-128 characters)
- Multiple character set options:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special symbols
- Generate multiple passwords at once
- Password strength analysis

### 📊 Text Analysis Tool
- Comprehensive text statistics
- Word frequency analysis
- Readability assessment
- Character, word, sentence, and paragraph counts
- Most common words identification
- Average sentence length calculation

### 📁 File Organizer
- Organize files by extension
- Preview mode (shows what would be organized)
- Directory browser integration
- Detailed organization reports
- Safe preview before actual file operations

### 📱 QR Code Generator
- Generate QR codes from any text or URL
- High-quality image output
- Resizable display
- Copy-friendly format

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup
1. Clone or download this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

## 🎨 UI Design

The application features a modern, dark-themed interface with:
- Clean tabbed navigation
- Responsive layout
- Professional color scheme
- Intuitive controls
- Emoji-enhanced visual elements

## 🔧 Technical Details

### Built With
- **tkinter**: GUI framework (built into Python)
- **PIL/Pillow**: Image processing for QR codes
- **qrcode**: QR code generation
- **requests**: HTTP client for API calls
- **secrets**: Cryptographically secure random generation
- **threading**: Non-blocking operations

### Architecture
- Object-oriented design
- Modular tab system
- Threaded operations for responsiveness
- Error handling and user feedback
- Modern styling with ttk themes

## 🚀 Usage

1. **Launch the application**: Run `python main.py`
2. **Navigate tabs**: Click on any tab to access different tools
3. **Weather**: Enter a city name and click "Get Weather"
4. **Password Generator**: Configure options and click "Generate Password"
5. **Text Analysis**: Paste text and click "Analyze Text"
6. **File Organizer**: Select a directory and preview organization
7. **QR Code**: Enter text/URL and click "Generate QR Code"

## 🔮 Future Enhancements

- Real weather API integration
- File encryption/decryption tools
- Network utilities (ping, port scanner)
- System information display
- Database connectivity tools
- Advanced text processing (sentiment analysis)
- Export capabilities for analysis results
- Custom themes and styling options

## 🤝 Contributing

Feel free to fork this project and add your own tools and features! The modular design makes it easy to add new tabs and functionality.

## 📄 License

This project is open source and available under the MIT License.

## 🎯 Perfect for

- System administrators
- Developers
- Students learning Python GUI development
- Anyone who needs quick access to various utilities
- Demonstrating Python capabilities in Cursor

---

**Enjoy exploring the capabilities of Python with this multi-tool suite! 🐍✨**