from pomegranate import *
from Bio.Seq import Seq
import plotly.plotly as py
import plotly.graph_objs as go
import plotly

plotly.tools.set_credentials_file(username='charles_navarro', api_key='5s3DWpySz6HJSxYS6WYr')

s = open("NC_001416.txt", "r")
if s.mode == 'r':
    sequence = Seq(s.read())

# # arr = []
# ctrAT = 0
# ctrCG = 0
# # src = sequence.reverse_complement()
# # s_new = sequence + src
# # aa = s_new.count_overlap("aa")
# # ac = s_new.count_overlap("ac")
# # at = s_new.count_overlap("at")
# # ag = s_new.count_overlap("ag")
# #
# # ca = s_new.count_overlap("ca")
# # cc = s_new.count_overlap("cc")
# # ct = s_new.count_overlap("ct")
# # cg = s_new.count_overlap("cg")
# #
# # ga = s_new.count_overlap("ga")
# # gc = s_new.count_overlap("gc")
# # gt = s_new.count_overlap("gt")
# # gg = s_new.count_overlap("gg")
# #
# # ta = s_new.count_overlap("ta")
# # tc = s_new.count_overlap("tc")
# # tt = s_new.count_overlap("tt")
# # tg = s_new.count_overlap("tg")

#alphabet of symbols that are observed (initializing values of ACGT)
d1 = DiscreteDistribution({'A': 0.2462, 'C': 0.2476, 'G': 0.2985, 'T': 0.2077})
d2 = DiscreteDistribution({'A': 0.2700, 'C': 0.2084, 'G': 0.1981, 'T': 0.3236})

#adding the values to the state
s1 = State(d1, name="cg")
s2 = State(d2, name="at")

#initialize the HMM
model = HiddenMarkovModel(sequence)

#initialize the transition states
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

viterbipath = model.predict(sequence, algorithm='viterbi')
print(viterbipath)


trace1 = go.Bar(
    y=['viterbi'],
    x=[176],
    name='CG',
    orientation = 'h',
    marker = dict(
        color = 'rgba(61, 122, 245, 1)',
        line = dict(
            color = 'rgba(61, 122, 245, 1)',
            width = 3)
    )
)
trace2 = go.Bar(
    y=['viterbi'],
    x=[22323],
    name='AT',
    orientation = 'h',
    marker = dict(
        color = 'rgba(228, 12, 12, 1)',
        line = dict(
            color = 'rgba(228, 12, 12, 1)',
            width = 3)
    )
)
trace3 = go.Bar(
    y=['viterbi'],
    x=[8725],
    name='CG',
    orientation = 'h',
    marker = dict(
        color = 'rgba(61, 122, 245, 1)',
        line = dict(
            color = 'rgba(61, 122, 245, 1)',
            width = 3)
    )
)

trace4 = go.Bar(
    y=['viterbi'],
    x=[1962],
    name='AT',
    orientation = 'h',
    marker = dict(
        color = 'rgba(228, 12, 12, 1)',
        line = dict(
            color = 'rgba(228, 12, 12, 1)',
            width = 3)
    )
)

trace5 = go.Bar(
    y=['viterbi'],
    x=[5179],
    name='CG',
    orientation = 'h',
    marker = dict(
        color = 'rgba(61, 122, 245, 1)',
        line = dict(
            color = 'rgba(61, 122, 245, 1)',
            width = 3)
    )
)

trace6 = go.Bar(
    y=['viterbi'],
    x=[8128],
    name='AT',
    orientation = 'h',
    marker = dict(
        color = 'rgba(228, 12, 12, 1)',
        line = dict(
            color = 'rgba(228, 12, 12, 1)',
            width = 3)
    )
)

trace7 = go.Bar(
    y=['viterbi'],
    x=[2009],
    name='CG',
    orientation = 'h',
    marker = dict(
        color = 'rgba(61, 122, 245, 1)',
        line = dict(
            color = 'rgba(61, 122, 245, 1)',
            width = 3)
    )
)

data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7]
layout = go.Layout(
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='viterbi')


