def lru(czas_procesow_ram, strona, pamiec_ram, pamiec_dysk):
    strona_do_wymiany=czas_procesow_ram.index(max(czas_procesow_ram))
    pamiec_ram[strona_do_wymiany]=strona
    czas_procesow_ram[strona_do_wymiany]=0
    del pamiec_dysk[pamiec_dysk.index(strona)]
    return pamiec_ram, pamiec_dysk
