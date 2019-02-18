def sum_all(*args):             #가변매개변수 *args설정
    result = 0                  #초기화
    for i in args:
        result += i
 
    return result
 
print(sum_all(1, 2, 3))         #1-3까지의 합
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))  #1-8까지의 합

sumList = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10]
print(sum_all(*sumList))

def makeURL(**kwlist):
    myUrl = "http://192.168.1.120/index.php?"
    for k, v in kwlist.items():
        myUrl += k + '=' + v + '&'

    myUrl = myUrl.rstrip('&')
    print(myUrl)

makeURL(user = 'psychoria', index = '5', page = '10')
