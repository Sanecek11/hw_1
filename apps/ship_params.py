# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ship_params.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(226, 147)
        MainWindow.setMaximumSize(QSize(226, 147))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 201, 121))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel {\n"
"    color: orange;\n"
"}")

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel {\n"
"    color: green;\n"
"}")

        self.verticalLayout_2.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"QLabel {\n"
"    color: green;\n"
"}")

        self.verticalLayout_2.addWidget(self.label_9)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel {\n"
"    color: green;\n"
"}")

        self.verticalLayout_2.addWidget(self.label_10)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel {\n"
"    color: green;\n"
"}")

        self.verticalLayout_2.addWidget(self.label_11)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u0440\u0430\u0431\u043b\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043d\u0430 \u0431\u043e\u0440\u0442\u0443", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0433\u0435\u0440\u043c\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21161", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21162", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21163", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"22 C", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
    # retranslateUi

