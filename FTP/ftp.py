import ftplib
import os
server = '108.161.128.110'
username = 'pyftpuser'
password = 'PyDanta@1'
location = '/home/pyftpuser'

ftp = ftplib.FTP(server)
ftp.login(username, password)

ftp.cwd(location)

def storeFile():
    filename = 'transactions1.txt'
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()

storeFile()

# def upload(ftp, file):
#     ext = os.path.splitext(file)[1]
#     if ext in (".txt", ".htm", ".html"):
#         ftp.storlines("STOR " + file, open(file))
#     else:
#         ftp.storbinary("STOR " + file, open(file, "rb"), 1024)
#
# ftp = ftplib.FTP(server)
# ftp.login(username, password)

# upload(ftp, "transactions1.txt")




# ftp_connection = ftplib.FTP(server,username,password)
# location = '/home/pyftpuser'
# ftp_connection.cwd(location)
#
# fh = ('transactions.txt','rb')
# ftp_connection.storbinary