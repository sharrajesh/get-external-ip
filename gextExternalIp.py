import time
import urllib
import smtplib  
import re

def sendNewExternalIp():
    oldIp = ""
    while True:
        curIp = getIpFromWeb()
        if (curIp != oldIp):
            sendEmailExternalIp(curIp)
            oldIp = curIp
        time.sleep(3600*6)

def getIpFromWeb():
    urlOpener = urllib.URLopener()
    respObject = urlOpener.open('http://www.nirsoft.net/show_my_ip_address.php')
    htmlText = respObject.read()
    return getIpFromText(htmlText)

def getIpFromText(htmlText):
    my_regex = r'[0-9]+(?:\.[0-9]+){3}'
    for line in splitTextIntoLines(htmlText):
        print line
        ip = re.findall(my_regex, line)
        if len(ip) &gt; 0:
            return ip[0]

def splitTextIntoLines(text):
    return text.split('\n')

def sendEmailExternalIp(ipAddr):
    subject = 'Important: You external ip adress has changed!'
    body = 'The new ip address detected is :' + ipAddr 
    return sendEmail(subject, body)

def sendEmail(subject, body):
    fromaddr = 'sharrajeshspam@gmail.com'
    toaddrs  = ['sharrajesh@gmail.com', 'rsharma@accessdata.com']

    username = 'sharrajeshspam@gmail.com'
    password = 'YourPassword'

    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.starttls()  
    server.login(username,password)

    msg = 'Subject: %s\n\n%s' % (subject, body)

    for toad in toaddrs:
        server.sendmail(fromaddr, toad, msg)  
    server.quit()

sendNewExternalIp()