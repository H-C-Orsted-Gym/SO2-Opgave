# ALLE KRAV HER:

# - pH skal ligge på 7 - 7,4
# - Frit klor skal ligge på 0.5-3mg/l
# - z   

# ALLE MÅDER MAN LAVER JUSTERINGER PÅ:


# I vores 

# HOCL koncentration = frit Klor koncentration / volumen 
# 4.5 pH == HOCL

# HOCl/OCl-
# Disse chlorforbindelser benævnes ofte samlet
# som frit chlor. 

# pis = ammonium
# ammonium og frit klor = bundet klor
# Stop børnene i at pisse i vandet
# monoklorit = poolstank

from numpy import random
import time
nuværendepH = 7
nuværendeFritKlor = 1
nuværendeBundetKlor = 0

def CheckWater(førpH, førFritKlor, førBundetKlor):
    global nuværendepH
    nuværendepH = round(random.uniform(førpH - 0.1, førpH + 0.1), 2)
    print("nuværende pH værdi er:", nuværendepH)

    global nuværendeFritKlor
    nuværendeFritKlor = round(random.uniform(førFritKlor - 0.1, førFritKlor + 0.1), 2)
    if nuværendeFritKlor <= 0:
        nuværendeFritKlor = 0
    print("nuværende frit klor mængde er:", nuværendeFritKlor)

    
    global nuværendeBundetKlor
    nuværendeBundetKlor = round(random.uniform(førBundetKlor - 0.1, førBundetKlor + 0.1), 2)
    if nuværendeBundetKlor <= 0:
        nuværendeBundetKlor = 0
    print("nuværende bundet klor mængde er:", nuværendeBundetKlor)

    
    
    
def CheckData(pH, fritKlor, bundetKlor):
    
    if pH >=7.4:
        while pH >= 7.4:
            pH -= 0.2
        global nuværendepH
        nuværendepH = pH
        print("vi fjerne noget klor. \n pH'en er nu:", pH)
    if pH < 7:
        while pH < 7:
            pH += 0.2
        nuværendepH = pH
        print("vi fjerne noget klor. \n pH'en er nu:", pH)
        
    if fritKlor >=3:
        while fritKlor >= 3:
            fritKlor -= 0.2
        global nuværendeFritKlor
        nuværendeFritKlor = fritKlor
        print("Vi tilsætter lidt klor.\n fritKlor koncentrationen er nu:", fritKlor)
    if fritKlor < 0.5:
        while fritKlor < 0.5:
            fritKlor += 0.2
        nuværendeFritKlor = fritKlor
        print("vi fjerne noget klor. \n fritKlor koncentrationen er nu:", fritKlor)

    if bundetKlor >=1:
        while bundetKlor >= 1:
            bundetKlor -= 0.2
        global nuværendeBundetKlor
        nuværendeBundetKlor = bundetKlor
        print(time.asctime( time.localtime(time.time()) ), "Vi filtrere vand ud.\n bundetKlor koncentrationen er nu er nu:", bundetKlor)



while True: 
    time.sleep(5)   
    CheckWater(nuværendepH,nuværendeFritKlor,nuværendeBundetKlor)
    CheckData(nuværendepH,nuværendeFritKlor,nuværendeBundetKlor)
    print("\n\n")

















     