#!/usr/bin/env python

#########################################################################################################################
#                                                                                                                       #
#       PIPELINE - From Sequence to Folded Protein                                                                      #
#                                                                                                                       #
#       input: from linear_parameters.json file                                                                         #                                                               #
#                                                                                                                       #
#       output: AmberTools linear/parameters files                                                                      #
#                                                                                                                       #
#########################################################################################################################

import sys
import subprocess
import json
import numpy as np
import math


with open('fold_parameters.json') as json_file:
    data = json.load(json_file)
    name = data['name']
    fasta = data['fasta']
    distance_rst = data['distanceRstFile']
    distance_force = data['distanceForce']
    torsion_rst = data['angleRstFile']
    torsion_force = data['angleForce']
    temp = data['temp']
    annealing_runs = int(data['cycles'])
    mpi_prefix = data["mpi"]
    forcefield = data["forcefield"]


print("Reading Sequence ...")
#open and read FASTA
f = open(fasta, "r")
lines = f.readlines()
seq = ""
for l in lines:
        if (not (l.startswith(">") or l.startswith(";"))):
                seq = seq + l

f.close()

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

#generate Amber Tools helper file
subprocess.call('cp '+forcefield+' amberscript', shell=True)

h = open("amberscript", "a")

h.write("\n"+name+" = sequence "+triseq+"\nsaveoff "+name+" linear.lib\nsavepdb "+name+" linear.pdb\nsaveamberparm "+name+" prmtop rst7\nquit")

h.close()

print("Generating linear peptide ...")

#call Amber Tools tleap
subprocess.call('tleap -s -f amberscript', shell=True)

print("Amber paramaters and linear file generated")
