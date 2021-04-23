#! /usr/bin/env python3

import csv
import argparse
import re
from collections import defaultdict
from Bio import SeqIO
from Bio.Seq import Seq

#
#inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

# create an argument parser object
parser = argparse.ArgumentParser(description='this script will parse a GFF file and extract each feature from the genome')

# add positional arguments
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument("fasta", help='name of the FASTA file')

# parse the arguments
args = parser.parse_args()

# read in FASTA file
genome = SeqIO.read(args.fasta, 'fasta')
#print(genome.id)
#print(len(genome.seq))

# create a function that returns the reverse complement of features on the '-' strand
def rev_comp(mysequence, strand):
	if(strand == "-"):
		mysequence = mysequence.reverse_complement()
	return(mysequence)

# declare genes dictionary
CDS_dict = defaultdict(dict)

# read in GFF file
with open(args.gff, 'r') as gff_in:

	reader = csv.reader(gff_in, delimiter='\t')

	# loop over all the lines in our reader object (i.e., parsed file)
	for line in reader:
		start 	= line[3]
		end 	= line[4]
		strand 	= line[6]
		info	= line[8]
		gene 	= re.findall("Gene\s(.*?)\s",info)
		mysequence = genome.seq[(int(start)-1):int(end)]
		if (line[2] == "CDS"):
			if (CDS_dict[gene[0]] == {}):
				CDS_dict[gene[0]] = [strand, mysequence]
			else:
				CDS_dict[gene[0]].append(mysequence)

# this loops over the newly created dictionary to splice together coding sequences
# and then call the rev_comp function for relevant sequences
for line in CDS_dict:
	print(">Citrullus_lanatus_"+line)
	spacer = Seq("")
	spliced=str("")
	for seq in CDS_dict[line][1:]:
		spliced += seq
	CDS = rev_comp(spliced, CDS_dict[line][0])
	print(CDS)
	print()