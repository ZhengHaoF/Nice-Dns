from PyQt5.QtWidgets import QWidget, QLineEdit, QInputDialog


class Dlg(QWidget):
    def input(self, title, text):
        # 第三个参数表示显示类型，可选，有正常（QLineEdit.Normal）、密碼（ QLineEdit. Password）、不显示（ QLineEdit. NoEcho）三种情况
        value, ok = QInputDialog.getText(self, title, text, QLineEdit.Normal, "")
        print(value)
        print(ok)
