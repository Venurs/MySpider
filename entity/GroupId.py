from hashlib import md5
from util import *

class GroupId:
    groupid = ""
    headerimagepath = ""
    photodes = ""
    creatertime = ""
    size = ""
    path = ""
    saveimagepath = ""
    userid = ""
    status = ""

    def __init__(self, groupid, headerimagepath, photodes, createtime, size, path, userid=None, status=None):
        self.groupid = groupid
        self.headerimagepath = headerimagepath
        self.photodes = photodes
        self.createtime = createtime
        self.size = size
        self.path = path
        if userid == None:
            self.userid = config.USERID
        else:
            self.userid = userid
        self.status = status
        imagename = make_md5(headerimagepath)
        self.saveimagepath = config.GROUPIDHEADER_PATH + imagename + ".jpg"


def make_md5(str):
    m = md5()
    m.update(str.encode("utf-8"))
    return m.hexdigest()

