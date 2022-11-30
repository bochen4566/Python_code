import requests
if __name__ == "__main__":
    #step 1 For specific url
    url = 'https://www.sogou.com/'
    #step 2 make a request
    response = requests.get(url = url)
    #step 3 get the requested data return the char
    page_text = response.text
    
    #step 4 make a permanent storage of the data
    with open('./sogou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("done")