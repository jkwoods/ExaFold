#!/usr/bin/env python3

## INPUT: 1. Name of pdb output file


from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
from sys import *

outputfile = sys.argv[1]
dist_k = 40.0

#import Amber files
prmtop = AmberPrmtopFile('input.prmtop')
inpcrd = AmberInpcrdFile('input.inpcrd')

#make distance rst
dist_force = CustomBondForce("0.5*k*(r-r0)^2")
dist_force.addGlobalParameter("k", 30.0)
dist_force.addPerBondParameter("r0")

#make angle rst
#ang_force = CustomTorsionForce("0.5*k*(1-cos(theta-theta0))")
#force.addPerTorsionParameter("theta0");
#force.addPerTorsionParameter("k");


#add all dist
#restraints.txt consists of one restraint per line
#with the format:
#atom_index_i 	atom_index_j	r0	k

# where the indices are zero-based
# from linear amber file
# make sure this file is cleaned of duplicates!!
with open('dist_rst.txt') as input_file:
    for line in input_file:
        columns = line.split()
        atom_index_i = int(columns[0])
        atom_index_j = int(columns[1])
        r0 = float(columns[2])

        dist_force.addBond(atom_index_i, atom_index_j, [r0])

#add all ang
#restraints.txt consists of one restraint per line
#with the format:
#particle_1_index	part2	part3	part4	phase0	k

# where the indices are zero-based
# make sure this file is cleaned of duplicates!!
#with open('ang_rst.txt') as input_file:
#    for line in input_file:
#        columns = line.split()
#        par1 = int(columns[0])
#        par2 = int(columns[1])
#	par3 = int(columns[2])
#	par4 = int(columns[3])
#	phase = float(columns[4])
#        k = float(columns[5])
#        ang_force.addBond(par1, par2, par3, par4, [phase, k])
#print(ang_force.getNumBonds())


#make system
system = prmtop.createSystem(nonbondedMethod=NoCutoff, constraints=None) #gas phase
print("num of part: " + str(system.getNumParticles()))
print(XmlSerializer.serialize(system));
print("AFTER")
system.addForce(dist_force)

integrator = LangevinIntegrator(300*kelvin, 1/picosecond, 0.001*picoseconds) #1 fs steps
simulation = Simulation(prmtop.topology, system, integrator)
simulation.context.setPositions(inpcrd.positions)
simulation.context.setParameter("k", 0.0)

#minimize
print("Minimizing Energy of System ...")

print(simulation.context.getState(getEnergy=True).getPotentialEnergy())
simulation.minimizeEnergy()
print(simulation.context.getState(getEnergy=True).getPotentialEnergy())
#simulated annealing
print("Running Simulated Annealing MD ...")
print(simulation.context.getState(getEnergy=True).getPotentialEnergy())
#heating
for i in range(5): #0K to 600K in 5 ps
    integrator.setTemperature(120*(i)*kelvin)
    simulation.reporters.append(PDBReporter(outputfile, 1000))
    simulation.reporters.append(StateDataReporter(stdout, 1000, step=True, potentialEnergy=True, temperature=True))
    simulation.step(1000)

print("Turning on Restraints ...")
#production #10 ps at 600K
f_incr = 0.0
for i in range(10): #turn on force rest
    integrator.setTemperature(600*kelvin)

    f_incr = f_incr + 0.1
    simulation.context.setParameter("k", (dist_k*f_incr))    

    simulation.reporters.append(PDBReporter(outputfile, 1000))
    simulation.reporters.append(StateDataReporter(stdout, 1000, step=True, potentialEnergy=True, temperature=True))
    simulation.step(1000)


print("Slow Cooling ...")
#cooling
for i in range(100): #600k to 0k slow cooling
    integrator.setTemperature(6*(100-i)*kelvin)
    simulation.context.setParameter("k", dist_k)

    simulation.reporters.append(PDBReporter(outputfile, 1000))
    simulation.reporters.append(StateDataReporter(stdout, 1000, step=True, potentialEnergy=True, temperature=True))
    simulation.step(1000)

print(XmlSerializer.serialize(system));
