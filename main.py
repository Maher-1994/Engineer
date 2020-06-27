import sys
from dd import database
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

a = QApplication (sys.argv)
w = QWidget ()
im = QPixmap ('ss.jpg')
im.mask ()
lab = QLabel (w)
lab.setPixmap (im)
w.resize (300, im.height ())
w.setWindowTitle ('Hi')
l1 = QLabel ('username', w)
l2 = QLabel ('password', w)
l1.move (30, 50)
l2.move (30, 83)
e1 = QLineEdit (w)
e2 = QLineEdit (w)
e1.setGeometry (80, 50, 100, 20)
e2.setGeometry (80, 80, 100, 20)


def p1func():
    try:
        x, y = database ().check ()
        a = s = False
        for i in range (len (x)):
            if e1.text () == x[i]: a = True
            if e2.text () == y[i]: s = True
        if a == True and s == True:
            import MainWindow
            w.hide ()
        else:
            b = QMessageBox.question (w, 'Wrong', 'You have Wrong info. are you want Retry',
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if b == QMessageBox.Yes:
                  p1func
            elif b == QMessageBox.No: sys.exit()
    except:print('lol')



p1 = QPushButton ('sign in', w)
p1.move (70, 150)
p1.clicked.connect (p1func)


def p2func():
    import xx

p2 = QPushButton ('sign up', w)
p2.move (150, 150)
p2.clicked.connect (p2func)

w.show ()
sys.exit (a.exec_ ())
