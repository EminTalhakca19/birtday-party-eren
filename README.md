# birtday-party-eren
import tkinter as tk
from tkinter import ttk
import threading
import time
import random
import math

class EnhancedLegendBirthday:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.setup_styles()
        self.create_widgets()
        self.animation_running = False
        
    def setup_window(self):
        """Configure main window properties"""
        self.root.title("🔥 LEGEND MODE: EREN ABİ 🔥")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#0a0a0a")
        
        # Center window on screen
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (1000 // 2)
        y = (self.root.winfo_screenheight() // 2) - (700 // 2)
        self.root.geometry(f"1000x700+{x}+{y}")
    
    def setup_styles(self):
        """Define color schemes and styles"""
        self.colors = {
            'backgrounds': ["#0f0f23", "#1a1a2e", "#16213e", "#0f3460", "#533483"],
            'neon_colors': ["#ff006e", "#8338ec", "#3a86ff", "#06ffa5", "#ffbe0b"],
            'text_primary': "#ffffff",
            'text_secondary': "#b8b8b8",
            'button_bg': "#ff006e",
            'button_hover': "#d90058"
        }
        self.current_bg_index = 0
        
    def create_widgets(self):
        """Create and position all UI elements"""
        # Main canvas
        self.canvas = tk.Canvas(
            self.root, 
            width=1000, 
            height=700, 
            highlightthickness=0,
            bg=self.colors['backgrounds'][0]
        )
        self.canvas.pack(fill="both", expand=True)
        
        # Animated title with glow effect
        self.title = tk.Label(
            self.canvas,
            text="🎧 LEGEND BIRTHDAY PARTY 🎧",
            font=("Arial Black", 32, "bold"),
            fg=self.colors['text_primary'],
            bg=self.colors['backgrounds'][0]
        )
        self.title.place(relx=0.5, rely=0.12, anchor="center")
        
        # Subtitle
        self.subtitle = tk.Label(
            self.canvas,
            text="✨ Eren Abi için özel kutlama ✨",
            font=("Arial", 16),
            fg=self.colors['text_secondary'],
            bg=self.colors['backgrounds'][0]
        )
        self.subtitle.place(relx=0.5, rely=0.2, anchor="center")
        
        # Enhanced button with hover effects
        self.button = tk.Button(
            self.canvas,
            text="🚀 KUTLAMAYA BAŞLA 🚀",
            font=("Arial", 18, "bold"),
            bg=self.colors['button_bg'],
            fg="white",
            activebackground=self.colors['button_hover'],
            activeforeground="white",
            relief="flat",
            padx=30,
            pady=15,
            cursor="hand2",
            command=self.start_celebration
        )
        self.button.place(relx=0.5, rely=0.32, anchor="center")
        
        # Message area with better styling
        self.message_frame = tk.Frame(
            self.canvas,
            bg=self.colors['backgrounds'][0],
            relief="flat"
        )
        self.message_frame.place(relx=0.5, rely=0.65, anchor="center")
        
        self.message = tk.Label(
            self.message_frame,
            text="",
            font=("Georgia", 18),
            fg=self.colors['text_primary'],
            bg=self.colors['backgrounds'][0],
            justify="center",
            wraplength=800
        )
        self.message.pack(padx=20, pady=20)
        
        # Progress indicator
        self.progress_var = tk.DoubleVar()
        self.progress = ttk.Progressbar(
            self.canvas,
            variable=self.progress_var,
            maximum=100,
            length=400,
            mode='determinate'
        )
        
    def start_celebration(self):
        """Start the birthday celebration sequence"""
        if self.animation_running:
            return
            
        self.animation_running = True
        self.button.config(state="disabled", text="🎉 KUTLAMA BAŞLADI 🎉")
        
        # Show progress bar
        self.progress.place(relx=0.5, rely=0.45, anchor="center")
        
        # Start all animations
        threading.Thread(target=self.animate_background, daemon=True).start()
        threading.Thread(target=self.create_fireworks, daemon=True).start()
        threading.Thread(target=self.type_birthday_message, daemon=True).start()
        threading.Thread(target=self.pulse_title, daemon=True).start()
        
    def animate_background(self):
        """Smooth background color transitions"""
        while self.animation_running:
            for i in range(len(self.colors['backgrounds'])):
                if not self.animation_running:
                    break
                    
                bg_color = self.colors['backgrounds'][i]
                self.canvas.configure(bg=bg_color)
                self.title.configure(bg=bg_color)
                self.subtitle.configure(bg=bg_color)
                self.message_frame.configure(bg=bg_color)
                self.message.configure(bg=bg_color)
                
                time.sleep(3)
                
    def create_fireworks(self):
        """Enhanced particle system for fireworks"""
        particles = []
        
        for _ in range(150):
            particle = {
                'x': random.randint(50, 950),
                'y': random.randint(-100, 0),
                'vx': random.uniform(-2, 2),
                'vy': random.uniform(2, 6),
                'size': random.randint(2, 8),
                'color': random.choice(self.colors['neon_colors']),
                'life': random.randint(50, 100)
            }
            particles.append(particle)
            
        while self.animation_running:
            self.canvas.delete("particle")
            
            for particle in particles:
                # Update position
                particle['x'] += particle['vx']
                particle['y'] += particle['vy']
                particle['life'] -= 1
                
                # Reset particle if it goes off screen or dies
                if (particle['y'] > 700 or particle['x'] < 0 or 
                    particle['x'] > 1000 or particle['life'] <= 0):
                    particle['x'] = random.randint(50, 950)
                    particle['y'] = random.randint(-100, -10)
                    particle['vx'] = random.uniform(-2, 2)
                    particle['vy'] = random.uniform(2, 6)
                    particle['life'] = random.randint(50, 100)
                    particle['color'] = random.choice(self.colors['neon_colors'])
                
                # Draw particle with glow effect
                self.canvas.create_oval(
                    particle['x'] - particle['size'],
                    particle['y'] - particle['size'],
                    particle['x'] + particle['size'],
                    particle['y'] + particle['size'],
                    fill=particle['color'],
                    outline=particle['color'],
                    width=2,
                    tags="particle"
                )
                
            time.sleep(0.05)
            
    def pulse_title(self):
        """Add pulsing effect to title"""
        sizes = [32, 34, 36, 34, 32, 30, 32]
        colors = self.colors['neon_colors']
        
        while self.animation_running:
            for size in sizes:
                if not self.animation_running:
                    break
                color = random.choice(colors)
                self.title.configure(
                    font=("Arial Black", size, "bold"),
                    fg=color
                )
                time.sleep(0.3)
                
    def type_birthday_message(self):
        """Type birthday message with progress indication"""
        messages = [
            "🖤 DOĞUM GÜNÜN KUTLU OLSUN EREN ABİ 🖤\n\n",
            "Senin gibisi bir daha gelmez bu dünyaya.\n",
            "Karanlık gelse de ışık gibi parlıyorsun.\n", 
            "Hep güçlü, hep sağlam, hep legend modunda.\n\n",
            "Her yaşın sana yakışsın, her günün güzel geçsin.\n",
            "Başarıların hiç bitmesin, mutluluğun hep artsın.\n\n",
            "Mihrimah'tan sonsuz saygı ve sevgilerle 💼🔥\n\n",
            "🎉 İyi ki doğdun EREN ABİ! 🎉"
        ]
        
        displayed_text = ""
        total_chars = sum(len(msg) for msg in messages)
        char_count = 0
        
        for message in messages:
            for char in message:
                displayed_text += char
                char_count += 1
                
                self.message.config(text=displayed_text)
                self.progress_var.set((char_count / total_chars) * 100)
                
                time.sleep(0.06)
                
        # Hide progress bar when done
        self.progress.place_forget()
        
        # Final celebration effect
        self.final_celebration()
        
    def final_celebration(self):
        """Final celebration with special effects"""
        time.sleep(2)
        
        # Flash effect
        for _ in range(5):
            self.canvas.configure(bg="#ffffff")
            time.sleep(0.1)
            self.canvas.configure(bg=self.colors['backgrounds'][0])
            time.sleep(0.1)
            
        # Re-enable button with new text
        self.button.config(
            state="normal", 
            text="🎊 TEBRİKLER EREN ABİ 🎊",
            bg="#06ffa5"
        )

def main():
    """Main application entry point"""
    root = tk.Tk()
    app = EnhancedLegendBirthday(root)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("Application closed by user")

if __name__ == "__main__":
    main()
├── src/
├── tests/
├── docs/
└── README.md
