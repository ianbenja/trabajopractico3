import random


def Dia_averia ():
    rnd_averia = random.random()
    dia_ave = None  
    if rnd_averia < 0.25:
        dia_ave = 5
    elif rnd_averia < 0.70:
        dia_ave = 6
    elif rnd_averia < 0.90:
        dia_ave = 7
    elif rnd_averia < 1:
        dia_ave = 8
        

    return (rnd_averia, dia_ave)



rnd, dia = Dia_averia()
print("El random generado es:", rnd)
print ("El dia que toca es el dia: ",dia)
