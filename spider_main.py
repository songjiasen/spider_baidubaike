import urllib.request
from bs4 import BeautifulSoup
import re

class SpiderMain(object):
	"""docstring for SpiderMain"""
	#def __init__(self):
		
	def crawl(self, url):
		html_content = self.download(url)
		soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
		urls = self.get_urls(url,soup)
		i=1
		fout = open('output.html', 'w', encoding="utf-8")
		for url in urls:
			html_content = self.download(url)
			soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
			data = self.get_data(soup)
			fout.write(data)
			fout.write("<br>")
			if i==10:
				break
			i = i+1
		fout.close()

	#下载此url内容
	def download(self, url):
		response = urllib.request.urlopen(url)
		if response.getcode() != 200:
			return None
		return response.read()

	#获取需要的数据
	def get_data(self,soup):
		title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
		title = title_node.get_text()
		return title

	def get_urls(self,url,soup):
		new_urls = set()
		links = soup.find_all('a', href=re.compile(r"/item/*"))
		for link in links:
			new_url = link['href']
			new_full_url = urllib.parse.urljoin(url, new_url)
			new_urls.add(new_full_url)
		return new_urls
