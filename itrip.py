# -*- coding: utf-8 -*-

import urllib2
import urllib
import re
url = "http://www.itrip.com/ouzhou/"
url1 ="http://item.jd.com/1692335000.html"
response = urllib2.urlopen(url).read()
#print response.decode("utf-8")

