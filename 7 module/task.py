from requests import request
from bs4 import BeautifulSoup as BS
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')
np.random.seed(3)
x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))

response = request(method='GET', url='https://mfd.ru/currency/?currency=USD')

table = BS(response.text).find('table', class_='mfd-table mfd-currency-table')

usdt_courses = []

i = 0
for tr in table:
    if i < 10:
        usdt_courses.append(tr.find_all_next('td')[1].text)
        i += 1

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(usdt_courses) 
    
plt.show()