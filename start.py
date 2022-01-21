import procesor
import pamiec
import generator

wybor1=int(input("proszę wybrać działanie 1.szeregowanie procesów 2.zastępowanie stron : "))
wybor2=int(input("proszę zdecydować 1.gotowe dane z plików 2.wygenerowanie nowych danych : "))
if wybor1==1:
    if wybor2==1:
        procesor.procesor()
    else:
        generator.generator_procesów()
        procesor.procesor()
if wybor1==2:
    if wybor2==1:
        pamiec.pamiec()
    else:
        generator.generator_strony()
        pamiec.pamiec()
if wybor1!=1 and wybor1!=2:
    wybor=input("proszę spróbować jeszcze raz 1.szeregowanie procesów 2.zastępowanie stron: ")