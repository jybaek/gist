# coding: utf-8

import sys
from PyQt4 import QtGui, uic, QtCore

class form(QtGui.QMainWindow):
    def __init__(self):
        super(form, self).__init__()
        self.ui = uic.loadUi('attack-mail.ui', self)
        self.show()

        self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.someFunc)

    def someFunc(self):
        print "hello"
        print self.ui.form_mailserver.text()
        print self.ui.form_ehlo.text()
        print self.ui.form_mailfrom.text()
        print self.ui.form_rcptto.text()
        print self.ui.form_subject.text()
        print self.ui.form_data.toPlainText()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = form()
    sys.exit(app.exec_())
