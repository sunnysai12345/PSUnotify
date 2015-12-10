import mechanize
import re
import urllib2
from random import *
br=mechanize.Browser()
br.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
br.set_handle_robots(False)
page=raw_input('Enter Page No:')
print type(page)
p=urllib2.Request('https://www.google.co.in/search?q=gate+psu+2016+ext:pdf&start='+page)
ht=br.open(p)
text='<cite\sclass="_Rm">(.+?)</cite>'
patt=re.compile(text)
h=ht.read()
url=re.findall(patt,h)
int=0
while int<len(url):
    url[int]=url[int].replace("<b>","")
    url[int]=url[int].replace("</b>","")
    int=int+1
print url
for i in url:
    try:
     q=str(randint(0,1000))
     r=urllib2.urlopen("http://"+i)
     file=open('psu2'+q+'.pdf','wb')
     file.write(r.read())
     file.close()
     print "Done"
    except urllib2.URLError as e:
     print "Sorry there exists a problem with this URL Please Download this Manually "%i

