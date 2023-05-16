# #Уровень 1
import time
from tracemalloc import start
from requests import request
from threading import Thread

def get_thread(thread_name: str):
    time.sleep(1)

    print(thread_name)

names = ['thread 1','thread 2','thread 3','thread 4','thread 5']
threads = []

for name in names:
    threads.append(Thread(target=get_thread, args=(name,)))

start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
end = time.time()
print('time:',end - start)

# #Уровень 2
def waiting(seconds: int):
    time.sleep(seconds)

start = time.time()
th1 = Thread(target=waiting, args=(2,))
th2 = Thread(target=waiting, args=(2,))

th1.start()
th2.start()
th1.join()
th2.join()
end = time.time()
print('-----параллельное выполнение-----')
print('time:', end - start)
print('-----последовательное выполнение-----')
start = time.time()
waiting(2)
waiting(2)
end = time.time()
print('time:', end - start)

#Уровень 3
links = ['https://www.google.com/', 'https://ya.ru/','https://www.bing.com/','https://duckduckgo.com/','https://www.mozilla.org/']
threads: list[Thread] = []

def get_html(link: str):
    res = request(method='GET', url=link)
    return res.text

print('-----параллельное выполнение-----')
for link in links:
    threads.append(Thread(target=get_html, args=(link,)))

start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
end = time.time()
print(end - start)

print('-----последовательное выполнение-----')
start = time.time()
get_html('https://www.google.com/')
get_html('https://ya.ru/')
get_html('https://habr.com/')
get_html('https://duckduckgo.com/')
get_html('https://www.mozilla.org/')
end = time.time()
print('time:', end - start)