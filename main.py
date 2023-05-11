import conv as con
import random as r


def print_mat(mat):
    for i in mat:
        print(*i)


if __name__ == '__main__':

    CHILD_CHANCE = 50
    MUTATION_CHANCE = 5

    n = int(input("Input number of points: "))
    start = int(input(f"Select a starting point(<{n}): "))
    first = int(input(f"Input number of options of first generation: "))
    selection = int(input(f"Input number of selection: "))

    poi_mat = con.Point_mat(n)
    mat = []
    for i in poi_mat:
        mat.append(i.way)
    print_mat(mat)
    mas_gen = con.first_gen(first, n, start)

    print(mas_gen)
    s = ""
    for i in range(len(mas_gen)):
        s = s + str(con.way_len(mas_gen[i], mat)) + " "
    print(s)
    new_mas_gen = []
    for i in range(selection):
        if i == 0:
            new_mas_gen = con.tour_select(mas_gen, mat)
        else:
            new_mas_gen = con.tour_select(new_mas_gen, mat)
        for j in range(first//2):
            child = r.randint(1, 100)
            if child <= CHILD_CHANCE:
                i1, i2 = [], []
                while i1 == i2:
                    i1 = r.randint(0, len(new_mas_gen)-1)
                    i2 = r.randint(0, len(new_mas_gen)-1)
                # print(new_mas_gen[i1], new_mas_gen[i2])
                # print(con.cross_gen(new_mas_gen[i1], new_mas_gen[i2])[0],
                #       con.cross_gen(new_mas_gen[i1], new_mas_gen[i2])[1])
                child1 = con.cross_gen(new_mas_gen[i1], new_mas_gen[i2])[0]
                child2 = con.cross_gen(new_mas_gen[i1], new_mas_gen[i2])[1]
                one = False
                two = False
                if child1 not in new_mas_gen and con.way_len(child1, mat) < con.way_len(new_mas_gen[i1], mat):
                    new_mas_gen[i1] = child1
                    one = True
                if child2 not in new_mas_gen and con.way_len(child2, mat) < con.way_len(new_mas_gen[i2], mat):
                    new_mas_gen[i2] = child2
                    two = True
                if one is False and two is False:
                    zap_child = min(con.way_len(child1, mat), con.way_len(child2, mat))
                    if zap_child == con.way_len(child1, mat):
                        far_child = child1
                    else:
                        far_child = child2
                    zap_gen = max(con.way_len(new_mas_gen[i1], mat), con.way_len(new_mas_gen[i2], mat))
                    if zap_gen == con.way_len(new_mas_gen[i1], mat):
                        far_i = i1
                    else:
                        far_i = i2
                    new_mas_gen[far_i] = far_child
            mutation = r.randint(1, 100)
            if mutation <= MUTATION_CHANCE and j % 3 == 0:
                res_mut = con.mutation_gen(new_mas_gen)[0]
                index_mut = con.mutation_gen(new_mas_gen)[1]
                if res_mut not in new_mas_gen and con.way_len(res_mut, mat) <= con.way_len(new_mas_gen[index_mut], mat):
                    print(con.way_len(res_mut, mat), con.way_len(new_mas_gen[index_mut], mat))
                    new_mas_gen[index_mut] = res_mut
                print(new_mas_gen, res_mut, index_mut)
        print(new_mas_gen)
        s1 = ""
        for i in range(len(new_mas_gen)):
            s1 = s1 + str(con.way_len(new_mas_gen[i], mat)) + " "
        print(s1)

    # s1 = ""
    # for i in range(len(new_mas_gen)):
    #     s1 = s1 + str(con.way_len(new_mas_gen[i], mat)) + " "
    # print(s1)
