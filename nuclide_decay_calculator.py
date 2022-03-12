from tables import *
from colorama import *

# Add color for output
C = Fore.LIGHTCYAN_EX
Y = Fore.LIGHTYELLOW_EX
W = Fore.LIGHTWHITE_EX

def type_of_decay(l_el, r_el):
    try:
        # Search periodic table
        for el in ElementData.table:       
            if el in r_el.split("-")[0]:
                atomic_right = ElementData.table.index(el)
                mass_right = int(r_el.split("-")[1])         
        
            if el in l_el.split("-")[0]:
                atomic_left = ElementData.table.index(el)
                mass_left = int(l_el.split("-")[1])            
    
        # Difference
        atomic = atomic_left - atomic_right
        mass = mass_left - mass_right  
    
        # Return Decay
        return ElementData.subpart[f'{atomic}, {mass}']

    except Exception as e:
        print(f'{e}')    
    
def daughter_nuclide(l_el, _particle):
    try:
        for el in ElementData.table:    
            if el in l_el.split("-")[0]:
                atomic_numpl = ElementData.table.index(el)
                mass_numpl = int(l_el.split("-")[1])

            # Loops for Validation, saves time
        for mass, particle in ElementData.subpart.items():
            if _particle in particle:        
                atom_nump = int(mass.split(', ')[0])
                mass_nump = int(mass.split(', ')[1])

        # Difference  
        dghtr_atom = atomic_numpl - atom_nump                                
        dghtr_mass = mass_numpl - mass_nump        

        return f'{ElementData.table[dghtr_atom]}-{dghtr_mass}'

    except Exception as e:
        print(f'{e}') 

# Results
type = type_of_decay('S-26', 'P-25')
nucl = daughter_nuclide('N-10', 'proton')

# Output formatted
print(f'{C}Type of Decay: {Y}{type.title()}\n{C}Daughter Nuclide: {Y}{nucl}{W}')