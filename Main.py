from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QProgressBar

app = QApplication([])

window = QWidget()
layout = QVBoxLayout()

window.setWindowTitle('Button Clicker')
window.setGeometry(100, 100, 400, 300)

button1 = QPushButton('Botón 1')
button2 = QPushButton('Botón 2')
button3 = QPushButton('Botón 3')

"""Listeners"""
x = 0
y = 0
z = 0

def actualizar(param):
    elegir_variable(param)
    actualizar_perCent()
    progressBar.setValue(perCent)
    completar()

def elegir_variable(param):
    if param == 1:
        global x
        x += 1
        panel1F.setText(string_x())
        print(x)
    elif param == 2:
        global y
        y += 1
        panel2F.setText(string_y())
        print(y)
    else:
        global z
        z += 1
        panel3F.setText(string_z())
        print(z)

def string_x():
    return str(x)

def string_y():
    return str(y)

def string_z():
    return str(z)

"""Progress bar"""
perCent = 0
def actualizar_perCent():
    global perCent
    perCent += 1
    print(perCent)

progressBar = QProgressBar()
progressBar.setValue(perCent)

def completar():
    if progressBar.value() == 100:
        global perCent
        print("Bien!!!! Has tocado 100 Botones!!!")
        perCent = 0
        progressBar.setValue(perCent)


button1.clicked.connect(lambda: actualizar(1))
button2.clicked.connect(lambda: actualizar(2))
button3.clicked.connect(lambda: actualizar(3))

"""Paneles de texto"""
panel1 = QLabel('Panel 1')
panel2 = QLabel('Panel 2')
panel3 = QLabel('Panel 3')
panel1F = QLabel(string_x())
panel2F = QLabel(string_y())
panel3F = QLabel(string_z())

layout.addWidget(panel1)
layout.addWidget(button1)
layout.addWidget(panel1F)
layout.addWidget(panel2)
layout.addWidget(button2)
layout.addWidget(panel2F)
layout.addWidget(panel3)
layout.addWidget(button3)
layout.addWidget(panel3F)
layout.addWidget(progressBar)
layout.addStretch()

layout.setAlignment(panel1, Qt.AlignCenter)
layout.setAlignment(panel2, Qt.AlignCenter)
layout.setAlignment(panel3, Qt.AlignCenter)
layout.setAlignment(panel1F, Qt.AlignCenter)
layout.setAlignment(panel2F, Qt.AlignCenter)
layout.setAlignment(panel3F, Qt.AlignCenter)

window.setLayout(layout)
window.show()

app.exec_()
