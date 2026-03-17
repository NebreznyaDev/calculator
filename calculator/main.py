import sys
from typing import Union, Optional
from operator import add, sub, mul, truediv


from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile

from design import Ui_MainWindow

operations = {
    '+': add,
    '−': sub,
    '×': mul,
    '/': truediv
}

from decimal import *

print('1.2 - 1 =', Decimal('1.2') - Decimal('1'))
print('3.4 + 4.3 =', Decimal('3.4') + Decimal('4.3'))
print('0.2 + 0.1 =', Decimal('0.2') + Decimal('0.1'))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # digits
        self.ui.BTN_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.BTN_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.BTN_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.BTN_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.BTN_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.BTN_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.BTN_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.BTN_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.BTN_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.BTN_9.clicked.connect(lambda: self.add_digit('9'))

        # actions
        self.ui.BTM_CLEAR.clicked.connect(self.clear_all)
        self.ui.BTN_CE.clicked.connect(self.clear_entry)
        self.ui.BTN_POINT.clicked.connect(self.add_point)
        self.ui.BTM_SUB.clicked.connect(self.negate)
        self.ui.BTN_BACKPASE.clicked.connect(self.backspace)


        #math

        self.ui.BTM_EQU.clicked.connect(self.calculate)
        self.ui.BTN_PLUS.clicked.connect(lambda: self.math_operation('+'))
        self.ui.BTN_NEG.clicked.connect(lambda: self.math_operation('−'))
        self.ui.BTN_MUL.clicked.connect(lambda: self.math_operation('×'))
        self.ui.BTN_DIV.clicked.connect(lambda: self.math_operation('/'))



    def add_digit(self, btn_text: str) -> None:
        if self.ui.le_entry.text() == "0":
            self.ui.le_entry.setText(btn_text)

        else:
         self.ui.le_entry.setText(self.ui.le_entry.text() + btn_text)

    def clear_all(self) -> None:
        self.ui.le_entry.setText('0')
        self.ui.lbl_temp.clear()

    def clear_entry(self) -> None:
        self.ui.le_entry.setText('0')

    def add_point(self) -> None:
        if '.' not in self.ui.le_entry.text():
            self.ui.le_entry.setText(self.ui.le_entry.text() + '.')

    def add_temp(self, math_sign: str):
        if not self.ui.lbl_temp.text() or self.get_math_sign() == '=':
            self.ui.lbl_temp.setText(self.remove_trailing_zeros(self.ui.le_entry.text()) + f' {math_sign}')
            self.ui.le_entry.setText('0')

    def get_entry_num(self) -> int | float:
        entry = self.ui.le_entry.text().strip('.')


        return float(entry) if '.' in entry else int(entry)

    def add_temp(self, operation) -> None:
        btn = self.sender()
        entry = self.remove_trailing_zeros(self.ui.le_entry.text())


        if not self.ui.lbl_temp.text() or self.get_math_sign() == '=':
            self.ui.lbl_temp.setText(self.ui.le_entry.text () + f' {operation} ')
            self.ui.le_entry.setText('0')

    def get_temp_num(self) -> Union[int, float, None]:
        if self.ui.lbl_temp.text():
            temp = self.ui.lbl_temp.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)

    def get_math_sign(self)  -> Optional[str]:
        if self.ui.lbl_temp.text():
            return self.ui.lbl_temp.text().strip('.').split()[-1]

    def calculate(self) -> Optional[str]:
        entry = self.ui.le_entry.text()
        temp = self.ui.lbl_temp.text()

        if temp:
            try:
                result = self.remove_trailing_zeros(
                    str(operations[self.get_math_sign()](
                        self.get_temp_num(),
                        self.get_entry_num()
                    ))
                )

                self.ui.lbl_temp.setText(temp + self.remove_trailing_zeros(entry) + ' =')
                self.ui.le_entry.setText(result)

                return result
            except KeyError:
                pass
            except ZeroDivisionError:
                if self.get_temp_num() == 0:
                    self.show_error(error_undefined)
                else:
                    self.show_error(error_zero_div)

    def remove_trailing_zeros(self, num: str) -> str:
        if '.' in num:
            num = num.rstrip('0').rstrip('.')
        return num

    def math_operation(self, math_sign: str):
        temp = self.ui.lbl_temp.text()

        if not temp:
            self.add_temp(math_sign)
        else:
            if self.get_math_sign() != math_sign:
                if self.get_math_sign() == '=':
                    self.add_temp(math_sign)
                else:
                    self.ui.lbl_temp.setText(temp[:-2] + f'{math_sign} ')
            else:
                self.ui.lbl_temp.setText(self.calculate() + f' {math_sign}')

    def negate(self) -> None:
        entry = self.ui.le_entry.text()

        if '-' not in entry:
            if entry != '0':
                entry = '-' + entry
        else:
            entry = entry[1:]

        self.ui.le_entry.setText(entry)

    def backspace(self) -> None:
        entry = self.ui.le_entry.text()

        if len(entry) != 1:
            if len(entry) == 2 and '-' in entry:
                self.ui.le_entry.setText('0')
            else:
                self.ui.le_entry.setText(entry[:-1])
        else:
            self.ui.le_entry.setText('0')



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())