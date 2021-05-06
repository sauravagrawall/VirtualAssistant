from selenium import webdriver
import pyttsx3 as px

engine = px.init()
engine.setProperty('rate',190)
def speak(text):
    engine.say(text)
    engine.runAndWait()

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')

    def get_info(self,query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()
        read = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[1]')
        r = read.text
        r.split('.')
        r1 = r.split('.')[0]
        speak(r1)


