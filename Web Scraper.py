import requests
from bs4 import BeautifulSoup
import pickle

URL = "https://www.google.com/"
URL2 = "https://www.bing.com/"
URL3 = "https://www.safari.com/"

number_of_data = 3
data = []


page = requests.get(URL)
page2 = requests.get(URL2)
page3 = requests.get(URL3)

for i in range(number_of_data):
    raw = (page.text)
    raw2 = (page2.text)
    raw3 = (page3.text)

    data.append(raw)
    data.append(raw2)
    data.append(raw3)

    file = open('db_contents', 'wb')
    pickle.dump(data, file)
    file.close()
    
    input1 = input('\n\nScraped data successfully serialized!')

