from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://www.weather.go.kr/w/weather/forecast/short-term.do')

table = driver.find_element_by_xpath('/html/body/div[2]/section/div/div[3]/div[2]/section/div[4]/div/table')