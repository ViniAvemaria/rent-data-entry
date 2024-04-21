from driver import Driver
from soup import Soup


RENT = "https://appbrewery.github.io/Zillow-Clone/"
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfmHWLAADlkfAmysZa7Ni3_LVWxcmo5BVFUm_aqo6Yi9D29sg/viewform?hl=en"

soup = Soup(RENT)
addresses = soup.find_adresses()
prices = soup.find_prices()
links = soup.find_links()

driver = Driver()
driver.open_page(FORM)
driver.answer_form((addresses, prices, links))
driver.quit()
