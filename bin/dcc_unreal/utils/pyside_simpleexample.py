# Copyright 1998-2018 Epic Games, Inc. All Rights Reserved.
#
import unreal
import sys
from PySide import QtGui
 
sys.path.append('C:/Python27/Lib/site-packages')
APP = None
if not QtGui.QApplication.instance():
   APP = QtGui.QApplication(sys.argv)
   unreal.log("Created QApplication instance: {0}".format(APP))
 
class PySideTest(QtGui.QWidget):
   def __init__(self):
       super(PySideTest, self).__init__()
       pass
   # def closeEvent(self, event):
       # if APP:
           # sys.exit(APP.exec_())
 
tool = PySideTest()
tool.show()
