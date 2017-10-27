#!/usr/bin/env python
# _*_ coding:utf8 _*_ 
__date__ = '2017/10/27 22:16'
__author__ = 'zhourudong'


dsn="http://34194604e3da46f6a2bee19462af4347:7b41b44770804262bc56e18f32dcba62@192.168.193.133:9000/2"


pdsn="http://34194604e3da46f6a2bee19462af4347@192.168.193.133:9000/2"


from raven import Client

client = Client(dsn)

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()
