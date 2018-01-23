from util import *
from entity import *
import traceback


def tagTable():
    """
    爬取唯一图库中标签云下的图片
    :return:
    """
    url = "http://www.mmonly.cc/tag/"
    soup = MyHtmlParser.netUrlParser(url=url)

    tagbox_element = MyHtmlParser.getElementByFindFirst(element=soup, tag="div", param={"class": "TagBox"})
    h2s = MyHtmlParser.getElementByFind(element=tagbox_element, tag="h2", param=None)
    tagList = MyHtmlParser.getElementByFind(element=tagbox_element, tag="div", param={"class": "TagList"})
    for i in zip(h2s, tagList):
        tag = Tag.Tag()
        h2, tag_div = i
        tag.categroy = h2.text
        tag_as = MyHtmlParser.getElementByFind(element=tag_div, tag="a", param=None)
        for a in tag_as:
            a_href = MyHtmlParser.getElementByAtt(a, "href")
            a_title = MyHtmlParser.getElementByAtt(a, "title")
            tag.title = a_title
            tag.tag = str(a_href).split("/")[2]
            url1 = "https://www.mmonly.cc/tag/" + tag.tag + "/"
            try:
                soup = MyHtmlParser.netUrlParser(url=url1)
                body = MyHtmlParser.getElementByFindFirst(element=soup, tag="body", param=None)
                body_style = MyHtmlParser.getElementByAtt(body, "style")
                imageurl = body_style[str(body_style).find("(") + 1:str(body_style).find(")")]
                if str(imageurl).startswith("http"):
                    tag.imagepath = imageurl
                elif imageurl != "":
                    tag.imagepath = "http://t1.mmonly.cc" + imageurl
                p_div = MyHtmlParser.getElementByFindFirst(element=soup, tag="div", param={"class": "TagTxt"})
                if p_div is not None:
                    p_text = MyHtmlParser.getElementByFindFirst(element=p_div, tag="p", param=None).text
                    tag.tagdes = p_text
                print(tag)
                #  插入数据库
                DBUtil.tagTableAdd(tag)
            except Exception as e:
                print("出错：" + url1)
                print(traceback.print_exc())


if __name__ == '__main__':
    tagTable()

