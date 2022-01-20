def fifo(strona, pamiec_ram, pamiec_dysk):
    pomocnicza=pamiec_ram[0]
    del pamiec_ram[0]
    pamiec_ram.append(strona)
    del pamiec_dysk[pamiec_dysk.index(strona)]
    pamiec_dysk.append(pomocnicza)
    return pamiec_ram, pamiec_dysk