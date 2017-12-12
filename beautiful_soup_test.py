from bs4 import BeautifulSoup
from urllib2 import urlopen

my_address = "https://docs.python.org/2/whatsnew/2.7.html"
html_page = urlopen(my_address)
html_text = html_page.read()

soup = BeautifulSoup(html_text, "lxml")

print soup.get_text().encode("utf-8")