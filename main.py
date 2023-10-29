from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from random import randint

app = QApplication([])

window = QWidget()
window.resize(200,100)


line = QVBoxLayout()

text = QLabel("random number:")
number = QLabel("?")
button = QPushButton("generate")


line.addWidget(text)
line.addWidget(number)
line.addWidget(button)

window.setLayout(line)

def generate_rand():
    r = randint(0,1000)
    number.setText(str(r))

button.clicked.connect(generate_rand)



window.show()
app.exec()
