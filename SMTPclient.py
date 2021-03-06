#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib

def composeSubject(number, name = None):
    subject = number
    if name:
        subject = "%s - %s" % (number, name)
    
    return subject

def composeMail(mail_login, to, subject, body):
    message = 'from: Domo.Granada <%s>\nto: Jorge Garcia <%s>\nSubject: %s\n\n%s\n' % (mail_login, to, subject, body )
    return message

def sendMail(message, mail_login, mail_password, to, smpt_server, port = 465):
    try:
        mail = smtplib.SMTP(smpt_server, port)
    except smtplib.socket.gaierror:
        print "Error al conectar al servidor SMTP."
        return False
    try:
        mail.starttls()
        mail.login(mail_login, mail_password)
    except smtplib.SMTPAuthenticationError:
        mail.quit()
        print "Error al identificarse al servidor SMTP."
        return False
    try:
        err = mail.sendmail(mail_login, to, message)
        print "Mensaje enviado correctamente a %s." % to
        return True
    except Exception, err:
        print "Error al enviar el mensage: %s, " % err
        return False
    finally:
        mail.quit()
