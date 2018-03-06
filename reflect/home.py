# _*_coding:utf-8_*_
# !/bin/env python

url = raw_input('please input url')
format_url = url.split('/')

packagefile = __import__('backend.' + format_url[0])
module1 = getattr(packagefile, format_url[0])
func2 = getattr(module1, format_url[1])
func2()
