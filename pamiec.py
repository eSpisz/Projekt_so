from random import randrange
import math
import json
#założenia: 1 adres = 1 strona, 1 czas wykonania= 1 strona
plik = "dane_testowe.json"
with open(plik) as plik_json:  # ładowanie danych z pliku
    procesy_pomocnicza = json.load(plik_json)
procesy = {}
# ładowanie danych z formatu json zmienia int w kluczach na str, więc tu następuje ponowna konwersja do poprawnego typu
for pid, tablica in procesy_pomocnicza.items():
    procesy[int(pid)] = tablica


pamiec_logiczna={} #key=pid, tablica=adresy logiczne
pamiec_ram={} #key=pid, tablica=adresy fizyczne
pamiec_dysk={} #key=pid, tablica=adresy stron zrzuconych 
procent_stron_zrzucanych=0.3 #procent stron(około), ostatnie, które mają być zrzucone na dysk 

def pamiec(procesy):
    global pamiec_logiczna
    global pamiec_ram
    global pamiec_dysk
    adres=0
    for pid, strony in procesy.items():
        adres+=strony[1]
        pamiec_logiczna[pid] = [x for x in range(adres-strony[1],adres)]
        pamiec_ram[pid]=[x for x in range(adres-strony[1],adres-math.floor(strony[1]*procent_stron_zrzucanych))]
        pamiec_dysk[pid]=[x for x in range(adres-math.floor(strony[1]*procent_stron_zrzucanych),adres)]
pamiec(procesy)
print(pamiec_logiczna)
print(pamiec_ram)
print(pamiec_dysk)