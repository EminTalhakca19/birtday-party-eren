"""
Python Tkinter ile sevgiliye teklif uygulaması!
Arama motoruna 'uygula sevgiliye teklif python' yazınca bulabilirsiniz.
Daha yüksek çözünürlük desteği ile ekran boyutunu otomatik ayarlar!
"""

import tkinter as tk
import random

class CikmaTeklifi:
    def __init__(self, root):
        self.root = root
        self.root.title("💘 Ebrar'a Teklif - Uygula 💘")
        self.root.configure(bg="#ffe6f0")

        # Pencereyi ekranın ortasına ve tam ekran moduna getir
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}+0+0")

        self.start_btn = tk.Button(root, text="💌 Tıkla ve Uygula 💌", font=("Arial", 32, "bold"),
                                   bg="#ff6699", fg="white", command=self.show_teklif)
        self.start_btn.pack(pady=screen_height // 4)

    def show_teklif(self):
        self.start_btn.destroy()

        self.label = tk.Label(self.root, text="Ebrar, benimle çıkar mısın? 💘",
                              font=("Arial", 28), bg="#ffe6f0", fg="#cc0066")
        self.label.pack(pady=60)

        self.evet_btn = tk.Button(self.root, text="Evet 💖", font=("Arial", 22, "bold"),
                                  bg="#66ff99", command=self.show_love)
        self.evet_btn.place(x=self.root.winfo_width()//4, y=self.root.winfo_height()//2)

        self.hayir_btn = tk.Button(self.root, text="Hayır 🙈", font=("Arial", 22, "bold"),
                                   bg="#ff6666")
        self.hayir_btn.place(x=self.root.winfo_width()//2, y=self.root.winfo_height()//2)

        self.root.bind("<Motion>", self.kacir_hayir)

    def kacir_hayir(self, event):
        x, y = event.x_root, event.y_root
        bx = self.hayir_btn.winfo_rootx()
        by = self.hayir_btn.winfo_rooty()
        bw = self.hayir_btn.winfo_width()
        bh = self.hayir_btn.winfo_height()
        win_w = self.root.winfo_width()
        win_h = self.root.winfo_height()

        if bx < x < bx + bw and by < y < by + bh:
            new_x = random.randint(50, win_w - 200)
            new_y = random.randint(100, win_h - 100)
            self.hayir_btn.place(x=new_x, y=new_y)

    def show_love(self):
        self.label.destroy()
        self.evet_btn.destroy()
        self.hayir_btn.destroy()
        self.root.unbind("<Motion>")

        for _ in range(100):
            kalp = tk.Label(self.root, text="❤️", font=("Arial", 28), bg="#ffe6f0")
            kalp.place(x=random.randint(0, self.root.winfo_width()-50), y=random.randint(0, self.root.winfo_height()-50))

        sevgi = tk.Label(self.root, text="SENİ SEVİYORUM EBRAR 💘", font=("Arial", 36, "bold"),
                         fg="#ff3399", bg="#ffe6f0")
        sevgi.pack(pady=100)

if __name__ == "__main__":
    root = tk.Tk()
    app = CikmaTeklifi(root)
    root.mainloop()