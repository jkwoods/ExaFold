#!/usr/bin/env python

"""
Small script to handle RMSD and TMscores and easily asses accuracy of folded proteins

TO RUN: python scores.py <original pdb file> <generated pdb file>

"""

import sys
import subprocess

#generate output file
subprocess.call(["./TMscore "+sys.argv[1]+" "+sys.argv[2]+" > TMoutput"], shell=True)


#read rmsd and tm
o = open("TMoutput", "r")

rmsd = ""
tm = ""

for line in o:
	if "RMSD of  the common residues=" in line: rmsd = line[33:38]
	if "TM-score    =" in line: tm = line[14:20]

o.close()

if (len(rmsd) == 0): rmsd = "err"
if (len(tm) == 0): tm = "err"

#write scores
s = open("scores_output", "w+")

s.write(sys.argv[2] + "	rmsd=" + rmsd + "	tm=" + tm + "")

s.close()
