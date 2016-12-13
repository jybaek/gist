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
        """ subject """
        msg['Subject'] = str(self.ui.form_subject.text())

        """ mail from """
        msg['From'] = str(self.ui.form_mailfrom.text())

        """ rcpt to """
        msg['To'] = str(self.ui.form_rcptto.text())

        """ return-path """
        if len(str(self.ui.form_returnpath.text()).strip()) != 0:
            msg['Return-path'] = str(self.ui.form_returnpath.text())

        """ reply-to """
        if len(str(self.ui.form_replyto.text()).strip()) != 0:
            msg['Reply-to'] = str(self.ui.form_replyto.text())

        """ x-header """
        if len(str(self.ui.form_xheader.toPlainText()).strip()) != 0:
            x_header_line = str(self.ui.form_xheader.toPlainText()).split('\n')
            for x_header in x_header_line:
                msg[x_header.split(':')[0]] = x_header.split(':')[1]

        """ smtp server """
        s = smtplib.SMTP(str(self.ui.form_mailserver.text()))

        """ ehlo """
        s.ehlo(str(self.ui.form_ehlo.text()))
        #s.starttls()

        """ sendmail """
        ret = s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()

        print ret

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = form()
    sys.exit(app.exec_())
