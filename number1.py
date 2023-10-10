from Bio import pairwise2 
from Bio.Seq import Seq 
from Bio.pairwise2 import format_alignment

seq1 = Seq("AGCGGTTT")
seq2 = Seq("ACGT")

print("--- LOCAL ---")
for a in pairwise2.align.localxx(seq1, seq2):
    print(format_alignment(*a))

print("--- GLOBAL ---")
alignments = pairwise2.align.globalxx(seq1, seq2)

for g in alignments:
    print(format_alignment(*g))