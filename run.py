import spider_main

if __name__ == '__main__':
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = spider_main.SpiderMain()
    obj_spider.crawl(root_url)