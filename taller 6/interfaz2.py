from PyQt5.QtWidgets import QApplication, QLabel, QWidget
import sys

app = QApplication(sys.argv)
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ejemplo PyQt5")
        self.setGeometry(100, 100, 400, 300)

        label = QLabel("¡Hola, PyQt5!", self)
        label.move(150, 130)

# Crear la ventana principal
window = MainWindow()
window.show()

# Ejecutar la aplicación
sys.exit(app.exec_())