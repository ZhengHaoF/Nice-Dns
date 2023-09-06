from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QWidget, QLineEdit, QInputDialog

import uiStart


class Log:
    def consoleLog(self, text):
        log_text_edit = uiStart.MyWindow.Ui.logTextEdit
        log_text_edit.setPlainText(log_text_edit.toPlainText() + text + "\n")
        log_text_edit.moveCursor(QTextCursor.End)


class Dlg(QWidget):
    def input(self, title, text):
        # 第三个参数表示显示类型，可选，有正常（QLineEdit.Normal）、密碼（ QLineEdit. Password）、不显示（ QLineEdit. NoEcho）三种情况
        value, ok = QInputDialog.getText(self, "输入框标题", "这是提示信息\n\n请输入文本:", QLineEdit.Normal,
                                         "这是默认值")
        print(value)
        print(ok)
