#coding:utf8
# import httplib
# #http://www.mmonly.cc/mmtp/hgmn/
# #创建连接
# conn= httplib.HTTPConnection("www.mmonly.cc")
# # httplib.HTTPSConnection
# #写子路径
# conn.request('GET','/mmtp/hgmn/')
# response = conn.getresponse()
# print  response.status
# #打印请求的内容
# print response.read().decode("GBK")
# conn.close()


# import urllib
# htmlString = urllib.urlopen("http://www.mmonly.cc/mmtp/hgmn/")
# #获取基本信息
# print  htmlString.info()
# #获得状态码
# print  htmlString.getcode()
# #获得消息体
# print  htmlString.read().decode("GBK")

#import urllib
# import urllib2
# url="http://www.mmonly.cc/mmtp/hgmn/"
# req = urllib2.Request(url)
# response = urllib2.urlopen(req)
# print response.code
# print response.read().decode("GBK")

# import requests
# url="http://www.mmonly.cc/mmtp/hgmn/"
# res = requests.get(url,None)
# print res.status_code
# print res.content.decode("GBK")

import requests
coding = "GBK"
"""
url 是地址
param 是参数  类型字典
"""


def getURLHtml(url, param):
    res = requests.get(url, param)
    if res.status_code == 200:
        return res.content.decode(coding)
    else:
        return None







