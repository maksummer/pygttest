from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton



from PyQt5.QtCore import Qt


app = QApplication([])
window = QWidget()
window.resize(400,300)

main_line = QVBoxLayout()

H1 = QHBoxLayout()
H2 = QHBoxLayout()
H3 = QHBoxLayout()

guestion = QLabel("Який зараз рік")

Btn_answer = QRadioButton("2023")
btn_wrong1 = QRadioButton("2000")
btn_wrong2 = QRadioButton("2129")
btn_wrong3 = QRadioButton("2390")

H1.addWidget(guestion, alignment=Qt.AlignCenter)

H2.addWidget(btn_wrong2, alignment=Qt.AlignCenter)
H2.addWidget(btn_wrong1, alignment=Qt.AlignCenter)

H3.addWidget(Btn_answer, alignment=Qt.AlignCenter)
H3.addWidget(btn_wrong3, alignment=Qt.AlignCenter)

main_line.addLayout(H1)
main_line.addLayout(H2)
main_line.addLayout(H3)

window.setLayout(main_line)

def show_win():
    msg = QMessageBox()
    msg.setText("Правильно ти виграв 250 тис тон тротила")
    msg.exec()

def show_lose():
    msg = QMessageBox()
    msg.setText("Японська армия розлютилась для тебе буде казнь")
    msg.exec()

Btn_answer.clicked.connect(show_win)

btn_wrong1.clicked.connect(show_lose)
btn_wrong2.clicked.connect(show_lose)
btn_wrong3.clicked.connect(show_lose)

window.show()
app.exec()

