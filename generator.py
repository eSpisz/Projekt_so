import json
from random import randrange

plik="dane_testowe.json"
procesy = {} # key=PID, wartosc tablicy[0]=czas przyjscia, wartosc tablicy[1]=czas wykonywania procesu

def generator():
    ilosc_procesow=int(input("proszę podać ilość procesów: "))  #przyjmowanie danych od użytkownika oraz sprawdzenie ich poprawności
    if ilosc_procesow < 0:
        print("niepoprawna ilość procesów")
        ilosc_procesow = int(input("proszę spróbować jeszcze raz: "))
    
    czas_przyjscia_min = int(input("proszę podać dolny limit czasu przyjścia procesu: "))  #przyjmowanie danych od użytkownika oraz sprawdzenie ich poprawności
    if czas_przyjscia_min < 1:
        print("niepoprawny czas")
        czas_przyjscia_min = int(input("proszę spróbować jeszcze raz: "))

    czas_przyjscia_max = int(input("proszę podać górny limit czasu przyjścia procesu: "))  #przyjmowanie danych od użytkownika oraz sprawdzenie ich poprawności
    if czas_przyjscia_max <= czas_przyjscia_min:
        print("niepoprawny czas")
        czas_przyjscia_max = int(input("proszę spróbować jeszcze raz: "))

    odchylenie = int(input("proszę podać odchylenie: "))   #przyjmowanie danych od użytkownika oraz sprawdzenie ich poprawności
    if odchylenie < 0:
        print("niepoprawne odchylenie")
        odchylenie = int(input("proszę spróbować jeszcze raz: "))

    sredni_czas_wykonania = int(input("proszę podać górny limit czasu trwania procesu: ")) #przyjmowanie danych od użytkownika oraz sprawdzenie ich poprawności
    if sredni_czas_wykonania < odchylenie:
        print("niepoprawny średni czas")
        sredni_czas_wykonania = int(input("proszę spróbować jeszcze raz: "))

    for proces in range(ilosc_procesow):   #generowanie procesów
        procesy[proces]=[0,0]
        procesy[proces][0]=randrange(czas_przyjscia_max-czas_przyjscia_min)+czas_przyjscia_min
        procesy[proces][1]=sredni_czas_wykonania-odchylenie+randrange(2*odchylenie)
    
    with open(plik,"w") as dane:   #zapis procesów do pliku
        json.dump(procesy,dane)
