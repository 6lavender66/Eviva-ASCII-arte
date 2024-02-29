# menu.py

import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from tkinter import Toplevel
import threading

import os

from logic import Logic

class UX:

    def __init__(self, char_set, scale_factor, one_char_width, one_char_height, font_path, font_size):
        
        # tworzenie głównego okna
        self.root = tk.Tk()
        self.root.title("ASCII Art Generator")
        self.root.geometry("395x205")
        self.root.resizable(False, False)
        
        # ta linijka jest żeby sprawdzić położenie i rozmiar okna, przy innych też występuje
        #self.root.bind("<Configure>", lambda event: print(f"Wymiary: {self.root.winfo_width()}x{self.root.winfo_height()} | Położenie: {event.x}x{event.y}"))
        
        # zmienne które "skaczą" między oknami 
        self.char_set_var = tk.StringVar(value=char_set)
        self.scale_factor_var = tk.DoubleVar(value=scale_factor)
        self.one_char_width_var = tk.IntVar(value=one_char_width)
        self.one_char_height_var = tk.IntVar(value=one_char_height)
        self.font_path_var = tk.StringVar(value=font_path)
        self.font_size_var = tk.IntVar(value=font_size)

        # wywołanie klasy logic
        self.ascii_art_generator = Logic(
            char_set, scale_factor, one_char_width, one_char_height, font_path, font_size)
        
        # wywołanie głownego okna
        self.create_main_window()

    def create_main_window(self):
    
        # Logo    
        logo_text = r"""
    ╔═══╗              ╔═══╗    ╔╗
    ║╔═╗║              ║╔═╗║   ╔╝╚╗
    ║║ ║║╔══╗╔══╗╔╗    ║║ ║║╔═╗╚╗╔╝
    ║╚═╝║║══╣║╔═╝╠╣    ║╚═╝║║╔╝ ║║
    ║╔═╗║╠══║║╚═╗║║    ║╔═╗║║║  ║╚╗
    ╚╝ ╚╝╚══╝╚══╝╚╝    ╚╝ ╚╝╚╝  ╚═╝ 
"""

        logo_label = tk.Label(
            self.root, 
            text=logo_text, 
            font=("Courier", 12),  
            justify=tk.LEFT,        # Notka dla przyszłych polokeń: To ustawienie pozwala na na drukowanie stringów z zachowaniem miejsca, bez tego wychodziły babole
        )
        logo_label.grid(row=0, column=0, columnspan=2, pady=10)


        # przycisk do zmiany parametrów
        param_button = tk.Button(self.root, text="Zmień parametry", command=self.change_parameters)
        param_button.grid(row=1, column=0, padx=10)

        # przycisk do konwertowania
        convert_button = tk.Button(self.root, text="Konwertuj", command=self.convert_image)
        convert_button.grid(row=1, column=1, padx=10)

        # funkcja do otwierania okiena wyboru pliku, przez to powstał cały ten plik
    def open_file_dialog(self, filetypes, title):
        return filedialog.askopenfilename(title=title, filetypes=filetypes)
        
        # to samo co wyżej, tylko wybierasz scieżki outputu
    def save_file_dialog(self, defaultextension, filetypes, title):
        return filedialog.asksaveasfilename(title=title, defaultextension=defaultextension, filetypes=filetypes)
    
        # zmiany parametrów
    def change_parameters(self):
        param_window = tk.Toplevel(self.root)
        param_window.title("Change Parameters")
        param_window.geometry("660x400")
        param_window.resizable(False, False)
        #param_window.bind("<Configure>", lambda event: print(f"Wymiary: {param_window.winfo_width()}x{param_window.winfo_height()} | Położenie: {event.x}x{event.y}"))


        # widgety, głównie inputy, etykiety i guziczki

        char_set_label = tk.Label(param_window, text="Lista wykorzystywnach znaków:", pady=10)
        char_set_entry = tk.Entry(param_window, textvariable=self.char_set_var, width=70, validate="key", validatecommand=(param_window.register(self.validate_char_set_entry), '%P'))
        char_set_label.pack()
        char_set_entry.pack()

        scale_factor_label = tk.Label(param_window, text="Skala:", pady=10)
        scale_factor_entry = tk.Entry(param_window, textvariable=self.scale_factor_var, width=3)
        scale_factor_label.pack()
        scale_factor_entry.pack()

        one_char_width_label = tk.Label(param_window, text="Szerokość jednego znaku:", pady=10)
        one_char_width_entry = tk.Entry(param_window, textvariable=self.one_char_width_var, width=3)
        one_char_width_label.pack()
        one_char_width_entry.pack()

        one_char_height_label = tk.Label(param_window, text="Wysokość jednego znaku:", pady=10)
        one_char_height_entry = tk.Entry(param_window, textvariable=self.one_char_height_var, width=3)
        one_char_height_label.pack()
        one_char_height_entry.pack()

        font_path_label = tk.Label(param_window, text="Sćieżka do czcionki:", pady=10)
        font_path_entry = tk.Entry(param_window, textvariable=self.font_path_var, width=50)
        font_path_label.pack()
        font_path_entry.pack()

        font_size_label = tk.Label(param_window, text="Rozmiar czcionki:", pady=10)
        font_size_entry = tk.Entry(param_window, textvariable=self.font_size_var, width=3)
        font_size_label.pack()
        font_size_entry.pack()
        
        # przycisk save
        save_button = tk.Button(param_window, text="Zapisz", command=self.save_parameters)
        save_button.pack()
        
        # funckja sprawdzająca czy jakiś znak w ciągu możliwych do wybrania sie powtórzył
    def validate_char_set_entry(self, new_value):
        if any(new_value.count(char) > 1 for char in new_value):
            return False
        return True
    
        # zgarniamy zmienne z save żeby przekazać je dalej
    def save_parameters(self):
        char_set = self.char_set_var.get()
        scale_factor = self.scale_factor_var.get()
        one_char_width = self.one_char_width_var.get()
        one_char_height = self.one_char_height_var.get()
        font_path = self.font_path_var.get()
        font_size = self.font_size_var.get()

        # update ów zmiennych do main
        self.ascii_art_generator.char_array = list(char_set[::-1])
        self.ascii_art_generator.char_length = len(self.ascii_art_generator.char_array)
        self.ascii_art_generator.interval = self.ascii_art_generator.char_length / 256
        self.ascii_art_generator.scale_factor = scale_factor
        self.ascii_art_generator.one_char_width = one_char_width
        self.ascii_art_generator.one_char_height = one_char_height

        try:
            self.ascii_art_generator.font = ImageFont.truetype(font_path, font_size)
        except IOError:
            print("Error: Nie ma takiej czcionki")
            self.ascii_art_generator.font = ImageFont.load_default()
            # kontrola błedu
            
        # obejście problemu zamykania okien
        tk.messagebox.showerror("Info", "Zapisano pomyślnie")
        
        # funkcja tworzy okno przy konwertowaniu
    def create_progress_window(self, input_image, output_path_png, output_path_txt):
    
        progress_window = Toplevel(self.root)
        progress_window.title("Przetwarzanie...")
        #progress_window.bind("<Configure>", lambda event: print(f"Wymiary: {progress_window.winfo_width()}x{progress_window.winfo_height()} | Położenie: {event.x}x{event.y}"))

        file_label = tk.Label(progress_window, text=f"Wczytany plik: {os.path.basename(input_image)}")
        file_label.pack(pady=5)
        file_label.destroy()

        progress_bar = ttk.Progressbar(
            progress_window, orient="horizontal", length=300, mode="determinate")
        progress_bar.pack(pady=10)
        progress_bar.destroy()

        # generowanie obraz
        self.ascii_art_generator.generate_ascii_art(input_image, output_path_png, output_path_txt, progress_bar, file_label)

        file_label2 = tk.Label(progress_window, text="Obraz pomyślnie wygenerowano")
        file_label2.pack(pady=5)
        
        destroy_button = ttk.Button(progress_window, text="Ok :D", command = lambda: progress_window.destroy())
        destroy_button.pack(pady=5)
        
        threading.Thread(target=run_in_thread).start()

    def convert_image(self):
        input_image = None
        output_path_png = None
        output_path_txt = None

        while not (input_image and output_path_png and output_path_txt):
            input_image = self.open_file_dialog(
                [("Pliki JPEG", ".jpeg"), ("Pliki JPG", "*.jpg"), ("Wszystkie pliki", "*.*")],
                "Wybierz zdjęcie"
            )

            if not input_image:
                # jeśli użytownik anuluje wyboru, przerywa sie pętla
                break
                
             #kontrola błedu dla plików nie zdjęciowych
            if not input_image.lower().endswith(('.jpg', '.jpeg')):
                tk.messagebox.showerror("Error", "Program obsługuje tylko formaty JPG i JPEG")
                continue

            output_path_png = self.save_file_dialog(
                ".png",
                [("Pliki PNG", "*.png"), ("Wszystkie pliki", "*.*")],
                "Zapisz plik PNG"
            )

            if not output_path_png:
                # jeśli nie wybrało outputu pętla zaczyna sie od nowa
                continue

            output_path_txt = self.save_file_dialog(
                ".txt",
                [("Pliki TXT", "*.txt"), ("Wszystkie pliki", "*.*")],
                "Zapisz plik TXT"
            )

            if not output_path_txt:
                continue

        # kontrola błedu
        if input_image and output_path_png and output_path_txt:
            self.create_progress_window(input_image, output_path_png, output_path_txt)
        else:
            tk.messagebox.showerror("Error", "Musisz wybrać obie ścieżki zapisu!")
