#!/usr/bin/env python

from exafold import (
    OmmSystem, linear_peptide, read_restraints, OMM_RESTRAIN_distance)

from test_configuration import (
    input_prefix, system_file, restraint_prefix)

from simtk import unit as u

#---------- READ OpenMM Base System ------------------------#
linear_peptide()

prmtop = input_prefix / "prmtop"
inpcrd = input_prefix / "rst7"

ommsystem = OmmSystem(
    ff_type="amber",
    topology=prmtop,
    coordinates=inpcrd,)

ommsystem.save_xml(system_file)
othsystem = OmmSystem(system_file=system_file)

#---------- READ Restraints --------------------------------#
#file_torsion_restraints  = restraint_prefix / "dihedral.tbl"
file_distance_restraints = restraint_prefix / "8col.dist"
#torsion_restraints = read_restraints(file_torsion_restraints, "torsion")
distance_restraints = read_restraints(file_distance_restraints, "distance")

# Same force for each interaction right now
f_r = 2.0
[ri.append(f_r) for ri in distance_restraints]

#---------- APPLY Restraints ------------------------------#
#  - we select a restraint force implementation from
#    list of those defined in the `exafold` package
restraint_name = "simpleharmonic_customforce"
this_restraint = OMM_RESTRAIN_distance[restraint_name]
restraint_type = list(this_restraint)[0]

ommsystem.initialize_restraint_force(this_restraint)
ommsystem.add_restraint_interactions(restraint_type, distance_restraints)


