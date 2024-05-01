# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'engine_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QSizePolicy, QSlider, QSpacerItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(583, 210)
        MainWindow.setMaximumSize(QSize(641, 210))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 621, 191))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 3, 1, 1, 1)

        self.verticalSlider_3 = QSlider(self.widget)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        self.verticalSlider_3.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider_3, 1, 1, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)

        self.verticalSlider = QSlider(self.widget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 1, 0, 1, 1)

        self.verticalSlider_2 = QSlider(self.widget)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider_2, 1, 2, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 3, 2, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 3, 1, 1)

        self.verticalSlider_4 = QSlider(self.widget)
        self.verticalSlider_4.setObjectName(u"verticalSlider_4")
        self.verticalSlider_4.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider_4, 1, 3, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSlider_5 = QSlider(self.widget)
        self.verticalSlider_5.setObjectName(u"verticalSlider_5")
        self.verticalSlider_5.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.verticalSlider_5, 3, 1, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21162", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21161", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21163", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21164", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0442\u044f\u0433\u0430", None))
    # retranslateUi

