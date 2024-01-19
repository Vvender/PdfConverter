from PyQt5 import QtCore, QtGui, QtWidgets
import Gui.Icons.converter_rc as converter_rc


class Ui_ConverterForm(object):
    def setupUi(self, ConverterForm):
        ConverterForm.setObjectName("ConverterForm")
        ConverterForm.resize(500, 350)
        ConverterForm.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ConverterForm.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ConverterForm.setMinimumSize(QtCore.QSize(500, 350))
        ConverterForm.setMaximumSize(QtCore.QSize(500, 350))
        ConverterForm.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(ConverterForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frm_outer = QtWidgets.QFrame(ConverterForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_outer.sizePolicy().hasHeightForWidth())
        self.frm_outer.setSizePolicy(sizePolicy)
        self.frm_outer.setMaximumSize(QtCore.QSize(800, 600))
        self.frm_outer.setStyleSheet("background-color:#2596be;\n"
                                     "border-radius:20px;\n"
                                     "")
        self.frm_outer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_outer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_outer.setObjectName("frm_outer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frm_outer)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frm_middle = QtWidgets.QFrame(self.frm_outer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_middle.sizePolicy().hasHeightForWidth())
        self.frm_middle.setSizePolicy(sizePolicy)
        self.frm_middle.setStyleSheet(
            "background-color:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:0.715909,stop:0 rgba(0,0,0,9), stop:0.375 rgba(0,0,0,50),stop:0.835227 rgba(0,0,0,75));\n"
            "border-radius:20px;\n"
            "")
        self.frm_middle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_middle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_middle.setObjectName("frm_middle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frm_middle)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frm_inside = QtWidgets.QFrame(self.frm_middle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_inside.sizePolicy().hasHeightForWidth())
        self.frm_inside.setSizePolicy(sizePolicy)
        self.frm_inside.setStyleSheet("background-color:rgba(0,0,0,100);\n"
                                      "border-radius:15px;\n"
                                      "\n"
                                      "\n"
                                      "")
        self.frm_inside.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_inside.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_inside.setObjectName("frm_inside")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frm_inside)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 2)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frm_header = QtWidgets.QFrame(self.frm_inside)
        self.frm_header.setMinimumSize(QtCore.QSize(0, 50))
        self.frm_header.setStyleSheet("background-color:#0b1e3b;\n"
                                      "border-radius:15px;\n"
                                      "")
        self.frm_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_header.setObjectName("frm_header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frm_header)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frm_contact_info = QtWidgets.QFrame(self.frm_header)
        self.frm_contact_info.setStyleSheet("QPushButton{\n"
                                            "    background-color: transparent;\n"
                                            "    color:rgba(255, 255, 255, 210);\n"
                                            "    border-radius:5px;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                                            "}\n"
                                            "QPushButton:pressed{\n"
                                            "    padding-left:5px;\n"
                                            "    padding-top:5px;\n"
                                            "    background-color:rgba(105, 118, 132, 200);\n"
                                            "}")
        self.frm_contact_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_contact_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_contact_info.setObjectName("frm_contact_info")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frm_contact_info)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_github = QtWidgets.QPushButton(self.frm_contact_info)
        self.btn_github.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_github.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/github.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_github.setIcon(icon)
        self.btn_github.setIconSize(QtCore.QSize(40, 40))
        self.btn_github.setObjectName("btn_github")
        self.horizontalLayout_3.addWidget(self.btn_github)
        self.btn_linkedin = QtWidgets.QPushButton(self.frm_contact_info)
        self.btn_linkedin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_linkedin.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/linkedin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_linkedin.setIcon(icon1)
        self.btn_linkedin.setIconSize(QtCore.QSize(40, 40))
        self.btn_linkedin.setObjectName("btn_linkedin")
        self.horizontalLayout_3.addWidget(self.btn_linkedin)
        self.btn_cv = QtWidgets.QPushButton(self.frm_contact_info)
        self.btn_cv.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cv.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/paperclip.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cv.setIcon(icon2)
        self.btn_cv.setIconSize(QtCore.QSize(40, 40))
        self.btn_cv.setObjectName("btn_cv")
        self.horizontalLayout_3.addWidget(self.btn_cv)
        self.btn_email = QtWidgets.QPushButton(self.frm_contact_info)
        self.btn_email.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_email.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/mail.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_email.setIcon(icon3)
        self.btn_email.setIconSize(QtCore.QSize(40, 40))
        self.btn_email.setObjectName("btn_email")
        self.horizontalLayout_3.addWidget(self.btn_email)
        self.horizontalLayout.addWidget(self.frm_contact_info, 0, QtCore.Qt.AlignLeft)
        self.frm_top_right = QtWidgets.QFrame(self.frm_header)
        self.frm_top_right.setStyleSheet("QPushButton{\n"
                                         "    background-color: transparent;\n"
                                         "    color:rgba(255, 255, 255, 210);\n"
                                         "    border-radius:5px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    padding-left:5px;\n"
                                         "    padding-top:5px;\n"
                                         "    background-color:rgba(105, 118, 132, 200);\n"
                                         "}")
        self.frm_top_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_top_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_top_right.setObjectName("frm_top_right")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frm_top_right)
        self.horizontalLayout_2.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_minimize = QtWidgets.QPushButton(self.frm_top_right)
        self.btn_minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimize.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/chevron-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon4)
        self.btn_minimize.setIconSize(QtCore.QSize(40, 40))
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_2.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.frm_top_right)
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon5)
        self.btn_close.setIconSize(QtCore.QSize(40, 40))
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_2.addWidget(self.btn_close)
        self.horizontalLayout.addWidget(self.frm_top_right, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addWidget(self.frm_header)
        self.pages = QtWidgets.QStackedWidget(self.frm_inside)
        self.pages.setStyleSheet("background-color: transparent;\n"
                                 "border-radius:15px;")
        self.pages.setObjectName("pages")
        self.page_convert = QtWidgets.QWidget()
        self.page_convert.setObjectName("page_convert")
        self.btn_file_location = QtWidgets.QPushButton(self.page_convert)
        self.btn_file_location.setGeometry(QtCore.QRect(173, 20, 100, 100))
        self.btn_file_location.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_file_location.setStyleSheet("QPushButton{\n"
                                             "    background-color: transparent;\n"
                                             "    color:rgba(255, 255, 255, 210);\n"
                                             "    border-radius:5px;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                                             "}\n"
                                             "QPushButton:pressed{\n"
                                             "    padding-left:5px;\n"
                                             "    padding-top:5px;\n"
                                             "    background-color:rgba(105, 118, 132, 200);\n"
                                             "}")
        self.btn_file_location.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons/file-plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_file_location.setIcon(icon6)
        self.btn_file_location.setIconSize(QtCore.QSize(100, 100))
        self.btn_file_location.setObjectName("btn_file_location")
        self.frm_checkbox = QtWidgets.QFrame(self.page_convert)
        self.frm_checkbox.setGeometry(QtCore.QRect(105, 130, 241, 37))
        self.frm_checkbox.setStyleSheet("background-color:transparent;\n"
                                        "color: #2586be;\n"
                                        "border-radius:15px;")
        self.frm_checkbox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_checkbox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_checkbox.setObjectName("frm_checkbox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frm_checkbox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cb_excel = QtWidgets.QCheckBox(self.frm_checkbox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cb_excel.setFont(font)
        self.cb_excel.setChecked(True)
        self.cb_excel.setObjectName("cb_excel")
        self.horizontalLayout_4.addWidget(self.cb_excel)
        self.cb_word = QtWidgets.QCheckBox(self.frm_checkbox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cb_word.setFont(font)
        self.cb_word.setTabletTracking(False)
        self.cb_word.setChecked(False)
        self.cb_word.setObjectName("cb_word")
        self.horizontalLayout_4.addWidget(self.cb_word)
        self.btn_convert = QtWidgets.QPushButton(self.page_convert)
        self.btn_convert.setGeometry(QtCore.QRect(148, 170, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_convert.setFont(font)
        self.btn_convert.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_convert.setStyleSheet("QPushButton#btn_convert{\n"
                                       "    background-color: #0b1e3b;\n"
                                       "    color: #2596be;\n"
                                       "    border-radius: 5px;\n"
                                       "    padding: 8px 10px; /* Adjust the padding for the pop-up effect */\n"
                                       "    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Add a box shadow for the pop-up effect */\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#btn_convert:hover{\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 150, 190, 200), stop:1 rgba(85, 98, 112, 226));\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#btn_convert:pressed{\n"
                                       "    padding-left: 8px;\n"
                                       "    padding-top: 10px;\n"
                                       "    background-color: rgba(105, 118, 132, 200);\n"
                                       "    box-shadow: none; /* Remove the box shadow when pressed */\n"
                                       "}")
        self.btn_convert.setObjectName("btn_convert")
        self.pages.addWidget(self.page_convert)
        self.page_info = QtWidgets.QWidget()
        self.page_info.setObjectName("page_info")
        self.lbl_info_message = QtWidgets.QLabel(self.page_info)
        self.lbl_info_message.setGeometry(QtCore.QRect(90, 90, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_info_message.setFont(font)
        self.lbl_info_message.setStyleSheet("background-color:transparent;\n"
                                            "color: #2586be;\n"
                                            "border-radius:15px;\n"
                                            "\n"
                                            "")
        self.lbl_info_message.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_info_message.setWordWrap(True)
        self.lbl_info_message.setObjectName("lbl_info_message")
        self.btn_info_return = QtWidgets.QPushButton(self.page_info)
        self.btn_info_return.setGeometry(QtCore.QRect(150, 170, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_info_return.setFont(font)
        self.btn_info_return.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_info_return.setStyleSheet("QPushButton#btn_info_return{\n"
                                           "    background-color: #0b1e3b;\n"
                                           "    color:#2596be;\n"
                                           "    border-radius:5px;\n"
                                           "}\n"
                                           "QPushButton#btn_info_return:hover{\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 150, 190 200), stop:1 rgba(85, 98, 112, 226));\n"
                                           "}\n"
                                           "QPushButton#btn_info_return:pressed{\n"
                                           "    padding-left:5px;\n"
                                           "    padding-top:5px;\n"
                                           "    background-color:rgba(85, 98, 112, 226);\n"
                                           "}")
        self.btn_info_return.setObjectName("btn_info_return")
        self.lbl_icon_converted = QtWidgets.QLabel(self.page_info)
        self.lbl_icon_converted.setGeometry(QtCore.QRect(185, 10, 71, 71))
        self.lbl_icon_converted.setText("")
        self.lbl_icon_converted.setPixmap(QtGui.QPixmap(":/Icons/check-circle .svg"))
        self.lbl_icon_converted.setScaledContents(True)
        self.lbl_icon_converted.setObjectName("lbl_icon_converted")
        self.pages.addWidget(self.page_info)
        self.verticalLayout_4.addWidget(self.pages)
        self.verticalLayout_2.addWidget(self.frm_inside)
        self.verticalLayout_3.addWidget(self.frm_middle)
        self.verticalLayout.addWidget(self.frm_outer)

        self.retranslateUi(ConverterForm)
        self.pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ConverterForm)
        ConverterForm.setTabOrder(self.btn_github, self.btn_linkedin)
        ConverterForm.setTabOrder(self.btn_linkedin, self.btn_cv)
        ConverterForm.setTabOrder(self.btn_cv, self.btn_email)
        ConverterForm.setTabOrder(self.btn_email, self.btn_minimize)
        ConverterForm.setTabOrder(self.btn_minimize, self.btn_close)
        ConverterForm.setTabOrder(self.btn_close, self.btn_file_location)
        ConverterForm.setTabOrder(self.btn_file_location, self.cb_word)
        ConverterForm.setTabOrder(self.cb_word, self.btn_convert)
        ConverterForm.setTabOrder(self.btn_convert, self.btn_info_return)

    def retranslateUi(self, ConverterForm):
        _translate = QtCore.QCoreApplication.translate
        ConverterForm.setWindowTitle(_translate("ConverterForm", "PDF Converter"))
        self.cb_excel.setText(_translate("ConverterForm", "Excel"))
        self.cb_word.setText(_translate("ConverterForm", "Word"))
        self.btn_convert.setText(_translate("ConverterForm", "CONVERT"))
        self.lbl_info_message.setText(_translate("ConverterForm",
                                                 "<html><head/><body><p align=\"center\">Your files have been </p><p align=\"center\">succesfully converted.<br/></p></body></html>"))
        self.btn_info_return.setText(_translate("ConverterForm", "RETURN"))
