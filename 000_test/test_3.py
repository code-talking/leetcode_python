# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/20/18
    Time:   9:30 AM
    Package 
    File    test_3.py
    Description
    
'''
from urllib import request

url = 'https://blog.csdn.net/c406495762/article/details/58716886'
if __name__ == '__main__':
    def run():
        response = request.urlopen(url)
        html = response.read()
        html = html.decode('utf-8')
        print(html)

    run()

