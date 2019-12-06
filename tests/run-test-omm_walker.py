#!/usr/bin/env python

from exafold import (
    OmmSystem, read_restraints, OMM_RESTRAIN_distance)

from test_configuration import (
    input_prefix, system_file, restraint_prefix)

from simtk import unit as u

#---------- READ OpenMM Base System ------------------------#
prmtop = input_prefix / "prmtop"
inpcrd = input_prefix / "rst7"
ommsystem = OmmSystem(ff_type="amber", topology=prmtop, coordinates=inpcrd,)

#---------- READ Restraints --------------------------------#
restraints = read_restraints(restraint_prefix / "contact.tbl", "distance")
[ri.append(2.0) for ri in restraints]

#---------- APPLY Restraints ------------------------------#
this_restraint = OMM_RESTRAIN_distance["simpleharmonic_customforce"]
restraint_type = list(this_restraint)[0]
ommsystem.initialize_restraint_force(this_restraint)
ommsystem.add_restraint_interactions(restraint_type, restraints[::10])

from exafold import Walker
#from test_configuration import md_instructions

walker = Walker()
#walker.set_instructions(md_instructions)
walker.generate_simulation(ommsystem)
walker.go()
