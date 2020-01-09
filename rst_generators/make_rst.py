#!/usr/bin/env python

"""Makes distance and torsion restraints files of user-specified type


"""

from generators import *

def incorporate(part, main_dict):
	for k in part:
		if main_dict[k] == None: main_dict[k] = part[k]

	return main_dict


def make_restraints(secondary_structure=False, contact_map=False, original_pdb=False, struc_seq="", dist_file="distance_restraints", tor_file="torsion_restraints"):
	dist_rst = dict();
	tor_rst = dict();

	#TODO - get Fasta

	if (original_pdb):
		o_dist, o_tor = make_pdb_rst(70.0, 1.0, 70.0, 1.0);
                dist_rst = incorporate(o_dist, dist_rst)
                tor_rst = incorporate(o_tor, tor_rst)

	if (secondary_structure):
		s_dist, s_tor = make_sec_struc_rst(seq, struc_seq);
		dist_rst = incorporate(s_dist, dist_rst)
		tor_rst = incorporate(s_tor, tor_rst)

	if (contact_map):
                c_dist, c_tor = make_contact_rst();
                dist_rst = incorporate(c_dist, dist_rst)
                tor_rst = incorporate(c_tor, tor_rst)

d = open(dist_file, "w+")
for k in dist_rst:
	d.write(); #TODO

d.close()

t = open(tor_file, "w+")
for k in tor_rst:
        t.write(); #TODO

t.close()

