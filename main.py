import FCFS 
import Round_robin


stat_procesy={1:[0,0],2: [0,0], 3: [0, 0]} #statystyka procesow, key=PID, wartosc tablicy[0]=czas zakończenia, wartosc tablicy[1]=czas oczekiwania
procesy = {1: [0, 1], 2: [1, 2], 3: [3, 3]}
czas=0
#wybor_algorytmu_szeregowania=input("proszę wybrać algorytm szeregowania (wpisać odpowiadającą liczbę): 1.FCFS 2.Round-Robin")   #wybor algorytmu
while True:
    kolejka = Round_robin.round_robin(czas, procesy)
    print(kolejka)
    #if wybor_algorytmu_szeregowania==int(1):                        #obsługa błedu wyboru
        #kolejka=FCFS.fcfs(czas, procesy)
    #elif wybor_algorytmu_szeregowania==int(2):
        #kolejka = Round_robin.round_robin(czas, procesy)
    #else:
        #wybor_algorytmu_szeregowania=input("Niepoprawny wybór, proszę spróbować jeszcze raz:")
    if czas == 20:                                 #warunek kończący po upływie określonego czasu
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
    
        
print(procesy)
print(stat_procesy)