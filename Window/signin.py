# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class SignIn_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SimpleNet")
        MainWindow.resize(274, 311)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 271, 254))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.usrLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.usrLabel.setObjectName("usrLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.usrLabel)
        self.usrLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.usrLineEdit.setObjectName("usrLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.usrLineEdit)
        self.passwrdLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.passwrdLineEdit.setObjectName("passwrdLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwrdLineEdit)
        self.passwrdLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.passwrdLabel.setObjectName("passwrdLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.passwrdLabel)
        self.signinpushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.signinpushButton.setAutoDefault(True)
        self.signinpushButton.setObjectName("signinpushButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.signinpushButton)
        self.CreatePpushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.CreatePpushButton.setAutoDefault(True)
        self.CreatePpushButton.setObjectName("CreatePpushButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.CreatePpushButton)
        self.CreateOpushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.CreateOpushButton.setAutoDefault(True)
        self.CreateOpushButton.setObjectName("CreateOpushButton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.CreateOpushButton)
        self.siginLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.siginLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.siginLabel.setObjectName("siginLabel")
        font = QtGui.QFont()
        font.setFamily("Jamrul")
        font.setPointSize(14)
        self.siginLabel.setFont(font)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.siginLabel)
        self.invalidUsrLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.invalidUsrLabel.setText("")
        self.invalidUsrLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.invalidUsrLabel.setObjectName("invalidUsrLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.invalidUsrLabel)
        self.verticalLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 274, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SimpleNet-LogIn"))
        self.usrLabel.setText(_translate("MainWindow", "Usuário:"))
        self.passwrdLabel.setText(_translate("MainWindow", "Senha:"))
        self.CreatePpushButton.setText(_translate("MainWindow", "Criar conta pessoal"))
        self.CreateOpushButton.setText(_translate("MainWindow", "Criar conta de uma organização"))
        self.siginLabel.setText(_translate("MainWindow", "Bem-vind@ à SimpleNet!"))
        self.signinpushButton.setText(_translate("MainWindow", "ENTRAR"))

