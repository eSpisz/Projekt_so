kolejka = []  # PID
licznik_pomocniczy = 0  #zmienna, która wskazuje kiedy powinno nastąpić przesunięcie kolejki
czas_dla_procesu = 0  #stała która służy do resetowania zmiennej licznik_pomocniczy

def przypisanie_wartosci():                         #funkcja wywolywana w main.py aby przekazac wartosc interwału czasu 
    global licznik_pomocniczy
    global czas_dla_procesu
    licznik_pomocniczy = int(input("proszę wybrać interwał czasowy dla każdego procesu: "))
    czas_dla_procesu = licznik_pomocniczy


def round_robin(czas, procesy):         #ciało funkcji tworzacej kolejke dla procesora 
    global licznik_pomocniczy
    global czas_dla_procesu
    for key, czas_przyjscia in procesy.items():    #pętla dodająca proces, którzy nadszedł do kolejki 
        if czas_przyjscia[0] == czas:
            kolejka.append(key)
    if licznik_pomocniczy ==0:          
        try:
            zmienna_pomocnicza=kolejka[0]    #blok kodu odpowiedzialny za przesuwanie kolejki
        except:
            zmienna_pomocnicza=0
        else:
            kolejka.pop(0)
            kolejka.append(zmienna_pomocnicza)
            licznik_pomocniczy += czas_dla_procesu
    if licznik_pomocniczy>0:
        licznik_pomocniczy-=1
    return kolejka

