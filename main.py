
import GUI


if __name__ == '__main__':
    import sys
    app = GUI.QtWidgets.QApplication(sys.argv)
    MainWindow = GUI.QtWidgets.QMainWindow()
    main = GUI.MainWindow()
    main.setup(MainWindow)
    MainWindow.show()

    def Result_Out():
        global Resul
        Resul = GUI.QtWidgets.QDialog()
        if main.mer!=[0, 0, 0]:
            result = GUI.Result(1)
        else:
            result = GUI.Result(0)
        result.setup(Resul)
        Resul.show()


    main.Result_Button.clicked.connect(Result_Out)
    sys.exit(app.exec_())
