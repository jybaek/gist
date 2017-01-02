# coding: utf-8

import sys
import smtplib
import socket
import time
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
        print "terminate"
        exit(0)

    def create_jobs(self):
        print "create_jobs (%s) " % self.ui.mail_total.text()
        jobs = list()
        mps = int(self.ui.mps.text())

        for i in range(int(self.ui.mail_total.text())):
            jobs.append(Process(target = self.start_sendmail),)

        for job in jobs:

            job.start()

            if mps == 0:
                mps = 1

            time.sleep(1.0 / mps)
            time.sleep(1.0 / mps)

        for job in jobs:
            job.join()


    def start_sendmail(self):

        """
        print self.ui.form_mailserver.text()
        print self.ui.form_ehlo.text()
        print self.ui.form_mailfrom.text()
        print self.ui.form_rcptto.text()
        print self.ui.form_subject.text()
        print self.ui.form_data.toPlainText()
        print self.ui.form_mailfrom_inc.isChecked()
        """
        start = time.time()

        msg = MIMEText(str(self.ui.form_data.toPlainText()), _charset='euc-kr')
        """ subject """
        msg['Subject'] = str(self.ui.form_subject.text())

        """ from """
        msg['From'] = str(self.ui.form_mailfrom.text())

        """ rcpt to """
        recipients = []
        for recipient in str(self.ui.form_rcptto.text()).split(","):
            recipients.append(recipient)

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
            print "could not connect: %s" % str(e)
            return 0
        except smtplib.SMTPConnectError, e:
            print "Failure to send email: %s" % str(e)
            return 0
        """ ehlo """
        s.ehlo(str(self.ui.form_ehlo.text()))
        #s.starttls()

        """ sendmail """
        try:
            ret = s.sendmail(msg['From'], recipients, msg.as_string())
            s.quit()
        # Catch all for SMTP exceptions
        except smtplib.SMTPException, e:
            print "Failure to send email: %s" % str(e)

        end = time.time()

        print "successed (%d) " % (end-start)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = form()
    sys.exit(app.exec_())
