# import the urlfunction. This reads html
from urllib2 import urlopen

# set the URL for the HTML content
url = 'https://en.wikipedia.org/wiki/Web_scraping'

# convert html content into string variable
html_page = urlopen(url)
html_text = html_page.read()

# set the range we want to filter\
start_tag = "<title>"
end_tag = "</title>"

start_index = html_text.find(start_tag) + len(start_tag)
end_index = html_text.find(end_tag)

#print everything
print html_text[start_index:end_index]