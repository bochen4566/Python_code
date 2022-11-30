import requests
import json

if __name__ == "__main__":
    url = 'https://fanyi.baidu.com/sug'

    #UA
    headers = {#the dictionary is defined here as a parameter
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    word = input('enter word:')

    data = {
        'kw':word
    }

    response = requests.post(url=url, data=data, headers=headers)
    #the return type is json so that requires the use of json here
    dic_obj = response.json()
    fileName = word+'.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
    fp.close()
    print('done')
