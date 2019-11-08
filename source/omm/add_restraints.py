#!/usr/bin/env python

from configuration import *

from omm_tools import system_from_xml
from read_restraints import read_restraints

file_distance_restraints = input_prefix / "contacts.txt"
distance_restraints = read_restraints(file_distance_restraints, "distance")

#system = system_from_xml(system_file)

for restraint_func, restraints in distance_restraints.items():
    print("Adding restraints with function: %s" % restraint_func)
    for rr, k in zip(*restraints):
        print(rr, k)
