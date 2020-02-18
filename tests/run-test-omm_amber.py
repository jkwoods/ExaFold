#!/usr/bin/env python

from exafold import (Walker,
    OmmSystem, read_restraints, linear_peptide, OMM_RESTRAIN_distance, OMM_RESTRAIN_torsion)

from test_configuration import (
    input_prefix, system_file, restraint_prefix,
    md_instructions)

from simtk import unit as u

#---------- READ OpenMM Base System ------------------------#
linear_peptide()

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

#---------- BIND MD System to Walker -----------------------#
walker = Walker()
walker.generate_simulation(ommsystem)
walker.simulation.minimizeEnergy()

walker.configure_walk(md_instructions)
walker.go(distance_force, torsion_force)



