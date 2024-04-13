# 设置延滞时间
import time
# http访问
import requests
# html处理器
from bs4 import BeautifulSoup


class Spider:
    def __init__(self):
        # 二元组,第一关键字是连接,第二关键字是章节名称
        self.href_chapter = []

        self.url = None
        self.headers = None
        self.save_path = './HLM_FullText.txt'

    # 将所有章节的链接取下来存到二元组里
    def all_page(self):

        self.url = 'https://hongloumeng.5000yan.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.1'
        }
        page_text = requests.get(url=self.url, headers=self.headers, timeout=10)

        page_text.encoding = 'utf-8'
        page_content = page_text.text
        # 现在page_content就是该网页的html原码
        soup = BeautifulSoup(page_content, 'html.parser')
        all_chapters = soup.findAll("li", attrs={'class': 'menu-item'})

        # 二元组存储每个章节的url,该章节的名字

        # 提取字段中的连接和章节名称,,,
        for item in all_chapters:
            a_tag = item.find('a')
            href = a_tag['href']
            chapter = a_tag.text.strip()

            self.href_chapter.append([str(href), str(chapter)])
        # 提取到的信息前四条是没用的,直接删了
        del self.href_chapter[:4]
        # print(href,chapter,sep='    ')

        for x in self.href_chapter:
            print(x[0], x[1], sep=' ')

    def every_page(self):
        all = len(self.href_chapter)
        with open(self.save_path, 'a', encoding='utf-8') as file:
            for i in range(all):
                # temp表示该列表中的每一个二元组
                temp = self.href_chapter[i]
                url = temp[0]
                page_text = requests.get(url=url, headers=self.headers, timeout=10)
                page_text.encoding = 'utf-8'
                page_content = page_text.text
                soup = BeautifulSoup(page_content, 'html.parser')
                # article中存放的是文章的内容
                articles = soup.findAll('div', attrs={'class': 'grap'})
                for idx, article in enumerate(articles, start=1):
                    # 提取纯文本内容
                    text = article.get_text()
                    print(text)
                    # 写入文件时设置保存路径
                    file.write(temp[1] + text)
                # 每次请求之后休眠一段时间
                time.sleep(1)  # 休眠1秒

    def run_spider(self):
        self.all_page()
        self.every_page()
