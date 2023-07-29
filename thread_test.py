# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : thread_test.py
# Time       ：2022/6/15 10:30
# Author     ：Jago
# Email      ：18146856052@163.com
# version    ：python 3.7
# Description：
"""
import _thread
import random
import time
import threading
from threading import Thread
from queue import Queue
from random import randint
from time import sleep
import multiprocessing
from multiprocessing import Process
import concurrent
from concurrent.futures import ThreadPoolExecutor
from urllib import request
import os
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
from multiprocessing.dummy import Pool

'''
Python 3.X _thread 模块演示 Demo
当注释掉 self.lock.acquire() 和 self.lock.release() 后运行代码会发现最后的 count 为 467195 等随机值，并发问题。
当保留 self.lock.acquire() 和 self.lock.release() 后运行代码会发现最后的 count 为 1000000，锁机制保证了并发。
time.sleep(5) 就是为了解决 _thread 模块的诟病，注释掉的话子线程没机会执行了
'''

# class ThreadTest(object):
#     def __init__(self):
#         self.count = 0
#         self.lock = None
#
#     def runnable(self):
#         self.lock.acquire()
#         print('thread ident is '+str(_thread.get_ident())+', lock acquired!')
#         for i in range(0, 100000):
#             self.count += 1
#         print('thread ident is ' + str(_thread.get_ident()) + ', pre lock release!')
#         self.lock.release()
#
#     def test(self):
#         self.lock = _thread.allocate_lock()
#         for i in range(0, 10):
#             _thread.start_new_thread(self.runnable, ())
#
#
# if __name__ == '__main__':
#     test = ThreadTest()
#     test.test()
#     print('thread is running...')
#     time.sleep(5)
#     print('test finish, count is:' + str(test.count))

'''
Python 3.X threading 模块演示 Demo
threading 的 Thread 类基本使用方式（继承重写 run 方法及直接传递方法）
'''

# class NormalThread(Thread):
#     '''
#     重写类比 Java 的 Runnable 中 run 方法方式
#     '''
#     def __init__(self, name=None):
#         Thread.__init__(self, name=name)
#         self.counter = 0
#
#     def run(self):
#         print(self.getName() + ' thread is start!')
#         self.do_customer_things()
#         print(self.getName() + ' thread is end!')
#
#     def do_customer_things(self):
#         while self.counter < 10:
#             time.sleep(1)
#             print('do customer things counter is:'+str(self.counter))
#             self.counter += 1
#
#
# def loop_runner(max_counter=5):
#     '''
#     直接被 Thread 调用方式
#     '''
#     print(threading.current_thread().getName() + " thread is start!")
#     cur_counter = 0
#     while cur_counter < max_counter:
#         time.sleep(1)
#         print('loop runner current counter is:' + str(cur_counter))
#         cur_counter += 1
#     print(threading.current_thread().getName() + " thread is end!")
#
#
# if __name__ == '__main__':
#     print(threading.current_thread().getName() + " thread is start!")
#
#     normal_thread = NormalThread("Normal Thread")
#     normal_thread.start()
#
#     loop_thread = Thread(target=loop_runner, args=(10,), name='LOOP THREAD')
#     loop_thread.start()
#
#     loop_thread.join()
#     normal_thread.join()
#
#     print(threading.current_thread().getName() + " thread is end!")

'''
Python 3.X threading 与 Queue 结合演示 Demo
经典的并发生产消费者模型
'''

# class TestQueue(object):
#     def __init__(self):
#         self.queue = Queue(2)
#
#     def writer(self):
#         print('Producer start write to queue.')
#         self.queue.put('key', block=1)
#         print('Producer write to queue end. size is:'+str(self.queue.qsize()))
#
#     def reader(self):
#         value = self.queue.get(block=1)
#         print('Consumer read from queue end. size is:'+str(self.queue.qsize()))
#
#     def producer(self):
#         for i in range(5):
#             self.writer()
#             sleep(randint(0, 3))
#
#     def consumer(self):
#         for i in range(5):
#             self.reader()
#             sleep(randint(2, 4))
#
#     def go(self):
#         print('TestQueue Start!')
#         threads = []
#         functions = [self.consumer, self.producer]
#         for func in functions:
#             thread = Thread(target=func, name=func.__name__)
#             thread.start()
#             threads.append(thread)
#         for thread in threads:
#             thread.join()
#         print('TestQueue Done!')
#
#
# if __name__ == '__main__':
#     TestQueue().go()

'''
Python 3.X multiprocess 模块演示 Demo
其实完全类似 threading 用法，只不过含义和实质不同而已
multiprocess 的 Process 类基本使用方式（继承重写 run 方法及直接传递方法）
'''

# class NormalProcess(Process):
#     def __init__(self, name=None):
#         Process.__init__(self, name=name)
#         self.counter = 0
#
#     def run(self):
#         print(self.name + ' process is start!')
#         self.do_customer_things()
#         print(self.name + ' process is end!')
#
#     def do_customer_things(self):
#         while self.counter < 10:
#             time.sleep(1)
#             print('do customer things counter is:'+str(self.counter))
#             self.counter += 1
#
#
# def loop_runner(max_counter=5):
#     print(multiprocessing.current_process().name + " process is start!")
#     cur_counter = 0
#     while cur_counter < max_counter:
#         time.sleep(1)
#         print('loop runner current counter is:' + str(cur_counter))
#         cur_counter += 1
#     print(multiprocessing.current_process().name + " process is end!")
#
#
# if __name__ == '__main__':
#     print(multiprocessing.current_process().name + " process is start!")
#     print("cpu count:"+str(multiprocessing.cpu_count())+", active chiled count:"+str(len(multiprocessing.active_children())))
#     normal_process = NormalProcess("NORMAL PROCESS")
#     normal_process.start()
#
#     loop_process = Process(target=loop_runner, args=(10,), name='LOOP PROCESS')
#     loop_process.start()
#
#     print("cpu count:" + str(multiprocessing.cpu_count()) + ", active chiled count:" + str(len(multiprocessing.active_children())))
#     normal_process.join()
#     loop_process.join()
#     print(multiprocessing.current_process().name + " process is end!")

'''
这是主线程： MainThread
主线程结束！ MainThread
一共用时： 0.0020024776458740234
当前线程的名字是：  Thread-2
当前线程的名字是：  Thread-1
当前线程的名字是：  Thread-3
当前线程的名字是：  Thread-5
当前线程的名字是：  Thread-4
'''

# def run():
#     time.sleep(2)
#     print('当前线程的名字是： ', threading.current_thread().name)
#     time.sleep(2)
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#
#     print('这是主线程：', threading.current_thread().name)
#     thread_list = []
#     for i in range(5):
#         t = threading.Thread(target=run)
#         thread_list.append(t)
#
#     for t in thread_list:
#         t.start()
#
#     print('主线程结束！', threading.current_thread().name)
#     print('一共用时：', time.time()-start_time)

'''
这是主线程： MainThread
主线程结束了！ MainThread
一共用时： 0.002000093460083008
'''

# def run():
#     time.sleep(2)
#     print('当前线程的名字是： ', threading.current_thread().name)
#     time.sleep(2)
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#
#     print('这是主线程：', threading.current_thread().name)
#     thread_list = []
#     for i in range(5):
#         t = threading.Thread(target=run)
#         thread_list.append(t)
#
#     for t in thread_list:
#         t.setDaemon(True)
#         t.start()
#
#     print('主线程结束了！', threading.current_thread().name)
#     print('一共用时：', time.time()-start_time)

'''
这是主线程： MainThread
当前线程的名字是： 当前线程的名字是：  Thread-3当前线程的名字是：  Thread-4
当前线程的名字是：  Thread-2
 Thread-1
当前线程的名字是： 
 Thread-5
主线程结束了！ MainThread
一共用时： 4.013599872589111
'''

# def run():
#     time.sleep(2)
#     print('当前线程的名字是： ', threading.current_thread().name)
#     time.sleep(2)
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#
#     print('这是主线程：', threading.current_thread().name)
#     thread_list = []
#     for i in range(5):
#         t = threading.Thread(target=run)
#         thread_list.append(t)
#
#     for t in thread_list:
#         t.setDaemon(True)
#         t.start()
#
#     for t in thread_list:
#         t.join()
#
#     print('主线程结束了！', threading.current_thread().name)
#     print('一共用时：', time.time()-start_time)

'''
Python 3.X ThreadPoolExecutor 模块演示 Demo
'''

# class TestThreadPoolExecutor(object):
#     def __init__(self):
#         self.urls = [
#             'https://www.baidu.com/',
#             'http://blog.jobbole.com/',
#             'http://www.csdn.net/',
#             'https://juejin.im/',
#             'https://www.zhihu.com/'
#         ]
#
#     def get_web_content(self, url=None):
#         print('start get web content from: '+url)
#         try:
#             headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}
#             req = request.Request(url, headers=headers)
#             return request.urlopen(req).read().decode("utf-8")
#         except BaseException as e:
#             print(str(e))
#             return None
#
#     def runner(self):
#         thread_pool = ThreadPoolExecutor(max_workers=2, thread_name_prefix='DEMO')
#         futures = dict()
#         for url in self.urls:
#             future = thread_pool.submit(self.get_web_content, url)
#             futures[future] = url
#
#         for future in concurrent.futures.as_completed(futures):
#             url = futures[future]
#             try:
#                 data = future.result()
#             except Exception as e:
#                 print('Run thread url ('+url+') error. '+str(e))
#             else:
#                 print(url+'Request data ok. size='+str(len(data)))
#         print('Finished!')
#
#
# if __name__ == '__main__':
#     TestThreadPoolExecutor().runner()

# gMoney = 0
# gCondition = threading.Condition()
# gTime = 0
#
#
# class Producer(threading.Thread):  # 定义生产者类
#     def run(self) -> None:
#         global gMoney  # 定义为全球变量
#         global gTime
#         while True:
#             gCondition.acquire()  # 获取线程
#             if gTime >= 10:  # 如果生产者生产次数大于10
#                 gCondition.release()  # 释放线程并推出循环
#                 break
#             money = random.randint(0, 100)  # 生产的钱在0，100之间随机取
#             gMoney += money  # 赋值给生产的钱
#             gTime += 1  # 生产次数加一
#             print("%s生产了%d元" % (threading.current_thread().name, money))  # 生产者的名字和生产的钱
#             gCondition.notify_all()  # 唤醒所有等待的线程
#             gCondition.release()  # 释放掉当前线程
#             time.sleep(1)
#
#
# # 整个过程是获取线程-唤醒所有等待的其他线程-然后把当前线程释放掉（在取获取线程这样的一个过程）
# class Consumer(threading.Thread):
#     def run(self) -> None:
#         global gMoney  # 消费者主要负责花钱，直至花完，所以不用定义次数
#         while True:  # 进入循环
#             gCondition.acquire()  # 获取次数
#             money = random.randint(0, 100)  # 花钱的数量
#             while gMoney < money:  # 当剩的钱不足以支撑花的钱的时候
#                 if gTime >= 10:  # 消费者消费大于等于10次后
#                     print("%s想要消费%d元，但是目前只有%d元,生产者已经不在生产！" % (threading.current_thread().name, money, gMoney))
#                     gCondition.release()
#                     return
#                 print("%s想要消费%d元，但是目前只有%d元,消费失败！" % (threading.current_thread().name, money, gMoney))  # 不大于10次时候就不足以支持消费者花销，打印消费失败！
#                 gCondition.wait()  # 消费者线程等待，等待生产者为他生产
#             gMoney -= money
#             print("%s想要消费%d元，目前剩余只有%d元" % (threading.current_thread().name, money, gMoney))
#             gCondition.release()
#             time.sleep(1)
#
#
# def main():
#     for i in range(5):
#         th = Producer(name='生产者%d号' % i)
#         th.start()  # 制造5个生产者
#     for i in range(5):
#         th = Consumer(name="消费者%d号" % i)
#         th.start()  # 制造5个消费者者
#
#
# if __name__ == "__main__":
#     main()

# 爬取的主网站地址
start_url = 'https://www.kanunu8.com/book2/11138/'
"""
获取网页源代码
:param url: 网址
:return 网页源代码
"""


def get_source(url):
    html = requests.get(url)
    return html.content.decode('gbk')  # 这个网页需要使用gbk方式解码才能让中文正常显示


"""
获取每一章链接，储存到一个列表中并返回
:param html: 目录页源代码
:return: 每章链接
"""


def get_article_url(html):
    article_url_list = []
    article_block = re.findall('正文(.*?)<div class="clear">', html, re.S)[0]
    article_url = re.findall('<a href="(\d*.html)">', article_block, re.S)
    for url in article_url:
        article_url_list.append(start_url + url)
    return article_url_list


"""
获取每一章的正文并返回章节名和正文
:param html: 正文源代码
:return: 章节名，正文
"""


def get_article(html):
    chapter_name = re.findall('<h1>(.*?)<br>', html, re.S)[0]
    text_block = re.search('<p>(.*?)</p>', html, re.S).group(1)
    text_block = text_block.replace('&nbsp;', '')  # 替换 &nbsp; 网页空格符
    text_block = text_block.replace('<p>', '')  # 替换 <p></p> 中的嵌入的 <p></p> 中的 <p>
    return chapter_name, text_block


"""
将每一章保存到本地
:param chapter: 章节名, 第X章
:param article: 正文内容
:return: None
"""


def save(chapter, article):
    os.makedirs('北欧众神', exist_ok=True)  # 如果没有"北欧众神"文件夹，就创建一个，如果有，则什么都不做"
    with open(os.path.join('北欧众神', chapter + '.txt'), 'w', encoding='utf-8') as f:
        f.write(article)


"""
根据正文网址获取正文源代码，并调用get_article函数获得正文内容最后保存到本地
:param url: 正文网址
:return: None
"""


def query_article(url):
    article_html = get_source(url)
    chapter_name, article_text = get_article(article_html)
    # print(chapter_name)
    # print(article_text)
    save(chapter_name, article_text)


if __name__ == '__main__':
    toc_html = get_source(start_url)
    toc_list = get_article_url(toc_html)
    pool = Pool(4)
    pool.map(query_article, toc_list)
