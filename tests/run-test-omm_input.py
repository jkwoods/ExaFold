#!/usr/bin/env python

from xlafold import (
    OmmSystem, read_restraints,
)
from test_configuration import (
    input_prefix, system_file, restraint_prefix
)

#---------- READ OpenMM Base System ------------------------#
prmtop = input_prefix / "prmtop"
inpcrd = input_prefix / "rst7"

ommsystem = OmmSystem(
    ff_type="amber",
    topology=prmtop,
    coordinates=inpcrd,
)

ommsystem.save_xml(system_file)
othsystem = OmmSystem(system_file=system_file)

#---------- READ Restraints --------------------------------#
file_torsion_restraints  = restraint_prefix / "dihedral.tbl"
file_distance_restraints = restraint_prefix / "contact.tbl"
#torsion_restraints = read_restraints(file_torsion_restraints, "torsion")
distance_restraints = read_restraints(file_distance_restraints, "distance")

#---------- APPLY Restraints ------------------------------#
for restraint_func, restraints in distance_restraints.items():
    print("Adding restraints with function: %s" % restraint_func)
    for rr, k in zip(*restraints):
        print(rr, k)
