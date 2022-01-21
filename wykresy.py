import matplotlib.pyplot as plt
import json

def wykres():
    plik="wyniki_szeregowanie.json"
    with open(plik,"r") as plik_json:     #ładowanie danych z pliku
        dane=json.load(plik_json)
    x = dane.keys()
    y=[]
    z=[]
    for czas_zakonczenia in dane.values():
        y.append(czas_zakonczenia[0])
    for czas_oczekiwania in dane.values():
        z.append(czas_oczekiwania[1])
    wykres1=plt.subplot()
    wykres1.set_xlabel("pid")
    wykres1.set_ylabel("czas zakończenia")
    wykres1.scatter(x,y,color='blue')
    plt.show()
    wykres2=plt.subplot()
    wykres2.set_xlabel("pid")
    wykres2.set_ylabel("czas oczekiwania")
    wykres2.scatter(x,z,color='red')
    plt.show()
wykres()