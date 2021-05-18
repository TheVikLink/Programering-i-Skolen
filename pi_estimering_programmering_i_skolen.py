



import random
from matplotlib import pyplot as plt
from math import pi


def estimer_pi(antall_decimaler_nøyaktighet):
    
    X = [] #Lagre x- koordinat til pilkast
    Y = [] #Lagre y- koordinat til pilkast

    innenfor_sirkelen = 0 #Tell antall pilkast som treffer inni sirkelen
    antall_kast = 0 #Tell antall kast
    
    pi_med_ønsket_antall_decimaler = '{:.{}f}'.format(pi, antall_decimaler_nøyaktighet) #Formatter pi med ønsket antall decimaler ved å gjøre den om
                                                                                        #til en string. Dette gjør at vi kan bruke format- metoden for å velge 
                                                                                        #antall desimal. 
                                                                                        
    pi_med_ønsket_antall_decimaler = float(pi_med_ønsket_antall_decimaler) #Gjør deretter om fra string til float, for å kunne sammenligne
                                                                           # verdien med estimert verdi i while not- loopen
    
    formattert_pi_estimat_float = 0 #Må definere variabelen før den brukes som vilkår for while- loopen
    
    while not pi_med_ønsket_antall_decimaler == formattert_pi_estimat_float: #Fortsetter til ønsket antall decimalers nøyaktighet er oppnådd
    
        x = random.uniform(-1, 1) #Velger et tilfeldig x- koordinat mellom -1 og 1. Uniform sannsynlighet
        y = random.uniform(-1, 1) #Velger et tilfeldig y- koordinat mellom -1 og 1. Uniform sannsynlighet
        
        if x**2 + y**2 < 1: #Sjekker om pilkastet treffer inni sirklene. Hvis ja, legg til koordinatene i X og Y, og øk tellevariabel med 1
            innenfor_sirkelen += 1
            X.append(x)
            Y.append(y)
            
        antall_kast += 1 #Må telle antall kast for å bruke tallet som nevner i pi- estimatet
        
        pi_estimat = (innenfor_sirkelen / antall_kast) *4 #Areal sirkel = pi. Areal firkant = 4. Sannsynlighet for å treffe i sirkel = pi / 4.
                                                          #Må derfor gange med 4 for å finne pi. 
        
        formattert_pi_estimat = '{:.{}f}'.format(pi_estimat, antall_decimaler_nøyaktighet) #Formatterer pi- estimatet til ønsket antall desimal
        formattert_pi_estimat_float = float(formattert_pi_estimat) #Gjør om til float for å kunne sammenligne med pi med ønsket antall desimaler
        print(formattert_pi_estimat, pi_med_ønsket_antall_decimaler) #Printer pi_estimat for å følge prosessen når vi nærmer oss pi.
    
    plt.figure(figsize=(7,7)) 
    plt.plot(X,Y,'bo', markersize=7)  #Plotter x- og y- koordinatene fra alle pilkast som har truffet inni sirkelen
    plt.axis([-1, 1, -1, 1]) #Definerer aksegrenser
    plt.show() #Viser plottet
    return pi_estimat, antall_kast
        

print(estimer_pi(2))