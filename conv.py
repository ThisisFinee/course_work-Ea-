import random as r


class Point:
    def __init__(self, num=0, way=[]):
        self.num = num
        self.way = way
        self.prod()
    def prod(self):
        self.way[self.num] = 0


def way_len(way, mat):
    s = 0
    for i in range(len(way)-1):
        s += mat[way[i]][way[i+1]]
    return s


def optim_est(i1, i2, i3, mat):
    a = min(way_len(i1, mat), way_len(i2, mat), way_len(i3, mat))
    if a == way_len(i1, mat):
        return i1
    elif a == way_len(i2, mat):
        return i2
    else:
        return i3


def tour_select(ways, mat): #Tournament selection
        new_ways = []
        num = len(ways)
        if len(ways) == 1:
            new_ways.append(ways[0])
            return new_ways
        elif len(ways) == 2:
            i1, i2=[], []
            while i1 == i2:
                i1 = r.randint(0, len(ways) - 1)
                i2 = r.randint(0, len(ways) - 1)
            new_ways.append(optim_est(ways[i1], ways[i2], ways[i1], mat))
            return new_ways
        for i in range(num):
            i1, i2, i3 = [], [], []
            while i1 == i2 or i1 == i3 or i2 == i3:
                i1 = r.randint(0, len(ways)-1)
                i2 = r.randint(0, len(ways)-1)
                i3 = r.randint(0, len(ways)-1)
            new_ways.append(optim_est(ways[i1], ways[i2], ways[i3], mat))
        return new_ways


def only_mas(arr, mas, sc):
    if sc == 0:
        return True
    if mas in arr[:sc-1]:
        return False
    else:
        return True


def no_re_way(way, mas):#no repeat way
    res = []
    for val in way:
        if val not in mas:
            res.append(val)
    return res


def first_gen(var, n, start):
    a = [[] for i in range(var)]
    sc = 0
    a_w = [i for i in range(n)]
    while not a[var - 1]:
        all_way_r = a_w
        all_way = []
        a[sc].append(start)
        all_way.append(start)
        for j in range(n):
            all_way_r = no_re_way(all_way_r, all_way)
            if not all_way_r:
                break
            else:
                a[sc].append(r.choice(all_way_r))
                all_way.append(a[sc][-1])
                all_way_r = a_w
        a[sc].append(start)
        if only_mas(a, a[sc], sc):
            sc+=1
        else:
            a[sc] = []
    return a


def form_way(n):
    a = [r.randint(1, 10) for i in range(n)]
    return a


def Point_mat(n):
    arr = []
    for i in range(n):
        if i == 0:
            arr.append(Point(i, form_way(n)))
        else:
            a = form_way(n)
            for j in range(len(arr)):
                a[j] = arr[j].way[i]
            arr.append(Point(i, a))
    return arr


def cross_gen(par1, par2):
    mid = (len(par1)//2)//2+1
    child1 = []
    child2 = []
    for i in range(mid+1):
        child1.append(par1[i])
        child2.append(par2[i])
    for i in range(mid+1, len(par1)):
        if par2[i] not in child1:
            child1.append(par2[i])
        if par1[i] not in child2:
            child2.append(par1[i])
    if len(child1)!=len(par1):
        for i in range(mid+1, len(par1)):
            if par1[i] not in child1:
                child1.append(par1[i])
    if len(child2)!=len(par2):
        for i in range(mid+1, len(par2)):
            if par2[i] not in child2:
                child2.append(par2[i])
    child1.append(child1[0])
    child2.append(child2[0])
    return [child1, child2]


def mutation_gen(par):
    i1, i2 = [], []
    i = r.randint(0, len(par)-1)
    while i1 == i2:
        i1 = r.randint(1, len(par[i]) - 2)
        i2 = r.randint(1, len(par[i]) - 2)
    mut_res = par[i]
    mut_res[i1], mut_res[i2] = mut_res[i2], mut_res[i1]
    return [mut_res, 1]
