#!/usr/bin/env python

#########################################################################################################################
#                                                                                                                       #
#       Sequence to Amber Linear pdb                                                                                    #
#                                                                                                                       #
#       input: from fold_parameters.json file                                                                         #                                                               #
#                                                                                                                       #
#       output: AmberTools linear/parameters files                                                                      #
#                                                                                                                       #
#########################################################################################################################

import sys
import subprocess
import json
import numpy as np

with open('fold_parameters.json') as json_file: #left some currently unused restraints in case we want to use later
    data = json.load(json_file)
    name = data['name']
    input_seq = data['input_seq']
    #distance_rst = data['distanceRstFile']
    #distance_force = data['distanceForce']
    #torsion_rst = data['angleRstFile']
    #torsion_force = data['angleForce']
    #temp = data['temp']
    #annealing_runs = int(data['cycles'])
    forcefield = data["forcefield"] #i've copied in ff14SB to the repo, bc otherwise hard to find on cades vs personal computers. Its Amber's proclaimed "best for protiens" forcefeild

#open and read FASTA
with open(input_seq) as f:
    lines = f.readlines()
    seq = ""
    for l in lines:
        seq = seq + l

seq = seq.replace("\n", "") #clean

triseq = "{ "+ seq + "}"

print("Sequence is: "+ str(triseq))

#generate Amber Tools helper file - tleap will not run unless everything is copied into the forcefield file
subprocess.call('cp '+forcefield+' amberscript', shell=True)

h = open("amberscript", "a")

h.write("\n"+name+" = sequence "+triseq+"\nsaveoff "+name+" linear.lib\nsavepdb "+name+" linear.pdb\nsaveamberparm "+name+" prmtop rst7\nquit")

h.close()

#call Amber Tools tleap
subprocess.call('tleap -s -f amberscript', shell=True)

print("Amber paramaters and linear file generated")
