import crypt


def testPass(cryptPass, dictPath):
    salt = cryptPass[0:2]
    dictFile = open(dictPath, 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if(cryptWord == cryptPass):
            print('[+] Found Password:' + word + '\n')
            return
    print("[-] Password Not Found.\n")
    return


def main():
    dictPath = input('Enter the path for dictonary file: ')
    passwordFile = input('Enter the path for password file: ')
    passFile = open(passwordFile, 'r')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print('[*] Cracking Password For: ' + user)
            testPass(cryptPass, dictPath)


if __name__ == "__main__":
    main()
