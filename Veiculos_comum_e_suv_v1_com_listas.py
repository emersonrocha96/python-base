#!/usr/bin/env python3




modelo1 = ["RENEGADE","COMPASS","HILLUX","DISCOVERY","EVOQUE","HRV","2008","T-308"]
modelo2 = ["PE208","GOL","POLO","PALIO","CIVIC", "COROLA"]



VOLKSWAGEN = ["GOL","POLO","T-308"]
FIAT = ["RENEGADE","COMPASS","PALIO"]
PEUGEOT = ["PE208","2008"]
HONDA = ["HRV","CIVIC"]
LAND_ROUVER = ["DISCOVERY","EVOQUE"]
TOYOTA = ["HILLUX","COROLA"]


modelos = [
    ("VOLKSWAGEN",VOLKSWAGEN),
    ("FIAT", FIAT),
    ("PEUGEOT", PEUGEOT),
    ("HONDA", HONDA),
    ("LAND ROUVER", LAND_ROUVER),
    ("TOYOTA", TOYOTA),
    
    
] 

for nome_modelo, modelo in modelos:

    print()
    print("-" * 40)
    print(f" A Marca do veículo é {nome_modelo}")
    print("-" * 40)
    
    suv_modelo1 = []
    comum_modelo2 = []

    for carro in modelo:
        if carro in modelo1:
            suv_modelo1.append(carro)
        elif carro in modelo2:
            comum_modelo2.append(carro)
      

    print()        
    print("SUV:   ",suv_modelo1)
    print("COMUM: ",comum_modelo2)
    print("*" * 40)
