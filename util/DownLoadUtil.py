import urllib
import requests

"""
url 网络地址
path 本地保存地址
"""
def downLoadPhotoForUrllib(url,path):
    #进行保存
    try:
        urllib.urlretrieve(url,path)
        return True
    except:
        return False


"""

"""
def downLoadPhotoForRequest(url,path):
    #发起请求
    ir=requests.get(url,stream=True)
    if ir.status_code == 200:
        with open(path,'wb') as f:
            for chunk in ir:
                f.write(chunk)
        return True
    else:
        return False


