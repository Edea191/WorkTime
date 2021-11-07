
import mainwindow1
from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QStackedWidget, QScrollBar, QTableWidget, QTableView, QComboBox
from PyQt5 import QtCore, QtSql, QtGui
from PyQt5.QtCore import QDate, Qt, QPoint, QSortFilterProxyModel

import PyQt5.QtWidgets
import PyQt5
from PyQt5.QtGui import QPainter, QCursor
import sqlite3
import datetime

"""
class StackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent=parent)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap("image.png"))
        QStackedWidget.paintEvent(self, event)

"""
class MainWindow(QMainWindow):


    def __init__(self, parent =None):
        QMainWindow.__init__(self, parent)
        self.ui = mainwindow1.Ui_MainWindow()
        #self.setCentralWidget(StackedWidget())
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)


    #------------------------------SET STYLE-------------------------------
        ico = 'mssvp_8_7.ico'
        self.setWindowIcon(QtGui.QIcon(ico))
        self.setWindowTitle('Work Time')
        #self.setStyleSheet("background-color: rgb(254, 235, 201);")

        self.setStyleSheet( "background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 #F5EEF8, stop:1 #FADBD8);"
                            "background-image: url(plotno.png);"
                            )
        #self.setStyleSheet("QMainWindow {background - color: rgba(0, 41, 59, 255);}QScrollBar: horizontal{width: 1px;height: 1px;background - color: rgba(0, 41, 59, 255);}QScrollBar: vertical{width: 1px;height: 1px;background - color: rgba(0, 41, 59, 255);}")


        color_button = (#"QPushButton"
                        #"{"
                        #"background-color : qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 #FEDED2, stop:1 #E7CACA);"
                        #"}"
                        "QPushButton::hover"
                        "{"
                        "background-color : qlineargradient(x1:0, y1:0, x1:0, y2:1,stop:0 #F1D3D2, stop:1 #E7CACA);"
                        "}"
                        #"QPushButton"
                        "{"
                        "border: 1px solid #E7CACA;"
                        "}"
                        #"{"
                       # "padding: 5px;"
                        #"}"
                        )
        self.ui.pushButton_exit.setStyleSheet("QPushButton"
                        "{"
                        "background-color : #FEDED2;"
                        "}"
                        "QPushButton::hover"
                        "{"
                        "background-color : qlineargradient(x1:0, y1:0, x1:0, y2:1,stop:0 #F1D3D3, stop:1 #FEDED2);")
        self.ui.pushButton_dodaj.setStyleSheet(color_button)

        self.ui.label_przepracowane_godziny.setStyleSheet("background-color: #FEDED2;")
        self.ui.pushButton_exit.clicked.connect(self.close)

        color = PyQt5.QtWidgets.QGraphicsColorizeEffect() #QGraphicsColorizeEffect()

        #color.setColor(Qt.darkRed)
        #self.ui.calendarWidget.setGraphicsEffect(color)

        self.ui.calendarWidget.setStyleSheet("background-color: #FDEDEC ; color: black; selection-background-color: #F2D7D5 ; alternate-background-color: #F2D7D5 ; selection-border: 1px solid red; border: 1px #FEDED2;"
                                             #"QHeaderView::section"
                                             #"{"
                                             #"background: #FEDEDD;"
                                            # "}"
                                            )


        self.ui.tableView.setStyleSheet("QTableView" "{" "selection-background-color: #E7CACA;" "}" "QTableView" "{" "gridline-color: #E7CACA;" "}""QTableView""{" "border: none;" "}""QTableView""{" "selection-border: 1px #FEDED2;" "}"
                                        "QTableView QTableCornerButton::section" "{""background-image:  url(plotno.png)""}"
                                        "QHeaderView::section"
                                        "{"
                                        "background: #FDEDEC;"
                                        "}"
                                        "QHeaderView::section""{"
                                        "border: 1px solid qlineargradient(x1:0, y1:0, x1:0, y2:1,stop:0 #F1D3D3, stop:1 #E7CACA);;"
                                        "}"
                                        "{"
                                        "padding: 1px;"
                                        "}"
                                        "front-size: 1pt;"
                                        "}"
                                        )


        #self.ui.calendarWidget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.ui.timeEdit_poczatek.setStyleSheet("boder: 1px solid #E7CACA;")


    #-------------------------------------------------------------
        self.db_connect = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db_connect.setDatabaseName("database.db")
        self.db_connect.open()
        self.model = QtSql.QSqlTableModel()


    #-----------------wybór tabeli--------------------------------
        for table in self.db_connect.tables():
            if table == 'sqlite_sequence':
                continue
            self.ui.listWidget.addItem(table)

        self.model.setTable(table)
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)

        self.ui.tableView.setModel(self.model)
        self.createtableview()
        self.ui.listWidget.clicked.connect(self.wybormiesiaca)
        self.TableChoice = table
        self.ui.pushButton_dodaj.clicked.connect(self.dodaj)
        self.ui.calendarWidget.clicked.connect(self.Data)
        self.ui.tableView.doubleClicked.connect(self.delete)

    def createtableview(self):

        self.model.setSort(1, Qt.AscendingOrder)
        self.model.select()

        self.model.setHeaderData(1, Qt.Horizontal, ("Data"))
        self.model.setHeaderData(2, Qt.Horizontal, ("Początek"))
        self.model.setHeaderData(3, Qt.Horizontal, ("Koniec"))
        self.model.setHeaderData(4, Qt.Horizontal, ("Czas pracy"))

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnHidden(0, True)
        self.ui.tableView.setColumnHidden(5, True)
        self.ui.tableView.setColumnHidden(6, True)

        self.sumuj()


    def wybormiesiaca(self):
        self.model.setTable(self.ui.listWidget.currentItem().text())
        self.model.select()
        self.TableChoice = self.ui.listWidget.currentItem().text()
        print(self.TableChoice)
        self.createtableview()

    def close(self):
        sys.exit()

    def sumuj(self):
        connection = sqlite3.connect("database.db")
        crs = connection.cursor()
        try:
            crs.execute("Select hour from "+ self.TableChoice)#"work")
        except:
            crs.execute("Select hour from work")

        RawHour = crs.fetchall()
        licznik_hour = 0
        licznik_minute = 0
        for i in RawHour:
            dane = int(i[0])
            licznik_hour = licznik_hour + dane

        try:
            crs.execute("Select minute from " + self.TableChoice)
        except:
            crs.execute("Select minute from work")

        RawMinute = crs.fetchall()
        for i in RawMinute:
            dane = int(i[0])
            licznik_minute = licznik_minute + dane

        dodaj_godziny = licznik_minute // 60
        dodaj_minuty = licznik_minute % 60

        licznik_hour = licznik_hour + dodaj_godziny
        licznik_minuty_po_odjeciu = dodaj_minuty


        self.ui.lineEdit_suma.setText("    " + str(licznik_hour) + ':' + str(licznik_minuty_po_odjeciu))


    def delete(self):
        self.model.removeRow(self.ui.tableView.currentIndex().row())
        self.model.submitAll()
        self.model.select()
        self.sumuj()

    def Data(self, qDate):
        self.CalendarDay = '{2}-{0}-{1}'.format(qDate.month(), qDate.day(), qDate.year())
        StartWork = self.ui.timeEdit_poczatek.text()
        #---------korekta daty---------
        self.month = '{0}'.format(qDate.month())
        self.day = '{0}'.format(qDate.day())

        self.month = int(self.month)
        self.day = int(self.day)

        if self.month <= 9:
            self.CalendarDay = '{2}-0{0}-{1}'.format(qDate.month(), qDate.day(), qDate.year())
            if self.day <= 9:
                self.CalendarDay = '{2}-0{0}-0{1}'.format(qDate.month(), qDate.day(), qDate.year())

    def wyliczminuty(self, czas_pracy_poczatek, czas_pracy_koniec):

    #------------poczatek pracy---------------
        czas_pracy_INT_godziny = czas_pracy_poczatek[0:2]
        czas_pracy_INT_godziny = int(czas_pracy_INT_godziny)
        czas_pracy_INT_minuty = czas_pracy_poczatek[3:5]
        czas_pracy_INT_minuty = int(czas_pracy_INT_minuty)
        czas_pracy_razem = (czas_pracy_INT_godziny * 60) + czas_pracy_INT_minuty
    #---------koniec pracy-------------------
        czas_pracy_INT_godzinyend = czas_pracy_koniec[0:2]
        czas_pracy_INT_godzinyend = int(czas_pracy_INT_godzinyend)
        czas_pracy_INT_minutyend = czas_pracy_koniec[3:5]
        czas_pracy_INT_minutyend = int(czas_pracy_INT_minutyend)
        czas_pracy_razem_end = (czas_pracy_INT_godzinyend * 60) + czas_pracy_INT_minutyend
    #------------różnica---------------------
        try:
            przepracowane_minuty = int(czas_pracy_razem_end) - int(czas_pracy_razem)


        except:
            print("nie bagla")
        return przepracowane_minuty

    def dodaj(self):
        StartWork = self.ui.timeEdit_poczatek.text()
        EndWork = self.ui.timeEdit_koniec.text()
        czas_pracy = self.wyliczminuty(StartWork, EndWork)


        try:
            WorkDay = self.CalendarDay
            przelicz_h = int(czas_pracy) // 60

            przelicz_min = int(czas_pracy) % 60
            if przelicz_h < 10:
                przelicz_h = "0" + str(przelicz_h)
            else:
                przelicz_h = str(przelicz_h)


            if przelicz_min < 10:
                przelicz_min = "0" + str(przelicz_min)
            else:
                przelicz_min= str(przelicz_min)

            przepracowany_czas = przelicz_h + ":" + przelicz_min


            sql = "INSERT INTO " + self.TableChoice + "(date, work_start, work_end, worktime, hour, minute) VALUES " \
                  "('" + WorkDay + "', '" + StartWork + "', '" + EndWork + "', '"+ przepracowany_czas +"', '"+ przelicz_h + "', '"+ przelicz_min +"')"
            self.db_connect.exec(sql)
            self.model.select()

            self.sumuj()
        except:
            pass

    #def suma(self):
        #self.suma_godzin = QtSql.QSqlQueryModel()
        #self.suma_godzin.setQuery("select time(sum(strftime('%s', worktime) - strftime('%s', '00:00')), 'unixepoch') from work")
        #self.ui.listView_suma_czasu.setModel(self.suma_godzin)



    def mousePressEvent(self, event):
        self.last_pos = QCursor.pos()

    def mouseMoveEvent(self, event):
        buttons = event.buttons()
        new_pos = QCursor.pos()
        offset = new_pos - self.last_pos
        if buttons & Qt.LeftButton:
            self.move(self.pos() + offset)
            self.update()
        elif buttons & Qt.RightButton:
            size = self.size()
            self.resize(size.width() + offset.x(),
                        size.height() + offset.y())
            self.update()
        self.last_pos = QPoint(new_pos)




if __name__ == '__main__':
    import sys

    app=QApplication(sys.argv)
    app.setStyleSheet('QWidget { background-color: #aa8888; } QHeaderView::section { background-color: #88aa88; } QTableWidget QTableCornerButton::section {background-color: #8888aa; }')
    windows=MainWindow()
    windows.show()
    app.exec_()