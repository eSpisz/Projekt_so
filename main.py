import FCFS 
import Round_robin
import json
import generator

#generator.generator() #wywołanie generatora danych

plik = "dane_testowe.json"    
with open(plik) as plik_json:     #ładowanie danych z pliku
    procesy_pomocnicza=json.load(plik_json)

procesy={}   # key=PID, wartosc tablicy[0]=czas przyjscia, wartosc tablicy[1]=czas wykonywania procesu
stat_procesy={} #statystyka procesow, key=PID, wartosc tablicy[0]=czas zakończenia, wartosc tablicy[1]=czas oczekiwania
for pid, tablica in procesy_pomocnicza.items():   #ładowanie danych z formatu json zmienia int w kluczach na str, więc tu następuje ponowna konwersja do poprawnego typu
    procesy[int(pid)]=tablica
    stat_procesy[int(pid)]=[0,0]

del procesy_pomocnicza #usuwanie niepotrzebnej już zmiennej
czas=0
wybor_algorytmu_szeregowania=int(input("proszę wybrać algorytm szeregowania (wpisać odpowiadającą liczbę) 1.FCFS 2.Round-Robin: "))   #wybor algorytmu
if wybor_algorytmu_szeregowania == 2:
    Round_robin.przypisanie_wartosci()


while True:
    if wybor_algorytmu_szeregowania==1:                        #obsługa błedu wyboru
        kolejka=FCFS.fcfs(czas, procesy)
    elif wybor_algorytmu_szeregowania==2:
        kolejka = Round_robin.round_robin(czas, procesy)
    else:
        wybor_algorytmu_szeregowania=input("Niepoprawny wybór, proszę spróbować jeszcze raz:")

    if czas == 50:                                 #warunek kończący po upływie określonego czasu
        break

    try:
        if procesy[kolejka[0]][1]>0:        #wykonywanie procesu
            procesy[kolejka[0]][1]-=1
            for oczekujace in kolejka:           #gdy proces sie wykonuje inne czekaja w kolejce, zliczanie czasow oczekiwan
                if oczekujace!=kolejka[0]:
                    stat_procesy[oczekujace][1]+=1
        if procesy[kolejka[0]][1] == 0:
            stat_procesy[kolejka[0]][0]=czas    #statystyka dotyczaca czasu zakonczenia
            del kolejka[0]                      #usuwanie wykonanych procesow z kolejki
    except:
        czas+=1
        continue

    czas += 1  # licznik czasu
    print(kolejka)
        
print(stat_procesy)