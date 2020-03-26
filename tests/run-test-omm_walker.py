#!/usr/bin/env python

from exafold import (Walker,
    OmmSystem, read_restraints, OMM_RESTRAIN_distance, OMM_RESTRAIN_torsion)

from test_configuration import (
    input_prefix, system_file, restraint_prefix,
    md_instructions)

from simtk import unit as u

#---------- READ OpenMM Base System ------------------------#
prmtop = input_prefix / "prmtop"
inpcrd = input_prefix / "rst7"
ommsystem = OmmSystem(ff_type="amber", topology=prmtop, coordinates=inpcrd,)

#---------- READ Restraints --------------------------------#
#distances
distance_restraints = read_restraints(restraint_prefix / "8col.dist", "distance")
distance_force = 100.0

#torsions
torsion_restraints = read_restraints(restraint_prefix / "5col.angles", "torsion")
torsion_force = 100.0
#print(torsion_restraints)

#---------- APPLY Restraints -------------------------------#

#distances
this_restraint = OMM_RESTRAIN_distance["flatbottom_customforce"]
restraint_type = list(this_restraint)[0]
ommsystem.initialize_restraint_force(this_restraint)
ommsystem.add_restraint_interactions(restraint_type, distance_restraints) #[::10]
ommsystem.apply_restraint_force(restraint_type)

#torsions
tor_restraint = OMM_RESTRAIN_torsion["flatbottom_customforce"]
t_restraint_type = list(tor_restraint)[0]
ommsystem.initialize_restraint_force(tor_restraint)
ommsystem.add_restraint_interactions(t_restraint_type, torsion_restraints)
ommsystem.apply_restraint_force(t_restraint_type)


# ---------- Remove nonbounded forces -----------------------#
ommsystem.remove_nonbounded_forces()
print('Nonbounded forces has been removed \n')


# ---------- Apply Custom Nonbounded force ------------------#
weight = 0.1
ommsystem.apply_repulsive_force( weight)
print('Custom nonbounded force (LJ-repulsive only) has been applied \n')

#---------- BIND MD System to Walker -----------------------#
walker = Walker()
walker.generate_simulation(ommsystem)
print('Simulation has been generated \n')

print('Energy minimization 1) ... \n')
walker.simulation.minimizeEnergy( )
#walker.simulation.minimizeEnergy( maxIterations=200)
print('Energy minimization 1 has been completed \n')

#walker.update_sigma()
#walker.update_weight(0.6)
#print('Parameters have been updated \n')

walker.configure_walk("1aki_test_gomd.pdb", 5000, md_instructions)
print('Heat annealing ... \n')
#walker.go(distance_force, torsion_force, 1000)
walker.torsion_angle_md_go(distance_force, torsion_force, [800,500, 300], [1000, 1000, 1000])

#print('Energy minimization 2) ... \n')
#walker.simulation.minimizeEnergy( maxIterations=1000)
#print('Energy minimization 2 has been completed \n')

#walker.update_sigma()
#walker.update_weight(1.0)
#print('Parameters have been updated \n')

#print('Energy minimization 3) ... \n')
#walker.simulation.minimizeEnergy( maxIterations=100)


