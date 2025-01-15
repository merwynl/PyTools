import sys

from PySide2 import QtGui
from PySide2 import QtWidgets

import unreal


class TestWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TestWidget, self).__init__(parent)

        vbox = QtWidgets.QVBoxLayout(self)
        btn = QtWidgets.QPushButton("Test")
        btn.clicked.connect(self.btn_clicked)
        vbox.addWidget(btn)

    def btn_clicked(self):
        print("Clicked")
        unreal.log("Clicked")


app = None
if not QtWidgets.QApplication.instance():
    app = QtWidgets.QApplication(sys.argv)

widget = TestWidget()
widget.show()
unreal.parent_external_window_to_slate(widget.winId())