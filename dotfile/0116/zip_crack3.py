import zipfile

zFile = zipfile.ZipFile("secret.zip")
 
for x in range (0,100000):
    if x %  100000 ==0:
        print("[*] Looking for password...",x)
    if x <10:
        passwd ="00000"+str(x)
    elif x <100:
        passwd = "0000"+str(x)
    elif x<1000:
        passwd = "000"+str(x)
    elif x<10000:
        passwd = "00"+str(x)
    else:
        passwd = str(x)
    try:
        zFile.extractall(pwd=bytes(passwd,'utf-8'))
        print("[+ ] Found password = "+str(x))
        exit(0)
    except Exception as e:
        pass
