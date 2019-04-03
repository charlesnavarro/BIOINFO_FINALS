from pomegranate import *
from Bio.Seq import Seq

s = open("NC_001416.txt", "r")
if s.mode == 'r':
    sequence = Seq(s.read())

# arr = []
n = 0
p = 0
# src = sequence.reverse_complement()
# s_new = sequence + src
# aa = s_new.count_overlap("aa")
# ac = s_new.count_overlap("ac")
# at = s_new.count_overlap("at")
# ag = s_new.count_overlap("ag")
#
# ca = s_new.count_overlap("ca")
# cc = s_new.count_overlap("cc")
# ct = s_new.count_overlap("ct")
# cg = s_new.count_overlap("cg")
#
# ga = s_new.count_overlap("ga")
# gc = s_new.count_overlap("gc")
# gt = s_new.count_overlap("gt")
# gg = s_new.count_overlap("gg")
#
# ta = s_new.count_overlap("ta")
# tc = s_new.count_overlap("tc")
# tt = s_new.count_overlap("tt")
# tg = s_new.count_overlap("tg")

d1 = DiscreteDistribution({'A': 0.2462, 'C': 0.2476, 'G': 0.2985, 'T': 0.2077})
d2 = DiscreteDistribution({'A': 0.2700, 'C': 0.2084, 'G': 0.1981, 'T': 0.3236})

s1 = State(d1, name="cg")
s2 = State(d2, name="at")

model = HiddenMarkovModel(sequence)

model.add_states(s1, s2)
model.add_transition(model.start, s1, 0.5)
model.add_transition(model.start, s2, 0.5)
model.add_transition(s1, s1, 0.9998)
model.add_transition(s1, s2, 0.0002)
model.add_transition(s2, s2, 0.9998)
model.add_transition(s2, s1, 0.0002)
model.add_transition(s2, model.end, 0.5)
model.add_transition(s1, model.end, 0.5)
model.bake()

print(model.predict(sequence, algorithm='viterbi'))
for x in range(len(sequence)):
    # if(model.predict(sequence, algorithm='viterbi').pop(x) == 2):


    if(model.predict(sequence, algorithm='viterbi').pop(x) == 0):
        # print("at")
        # arr.append("at")
        n = n + 1
    if(model.predict(sequence, algorithm='viterbi').pop(x) == 1):
        # print("cg")
        # arr.append("cg")
        p = p + 1
    # if(model.predict(sequence, algorithm='viterbi').pop(x) == 3):

print(n)
print(p)
# example-start, s1, s2, s2, s2, s2, s2, s2, s2, s2, s2, s2, s2,
# print(model)
# model.viterbi(sequence)

