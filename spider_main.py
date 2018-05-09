import urllib.request
from bs4 import BeautifulSoup

class SpiderMain(object):
	"""docstring for SpiderMain"""
	#def __init__(self):
		
	def crawl(self, url):
		html_content = self.download(url)
		data = self.get_data(html_content)
		self.output_html(data)
	#下载此url内容
	def download(self, url):
		response = urllib.request.urlopen(url)
		if response.getcode() != 200:
			return None
		return response.read()

	#获取需要的数据
	def get_data(self,content):
		soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
		title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
		title = title_node.get_text()
		return title

	#将数据写入文件
	def output_html(self,data):
		fout = open('output.html', 'w', encoding="utf-8")
		fout.write(data)
		fout.close()