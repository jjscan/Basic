import zipfile

def extract(zFile, passwd):
    try:
        zFile.extractall(pwd = bytes(passwd,'utf-8'))
        return passwd
    except Exception as e:
        if passwd == '000000':
            print("[-] Password not found...")

def check(x):
    if x <10:
        passwd ="00000"+str(x)
    elif x <100:
        passwd = "0000"+str(x)
    elif x<1000:
        passwd = "000"+str(x)
    elif x<10000:
        passwd = "00"+str(x)
    elif x<100000:
        passwd = "0"+str(x)
    else:
        passwd = str(x)
    return passwd

def main():

    zFile = zipfile.ZipFile("secret.zip")

    for x in range (999999,-1,-1):      
    #999999부터 1(3번째)씩 감소하면서 -1(2번째)보다 클 때까지
        passwd =check(x)
        guess = extract(zFile, passwd)

        if guess:
            print("[+] Found password = " +passwd)
            exit(0)

if __name__ == '__main__':
#__name__은 현재 모듈이 메인이면?
    main()