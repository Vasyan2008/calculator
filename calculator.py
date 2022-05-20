from PyQt5.QtWidgets import*
app = QApplication([])


okno3 = QWidget()


line3 = QVBoxLayout()
okno3.setLayout(line3)

line4 = QHBoxLayout()
line3.addLayout(line4)


v1 =QPushButton('*')
line3.addWidget(v1)

v2 =QPushButton('+')
line3.addWidget(v2)

v3 =QPushButton('—')
line3.addWidget(v3)

v4 =QPushButton('/')
line3.addWidget(v4)



pole1 = QLineEdit()
line4.addWidget(pole1)
pole2 = QLineEdit()
line4.addWidget(pole2)

otvet2= QLabel('=')
line4.addWidget(otvet2)

otvet1 = QLabel('answer')
line4.addWidget(otvet1)


def plus():
    a = pole1.text()
    b =pole2.text()
    try:
        a = int(a)
        b = int(b)
        result = a + b
        otvet1.setText(str(result))

    except:
        err = QMessageBox()
        err.setText('error')
        err.exec_()

def minus():
    a = pole1.text()
    b =pole2.text()
    try:
        a = int(a)
        b = int(b)
        result = a - b
        otvet1.setText(str(result))

    except:
        err = QMessageBox()
        err.setText('error')
        err.exec_()

def umnoj():
    a = pole1.text()
    b =pole2.text()
    try:
        a = int(a)
        b = int(b)
        result = a * b
        otvet1.setText(str(result))

    except:
        err = QMessageBox()
        err.setText('error')
        err.exec_()

def delen():
    a = pole1.text()
    b =pole2.text()
    try:
        a = int(a)
        b = int(b)
        result = a / b
        otvet1.setText(str(result))

    except:
        err = QMessageBox()
        err.setText('error')
        err.exec_()

v4.clicked.connect(delen)
v1.clicked.connect(umnoj)
v3.clicked.connect(minus)
v2.clicked.connect(plus)

okno3.show()
app.exec_()