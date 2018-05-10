import urllib.request
from bs4 import BeautifulSoup
import re

class SpiderMain(object):
	"""docstring for SpiderMain"""
	def __init__(self):
		self.datas = []
	
	def crawl(self, url):
		html_content = self.download(url)
		soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
		urls = self.get_urls(url,soup)
		i=1
		for url in urls:
			html_content = self.download(url)
			soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
			data = self.get_data(url,soup)
			self.collect_data(data)
			if i==10:
				break
			i = i+1
		self.output_html()
		
	def collect_data(self,data):
		if data is None:
			return
		self.datas.append(data)

	def output_html(self):
		fout = open('output.html', 'w', encoding="utf-8")
		for data in self.datas:
			fout.write("<a href='")
			fout.write(data['url'])
			fout.write("'>")
			fout.write(data['title'])
			fout.write("</a>")
			fout.write("<br>")
		fout.close()

	#下载此url内容
	def download(self, url):
		response = urllib.request.urlopen(url)
		if response.getcode() != 200:
			return None
		return response.read()

	#获取需要的数据
	def get_data(self,url,soup):
		title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
		data = {}
		data['title'] = title_node.get_text()
		data['url']   = url
		return data

	def get_urls(self,url,soup):
		new_urls = set()
		links = soup.find_all('a', href=re.compile(r"/item/*"))
		for link in links:
			new_url = link['href']
			new_full_url = urllib.parse.urljoin(url, new_url)
			new_urls.add(new_full_url)
		return new_urls
