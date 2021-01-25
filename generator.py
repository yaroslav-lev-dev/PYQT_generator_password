from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt,  QCoreApplication
from PyQt5.QtGui import QIcon
import sys
from design import Ui_form

from random import choices

import time
import datetime

SYMBOL_USE_DIGIT = "0123456789"
SYMBOL_USE_LETTERS = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
SYMBOL_USE_SYMBOLS_AND_SPECIAL = "_-@#$%^&*!?/|"

#----- {Создание приложения} -----
app = QtWidgets.QApplication(sys.argv)

#----- {Создание формы} ----
form = QtWidgets.QWidget()
ui = Ui_form()
ui.setupUi(form)
form.show()

#----- {Код всего приложения} ----

def pressedGet():
    result_charaster = ""
    if ui.select_use_digit.checkState():
        global SYMBOL_USE_DIGIT
        result_charaster += SYMBOL_USE_DIGIT

    if ui.select_use_letters.checkState():
        global SYMBOL_USE_LETTERS
        result_charaster += SYMBOL_USE_LETTERS

    if ui.select_use_spec_symbols.checkState():
        global SYMBOL_USE_SYMBOLS_AND_SPECIAL
        result_charaster += SYMBOL_USE_SYMBOLS_AND_SPECIAL

    try:
        result_charaster = choices(result_charaster, k=len(result_charaster))

        count_password_symbols = ui.select_count.value()

        result_charaster =   choices(result_charaster, k=count_password_symbols)

        ui.received_password.setPlainText("".join(result_charaster))

    except IndexError:
          ui.received_password.setPlainText("Ошибка! Предположительно вы не выбрали не один из вариантов создания пароля!")

ui.get_generator_password.clicked.connect( pressedGet )


#----- {Запуск приложения} ----
sys.exit(app.exec_())

time.sleep(3)