# coding: utf-8

import sys
import smtplib
from email.MIMEText import MIMEText
from PyQt4 import QtGui, uic, QtCore

"""
sendmail examples: https://docs.python.org/2/library/email-examples.html
"""

class form(QtGui.QMainWindow):
    def __init__(self):
        super(form, self).__init__()
        self.ui = uic.loadUi('measure.ui', self)
        self.show()

        self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.sendmail)

    def sendmail(self):

        """
        print self.ui.form_mailserver.text()
        print self.ui.form_ehlo.text()
        print self.ui.form_mailfrom.text()
        print self.ui.form_rcptto.text()
        print self.ui.form_subject.text()
        print self.ui.form_data.toPlainText()
        """
        msg = MIMEText(str(self.ui.form_data.toPlainText()), _charset='euc-kr')
        msg['Subject'] = str(self.ui.form_subject.text())
        msg['From'] = str(self.ui.form_mailfrom.text())
        msg['To'] = str(self.ui.form_rcptto.text())

        s = smtplib.SMTP(str(self.ui.form_mailserver.text()))
        s.ehlo(str(self.ui.form_ehlo.text()))
        #s.starttls()
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = form()
    sys.exit(app.exec_())
