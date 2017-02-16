#!/usr/bin/python3

# Author: Sari Sabban
# Email:  sari.sabban@gmail.com
# URL:    https://github.com/sarisabban
#
# Created By:   	Sari Sabban
# Created Date: 	17 February 2017

import re
import itertools
import numpy
import sys
from Bio.PDB import *

filename=sys.argv[1]				#file input from command line
						#_
p=PDBParser()					# |
structure=p.get_structure('X',filename)		# |Standard structure to setup biopython's DSSP to calculate SASA using Wilke constants
model=structure[0]				# |
dssp=DSSP(model,filename,acc_array='Wilke')	#_|

print('Found polar residues in core:')
reslist=list()
count=0
for x in dssp:					#Loop to isolate SASA for each amino acid
	if x[1]=='A':sasa=129*(x[3])
	elif x[1]=='V':sasa=174*(x[3])
	elif x[1]=='I':sasa=197*(x[3])
	elif x[1]=='L':sasa=201*(x[3])
	elif x[1]=='M':sasa=224*(x[3])
	elif x[1]=='P':sasa=159*(x[3])
	elif x[1]=='Y':sasa=263*(x[3])
	elif x[1]=='F':sasa=240*(x[3])
	elif x[1]=='W':sasa=285*(x[3])
	elif x[1]=='R':sasa=274*(x[3])
	elif x[1]=='N':sasa=195*(x[3])
	elif x[1]=='C':sasa=167*(x[3])
	elif x[1]=='Q':sasa=225*(x[3])
	elif x[1]=='E':sasa=223*(x[3])
	elif x[1]=='G':sasa=104*(x[3])
	elif x[1]=='H':sasa=224*(x[3])
	elif x[1]=='K':sasa=236*(x[3])
	elif x[1]=='S':sasa=155*(x[3])
	elif x[1]=='T':sasa=172*(x[3])
	elif x[1]=='D':sasa=193*(x[3])

#Calculate if polar amino acids are in core and print them
	if (x[2]=='G' or x[2]=='H' or x[2]=='I' or x[2]=='B' or x[2]=='E') and (x[1]=='D' or x[1]=='E' or x[1]=='K' or x[1]=='H' or x[1]=='R' or x[1]=='Q' or x[1]=='N' or x[1]=='S' or x[1]=='T' or x[1]=='C' or x[1]=='G') and sasa <= 15:
		print(x[0],x[1])
		count=count+1
		reslist.append(x[0])
	if (x[2]=='-' or x[2]=='T' or x[2]=='S') and (x[1]=='D' or x[1]=='E' or x[1]=='K' or x[1]=='H' or x[1]=='R' or x[1]=='Q' or x[1]=='N' or x[1]=='S' or x[1]=='T' or x[1]=='C' or x[1]=='G') and sasa <= 25:
		print(x[0],x[1])
		count=count+1
		reslist.append(x[0])

#Print results
print('-----------------')
print('Pymol command:')
print('select PolarCoreRes, resi','+'.join(str(x) for x in reslist))
print('-----------------')
print('Polar residues in core:',count)
