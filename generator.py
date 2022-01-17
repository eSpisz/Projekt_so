import json
from random import randrange

plik="dane_testowe.json"
procesy = {1: [0, 0]} # key=PID, wartosc tablicy[0]=czas przyjscia, wartosc tablicy[1]=czas wykonywania procesu

def generator():
    ilosc_procesow=int(input("proszę podać ilość procesów: "))
    if ilosc_procesow < 0:
        print("niepoprawna ilość procesów")
        ilosc_procesow = int(input("proszę spróbować jeszcze raz: "))
    
    czas_przyjscia_min = int(input("proszę podać dolny limit czasu przyjścia procesu: "))
    if czas_przyjscia_min < 0:
        print("niepoprawny czas")
        czas_przyjscia_min = int(input("proszę spróbować jeszcze raz: "))

    czas_przyjscia_max = int(input("proszę podać górny limit czasu przyjścia procesu: "))
    if czas_przyjscia_max <= czas_przyjscia_min:
        print("niepoprawny czas")
        czas_przyjscia_max = int(input("proszę spróbować jeszcze raz: "))

    odchylenie = int(input("proszę podać odchylenie: "))
    if odchylenie < 0:
        print("niepoprawne odchylenie")
        odchylenie = int(input("proszę spróbować jeszcze raz: "))

    sredni_czas_wykonania = int(input("proszę podać górny limit czasu trwania procesu: "))
    if sredni_czas_wykonania < odchylenie:
        print("niepoprawny średni czas")
        sredni_czas_wykonania = int(input("proszę spróbować jeszcze raz: "))

    for proces in range(ilosc_procesow):
        procesy[proces]=[0,0]
        procesy[proces][0]=randrange(czas_przyjscia_max-czas_przyjscia_min)+czas_przyjscia_min
        procesy[proces][1]=sredni_czas_wykonania-odchylenie+randrange(2*odchylenie)
    
    with open(plik,"w") as dane:
        json.dump(procesy,dane)
generator()