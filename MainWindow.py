import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dd import database

a = QApplication (sys.argv)
t = QMainWindow ()
t.setGeometry (30, 30, 620, 600)
t.setWindowTitle ('Hi')
tab = QTabWidget (t)
tab.resize (580, 580)
t1 = QWidget ()
t1 = QWidget ()
t2 = QWidget ()
t3 = QWidget ()
t4 = QWidget ()

#######################################################################################
#                                                                                     #
#######################################################################################
tab.addTab (t1, 'Details')
tab.addTab (t2, 'AddDegree')
tab.addTab (t3, 'EditDegree')
tab.addTab (t4, 'Information')
#####################################################
#   t1      Tab of Details                          #
#####################################################
v = database ().get_student ()
table = QTableWidget (t1)
table.resize (600, 500)
table.setColumnCount (5)
table.setRowCount (len (v))
table.setHorizontalHeaderLabels (str ('id,fullname,username,type,department').split (','))
for i in range (len (v)):
    table.setItem (i, 0, QTableWidgetItem (str (v[i][0])))
    table.setItem (i, 1, QTableWidgetItem (v[i][1]))
    table.setItem (i, 2, QTableWidgetItem (v[i][2]))
    #table.setItem (i, 3, QTableWidgetItem (v[i][3]))
    table.setItem (i, 3, QTableWidgetItem (v[i][4]))
    table.setItem (i, 4, QTableWidgetItem (v[i][5]))
#############################################################################################################
#   Tab of AddDegree                         t2                                                            #
#############################################################################################################
label1 = QLabel ('id', t2)
label1.move (100, 30)
leid = QLineEdit (t2)
leid.move (150, 30)

label2 = QLabel ('mark1', t2)
label2.move (100, 60)
el2 = QLineEdit (t2)
el2.move (150, 60)
label3 = QLabel ('mark2', t2)
label3.move (100, 90)
el3 = QLineEdit (t2)
el3.move (150, 90)
label4 = QLabel ('mark3', t2)
label4.move (100, 120)
el4 = QLineEdit (t2)
el4.move (150, 120)


def idfunc():
    try:
        a = int (leid.text ())
        b = int (el2.text ())
        z = int (el3.text ())
        q = int (el4.text ())
        database ().add_degree (a, b, z, q)
        leid.setText ('')
        el2.setText ('')
        el3.setText ('')
        el4.setText ('')
    except:
        print("Change ID please")


pid = QPushButton (QIcon ('add1.jpeg'), '', t2)
pid.resize (22, 22)
pid.move (300, 30)
pid.clicked.connect (idfunc)
##################################################################################################
#       Tab of Edit Degrees                t3                                                    #
##################################################################################################
lab1 = QLabel ('ID', t3)
lab1.move (100, 33)
leid1 = QLineEdit (t3)
leid1.move (130, 30)
leid1.resize (30, 20)
################################
lab2 = QLabel ('mark1', t3)
lab2.move (100, 60)
el22 = QLineEdit (t3)
el22.move (180, 60)
##############################
lab3 = QLabel ('mark2', t3)
lab3.move (100, 90)
el33 = QLineEdit (t3)
el33.move (180, 90)
#############################
lab4 = QLabel ('mark3', t3)
lab4.move (100, 120)
el44 = QLineEdit (t3)
el44.move (180, 120)
#############################
m_1 = QLabel ('null', t3)
m_1.move (150, 60)
m_1.resize (20, 20)
m_2 = QLabel ('null', t3)
m_2.move (150, 90)
m_2.resize (20, 20)
m_3 = QLabel ('null', t3)
m_3.move (150, 120)
m_3.resize (20, 20)


def search1():
    try:
        srch = leid1.text ()
        m_degree = database ().search (srch)

        m_1.setText (str (m_degree[0][1]))
        m_2.setText (str (m_degree[0][2]))
        m_3.setText (str (m_degree[0][3]))
    except:
        print("change'id' please to Search")


def updt():
  try:
      ii = int (leid1.text ())
      aa = int (el22.text ())
      bb = int (el33.text ())
      cc = int (el44.text ())
      m_1.setText (str (aa))
      m_2.setText (str (bb))
      m_3.setText (str (cc))
      database ().degree_update (ii, aa, bb, cc)
      leid1.setText ('')
      el22.setText ('')
      el33.setText ('')
      el44.setText ('')
  except:
      print('Please add correct values')


psrch = QPushButton ('Search', t3)
psrch.move (210, 30)
psrch.clicked.connect (search1)
padd = QPushButton ('Change', t3)
padd.move (170, 150)
padd.clicked.connect (updt)
######################################################################################################################
#                        Tap4 of AllInformation          t4                                                          #
#####################################################################################################################
co=database().twice() # get the information from 2tables database
table_all=QTableWidget(t4)
table_all.resize (600, 500)
table_all.setColumnCount (7)
table_all.setRowCount (len (co))
table_all.setHorizontalHeaderLabels (str ('id,fullname,department,mark1,mark2,mark3,average').split (','))
for j in range (len (co)):                                      ######################################################
    table_all.setItem (j, 0, QTableWidgetItem (str (co[j][0]))) #                                                     #
    table_all.setItem (j, 1, QTableWidgetItem (co[j][1]))       #                                                     #
    table_all.setItem (j, 2, QTableWidgetItem (co[j][2]))       #                                                     #
    table_all.setItem (j, 3, QTableWidgetItem (str(co[j][3])))  #                                                     #
    table_all.setItem (j, 4, QTableWidgetItem (str(co[j][4])))  #                                                     #
    table_all.setItem (j, 5, QTableWidgetItem (str(co[j][5])))  #                                                     #
    table_all.setItem (j, 6, QTableWidgetItem (str(co[j][6])))  #                                                     #
t.show ()                                                      #######################################################
