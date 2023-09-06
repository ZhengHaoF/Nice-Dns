# include <QApplication>
# include <QWidget>
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QMessageBox, QWidget, QLineEdit, QInputDialog

import Dialog
import niceDns
import ui  # 导入QtTest文件


class MyWindow:
    server = []
    domainName = []
    Ui = ui.Ui_MainWindow()

    def __init__(self, server, domainName):
        self.server = server
        self.domainName = domainName
        super().__init__()
        # 实例化列表模型，添加数据
        self.modifyList = QStringListModel()
        # 设置模型列表视图，加载数据列表
        self.modifyList.setStringList(niceDns.getModifyHost())

        # 实例化列表模型，添加数据
        self.domainList = QStringListModel()
        # 设置模型列表视图，加载数据列表
        self.domainList.setStringList(self.domainName)

        # 实例化列表模型，添加数据
        self.dnsList = QStringListModel()
        # 设置模型列表视图，加载数据列表
        self.dnsList.setStringList(self.server)

        app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QMainWindow()
        # 调自定义的界面（即刚转换的.py对象）
        self.Ui.setupUi(main_window)
        self.Ui.yesButton.clicked.connect(self.run)
        self.Ui.revButton.clicked.connect(self.rev)
        # 设置列表视图的模型
        self.Ui.modifyList.setModel(self.modifyList)
        self.Ui.domainList.setModel(self.domainList)
        self.Ui.dnsList.setModel(self.dnsList)

        # 刷新
        self.Ui.refButton.clicked.connect(self.ref)
        # 显示窗口并释放资源
        main_window.show()
        sys.exit(app.exec_())

    # 运行
    def run(self):
        niceDns.run()
        self.modifyList.setStringList(niceDns.getModifyHost())
        QMessageBox(QMessageBox.Question, '完成', '执行成功').exec_()

    # 还原
    def rev(self):
        niceDns.cleanHost()
        self.modifyList.setStringList(niceDns.getModifyHost())

    def ref(self):
        self.modifyList.setStringList(niceDns.getModifyHost())
        self.Ui.logTextEdit.clear()
