# Imports: PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QProgressBar


# Clase principal de la aplicación heredada de QWidget (ventana básica de PyQt5)
class ButtonClickerApp(QWidget):
    def __init__(self):
        super().__init__()  # Llamamos al constructor de la clase padre

        # Inicializa atributos
        self.progressBar = None
        self.paneles = []  # Cambiado a una lista vacía desde el inicio
        self.total_clicks = 0  # Inicializado directamente a 0
        self.contadores = [0, 0, 0]  # Inicializa directamente la lista de contadores

        self.initUI()  # Inicializa la interfaz gráfica

    # Función que configura la interfaz de usuario
    def initUI(self):
        # Ventanas
        self.setWindowTitle('Button Clicker')  # Título
        self.setGeometry(100, 100, 400, 300)  # Define el tamaño y posición de la ventana

        # Layout principal (Vertical)
        layout = QVBoxLayout()
        self.setLayout(layout)  # Establece el layout como principal

        # Crea 3 botones y 3 paneles dinámicamente
        for i in range(3):
            # Crear un QLabel para cada "Panel X" (donde X es el número del panel)
            panel = QLabel(f'Panel {i + 1}')
            layout.addWidget(panel)  # Añadimos el panel al layout

            # Crear un botón que será "Botón X" y lo conectamos a la función 'actualizar'
            boton = QPushButton(f'Botón {i + 1}')

            # Metodo lambda que pasa el índice 'i' al metodo 'actualizar' cuando se hace clic
            boton.clicked.connect(lambda _, index=i: self.actualizar(index))

            # Añadimos el botón al layout
            layout.addWidget(boton)

            # Crear un QLabel para mostrar el valor del contador correspondiente
            panelF = QLabel(str(self.contadores[i]))  # Muestra el valor inicial (0) del contador
            layout.addWidget(panelF)  # Añadimos el QLabel al layout

            # Guarda el QLabel del contador en la lista de paneles
            self.paneles.append(panelF)

        # Crear una barra de progreso para mostrar los clics totales
        self.progressBar = QProgressBar()
        self.progressBar.setValue(0)  # Inicializamos la barra en 0
        self.progressBar.setFixedWidth(300)
        layout.addWidget(self.progressBar)  # Añadimos la barra de progreso al layout

        layout.addStretch()  # Mete un espacio flexible

        # Alinear los paneles de los contadores al centro del layout
        for panel in self.paneles:
            layout.setAlignment(panel, Qt.AlignCenter)

        # Alinear la barra de progreso al centro del layout
        layout.setAlignment(self.progressBar, Qt.AlignCenter)

    # Actualiza los contadores
    def actualizar(self, index):
        # Incrementar el contador del botón que fue presionado
        self.contadores[index] += 1

        # Actualizar el texto del QLabel que muestra el valor del contador
        self.paneles[index].setText(str(self.contadores[index]))

        # Actualizar el total de clics realizados
        self.total_clicks += 1

        # Actualizamos la barra de progreso, que se resetea cuando llega a 100
        self.progressBar.setValue((self.total_clicks % 100))

        # Si se han hecho exactamente 100 clics, mostramos un mensaje en la consola
        if self.total_clicks % 100 == 0:
            print("Bien!!!! Has tocado 100 botones!!!")
            self.progressBar.setValue(0)  # Reinicia la barra de progreso a 0


# Inicia la app
app = QApplication([])

# Instancia la ventana de la aplicación y la inicia
window = ButtonClickerApp()
window.show()

# Inicia el flujo de code de la app
app.exec_()
