import json

plik="dane_testowe.json"
procesy = {1: [0, 0]} # key=PID, wartosc tablicy[0]=czas przyjscia, wartosc tablicy[1]=czas wykonywania procesu











with open(plik,"w") as dane:
    json.dump(procesy,dane)