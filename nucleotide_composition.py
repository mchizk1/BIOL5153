#!/usr/bin/env python3
# coding=UTF-8

# set the name of input DNA sequence file
filename = '/home/mason/Desktop/watermelon_files/nt/nad4L.fasta'

# getting rid of the fasta label
with open(filename, 'r') as f:
    for line in f.readlines():
        if '>' not in line:
        	dna_sequence = line

# close the file
#infile.close()

# print the dna sequence
# print(dna_sequence)

seqlen = len(dna_sequence)
freqA = round(dna_sequence.count('A')/seqlen, 3)
freqC = round(dna_sequence.count('C')/seqlen, 3)
freqG = round(dna_sequence.count('G')/seqlen, 3)
freqT = round(dna_sequence.count('T')/seqlen, 3)
GC = round(freqG+freqC ,3)

print("Sequence length", seqlen)
print()
print("Freq of A:", freqA)
print()
print("Freq of C:", freqC)
print()
print("Freq of G:", freqG)
print()
print("Freq of T:", freqT)
print()
print("G+C content:", GC)

#This part check that all frequencies add up to 1
#however, the sum is actually 0.997 due to rounding error
check = round(freqA+freqC+freqG+freqT,3)
#print("The sum of all freqencies is",check)

# This section writes the desired output to an undefined output file
#outfile = 
#outfile.write('Sequence length:' + str(seqlen))
#outfile.write("Freq of A:", str(freqA) + '\n')
#outfile.write("Freq of C:", str(freqA) + '\n')
#outfile.write("Freq of G:", str(freqA) + '\n')
#outfile.write("Freq of T:", str(freqA) + '\n')
#outfile.write("G+C content:", str(freqA) + '\n')



