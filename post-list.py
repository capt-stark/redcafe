# A script to get data from a list of posts on a thread. 
import urllib2

# Remove/Change the following code according to your proxy
proxy = urllib2.ProxyHandler({'http': 'proxy.iiit.ac.in:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

# 
url = 'http://www.redcafe.net/threads/juan-mata-2016-17-performances.419643/page-8'
response = urllib2.urlopen(url)
data = response.read()
file = open("mata8.html", 'w')
file.write(data)
file.close()