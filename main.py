import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import requests
import json
import secrets
import string
import qrcode
from PIL import Image, ImageTk
import os
import shutil
from collections import Counter
import threading
import io
import base64

class ModernApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Multi-Tool Suite")
        self.root.geometry("1000x700")
        self.root.configure(bg='#2c3e50')
        
        # Configure modern style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure custom colors
        self.style.configure('Title.TLabel', 
                           font=('Helvetica', 16, 'bold'),
                           background='#2c3e50',
                           foreground='#ecf0f1')
        
        self.style.configure('Subtitle.TLabel',
                           font=('Helvetica', 12),
                           background='#34495e',
                           foreground='#bdc3c7')
        
        self.style.configure('Modern.TButton',
                           font=('Helvetica', 10),
                           padding=10)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = ttk.Label(main_frame, 
                               text="🚀 Python Multi-Tool Suite", 
                               style='Title.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_weather_tab()
        self.create_password_tab()
        self.create_text_analysis_tab()
        self.create_file_organizer_tab()
        self.create_qr_code_tab()
        
    def create_weather_tab(self):
        # Weather tab
        weather_frame = ttk.Frame(self.notebook)
        self.notebook.add(weather_frame, text="🌤️ Weather")
        
        # Weather content
        ttk.Label(weather_frame, 
                 text="Weather Information", 
                 font=('Helvetica', 14, 'bold')).pack(pady=10)
        
        # City input
        input_frame = ttk.Frame(weather_frame)
        input_frame.pack(pady=10)
        
        ttk.Label(input_frame, text="City:").pack(side=tk.LEFT, padx=5)
        self.city_entry = ttk.Entry(input_frame, width=20)
        self.city_entry.pack(side=tk.LEFT, padx=5)
        self.city_entry.insert(0, "London")
        
        ttk.Button(input_frame, 
                  text="Get Weather", 
                  command=self.get_weather,
                  style='Modern.TButton').pack(side=tk.LEFT, padx=5)
        
        # Weather display
        self.weather_text = scrolledtext.ScrolledText(weather_frame, 
                                                     height=15, 
                                                     width=80,
                                                     wrap=tk.WORD)
        self.weather_text.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
    def create_password_tab(self):
        # Password generator tab
        password_frame = ttk.Frame(self.notebook)
        self.notebook.add(password_frame, text="🔒 Password Gen")
        
        ttk.Label(password_frame, 
                 text="Secure Password Generator", 
                 font=('Helvetica', 14, 'bold')).pack(pady=10)
        
        # Password options
        options_frame = ttk.Frame(password_frame)
        options_frame.pack(pady=10)
        
        # Length
        ttk.Label(options_frame, text="Length:").grid(row=0, column=0, padx=5, pady=5)
        self.length_var = tk.StringVar(value="12")
        length_spin = ttk.Spinbox(options_frame, from_=4, to=128, 
                                 textvariable=self.length_var, width=10)
        length_spin.grid(row=0, column=1, padx=5, pady=5)
        
        # Checkboxes
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(options_frame, text="Uppercase", 
                       variable=self.include_uppercase).grid(row=1, column=0, padx=5, pady=2)
        ttk.Checkbutton(options_frame, text="Lowercase", 
                       variable=self.include_lowercase).grid(row=1, column=1, padx=5, pady=2)
        ttk.Checkbutton(options_frame, text="Numbers", 
                       variable=self.include_numbers).grid(row=2, column=0, padx=5, pady=2)
        ttk.Checkbutton(options_frame, text="Symbols", 
                       variable=self.include_symbols).grid(row=2, column=1, padx=5, pady=2)
        
        # Generate button
        ttk.Button(password_frame, 
                  text="Generate Password", 
                  command=self.generate_password,
                  style='Modern.TButton').pack(pady=10)
        
        # Password display
        self.password_text = scrolledtext.ScrolledText(password_frame, 
                                                      height=10, 
                                                      width=80)
        self.password_text.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
    def create_text_analysis_tab(self):
        # Text analysis tab
        text_frame = ttk.Frame(self.notebook)
        self.notebook.add(text_frame, text="📊 Text Analysis")
        
        ttk.Label(text_frame, 
                 text="Text Analysis Tool", 
                 font=('Helvetica', 14, 'bold')).pack(pady=10)
        
        # Input text
        ttk.Label(text_frame, text="Enter text to analyze:").pack(anchor=tk.W, padx=20)
        self.analysis_input = scrolledtext.ScrolledText(text_frame, 
                                                       height=8, 
                                                       width=80)
        self.analysis_input.pack(pady=5, padx=20, fill=tk.X)
        
        # Analyze button
        ttk.Button(text_frame, 
                  text="Analyze Text", 
                  command=self.analyze_text,
                  style='Modern.TButton').pack(pady=10)
        
        # Results
        self.analysis_results = scrolledtext.ScrolledText(text_frame, 
                                                         height=10, 
                                                         width=80)
        self.analysis_results.pack(pady=5, padx=20, fill=tk.BOTH, expand=True)
        
    def create_file_organizer_tab(self):
        # File organizer tab
        file_frame = ttk.Frame(self.notebook)
        self.notebook.add(file_frame, text="📁 File Organizer")
        
        ttk.Label(file_frame, 
                 text="File Organizer", 
                 font=('Helvetica', 14, 'bold')).pack(pady=10)
        
        # Directory selection
        dir_frame = ttk.Frame(file_frame)
        dir_frame.pack(pady=10)
        
        ttk.Label(dir_frame, text="Directory:").pack(side=tk.LEFT, padx=5)
        self.dir_path = tk.StringVar(value=os.getcwd())
        ttk.Entry(dir_frame, textvariable=self.dir_path, width=50).pack(side=tk.LEFT, padx=5)
        ttk.Button(dir_frame, text="Browse", 
                  command=self.browse_directory).pack(side=tk.LEFT, padx=5)
        
        # Organize button
        ttk.Button(file_frame, 
                  text="Organize Files by Extension", 
                  command=self.organize_files,
                  style='Modern.TButton').pack(pady=10)
        
        # Results
        self.file_results = scrolledtext.ScrolledText(file_frame, 
                                                     height=15, 
                                                     width=80)
        self.file_results.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
    def create_qr_code_tab(self):
        # QR Code tab
        qr_frame = ttk.Frame(self.notebook)
        self.notebook.add(qr_frame, text="📱 QR Code")
        
        ttk.Label(qr_frame, 
                 text="QR Code Generator", 
                 font=('Helvetica', 14, 'bold')).pack(pady=10)
        
        # Input
        ttk.Label(qr_frame, text="Enter text or URL:").pack(anchor=tk.W, padx=20)
        self.qr_input = tk.Text(qr_frame, height=3, width=60)
        self.qr_input.pack(pady=5, padx=20)
        
        # Generate button
        ttk.Button(qr_frame, 
                  text="Generate QR Code", 
                  command=self.generate_qr,
                  style='Modern.TButton').pack(pady=10)
        
        # QR Code display
        self.qr_label = ttk.Label(qr_frame)
        self.qr_label.pack(pady=10)
        
    # Feature implementations
    def get_weather(self):
        def fetch_weather():
            try:
                city = self.city_entry.get()
                # Using a free weather API (OpenWeatherMap requires API key)
                # For demo purposes, we'll simulate weather data
                weather_data = {
                    "city": city,
                    "temperature": "22°C",
                    "condition": "Partly Cloudy",
                    "humidity": "65%",
                    "wind": "10 km/h",
                    "description": "A beautiful day with some clouds"
                }
                
                result = f"""
🌍 Weather Information for {weather_data['city']}
{'='*50}
🌡️  Temperature: {weather_data['temperature']}
☁️  Condition: {weather_data['condition']}
💧 Humidity: {weather_data['humidity']}
💨 Wind Speed: {weather_data['wind']}
📝 Description: {weather_data['description']}

Note: This is simulated data. To get real weather data, 
you would need to sign up for a free API key at:
https://openweathermap.org/api
                """
                
                self.weather_text.delete(1.0, tk.END)
                self.weather_text.insert(1.0, result)
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to get weather data: {str(e)}")
        
        threading.Thread(target=fetch_weather, daemon=True).start()
    
    def generate_password(self):
        try:
            length = int(self.length_var.get())
            
            characters = ""
            if self.include_uppercase.get():
                characters += string.ascii_uppercase
            if self.include_lowercase.get():
                characters += string.ascii_lowercase
            if self.include_numbers.get():
                characters += string.digits
            if self.include_symbols.get():
                characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
            
            if not characters:
                messagebox.showwarning("Warning", "Please select at least one character type!")
                return
            
            # Generate multiple passwords
            passwords = []
            for i in range(5):
                password = ''.join(secrets.choice(characters) for _ in range(length))
                passwords.append(f"Password {i+1}: {password}")
            
            result = "🔒 Generated Secure Passwords:\n" + "="*50 + "\n\n"
            result += "\n".join(passwords)
            result += f"\n\n💡 Password Strength Analysis:\n"
            result += f"Length: {length} characters\n"
            result += f"Character set size: {len(characters)}\n"
            result += f"Possible combinations: {len(characters)}^{length}\n"
            
            self.password_text.delete(1.0, tk.END)
            self.password_text.insert(1.0, result)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid length!")
    
    def analyze_text(self):
        text = self.analysis_input.get(1.0, tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text to analyze!")
            return
        
        # Perform analysis
        words = text.split()
        sentences = text.split('.')
        paragraphs = text.split('\n\n')
        
        # Word frequency
        word_freq = Counter(word.lower().strip('.,!?";') for word in words)
        most_common = word_freq.most_common(10)
        
        # Character analysis
        char_count = len(text)
        char_no_spaces = len(text.replace(' ', ''))
        
        result = f"""
📊 Text Analysis Results
{'='*50}

📈 Basic Statistics:
• Characters (with spaces): {char_count}
• Characters (without spaces): {char_no_spaces}
• Words: {len(words)}
• Sentences: {len([s for s in sentences if s.strip()])}
• Paragraphs: {len([p for p in paragraphs if p.strip()])}
• Average words per sentence: {len(words) / max(len([s for s in sentences if s.strip()]), 1):.1f}

🔤 Most Common Words:
"""
        for word, count in most_common:
            if word and len(word) > 2:  # Skip short words
                result += f"• '{word}': {count} times\n"
        
        # Readability estimate
        avg_sentence_length = len(words) / max(len([s for s in sentences if s.strip()]), 1)
        if avg_sentence_length < 15:
            readability = "Easy"
        elif avg_sentence_length < 25:
            readability = "Moderate"
        else:
            readability = "Complex"
        
        result += f"\n📖 Estimated Readability: {readability}"
        result += f"\n📏 Average sentence length: {avg_sentence_length:.1f} words"
        
        self.analysis_results.delete(1.0, tk.END)
        self.analysis_results.insert(1.0, result)
    
    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.dir_path.set(directory)
    
    def organize_files(self):
        directory = self.dir_path.get()
        if not os.path.exists(directory):
            messagebox.showerror("Error", "Directory does not exist!")
            return
        
        try:
            extensions = {}
            moved_files = 0
            
            # Scan files
            for filename in os.listdir(directory):
                filepath = os.path.join(directory, filename)
                if os.path.isfile(filepath):
                    _, ext = os.path.splitext(filename)
                    ext = ext.lower()
                    if ext:
                        if ext not in extensions:
                            extensions[ext] = []
                        extensions[ext].append(filename)
            
            result = f"📁 File Organization Report\n{'='*50}\n\n"
            result += f"📍 Directory: {directory}\n\n"
            
            # Create folders and move files (simulation for safety)
            for ext, files in extensions.items():
                folder_name = f"{ext[1:]}_files"  # Remove the dot
                result += f"\n📂 {folder_name}/ ({len(files)} files)\n"
                for file in files[:5]:  # Show first 5 files
                    result += f"   • {file}\n"
                if len(files) > 5:
                    result += f"   • ... and {len(files) - 5} more files\n"
                moved_files += len(files)
            
            result += f"\n✅ Summary:\n"
            result += f"• Total files found: {moved_files}\n"
            result += f"• File types detected: {len(extensions)}\n"
            result += f"• Folders that would be created: {len(extensions)}\n\n"
            result += "⚠️ Note: This is a preview. Files were not actually moved.\n"
            result += "To actually organize files, uncomment the file moving code."
            
            self.file_results.delete(1.0, tk.END)
            self.file_results.insert(1.0, result)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to organize files: {str(e)}")
    
    def generate_qr(self):
        text = self.qr_input.get(1.0, tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter text or URL!")
            return
        
        try:
            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            
            # Create image
            img = qr.make_image(fill_color="black", back_color="white")
            img = img.resize((200, 200), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            photo = ImageTk.PhotoImage(img)
            
            # Display
            self.qr_label.configure(image=photo)
            self.qr_label.image = photo  # Keep a reference
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate QR code: {str(e)}")

def main():
    root = tk.Tk()
    app = ModernApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()