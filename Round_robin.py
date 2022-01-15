kolejka = []  # PID
czas_dla_procesu=int(input("proszę podać czas dla każdego procesu (>1): ")) #interwał czasowy jaki zostanie przydzielony procesowi na wykonanie
licznik_pomocniczy=czas_dla_procesu
def round_robin(czas, procesy):
    for key, czas_przyjscia in procesy.items():
        if czas_przyjscia[0] == czas:
            kolejka.append(key)
            licznik_pomocniczy=czas_dla_procesu
    if licznik_pomocniczy ==0:
        zmienna_pomocnicza=kolejka[0]
        kolejka.pop(0)
        kolejka.append(zmienna_pomocnicza)
    if licznik_pomocniczy>0:
        licznik_pomocniczy-=1
    return kolejka