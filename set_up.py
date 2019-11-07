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
    fasta = data['fasta']
    distance_rst = data['distanceRstFile']
    distance_force = data['distanceForce']
    torsion_rst = data['angleRstFile']
    torsion_force = data['angleForce']
    temp = data['temp']
    annealing_runs = int(data['cycles'])
    forcefield = data["forcefield"]

#open and read FASTA
with open(fasta) as f:
    lines = f.readlines()
    seq = ""
    for l in lines:
            if (not (l.startswith(">") or l.startswith(";"))):
                    seq = seq + l

seq = seq.replace("\n", "") #clean

print(seq)

#generate sequence of triples
def tri(x):
        return {
                'A': 'ALA',
                'R': 'ARG',
                'N': 'ASN',
                'D': 'ASP',
                'C': 'CYS',
                'Q': 'GLN',
                'E': 'GLU',
                'G': 'GLY',
                'H': 'HIS',
                'I': 'ILE',
                'L': 'LEU',
                'K': 'LYS',
                'M': 'MET',
                'F': 'PHE',
                'P': 'PRO',
                'S': 'SER',
                'T': 'THR',
                'W': 'TRP',
                'Y': 'TYR',
                'V': 'VAL'
        }.get(x, '')

triseq = "{ "
for s in seq:
        triseq = triseq + tri(s) + " "
triseq = triseq + "}"

print("Sequence is: "+ str(triseq))

#generate Amber Tools helper file - tleap will not run unless everything is copied into the forcefield file
subprocess.call('cp '+forcefield+' amberscript', shell=True)

h = open("amberscript", "a")

h.write("\n"+name+" = sequence "+triseq+"\nsaveoff "+name+" linear.lib\nsavepdb "+name+" linear.pdb\nsaveamberparm "+name+" prmtop rst7\nquit")

h.close()

#call Amber Tools tleap
subprocess.call('tleap -s -f amberscript', shell=True)

print("Amber paramaters and linear file generated")
