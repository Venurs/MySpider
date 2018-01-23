#py3自带html解析库，但是不够强大
#SGMLParser->BeautifulSoup4 bs4

#tag  标签
#class
#attrs
#id
from bs4 import *
from util import HttpUtil
"""
网络地址dom解析
url html网络地址
"""


def netUrlParser(url):
    soup = BeautifulSoup(HttpUtil.getURLHtml(url, None), 'html.parser')
    return soup

"""
解析内容
element 文档流
tag     标签
param   接收的格式是字典  class、id、name
"""


def getElementByFindFirst(element, tag, param):
    if param == None:
        return element.find(tag)
    else:
        return element.find(tag, param)


def getElementByFind(element, tag, param):
    if param == None:
        return element.findAll(tag)
    else:
        return element.findAll(tag, param)

"""
解析属性
element 解析后的文档流
attName 属性名
"""


def getElementByAtt(element, attName):
    return element.get(attName)