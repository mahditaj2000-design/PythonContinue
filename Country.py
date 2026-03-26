import mariadb as ma
import requests
from bs4 import BeautifulSoup as bs

url = "https://www.scrapethissite.com/pages/simple/"

def data(n , c , p , a):
    con = ma.connect(
        host = "localhost",
        user = "root",
        password = "",
        port = 3307,
        database = "information"
    )
    crs = con.cursor()

    crs.execute("INSERT INTO country (name , capital , population , area) VALUES (?,?,?,?)", (n ,c , p , a))
    con.commit()


def Countries():
    req = requests.get(url)
    text = req.text
    soup = bs(text , "html.parser")

    s1 = soup.find_all(class_ = "country-name")
    s2 = soup.find_all(class_ = "country-capital")
    s3 = soup.find_all(class_ = "country-population")
    s4 = soup.find_all(class_ = "country-area")
    
    count = 0

    for i , ii , iii , iiii in zip(s1 , s2 , s3 , s4):  
        n = i.get_text(strip=True)
        c = ii.get_text(strip=True)
        p = iii.get_text(strip=True)
        a = iiii.get_text(strip=True)

        data(n , c , p , a)

        count += 1
        if count == 20:
            break

Countries()