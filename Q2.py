#BIOINFO HW2

from Bio.Seq import Seq
f = open("NC_001416.txt", "r")
if f.mode == 'r':
    s = Seq(f.read()).lower()
    print(s)

for y in range(10):
    ctr1 = y + 1
    src = s.reverse_complement().lower()
    s_new = s + src
    print('reverse complement is %s' % s.reverse_complement())

    aa = 0
    ac = 0
    at = 0
    ag = 0

    ca = 0
    cc = 0
    ct = 0
    cg = 0

    ga = 0
    gc = 0
    gt = 0
    gg = 0

    ta = 0
    tc = 0
    tt = 0
    tg = 0

    ccgg = 0
    agct = 0
    gatc = 0
    catg = 0
    acgt = 0
    aatt = 0

    a = 0
    c = 0
    g = 0
    t = 0

    aa = s_new.count_overlap("aa")
    ac = s_new.count_overlap("ac")
    at = s_new.count_overlap("at")
    ag = s_new.count_overlap("ag")

    ca = s_new.count_overlap("ca")
    cc = s_new.count_overlap("cc")
    ct = s_new.count_overlap("ct")
    cg = s_new.count_overlap("cg")

    ga = s_new.count_overlap("ga")
    gc = s_new.count_overlap("gc")
    gt = s_new.count_overlap("gt")
    gg = s_new.count_overlap("gg")

    ta = s_new.count_overlap("ta")
    tc = s_new.count_overlap("tc")
    tt = s_new.count_overlap("tt")
    tg = s_new.count_overlap("tg")

    a = s_new.count_overlap("a")
    c = s_new.count_overlap("c")
    t = s_new.count_overlap("t")
    g = s_new.count_overlap("g")

    ccgg = cc + gg
    agct = ag + ct
    gatc = ga + tc
    catg = ca + tg
    acgt = ac + gt
    aatt = aa + tt

    total = aa + ac + at + ag + ca + cc + ct + cg + ga + gc + gt + gg + ta + tc + tt + tg

    print("aa: ", aa)
    print("ac: ", ac)
    print("at: ", at)
    print("ag: ", ag)

    print("ca: ", ca)
    print("cc: ", cc)
    print("ct: ", ct)
    print("cg: ", cg)

    print("ga: ", ga)
    print("gc: ", gc)
    print("gt: ", gt)
    print("gg: ", gg)

    print("ta: ", ta)
    print("tc: ", tc)
    print("tt: ", tt)
    print("tg: ", tg)

    print("total: ", total)

    if (ctr1 == 1):
        o = cg / total
        e = ((c + g) / len(s_new))
        r = o / e
        print("o: ", o)
        print("e: ", e)
        print("r: ", r)
    elif (ctr1 == 2):
        o = gc / total
        e = ((g + c) / len(s_new))
        r = o / e
        print("o: ", o)
        print("e: ", e)
        print("r: ", r)
    elif (ctr1 == 3):
        o = ccgg / total
        e = ((c + g) / len(s_new)) * ((c + g) / len(s_new))
        r = o / e
        print("o: ", o)
        print("e: ", e)
        print("r: ", r)
    elif (ctr1 == 4):
        o = agct / total
        e = ((a + t) / len(s_new)) * ((g + c) / len(s_new))
        r = o / e
        print("o: ", o)
        print("e: ", e)
        print("r: ", r)
    elif (ctr1 == 5):
        o = gatc / total
        e = ((g + c) / len(s_new)) * ((a + t) / len(s_new))
        r = o / e
        print("o: ", o)
        print("e: ", e)
        print("r: ", r)
    elif (ctr1 == 6):
        o = catg / total
        e = ((c + g) / len(s_new)) * ((a + t) / len(s_new))
        r = o / e
        print("o: ", o)
        print("e: ", e)
        print("r: ", r)
    elif (ctr1 == 7):
        o = acgt / total
        e = ((a + t) / len(s_new)) * ((c + g) / len(s_new))
        r = o / e
        print("o: ", o)
        print("e: ", e)
        print("r: ", r)
    elif (ctr1 == 8):
        o = aatt / total
        e = ((a + t) / len(s_new)) * ((a + t) / len(s_new))
        r = o / e
        print("o: ", o)
        print("e: ", e)
        print("r: ", r)
    elif (ctr1 == 9):
        o = ta / total
        e = ((t + a) / len(s_new))
        r = o / e
        # print("c: ", c)
        # print("g: ", g)
        # print("len: ", len(src))
        print("o: ", o)
        print("e: ", e)
        print("r: ", r)
    elif (ctr1 == 10):
        o = at / total
        e = ((a + t) / len(s_new))
        r = o / e
        # print("c: ", c)
        # print("g: ", g)
        # print("len: ", len(s_new))
        print("o: ", o)
        print("e: ", e)
        print("r: ", r)
