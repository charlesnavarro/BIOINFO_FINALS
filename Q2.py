# Import libraries
from Bio import pairwise2
from Bio import SeqIO
from Bio.Phylo.TreeConstruction import DistanceMatrix, DistanceTreeConstructor

# Define function readfile
def readSequence(filename):
    file = open(filename)
    sequence = SeqIO.read(file, "fasta")
    return sequence

def get_distance(alignment1, alignment2, score, begin, end):
    mismatch = 0
    match = 0
    gap = 0
    s = []
    s.append("%s\n" % alignment1)
    s.append(" " * begin)
    for a, b in zip(alignment1[begin:end], alignment2[begin:end]):
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
    s.append("%s\n" % alignment2)
    s.append("score=%g\n" % score)
    s.append("match=%g\n" % match)
    s.append("gap=%g\n" % gap)
    s.append("mismatch=%g\n" % mismatch)
    distance = mismatch / match
    return distance


constructor = DistanceTreeConstructor()

sequences = [readSequence("1-AY278489.2.fasta"), readSequence("2-AY394997.1.fasta"), readSequence("3-AY394978.1.fasta"),
             readSequence("4-AY278554.2.fasta"), readSequence("5-AY278741.1.fasta"), readSequence("6-AY274119.3.fasta"),
             readSequence("7-AY283794.1.fasta"), readSequence("8-AY291451.1.fasta"), readSequence("9-AY345986.1.fasta"),
             readSequence("10-AY394999.1.fasta"), readSequence("11-AY572034.1.fasta")]

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


