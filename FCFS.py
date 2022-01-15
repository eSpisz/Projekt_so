kolejka = []  # PID
def fcfs(czas, procesy):
    for key,czas_przyjscia in procesy.items():
        if czas_przyjscia[0] == czas:
            kolejka.append(key)
    return kolejka
