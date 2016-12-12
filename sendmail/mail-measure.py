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

        self.connect(self.ui.form_start, QtCore.SIGNAL("clicked()"), self.start_sendmail)
        self.connect(self.ui.form_stop, QtCore.SIGNAL("clicked()"), self.stop_sendmail)

    def stop_sendmail(self):
        print "debug"

    def start_sendmail(self):

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
        msg['Return-path'] = str(self.ui.form_returnpath.text())
        msg['Reply-to'] = str(self.ui.form_replyto.text())

        x_header_line = str(self.ui.form_xheader.toPlainText()).split('\n')
        for x_header in x_header_line:
            msg[x_header.split(':')[0]] = x_header.split(':')[1]

        s = smtplib.SMTP(str(self.ui.form_mailserver.text()))
        s.ehlo(str(self.ui.form_ehlo.text()))
        #s.starttls()
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = form()
    sys.exit(app.exec_())
