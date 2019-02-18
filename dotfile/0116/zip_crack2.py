import zipfile

zFile = zipfile.ZipFile("secret.zip")
try:        #원랴 동작하는 코드!!
    zFile.extractall(pwd=b'1234')
except Exception as e:
    #동작하다가 에러가 발생할 경우 이부분에서 동작!!
    #Exception as e는 에러는 e 로 정의하겠다는 말이다!!
    print(e)
    #그리고 에러를 출력한다
