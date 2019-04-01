import pomegranate

s = open("NC_001416.txt", "r")
if s.mode == 'r':
    sequence = (s.read())

d1 = pomegranate.DiscreteDistribution({'A': 0.2462, 'C': 0.2476, 'G': 0.2985, 'T': 0.2077})
d2 = pomegranate.DiscreteDistribution({'A': 0.2700, 'C': 0.2084, 'G': 0.1981, 'T': 0.3236})

s1 = pomegranate.State(d1, name="cg")
s2 = pomegranate.State(d2, name="at")

model = pomegranate.HiddenMarkovModel()

model.add_states(s1, s2)
model.add_transition(model.start, s1, 1.0)
model.add_transition(s1, s1, 0.9998)
model.add_transition(s1, s2, 0.3)
model.add_transition(s2, s2, 0.9998)
model.add_transition(s2, s1, 0.2)
model.add_transition(s2, model.end, 0.1)
model.bake()

print(model)
#viterbi(sequence)
