#!/usr/bin/env python

"""Generates list of distance and torsion restraints
based on a folded, confirmed correct PDB file

"""
import sys
from itertools import combinations
import numpy as np
from simtk.openmm import app

__all__ = ["make_pdb_rst"]

def make_pdb_rst(orig_pdbfile, linear_pdbfile, dist_range=1.0, dist_force=70.0, tor_range=1.0, tor_force=70.0):

	# distance in sequence space
	_min_res_distance = 2

	# TODO not adequate for general case!
	is_protein = lambda res: res.name.lower() not in {"hoh","h2o","tip3"}

	# dict of {res #: (linear serial #, RCSB serial #)}
	serials_map = dict()
	rcsb_pdb = app.PDBFile(orig_pdbfile)
	linear_pdb = app.PDBFile(linear_pdbfile)

	# Because in case there are waters first, etc.
	#  - we are assuming the linear_pdb is ONLY protein
	#    AND every residue is present in the RCSB file
	custom_residue_index = -1
	for residue in linear_pdb.topology.residues():
		custom_residue_index += 1
		for atom in residue.atoms():
			if (atom.name.lower() == 'cb') or ((residue.name.lower() == 'gly') and (atom.name.lower() == 'ca')):
				serials_map.update({(residue.name, custom_residue_index): [atom.index]})

	custom_residue_index = -1
	for residue in rcsb_pdb.topology.residues():
		if is_protein(residue):
 			custom_residue_index += 1
			for atom in residue.atoms():
				if (atom.name.lower() == 'cb') or ((residue.name.lower() == 'gly') and (atom.name.lower() == 'ca')):
					try:
						serials_map[(residue.name, custom_residue_index)].append(atom.index)
					except KeyError:
						raise Exception("Mismatch detected between residue sequences")

	rcsb_positions = rcsb_pdb.positions
	linear_positions = linear_pdb.positions

   	dist_rst = dict()
	for (a1,i1), (a2,i2) in combinations(serials_map.items(), 2):

        	# Skip if have 'close neighbors'
        	if a2[1] - a1[1] <= _min_res_distance:
			continue

		r1 = rcsb_positions[i1[1]]
		r2 = rcsb_positions[i2[1]]
		d  = np.linalg.norm(r2 - r1)

		an1 = 'CB'
		an2 = 'CB'

		if (a1.name.lower() = 'gly'):
			an1 = 'CA'
		if (a2.name.lower() = 'gly'):
                        an2 = 'CA'
		if (i1 < i2):
			key = (i1, an1, i2, an2)
		else:
			key = (i2, an2, i1, an1)

		if (dist_rst[key] == None): dist_rst[key] = {'lower': (d._value - dist_range), 'upper': (d._value + dist_range), 'force': dist_force}        




	return (dist_rst, tor_rst)
