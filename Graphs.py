import requests
from bs4 import BeautifulSoup
def getHTML(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
    r = requests.get(url,headers=headers)
    r.raise_for_status()
    print("get html successfully")
    r.encoding = 'utf-8'
    # print(r.text)
    return r.text

def parseHTML(html):
    try:
        soup = BeautifulSoup(html,"html.parser")
        A = soup.find_all('span',attrs = {'class':'short'})
        B = []
        for i in A:
            B.append(i.get_text())
        return B
    except:
        return []
def main():
    discuss = []
    text=''
    a = 0
    for i in range(0,100,20):
        url = 'https://movie.douban.com/subject/26100958/comments?start='+ str(i) +'&limit=20&sort=new_score&status=P'
        HTMLpage = getHTML(url)
        for t in parseHTML(HTMLpage):
            discuss.append(t)
    for i in discuss:
        text+=i
#         print(str(a) + ':' + i)
#         a = a + 1
    print(text)     
if __name__ == "__main__":
    main()
