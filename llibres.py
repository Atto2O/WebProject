
import urllib
from bs4 import BeautifulSoup 
import subprocess

def main():
	html = gethtml('https://www.packtpub.com/packt/offers/free-learning/')
	find_title(html)

def gethtml(link):
	#obtenim el url
	url = urllib.urlopen(link)
	##obtenim el codi
	web_code = url.read()
	
	return web_code

def find_title(code):
	#busquem entre les rames del codi
	soup = BeautifulSoup(code,"html.parser")
	
	soup = soup.find("div", "dotd-title")
	#utilizem el strip per neteijar el string
	title = str(soup.find("h2")).strip('</h2> <h2> \n').lstrip()
	#busquem la info del llibre
	soup = soup.findNext()
	soup = soup.findNext()
	soup = soup.findNext()
	
	info = str(soup).strip('</div> <div> \n').lstrip()

	show_msg(title, info)

def show_msg(title, info):
	#apareix un popup en pantalla
	subprocess.Popen(['notify-send', title])
	subprocess.Popen(['notify-send', info])

if __name__ == "__main__":
	main()
