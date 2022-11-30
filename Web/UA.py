import requests
if __name__ == "__main__":
    #step 1 For specific url
    url = 'https://www.sogou.com/web'
    #step 2 make a request and use ua to modify the search
    headers = {#the dictionary is defined here as a parameter
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    kw = input('enter a word:')

    param = {
        'query':kw
    }
    response = requests.get(url = url, params=param,headers=headers)
    #step 3 get the requested data return the char
    page_text = response.text
    fileName = kw+'.html'
    #step 4 make a permanent storage of the data
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("done")