# Imports: PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QProgressBar, QGridLayout

# Clase principal de la aplicación heredada de QWidget (ventana básica de PyQt5)
class ButtonClickerApp(QWidget):
    def __init__(self):
        # Llama al constructor de la clase padre
        super().__init__()

        # Inicializa atributos
        self.progressBar = None
        self.paneles = []  # Inicializa la lista vacía
        self.total_clicks = 0
        self.completaciones = 0  # Inicializa el contador de completaciones
        self.contadores = [0, 0, 0]
        self.perCent = 0  # Inicializa la variable de porcentaje

        # Inicializa la interfaz gráfica
        self.initUI()

    # Función que configura la interfaz de usuario
    def initUI(self):
        # Ventanas
        self.setWindowTitle('Button Clicker')  # Título
        self.setGeometry(100, 100, 400, 300)  # Define el tamaño y posición de la ventana

        # Layout principal (Cuadrícula)
        layout = QGridLayout()
        layout.setVerticalSpacing(20)
        self.setLayout(layout)

        # Panel de completaciones
        panel0 = QLabel('Completaciones')
        self.completacionesCount = QLabel('0')  # Para mostrar el número de completaciones
        layout.addWidget(panel0, 0, 0, 1, 3)  # Alinea el texto de completaciones
        layout.addWidget(self.completacionesCount, 0, 1, 1, 2)  # Muestra el conteo de completaciones

        # Botones
        button1 = QPushButton('Botón 1')
        button1.setStyleSheet("background-color: red")

        button2 = QPushButton('Botón 2')
        button2.setStyleSheet("background-color: green")

        button3 = QPushButton('Botón 3')
        button3.setStyleSheet("background-color: blue")

        # Conectar botones a la función de actualización
        button1.clicked.connect(lambda: self.actualizar(0))
        button2.clicked.connect(lambda: self.actualizar(1))
        button3.clicked.connect(lambda: self.actualizar(2))

        # Paneles de texto
        panel1 = QLabel('Panel 1')
        panel1F = QLabel('0')  # Inicializa el contador para el panel 1
        panel2 = QLabel('Panel 2')
        panel2F = QLabel('0')  # Inicializa el contador para el panel 2
        panel3 = QLabel('Panel 3')
        panel3F = QLabel('0')  # Inicializa el contador para el panel 3

        # Añadir widgets al layout en las posiciones adecuadas
        layout.addWidget(panel0, 0, 0, 1, 3)  # Completaciones
        layout.addWidget(self.completacionesCount, 0, 1, 1, 2)  # Conteo de completaciones
        layout.addWidget(panel1, 1, 0)  # Panel 1
        layout.addWidget(button1, 1, 1)  # Botón 1
        layout.addWidget(panel1F, 1, 2)  # Contador Panel 1
        layout.addWidget(panel2, 2, 0)  # Panel 2
        layout.addWidget(button2, 2, 1)  # Botón 2
        layout.addWidget(panel2F, 2, 2)  # Contador Panel 2
        layout.addWidget(panel3, 3, 0)  # Panel 3
        layout.addWidget(button3, 3, 1)  # Botón 3
        layout.addWidget(panel3F, 3, 2)  # Contador Panel 3

        # Barra de progreso
        self.progressBar = QProgressBar()
        self.progressBar.setValue(self.perCent)  # Inicializamos la barra en 0
        layout.addWidget(self.progressBar, 4, 0, 1, 3)  # Añadimos la barra de progreso en la fila 4

        # Guardar los paneles de contadores en la lista
        self.paneles = [panel1F, panel2F, panel3F]  # Inicializa la lista de paneles con los contadores

        # Alinear todos los elementos al centro
        layout.setAlignment(panel0, Qt.AlignCenter)
        layout.setAlignment(panel1, Qt.AlignCenter)
        layout.setAlignment(panel2, Qt.AlignCenter)
        layout.setAlignment(panel3, Qt.AlignCenter)
        layout.setAlignment(self.completacionesCount, Qt.AlignCenter)
        layout.setAlignment(panel1F, Qt.AlignCenter)
        layout.setAlignment(panel2F, Qt.AlignCenter)
        layout.setAlignment(panel3F, Qt.AlignCenter)

    # Actualiza los contadores
    def actualizar(self, index):
        # Incrementar el contador del botón que fue presionado
        self.contadores[index] += 1

        # Actualizar el texto del QLabel que muestra el valor del contador
        self.paneles[index].setText(str(self.contadores[index]))  # Actualiza el panel correspondiente

        # Actualizar el total de clics realizados
        self.total_clicks += 1

        # Actualizamos el porcentaje para la barra de progreso
        self.perCent = (self.total_clicks % 100)
        self.progressBar.setValue(self.perCent)  # Actualiza la barra de progreso

        # Comprobar si se han hecho 100 clics
        if self.perCent == 0 and self.total_clicks > 0:
            print("Bien!!!! Has clicado 100 veces un botón!!!")
            self.completaciones += 1  # Incrementa el contador de completaciones
            self.completacionesCount.setText(str(self.completaciones))  # Actualiza el QLabel de completaciones
            self.progressBar.setValue(0)  # Reinicia la barra de progreso a 0

# Inicia la app
app = QApplication([])

# Instancia la ventana de la aplicación y la inicia
window = ButtonClickerApp()
window.show()

# Inicia el flujo de código de la app
app.exec_()
