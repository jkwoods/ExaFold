#!/usr/bin/env python

"""Generates distance and torsion restraints based on
secondary structure predictions as determined by MELD

Functions
_________
four_of_five :: true if >= 4/5 of the slots match the test case

tri ::
	helper function to convert single letter amino acid
	sequence to 3-letter sequence

make_sec_struc_rst ::
	takes in a single-letter amino acid sequence and a secondary
	structure prediction sequence of 'H' (helix), 'E' (sheets),
	and 'C' (coils) from PSIPRED or RaptorX prediction

"""

#TODO correct force constant

import sys

__all__ = ["four_of_five", "tri", "make_sec_struc_rst"]

def four_of_five(a, b, c, d, e, test):
    if (test == a) and (test == b) and (test == c) and (test == d):
        return True
    elif (test == a) and (test == b) and (test == c) and (test == e):
        return True
    elif (test == a) and (test == b) and (test == d) and (test == e):
        return True
    elif (test == a) and (test == c) and (test == d) and (test == e):
        return True
    elif (test == b) and (test == c) and (test == d) and (test == e):
        return True
    else:
        return False

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

def make_sec_struc_rst(seq, struc_seq):
	helix = 'H'
	sheet = 'E'
	tracker = dict()
	dist_rst = dict()
	tor_rst = dict()

	for s in range(0, len(seq)):
		tracker[s] = {'helix': 0, 'sheet': 0}

	if (len(seq) != len(struc_seq)):
		sys.exit("Error: sequence length and prediction string length do not match!")
		
	for i in range(0, len(seq)-4):
		a = struc_seq[i]
		b = struc_seq[i+1]
		c = struc_seq[i+2]
		d = struc_seq[i+3]
		e = struc_seq[i+4]
	
		if four_of_five(a,b,c,d,e,helix):
			for c in range(0, 5):
				tracker[i+c]['helix'] += 1

			#distance restraints a&d, b&e, a&e CA atoms
			key = (i+1, 'CA', i+4, 'CA')
			if (dist_rst[key] == None): dist_rst[key] = {'lower': 4.85, 'upper': 5.61, 'force':2500}			
                        key = (i+2, 'CA', i+5, 'CA')                        
			if (dist_rst[key] == None): dist_rst[key] = {'lower': 4.85, 'upper': 5.61, 'force':2500}
                        key = (i+1, 'CA', i+5, 'CA')
			if (dist_rst[key] == None): dist_rst[key] = {'lower': 5.81, 'upper': 6.84, 'force':2500}

			#"phi" applied to b-e
			for j in range(i+1, i+5):
				key = (j+1, 'PHI')
				if (tor_rst[key] == None): tor_rst[key] = {'lower': -80, 'upper': -45, 'force': 2.5}

			#"psi" applied to a-d
                        for j in range(i, i+4):
                                key = (j+1, 'PSI')
                                if (tor_rst[key] == None): tor_rst[key] = {'lower': -60, 'upper': -25, 'force': 2.5}

		elif four_of_five(a,b,c,d,e,sheet):
			for c in range(0, 5):
                                tracker[i+c]['sheet'] += 1

			#distance restraints a&d, b&e, a&e CA atoms
			key = (i+1, 'CA', i+4, 'CA')
                        if (dist_rst[key] == None): dist_rst[key] = {'lower': 7.85, 'upper': 10.63, 'force':2500}
                        key = (i+2, 'CA', i+5, 'CA')
                        if (dist_rst[key] == None): dist_rst[key] = {'lower': 7.85, 'upper': 10.63, 'force':2500}
                        key = (i+1, 'CA', i+5, 'CA')
                        if (dist_rst[key] == None): dist_rst[key] = {'lower': 10.86, 'upper': 13.94, 'force':2500}

                        #"phi" applied to b-e
                        for j in range(i+1, i+5):
                                key = (j+1, 'PHI')
                                if (tor_rst[key] == None): tor_rst[key] = {'lower': 90, 'upper': 145, 'force': 2.5}

                        #"psi" applied to a-d
                        for j in range(i, i+4):
                                key = (j+1, 'PSI')
                                if (tor_rst[key] == None): tor_rst[key] = {'lower': 120, 'upper': 170, 'force': 2.5}

	for j in range(0, len(seq)):
    		if (tracker[j][helix] > 0) and (tracker[j][sheet] > 0):
		#if an amino acid is being treated as both, eliminate all of its restraints	
			print("Warning: Residue %i is recognized as both a helix and a sheet. All restraints for residue %i being removed") % (j+1, j+1)
			for k in dist_rst:
				if i in k: my_dict.pop(k, None)
			for k in tor_rst:
				if i in k: my_dict.pop(k, None)


	return (dist_rst, tor_rst)
