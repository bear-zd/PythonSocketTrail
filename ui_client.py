# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientJvnWdP.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(556, 590)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 80, 91, 16))
        self.label.setLineWidth(3)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setIndent(-1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 130, 81, 16))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(160, 130, 256, 31))
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(160, 291, 256, 151))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(460, 130, 71, 24))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(220, 480, 121, 24))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 290, 91, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 180, 71, 16))
        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(160, 180, 256, 91))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(24, 9, 511, 31))
        self.textEdit_4 = QTextEdit(self.centralwidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(160, 80, 256, 31))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(460, 180, 75, 24))
        #self.pushButton_4 = QPushButton(self.centralwidget)
        #self.pushButton_4.setObjectName(u"pushButton_4")
        #self.pushButton_4.setGeometry(QRect(460, 290, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 556, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Server", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Localhost", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ChoosePort", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"MessageBox", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextSend", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5982\u4f55\u4f7f\u7528\uff1a\u9009\u62e9\u4f60\u8981\u8fde\u63a5\u7684\u7aef\u53e3\uff08\u5373\u81ea\u5df1\u5f00\u653e\u7684\u670d\u52a1\u5668\u7aef\u53e3\uff09\uff0c\u70b9\u51fb\u8fde\u63a5\u3002\u3002\u3002\u3002\u3002", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI';\">\u5982\u679c\u4e0d\u8f93\u5165\uff0c\u5219\u9ed8\u8ba4\u4e3a\u672c\u5730ip</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"send", None))
        #self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
    # retranslateUi

