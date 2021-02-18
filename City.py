# Yair Gat 18.2.2021
from selenium import webdriver


# The city class holds attribute cities which is list of all city in the program and function that return
# the local news in each city in the list.
class City:
    # Constructor City object.
    def __init__(self):
        self.cities = ['Paris', 'Jerusalem', 'London', 'Washington']  # All the city in the program.

    # return the cities.
    def get_cities(self):
        return self.cities

    # Get city and return the local news in that city.
    def get_local_news(self, city):
        country_local_news = {'Jerusalem': 'https://www.jpost.com/',
                              'London': 'https://www.bbc.com/news/england/london',
                              'Washington': 'https://www.washingtonpost.com/'}
        PATH = 'C:\Program Files (x86)\chromedriver.exe'
        driver = webdriver.Chrome(PATH)
        driver.get(country_local_news[city])
        return driver.title
