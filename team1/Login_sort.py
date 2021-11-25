import requests
import json
def Login(id,pwd):
    url="http://81.68.149.16:8080/user/login"
    print(id)
    print(pwd)

    data = {
        "account": id,
        "password": pwd
    }
    res = requests.post(url=url, data=data).json()
    print(res)
    if res["message"] == "success":
        return 1
    else:
        return 0

def CUsers(email,id,pwd,phone,name):
    url = "http://81.68.149.16:8080/user"
    HEADERS = {'Content-Type': 'application/json'}
    user = {
        "email": email,
        "id": id,
        "password": pwd,
        "phone": phone,
        "username": name
    }
    res = requests.post(url=url, data=json.dumps(user), headers=HEADERS).json()
    print(res)
    return 1

def UPdate_User(email,id,pwd,phone,name):
    url = "http://81.68.149.16:8080/user"
    HEADERS = {'Content-Type': 'application/json'}
    user = {
        "email": email,
        "id": id,
        "password": pwd,
        "phone": phone,
        "username": name
    }
    res = requests.put(url=url, data=json.dumps(user), headers=HEADERS).json()
    print(res)
    return 1

def Find_User(id):
    url = "http://81.68.149.16:8080/user"
    data = {
        "id": id
    }
    res = requests.get(url=url, params=data).json()
    print(res)
    return 1

def DEL_User(id):
    url = "http://81.68.149.16:8080/user"
    HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        "id": id
    }
    res = requests.delete(url=url, data=data, headers=HEADERS).json()
    print(res)
    return 1

#print(Login('123456','qweqwe123'))
# CUsers("411294809@qq.com",123456,"qweqwe123","123111","帅哥")
# UPdate_User("411294809@qq.com",123456,"qweqwe123","123111","帅哥")
# Find_User(12)
#DEL_User('22')