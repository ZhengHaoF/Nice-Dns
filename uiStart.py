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
        self.domainList.setStringList(info.domainListRow)

        # 实例化列表模型，添加数据
        self.dnsList = QStringListModel()
        # 设置模型列表视图，加载数据列表
        self.dnsList.setStringList(info.dnsListRow)

        app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QMainWindow()
        # 调自定义的界面（即刚转换的.py对象）
        self.Ui.setupUi(main_window)
        self.Ui.yesButton.clicked.connect(self.run)
        self.Ui.revButton.clicked.connect(self.rev)
        self.Ui.addDns.clicked.connect(self.addServer)
        self.Ui.refDnsButton.clicked.connect(self.refDnsButton)
        self.Ui.revDnsAndDom.clicked.connect(self.revDnsAndDom)
        self.Ui.delItem.clicked.connect(self.delItme)
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
        self.domainList.setStringList(info.domainListRow)
        self.Ui.domainList.setModel(self.domainList)
        self.dnsList.setStringList(info.dnsListRow)
        self.Ui.dnsList.setModel(self.dnsList)

    # 添加域名
    def addDomain(self):
        Dlg = Dialog.Dlg()
        dom = Dlg.input("添加域名", "输入域名")
        if dom != "":
            info.domainListRow.append(dom)
            self.domainList.setStringList(info.domainListRow)
            self.Ui.domainList.setModel(self.domainList)
            info.info['domainName'] = info.domainListRow
            with open("info.json", "w") as f:
                json.dump(info.info, f)

    # 添加DNS服务
    def addServer(self):
        Dlg = Dialog.Dlg()
        dom = Dlg.input("添加DNS", "输入DNS")
        if dom != "":
            info.dnsListRow.append(dom)
            self.dnsList.setStringList(info.dnsListRow)
            self.Ui.dnsList.setModel(self.dnsList)
            info.info['server'] = info.dnsListRow
            with open("info.json", "w") as f:
                json.dump(info.info, f)

    # 删除DNS服务
    def delItme(self):
        if self.Ui.dnsList.currentIndex().row() != -1:
            del info.dnsListRow[self.Ui.dnsList.currentIndex().row()]
            self.dnsList.setStringList(info.dnsListRow)
            self.Ui.dnsList.setModel(self.dnsList)
            with open("info.json", "w") as f:
                json.dump(info.info, f)

        if self.Ui.domainList.currentIndex().row() != -1:
            del info.domainListRow[self.Ui.domainList.currentIndex().row()]
            self.domainList.setStringList(info.domainListRow)
            self.Ui.domainList.setModel(self.domainList)
            with open("info.json", "w") as f:
                json.dump(info.info, f)

    # 刷新Dns缓存
    def refDnsButton(self):
        if os.system("ipconfig /flushdns") == 0:
            QMessageBox(QMessageBox.Question, '完成', '刷新Dns缓存成功').exec_()  # 刷新Dns缓存

    # 还原DNS和域名
    def revDnsAndDom(self):
        row = {
            "dns": [
                "8.8.8.8",
                "114.114.114.114",
                "1.1.1.1",
                "119.29.29.29",
                "182.254.116.116",
                "223.5.5.5",
                "223.6.6.6",
                "180.76.76.76",
                "9.9.9.9",
                "149.112.112.112",
                "208.67.222.222",
                "101.101.101.101"
            ],
            "domain": [
                "github.com",
                "api.github.com",
                "github.githubassets.com",
                "favicons.githubusercontent.com",
                "raw.githubusercontent.com"
            ]
        }
        info.info = row
        info.dnsListRow = info.info['dns']
        info.domainListRow = info.info['domain']
        self.dnsList.setStringList(info.dnsListRow)
        self.domainList.setStringList(info.domainListRow)
        self.Ui.dnsList.setModel(self.dnsList)
        self.Ui.domainList.setModel(self.domainList)

        with open("info.json", "w") as f:
            json.dump(info.info, f)
