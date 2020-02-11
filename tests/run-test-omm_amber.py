#!/usr/bin/env python

from exafold import (Walker,
    OmmSystem, read_restraints, OMM_RESTRAIN_distance, linear_peptide)

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
restraints = read_restraints(restraint_prefix / "dist_made", "distance")
force_constant = 5.0 #this is actually a good range for whatever reason

#---------- APPLY Restraints -------------------------------#
this_restraint = OMM_RESTRAIN_distance["simpleharmonic_customforce"]
restraint_type = list(this_restraint)[0]
ommsystem.initialize_restraint_force(this_restraint)
ommsystem.add_restraint_interactions(restraint_type, restraints) #[::10]
ommsystem.apply_restraint_force(restraint_type)

#---------- BIND MD System to Walker -----------------------#
walker = Walker()
walker.generate_simulation(ommsystem)
walker.simulation.minimizeEnergy()

walker.configure_walk(md_instructions)
walker.go(force_constant)


