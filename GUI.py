from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import matplotlib as mpl
import main
import sys
import time
import os
import Random_Brute_Force as rbf
import conv as con
import random as r
import matplotlib.pyplot as plt


def Search(mer):
    global mer1
    mer1 = mer


class MainWindow(object):

    def setup(self, MainWindow):
        self.mer = [0, 0, 0]
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(361, 600)
        MainWindow.setMinimumSize(QtCore.QSize(361, 600))
        MainWindow.setMaximumSize(QtCore.QSize(361, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.Generate_button.setGeometry(QtCore.QRect(90, 240, 171, 51))
        self.Generate_button.setStyleSheet("color:white;\n"
                                           "border-top-left-radius: 14px;\n"
                                           "border-top-right-radius: 14px;\n"
                                           "border-bottom-left-radius: 14px;\n"
                                           "border-bottom-right-radius: 14px;\n"
                                           "background-color:rgb(255, 170, 0);")
        self.Generate_button.setObjectName("Generate_button")
        self.Generate_button.clicked.connect(self.Generate_func)
        self.line_num = QtWidgets.QLineEdit(self.centralwidget)
        self.line_num.setGeometry(QtCore.QRect(20, 31, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_num.setFont(font)
        self.line_num.setStyleSheet("background-color: #22222e;\n"
                                    "border-top-left-radius: 10px;\n"
                                    "border-top-right-radius: 10px;\n"
                                    "border-bottom-left-radius: 10px;\n"
                                    "border-bottom-right-radius: 10px;\n"
                                    "color: white;")
        self.line_num.setObjectName("line_num")
        self.line_start = QtWidgets.QLineEdit(self.centralwidget)
        self.line_start.setGeometry(QtCore.QRect(20, 80, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_start.setFont(font)
        self.line_start.setStyleSheet("background-color: #22222e;\n"
                                      "border-top-left-radius: 10px;\n"
                                      "border-top-right-radius: 10px;\n"
                                      "border-bottom-left-radius: 10px;\n"
                                      "border-bottom-right-radius: 10px;\n"
                                      "color: white;")
        self.line_start.setObjectName("line_start")
        self.line_first = QtWidgets.QLineEdit(self.centralwidget)
        self.line_first.setGeometry(QtCore.QRect(20, 130, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_first.setFont(font)
        self.line_first.setStyleSheet("background-color: #22222e;\n"
                                      "border-top-left-radius: 10px;\n"
                                      "border-top-right-radius: 10px;\n"
                                      "border-bottom-left-radius: 10px;\n"
                                      "border-bottom-right-radius: 10px;\n"
                                      "color: white;")
        self.line_first.setObjectName("line_first")
        self.line_selection = QtWidgets.QLineEdit(self.centralwidget)
        self.line_selection.setGeometry(QtCore.QRect(20, 180, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_selection.setFont(font)
        self.line_selection.setStyleSheet("background-color: #22222e;\n"
                                          "border-top-left-radius: 10px;\n"
                                          "border-top-right-radius: 10px;\n"
                                          "border-bottom-left-radius: 10px;\n"
                                          "border-bottom-right-radius: 10px;\n"
                                          "color: white;")
        self.line_selection.setObjectName("line_selection")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 361, 601))
        self.frame.setStyleSheet("background-color: rgb(255, 60, 60);\n"
                                 "border-top-left-radius: 14px;\n"
                                 "border-top-right-radius: 14px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(80, 230, 191, 371))
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                   "border-top-left-radius: 14px;\n"
                                   "border-top-right-radius: 14px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Result_Button = QtWidgets.QPushButton(self.frame_2)
        self.Result_Button.setGeometry(QtCore.QRect(10, 70, 171, 51))
        self.Result_Button.setStyleSheet("color:white;\n"
                                         "border-top-left-radius: 14px;\n"
                                         "border-top-right-radius: 14px;\n"
                                         "border-bottom-left-radius: 14px;\n"
                                         "border-bottom-right-radius: 14px;\n"
                                         "background-color:rgb(255, 170, 0);")
        self.Result_Button.setObjectName("Result_Button")
        self.cat = QtWidgets.QLabel(self.frame_2)
        self.cat.setGeometry(QtCore.QRect(50, 140, 101, 101))
        self.cat.setText("")
        main_path = os.getcwd()
        self.cat.setPixmap(QtGui.QPixmap(main_path + "/kot.jpg"))
        self.cat.setObjectName("cat")
        self.frame.raise_()
        self.line_num.raise_()
        self.line_selection.raise_()
        self.line_start.raise_()
        self.frame_2.raise_()
        self.Generate_button.raise_()
        self.line_first.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslate(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Genetic algorithm"))
        self.Generate_button.setText(_translate("MainWindow", "Генерация"))
        self.line_num.setPlaceholderText(_translate("MainWindow", "Введите количество городов"))
        self.line_start.setPlaceholderText(_translate("MainWindow", "Введите точку старта"))
        self.line_first.setPlaceholderText(_translate("MainWindow", "Размер первичной популяции"))
        self.line_selection.setPlaceholderText(_translate("MainWindow", "Введите количество отборов"))
        self.Result_Button.setText(_translate("MainWindow", "Результаты"))

    def Generate_func(self, MainWindow):
        if not self.line_num.text() or not self.line_start.text() or not self.line_first.text()\
                or not self.line_selection.text() or int(self.line_start.text())>int(self.line_num.text()):
            return 0
        n = int(self.line_num.text())
        start = int(self.line_start.text())
        first = int(self.line_first.text())
        selection = int(self.line_selection.text())
        print(n, start, first, selection)
        poi_mat = con.Point_mat(n)
        mas_gen = con.first_gen(first, n, start)
        dis = self.distance_matrix(poi_mat, mas_gen)
        self.mer = self.main_func(n, start, first, selection, dis)
        Search(self.mer)
        return self.mer

    def print_mat(self, mat):
        for i in mat:
            print(*i)

    def distance_matrix(self, poi_mat1, mas_gen1):
        poi_mat = poi_mat1
        mat = []
        for i in poi_mat:
            mat.append(i.way)
        self.print_mat(mat)
        mas_gen = mas_gen1
        # данные первичной популяции
        # print(mas_gen)
        say = []
        for ind in range(len(mas_gen)):
            say.append(con.way_len(mas_gen[ind], mat))
        # print(say)
        return [mas_gen, mat, say]

    def Brute_chance(self, n, selection, first, start, mat):
        bf = rbf.Brute_Force(n, selection, first, start, mat)
        return bf

    def result_gen(self, new_mas_gen, s1):
        res_ind = s1.index(min(s1))
        res_way = new_mas_gen[res_ind]
        res_sum = s1[res_ind]
        return [res_way, res_sum]

    def main_func(self, n1, start1, first1, selection1, m1):

        CHILD_CHANCE = 50
        MUTATION_CHANCE = 10

        # n = int(input("Input number of points: "))
        # start = int(input(f"Select a starting point(<{n}): "))
        # first = int(input(f"Input number of options of first generation: "))
        # selection = int(input(f"Input number of selection: "))
        n = n1
        start = start1
        first = first1
        selection = selection1
        m = m1
        mat = m[1]
        mas_gen = m[0]
        new_mas_gen = []
        plt.ion()
        for i in range(selection):
            if i == 0:
                new_mas_gen = con.tour_select(mas_gen, mat)
            else:
                new_mas_gen = con.tour_select(new_mas_gen, mat)
            for j in range(first // 2):
                child = r.randint(1, 100)
                if child <= CHILD_CHANCE:
                    i1, i2 = [], []
                    while i1 == i2:
                        i1 = r.randint(0, len(new_mas_gen) - 1)
                        i2 = r.randint(0, len(new_mas_gen) - 1)
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
                    if res_mut not in new_mas_gen and con.way_len(res_mut, mat) <= con.way_len(new_mas_gen[index_mut],
                                                                                               mat):
                        # print(con.way_len(res_mut, mat), con.way_len(new_mas_gen[index_mut], mat))
                        new_mas_gen[index_mut] = res_mut
            #         print(new_mas_gen, res_mut, index_mut)
            # print(new_mas_gen)
            s1 = []
            for i in range(len(new_mas_gen)):
                s1.append(con.way_len(new_mas_gen[i], mat))
            x = [i for i in range(len(s1))]
            y = s1
            plt.clf()
            plt.scatter(x, y)
            plt.xlabel(r'Population')
            plt.ylabel(r'Way length')
            plt.ylim([0, max(m[2])])
            plt.draw()
            plt.gcf().canvas.flush_events()
            time.sleep(0.2)
        plt.ioff()
        plt.show()
        # print(*s1)
        print("Первичная популяция:")
        print(m[2])
        print("Лучший результат первичной популяции:")
        print(min(m[2]))

        brute = self.Brute_chance(n, selection, first, start, mat)
        brute_sum = brute[1]
        brute_way = brute[0]
        print("Лучший путь найденный с помощью частичного случайного перебора:")
        print(brute_way)
        print("Лучший результат найденный с помощью частичного перебора")
        print(brute_sum)

        res_gen = self.result_gen(new_mas_gen, s1)
        res_way = res_gen[0]
        res_sum = res_gen[1]
        print("Лучший путь найденный с помощью генетического алгоритма:")
        print(res_way)
        print("Результат работы генетического алгоритма:")
        print(res_sum)
        # s1 = ""
        # for i in range(len(new_mas_gen)):
        #     s1 = s1 + str(con.way_len(new_mas_gen[i], mat)) + " "
        # print(s1)
        return [min(m[2]), brute_sum, res_sum]



class Result(object):
    def __init__(self, flag1 = 0):
        self.flag = flag1

    def setup(self, Result):
        Result.setObjectName("Result")
        Result.resize(400, 300)
        self.frame = QtWidgets.QFrame(Result)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.frame.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 15, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.res_first_label = QtWidgets.QLabel(self.frame)
        self.res_first_label.setGeometry(QtCore.QRect(20, 50, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.res_first_label.setFont(font)
        self.res_first_label.setStyleSheet("color: rgb(255, 255, 255);")
        if self.flag == 1:
            self.res_first_label.setText(str(mer1[0]))
        else:
            self.res_first_label.setText("Сгенерируйте первичную популяцию!")
        self.res_first_label.setObjectName("res_first_label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.res_brute_label = QtWidgets.QLabel(self.frame)
        self.res_brute_label.setGeometry(QtCore.QRect(20, 135, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.res_brute_label.setFont(font)
        self.res_brute_label.setStyleSheet("color: rgb(255, 255, 255);")
        if self.flag == 1:
            self.res_brute_label.setText(str(mer1[1]))
        else:
            self.res_brute_label.setText("Сгенерируйте результат перебора!")
        self.res_brute_label.setObjectName("res_brute_label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 185, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.res_gen_label = QtWidgets.QLabel(self.frame)
        self.res_gen_label.setGeometry(QtCore.QRect(20, 220, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.res_gen_label.setFont(font)
        self.res_gen_label.setStyleSheet("color: rgb(255, 255, 255);")
        if self.flag == 1:
            self.res_gen_label.setText(str(mer1[2]))
        else:
            self.res_gen_label.setText("Сгенерируйте результат ГА")
        self.res_gen_label.setObjectName("res_gen_label")

        self.retranslate(Result)
        QtCore.QMetaObject.connectSlotsByName(Result)

    def retranslate(self, Result):
        _translate = QtCore.QCoreApplication.translate
        Result.setWindowTitle(_translate("Result", "Dialog"))
        self.label.setText(_translate("Result", "Лучший результат первичной популяции:"))
        self.label_2.setText(_translate("Result", "Результат частичного перебора:"))
        self.label_3.setText(_translate("Result", "Результат генетического алгоритма:"))
