# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

mailList = []

def getAllMail():
    global mailList
    with open('./data/mails.txt', 'r+') as reader:
        mails = reader.readlines()
        mailList = [x.strip() for x in mails]        

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 320)
        MainWindow.setMinimumSize(QtCore.QSize(700, 320))
        MainWindow.setMaximumSize(QtCore.QSize(700, 320))
        MainWindow.setStyleSheet("QDialog{\n"
"    background-color: #3bc6d1;\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(MainWindow)
        self.horizontalLayout.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon = QtWidgets.QPushButton(MainWindow)
        self.icon.setMinimumSize(QtCore.QSize(300, 300))
        self.icon.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.icon.setFont(font)
        self.icon.setStyleSheet("border-radius: 20px;")
        self.icon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../design/images/PCMAIL.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon.setIcon(icon)
        self.icon.setIconSize(QtCore.QSize(300, 300))
        self.icon.setObjectName("icon")
        self.horizontalLayout.addWidget(self.icon)
        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setMinimumSize(QtCore.QSize(0, 300))
        self.frame.setMaximumSize(QtCore.QSize(1000, 300))
        self.frame.setStyleSheet("QFrame#frame{\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#add:pressed{\n"
"    padding-left: 3px;\n"
"    padding-top: 3px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(5, 5, 5, 10)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("border: 2px solid #34b2bb;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"color: #009ba1;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.scroll = QtWidgets.QScrollArea(self.frame)
        self.scroll.setMinimumSize(QtCore.QSize(0, 200))
        self.scroll.setMaximumSize(QtCore.QSize(16777215, 200))
        self.scroll.setStyleSheet("QWidget#widget{\n"
"    background-color: white;\n"
"}\n"
"")
        self.scroll.setWidgetResizable(True)
        self.scroll.setObjectName("scroll")
        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(0, 0, 356, 198))
        self.widget.setObjectName("widget")
        self.layout = QtWidgets.QGridLayout()
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        
        
        self.widget.setLayout(self.layout)
        self.scroll.setWidget(self.widget)
        self.verticalLayout.addWidget(self.scroll)
        self.add = QtWidgets.QPushButton(self.frame,  clicked=lambda: self.addMail(MainWindow))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy)
        self.add.setMinimumSize(QtCore.QSize(200, 30))
        self.add.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.add.setFont(font)
        self.add.setStyleSheet("border: 2px solid #34b2bb;\n"
"background-color: white;\n"
"color: #009ba1;\n"
"border-radius: 10px;")
        self.add.setIconSize(QtCore.QSize(0, 0))
        self.add.setObjectName("add")
        self.verticalLayout.addWidget(self.add, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(MainWindow)
        self.init()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def remove(self, lbl, btn):
        self.layout.removeWidget(lbl)
        self.layout.removeWidget(btn)
        mail = lbl.text()
        idx = mailList.index(mail)
        mailList.pop(idx)
        lbl.deleteLater()
        btn.deleteLater()
        with open('./data/mails.txt', 'w') as writer:
            for mail in mailList:
                writer.write(mail)

    def addWidget(self, text, i, flag=True):
        lbl = QtWidgets.QLabel(text)

        btn = QtWidgets.QPushButton('Remove', clicked=lambda:self.remove(lbl, btn))
        btn.setMinimumSize(100, 32)
        btn.setMaximumSize(100, 32)
        self.layout.addWidget(lbl, i, 0)
        self.layout.addWidget(btn, i, 1)
        if flag:
            mailList.append(text)
        with open('./data/mails.txt', 'w') as writer:
            for mail in mailList:
                writer.write(mail + '\n')

    def init(self):
        for i, text in enumerate(mailList):
            self.addWidget(text, i, False)


    def addMail(self, par):
        text, ok = QtWidgets.QInputDialog.getText(par, 'Input', 'Input Controller Mail:')
        if ok:
            if text != '' and text not in mailList:
                self.addWidget(text, len(mailList))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PC Mail Controller"))
        self.label.setText(_translate("MainWindow", "Controllers"))
        self.add.setText(_translate("MainWindow", "Add Control Mail"))

if __name__ == "__main__":
    import sys
    getAllMail()
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())