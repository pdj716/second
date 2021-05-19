from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://www.weather.go.kr/w/weather/forecast/short-term.do')

table = driver.find_element_by_xpath('/html/body/div[2]/section/div/div[3]/div[2]/section/div[4]/div/table')

lists = []
count = 0
for i in table.find_elements_by_css_selector('tr'):
    count += 1
    list = []
    for m in i.find_elements_by_css_selector('th'):
        print(m.text,end=' ')
        list.append(m.text)

    for n in i.find_elements_by_css_selector('td'):
        print(n.text,end=' ')
        list.append(n.text)

    print('')

    lists.append(list)

    if count == 3:
        break

for i in lists:
    del i[0]

day_list = lists[0]
min_list1 = lists[1]
max_list1 = lists[2]