import numpy as np
from ase import io, atoms

Temp = '300'
atoms = io.read('POSCAR')
pos = atoms.get_positions()
disp = np.loadtxt('thermal_displacements.yaml',skiprows=6,usecols=(2,3,4))
pos += disp
atoms.set_positions(pos)
io.write('POSCAR'+Temp,atoms,direct=True)
