import requests
import array
import schedule 
import time
from bs4 import BeautifulSoup

def scraper():
    URL = "https://www.blockchain.com/btc/unconfirmed-transactions"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="sc-20ch6p-0 beTSoK")
    job_elements = results.find_all("div", class_="sc-1g6z4xm-0 hXyplo")
    bitcoin = []
    for job_element in job_elements:
        hash = job_element.find("a", class_="sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK")
        hash = hash.text.strip()
        bitcoin.append(hash)
        i = job_element.find_all("div", class_= "sc-6nt7oh-0 PtIAf")
        for j in i:
            amount = j.find_all("span", class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC")
            for a in amount:
                a = a.text.strip()
                bitcoin.append(a)
    BT= []
    for word in bitcoin:
        word = word.replace("BTC","").replace("$","")
        BT.append(word)
    n = 3
    m = len(BT)
    while n < (m/4)-8:
        if BT[n] < BT[n+4]:
            del BT[n-3:n+1]
        elif BT[n] > BT[n+4]:
            del BT[n+1:n+5]
        else:
            del BT[n-3:n+1]
        n = n + 4
    
    n = 4
    BT = BT[:n]
    print(BT)
    

scraper()

schedule.every(1).minutes.do(scraper)
while True:
    schedule.run_pending()
    time.sleep(1)




