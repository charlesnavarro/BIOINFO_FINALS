from Bio import pairwise2
from Bio import SeqIO
from Bio.Phylo.TreeConstruction import DistanceMatrix, DistanceTreeConstructor

def readSequence(filename): #read sequence function
    file = open(filename)
    sequence = SeqIO.read(file, "fasta")
    return sequence

def get_distance(alignment1, alignment2, score, begin, end): #distance function
    match = 0
    mismatch = 0
    values = []
    values.append("%s\n" % alignment1)
    values.append(" " * begin)
    for a, b in zip(alignment1[begin:end], alignment2[begin:end]):
        if a == b:
            values.append("|")
            match = match + 1
        elif a == "-" or b == "-":
            values.append(" ")
        else:
            values.append(".")
            mismatch = mismatch + 1
    values.append("\n")
    values.append("%s\n" % alignment2)
    values.append("score=%f\n" % score)
    values.append("match=%d\n" % match)
    values.append("mismatch=%d\n" % mismatch)
    distance = mismatch / (match + mismatch)
    return distance


constructor = DistanceTreeConstructor()

virus = [readSequence("1-AY278489.2.fasta"), readSequence("2-AY394997.1.fasta"), readSequence("3-AY394978.1.fasta"), readSequence("4-AY278554.2.fasta"), readSequence("5-AY278741.1.fasta"), readSequence("6-AY274119.3.fasta"),readSequence("7-AY283794.1.fasta"), readSequence("8-AY291451.1.fasta"), readSequence("9-AY345986.1.fasta"), readSequence("10-AY394999.1.fasta"), readSequence("11-AY572034.1.fasta")]
names = ["Guangzhou (Dec 2002)", "Zhongshan", "Guangzhou (Jan 2003)", "Hong Kong (Feb 2003)", "Hanoi", "Toronto", "Singapore", "Taiwan", "Hong Kong (Mar 2003)", "Hong Kong (May 2003)", "Palm Civet"]

dMatrix = []

for x in range(0, 11):
    mList = []
    for y in range(0, 11):
        if x == y:
            mList.append(0)
        elif x > y:
            alignments = pairwise2.align.globalxx(virus[x], virus[y])
            max_mismatch = 0
            for z in alignments:
                curr_mismatch = get_distance(*z)
                if max_mismatch < curr_mismatch:
                    max_mismatch = curr_mismatch
            mList.append(max_mismatch)
    dMatrix.append(mList)

distanceMatrix = DistanceMatrix(names, dMatrix)
upgmaTree = constructor.upgma(distanceMatrix)
print(upgmaTree)