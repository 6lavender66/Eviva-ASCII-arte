# logic.py

from PIL import Image, ImageDraw, ImageFont
import math # kocham matme
import os
import threading

class Logic:

    def __init__(self, char_set, scale_factor, one_char_width, one_char_height, font_path, font_size):
        self.char_array = list(char_set[::-1]) # tworzymy liste tych znaków (przeniosłem tutaj również iterowanie od końca)
        self.char_length = len(self.char_array) # pobieramy jego długośc 
        self.interval = self.char_length / 256 # i bam mamy interwał 
        self.scale_factor = scale_factor
        self.one_char_width = one_char_width
        self.one_char_height = one_char_height

        # obsługa błędu czcionki, powinna wczytać wtedy systemową 
        try:
            self.font = ImageFont.truetype(font_path, font_size)
        except IOError:
            print("Error: Nie ma takiej czcionki")
            self.font = ImageFont.load_default()

    def get_char(self, input_int): # więc wartości pikseli są zapisywane w przedziale od 0 do 255
        return self.char_array[math.floor(input_int * self.interval)] # pixel jako input, mnożony jest z interwałem (w tym kontkeście zakres jednego znaku) następnie zwracana jest wartość zaokrąglona w dół które powinny być używanie na podstawie wartości pixela 

    def generate_ascii_art(self, image_path, output_path_png, output_path_txt, progress_bar, file_label):
        im = Image.open(image_path) # otwarcie pliku na którym będziemy operować 
        width, height = im.size # pobieranie szerokości i wysokości zdjęcia
        im = im.resize(
            (
                int(self.scale_factor * width),
                int(self.scale_factor * height * (self.one_char_width / self.one_char_height))
            ),
            Image.NEAREST
            
        ) # więc tak, przeskaluemy zdjęcie przez Skale oraz dla wysokości mnożmy przez iloraz szerokosci i długości jednego znaku, dlaczego wyjaśnione jest w main
        width, height = im.size # pobieranie szerokości i wysokości zdjęcia jeszcze raz, tym razem przeskalowanego
        pix = im.load() # załadowanie zdjęcia

        output_image = Image.new('RGB', (self.one_char_width * width, self.one_char_height * height), color=(0, 0, 0))
        draw = ImageDraw.Draw(output_image)

        # tutaj dodałem logike paska łądowania do menu 
        total_pixels = width * height
        progress_step = 100 / total_pixels

        with open(output_path_txt, 'w') as text_file:
            for i in range(height):
                for j in range(width): # kolejno iteratacja przez każdy pixel
                    r, g, b = pix[j, i] # pobieramy wartości kolorów w formacie RGB

                    # tutaj zatrzymajmy sie na chwile, natężenie/pokrycie znaku mówi co dokładnie zobaczymy, tak więc musimy przerobić zdjęcie na czarnobiałe 
        
                    h = int(r/3 + g/3 + b/3) # efekt otrzymuje tutaj przez wyciągnięciu średniej 

                    pix[j, i] = (h, h, h) # teraz zastępujemy pixel kolorem szarym

                    text_file.write(self.get_char(h)) # teraz każdy pixel zapisujemy do danego znaku
                    draw.text((

                                j * self.one_char_width, 
                                i * self.one_char_height), 
                                self.get_char(h), 
                                font=self.font,
                                fill=(r, g, b)
                                
                    ) # tutaj rysujemy na obrazku, najporściej mówiąc
                    
                    # aktualizacja paska postępu
                    progress_bar['value'] += progress_step
                    progress_bar.update()

                text_file.write('\n') # nowa linia co każdy wiersz

        output_image.save(output_path_png)

        # reset pasku postępu po zakończeniu generowania
        progress_bar['value'] = 0
        progress_bar.update()

        # eykieta pliku
        file_label.config(text=f"Wczytany plik: {os.path.basename(image_path)}") # zapisanie ciągów znaków jako zdjęcie, całkiem cool, taka znakocepcja + zmienna przekazywana do menu
