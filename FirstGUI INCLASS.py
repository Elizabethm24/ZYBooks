from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

def onClick():
    print("You clicked me!")
    button.setText("Ouch!")

app = QApplication()
window = QMainWindow()

window.setWindowTitle("My First GUI App")
button = QPushButton("Click me!")
button.clicked.connect(onClick)

window.setCentralWidget(button)
window.show()
app.exec()