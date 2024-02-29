# ASCII Art Generator

## Opis
Prosty program w Pythonie do generowania sztuki ASCII z obrazów. Konwertuje obrazy w formatach JPG/JPEG na pliki tekstowe (.txt) i obrazy PNG. Użtykownik może dowolnie zmienić parametry generowania obrazu, takie jak lista znaków, skala, szerokość i wysokość znaku, itp.

## Wymagania
- Python 3.x
- Biblioteka Pillow
- Biblioteka Tkinter

## Jak korzystać
1. Uruchom program za pomocą pliku `ascii.py`.
2. Program otworzy główne okno z logiem i przyciskiem do konwersji.
3. Wybierz przycisk "Konwertuj", aby wybrać plik obrazu jako input, następnie ścieżki gdzie; plik PNG (do zapisania obrazu) i plik TXT (do zapisania tekstu ASCII) zostaną końcowo zapisane.
4. Pasek postępu pokaże postęp konwersji.
5. Po zakończeniu konwersji pojawi się komunikat o sukcesie, a pliki zostaną zapisane.

## Uwagai 
- Z racji na nacisk czasowy i tego że dopiero ucze się frameworka tkintera, mogą pojawić się błedy mimo że dodałem obsługę błedów do wszystkiego co mi wpadło do głowy.
- Nie ma wielowątkowości, tzn. przez sposób napiania GUI obrazy sie kolejkują zamiast wykonywać naraz.
- Za wygląd makaronowy klasy UX, z góry przeprszam. Inwencja twórcza. 

Niech żyje sztuka. 
