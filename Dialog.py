from PyQt5.QtWidgets import QWidget, QLineEdit, QInputDialog


class Dlg(QWidget):
    def input(self, title, text) -> str:
        # 第三个参数表示显示类型，可选，有正常（QLineEdit.Normal）、密碼（ QLineEdit. Password）、不显示（ QLineEdit. NoEcho）三种情况
        Dialog = QInputDialog()
        Dialog.setFixedSize(1000, 1000)
        value, ok = Dialog.getText(self, title, text, QLineEdit.Normal, "")
        if ok:
            return value
        else:
            return ""
