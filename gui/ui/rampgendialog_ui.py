# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rampgendialog.ui'
#
# Created: Thu Nov 23 15:18:14 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_RampGenDialog(object):
    def setupUi(self, RampGenDialog):
        RampGenDialog.setObjectName("RampGenDialog")
        RampGenDialog.resize(874, 614)
        self.verticalLayout = QtGui.QVBoxLayout(RampGenDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtGui.QTableWidget(RampGenDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.verticalLayout.addWidget(self.table)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formWidget = QtGui.QWidget(RampGenDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formWidget.sizePolicy().hasHeightForWidth())
        self.formWidget.setSizePolicy(sizePolicy)
        self.formWidget.setObjectName("formWidget")
        self.gridLayout = QtGui.QGridLayout(self.formWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.savePushButton = QtGui.QPushButton(self.formWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savePushButton.sizePolicy().hasHeightForWidth())
        self.savePushButton.setSizePolicy(sizePolicy)
        self.savePushButton.setAutoDefault(False)
        self.savePushButton.setObjectName("savePushButton")
        self.gridLayout.addWidget(self.savePushButton, 0, 2, 1, 1)
        self.rampNameFormLabel = QtGui.QLabel(self.formWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rampNameFormLabel.sizePolicy().hasHeightForWidth())
        self.rampNameFormLabel.setSizePolicy(sizePolicy)
        self.rampNameFormLabel.setObjectName("rampNameFormLabel")
        self.gridLayout.addWidget(self.rampNameFormLabel, 1, 0, 1, 1)
        self.fcutDoubleSpinBox = QtGui.QDoubleSpinBox(self.formWidget)
        self.fcutDoubleSpinBox.setDecimals(3)
        self.fcutDoubleSpinBox.setMaximum(99.999)
        self.fcutDoubleSpinBox.setSingleStep(0.001)
        self.fcutDoubleSpinBox.setObjectName("fcutDoubleSpinBox")
        self.gridLayout.addWidget(self.fcutDoubleSpinBox, 6, 2, 1, 2)
        self.line = QtGui.QFrame(self.formWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 4)
        self.rampNameLabel = QtGui.QLabel(self.formWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rampNameLabel.sizePolicy().hasHeightForWidth())
        self.rampNameLabel.setSizePolicy(sizePolicy)
        self.rampNameLabel.setObjectName("rampNameLabel")
        self.gridLayout.addWidget(self.rampNameLabel, 1, 1, 1, 3)
        self.fcutLabel = QtGui.QLabel(self.formWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fcutLabel.sizePolicy().hasHeightForWidth())
        self.fcutLabel.setSizePolicy(sizePolicy)
        self.fcutLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fcutLabel.setIndent(10)
        self.fcutLabel.setObjectName("fcutLabel")
        self.gridLayout.addWidget(self.fcutLabel, 6, 0, 1, 2)
        self.newPushButton = QtGui.QPushButton(self.formWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newPushButton.sizePolicy().hasHeightForWidth())
        self.newPushButton.setSizePolicy(sizePolicy)
        self.newPushButton.setAutoDefault(False)
        self.newPushButton.setObjectName("newPushButton")
        self.gridLayout.addWidget(self.newPushButton, 0, 0, 1, 1)
        self.loadPushButton = QtGui.QPushButton(self.formWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadPushButton.sizePolicy().hasHeightForWidth())
        self.loadPushButton.setSizePolicy(sizePolicy)
        self.loadPushButton.setAutoDefault(False)
        self.loadPushButton.setObjectName("loadPushButton")
        self.gridLayout.addWidget(self.loadPushButton, 0, 1, 1, 1)
        self.saveAsPushButton = QtGui.QPushButton(self.formWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveAsPushButton.sizePolicy().hasHeightForWidth())
        self.saveAsPushButton.setSizePolicy(sizePolicy)
        self.saveAsPushButton.setAutoDefault(False)
        self.saveAsPushButton.setObjectName("saveAsPushButton")
        self.gridLayout.addWidget(self.saveAsPushButton, 0, 3, 1, 1)
        self.npointsFormLabel = QtGui.QLabel(self.formWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.npointsFormLabel.sizePolicy().hasHeightForWidth())
        self.npointsFormLabel.setSizePolicy(sizePolicy)
        self.npointsFormLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.npointsFormLabel.setIndent(10)
        self.npointsFormLabel.setObjectName("npointsFormLabel")
        self.gridLayout.addWidget(self.npointsFormLabel, 7, 0, 1, 2)
        self.writeOutPushButton = QtGui.QPushButton(self.formWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.writeOutPushButton.sizePolicy().hasHeightForWidth())
        self.writeOutPushButton.setSizePolicy(sizePolicy)
        self.writeOutPushButton.setStyleSheet("QPushButton{color: red;}\n"
"")
        self.writeOutPushButton.setAutoDefault(False)
        self.writeOutPushButton.setObjectName("writeOutPushButton")
        self.gridLayout.addWidget(self.writeOutPushButton, 10, 0, 1, 4)
        self.line_2 = QtGui.QFrame(self.formWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 9, 0, 1, 4)
        self.npointsLabel = QtGui.QLabel(self.formWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.npointsLabel.sizePolicy().hasHeightForWidth())
        self.npointsLabel.setSizePolicy(sizePolicy)
        self.npointsLabel.setText("")
        self.npointsLabel.setObjectName("npointsLabel")
        self.gridLayout.addWidget(self.npointsLabel, 7, 2, 1, 2)
        self.tfinalFormLabel = QtGui.QLabel(self.formWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tfinalFormLabel.sizePolicy().hasHeightForWidth())
        self.tfinalFormLabel.setSizePolicy(sizePolicy)
        self.tfinalFormLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tfinalFormLabel.setIndent(10)
        self.tfinalFormLabel.setObjectName("tfinalFormLabel")
        self.gridLayout.addWidget(self.tfinalFormLabel, 8, 0, 1, 2)
        self.tfinalLabel = QtGui.QLabel(self.formWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tfinalLabel.sizePolicy().hasHeightForWidth())
        self.tfinalLabel.setSizePolicy(sizePolicy)
        self.tfinalLabel.setText("")
        self.tfinalLabel.setObjectName("tfinalLabel")
        self.gridLayout.addWidget(self.tfinalLabel, 8, 2, 1, 2)
        self.linkRampsCheckBox = QtGui.QCheckBox(self.formWidget)
        self.linkRampsCheckBox.setCheckable(True)
        self.linkRampsCheckBox.setObjectName("linkRampsCheckBox")
        self.gridLayout.addWidget(self.linkRampsCheckBox, 5, 0, 1, 1)
        self.blockEditComboBox = QtGui.QComboBox(self.formWidget)
        self.blockEditComboBox.setObjectName("blockEditComboBox")
        self.gridLayout.addWidget(self.blockEditComboBox, 5, 2, 1, 2)
        self.blockEditLabel = QtGui.QLabel(self.formWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blockEditLabel.sizePolicy().hasHeightForWidth())
        self.blockEditLabel.setSizePolicy(sizePolicy)
        self.blockEditLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.blockEditLabel.setObjectName("blockEditLabel")
        self.gridLayout.addWidget(self.blockEditLabel, 5, 1, 1, 1)
        self.horizontalLayout.addWidget(self.formWidget)
        self.rampPlotWidget = QtGui.QWidget(RampGenDialog)
        self.rampPlotWidget.setObjectName("rampPlotWidget")
        self.horizontalLayout.addWidget(self.rampPlotWidget)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(RampGenDialog)
        QtCore.QMetaObject.connectSlotsByName(RampGenDialog)

    def retranslateUi(self, RampGenDialog):
        RampGenDialog.setWindowTitle(QtGui.QApplication.translate("RampGenDialog", "Ramp Generator", None, QtGui.QApplication.UnicodeUTF8))
        self.savePushButton.setText(QtGui.QApplication.translate("RampGenDialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.rampNameFormLabel.setText(QtGui.QApplication.translate("RampGenDialog", "Ramp:", None, QtGui.QApplication.UnicodeUTF8))
        self.rampNameLabel.setText(QtGui.QApplication.translate("RampGenDialog", "---", None, QtGui.QApplication.UnicodeUTF8))
        self.fcutLabel.setText(QtGui.QApplication.translate("RampGenDialog", "f cut", None, QtGui.QApplication.UnicodeUTF8))
        self.newPushButton.setText(QtGui.QApplication.translate("RampGenDialog", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.loadPushButton.setText(QtGui.QApplication.translate("RampGenDialog", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAsPushButton.setText(QtGui.QApplication.translate("RampGenDialog", "Save as...", None, QtGui.QApplication.UnicodeUTF8))
        self.npointsFormLabel.setText(QtGui.QApplication.translate("RampGenDialog", "N points", None, QtGui.QApplication.UnicodeUTF8))
        self.writeOutPushButton.setText(QtGui.QApplication.translate("RampGenDialog", "WRITE OUT", None, QtGui.QApplication.UnicodeUTF8))
        self.tfinalFormLabel.setText(QtGui.QApplication.translate("RampGenDialog", "t final", None, QtGui.QApplication.UnicodeUTF8))
        self.linkRampsCheckBox.setText(QtGui.QApplication.translate("RampGenDialog", "link ramps", None, QtGui.QApplication.UnicodeUTF8))
        self.blockEditLabel.setText(QtGui.QApplication.translate("RampGenDialog", "block edit", None, QtGui.QApplication.UnicodeUTF8))

