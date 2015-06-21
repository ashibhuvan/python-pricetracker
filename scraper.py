import datetime
import urllib
from lxml import etree
import requests 
import StringIO
import time

print "Enter tracker url"
variable = raw_input("-->")
result = urllib.urlopen(variable)
html = result.read()

parser = etree.HTMLParser()
tree = etree.parse(StringIO.StringIO(html),parser)


filtered_html = tree.xpath('//*[@id="prices"]/div[1]/div/span[1]/text()')

print filtered_html
print 'The time is      :', time.ctime()
			
	




"""http://thetracktor.com/detail/B00A2T6X0K"""





