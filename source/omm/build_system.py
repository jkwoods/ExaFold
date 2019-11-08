#!/usr/bin/env python

from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *

from configuration import *

#--------- BUILD OpenMM System --------------------#
#import Amber files
prmtop = AmberPrmtopFile(input_prefix / "prmtop")
inpcrd = AmberInpcrdFile(input_prefix / "rst7")
system = prmtop.createSystem(nonbondedMethod=NoCutoff)

#--------- SAVE the system -----------------------#
with open(system_file, "w") as f:
    f.write(XmlSerializer.serialize(system))

