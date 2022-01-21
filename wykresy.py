import matplotlib.pyplot as plt
import json

def wykres():
    wybor=int(input("proszę wybrać rodzaj wykresu 1.szeregowanie procesów 2.zastępowanie stron : "))
    plik1="wyniki_szeregowanie.json"
    plik2="wyniki_zastepowanie.json"
    if wybor==1:
        with open(plik1,"r") as plik_json:     #ładowanie danych z pliku
            dane=json.load(plik_json)
        x = dane.keys()
        y=[]
        for czas_oczekiwania in dane.values():
            y.append(czas_oczekiwania[1])
        wykres=plt.subplot()
        wykres.set_title("Szeregowanie procesów")
        wykres.set_xlabel("pid")
        wykres.set_ylabel("czas oczekiwania")
        wykres.scatter(x,y,color='blue')
        plt.show()
    if wybor==2:
        with open(plik2,"r") as plik_json:     #ładowanie danych z pliku
            dane=json.load(plik_json)
        x = dane.keys()
        y=dane.values()
        wykres=plt.subplot()
        wykres.set_title("Zastępowanie stron")
        wykres.set_xlabel("pid")
        wykres.set_ylabel("całkowity czas spędzony w ramie")
        wykres.scatter(x,y,color='red')
        plt.show()
    if wybor!=1 and wybor!=2:
        wybor=int(input("proszę spróbować jeszcze raz 1.szeregowanie procesów 2.zastępowanie stron : "))
wykres()