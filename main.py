import sys

from PyQt5.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
                             QPushButton, QSizePolicy, QWidget)


class Calculadora(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(400, 400)
        self.central_Widget = QWidget()
        self.grid = QGridLayout(self.central_Widget)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '''QLineEdit { background-color: #fff, color: #000,
            font: bold 30px }'''
        )
        self.display.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding
        )

        # criando os caracteres da calculadora
        count_7_to_9 = 0
        count_4_to_6 = 0
        count_1_to_3 = 0
        for i in range(0, 10):
            if i >= 1 and i <= 3:
                self.add_buttons(QPushButton(f'{i}'), 3, count_1_to_3, 1, 1)
                count_1_to_3 += 1

            if i >= 4 and i <= 6:
                self.add_buttons(QPushButton(f'{i}'), 2, count_4_to_6, 1, 1)
                count_4_to_6 += 1

            if i >= 7:
                self.add_buttons(QPushButton(f'{i}'), 1, count_7_to_9, 1, 1)
                count_7_to_9 += 1

        # caracteres dos sinais da operação
        self.add_buttons(QPushButton('+'), 1, 3, 1, 1,
                         lambda: self.exec_operator('+'))
        self.add_buttons(QPushButton('-'), 2, 3, 1, 1,
                         lambda: self.exec_operator('-'))
        self.add_buttons(QPushButton('/'), 3, 3, 1, 1,
                         lambda: self.exec_operator('/'))
        self.add_buttons(QPushButton('*'), 4, 3, 1, 1,
                         lambda: self.exec_operator('*'))
        self.add_buttons(QPushButton('^'), 4, 2, 1, 1,
                         lambda: self.exec_operator('**'))

        # caracteres dos demais sinais da calculadora
        self.add_buttons(QPushButton('C'), 2, 4, 1, 1,
                         lambda: self.display.setText(''),
                         '''background: #8c1812; color: #fff; font-weight: 700;
                         border-radius:5px'''
                         )
        self.add_buttons(QPushButton('⌫'), 3, 4, 1, 1,
                         lambda: self.display.setText(
            self.display.text()[:-1]
        ),
            '''background: #000; color: #fff;
                            font-weight: 700; border-radius:5px''')
        self.add_buttons(QPushButton('0'), 4, 1, 1, 1)
        self.add_buttons(QPushButton('.'), 4, 0, 1, 1)
        self.add_buttons(QPushButton('='), 4, 4, 1, 1, self.result,
                         '''background: #13823a; color: #fff; font-weight: 700;
                         border-radius:5px''')

        self.setCentralWidget(self.central_Widget)

    def add_buttons(
            self, btn, row: int, col: int, rowspan: int,
            colspan: int, function=None, style=None,) -> None:

        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not function:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(function)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def result(self) -> None:
        try:
            self.display.setText(
                str(
                    eval(f'{self.first_numbers}{self.display.text()}')
                )
            )

        except Exception as error:
            self.display.setText('Conta inválida')
            raise Exception(error, 'Digita direito ai mermao')

    def exec_operator(self, operator: str) -> None:
        self.first_numbers = f'''{self.display.text()}{operator}'''
        self.display.setText('')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calculator = Calculadora()
    calculator.show()
    qt.exec_()
