#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
try:
  import requests
  from bs4 import BeautifulSoup
except ImportError:
  print("Please install requests, BeautifulSoup.")

def usage():
	print "Usage: %s code" % sys.argv[0] 
	exit(255)

if len(sys.argv) == 1:
	usage()

code = sys.argv[1]

url = "http://finance.naver.com/item/main.nhn?code=" + code
s = requests.get(url)
plain_text = s.text

soup = BeautifulSoup(plain_text, "lxml")
ranks = soup.find("dl", {"class": "blind"})

if ranks == None:
	print "Unknown code(%s)" % code
	exit(255)

print ranks.get_text()
exit(0)
