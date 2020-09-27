import requests


def main():
    # 配置账号信息
    url = "https://www.baidu.com/"
    uKey = "uuu"
    api_key = "akak"

    apkPath = "C:/Users/Administrator/Desktop/test.apk"
    apkfile = {"file":open(apkPath,"rb")}
    headers = {"enctype":"multipart/form-data"}
    payload= {
        "uKey":uKey,
        "_api_key":api_key,
        "installType":1,
        "updateDescription":"android自动化打包"
    }

    print(payload)
    print(apkfile)
    r = requests.post(url,data= payload,headers=headers,files = apkfile)
    r = requests.get(url)
    jsonResult = r.json()
    print(r)


if __name__ == '__main__':
    main()