# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gResult.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(845, 632)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 831, 618))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tree_result = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tree_result.setFont(font)
        self.tree_result.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tree_result.setObjectName("tree_result")
        self.tree_result.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tree_result.headerItem().setFont(0, font)
        self.tree_result.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tree_result.headerItem().setFont(1, font)
        self.tree_result.headerItem().setTextAlignment(2, QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tree_result.headerItem().setFont(2, font)
        self.tree_result.headerItem().setTextAlignment(3, QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tree_result.headerItem().setFont(3, font)
        self.tree_result.headerItem().setTextAlignment(4, QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tree_result.headerItem().setFont(4, font)
        self.tree_result.headerItem().setTextAlignment(5, QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tree_result.headerItem().setFont(5, font)
        self.verticalLayout.addWidget(self.tree_result)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Search Result"))
        self.tree_result.headerItem().setText(0, _translate("Form", "New Column"))
        self.tree_result.headerItem().setText(1, _translate("Form", "New Column"))
        self.tree_result.headerItem().setText(2, _translate("Form", "New Column"))
        self.tree_result.headerItem().setText(3, _translate("Form", "New Column"))
        self.tree_result.headerItem().setText(4, _translate("Form", "New Column"))
        self.tree_result.headerItem().setText(5, _translate("Form", "New Column"))
