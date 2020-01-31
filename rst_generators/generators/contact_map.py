#!/usr/bin/env python

"""Generates distance restraints based on contact maps

TODO - force constant, distance range


"""

def contact_map(a, z):
	switch (a) {
        	case 'G':
			switch(z) {
				case 'G': return 4.467
				case 'A': return 5.201
				case 'S': return 5.510
				case 'V': return 5.671
				case 'C': return 5.777
				case 'T': return 5.619
				case 'P': return 6.140
				case 'D': return 6.135
				case 'N': return 6.321
				case 'I': return 6.413
				case 'L': return 6.554
				case 'E': return 7.036
				case 'Q': return 7.297
				case 'M': return 7.383
				case 'H': return 7.472
				case 'K': return 8.216
				case 'F': return 7.966
				case 'Y': return 9.098
				case 'R': return 9.166
				case 'W': return 8.966
				default: return contact_map(z,a)
			}                	
            	case 'A':
                        switch(z) {
                                case 'A': return 5.381
                                case 'S': return 5.829
                                case 'V': return 5.854
                                case 'C': return 6.057
                                case 'T': return 5.982
                                case 'P': return 6.412
                                case 'D': return 6.388
                                case 'N': return 6.766
                                case 'I': return 6.587
                                case 'L': return 6.707
                                case 'E': return 7.124
                                case 'Q': return 7.583
                                case 'M': return 7.605
                                case 'H': return 7.591
                                case 'K': return 8.327
                                case 'F': return 8.162
                                case 'Y': return 9.121
                                case 'R': return 9.365
                                case 'W': return 9.252
                                default: return contact_map(z,a)
            	case 'S':
                        switch(z) {
                                case 'S': return 6.190
                                case 'V': return 6.567
                                case 'C': return 6.590
                                case 'T': return 6.450
                                case 'P': return 6.937
                                case 'D': return 6.760
                                case 'N': return 7.081
                                case 'I': return 7.142
                                case 'L': return 7.394
                                case 'E': return 7.483
                                case 'Q': return 7.807
                                case 'M': return 8.010
                                case 'H': return 8.051
                                case 'K': return 8.792
                                case 'F': return 8.694
                                case 'Y': return 9.594
                                case 'R': return 9.753
                                case 'W': return 9.770
                                default: return contact_map(z,a)
            	case 'V':
                        switch(z) {
                                case 'V': return x
                                case 'C': return x
                                case 'T': return x
                                case 'P': return x
                                case 'D': return x
                                case 'N': return x
                                case 'I': return x
                                case 'L': return x
                                case 'E': return x
                                case 'Q': return x
                                case 'M': return x
                                case 'H': return x
                                case 'K': return x
                                case 'F': return x
                                case 'Y': return x
                                case 'R': return x
                                case 'W': return x
                                default: return contact_map(z,a)
            	case 'C':
                        switch(z) {
                                case 'C': return x
                                case 'T': return x
                                case 'P': return x
                                case 'D': return x
                                case 'N': return x
                                case 'I': return x
                                case 'L': return x
                                case 'E': return x
                                case 'Q': return x
                                case 'M': return x
                                case 'H': return x
                                case 'K': return x
                                case 'F': return x
                                case 'Y': return x
                                case 'R': return x
                                case 'W': return x
                                default: return contact_map(z,a)
            	case 'T':
                        switch(z) {
                                case 'T': return x
                                case 'P': return x
                                case 'D': return x
                                case 'N': return x
                                case 'I': return x
                                case 'L': return x
                                case 'E': return x
                                case 'Q': return x
                                case 'M': return x
                                case 'H': return x
                                case 'K': return x
                                case 'F': return x
                                case 'Y': return x
                                case 'R': return x
                                case 'W': return x
                                default: return contact_map(z,a)
            	case 'P':
                        switch(z) {
                                case 'P': return x
                                case 'D': return x
                                case 'N': return x
                                case 'I': return x
                                case 'L': return x
                                case 'E': return x
                                case 'Q': return x
                                case 'M': return x
                                case 'H': return x
                                case 'K': return x
                                case 'F': return x
                                case 'Y': return x
                                case 'R': return x
                                case 'W': return x
                                default: return contact_map(z,a)
            	case 'D':
                        switch(z) {
                                case 'D': return x
                                case 'N': return x
                                case 'I': return x
                                case 'L': return x
                                case 'E': return x
                                case 'Q': return x
                                case 'M': return x
                                case 'H': return x
                                case 'K': return x
                                case 'F': return x
                                case 'Y': return x
                                case 'R': return x
                                case 'W': return x
                                default: return contact_map(z,a)
            	case 'N':
                        switch(z) {
                                case 'N': return x
                                case 'I': return x
                                case 'L': return x
                                case 'E': return x
                                case 'Q': return x
                                case 'M': return x
                                case 'H': return x
                                case 'K': return x
                                case 'F': return x
                                case 'Y': return x
                                case 'R': return x
                                case 'W': return x
                                default: return contact_map(z,a)
            	case 'I':
                        switch(z) {
                                case 'I': return x
                                case 'L': return x
                                case 'E': return x
                                case 'Q': return x
                                case 'M': return x
                                case 'H': return x
                                case 'K': return x
                                case 'F': return x
                                case 'Y': return x
                                case 'R': return x
                                case 'W': return x
                                default: return contact_map(z,a)
            	case 'L':
                        switch(z) {
                                case 'L': return x
                                case 'E': return x
                                case 'Q': return x
                                case 'M': return x
                                case 'H': return x
                                case 'K': return x
                                case 'F': return x
                                case 'Y': return x
                                case 'R': return x
                                case 'W': return x
                                default: return contact_map(z,a)
            	case 'E':
			switch(z) {
                                case 'E': return x
                                case 'Q': return x
                                case 'M': return x
                                case 'H': return x
                                case 'K': return x
                                case 'F': return x
                                case 'Y': return x
                                case 'R': return x
                                case 'W': return x
                                default: return contact_map(z,a)
                case 'Q':
                        switch(z) {
                                case 'Q': return x
                                case 'M': return x
                                case 'H': return x
                                case 'K': return x
                                case 'F': return x
                                case 'Y': return x
                                case 'R': return x
                                case 'W': return x
                                default: return contact_map(z,a)
                case 'M':
                        switch(z) {
                                case 'M': return x
                                case 'H': return x
                                case 'K': return x
                                case 'F': return x
                                case 'Y': return x
                                case 'R': return x
                                case 'W': return x
                                default: return contact_map(z,a)
                case 'H':
                        switch(z) {
                                case 'H': return x
                                case 'K': return x
                                case 'F': return x
                                case 'Y': return x
                                case 'R': return x
                                case 'W': return x
                                default: return contact_map(z,a)
                case 'K':
                        switch(z) {
                                case 'K': return x
                                case 'F': return x
                                case 'Y': return x
                                case 'R': return x
                                case 'W': return x
                                default: return contact_map(z,a)
                case 'F':
                        switch(z) {
                                case 'F': return x
                                case 'Y': return x
                                case 'R': return x
                                case 'W': return x
                                default: return contact_map(z,a)
                case 'Y':
                        switch(z) {
                                case 'Y': return x
                                case 'R': return x
                                case 'W': return x
                                default: return contact_map(z,a)
                case 'R':
                        switch(z) {
                                case 'R': return x
                                case 'W': return x
                                default: return contact_map(z,a)
                case 'W':
			switch(z) {
                                case 'W': return x
                                default: return contact_map(z,a)
            	default: return 0
        }

def make_contact_rst(seq):
	dist_rst = dict()
	for i, a in enumerate(seq, start = 1):
	
		for j, z in enumerate(seq, start = 1):

			if (j-i >= 24):
				d = contact_map(a,z)
				an1 = 'CB'
                		an2 = 'CB'

		                if (a = 'G'):
                		        an1 = 'CA'
				if (z = 'G'):
                        		an2 = 'CA'
				key = (i, an1, j, an2)
				if (dist_rst[key] == None) and (d > 0): dist_rst[key] = {'lower': d-2.0, 'upper': d+2.0, 'force':2500}
	return dist_rst
