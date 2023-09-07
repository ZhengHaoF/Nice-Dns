# include <QApplication>
# include <QWidget>
import json
import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QStringListModel, QCoreApplication, Qt
from PyQt5.QtWidgets import QMessageBox

import Dialog
import info
import niceDns
import ui  # 导入QtTest文件


class MyWindow:
    Ui = ui.Ui_MainWindow()
    # 高分辨率DPI屏幕自动缩放和去除弹窗的?按钮
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling | Qt.AA_DisableWindowContextHelpButton)

    def __init__(self):
        super().__init__()
        # 实例化列表模型，添加数据
        self.modifyList = QStringListModel()
        # 设置模型列表视图，加载数据列表
        self.modifyList.setStringList(niceDns.getModifyHost())

        # 实例化列表模型，添加数据
        self.domainList = QStringListModel()
        # 设置模型列表视图，加载数据列表
        self.domainList.setStringList(info.domainName)

        # 实例化列表模型，添加数据
        self.dnsList = QStringListModel()
        # 设置模型列表视图，加载数据列表
        self.dnsList.setStringList(info.server)

        app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QMainWindow()
        # 调自定义的界面（即刚转换的.py对象）
        self.Ui.setupUi(main_window)
        self.Ui.yesButton.clicked.connect(self.run)
        self.Ui.revButton.clicked.connect(self.rev)
        self.Ui.addDns.clicked.connect(self.addServer)
        self.Ui.refDnsButton.clicked.connect(self.refDnsButton)
        self.Ui.delItem.clicked.connect(self.delServer)
        # 设置列表视图的模型
        self.Ui.modifyList.setModel(self.modifyList)
        self.Ui.domainList.setModel(self.domainList)
        self.Ui.dnsList.setModel(self.dnsList)
        # 添加域名
        self.Ui.addDomain.clicked.connect(self.addDomain)

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

    # 添加域名
    def addDomain(self):
        Dlg = Dialog.Dlg()
        dom = Dlg.input("添加域名", "输入域名")
        if dom != "":
            info.domainName.append(dom)
            self.domainList.setStringList(info.domainName)
            self.Ui.domainList.setModel(self.domainList)
            info.info['domainName'] = info.domainName
            with open("info.json", "w") as f:
                json.dump(info.info, f)

    # 添加DNS服务
    def addServer(self):
        Dlg = Dialog.Dlg()
        dom = Dlg.input("添加DNS", "输入DNS")
        if dom != "":
            info.server.append(dom)
            self.dnsList.setStringList(info.server)
            self.Ui.dnsList.setModel(self.dnsList)
            info.info['server'] = info.server
            with open("info.json", "w") as f:
                json.dump(info.info, f)

    # 删除DNS服务
    def delServer(self):
        pass
        # self.dnsList.removeRow(0)
        # print(self.dnsList.currentRow())
        # Dlg = Dialog.Dlg()
        # dom = Dlg.input("添加DNS", "输入DNS")
        # if dom != "":
        #     info.server.append(dom)
        #     self.dnsList.setStringList(info.server)
        #     self.Ui.dnsList.setModel(self.dnsList)
        #     info.info['server'] = info.server
        #     with open("info.json", "w") as f:
        #         json.dump(info.info, f)

    # 刷新Dns缓存
    def refDnsButton(self):
        if os.system("ipconfig /flushdns") == 0:
            QMessageBox(QMessageBox.Question, '完成', '刷新Dns缓存成功').exec_()

