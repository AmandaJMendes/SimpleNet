# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Menu_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(898, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 231, 236))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Jamrul")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.profilepushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.profilepushButton.setAutoDefault(True)
        self.profilepushButton.setObjectName("profilepushButton")
        self.verticalLayout.addWidget(self.profilepushButton)
        self.connspushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.connspushButton.setAutoDefault(True)
        self.connspushButton.setObjectName("connspushButton")
        self.verticalLayout.addWidget(self.connspushButton)
        self.searchpushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.searchpushButton.setObjectName("searchpushButton")
        self.searchpushButton.setAutoDefault(True)
        self.verticalLayout.addWidget(self.searchpushButton)
        self.graphpushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.graphpushButton.setAutoDefault(True)
        self.graphpushButton.setObjectName("graphpushButton")
        self.verticalLayout.addWidget(self.graphpushButton)
        self.logoutpushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.logoutpushButton.setAutoDefault(True)
        self.logoutpushButton.setObjectName("logoutpushButton")
        self.verticalLayout.addWidget(self.logoutpushButton)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(260, 10, 631, 126))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.postpushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.postpushButton.setAutoDefault(True)
        self.postpushButton.setObjectName("postpushButton")
        self.gridLayout.addWidget(self.postpushButton, 0, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(260, 140, 631, 501))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget_3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 625, 413))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SimpleNet-Menu"))
        self.label_2.setText(_translate("MainWindow", "SimpleNet"))
        self.profilepushButton.setText(_translate("MainWindow", "Meu perfil"))
        self.connspushButton.setText(_translate("MainWindow", "Minhas conexões"))
        self.searchpushButton.setText(_translate("MainWindow", "Buscar perfil"))
        self.graphpushButton.setText(_translate("MainWindow", "Visualizar grafo"))
        self.logoutpushButton.setText(_translate("MainWindow", "Sair"))
        self.postpushButton.setText(_translate("MainWindow", "Postar"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Digite sua nova postagem"))
        self.label.setText(_translate("MainWindow", "Filtre as postagens por usuário:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Todas"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Minhas"))
        self.pushButton_2.setText(_translate("MainWindow", "Aplicar "))
        self.pushButton.setText(_translate("MainWindow", "Atualizar"))
