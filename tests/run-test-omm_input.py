#!/usr/bin/env python

from OpenMMPlayground import (
    OmmSystem, read_restraints,
)
from test_configuration import (
    input_prefix, system_file
)

prmtop = input_prefix / "prmtop"
inpcrd = input_prefix / "rst7"

ommsystem = OmmSystem(
    ff_type="amber",
    topology=prmtop,
    coordinates=inpcrd
)

ommsystem.save_xml(system_xml)


file_distance_restraints = input_prefix / "contacts.txt"
distance_restraints = read_restraints(file_distance_restraints, "distance")

#system = system_from_xml(system_file)

for restraint_func, restraints in distance_restraints.items():
    print("Adding restraints with function: %s" % restraint_func)
    for rr, k in zip(*restraints):
        print(rr, k)
