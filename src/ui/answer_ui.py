# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'answer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Answer(object):
    def setupUi(self, Answer):
        Answer.setObjectName("Answer")
        Answer.resize(693, 328)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Answer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(Answer)
        self.toolBox.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.toolBox.setObjectName("toolBox")
        self.bloodPage = QtWidgets.QWidget()
        self.bloodPage.setGeometry(QtCore.QRect(0, 0, 679, 170))
        self.bloodPage.setObjectName("bloodPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.bloodPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEditBlood = QtWidgets.QTextEdit(self.bloodPage)
        self.textEditBlood.setReadOnly(True)
        self.textEditBlood.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.textEditBlood.setTabStopWidth(78)
        self.textEditBlood.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEditBlood.setObjectName("textEditBlood")
        self.verticalLayout_3.addWidget(self.textEditBlood)
        self.toolBox.addItem(self.bloodPage, "")
        self.urinePage = QtWidgets.QWidget()
        self.urinePage.setGeometry(QtCore.QRect(0, 0, 679, 170))
        self.urinePage.setObjectName("urinePage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.urinePage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textEditUrine = QtWidgets.QTextEdit(self.urinePage)
        self.textEditUrine.setReadOnly(True)
        self.textEditUrine.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.textEditUrine.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEditUrine.setObjectName("textEditUrine")
        self.verticalLayout_4.addWidget(self.textEditUrine)
        self.toolBox.addItem(self.urinePage, "")
        self.liverPage = QtWidgets.QWidget()
        self.liverPage.setGeometry(QtCore.QRect(0, 0, 679, 170))
        self.liverPage.setObjectName("liverPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.liverPage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textEditLiver = QtWidgets.QTextEdit(self.liverPage)
        self.textEditLiver.setReadOnly(True)
        self.textEditLiver.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.textEditLiver.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEditLiver.setObjectName("textEditLiver")
        self.verticalLayout_5.addWidget(self.textEditLiver)
        self.toolBox.addItem(self.liverPage, "")
        self.verticalLayout.addWidget(self.toolBox)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.returnBtn = QtWidgets.QPushButton(Answer)
        self.returnBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.returnBtn.setToolTipDuration(10)
        self.returnBtn.setObjectName("returnBtn")
        self.horizontalLayout.addWidget(self.returnBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.fontComboBox = QtWidgets.QFontComboBox(Answer)
        self.fontComboBox.setToolTipDuration(10)
        self.fontComboBox.setObjectName("fontComboBox")
        self.horizontalLayout.addWidget(self.fontComboBox)
        self.printBtn = QtWidgets.QPushButton(Answer)
        self.printBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.printBtn.setToolTipDuration(10)
        self.printBtn.setObjectName("printBtn")
        self.horizontalLayout.addWidget(self.printBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Answer)
        self.toolBox.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Answer)

    def retranslateUi(self, Answer):
        _translate = QtCore.QCoreApplication.translate
        Answer.setWindowTitle(_translate("Answer", "Form"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.bloodPage), _translate("Answer", "blood"))
        self.toolBox.setItemToolTip(self.toolBox.indexOf(self.bloodPage), _translate("Answer", "Click on this page, to check informations about your blood tests result"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.urinePage), _translate("Answer", "urine"))
        self.toolBox.setItemToolTip(self.toolBox.indexOf(self.urinePage), _translate("Answer", "Click on this page, to check informations about your urine tests result"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.liverPage), _translate("Answer", "liver"))
        self.toolBox.setItemToolTip(self.toolBox.indexOf(self.liverPage), _translate("Answer", "Click on this page, to check informations about your liver tests result"))
        self.returnBtn.setToolTip(_translate("Answer", "Click here, if you want to return to main window"))
        self.returnBtn.setText(_translate("Answer", "Return"))
        self.fontComboBox.setToolTip(_translate("Answer", "Choose3 your font type for printing"))
        self.printBtn.setToolTip(_translate("Answer", "Click here, if you want to print all informations about your tests"))
        self.printBtn.setText(_translate("Answer", "Print"))

