#!/usr/bin/env python

from exafold import (Walker,
    OmmSystem, read_restraints, OMM_RESTRAIN_distance)

from test_configuration import (
    input_prefix, system_file, restraint_prefix,
    md_instructions)

from simtk import unit as u

#---------- READ OpenMM Base System ------------------------#
prmtop = input_prefix / "prmtop"
inpcrd = input_prefix / "rst7"
ommsystem = OmmSystem(ff_type="amber", topology=prmtop, coordinates=inpcrd,)

#---------- READ Restraints --------------------------------#
restraints = read_restraints(restraint_prefix / "contact.tbl", "distance")
[ri.append(50) for ri in restraints]

#---------- APPLY Restraints -------------------------------#
this_restraint = OMM_RESTRAIN_distance["simpleharmonic_customforce"]
restraint_type = list(this_restraint)[0]
ommsystem.initialize_restraint_force(this_restraint)
ommsystem.add_restraint_interactions(restraint_type, restraints[::10])

#---------- BIND MD System to Walker -----------------------#
walker = Walker()
walker.generate_simulation(ommsystem)
walker.simulation.minimizeEnergy()

walker.configure_walk(md_instructions)
walker.go()



