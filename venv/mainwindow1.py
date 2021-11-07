# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 627)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 431, 561))
        self.tableView.setObjectName("tableView")
        self.label_przepracowane_godziny = QtWidgets.QLabel(self.centralwidget)
        self.label_przepracowane_godziny.setGeometry(QtCore.QRect(600, 30, 121, 16))
        self.label_przepracowane_godziny.setObjectName("label_przepracowane_godziny")
        self.lineEdit_suma = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_suma.setGeometry(QtCore.QRect(730, 30, 61, 21))
        self.lineEdit_suma.setReadOnly(True)
        self.lineEdit_suma.setObjectName("lineEdit_suma")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(470, 90, 321, 191))
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setObjectName("calendarWidget")
        self.pushButton_dodaj = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dodaj.setGeometry(QtCore.QRect(470, 330, 321, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_dodaj.setFont(font)
        self.pushButton_dodaj.setMouseTracking(False)
        self.pushButton_dodaj.setTabletTracking(False)
        self.pushButton_dodaj.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_dodaj.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_dodaj.setAcceptDrops(False)
        self.pushButton_dodaj.setToolTip("")
        self.pushButton_dodaj.setAutoFillBackground(False)
        self.pushButton_dodaj.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_dodaj.setCheckable(False)
        self.pushButton_dodaj.setAutoRepeat(False)
        self.pushButton_dodaj.setAutoExclusive(False)
        self.pushButton_dodaj.setAutoRepeatDelay(300)
        self.pushButton_dodaj.setAutoDefault(False)
        self.pushButton_dodaj.setDefault(False)
        self.pushButton_dodaj.setObjectName("pushButton_dodaj")
        self.timeEdit_poczatek = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_poczatek.setGeometry(QtCore.QRect(470, 290, 101, 22))
        self.timeEdit_poczatek.setObjectName("timeEdit_poczatek")
        self.timeEdit_koniec = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_koniec.setGeometry(QtCore.QRect(700, 290, 91, 22))
        self.timeEdit_koniec.setObjectName("timeEdit_koniec")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(800, 0, 21, 21))
        self.pushButton_exit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("acl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_exit.setIcon(icon)
        self.pushButton_exit.setCheckable(False)
        self.pushButton_exit.setAutoRepeat(False)
        self.pushButton_exit.setAutoExclusive(False)
        self.pushButton_exit.setFlat(True)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(650, 371, 141, 201))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_przepracowane_godziny.setText(_translate("MainWindow", "Przepracowane godziny"))
        self.pushButton_dodaj.setText(_translate("MainWindow", "Dodaj"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
