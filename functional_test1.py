from selenium import webdriver

browser = webdriver.Chrome("C:\\Users\\Odysseus\\Downloads\\chromedriver.exe")
browser.get('http://localhost:8000')

assert 'Django' in browser.title

browser.quit