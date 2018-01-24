from util import *
from entity import *
import traceback
import time


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


def groupidTable():
    # 组图的链接列表
    urls = ["mmtp/xgmn/"]
    i = 0
    for url in urls:
        error = 0
        j = 1
        while j != -1:
            if error >= 1000:
                print("%s错误次数已达上限，跳过该链接" % url)
                j = -1
                continue
            wholeurl = config.MMONLY_URL + url + "list" + "_" + str(i + 10) + "_" + str(j) + ".html"
            try:
                soup = MyHtmlParser.netUrlParser(url=wholeurl)
            except Exception as e:
                print("错误：" + wholeurl)
                print(traceback.print_exc())
                j = -1
                continue
            if soup == None:
                continue
            image_div = MyHtmlParser.getElementByFind(element=soup, tag="div", param={"class":"item masonry_brick masonry-brick"})
            for tag_a in image_div:
                # 获取groupid
                groupid_a = MyHtmlParser.getElementByFindFirst(element=tag_a, tag="a", param=None)
                group_url = MyHtmlParser.getElementByAtt(element=groupid_a, attName="href")
                groupid = group_url[str(group_url).rfind("/") + 1: str(group_url).rfind(".")]
                # 获取path
                path = "/" + str(group_url).split("/")[-3] + "/" + str(group_url).split("/")[-2] + "/"
                # 获取photodes
                group_img = MyHtmlParser.getElementByFindFirst(element=tag_a, tag="img", param=None)
                photodes = MyHtmlParser.getElementByAtt(element=group_img, attName="alt")
                # 获取headerimagepath
                headerimagepath = MyHtmlParser.getElementByAtt(element=group_img, attName="src")
                # 获取size和time
                group_size_time = MyHtmlParser.getElementByFindFirst(element=tag_a, tag="div", param={"class": "items_likes"}).text.replace("\xa0\xa0", " ").split(" ")
                # 处理获取的时间和大小信息
                size = group_size_time[2][1:-1]
                time0 = group_size_time[0].split(":")[1] + " " + group_size_time[1]
                timeArr = time.strptime(time0, "%Y-%m-%d %H:%M:%S")
                createTime = str(int(time.mktime(timeArr)))
                # 初始化一个GroupId对象
                # __init__(self, groupid, headerimagepath, photodes, creatertime, size, path, userid, status=None)
                groupid = GroupId.GroupId(groupid, headerimagepath, photodes, createTime, size, path)
                DBUtil.groupIdTableAdd(groupid)
            error += 1
            j += 1
        i += 1


if __name__ == '__main__':
    groupidTable()
    # tagTable()


