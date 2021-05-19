from selenium import webdriver
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

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

min_list2 = []
max_list2 = []
for i in min_list1:
    a,b = i.split('~')
    a = float(a)
    b = float(b)
    min = (a+b)/2
    min_list2.append(min)

for i in max_list1:
    a,b = i.split('~')
    a = float(a)
    b = float(b)
    max = (a+b)/2
    max_list2.append(max)

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

plt.plot(range(1,6),min_list2,label='최저기온',color='lightskyblue')
plt.plot(range(1,6),max_list2,label='최고기온',color='lightpink')
plt.suptitle('최저기온과 최고기온')
plt.xticks(range(1,7),day_list,fontsize=9)
plt.xlabel('날짜')
plt.ylabel('온도')
plt.legend()
plt.show()