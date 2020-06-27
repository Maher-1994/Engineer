import sys
from dd import database
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

a = QApplication (sys.argv)
w1 = QWidget ()
w1.setWindowTitle ('Hi')
im1 = QPixmap ('ss.jpg')
lab1 = QLabel (w1)
lab1.setPixmap (im1)
w1.resize (im1.width (), w1.height ())
lf = QLabel ('fullname', w1)
lf.move (30, 50)
elf = QLineEdit (w1)
elf.setGeometry (80, 49, 100, 20)
lu = QLabel ('username', w1)
lu.move (30, 83)
e11 = QLineEdit (w1)
e11.setGeometry (80, 80, 100, 20)
lp = QLabel ('password', w1)
lp.move (30, 113)
e22 = QLineEdit (w1)
e22.setGeometry (80, 110, 100, 20)

tp = QRadioButton ('student', w1)
tp1 = QRadioButton ('professor', w1)
tp1.setChecked (True)
tp.move (400, 50)
tp1.move (400, 100)
ldep = QLabel ('Department', w1)
ldep.move (244,48)
dep = QComboBox (w1)
dep.setGeometry(240, 65,60,20)
dep.addItem ('ios')
dep.addItem ('cs')
dep.addItem ('dc')
def bpfunc():
   try:
       if tp.isChecked () == True:
           type1 = 'student'
       else:
           type1 = 'professor'
       depart = dep.currentText ()
       fulnam = elf.text ()
       usrnam = e11.text ()
       password = e22.text ()
       database ().new_user (fulnam, usrnam, password, type1, depart)
       b11 = QMessageBox.question (w1, 'Add', 'Are you want to add another one ??',
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
       if b11 == QMessageBox.Yes:
           elf.setText('')
           e11.setText('')
           e22.setText('')
           bpfunc

       else:
           w1.hide()
   except:
       b = QMessageBox.question (w1, 'Wrong', 'You have Wrong info. are you want Retry',
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
       if b == QMessageBox.Yes:
           bpfunc

       else:sys.exit()




bp=QPushButton('save',w1)
bp.move(80,200)
bp.clicked.connect(bpfunc)
w1.show ()

