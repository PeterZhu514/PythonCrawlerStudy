#!usr/bin/env python
#-*- coding=utf-8 -*-
#__author__='peterzhu514@gmail.comp'

#基本逻辑：url构建->获取html网页->获取contens->写入文件或输出

import requests
from bs4 import BeautifulSoup

def get_url(depth):
	depth=int(depth)
	url_list=[]
	head_url="http://tieba.baidu.com/f?kw=%E5%85%AD%E4%BA%BA%E8%A1%8C&ie=utf-8&pn="
	for i in range(0,depth):
		url_list.append(head_url+str(i*50))
	return url_list

def get_html(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding='utf-8'
		return r.text
	except:
		return'Error'
		
def get_contents(url):
	contents=[]
	html=get_html(url)

	soup=BeautifulSoup(html,'lxml')

	litags=soup.find_all('li',attrs={'class':' j_thread_list clearfix'})
	
	for li in litags:
		comment={}
		try:
			comment['title']=li.find('a',attrs={'class':'j_th_tit '}).text.strip()
			comment['link']='http://tieba.baidu.com'+li.find('a',attrs={'class':'j_th_tit '})['href']
			comment['name']=li.find('a',attrs={'class':'frs-author-name j_user_card '}).text.strip()
			comment['time']=li.find('span',attrs={'class':'threadlist_reply_date pull_right j_reply_data'}).text.strip()
			contents.append(comment)
		except:
			print('出Bug啦！')
	return contents


def out_file(dict):
	with open('tiebadata.txt','a+',encoding='utf-8') as f:
		for comment in dict:
			f.write("标题：{}\t链接：{}\t发帖人：{}\t最后回复时间：{}\n".format(comment['title'],comment['link'],comment['name'],comment['time']))
		print('当前页面爬取完成啦！')

def main():
	depth=int(input("请输入爬取的页数："))
	url_list=get_url(depth)	
	for url in url_list:
		content=get_contents(url)
		out_file(content)
	print('所有的爬取工作都已经完成啦！')

if __name__=='__main__':
	main()
			
