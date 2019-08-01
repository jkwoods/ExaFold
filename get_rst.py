#!/usr/bin/env python

import sys
import Bio.PDB
import numpy as np
import math

#INPUT: 1. name of orig
#	2. name of linear (-pdb)
#	3. dist k

#ang_kforce = float(sys.argv[2])
dist_kforce = float(sys.argv[3])

d = open("test.txt", "w+")
#a = open("5col.angles", "w+")

linear_serials = {} # dict of {res #: linear serial number for cb atom}
for model in Bio.PDB.PDBParser().get_structure(sys.argv[2], sys.argv[2] + ".pdb"):
    for chain in model:
        for seqnum, res in enumerate(chain, start=1):
            try:
                cbatom = res['CB']
                linear_serials.update({seqnum : cbatom.get_serial_number()})
            except KeyError:
                continue

#print(linear_serials)


for model in Bio.PDB.PDBParser().get_structure(sys.argv[1], sys.argv[1] + ".pdb"):
    for chain in model :
        
        ## phi psi
#        for res in chain[:-1]: #not the last one
#            atom1 =
#            atom2 =
#            atom3 =
#            atom4 =
#            vector1 = atom1.get_vector()
#            vector2 = atom2.get_vector()
#            vector3 = atom3.get_vector()
#            vector4 = atom4.get_vector()
#            torsion = calc_dihedral(vector1, vector2, vector3, vector4)
#            d.write("%i    %i    %i	%i	%.1f    %.1f\n" % (atom1.serial_number, atom2.serial_number, atom3.serial_number, atom4.serial_number, torsion, ang_kforce))

	
        ## CB distance
        no_dupes = []
        for seqnum1, res1 in enumerate(chain, start=1):
            for seqnum2, res2 in enumerate(chain, start=1):
                if res1 != res2:
                    try:    
                        atom1 = res1['N']
                        atom2 = res2['N']
                        distance = atom1 - atom2
                        if not ((atom2, atom1) in no_dupes) or ((atom1, atom2) in no_dupes):
#                            atom1_index = linear_serials.get(seqnum1) -1 #openmm indexs atoms at 0, pdb files index at 1
#                            atom2_index = linear_serials.get(seqnum2) -1

#                            print("atom1="+str(atom1_index)+"	atom2="+str(atom2_index))


                            d.write("%i    %i    %.1f    %.1f\n" % (res1.id[1], res2.id[1], distance, dist_kforce))
                            no_dupes.append((atom1, atom2))
                    except KeyError:
                        #no CB atom (GLY)
                       # d.write("%i    %i    %.1f    %.1f\n" % (res1.id[1], res2.id[1], 0.0, 0.0)) #this will be "exempted" in wrapper
                        continue

    break


#a.close()
d.close()
