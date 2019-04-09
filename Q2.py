# Import libraries
from Bio import pairwise2
from Bio import SeqIO
from Bio.Phylo.TreeConstruction import DistanceMatrix, DistanceTreeConstructor


# Define function readfile
def readfile(filename):
    file = open(filename)
    sequence = SeqIO.read(file, "fasta")

    return sequence


def get_distance(align1, align2, score, begin, end):
    mismatch = 0
    match = 0
    gap = 0
    s = []
    s.append("%s\n" % align1)
    s.append(" " * begin)
    for a, b in zip(align1[begin:end], align2[begin:end]):
        if a == b:
            s.append("|")  # match
            match = match + 1
        elif a == "-" or b == "-":
            s.append(" ")  # gap
            gap = gap + 11
        else:
            s.append(".")  # mismatch
            mismatch = mismatch + 1
    s.append("\n")
    s.append("%s\n" % align2)
    s.append("Score=%g\n" % score)
    s.append("Match=%g\n" % match)
    s.append("Gap=%g\n" % gap)
    s.append("Mismatch=%g\n" % mismatch)
    distance = mismatch / match
    return distance


constructor = DistanceTreeConstructor()
sequences = [readfile("1-AY278489.2.fasta"), readfile("2-AY394997.1.fasta"), readfile("3-AY394978.1.fasta"),
             readfile("4-AY278554.2.fasta"), readfile("5-AY278741.1.fasta"), readfile("6-AY274119.3.fasta"),
             readfile("7-AY283794.1.fasta"), readfile("8-AY291451.1.fasta"), readfile("9-AY345986.1.fasta"),
             readfile("10-AY394999.1.fasta"), readfile("11-AY572034.1.fasta")]

names = ["Guangzhou", "Zhongshan", "Guangzhou2", "Hong Kong", "Hanoi", "Toronto", "Singapore", "Taiwan", "Hong Kong 2", "Hong Kong 3", "Palm Civet"]

distanceMatrix = []

for x in range(0, 11):
    oneList = []
    for y in range(0, 11):
        if x == y:
            oneList.append(0)
        elif x > y:
            alignments = pairwise2.align.globalxx(sequences[x], sequences[y])
            max_mismatch = 0
            for aln in alignments:
                curr_mismatch = get_distance(*aln)
                if max_mismatch < curr_mismatch:
                    max_mismatch = curr_mismatch
            oneList.append(max_mismatch)
    distanceMatrix.append(oneList)

dMatrix = DistanceMatrix(names, distanceMatrix)
upgmaTree = constructor.upgma(dMatrix)
print(upgmaTree)


