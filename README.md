## ExaFold

Fast GPU-based protein folding simulations that run from only a protein sequence and set of restraints designed
to fold the protein.

**Pre-install**
If you do not have a suitable Python 3 installation, we recommend you use an Anaconda Python version.
Here is a lightweight version that will get you started:
```bash
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
rm Miniconda3-latest-Linux-x86_64.sh
```

**Install:**
```bash
git clone https://github.com/jkwoods/exafold
cd exafold
git checkout devel
# choose develop option if you want to
# make and test source changes
python setup.py [ install || develop ]
```

**Requirements:**
Python 3
Packages:
 - parse
 - OpenMM 7.3+
 - MDTraj 1.9.3+

**To Run:**
1. Run a test:
```bash
# from ExaFold top directory
cd tests
python run-test-omm_input.py
```
2. (incomplete) Edit `my_parameters.yaml` with your parameters in a working directory you set up (explaination below)
2.1. Run from structure + restraintlist
2.2. (incomplete) Run from protein sequence

**Input to the Program:**
1. From structure + restraint list
   - `my_parameters.yaml` with paths to structure, restraint files
2. From protein sequence
   - `my_parameters.yaml` with a protein sequence or fasta file

**Example API calls**
user configuration
exafold.mdsystem.ommsystem
exafold.restraints.reader
exafold.restraints.definitions

**Notes**
1. See previous repos and migrate relevant stuff

The code is currently under development. A full version will:
  - [partial] take a protein sequence for input via a config file
  - [partial] create a linear protein structure for this sequence
  - [outside] calculate distances used as restraints to help the protein fold correctly
  - [partial] calculate distances from secondary structure prediction
  - [v1 done] read a set of distance restraints
  - [v1 done] build a simulation system and apply restraints
  - [nostart] run a swarm of protein folding walkers
  - [nostart] prune and move walkers to more effectively fold the protein

Short-term Roadmap
v0.1  restraints are read and applied to an OpenMM system
v0.2  hook the sequence to PDB/restraints upstream
v0.x1 launches HPC job with swarm of folding walkers
v0.x2 prune and move walkers
v0.3  updates to config for more control of workflow
