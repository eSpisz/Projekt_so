import json
import FIFO
import LRU
from random import randrange

plik = "dane_testowe_zastepowanie.json"

def pamiec():
    wybor = 0
    czas = 0
    liczba_wymienionych = 0
    pojemnosc_ram = 5
    pamiec_logiczna = {}  # key=numer strony, value=czas przyjscia
    pamiec_ram = []  # numer strony
    pamiec_dysk = []  # numer strony
    czas_procesow_ram = []  # czas procesów w ramie

    with open(plik) as plik_json:  # ładowanie danych z pliku
        pomocnicza = json.load(plik_json)
    for strona, czas_przyjscia in pomocnicza.items():   #ładowanie danych z formatu json zmienia int w kluczach na str, więc tu następuje ponowna konwersja do poprawnego typu
        pamiec_logiczna[int(strona)]=czas_przyjscia

    wybor = int(input("proszę wybrać rodzaj zastępowania: 1.FIFO 2.LRU: "))
    while True:
        strona = randrange(len(pamiec_logiczna))   #losowanie, która strona będzie potrzebna
        if strona not in pamiec_ram and len(pamiec_ram)<pojemnosc_ram:  #decyzje czy strona jest aktualnie w pamięci ram czy trzeba ją ściągnąć z dysku
            pamiec_ram.append(strona)
            czas_procesow_ram.append(0)
        elif strona not in pamiec_dysk and strona not in pamiec_ram:
            pamiec_dysk.append(strona)
        elif strona not in pamiec_ram and not len(pamiec_ram) < pojemnosc_ram and strona in pamiec_dysk:
            if wybor == 1:
                pamiec_ram, pamiec_dysk = FIFO.fifo(strona, pamiec_ram, pamiec_dysk)
            if wybor == 2:
                pamiec_ram, pamiec_dysk = LRU.lru(czas_procesow_ram, strona, pamiec_ram, pamiec_dysk)
            liczba_wymienionych+=1
        for x in range(len(czas_procesow_ram)):
            czas_procesow_ram[x]+=1
        czas += 1
        if czas==50:
            break
        print("obecny stan pamięci ram: {}".format(pamiec_ram))
        print("obecny stan pamięci na dysku: {}".format(pamiec_dysk))
    print("liczba_wymienionych stron= {}".format(liczba_wymienionych))

