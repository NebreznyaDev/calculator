

################################################################################
## Form generated from reading UI file 'DESING.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setMinimumSize(QSize(300, 500))
        icon = QIcon()
        icon.addFile(u":/icons/icons/calculate_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color: white;\n"
"    background-color: #121212;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"    backround-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushBotton:pressed {\n"
"    background-color: #888;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_temp = QLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        self.lbl_temp.setStyleSheet(u"color: #888;")
        self.lbl_temp.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_temp)

        self.le_entry = QLineEdit(self.centralwidget)
        self.le_entry.setObjectName(u"le_entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
        self.le_entry.setSizePolicy(sizePolicy1)
        self.le_entry.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.le_entry.setStyleSheet(u"front-size: 40pt;\n"
"border: none;")
        self.le_entry.setMaxLength(10)
        self.le_entry.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.le_entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_entry)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.BTN_8 = QPushButton(self.centralwidget)
        self.BTN_8.setObjectName(u"BTN_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.BTN_8.sizePolicy().hasHeightForWidth())
        self.BTN_8.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTN_8, 1, 2, 1, 1)

        self.BTN_BACKPASE = QPushButton(self.centralwidget)
        self.BTN_BACKPASE.setObjectName(u"BTN_BACKPASE")
        sizePolicy2.setHeightForWidth(self.BTN_BACKPASE.sizePolicy().hasHeightForWidth())
        self.BTN_BACKPASE.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/backspace_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTN_BACKPASE.setIcon(icon1)
        self.BTN_BACKPASE.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.BTN_BACKPASE, 0, 3, 1, 1)

        self.BTN_3 = QPushButton(self.centralwidget)
        self.BTN_3.setObjectName(u"BTN_3")
        sizePolicy2.setHeightForWidth(self.BTN_3.sizePolicy().hasHeightForWidth())
        self.BTN_3.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTN_3, 3, 3, 1, 1)

        self.BTN_0 = QPushButton(self.centralwidget)
        self.BTN_0.setObjectName(u"BTN_0")
        sizePolicy2.setHeightForWidth(self.BTN_0.sizePolicy().hasHeightForWidth())
        self.BTN_0.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTN_0, 4, 2, 1, 1)

        self.BTM_SUB = QPushButton(self.centralwidget)
        self.BTM_SUB.setObjectName(u"BTM_SUB")
        sizePolicy2.setHeightForWidth(self.BTM_SUB.sizePolicy().hasHeightForWidth())
        self.BTM_SUB.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTM_SUB, 4, 0, 1, 1)

        self.BTN_4 = QPushButton(self.centralwidget)
        self.BTN_4.setObjectName(u"BTN_4")
        sizePolicy2.setHeightForWidth(self.BTN_4.sizePolicy().hasHeightForWidth())
        self.BTN_4.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTN_4, 2, 0, 1, 1)

        self.BTN_2 = QPushButton(self.centralwidget)
        self.BTN_2.setObjectName(u"BTN_2")
        sizePolicy2.setHeightForWidth(self.BTN_2.sizePolicy().hasHeightForWidth())
        self.BTN_2.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTN_2, 3, 2, 1, 1)

        self.BTN_POINT = QPushButton(self.centralwidget)
        self.BTN_POINT.setObjectName(u"BTN_POINT")
        sizePolicy2.setHeightForWidth(self.BTN_POINT.sizePolicy().hasHeightForWidth())
        self.BTN_POINT.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTN_POINT, 4, 3, 1, 1)

        self.BTM_EQU = QPushButton(self.centralwidget)
        self.BTM_EQU.setObjectName(u"BTM_EQU")
        sizePolicy2.setHeightForWidth(self.BTM_EQU.sizePolicy().hasHeightForWidth())
        self.BTM_EQU.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTM_EQU, 4, 4, 1, 1)

        self.BTN_DIV = QPushButton(self.centralwidget)
        self.BTN_DIV.setObjectName(u"BTN_DIV")
        sizePolicy2.setHeightForWidth(self.BTN_DIV.sizePolicy().hasHeightForWidth())
        self.BTN_DIV.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTN_DIV, 0, 4, 1, 1)

        self.BTN_1 = QPushButton(self.centralwidget)
        self.BTN_1.setObjectName(u"BTN_1")
        sizePolicy2.setHeightForWidth(self.BTN_1.sizePolicy().hasHeightForWidth())
        self.BTN_1.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTN_1, 3, 0, 1, 1)

        self.BTN_6 = QPushButton(self.centralwidget)
        self.BTN_6.setObjectName(u"BTN_6")
        sizePolicy2.setHeightForWidth(self.BTN_6.sizePolicy().hasHeightForWidth())
        self.BTN_6.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTN_6, 2, 3, 1, 1)

        self.BTN_NEG = QPushButton(self.centralwidget)
        self.BTN_NEG.setObjectName(u"BTN_NEG")
        sizePolicy2.setHeightForWidth(self.BTN_NEG.sizePolicy().hasHeightForWidth())
        self.BTN_NEG.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTN_NEG, 2, 4, 1, 1)

        self.BTN_CE = QPushButton(self.centralwidget)
        self.BTN_CE.setObjectName(u"BTN_CE")
        sizePolicy2.setHeightForWidth(self.BTN_CE.sizePolicy().hasHeightForWidth())
        self.BTN_CE.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTN_CE, 0, 2, 1, 1)

        self.BTN_5 = QPushButton(self.centralwidget)
        self.BTN_5.setObjectName(u"BTN_5")
        sizePolicy2.setHeightForWidth(self.BTN_5.sizePolicy().hasHeightForWidth())
        self.BTN_5.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTN_5, 2, 2, 1, 1)

        self.BTN_9 = QPushButton(self.centralwidget)
        self.BTN_9.setObjectName(u"BTN_9")
        sizePolicy2.setHeightForWidth(self.BTN_9.sizePolicy().hasHeightForWidth())
        self.BTN_9.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTN_9, 1, 3, 1, 1)

        self.BTN_MUL = QPushButton(self.centralwidget)
        self.BTN_MUL.setObjectName(u"BTN_MUL")
        sizePolicy2.setHeightForWidth(self.BTN_MUL.sizePolicy().hasHeightForWidth())
        self.BTN_MUL.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTN_MUL, 1, 4, 1, 1)

        self.BTN_7 = QPushButton(self.centralwidget)
        self.BTN_7.setObjectName(u"BTN_7")
        sizePolicy2.setHeightForWidth(self.BTN_7.sizePolicy().hasHeightForWidth())
        self.BTN_7.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTN_7, 1, 0, 1, 1)

        self.BTN_PLUS = QPushButton(self.centralwidget)
        self.BTN_PLUS.setObjectName(u"BTN_PLUS")
        sizePolicy2.setHeightForWidth(self.BTN_PLUS.sizePolicy().hasHeightForWidth())
        self.BTN_PLUS.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.BTN_PLUS, 3, 4, 1, 1)

        self.BTM_CLEAR = QPushButton(self.centralwidget)
        self.BTM_CLEAR.setObjectName(u"BTM_CLEAR")
        sizePolicy2.setHeightForWidth(self.BTM_CLEAR.sizePolicy().hasHeightForWidth())
        self.BTM_CLEAR.setSizePolicy(sizePolicy2)
        self.BTM_CLEAR.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.BTM_CLEAR, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.lbl_temp.setText("")
        self.le_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.BTN_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.BTN_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.BTN_BACKPASE.setText("")
#if QT_CONFIG(shortcut)
        self.BTN_BACKPASE.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.BTN_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.BTN_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.BTN_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.BTN_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.BTM_SUB.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.BTN_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.BTN_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.BTN_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.BTN_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.BTN_POINT.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.BTN_POINT.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.BTM_EQU.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.BTM_EQU.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.BTN_DIV.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.BTN_DIV.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.BTN_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.BTN_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.BTN_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.BTN_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.BTN_NEG.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.BTN_NEG.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.BTN_CE.setText(QCoreApplication.translate("MainWindow", u"CE", None))
#if QT_CONFIG(shortcut)
        self.BTN_CE.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.BTN_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.BTN_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.BTN_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.BTN_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.BTN_MUL.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
#if QT_CONFIG(shortcut)
        self.BTN_MUL.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.BTN_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.BTN_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.BTN_PLUS.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.BTN_PLUS.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.BTM_CLEAR.setText(QCoreApplication.translate("MainWindow", u"C", None))
    # retranslateUi

