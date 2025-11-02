import tkinter as tk
from tkinter import ttk, font
from googletrans import Translator

# GNOME Adwaita Dark color palette
COLORS = {
    'bg_primary': '#242424',
    'bg_secondary': '#303030',
    'bg_tertiary': '#383838',
    'fg_primary': '#ffffff',
    'fg_secondary': '#deddda',
    'accent': '#3584e4',
    'accent_hover': '#1c71d8',
    'border': '#1b1b1b',
    'text_bg': '#1e1e1e',
}


class RoundedButton(tk.Canvas):
    """Custom rounded button widget."""
    
    def __init__(self, parent, text, command, **kwargs):
        self.command = command
        self.bg_color = kwargs.get('bg', COLORS['accent'])
        self.hover_color = kwargs.get('activebackground', COLORS['accent_hover'])
        self.fg_color = kwargs.get('fg', COLORS['fg_primary'])
        self.font = kwargs.get('font', font.Font(family="DejaVu Sans Mono", size=13, weight="bold"))
        self.text = text
        
        tk.Canvas.__init__(self, parent, bg=COLORS['bg_primary'], 
                          highlightthickness=0, height=55, width=200)
        
        self.is_hovered = False
        self.create_button()
        self.bind('<Button-1>', lambda e: self.command())
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        
    def create_button(self):
        """Draw rounded rectangle button."""
        self.delete('all')
        color = self.hover_color if self.is_hovered else self.bg_color
        
        # Create rounded rectangle
        radius = 12
        x1, y1, x2, y2 = 10, 10, 190, 45
        
        self.create_arc(x1, y1, x1+2*radius, y1+2*radius, start=90, extent=90, 
                       fill=color, outline=color)
        self.create_arc(x2-2*radius, y1, x2, y1+2*radius, start=0, extent=90, 
                       fill=color, outline=color)
        self.create_arc(x1, y2-2*radius, x1+2*radius, y2, start=180, extent=90, 
                       fill=color, outline=color)
        self.create_arc(x2-2*radius, y2-2*radius, x2, y2, start=270, extent=90, 
                       fill=color, outline=color)
        self.create_rectangle(x1+radius, y1, x2-radius, y2, fill=color, outline=color)
        self.create_rectangle(x1, y1+radius, x2, y2-radius, fill=color, outline=color)
        
        # Add text
        self.create_text(100, 27.5, text=self.text, fill=self.fg_color, 
                        font=self.font, anchor='center')
        
    def on_enter(self, event):
        """Handle hover state."""
        self.is_hovered = True
        self.create_button()
        self.config(cursor='hand2')
        
    def on_leave(self, event):
        """Handle normal state."""
        self.is_hovered = False
        self.create_button()
        self.config(cursor='')


class RoundedFrame(tk.Canvas):
    """Frame with rounded corners."""
    
    def __init__(self, parent, **kwargs):
        self.bg_color = kwargs.pop('bg', COLORS['text_bg'])
        self.border_color = kwargs.pop('border', COLORS['border'])
        self.radius = kwargs.pop('radius', 12)
        
        tk.Canvas.__init__(self, parent, bg=COLORS['bg_primary'], 
                          highlightthickness=0, **kwargs)
        self.bind('<Configure>', self.draw_rounded_rect)
        
    def draw_rounded_rect(self, event=None):
        """Draw rounded rectangle background."""
        self.delete('all')
        w, h = self.winfo_width(), self.winfo_height()
        r = self.radius
        
        # Draw rounded rectangle
        self.create_arc(0, 0, 2*r, 2*r, start=90, extent=90, 
                       fill=self.bg_color, outline=self.border_color)
        self.create_arc(w-2*r, 0, w, 2*r, start=0, extent=90, 
                       fill=self.bg_color, outline=self.border_color)
        self.create_arc(0, h-2*r, 2*r, h, start=180, extent=90, 
                       fill=self.bg_color, outline=self.border_color)
        self.create_arc(w-2*r, h-2*r, w, h, start=270, extent=90, 
                       fill=self.bg_color, outline=self.border_color)
        self.create_rectangle(r, 0, w-r, h, fill=self.bg_color, outline=self.border_color)
        self.create_rectangle(0, r, w, h-r, fill=self.bg_color, outline=self.border_color)


class TranslatorApp:
    """Modern dark GNOME-styled translation application."""
    
    def __init__(self, root):
        self.root = root
        self.translator = Translator()
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        """Configure main window properties."""
        self.root.title("Translator")
        self.root.geometry("700x800")
        self.root.configure(bg=COLORS['bg_primary'])
        self.root.resizable(True, True)
        
        # Set minimum window size
        self.root.minsize(600, 700)
        
    def create_widgets(self):
        """Create and layout all UI components."""
        # Main container with padding
        main_frame = tk.Frame(self.root, bg=COLORS['bg_primary'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)
        
        # Header
        self._create_header(main_frame)
        
        # Input section
        self._create_input_section(main_frame)
        
        # Language selector
        self._create_language_selector(main_frame)
        
        # Translate button
        self._create_translate_button(main_frame)
        
        # Output section
        self._create_output_section(main_frame)
        
    def _create_header(self, parent):
        """Create application header."""
        header_frame = tk.Frame(parent, bg=COLORS['bg_primary'])
        header_frame.pack(fill=tk.X, pady=(0, 25))
        
        title_font = font.Font(family="DejaVu Sans Mono", size=24, weight="bold")
        title_label = tk.Label(
            header_frame,
            text="Text Translator",
            font=title_font,
            bg=COLORS['bg_primary'],
            fg=COLORS['fg_primary']
        )
        title_label.pack(anchor=tk.W)
        
    def _create_input_section(self, parent):
        """Create input text area with label."""
        input_frame = tk.Frame(parent, bg=COLORS['bg_primary'])
        input_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Label
        label_font = font.Font(family="DejaVu Sans Mono", size=14, weight="bold")
        input_label = tk.Label(
            input_frame,
            text="Enter text to translate:",
            font=label_font,
            bg=COLORS['bg_primary'],
            fg=COLORS['fg_secondary']
        )
        input_label.pack(anchor=tk.W, pady=(0, 12))
        
        # Rounded container for text widget
        text_container = RoundedFrame(input_frame, height=200, radius=12)
        text_container.pack(fill=tk.BOTH, expand=True)
        
        # Text widget with custom styling
        text_font = font.Font(family="DejaVu Sans Mono", size=16, weight="bold")
        self.input_text = tk.Text(
            text_container,
            font=text_font,
            bg=COLORS['text_bg'],
            fg='#00ff88',  # Vibrant cyan-green
            insertbackground=COLORS['accent'],
            relief=tk.FLAT,
            padx=15,
            pady=15,
            wrap=tk.WORD,
            borderwidth=0,
            highlightthickness=0
        )
        text_container.create_window(0, 0, anchor='nw', window=self.input_text, 
                                     width=text_container.winfo_reqwidth(), 
                                     height=text_container.winfo_reqheight())
        text_container.bind('<Configure>', lambda e: text_container.itemconfig(
            text_container.find_all()[0], width=e.width-4, height=e.height-4))
        self.input_text.place(x=2, y=2, relwidth=1, relheight=1, width=-4, height=-4)
        
    def _create_language_selector(self, parent):
        """Create language selection dropdown."""
        lang_frame = tk.Frame(parent, bg=COLORS['bg_primary'])
        lang_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Label
        label_font = font.Font(family="DejaVu Sans Mono", size=14, weight="bold")
        lang_label = tk.Label(
            lang_frame,
            text="Target language:",
            font=label_font,
            bg=COLORS['bg_primary'],
            fg=COLORS['fg_secondary']
        )
        lang_label.pack(side=tk.LEFT, padx=(0, 15))
        
        # Language options with full names
        languages = {
            'Spanish': 'es',
            'French': 'fr',
            'German': 'de',
            'Italian': 'it',
            'Russian': 'ru',
            'Portuguese': 'pt',
            'Japanese': 'ja',
            'Chinese': 'zh-cn',
            'Arabic': 'ar',
            'Hindi': 'hi'
        }
        
        self.target_lang_var = tk.StringVar(value='es')
        
        # Style the OptionMenu with rounded appearance
        dropdown_font = font.Font(family="DejaVu Sans Mono", size=12, weight="bold")
        self.lang_dropdown = tk.OptionMenu(
            lang_frame,
            self.target_lang_var,
            *languages.values()
        )
        self.lang_dropdown.config(
            bg=COLORS['bg_tertiary'],
            fg=COLORS['fg_primary'],
            activebackground=COLORS['accent'],
            activeforeground=COLORS['fg_primary'],
            font=dropdown_font,
            relief=tk.FLAT,
            highlightthickness=0,
            padx=20,
            pady=12,
            borderwidth=2
        )
        
        # Style the dropdown menu
        menu = self.lang_dropdown['menu']
        menu.config(
            bg=COLORS['bg_tertiary'],
            fg=COLORS['fg_primary'],
            activebackground=COLORS['accent'],
            activeforeground=COLORS['fg_primary'],
            font=dropdown_font,
            relief=tk.FLAT
        )
        
        self.lang_dropdown.pack(side=tk.LEFT)
        
    def _create_translate_button(self, parent):
        """Create styled translate button."""
        button_frame = tk.Frame(parent, bg=COLORS['bg_primary'])
        button_frame.pack(pady=(0, 20))
        
        self.translate_button = RoundedButton(
            button_frame,
            text="Translate",
            command=self.translate,
            bg=COLORS['accent'],
            activebackground=COLORS['accent_hover'],
            fg=COLORS['fg_primary']
        )
        self.translate_button.pack()
        
    def _create_output_section(self, parent):
        """Create output text area with label."""
        output_frame = tk.Frame(parent, bg=COLORS['bg_primary'])
        output_frame.pack(fill=tk.BOTH, expand=True)
        
        # Label
        label_font = font.Font(family="DejaVu Sans Mono", size=14, weight="bold")
        output_label = tk.Label(
            output_frame,
            text="Translation:",
            font=label_font,
            bg=COLORS['bg_primary'],
            fg=COLORS['fg_secondary']
        )
        output_label.pack(anchor=tk.W, pady=(0, 12))
        
        # Rounded container for text widget
        text_container = RoundedFrame(output_frame, height=200, radius=12)
        text_container.pack(fill=tk.BOTH, expand=True)
        
        # Text widget with custom styling
        text_font = font.Font(family="DejaVu Sans Mono", size=16, weight="bold")
        self.output_text = tk.Text(
            text_container,
            font=text_font,
            bg=COLORS['text_bg'],
            fg='#64d2ff',  # Vibrant sky blue
            relief=tk.FLAT,
            padx=15,
            pady=15,
            wrap=tk.WORD,
            state=tk.DISABLED,
            borderwidth=0,
            highlightthickness=0
        )
        text_container.create_window(0, 0, anchor='nw', window=self.output_text,
                                     width=text_container.winfo_reqwidth(),
                                     height=text_container.winfo_reqheight())
        text_container.bind('<Configure>', lambda e: text_container.itemconfig(
            text_container.find_all()[0], width=e.width-4, height=e.height-4))
        self.output_text.place(x=2, y=2, relwidth=1, relheight=1, width=-4, height=-4)
        
    def translate(self):
        """Perform translation and display result."""
        text = self.input_text.get("1.0", tk.END).strip()
        target_lang = self.target_lang_var.get()
        
        if not text:
            return
            
        try:
            # Perform translation
            translated = self.translator.translate(text, dest=target_lang)
            
            # Update output
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated.text)
            self.output_text.config(state=tk.DISABLED)
            
        except Exception as e:
            # Handle errors gracefully
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Error: {str(e)}")
            self.output_text.config(state=tk.DISABLED)


def main():
    """Application entry point."""
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()