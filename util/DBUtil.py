import mysql.connector as mysql
from util import config

"""
执行语句 增删改
成功返回True
失败返回False
"""


def executeSQL(sql):
    """

    :param sql:
    :return:
    """
    cnx= mysql.connect(user=config.USER, password=config.PASSEORD, host=config.HOST, database=config.DATABASE)
    try:
        cursor = cnx.cursor()
        cursor.execute(sql)
        cnx.commit()
        return True
    except:
        cnx.rollback()
    finally:
        cnx.close()
    return False

"""
查询语句
成功返回 查询结果
失败返回None
"""


def selectSQL(sql):
    cnx = mysql.connect(user=config.USER, password=config.PASSEORD, host=config.HOST, database=config.DATABASE)
    try:
        cursor = cnx.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except:
        cnx.close()
    return None


def executeSQL(sql, param=()):
    """
    执行数据库的插入 删除  修改操作
    :param sql: 数据库语句
    :param param: 所需要的参数，不需要参数时为空
    :return: 执行成功与否
    """
    cnx = mysql.connect(user=config.USER, password=config.PASSEORD, host=config.HOST, database=config.DATABASE)
    try:
        cur = cnx.cursor()
        print(sql)
        print(param)
        cur.execute(sql, param)
        cnx.commit()
        return True
    except:
        cnx.rollback()
        return False
    finally:
        cnx.close()


def tagTableAdd(model):
    # select_sql = "SELECT * FROM tagtable WHERE TAG = '%s'"
    print(model.tag)
    result = selectSQL("SELECT * FROM tagtable WHERE TAG = '%s'" % (model.tag,))
    if len(result) != 0:
        return False
    insert_sql = 'INSERT INTO tagtable(CATEGROY, TAG, TAGDES, TITLE, IMAGEPATH) VALUES (%s, %s, %s, %s, %s)'
    param = list()
    param.append(model.categroy)
    param.append(model.tag)
    param.append(model.tagdes)
    param.append(model.title)
    param.append(model.imagepath)
    params = tuple(param)
    isSuccess = executeSQL(sql=insert_sql, param=params)
    return isSuccess


def groupIdTableAdd(model):
    sql_insert = 'INSERT INTO groupidtable VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    result = selectSQL("SELECT * FROM groupidtable where GROUPID ='%s' and PATH ='%s' %(model.groupid,model.path)")
    if result != None and len(result) > 0:
        return False
    param = list()
    param.append(model.groupid)
    param.append(model.headerimagepath)
    param.append(model.photodes)
    param.append(model.createtime)
    param.append(model.size)
    param.append(model.path)
    param.append(model.saveimagepath)
    param.append(model.userid)
    param.append(model.status)
    params = tuple(param)
    isSuccess = executeSQL(sql=sql_insert, param=params)
    return isSuccess



