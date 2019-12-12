#!/usr/bin/env python

# socket.getaddrinfo('127.0.0.1', 8080)
# socket.getaddrinfo('localhost', 8080)
# socket.getaddrinfo('127.0.0.1', 8080)
def sendmail(mailto = None, url=None):

    import smtplib
    from email.mime.text import MIMEText
    import socket

    gmail_user = 'bokai830124@gmail.com'
    gmail_password = 'pzyqeegjopvfjqzp' # your gmail 

    mail_boby = """
    您已於BKWeb註冊會員，請點取以下連結，進行近一步確認 %s
    """ %url
    msg = MIMEText(mail_boby,_subtype='html',_charset='utf-8')
    msg['Subject'] = 'BKWeb註冊信件'
    msg['From'] = gmail_user
    # msg['To'] = 'bokai830124@gmail.com'
    msg['To'] = mailto


    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.quit()

    print('Email sent!')

# sendmail(mailto = 'bokai830124@gmail.com',url='test')
