# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uix-design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName("form")
        form.setWindowModality(QtCore.Qt.NonModal)
        form.resize(372, 311)
        form.setStyleSheet("QWidget#form {\n"
"    background-color: rgb(85, 170, 0);\n"
"}")
        self.select_count = QtWidgets.QSpinBox(form)
        self.select_count.setGeometry(QtCore.QRect(30, 70, 311, 22))
        self.select_count.setStyleSheet("QSpinBox#select_count {\n"
"    color: gray;\n"
"    border: 1px solid gray;\n"
"}")
        self.select_count.setInputMethodHints(QtCore.Qt.ImhNone)
        self.select_count.setWrapping(False)
        self.select_count.setAlignment(QtCore.Qt.AlignCenter)
        self.select_count.setReadOnly(False)
        self.select_count.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.select_count.setAccelerated(True)
        self.select_count.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.select_count.setKeyboardTracking(False)
        self.select_count.setPrefix("")
        self.select_count.setMinimum(1)
        self.select_count.setMaximum(74)
        self.select_count.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.select_count.setProperty("value", 8)
        self.select_count.setObjectName("select_count")
        self.label_form = QtWidgets.QLabel(form)
        self.label_form.setGeometry(QtCore.QRect(80, 10, 201, 31))
        self.label_form.setStyleSheet("QLabel#label_form {\n"
"    \n"
"    font: 87 18px \"Arial Black\";\n"
"    color: white;\n"
"}")
        self.label_form.setObjectName("label_form")
        self.label_select_count = QtWidgets.QLabel(form)
        self.label_select_count.setGeometry(QtCore.QRect(60, 40, 231, 31))
        self.label_select_count.setStyleSheet("QLabel#label_select_count {\n"
"    \n"
"    font: 87 13px \"Arial Narrow\";\n"
"    color: white;\n"
"}")
        self.label_select_count.setAlignment(QtCore.Qt.AlignCenter)
        self.label_select_count.setObjectName("label_select_count")
        self.select_use_digit = QtWidgets.QCheckBox(form)
        self.select_use_digit.setGeometry(QtCore.QRect(40, 120, 141, 21))
        self.select_use_digit.setStyleSheet("QCheckBox#select_use_digit {\n"
"    color: white;\n"
"    font: 87 13px \"Arial Narrow\";\n"
"}\n"
"")
        self.select_use_digit.setTristate(False)
        self.select_use_digit.setObjectName("select_use_digit")
        self.select_use_letters = QtWidgets.QCheckBox(form)
        self.select_use_letters.setGeometry(QtCore.QRect(200, 120, 141, 21))
        self.select_use_letters.setStyleSheet("QCheckBox#select_use_letters {\n"
"    color: white;\n"
"    font: 87 13px \"Arial Narrow\";\n"
"}\n"
"")
        self.select_use_letters.setTristate(False)
        self.select_use_letters.setObjectName("select_use_letters")
        self.select_use_spec_symbols = QtWidgets.QCheckBox(form)
        self.select_use_spec_symbols.setGeometry(QtCore.QRect(50, 150, 271, 21))
        self.select_use_spec_symbols.setStyleSheet("QCheckBox#select_use_spec_symbols {\n"
"    color: white;\n"
"    font: 87 13px \"Arial Narrow\";\n"
"}\n"
"")
        self.select_use_spec_symbols.setTristate(False)
        self.select_use_spec_symbols.setObjectName("select_use_spec_symbols")
        self.get_generator_password = QtWidgets.QPushButton(form)
        self.get_generator_password.setGeometry(QtCore.QRect(70, 190, 231, 31))
        self.get_generator_password.setStyleSheet("QPushButton#get_generator_password {\n"
"    color: gray;\n"
"    background-color: white;    \n"
"    font: 16px \"Arial Narrow\";\n"
"}\n"
"\n"
"QPushButton#get_generator_password:pressed {\n"
"    border: 2px solid gray;\n"
"}")
        self.get_generator_password.setCheckable(False)
        self.get_generator_password.setAutoRepeat(False)
        self.get_generator_password.setAutoExclusive(False)
        self.get_generator_password.setAutoDefault(False)
        self.get_generator_password.setDefault(False)
        self.get_generator_password.setFlat(False)
        self.get_generator_password.setObjectName("get_generator_password")
        self.received_password = QtWidgets.QPlainTextEdit(form)
        self.received_password.setGeometry(QtCore.QRect(30, 240, 311, 51))
        self.received_password.setStyleSheet("QPlainTextEdit#received_password {\n"
"    color:gray;\n"
"    font: 14px \"Arial Narrow\";\n"
"    border:none;\n"
"    border: 1px solid gray;\n"
"}\n"
"")
        self.received_password.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.received_password.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.received_password.setTabChangesFocus(False)
        self.received_password.setUndoRedoEnabled(False)
        self.received_password.setReadOnly(False)
        self.received_password.setOverwriteMode(False)
        self.received_password.setTabStopWidth(80)
        self.received_password.setBackgroundVisible(False)
        self.received_password.setCenterOnScroll(False)
        self.received_password.setObjectName("received_password")

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "Form"))
        self.select_count.setSuffix(_translate("form", " сиволов"))
        self.label_form.setText(_translate("form", "Генератор паролей"))
        self.label_select_count.setText(_translate("form", "Выберите количество символов для пароля"))
        self.select_use_digit.setText(_translate("form", "использовать цифры"))
        self.select_use_letters.setText(_translate("form", "использовать буквы"))
        self.select_use_spec_symbols.setText(_translate("form", "использовать спец.символы и знаки препинания"))
        self.get_generator_password.setText(_translate("form", "Сгенерировать пароль"))
        self.received_password.setPlainText(_translate("form", "Если вас не устраивает сгенерированный пароль - то нажмите кнопку еще раз!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = Ui_form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())