import zipfile

zFile = zipfile.ZipFile("")
#zipfile모듈의 ZipFile()메서드를 호출
#ZipFile()메서드는 zip파일의 이름을 넣어준다.

zFile.extractall(pwd=b"aaa")
#zFile변수를 추출한다.
