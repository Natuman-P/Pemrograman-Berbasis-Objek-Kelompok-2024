import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps, ImageDraw

# Daftar anggota (nama, nomor identitas, dan path foto)
anggota = [
    {"nama": "Rio Andrew Permadi", "NPM": "2215061044", "foto": r"C:\Users\user\Documents\File-file Kuliah\Tugas Semester 4 (File Jadi)\PBO\UAS PBO\boy.jpg"},
    {"nama": "Iqbal Al Himni", "NPM": "2215061068", "foto": r"C:\Users\user\Documents\File-file Kuliah\Tugas Semester 4 (File Jadi)\PBO\UAS PBO\boy.jpg"},
    {"nama": "M. Luthfi Alfaridzi", "NPM": "2215061072", "foto": r"C:\Users\user\Documents\File-file Kuliah\Tugas Semester 4 (File Jadi)\PBO\UAS PBO\boy.jpg"},
    {"nama": "Andes Potipera Sitepu", "NPM": "2215061080", "foto": r"C:\Users\user\Documents\File-file Kuliah\Tugas Semester 4 (File Jadi)\PBO\UAS PBO\boy.jpg"},
    {"nama": "M. Dai Hakiki", "NPM": "2265061001", "foto": r"C:\Users\user\Documents\File-file Kuliah\Tugas Semester 4 (File Jadi)\PBO\UAS PBO\boy.jpg"}
]

class LandingPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kelompok 7 Pemrograman Berorientasi Objek")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")
        
        # Header
        header = tk.Label(self, text="Kelompok 7 PBO", font=("Arial", 24, "bold"), bg="#f0f0f0")
        header.pack(pady=20)
        
        # Konten
        self.frame_content = tk.Frame(self, bg="#f0f0f0")
        self.frame_content.pack(pady=20)
        
        self.frame_row = None
        
        for i, anggota_info in enumerate(anggota):
            if i % 2 == 0:
                self.frame_row = tk.Frame(self.frame_content, bg="#f0f0f0")
                self.frame_row.pack(pady=10)
            self.add_member(self.frame_row, anggota_info["nama"], anggota_info["NPM"], anggota_info["foto"], i + 1)
    
    def add_member(self, frame_row, nama, identitas, foto_path, nomor):
        frame_member = tk.Frame(frame_row, bg="#f0f0f0")
        frame_member.pack(side="left", padx=20, pady=10)
        
        # Reshape and apply circular border to the photo
        img = Image.open(foto_path)
        img = img.resize((100, 100), Image.LANCZOS)
        
        # Create a mask to create a circular border
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)
        img = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
        img.putalpha(mask)
        
        img_tk = ImageTk.PhotoImage(img)
        
        label_photo = tk.Label(frame_member, image=img_tk, bg="#f0f0f0")
        label_photo.image = img_tk
        label_photo.pack(side="top", padx=10)
        
        label_name = tk.Label(frame_member, text=nama, font=("Arial", 14), bg="#f0f0f0")
        label_name.pack(side="top", padx=10)
        
        label_id = tk.Label(frame_member, text=f"NPM: {identitas}", font=("Arial", 12), bg="#f0f0f0")
        label_id.pack(side="top", padx=10)

if __name__ == "__main__":
    app = LandingPage()
    app.mainloop()
