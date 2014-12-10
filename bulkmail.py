import smtplib
import getpass

username = input('username: ')
password = getpass.getpass()

toaddressFile = input('filename for to-address: ')
msgContentFile = input('filename for message: ')

fp = open(msgContentFile, 'r')
msgContent = fp.read()
fp.close()

server = smtplib.SMTP_SSL('smtp.gmail.com:465')
server.login(username, password)

with open(toaddressFile) as fp:
    for toaddress in fp.readlines():
        server.sendmail(username, toaddress.strip(), msgContent)

server.quit()
