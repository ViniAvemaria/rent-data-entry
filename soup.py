from bs4 import BeautifulSoup
import requests


class Soup():
    def __init__(self, url) -> None:
        header = {
            "Accept-Language": "en-GB,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
        }

        response = requests.get(url=url, headers=header)
        self.soup = BeautifulSoup(response.content, "html.parser")

    def find_adresses(self):
        addr = self.soup.findAll("a", class_="StyledPropertyCardDataArea-anchor")
        all_addr = [a.getText().strip() for a in addr]
        return all_addr

    def find_prices(self):
        prices = self.soup.findAll("span", class_="PropertyCardWrapper__StyledPriceLine")
        all_prices = []
        for p in prices:
            if "+" in p.getText():
                all_prices.append(p.getText().split("+")[0])
            elif "/" in p.getText():
                all_prices.append(p.getText().split("/")[0])
        return all_prices

    def find_links(self):
        links = self.soup.findAll("a", class_="StyledPropertyCardDataArea-anchor")
        all_links = [l.get("href") for l in links]
        return all_links
