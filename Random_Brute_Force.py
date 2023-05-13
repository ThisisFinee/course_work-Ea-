import conv as c

def Brute_Force(n, selection, first, start, mat):
    fir = selection*first
    way_mas = c.first_gen(fir, n, start)
    res_mas = []
    for i in range(len(way_mas)):
        res_mas.append(c.way_len(way_mas[i], mat))
    res_index = res_mas.index(min(res_mas))
    result = [way_mas[res_index], res_mas[res_index]]
    return result
