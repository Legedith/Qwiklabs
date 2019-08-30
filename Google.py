from bs4 import BeautifulSoup
with open("Qwiklabs.html", encoding='utf-8') as fp:
    soup = BeautifulSoup(fp,'html.parser')
    a = soup.find_all('code',attrs={'class': None})
    f = open("code.txt","w")
    for i in a:
        s=i.get_text()
        f.write(s)
        f.write('\n')
    f.close()