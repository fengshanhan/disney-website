#!/usr/bin/env python3
#coding=utf-8

import pymysql
import  hashlib

class StopCommand():
    #读取Stop信息传回界面
    def readStop(self):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "dbwebsite")
        cursor = db.cursor()
        sql = """SELECT * FROM busStop"""
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
        except:
            import traceback
            traceback.print_exc()
            print("error")

        cursor.close()
        return results

    #更改或增加bus信息
    def modifyStop(self,stID,bno,stName,Time1,Time2,Time3,Time4):
        # open database
        db = pymysql.connect("localhost", "root", "rewq66505441-", "dbwebsite")
        cursor = db.cursor()
        sql = """SELECT * FROM busStop WHERE stID = '%s'"""%(stID)
        try:
            self.cursor.execute(sql)
            results=cursor.fetchall()
            if(results == None):
                sql = """INSERT INTO busStop(stID,bno,stName,Time1,Time2,Time3,Time4) VALUES ('%s','%s','%s','%s','%s','%s','%s')"""%(stID,bno,stName,Time1,Time2,Time3,Time4)
                cursor.execute(sql)
            else:
                sql = """UPDATE busStop SET bno='%s',stName='%s',Time1='%s',Time2='%s',Time3='%s',Time4='%s WHERE stID='%s'""" % (bno,stName,Time1,Time2,Time3,Time4,stID)
                cursor.execute(sql)
            print("成功")
            db.commit()
            return 1
        except:
            print("不能")
            db.rollback()

        cursor.close()
        return results