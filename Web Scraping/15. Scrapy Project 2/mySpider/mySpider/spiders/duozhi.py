# -*- coding: utf-8 -*-
import scrapy
from ..items import MyspiderItem
from bs4 import BeautifulSoup

class DuozhiSpider(scrapy.Spider):
    name = 'duozhi' #scrapy爬虫程序的唯一标识，用于区分不同的spider爬虫
    allowed_domains = ['duozhi.com'] #允许爬取的域名
    start_urls = ['http://duozhi.com/'] #爬虫程序起始的爬取url

    #解析提取
    def parse(self, response):
        #print(response, response.text)
        bs_response = BeautifulSoup(response.text, 'html.parser')
        posts = bs_response.find_all('div', class_= 'post-inner')
        for post in posts:
            item = MyspiderItem()
            item['post_title'] = post.find('a', class_= 'post-title').text.replace(' ', '')
            item['post_desc'] = post.find('p',class_= 'post-desc').text.replace(' ', '')
            yield item #return item