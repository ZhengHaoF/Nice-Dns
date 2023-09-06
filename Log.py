from PyQt5.QtGui import QTextCursor

import uiStart


class Log:
    def consoleLog(self, text):
        log_text_edit = uiStart.MyWindow.Ui.logTextEdit
        log_text_edit.setPlainText(log_text_edit.toPlainText() + text + "\n")
        log_text_edit.moveCursor(QTextCursor.End)
