from requests import request
from bs4 import BeautifulSoup as BS
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')
np.random.seed(3)
x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))

usdt_courses = []
page = request(method='GET', url='https://mfd.ru/currency/?currency=USD')
soup = BS(page.text, 'html.parser')
table = soup.find('table',{'class':'mfd-table mfd-currency-table'})
tds = table.find_all('td')
tds = (i.text for i in tds)

rows = []
row = []
i = 0
for td in tds:
    row.append(td)
    i += 1
    if i == 3:
        usdt_courses.append(row[1])
        i = 0
        row.clear()

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(usdt_courses) 
    
plt.show()