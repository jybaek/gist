# coding: utf-8

import sys
import smtplib
import socket
from email.MIMEText import MIMEText
from PyQt4 import QtGui, uic, QtCore
from multiprocessing import Process

"""
sendmail examples: https://docs.python.org/2/library/email-examples.html
"""

class form(QtGui.QMainWindow):
    def __init__(self):
        super(form, self).__init__()
        self.ui = uic.loadUi('measure.ui', self)
        self.show()

        self.connect(self.ui.form_start, QtCore.SIGNAL("clicked()"), self.create_jobs)
        self.connect(self.ui.form_stop, QtCore.SIGNAL("clicked()"), self.stop_sendmail)

    def stop_sendmail(self):
        print "debug"

    def create_jobs(self):
        print "create_jobs"
        p1 = Process(target = self.start_sendmail)
        p2 = Process(target=self.start_sendmail)
        p3 = Process(target=self.start_sendmail)
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()

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

        """ from """
        msg['From'] = str(self.ui.form_mailfrom.text())

        """ rcpt to """
        recipients = ["oops@jiran1.com", "test@jiran1.com"]

        """ to """
        msg['To'] = ", ".join(recipients)


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
        try:
            s = smtplib.SMTP(str(self.ui.form_mailserver.text()))
        except socket.error as e:
            print "could not connect"
            return 0
        """ ehlo """
        s.ehlo(str(self.ui.form_ehlo.text()))
        #s.starttls()

        """ sendmail """
        ret = s.sendmail(msg['From'], recipients, msg.as_string())
        s.quit()

        print ret

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = form()
    sys.exit(app.exec_())
