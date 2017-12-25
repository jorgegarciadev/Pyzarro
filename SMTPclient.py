#!/usr/bin/env python
# -*- coding: utf-8 -*-

from smtplib import SMTP

def composeSubject(number, name = None):
    subject = number
    if name:
        subject = "%s - %s" % (number, name)
    
    return subject

def composeMail(mail_login, to, subject, body):
    message = 'from: Domo.Granada <%s>\nto: Jorge Garcia <%s>\nSubject: %s\n\n%s\n' % (mail_login, to, subject, body )
    return message

def sendMail(message, mail_login, mail_password, to, smpt_server):
    try:
        mail = SMTP(smpt_server)
    except smtp.socket.gaierror:
        print "Error al conectar al servidor SMTP."
        return False
    try:
        mail.starttls()
        mail.login(mail_login, mail_password)
    except SMTPAuthentucationError:
        mail.quit()
        print "Error al identificarse al servidor SMTP."
        return False
    try:
        err = mail.sendmail(mail_login, to, message)
        print "Mensaje enviado correctamente a %s." % to
        return True
    except Exception:
        print "Error al enviar el mensage: %s, " % err
        return False
    finally:
        mail.quit()
