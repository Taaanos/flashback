# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QAbstractSpinBox, QCheckBox, QComboBox,
    QLabel, QMenuBar, QPushButton,
    QSpinBox, QStatusBar, QTextEdit,
    QWidget)
from compile import compile_videos


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(534, 518)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.TitleLabel = QLabel(self.centralwidget)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setGeometry(QRect(22, 11, 104, 16))
        self.compileBtn = QPushButton(self.centralwidget)
        self.compileBtn.setObjectName(u"compileBtn")
        self.compileBtn.setGeometry(QRect(360, 420, 150, 32))
        self.outputFolderTextEdit = QTextEdit(self.centralwidget)
        self.outputFolderTextEdit.setObjectName(u"outputFolderTextEdit")
        self.outputFolderTextEdit.setGeometry(QRect(210, 340, 301, 41))
        self.outFolderLabel = QLabel(self.centralwidget)
        self.outFolderLabel.setObjectName(u"outFolderLabel")
        self.outFolderLabel.setGeometry(QRect(17, 340, 175, 16))
        self.orderComboBox = QComboBox(self.centralwidget)
        self.orderComboBox.addItem("")
        self.orderComboBox.addItem("")
        self.orderComboBox.setObjectName(u"orderComboBox")
        self.orderComboBox.setGeometry(QRect(280, 30, 133, 32))
        self.debugCheckBox = QCheckBox(self.centralwidget)
        self.debugCheckBox.setObjectName(u"debugCheckBox")
        self.debugCheckBox.setGeometry(QRect(450, 30, 65, 20))
        self.maxOutputSeconds = QSpinBox(self.centralwidget)
        self.maxOutputSeconds.setObjectName(u"maxOutputSeconds")
        self.maxOutputSeconds.setGeometry(QRect(153, 37, 52, 21))
        self.maxOutputSeconds.setMinimum(1)
        self.maxOutputSeconds.setMaximum(9999)
        self.orderLabel = QLabel(self.centralwidget)
        self.orderLabel.setObjectName(u"orderLabel")
        self.orderLabel.setGeometry(QRect(240, 40, 32, 16))
        self.containerLabel = QLabel(self.centralwidget)
        self.containerLabel.setObjectName(u"containerLabel")
        self.containerLabel.setGeometry(QRect(240, 80, 60, 16))
        self.minClipSeconds = QSpinBox(self.centralwidget)
        self.minClipSeconds.setObjectName(u"minClipSeconds")
        self.minClipSeconds.setGeometry(QRect(153, 99, 52, 21))
        self.minClipSeconds.setMinimum(1)
        self.minClipSeconds.setMaximum(9999)
        self.minClipSeconds.setStepType(QAbstractSpinBox.DefaultStepType)
        self.maxOutputDurationLabel = QLabel(self.centralwidget)
        self.maxOutputDurationLabel.setObjectName(u"maxOutputDurationLabel")
        self.maxOutputDurationLabel.setGeometry(QRect(22, 37, 121, 16))
        self.maxClipSeconds = QSpinBox(self.centralwidget)
        self.maxClipSeconds.setObjectName(u"maxClipSeconds")
        self.maxClipSeconds.setGeometry(QRect(153, 68, 52, 21))
        self.maxClipSeconds.setMinimum(1)
        self.maxClipSeconds.setMaximum(9999)
        self.containerComboBox = QComboBox(self.centralwidget)
        self.containerComboBox.addItem("")
        self.containerComboBox.addItem("")
        self.containerComboBox.setObjectName(u"containerComboBox")
        self.containerComboBox.setGeometry(QRect(310, 70, 103, 32))
        self.maxClipDur = QLabel(self.centralwidget)
        self.maxClipDur.setObjectName(u"maxClipDur")
        self.maxClipDur.setGeometry(QRect(22, 68, 103, 16))
        self.minClipDur = QLabel(self.centralwidget)
        self.minClipDur.setObjectName(u"minClipDur")
        self.minClipDur.setGeometry(QRect(22, 99, 100, 16))
        self.videoFoldersLabel = QLabel(self.centralwidget)
        self.videoFoldersLabel.setObjectName(u"videoFoldersLabel")
        self.videoFoldersLabel.setGeometry(QRect(20, 130, 175, 16))
        self.inputFoldersTextEdit = QTextEdit(self.centralwidget)
        self.inputFoldersTextEdit.setObjectName(u"inputFoldersTextEdit")
        self.inputFoldersTextEdit.setGeometry(QRect(213, 130, 301, 192))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 534, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.compileBtn.clicked.connect(self.runCompile)
        
        self.retranslateUi(MainWindow)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def runCompile(self):
        folders = self.inputFoldersTextEdit.toPlainText().splitlines()
        folders = [folder.replace('file://', '') for folder in folders]
        max_output_duration = self.maxOutputSeconds.value()
        min_clip_duration = self.minClipSeconds.value()
        max_clip_duration = self.maxClipSeconds.value()
        order = self.orderComboBox.currentText()
        debug = self.debugCheckBox.isChecked()
        container = self.containerComboBox.currentText()
        output_location = self.outputFolderTextEdit.toPlainText().replace('file://', '')
        compile_videos(folders, max_output_duration, min_clip_duration, max_clip_duration, order, container, None, debug, output_location)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.TitleLabel.setText(QCoreApplication.translate("MainWindow", u"Flashback Config", None))
        self.compileBtn.setText(QCoreApplication.translate("MainWindow", u"Compile Flashaback", None))
        self.outputFolderTextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.outFolderLabel.setText(QCoreApplication.translate("MainWindow", u"output folder (drag and drop)", None))
        self.orderComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"chronological", None))
        self.orderComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"random", None))

#if QT_CONFIG(tooltip)
        self.debugCheckBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.debugCheckBox.setText(QCoreApplication.translate("MainWindow", u"Debug", None))
        self.orderLabel.setText(QCoreApplication.translate("MainWindow", u"order", None))
        self.containerLabel.setText(QCoreApplication.translate("MainWindow", u"container ", None))
        self.maxOutputDurationLabel.setText(QCoreApplication.translate("MainWindow", u"max output duration", None))
        self.containerComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"MP4", None))
        self.containerComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"MOV", None))

        self.containerComboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"MP4", None))
        self.maxClipDur.setText(QCoreApplication.translate("MainWindow", u"max clip duration", None))
        self.minClipDur.setText(QCoreApplication.translate("MainWindow", u"min clip duration", None))
        self.videoFoldersLabel.setText(QCoreApplication.translate("MainWindow", u"video folders (drag and drop)", None))
        self.inputFoldersTextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

