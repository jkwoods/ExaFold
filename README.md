# OpenMMPlayground

**To Run:**
1. Edit fold_parameters.json with your parameters (explaination below)
2. Run:
```
python set_up.py
```

**Input to the Program:  fold_parameters.json**
1. name of the protein (or run) as a string; this is just to identify output files, so you can really use any string you want
2. Jinbo Xu's txt file (input.seq) with the sequence in three letter chunks (i.e., "MET PHE ILE GLU ...")
3. Jinbo Xu's Distance Restraints list (contact.tbl)
4. Jinbo Xu's Torsion Restraints list (dihedral.tbl)
5. List of Force Constants for the distance restraints as floats (in kcal/mol·Angstroms)
6. List of Force Constants for the torsion restraints as floats (in in 70 kcal/mol·rad)
7. List of (highest) Temperatures for the simulated annealing cycles as floats (in K)
8. Number of simulated annealing cycles to run (int)
9. The path to the Amber forcefield, if you would like to change the forcefield; will vary depending on where your AmberTools package is

>The given example file has what I have found to be good defaults.


**Notes**
1. need to figure out Jinbo's other (bad python output) files
