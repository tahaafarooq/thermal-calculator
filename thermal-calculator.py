#author is @xploiter121(TELEGRAM) , email : tahacodez@gmail.com
"""
    Cw  = Specific heat capacity of water
    Cal = Specific heat capacity of aluminium
    Ccp = Specific heat capacity of copper
    Csw = Specific heat capacity of sea water
    Cpa = Specific heat capacity of paraffin
    Ti  = Initial temperature
    Tf  = Final temperature
    T   = Temperature
    M   = Mass of the substance

    Cal which is 900 Joules / Kg degrees Celcius

    This only calculates the heat absorbed only!
"""

import sys
import time

Cw = 4200
Ci = 2004
Cwv = 1996
Cal = 900
Ccp = 400
Csw = 3900
Cpa = 2200

#formula is MxCx(Ti-Tf) / MxCxTemp
#for dual its MCTemp = -(MCTemp)
#this is for single equation only thus the version upcoming will reconsider both 'A' and 'B'

#Example of a given question

M = int(input("enter the mass of the substance, dont specify units! : "))
substance_origin = str(input("enter the substance origin, copper, water, aluminium : "))
temperature_spec = input("Are the two specified temperatures , yes or no : ")
specific_heat_capacity = int()

def compare_heat_capacity():
    global specific_heat_capacity

    if substance_origin == 'water':
       specific_heat_capacity = Cw
    elif substance_origin == 'copper':
        specific_heat_capacity = Ccp
    elif substance_origin == 'aluminium':
        specific_heat_capacity = Cal
    elif substance_origin == 'sea water':
        specific_heat_capacity = Csw
    elif substance_origin == 'paraffin':
        specific_heat_capacity = Cpa
    elif substance_origin == 'ice':
	    specific_heat_capacity = Ci
    elif substance_origin == 'vapor':
	    specific_heat_capacity = Cwv
    else:
        sys.exit(1)

#def substance_origin_comparison():
#    if substance_origin == 'water':
#        substance_origin =  
#    elif substance_origin == 'copper':
#        substance_origin = Ccp
#    elif substance_origin == 'aluminium':
#        substance_origin = Cal
#    elif substance_origin == 'sea water':
#        substance_origin = Csw
#    elif substance_origin == 'paraffin':
#        substance_origin = Cpa
#    else:
#        sys.exit(1)
    
def calculate_thermal_energy():
#   substance_origin_comparison()
    compare_heat_capacity()
    if temperature_spec == 'yes':
        Ti = int(input("enter the initial temperature : "))
        Tf = int(input("enter the final temperature : "))
        energy = M*specific_heat_capacity*(Tf-Ti)
        print("calculating....")
        time.sleep(5)
        print("Your answer is : ")
        print(energy)
    elif temperature_spec == 'no':
        T = int(input("enter the temperature : "))
        energy = M*specific_heat_capacity*T
        print("calculating....")
        time.sleep(5)
        print("Your answer is : ")
        print(energy)
    else:
        sys.exit(1)

if __name__ == "__main__":
    calculate_thermal_energy()
