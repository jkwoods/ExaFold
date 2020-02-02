#!/usr/bin/env python

from pathlib import Path

#-------- CONFIG Additional -----------------------#
# INPUTs
# - config file (yaml)
# - topo   file (prmtop)
system_name   = "1aki"

#--------- SETUP with Input Files------------------#
# Path Objects
#cwd         = __file__.path ## modulefile path
cwd           = Path.cwd()   ## runtime    path
input_prefix  = cwd / "1aki_example_input"
output_prefix = cwd / "omm_systems"
system_file   = output_prefix / ("system-%s.xml" % system_name)
restraint_prefix = cwd / "1aki_example_input"

if not output_prefix.is_dir():
    output_prefix.mkdir()

md_instructions = dict(
    n_steps = 100000,
    temperature = [300,600,300,600,300],
    fr_save = 5000,
    fn_traj = "trajectory.dcd",
    fn_state= "state.log",
)

