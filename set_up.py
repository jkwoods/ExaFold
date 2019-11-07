#!/usr/bin/env python

#########################################################################################################################
#                                                                                                                       #
#       Sequence to Amber Linear pdb                                                                                    #
#                                                                                                                       #
#       input: from fold_parameters.json file                                                                           #                                                               #
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
    distance_rst = data['distanceRstFile']
    #distance_force = data['distanceForce']
    torsion_rst = data['angleRstFile']
    #torsion_force = data['angleForce']
    #temp = data['temp']
    #annealing_runs = int(data['cycles'])
    forcefield = data["forcefield"] #i've copied in ff14SB to the repo, bc otherwise hard to find on cades vs personal computers. Its Amber's proclaimed "best for protiens" forcefeild

#open and read Jinbo input
with open(input_seq) as f:
    lines = f.readlines()
    seq = ""
    for l in lines:
        seq = seq + l

seq = seq.replace("\n", "") #clean
triseq = "{ "+ seq + "}"
print("Sequence is: "+ str(triseq))

#generate Amber Tools helper file - tleap will not run unless commands are copied into the forcefield file
subprocess.call('cp '+forcefield+' amberscript', shell=True)
h = open("amberscript", "a")
h.write("\n"+name+" = sequence "+triseq+"\nsaveoff "+name+" linear.lib\nsavepdb "+name+" linear.pdb\nsaveamberparm "+name+" prmtop rst7\nquit")
h.close()

#call Amber Tools tleap
subprocess.call('tleap -s -f amberscript', shell=True)

print("Amber paramaters and linear file generated")


#preliminary parsing of Jinbo's rst files - you can change this however is needed for openmm

seq_array = seq.split(" ")
for s in seq_array:
    if(s==""): seq_array.remove(s)

with open(distance_rst) as f:
    for line in f:
        columns = line.split()
        
	#some of this (esp atom names) might have to be done differently
        res1_id = int(columns[2])
        res1_name = seq_array[res1_id-1]
        atom1_name = columns[5][:-1]
        atom1_name = atom1_name.upper()

        res2_id = int(columns[7])
        res2_name = seq_array[res2_id-1]
        atom2_name = columns[10][:-1]
        atom2_name = atom2_name.upper()
        #print("res1_id="+str(res1_id)+" res1_name="+str(res1_name)+" atom1_name="+str(atom1_name)+" res2_id="+str(res2_id)+" res2_name="+str(res2_name)+" atom2_name="+str(atom2_name))

        ave_dist = float(columns[11])
        dminus = float(columns[12])
        dplus = float(columns[13])

        dlower = ave_dist - dminus #lower bound
        dupper = ave_dist + dplus #upper bound

        #d.write("%i    %s    %s    %i    %s    %s    %.2f    %.2f\n" % (res1_id, res1_name, atom1_name, res2_id, res2_name, atom2_name, dlower,dupper))

        
with open(torsion_rst) as f:
    for line in f:
        columns = line.split()

        #completely different stuff here for openmm
        
        angle = float(columns[22])
        arange = float(columns[23])

        alower = angle - arange #lower bound
        aupper = angle + arange #upper bound

        # "exponent" for jx is always 2 - pretty sure that correlates to built in ^2 in harmonic force in amber and openmm

        #a.write("%i    %s    %s    %.1f    %.1f\n" % (res_id, res_name, phi_psi, alower, aupper))



