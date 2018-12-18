#!/usr/bin/env python3
#coding=utf-8

import pymysql
import  hashlib


class ActivityCommand():
    #读取activity booking的信息传回界面
    def readActivityBook(self,vno):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "database")
        cursor = db.cursor()
        sql = """SELECT * FROM activityBooking WHERE vno='%s'""" % (vno)
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
        except:
            import traceback
            traceback.print_exc()
            print("error")

        cursor.close()
        return results


    #读取activity信息传回界面
    def readActivity(self):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "database")
        cursor = db.cursor()
        sql="""SELECT * FROM ACTIVITY"""

        try:
            cursor.execute(sql)
            results=cursor.fetchall()
        except:
            import traceback
            traceback.print_exc()
            print("error")

        cursor.close()
        return results

    #读取特定的活动信息传回界面
    def readActivity_ww(self,activity):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "database")
        cursor = db.cursor()
        sql="""SELECT ANAME,TNUM,ALENGTH FROM ACTIVITY WHERE ANAME='%s'"""%(activity)
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
        except:
            import traceback
            traceback.print_exc()
            print("error")

        cursor.close()
        return results

    # 读取特定的活动信息传回界面
    def readComment(self, activity):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "database")
        cursor = db.cursor()
        sql = """SELECT REVIEW FROM ACTIVITYBOOKING WHERE ANAME='%s'""" % (activity)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
        except:
            import traceback
            traceback.print_exc()
            print("error")

        cursor.close()
        return results


    #更改或增加activity信息
    def modifyActivity(self,aname,aDescription,tnum,isVIP,aLength,stime,etime):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "database")
        cursor = db.cursor()
        sql = """SELECT * FROM ACTIVITY WHERE aname = '%s'"""%(aname)
        try:
            self.cursor.execute(sql)
            results=cursor.fetchall()
            if(results == None):
                sql = """INSERT INTO ACTIVITY(ANAME,aDescription,TNUM,isVIP,aLength,STIME,ETIME) VALUES ('%s','%s','%d','%c','%s','%s','%s')"""%(aname,aDescription,int(tnum),isVIP,aLength,stime,etime)
                cursor.execute(sql)
            else:
                sql = """UPDATE ACTIVITY SET aDescription='%s',TNUM='%s',isVIP='%d',aLength='%s',STIME='%s',ETIME='%s' WHERE ANAME='%s'""" % (aDescription, int(tnum), isVIP,aLength, stime, etime, aname)
                cursor.execute(sql)
            print("成功")
            db.commit()
            return 1
        except:
            print("不能")
            db.rollback()

        cursor.close()
        return results

    #删除activity信息
    def deleteActivity(self,aname):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "database")
        cursor = db.cursor()
        sql = """DELETE from ACTIVITY where aname = '%s'""" % (aname)
        try:
            self.cursor.execute(sql)
            results=cursor.fetchall()
            sql = """DELETE from ACTIVITY where aname = '%s'"""%(aname)

            cursor.execute(sql)
            print("成功")
            db.commit()
            return 1
        except:
            print("不能")
            db.rollback()

        cursor.close()
        return results
