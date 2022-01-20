import json
from random import randrange

plik1="dane_testowe_szeregowanie.json"
plik2="dane_testowe_zastepowanie.json"
procesy = {} # key=PID, wartosc tablicy[0]=czas przyjscia, wartosc tablicy[1]=czas wykonywania procesu

def generator_procesów():
    ilosc_procesow=int(input("proszę podać ilość procesów: "))  #przyjmowanie danych od użytkownika oraz sprawdzenie ich poprawności
    if ilosc_procesow < 0:
        print("niepoprawna ilość procesów")
        ilosc_procesow = int(input("proszę spróbować jeszcze raz: "))
    
    czas_przyjscia_min = int(input("proszę podać dolny limit czasu przyjścia procesu: "))  #przyjmowanie danych od użytkownika oraz sprawdzenie ich poprawności
    if czas_przyjscia_min < 0:
        print("niepoprawny czas")
        czas_przyjscia_min = int(input("proszę spróbować jeszcze raz: "))

    czas_przyjscia_max = int(input("proszę podać górny limit czasu przyjścia procesu: "))  #przyjmowanie danych od użytkownika oraz sprawdzenie ich poprawności
    if czas_przyjscia_max < czas_przyjscia_min:
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
    
    with open(plik1,"w") as dane:   #zapis procesów do pliku
        json.dump(procesy,dane)

def generator_strony():
    pamiec_logiczna={}
    ilosc_stron=int(input("proszę podać pożądaną ilość stron: "))
    if ilosc_stron<1:
        ilosc_stron = int(input("niepoprawna wartość, proszę spróbować jeszcze raz: "))
    czas_przyjscia_min=int(input("proszę podać dolny limit czasu przyjścia: "))
    if czas_przyjscia_min<0:
        czas_przyjscia_min = int(input("niepoprawna wartość, proszę spróbować jeszcze raz: "))
    czas_przyjscia_max=int(input("proszę podać górny limit czasu przyjścia: "))
    if czas_przyjscia_max<czas_przyjscia_min:
        czas_przyjscia_max = int(input("niepoprawna wartość, proszę spróbować jeszcze raz: "))
    for strona in range(ilosc_stron):
        pamiec_logiczna[strona]=czas_przyjscia_min+randrange(czas_przyjscia_max-czas_przyjscia_min)
    with open(plik2,"w") as dane:   #zapis procesów do pliku
        json.dump(pamiec_logiczna,dane)
