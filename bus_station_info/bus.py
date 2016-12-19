#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import os
import requests
from bs4 import BeautifulSoup

def usage():
	print "Usage: %s code" % sys.argv[0] 
	exit(255)

if len(sys.argv) == 1:
	usage()

code = sys.argv[1]

os.system('clear')
url = "http://bus.go.kr/xmlRequest/getStationByUid.jsp?strBusNumber=" + code
s = requests.get(url)
plain_text = s.text

soup = BeautifulSoup(plain_text, "lxml")
#print soup
print "Bus station : " + soup.find('stnm').string
print '---------------------------'
for link in soup.find_all('stationlist'):
	print "|   Bus : " + link.rtnm.string
	print "|   1) " + link.arrmsg1.string
	print "|   2) " + link.arrmsg2.string
	print '---------------------------'

exit(0)
